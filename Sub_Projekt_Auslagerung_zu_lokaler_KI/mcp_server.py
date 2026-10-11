"""
Lokaler MCP-Server: Whisper-Transkription, Claim-Extraktion, Frame-Beschreibung.
Läuft als stdio-Server, wird von Claude Code per settings.json eingebunden.
"""

import base64
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-ki")

_whisper_model = None


def _get_whisper():
    global _whisper_model
    if _whisper_model is None:
        from faster_whisper import WhisperModel
        _whisper_model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    return _whisper_model


@mcp.tool()
def transkript_erstellen(audio_pfad: str) -> str:
    """
    Transkribiert eine Audiodatei lokal mit Whisper large-v3 auf der GPU.
    Gibt den deutschen Volltext zurück (kein Zeitstempel, kein JSON).
    audio_pfad: absoluter Pfad zur .mp3 oder .wav Datei
    """
    model = _get_whisper()
    segments, _ = model.transcribe(audio_pfad, language="de", beam_size=5)
    return " ".join(s.text.strip() for s in segments)


@mcp.tool()
def claims_extrahieren(text: str) -> str:
    """
    Extrahiert prüfbare Tatsachenbehauptungen aus einem Transkript-Chunk via qwen3:14b.
    Gibt JSON zurück: {"claims":[{"claim":"...","zitat":"..."}]}
    text: Transkript-Abschnitt (ca. 5-10 Minuten Sprechzeit)
    """
    prompt = (
        "Extrahiere aus dem folgenden Transkript-Abschnitt alle überprüfbaren Tatsachenbehauptungen "
        "(Zahlen, Namen, Daten, technische Aussagen). Meinungen und Füllwörter ignorieren. "
        'Antworte nur als JSON in dieser Form: {"claims":[{"claim":"...","zitat":"wörtliche Stelle aus dem Text"}]}\n\n'
        f"TRANSKRIPT:\n{text}"
    )
    body = {
        "model": "qwen3:14b",
        "prompt": prompt,
        "stream": False,
        "think": False,
        "format": "json",
        "options": {"num_ctx": 16384, "temperature": 0},
    }
    r = httpx.post("http://localhost:11434/api/generate", json=body, timeout=300)
    r.raise_for_status()
    return r.json()["response"]


@mcp.tool()
def frame_beschreiben(bild_pfad: str) -> str:
    """
    Beschreibt einen Video-Frame auf Deutsch via qwen2.5vl:7b (lokal, kein Cloud-Token).
    Gibt Fließtext zurück: sichtbarer Inhalt, lesbarer Text, Kontext.
    bild_pfad: absoluter Pfad zur .jpg oder .png Datei
    """
    with open(bild_pfad, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    body = {
        "model": "qwen2.5vl:7b",
        "prompt": "Beschreibe diesen Video-Frame auf Deutsch. Was ist zu sehen? Welcher Text ist lesbar? Worum geht es?",
        "images": [b64],
        "stream": False,
        "options": {"temperature": 0},
    }
    r = httpx.post("http://localhost:11434/api/generate", json=body, timeout=120)
    r.raise_for_status()
    return r.json()["response"]


if __name__ == "__main__":
    mcp.run()
