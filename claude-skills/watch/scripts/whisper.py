#!/usr/bin/env python3
"""Transcribe a video via Groq, Replicate, or OpenAI Whisper API.

Strategy: extract audio (mono 16kHz mp3, tiny payload), upload to whichever
API has a key. Returns segments in the same shape as transcribe.parse_vtt so
the rest of the pipeline (filter_range, format_transcript) doesn't care where
the transcript came from.

Pure stdlib — no `pip install groq` or `pip install openai` needed.
"""
from __future__ import annotations

import base64
import io
import json
import math
import mimetypes
import os
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import uuid
from pathlib import Path
from urllib.request import Request, urlopen


GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3"

OPENAI_ENDPOINT = "https://api.openai.com/v1/audio/transcriptions"
OPENAI_MODEL = "whisper-1"

REPLICATE_MODEL_URL = "https://api.replicate.com/v1/models/openai/whisper"
REPLICATE_PREDICTIONS_URL = "https://api.replicate.com/v1/predictions"

# _poll_replicate() gives up after 6 minutes regardless of whether the
# prediction would eventually finish. Long videos (~15+ min) can exceed that
# processing time, so Replicate audio is split into chunks safely under the
# cap and transcribed one at a time instead of as a single call.
REPLICATE_CHUNK_SECONDS = 330


def load_api_key(preferred: str | None = None) -> tuple[str, str] | tuple[None, None]:
    """Return (backend, api_key). Prefers Groq, falls back to OpenAI.

    If `preferred` is "groq" or "openai", only that backend's key is considered.
    """
    def _from_env(name: str) -> str | None:
        value = os.environ.get(name)
        return value.strip() if value else None

    def _from_dotenv(path: Path, name: str) -> str | None:
        if not path.exists():
            return None
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                if key.strip() != name:
                    continue
                value = value.strip()
                if len(value) >= 2 and value[0] in ('"', "'") and value[-1] == value[0]:
                    value = value[1:-1]
                return value or None
        except OSError:
            return None
        return None

    dotenv_paths = [
        Path.home() / ".config" / "watch" / ".env",
        Path.cwd() / ".env",
    ]

    candidates = (
        ("GROQ_API_KEY", "groq"),
        ("REPLICATE_API_TOKEN", "replicate"),
        ("OPENAI_API_KEY", "openai"),
    )
    if preferred is not None:
        candidates = tuple(c for c in candidates if c[1] == preferred)

    for key_name, backend in candidates:
        value = _from_env(key_name)
        if not value:
            for candidate in dotenv_paths:
                value = _from_dotenv(candidate, key_name)
                if value:
                    break
        if value:
            return backend, value

    return None, None


def extract_audio(video_path: str, out_path: Path) -> Path:
    """Extract mono 16kHz 64kbps mp3 — ~480 kB/min, fits any Whisper limit."""
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg is not installed. Install with: brew install ffmpeg")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-y",
        "-i", str(Path(video_path).resolve()),
        "-vn",
        "-acodec", "libmp3lame",
        "-ar", "16000",
        "-ac", "1",
        "-b:a", "64k",
        str(out_path.resolve()),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg audio extraction failed: {result.stderr.strip()}")
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise SystemExit("ffmpeg produced no audio — video may have no audio track")
    return out_path


