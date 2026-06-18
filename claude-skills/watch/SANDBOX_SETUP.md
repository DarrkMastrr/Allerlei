# /watch auf der Sandbox einrichten

Dieser Ordner ist eine Kopie von `~/.claude/skills/watch` (Stand-PC), inklusive lokaler
Patches die noch nicht ins Upstream-Repo (`bradautomates/claude-video`) gepusht sind.
Ziel: gleicher Stand auf der Sandbox, damit Claude Code dort `/watch` versteht.

## Installation

1. Repo auf der Sandbox pullen/clonen.
2. Diesen Ordner nach `~/.claude/skills/watch` kopieren (oder den ganzen Ordner dorthin verschieben).
3. `.env`-Datei **manuell** anlegen (wird absichtlich nicht mitversioniert):

   ```text
   ~/.config/watch/.env
   ```

   Inhalt (mind. einen Key setzen):

   ```text
   GROQ_API_KEY=
   REPLICATE_API_TOKEN=
   OPENAI_API_KEY=
   ```

4. Voraussetzungen prüfen/installieren: `ffmpeg`, `ffprobe`, `yt-dlp`.

   - Windows: `winget install Gyan.FFmpeg` und `winget install yt-dlp.yt-dlp` (oder `pip install --user yt-dlp`).
   - `setup.py` zeigt fehlende Binaries automatisch an, installiert sie auf Windows aber nicht selbst (nur macOS/Homebrew macht das automatisch).

5. Check:

   ```bash
   python "${CLAUDE_SKILL_DIR}/scripts/setup.py" --check
   ```

   (Windows: **`python`**, nicht `python3` — `python3` ist auf Windows der Microsoft-Store-Stub und startet das Skript nicht.)

## Lokale Änderungen gegenüber Upstream

Replicate als dritter Whisper-Fallback (`scripts/setup.py`, `scripts/watch.py`, `scripts/whisper.py`):

- Priorität: Groq > Replicate > OpenAI (erster gefundener Key gewinnt, override mit `--whisper groq|replicate|openai`).
- Replicate nutzt `openai/whisper` (large-v3) über die Predictions-API, inkl. Polling bis `succeeded/failed/canceled` (Timeout 6 Min).
- Env-Var: `REPLICATE_API_TOKEN` (Token von `replicate.com/account/api-tokens`).
- Diese Änderungen sind noch nicht als PR an `bradautomates/claude-video` gegangen — sie existieren nur hier und auf dem Stand-PC.

## Bekannte Probleme bei der Windows-Einrichtung

- **`python3` startet nichts**: auf Windows immer `python` verwenden, nie `python3`.
- **Encoding-Bugs (bereits upstream gefixt, v0.1.3)**: `.env` und `video.info.json` müssen explizit als UTF-8 gelesen/geschrieben werden — `Path.read_text()` ohne Encoding nutzt unter Windows cp1252 und crasht/verschluckt Daten bei yt-dlps UTF-8-Output.
- **Emoji-Crash (gefixt, v0.1.2)**: cp1252-Konsolen konnten ein Emoji in der Lang-Video-Warnung nicht ausgeben — wurde entfernt.
- **`.env`-Berechtigungen 600 lassen sich unter Windows nicht zuverlässig setzen**: `setup.py` ruft `CONFIG_FILE.chmod(0o600)` auf, aber `os.chmod` unter Windows bildet POSIX-Modes nicht echt ab (steuert im Wesentlichen nur das Read-Only-Attribut). Ergebnis: die Datei landet trotzdem oft mit offeneren Rechten (z. B. 644), und der `/watch`-SessionStart-Hook meldet das bei jedem Start als Warnung. Auf einem Single-User-Windows-Rechner ist das praktisch unkritisch, lässt sich aber nicht durch das Skript selbst beheben — Hinweis ignorieren oder Rechte manuell über `icacls` einschränken; `chmod 600` (Git Bash) behebt die Meldung nicht dauerhaft, weil sie bei jedem Neuanlegen der Datei wiederkommen kann.
- **Plugin-Erkennung**: der Skill wird nicht über `/plugin marketplace add` registriert, sondern einfach dadurch, dass der Ordner mit `SKILL.md` unter `~/.claude/skills/` liegt (Quelle erscheint intern als `watch@skills-dir`). Kein zusätzlicher Registrierungsschritt nötig — Ordner an die richtige Stelle kopieren reicht.

## Danach

```bash
python "${CLAUDE_SKILL_DIR}/scripts/setup.py" --check
```

sollte exit 0 liefern (kein Output). Falls Exit 3 (kein Whisper-Key): Key in `~/.config/watch/.env` eintragen, fertig.
