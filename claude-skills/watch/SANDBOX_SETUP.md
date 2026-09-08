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

Cookie-Support für yt-dlp (`scripts/download.py`), ergänzt 2026-09-07, überarbeitet 2026-09-08:

Nötig für Videos, die mit `LOGIN_REQUIRED`/"Sign in to confirm you're not a bot" blockieren — der PO-Token-Provider (siehe oben) reicht dafür nicht aus, siehe dortige Einschränkung.

**Aktuelle Lösung (primär): Firefox installieren, automatisch genutzt.** `download.py` hängt automatisch `--cookies-from-browser firefox` an den yt-dlp-Aufruf an, sobald ein Firefox-Profil auf der Maschine existiert (per `_has_firefox_profile()` erkannt — kein Setup-Schritt im Skript nötig). Voraussetzung einmalig pro Maschine:

1. `winget install --id Mozilla.Firefox --accept-package-agreements --accept-source-agreements`
2. Firefox einmal öffnen, bei YouTube/Google einloggen.
3. Fertig — kein manueller Cookie-Export mehr nötig, jeder `watch.py`-Aufruf liest die Live-Session direkt aus Firefox.

**Wichtig, auf dem Stand-PC ebenfalls einrichten** (dieser Fix wurde nur auf der Sandbox gebaut und getestet — Firefox muss dort separat installiert und eingeloggt werden, sonst greift der Fallback nicht und `LOGIN_REQUIRED`-Videos schlagen dort weiterhin fehl).

Warum Firefox statt Chrome/Edge: Firefox speichert Cookies unverschlüsselt in einer SQLite-Datei. `--cookies-from-browser edge/chrome` scheiterte auf der Sandbox zuverlässig an einem DPAPI-Entschlüsselungsfehler (neuere Edge/Chrome-App-Bound-Encryption), auch bei komplett geschlossenem Browser — kein Workaround gefunden außer dem Wechsel auf Firefox.

**Fallback (falls Firefox mal nicht verfügbar/eingeloggt ist):** Env-Var `WATCH_YTDLP_COOKIES` (Pfad zu einer `cookies.txt` im Netscape-Format) hat Vorrang vor dem Firefox-Fallback, falls gesetzt und die Datei existiert — wird dann als `--cookies <pfad>` an yt-dlp übergeben. Export z. B. via Browser-Extension "Get cookies.txt LOCALLY". Nutzung: `WATCH_YTDLP_COOKIES=/pfad/zu/cookies.txt python scripts/watch.py <url>` (Git Bash: `export` davor; PowerShell: `$env:WATCH_YTDLP_COOKIES = "..."`). Nachteil dieses Wegs: Die exportierten Session-Cookies liefen auf der Sandbox mehrfach innerhalb einer Session ab/wurden von YouTube als "rotiert" abgelehnt (vermutlich durch die vielen automatisierten Anfragen von einer IP getriggert) — musste mehrfach neu exportiert werden. Der Firefox-Live-Ansatz oben hat dieses Problem nicht, da er die aktuelle Session jedes Mal frisch liest.

Encoding-Fix für `scripts/watch.py` (Titel-Ausgabe), ergänzt 2026-09-07:

- `sys.stdout`/`sys.stderr` werden jetzt explizit auf UTF-8 (`errors="replace"`) umgestellt. Ohne das crashte das Skript beim Ausgeben von Titeln mit kombinierenden Umlaut-Zeichen (z. B. `Büro` als `u` + combining diaeresis) auf der cp1252-Windows-Konsole (`UnicodeEncodeError`), obwohl Download/Transkription bereits erfolgreich durchgelaufen waren.

## Bekannte Probleme bei der Windows-Einrichtung