def _build_multipart(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    """Assemble a multipart/form-data body the Whisper APIs accept.

    Whisper's multipart upload is small and predictable — doing it by hand
    keeps us on pure stdlib instead of pulling requests/groq/openai SDKs.
    """
    boundary = f"----WatchBoundary{uuid.uuid4().hex}"
    eol = b"\r\n"
    buf = io.BytesIO()

    for name, value in fields.items():
        buf.write(f"--{boundary}".encode()); buf.write(eol)
        buf.write(f'Content-Disposition: form-data; name="{name}"'.encode()); buf.write(eol)
        buf.write(eol)
        buf.write(str(value).encode()); buf.write(eol)

    mimetype = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    buf.write(f"--{boundary}".encode()); buf.write(eol)
    buf.write(
        f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"'.encode()
    )
    buf.write(eol)
    buf.write(f"Content-Type: {mimetype}".encode()); buf.write(eol)
    buf.write(eol)
    buf.write(file_path.read_bytes())
    buf.write(eol)
    buf.write(f"--{boundary}--".encode()); buf.write(eol)

    return buf.getvalue(), boundary


MAX_ATTEMPTS = 4       # initial + 3 retries
MAX_429_RETRIES = 2
RETRY_BASE_DELAY = 2.0


def _post_whisper(endpoint: str, api_key: str, model: str, audio_path: Path) -> dict:
    fields = {
        "model": model,
        "response_format": "verbose_json",
        "temperature": "0",
    }
    body, boundary = _build_multipart(fields, audio_path)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        # Groq sits behind Cloudflare — the default `Python-urllib/3.x` UA
        # trips WAF rule 1010 (403) before auth even runs. Any non-default
        # UA clears it; we identify honestly.
        "User-Agent": "watch-skill/1.0 (+claude-code; python-urllib)",
    }

    context = ssl.create_default_context()
    rate_limit_hits = 0
    last_exc: Exception | None = None
    last_detail = ""

    for attempt in range(MAX_ATTEMPTS):
        request = Request(endpoint, data=body, headers=headers, method="POST")
        try:
            with urlopen(request, timeout=300, context=context) as response:
                payload = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            detail = _read_error_body(exc)
            last_exc, last_detail = exc, detail

            # 4xx other than 429 are client errors — no retry will fix them.
            if 400 <= exc.code < 500 and exc.code != 429:
                raise SystemExit(f"Whisper request failed: {exc}{detail}")

            if exc.code == 429:
                rate_limit_hits += 1
                if rate_limit_hits >= MAX_429_RETRIES:
                    raise SystemExit(f"Whisper request failed: {exc}{detail}")
                delay = _retry_after(exc) or RETRY_BASE_DELAY * (2 ** attempt) + 1
            else:
                delay = RETRY_BASE_DELAY * (2 ** attempt)

            if attempt < MAX_ATTEMPTS - 1:
                print(
                    f"[watch] whisper HTTP {exc.code} — retrying in {delay:.1f}s "
                    f"(attempt {attempt + 2}/{MAX_ATTEMPTS})",
                    file=sys.stderr,
                )
                time.sleep(delay)
            continue
        except (urllib.error.URLError, TimeoutError, ConnectionResetError, OSError) as exc:
            last_exc, last_detail = exc, ""
            if attempt < MAX_ATTEMPTS - 1:
                delay = RETRY_BASE_DELAY * (attempt + 1)
                print(
                    f"[watch] whisper network error ({type(exc).__name__}: {exc}) — "
                    f"retrying in {delay:.1f}s (attempt {attempt + 2}/{MAX_ATTEMPTS})",
                    file=sys.stderr,
                )
                time.sleep(delay)
            continue

        try:
            return json.loads(payload)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Whisper returned non-JSON response: {exc}: {payload[:200]}")

    raise SystemExit(
        f"Whisper request failed after {MAX_ATTEMPTS} attempts: {last_exc}{last_detail}"
    )


def _read_error_body(exc: urllib.error.HTTPError) -> str:
    try:
        body = exc.read()
    except Exception:
        return ""
    if not body:
        return ""
    try:
        return f" — {body.decode('utf-8', errors='replace')[:400]}"
    except Exception:
        return ""


def _retry_after(exc: urllib.error.HTTPError) -> float | None:
    header = exc.headers.get("Retry-After") if getattr(exc, "headers", None) else None
    if not header:
        return None
    try:
        return float(header)
    except ValueError:
        return None


def _segments_from_response(data: dict) -> list[dict]:
    """Convert Whisper verbose_json into our {start, end, text} segment format."""
    out: list[dict] = []
    for seg in data.get("segments") or []:
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        out.append({
            "start": round(float(seg.get("start") or 0.0), 2),
            "end": round(float(seg.get("end") or 0.0), 2),
            "text": text,
        })

    if not out:
        full = (data.get("text") or "").strip()
        if full:
            out.append({"start": 0.0, "end": 0.0, "text": full})

    return out


