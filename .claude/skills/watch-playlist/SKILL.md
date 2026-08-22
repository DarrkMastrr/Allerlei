---
name: watch-playlist
description: Arbeitet eine YouTube-Playlist (Standard "KI News", https://www.youtube.com/playlist?list=PLKmOsK7sxhDQ) komplett ab — findet noch nicht zusammengefasste Videos, sieht sie per `/watch`-Skill über parallele Subagents an, prüft Plausibilität, gleicht gegen bestehende Notizen ab und legt für jedes neue Video eine Datei in video-summaries/ an. Nutzen bei "Playlist abarbeiten", "KI News durchgehen", "neue Videos ansehen" oder ähnlichem.
allowed-tools: Bash, Glob, Grep, Read, Agent, SendMessage, TodoWrite
argument-hint: "[playlist-url]"
user-invocable: true
---

# /watch-playlist — Playlist komplett abarbeiten

Kontext: Statt Video-URLs einzeln einzufügen, pflegt der Nutzer eine unlisted YouTube-Playlist als Inbox (Standard: "KI News", `https://www.youtube.com/playlist?list=PLKmOsK7sxhDQ` — per Argument überschreibbar). `video-summaries/video-summary-<VIDEO_ID>.md` ist die "gesehen"-Liste; die Playlist selbst muss nie geleert werden (kein Schreib-/Lösch-Zugriff auf YouTube-Playlists vorhanden, und unnötig — die Dedup-Prüfung in Schritt 2 macht bereits gesehene Videos automatisch harmlos).

## Schritt 1 — Playlist lesen

`WebFetch` funktioniert NICHT für Playlist-Seiten (Videoliste wird clientseitig per JS gerendert). Stattdessen:

```bash
yt-dlp --flat-playlist -J "<playlist-url>"
```

Liefert JSON mit `entries[]`, je Eintrag `id`, `title`, `duration` (Sekunden).

## Schritt 2 — Unbekannte Videos ermitteln

```
Glob: video-summaries/video-summary-*.md
```

IDs aus den Dateinamen extrahieren, gegen die Playlist-IDs abgleichen. Videos, für die bereits eine Datei existiert, überspringen. Wenn nichts Neues übrig ist: das dem Nutzer kurz melden und aufhören — kein Grund, weiterzumachen.

## Schritt 3 — Reihenfolge festlegen

Kürzere Videos zuerst (schnelle Fehlererkennung, falls beim Vorgehen etwas nicht passt), sehr lange Videos (>40 Min) zuletzt und mit weniger Parallelität. `TodoWrite` mit einem Eintrag pro unbekanntem Video anlegen.

Manche Playlist-Einträge sind nicht abrufbar (`title`/`duration` = `null` im flat-playlist-JSON, meist "Private video" oder "Please sign in" bei einzelnem `yt-dlp -J <url>`-Aufruf zur Bestätigung). Diese aus der Liste streichen, dem Nutzer kurz melden, nicht versuchen zu erzwingen.

### Kontingent-Hinweis (Pro-Abo)

Der Nutzer hat ein Claude-Pro-Abo mit begrenztem Nutzungsfenster — **nicht** automatisch versuchen, eine große Zahl neuer Videos (mehr als ~5-6) in einer einzigen Session komplett abzuarbeiten. Bei einem größeren Rückstand:

- Kurz die Gesamtzahl neuer (abrufbarer) Videos nennen und den Nutzer fragen, wie groß die Batch-Größe für diese Session sein soll (z.B. per `AskUserQuestion`), statt stillschweigend alles zu starten.
- Nach der vereinbarten Batch-Größe anhalten, Abschlussbericht liefern (Schritt 7) und explizit erwähnen, wie viele Videos noch offen sind — der Skill lässt sich beim nächsten Mal einfach erneut aufrufen (Schritt 2 filtert automatisch nur die noch fehlenden heraus, siehe „Hinweis zur Wiederholung" unten).
- Kein Grund zur Sorge bei kleinen Nachträgen (1-4 neue Videos) — die können normal in einer Welle durchlaufen.

## Schritt 4 — Subagents in Wellen zu je ~3 dispatchen

Nicht alle Videos auf einmal starten — 3 parallele Hintergrund-Agents (`Agent`-Tool, `subagent_type: general-purpose`, `run_in_background: true`) sind ein guter Kompromiss zwischen Tempo und Belastung des lokalen Whisper/Replicate-Kontingents. Jeder Agent bekommt ein Video und folgenden Prompt (Platzhalter `{VIDEO_ID}`, `{VIDEO_URL}`, `{PLAYLIST_TITLE}`, `{DURATION}` ersetzen):

```
Repo: c:\Claude\Allerlei (git repo of German-language AI/tech notes built from YouTube videos, maintained by a hardware developer / technical team lead). Your job: watch ONE YouTube video with the project's `watch` skill and write a summary file matching this repo's established conventions.

VIDEO: {VIDEO_URL} — playlist title "{PLAYLIST_TITLE}", ~{DURATION} min.

## Step 1 — Watch it
Run (Windows, use `python` not `python3`). Don't hardcode a username — this repo is synced across multiple machines with different logged-in users, so resolve the home directory dynamically: in PowerShell use `$env:USERPROFILE`, in Git Bash use `~` or `$USERPROFILE`. E.g. PowerShell:
python "$env:USERPROFILE\.claude\skills\watch\scripts\watch.py" "{VIDEO_URL}"
or Git Bash:
python "$USERPROFILE/.claude/skills/watch/scripts/watch.py" "{VIDEO_URL}"
This downloads the video, extracts frames, and gets a transcript (native captions or Whisper fallback — the Whisper/Replicate backend already auto-chunks long audio into <330s pieces, so long videos won't time out; no need to intervene). Then Read every listed frame path (parallel Read calls) and read the transcript output. If native captions are missing and Whisper also fails, proceed frames-only and note that in the summary.

**IMPORTANT — do not end your turn while a background process is still running.** If you background the download/transcribe step, you must actively wait for it (poll it or use a blocking call) and continue in the SAME turn to read frames and write the file. You are a single agent process, not the orchestrator — nothing "notifies" you automatically the way it notifies the orchestrator. Ending your turn assuming a later turn will pick this back up leaves the task permanently incomplete. This matters especially for videos needing chunked Whisper transcription (roughly one chunk per 5-6 minutes of audio), which can take several minutes — just keep waiting.

**This is not a hypothetical warning — it happens routinely (observed in most agents of a 2026-08-22 batch), not just occasionally.** Any of these thoughts means you are about to fail the task: "I'll hold here and resume once the monitor reports," "standing by for X to complete," "I'll wait for the notification that Y finished." There is no monitor, no notification, and no later turn for you specifically — if you stop calling tools now, this task is permanently abandoned mid-way with no summary file ever written. The only correct move when transcription is still processing: immediately issue another blocking/polling tool call (e.g. re-check the process status, or sleep a short interval then check again) and keep doing that, in this same turn, until the watch script's `Work dir:` line actually appears in your own tool output — however many tool calls that takes.

## Step 2 — Write the summary file
Create c:\Claude\Allerlei\video-summaries\video-summary-{VIDEO_ID}.md. First read 2-3 existing files in that folder to match the exact structure/tone/German-language convention: `# "Title"` header, bullet metadata block (**Kanal:**, **URL:**, **Länge:**, **Zusammenfassung erstellt:** <today's date>), `---`, content sections in German with `##` headings covering what's actually said/shown, a `## Kernbotschaft` (1 paragraph), a `## Themen-Tags` line, and a `## Zu prüfen` section for anything uncertain/unverified. Write content in German regardless of the video's spoken language. Use the actual title/uploader from the script's metadata output.

## Step 3 — Plausibility check (be honest, don't fabricate)
Critically read the claims made. For strong/checkable factual claims, spot-check via WebSearch if something seems dubious or you're unsure, and note the outcome. Do NOT invent sources or verification you didn't actually do — if you didn't check something, say so plainly. If genuinely unsure and can't resolve something, say so explicitly in your final report rather than guessing. Treat sensational/clickbait titles with extra scrutiny — describe what's actually shown/claimed, not the hype framing.

## Step 4 — Cross-check against existing notes (do NOT edit other files)
Grep repo root *.md files and video-summaries/ for terms relevant to this video's themes to find contradictions or notable overlap with what's already documented. Do NOT edit any file other than the new one you're creating. Report contradictions/overlaps back to the orchestrator AND add a short cross-reference note inside your new file's "Zu prüfen" section.

## Step 5 — Value for the target reader
The reader is a hardware developer and technical/organizational team lead (Gruppenleiter). If this video contains anything specifically useful for that role, make sure it's clearly represented in the summary.

## Step 6 — Clean up
Delete the script's working/temp directory when done.

## Report back
Short (under 250 words): confirm the file was written, state the actual title/length found, list plausibility concerns and contradictions/overlaps found with existing notes, and list open questions for the user (don't guess).
```

## Schritt 5 — Nach jeder Fertigmeldung verifizieren, bevor der Todo als erledigt gilt

**Bekannter Fehlermodus (in ca. 3 von 17 Fällen aufgetreten):** Subagents lagern den `watch.py`-Aufruf manchmal in einen eigenen Hintergrundprozess aus und beenden dann ihren eigenen Turn in der Annahme, sie würden automatisch benachrichtigt — das gilt aber nur für den Orchestrator, nicht für Subagents selbst. Ergebnis: Die Task-Notification meldet `completed`, aber die Datei wurde nie geschrieben.

Deshalb **vor** jedem Abhaken im Todo prüfen:

```
Glob: video-summaries/video-summary-<VIDEO_ID>.md
```

Fehlt die Datei trotz `completed`-Meldung: **nicht** einen neuen Agent starten (verliert Kontext/Fortschritt), sondern per `SendMessage` an dieselbe Agent-ID eine Korrektur schicken (kurz erklären, dass die Datei fehlt, dass Hintergrundprozesse aktiv abgewartet werden müssen, und dass die Aufgabe jetzt in einem durchgehenden Turn zu Ende gebracht werden soll). Danach erneut auf die Fertigmeldung warten und wieder verifizieren.

## Schritt 6 — Wellen fortsetzen

Sobald ein Slot frei wird (Video verifiziert fertig), das nächste Video aus der Warteschlange starten — Konkurrenz bei ~3 halten, bis die Liste abgearbeitet ist.

## Schritt 7 — Abschlussbericht im Chat

Kein Roh-Dump aller Einzelberichte. Stattdessen kompakt zusammenfassen:
1. **Echte Widersprüche zu bestehenden Notizen zuerst**, falls welche gefunden wurden — klar benennen, aber NICHT selbst löschen/überschreiben ohne Zustimmung des Nutzers (nur meist veraltete Angaben markieren/korrigieren, bestehende Inhalte nicht kommentarlos entfernen).
2. Inhaltliche Lücken, die mehrfach auffielen (z.B. ein wiederkehrendes Thema ohne eigenen Übersichtsartikel) — anbieten, sie zu entwerfen, nicht ungefragt anlegen (gleiches Prinzip wie beim `notes-audit`-Skill).
3. Kurzer Hinweis, dass jede neue Datei ihren eigenen "Zu prüfen"-Abschnitt mit offenen Detailfragen hat — nicht einzeln auflisten, außer etwas ist wirklich blockierend.
4. Nichts automatisch committen/pushen — nur auf explizite Anfrage.

## Hinweis zur Wiederholung

Dieser Skill ist für einen erneuten Durchlauf gedacht, sobald der Nutzer neue Videos in die Playlist gelegt hat — einfach erneut aufrufen, Schritt 2 filtert automatisch nur die wirklich neuen Videos heraus.