- **`python3` startet nichts**: auf Windows immer `python` verwenden, nie `python3`.
- **Encoding-Bugs (bereits upstream gefixt, v0.1.3)**: `.env` und `video.info.json` müssen explizit als UTF-8 gelesen/geschrieben werden — `Path.read_text()` ohne Encoding nutzt unter Windows cp1252 und crasht/verschluckt Daten bei yt-dlps UTF-8-Output.
- **Emoji-Crash (gefixt, v0.1.2)**: cp1252-Konsolen konnten ein Emoji in der Lang-Video-Warnung nicht ausgeben — wurde entfernt.
- **`.env`-Berechtigungen 600 lassen sich unter Windows nicht zuverlässig setzen**: `setup.py` ruft `CONFIG_FILE.chmod(0o600)` auf, aber `os.chmod` unter Windows bildet POSIX-Modes nicht echt ab (steuert im Wesentlichen nur das Read-Only-Attribut). Ergebnis: die Datei landet trotzdem oft mit offeneren Rechten (z. B. 644), und der `/watch`-SessionStart-Hook meldet das bei jedem Start als Warnung. Auf einem Single-User-Windows-Rechner ist das praktisch unkritisch, lässt sich aber nicht durch das Skript selbst beheben — Hinweis ignorieren oder Rechte manuell über `icacls` einschränken; `chmod 600` (Git Bash) behebt die Meldung nicht dauerhaft, weil sie bei jedem Neuanlegen der Datei wiederkommen kann.
- **Plugin-Erkennung**: der Skill wird nicht über `/plugin marketplace add` registriert, sondern einfach dadurch, dass der Ordner mit `SKILL.md` unter `~/.claude/skills/` liegt (Quelle erscheint intern als `watch@skills-dir`). Kein zusätzlicher Registrierungsschritt nötig — Ordner an die richtige Stelle kopieren reicht.

## YouTube-Bot-Check ("Sign in to confirm you're not a bot")

Trat 2026-09-07 wiederholt auf: yt-dlp scheitert bei manchen Videos über alle Player-Clients hinweg (`playability status: LOGIN_REQUIRED`). Abhilfe (reduziert das Problem, behebt es aber nicht immer — siehe Einschränkung unten): der `bgutil-ytdlp-pot-provider` PO-Token-Plugin.

Einrichtung pro Maschine (nicht Teil dieses Repos, muss lokal installiert werden):

1. `python -m pip install -U bgutil-ytdlp-pot-provider`
2. `git clone https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git` nach `%USERPROFILE%\bgutil-ytdlp-pot-provider` (genau dieser Pfad — das Plugin sucht standardmäßig dort, sonst `--extractor-args "youtubepot-bgutilscript:server_home=..."` nötig)
3. `cd server && npm install && npx tsc` (braucht Node.js ≥ 22 im PATH)
4. Kein dauerhaft laufender Server nötig — das Plugin startet `node build/generate_once.js` pro yt-dlp-Aufruf selbst. Eine harmlose Warnung `[pot:bgutil:http] Error reaching GET http://127.0.0.1:4416/ping` erscheint deshalb bei jedem Lauf (kein HTTP-Server-Modus eingerichtet) — kann ignoriert werden.
5. Check: `yt-dlp -v --simulate <url>` sollte im Debug-Output `PO Token Providers: bgutil:http-..., bgutil:script-node-..., bgutil:script-deno-...` zeigen statt `none`.

**Wichtige Einschränkung (getestet, nicht nur vermutet):** Ein PO-Token hilft nur gegen weiche Bot-Erkennung. Bei zwei Videos blieb `LOGIN_REQUIRED` auch mit aktivem PO-Token-Provider über alle Player-Clients bestehen — per Kontrolltest bestätigt kein IP-weiter Block (ein anderes, bekanntes Video lief im selben Durchlauf problemlos). Diese Videos brauchen echte authentifizierte Cookies (`--cookies-from-browser` oder `--cookies`-Datei), kein PO-Token-Debugging mehr.

## Danach

```bash
python "${CLAUDE_SKILL_DIR}/scripts/setup.py" --check
```

sollte exit 0 liefern (kein Output). Falls Exit 3 (kein Whisper-Key): Key in `~/.config/watch/.env` eintragen, fertig.