def _replicate_get_version(api_key: str, context: ssl.SSLContext) -> str:
    """Fetch the latest openai/whisper version ID from Replicate."""
    headers = {
        "Authorization": f"Token {api_key}",
        "User-Agent": "watch-skill/1.0 (+claude-code; python-urllib)",
    }
    req = Request(REPLICATE_MODEL_URL, headers=headers)
    try:
        with urlopen(req, timeout=30, context=context) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = _read_error_body(exc)
        raise SystemExit(f"Replicate model lookup failed: {exc}{detail}")
    version_id = (data.get("latest_version") or {}).get("id")
    if not version_id:
        raise SystemExit("Could not determine latest Replicate whisper version")
    return version_id


def _poll_replicate(api_key: str, prediction_id: str, context: ssl.SSLContext) -> dict:
    """Poll a Replicate prediction until it reaches a terminal state."""
    poll_url = f"{REPLICATE_PREDICTIONS_URL}/{prediction_id}"
    headers = {
        "Authorization": f"Token {api_key}",
        "User-Agent": "watch-skill/1.0 (+claude-code; python-urllib)",
    }
    for _ in range(72):  # up to 6 minutes (72 × 5 s)
        time.sleep(5)
        req = Request(poll_url, headers=headers)
        try:
            with urlopen(req, timeout=30, context=context) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"[watch] replicate poll error ({type(exc).__name__}) — retrying…", file=sys.stderr)
            continue
        status = data.get("status")
        if status in ("succeeded", "failed", "canceled"):
            return data
        print(f"[watch] replicate: {status}…", file=sys.stderr)
    raise SystemExit("Replicate prediction timed out after 6 minutes")


def _replicate_whisper(api_key: str, audio_path: Path) -> dict:
    """Transcribe audio via Replicate openai/whisper. Returns verbose-JSON-compatible dict."""
    context = ssl.create_default_context()
    version_id = _replicate_get_version(api_key, context)
    print(f"[watch] replicate whisper version: {version_id[:12]}…", file=sys.stderr)

    audio_bytes = audio_path.read_bytes()
    b64 = base64.b64encode(audio_bytes).decode("ascii")
    mime = mimetypes.guess_type(audio_path.name)[0] or "audio/mpeg"

    body = json.dumps({
        "version": version_id,
        "input": {
            "audio": f"data:{mime};base64,{b64}",
            "model": "large-v3",
            "language": "auto",
        }
    }).encode("utf-8")

    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json",
        "Prefer": "wait=60",
        "User-Agent": "watch-skill/1.0 (+claude-code; python-urllib)",
    }
    req = Request(REPLICATE_PREDICTIONS_URL, data=body, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=120, context=context) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = _read_error_body(exc)
        raise SystemExit(f"Replicate request failed: {exc}{detail}")

    if data.get("status") not in ("succeeded", "failed", "canceled"):
        prediction_id = data.get("id")
        if not prediction_id:
            raise SystemExit(f"Replicate returned no prediction id: {data}")
        data = _poll_replicate(api_key, prediction_id, context)

    if data.get("status") != "succeeded":
        error = data.get("error") or "unknown error"
        raise SystemExit(f"Replicate prediction failed: {error}")

    output = data.get("output")
    if not output:
        raise SystemExit("Replicate returned empty output")
    # output is a dict with `segments`, `transcription`, `detected_language`
    return output if isinstance(output, dict) else {"text": str(output)}


def _probe_duration(path: Path) -> float:
    """Return media duration in seconds via ffprobe."""
    if shutil.which("ffprobe") is None:
        raise SystemExit("ffprobe is not installed. Install with: brew install ffmpeg")
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout.strip():
        raise SystemExit(f"ffprobe failed to read duration: {result.stderr.strip()}")
    return float(result.stdout.strip())


def _cut_audio_chunk(audio_path: Path, start: float, length: float, chunk_path: Path) -> None:
    """Stream-copy a slice of `audio_path` into `chunk_path` — no re-encoding."""
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-ss", str(start), "-i", str(audio_path),
        "-t", str(length), "-c", "copy", str(chunk_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg audio chunking failed: {result.stderr.strip()}")


def _replicate_whisper_chunked(api_key: str, audio_path: Path) -> list[dict]:
    """Transcribe audio via Replicate, splitting long audio into chunks so no
    single prediction risks _poll_replicate()'s fixed 6-minute cap.
    """
    duration = _probe_duration(audio_path)
    if duration <= REPLICATE_CHUNK_SECONDS:
        return _segments_from_response(_replicate_whisper(api_key, audio_path))

    chunk_count = math.ceil(duration / REPLICATE_CHUNK_SECONDS)
    print(
        f"[watch] audio is {duration:.0f}s — splitting into {chunk_count} chunks of "
        f"~{REPLICATE_CHUNK_SECONDS}s so Replicate doesn't hit its 6-minute cap…",
        file=sys.stderr,
    )

    all_segments: list[dict] = []
    start = 0.0
    idx = 0
    while start < duration:
        chunk_len = min(REPLICATE_CHUNK_SECONDS, duration - start)
        chunk_path = audio_path.with_name(f"{audio_path.stem}.chunk{idx:02d}{audio_path.suffix}")
        _cut_audio_chunk(audio_path, start, chunk_len, chunk_path)

        print(
            f"[watch] replicate chunk {idx + 1}/{chunk_count} "
            f"({start:.0f}s–{start + chunk_len:.0f}s)…",
            file=sys.stderr,
        )
        try:
            response = _replicate_whisper(api_key, chunk_path)
            for seg in _segments_from_response(response):
                all_segments.append({
                    "start": round(seg["start"] + start, 2),
                    "end": round(seg["end"] + start, 2),
                    "text": seg["text"],
                })
        finally:
            chunk_path.unlink(missing_ok=True)

        start += chunk_len
        idx += 1

    return all_segments


def transcribe_video(
    video_path: str,
    audio_out: Path,
    backend: str | None = None,
    api_key: str | None = None,
) -> tuple[list[dict], str]:
    """Run the full flow: extract audio → upload → parse segments.

    Returns (segments, backend_used). Raises SystemExit on any failure.
    """
    if backend is None or api_key is None:
        detected_backend, detected_key = load_api_key()
        backend = backend or detected_backend
        api_key = api_key or detected_key

    if not backend or not api_key:
        setup_py = Path(__file__).resolve().parent / "setup.py"
        raise SystemExit(
            "No Whisper API key available. Set GROQ_API_KEY (preferred) or OPENAI_API_KEY "
            "in the environment or in ~/.config/watch/.env. "
            f"Run `python3 {setup_py}` to configure."
        )

    print(f"[watch] extracting audio for Whisper ({backend})…", file=sys.stderr)
    audio_path = extract_audio(video_path, audio_out)
    size_kb = audio_path.stat().st_size / 1024
    print(f"[watch] audio: {size_kb:.0f} kB — uploading to {backend} Whisper…", file=sys.stderr)

    if backend == "groq":
        response = _post_whisper(GROQ_ENDPOINT, api_key, GROQ_MODEL, audio_path)
        segments = _segments_from_response(response)
    elif backend == "openai":
        response = _post_whisper(OPENAI_ENDPOINT, api_key, OPENAI_MODEL, audio_path)
        segments = _segments_from_response(response)
    elif backend == "replicate":
        segments = _replicate_whisper_chunked(api_key, audio_path)
    else:
        raise SystemExit(f"Unknown whisper backend: {backend}")

    if not segments:
        raise SystemExit("Whisper returned no transcript segments")

    print(f"[watch] transcribed {len(segments)} segments via {backend}", file=sys.stderr)
    return segments, backend


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: whisper.py <video-path> [<audio-out.mp3>] [--backend groq|replicate|openai]", file=sys.stderr)
        raise SystemExit(2)

    video = sys.argv[1]
    audio_out = Path(sys.argv[2]) if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else Path("audio.mp3")
    backend_override = None
    if "--backend" in sys.argv:
        backend_override = sys.argv[sys.argv.index("--backend") + 1]

    segments, backend = transcribe_video(video, audio_out, backend=backend_override)
    print(json.dumps({"backend": backend, "segments": segments}, indent=2))
