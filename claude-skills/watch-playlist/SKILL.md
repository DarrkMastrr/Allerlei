---
name: watch-playlist
description: Arbeitet eine YouTube-Playlist zu einem beliebigen Thema komplett ab — findet noch nicht zusammengefasste Videos, sieht sie per `/watch`-Skill über parallele Subagents an, prüft Plausibilität, gleicht gegen bestehende Notizen im aktuellen Projekt ab und legt für jedes neue Video eine Datei in video-summaries/ an. Themen-unabhängig (KI, Psychologie, Kochen, Geschichte, ...) — Playlist-URL und Themenkontext werden pro Aufruf übergeben oder erfragt. Nutzen bei "Playlist abarbeiten", "Videos zu Thema X durchgehen", "neue Videos ansehen" oder ähnlichem.
allowed-tools: Bash, Glob, Grep, Read, Agent, SendMessage, TodoWrite, AskUserQuestion
argument-hint: "[playlist-url] [thema/kontext]"
user-invocable: true
---

# /watch-playlist — Playlist komplett abarbeiten

Dieser Skill ist global installiert (`~/.claude/skills/`), projekt- und themen-unabhängig. Er verwendet immer das aktuelle Arbeitsverzeichnis (`{REPO_ROOT}` in den Beispielen unten) als Projekt, in dem `video-summaries/` liegt bzw. angelegt wird — egal ob dort KI-News, Kleinkind-Psychologie, Kochrezepte oder etwas ganz anderes gesammelt wird.

Kontext: Statt Video-URLs einzeln einzufügen, pflegt der Nutzer eine (meist unlisted) YouTube-Playlist als Inbox zu einem Thema. `video-summaries/video-summary-<VIDEO_ID>.md` ist die "gesehen"-Liste; die Playlist selbst muss nie geleert werden (kein Schreib-/Lösch-Zugriff auf YouTube-Playlists vorhanden, und unnötig — die Dedup-Prüfung in Schritt 2 macht bereits gesehene Videos automatisch harmlos).

## Schritt 0 — Kontext klären

Dieser Skill hat **keine** Standard-Playlist und **keine** feste Zielgruppe mehr — beides hängt vom jeweiligen Projekt/Thema ab. Vor Schritt 1 sicherstellen, dass Folgendes bekannt ist (aus dem Argument, dem bisherigen Gespräch, oder sonst per `AskUserQuestion` erfragen):

1. **Playlist-URL** — Pflicht, kein Default.
2. **Themenkontext in 1-2 Sätzen** — worum geht es (z. B. "Psychologie von Kleinkindern, Fokus auf Bindungsverhalten und Trotzphasen"), und für wen/mit welchem Blickwinkel die Zusammenfassungen gedacht sind (z. B. "Elternperspektive", "Fachpublikum", "Hardware-Entwickler und Team-Lead"). Dieser Kontext ersetzt eine hartcodierte Zielgruppen-Annahme und fließt in Schritt 4 (Step 5 des Subagent-Prompts) sowie in die Plausibilitätsprüfung ein.

Frage bei der Zielgruppe immer auch, ob die Leser Experten oder interessierte Laien sind; bei Laien gelten die Verständlichkeits-Vorgaben aus Step 2 des Subagent-Prompts.

Wenn im aktuellen Projekt bereits `video-summaries/*.md`-Dateien existieren, kurz eine Datei lesen, um Sprache/Struktur/Zielgruppe der bisherigen Zusammenfassungen zu übernehmen, statt erneut zu fragen.

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

Pro Video laufen ein Schreib-Agent und ein Prüf-Agent (Schritt 5b); der Kontingentbedarf ist damit etwa doppelt so hoch wie die Videozahl vermuten lässt — bei der Batch-Größe berücksichtigen.

Der Nutzer hat ein Claude-Pro-Abo mit begrenztem Nutzungsfenster — **nicht** automatisch versuchen, eine große Zahl neuer Videos (mehr als ~5-6) in einer einzigen Session komplett abzuarbeiten. Bei einem größeren Rückstand:

- Kurz die Gesamtzahl neuer (abrufbarer) Videos nennen und den Nutzer fragen, wie groß die Batch-Größe für diese Session sein soll (z.B. per `AskUserQuestion`), statt stillschweigend alles zu starten.
- Nach der vereinbarten Batch-Größe anhalten, Abschlussbericht liefern (Schritt 7) und explizit erwähnen, wie viele Videos noch offen sind — der Skill lässt sich beim nächsten Mal einfach erneut aufrufen (Schritt 2 filtert automatisch nur die noch fehlenden heraus, siehe „Hinweis zur Wiederholung" unten).
- Kein Grund zur Sorge bei kleinen Nachträgen (1-4 neue Videos) — die können normal in einer Welle durchlaufen.

## Schritt 4 — Subagents in Wellen zu je ~3 dispatchen

Nicht alle Videos auf einmal starten — 3 parallele Hintergrund-Agents (`Agent`-Tool, `subagent_type: general-purpose`, `run_in_background: true`) sind ein guter Kompromiss zwischen Tempo und Belastung des lokalen Whisper/Replicate-Kontingents. Jeder Agent bekommt ein Video und folgenden Prompt (Platzhalter `{REPO_ROOT}`, `{VIDEO_ID}`, `{VIDEO_URL}`, `{PLAYLIST_TITLE}`, `{DURATION}`, `{THEMENKONTEXT}`, `{ZIELGRUPPE}`, `{SPRACHE}` mit den in Schritt 0 geklärten Werten ersetzen):

```
Repo: {REPO_ROOT} (aktuelles Projektverzeichnis, hier die tatsächliche absolute Pfadangabe einsetzen — niemals eine feste Beispielangabe verwenden). Thema dieses Projekts: {THEMENKONTEXT}. Zielgruppe/Blickwinkel der Zusammenfassungen: {ZIELGRUPPE}. Your job: watch ONE YouTube video with the project's `watch` skill and write a summary file matching this project's established conventions.

VIDEO: {VIDEO_URL} — playlist title "{PLAYLIST_TITLE}", ~{DURATION} min.

## Step 1 — Watch it
Run (Windows, use `python` not `python3`). Don't hardcode a username — resolve the home directory dynamically: in PowerShell use `$env:USERPROFILE`, in Git Bash use `~` or `$USERPROFILE`. E.g. PowerShell:
python "$env:USERPROFILE\.claude\skills\watch\scripts\watch.py" "{VIDEO_URL}"
or Git Bash:
python "$USERPROFILE/.claude/skills/watch/scripts/watch.py" "{VIDEO_URL}"
This downloads the video, extracts frames, and gets a transcript (native captions first, Whisper/Replicate fallback if captions are missing/blocked).

**Known bug — the Whisper/Replicate backend does NOT auto-chunk long audio.** It fails on longer videos in one of two ways: a hard-coded ~6-minute Replicate poll timeout, or an outright HTTP 413 "payload too large" on the raw audio upload. For any video roughly **>15 minutes**, don't wait for the script to fail first — proactively chunk yourself:

1. Let `watch.py` download the video normally.
2. Split the resulting audio into ~5-minute segments with `ffmpeg -ss <start> -t 300 -c copy <chunk>.m4a` (stream-copy, no re-encode — fast).
3. Transcribe each chunk separately (reuse the transcription entry point in `scripts/whisper.py`/`transcribe.py`), forcing the `replicate` backend per chunk.
4. Offset each chunk's returned segment timestamps by that chunk's start time, then concatenate all chunks into one continuous transcript before writing the summary.

Then Read every listed frame path (parallel Read calls) and read the merged transcript. If native captions are missing and the chunked Whisper path also fails, proceed frames-only and note that in the summary.

**IMPORTANT — do not end your turn while a background process is still running.** If you background the download/transcribe step, you must actively wait for it (poll it or use a blocking call) and continue in the SAME turn to read frames and write the file. You are a single agent process, not the orchestrator — nothing "notifies" you automatically the way it notifies the orchestrator. Ending your turn assuming a later turn will pick this back up leaves the task permanently incomplete. This matters especially for videos needing chunked Whisper transcription (roughly one chunk per 5-6 minutes of audio), which can take several minutes — just keep waiting. Any of these thoughts means you are about to fail the task: "I'll hold here and resume once the monitor reports," "standing by for X to complete," "I'll wait for the notification that Y finished." There is no monitor, no notification, and no later turn for you specifically. The only correct move when transcription is still processing: immediately issue another blocking/polling tool call and keep doing that, in this same turn, until the watch script's `Work dir:` line actually appears in your own tool output — however many tool calls that takes.

## Step 2 — Write the summary file
Create {REPO_ROOT}\video-summaries\video-summary-{VIDEO_ID}.md. First read 2-3 existing files in that folder (if any exist) to match the exact structure/tone/language convention already established in this project. If this is the first video in this project, use this default structure: `# "Title"` header, bullet metadata block (**Kanal:**, **URL:**, **Länge:**, **Zusammenfassung erstellt:** <today's date>), `---`, content sections with `##` headings covering what's actually said/shown, a `## Kernbotschaft` (1 paragraph), a `## Themen-Tags` line, and a `## Zu prüfen` section for anything uncertain/unverified. Write content in {SPRACHE} regardless of the video's spoken language. Use the actual title/uploader from the script's metadata output.

Reader profile: the reader is interested in what's new but is NOT an expert. The summary must make the video understandable without prior knowledge — avoid compressing it to bare facts. Concretely: (a) Start with a `## Worum geht es?` section (1-2 paragraphs): what is new, what was the situation before, why does it matter. (b) Explain technical terms, product/model names and metrics briefly where they first appear (e.g. what a benchmark measures, what an "effort level" is). (c) Don't just list claims — explain the reasoning and connections (why, compared to what, what follows from it). (d) End the content with a `## Begriffe` glossary (4-10 entries, only terms that occur in the text), placed before `## Kernbotschaft`. (e) Length: about 50-80 % longer than the earlier summaries of this project (measured medians so far, body incl. "Zu prüfen": up to 10 min ≈ 1,350 words, 10-20 min ≈ 1,450, 20-30 min ≈ 1,800, 30-50 min ≈ 1,550, over 50 min ≈ 2,200 — so target roughly 2,000-2,400 / 2,200-2,600 / 2,700-3,200 / 2,500-3,000 / 3,300-4,000 words). Understandability beats completeness; don't pad.

## Step 3 — Plausibility check (be honest, don't fabricate)
Critically read the claims made. For strong/checkable factual claims, spot-check via WebSearch if something seems dubious or you're unsure, and note the outcome. Do NOT invent sources or verification you didn't actually do — if you didn't check something, say so plainly. If genuinely unsure and can't resolve something, say so explicitly in your final report rather than guessing. Treat sensational/clickbait titles with extra scrutiny — describe what's actually shown/claimed, not the hype framing.

## Step 4 — Cross-check against existing notes (do NOT edit other files)
Grep this project's root *.md files and video-summaries/ for terms relevant to this video's themes to find contradictions or notable overlap with what's already documented. Do NOT edit any file other than the new one you're creating. Report contradictions/overlaps back to the orchestrator AND add a short cross-reference note inside your new file's "Zu prüfen" section.

## Step 5 — Value for the target reader
The intended reader/use case for this project is: {ZIELGRUPPE}. If this video contains anything specifically useful for that reader, make sure it's clearly represented in the summary.

## Step 6 — Keep the working directory
Do NOT delete the script's working/temp directory: an independent verification agent needs the transcript and frames. Report the full path of the `Work dir:` in your final report. The orchestrator deletes it after verification.

## Report back
Short (under 250 words): confirm the file was written, state the actual title/length found, list plausibility concerns and contradictions/overlaps found with existing notes, and list open questions for the user (don't guess).
```

## Schritt 5 — Nach jeder Fertigmeldung verifizieren, bevor der Todo als erledigt gilt

**Bekannter Fehlermodus:** Subagents lagern den `watch.py`-Aufruf manchmal in einen eigenen Hintergrundprozess aus und beenden dann ihren eigenen Turn in der Annahme, sie würden automatisch benachrichtigt — das gilt aber nur für den Orchestrator, nicht für Subagents selbst. Ergebnis: Die Task-Notification meldet `completed`, aber die Datei wurde nie geschrieben.

Deshalb **vor** jedem Abhaken im Todo prüfen:

```
Glob: video-summaries/video-summary-<VIDEO_ID>.md
```

Fehlt die Datei trotz `completed`-Meldung: **nicht** einen neuen Agent starten (verliert Kontext/Fortschritt), sondern per `SendMessage` an dieselbe Agent-ID eine Korrektur schicken (kurz erklären, dass die Datei fehlt, dass Hintergrundprozesse aktiv abgewartet werden müssen, und dass die Aufgabe jetzt in einem durchgehenden Turn zu Ende gebracht werden soll). Danach erneut auf die Fertigmeldung warten und wieder verifizieren.

**Hinweis zur Meldung "no API key":** Die Meldung "No transcript available … no API key set" in `watch.py` ist generisch und erscheint bei jedem Whisper-Ausfall, nicht nur bei fehlendem Key. Vor dem Aufgeben den Key selbst prüfen (`~/.config/watch/.env`) und den Lauf einmal selbst wiederholen, bei Videos über 15 Min. mit eigenem 5-Minuten-Chunking. Erst wenn auch der zweite Versuch scheitert, dem Nutzer melden.

## Schritt 5b — Unabhängige Gesamtprüfung (immer)

Für jedes Video, dessen Datei verifiziert vorliegt (Schritt 5), startet der Orchestrator genau einen **eigenständigen Prüf-Agent** (`Agent`, `subagent_type: general-purpose`, `run_in_background: true`). Er darf nicht derselbe Agent sein, der die Zusammenfassung geschrieben hat. Der Prüf-Agent bekommt: Pfad der Zusammenfassung, Pfad des Arbeitsverzeichnisses (Transkript + Frames) des Schreib-Agents, Video-URL, Themenkontext. Er prüft **beides**:

1. **Zusammenfassung gegen das Video:** Jede inhaltliche Aussage, Zahl, Name und jedes Zitat der Zusammenfassung gegen Transkript und Frames abgleichen. Gesucht werden: falsch wiedergegebene Zahlen, Aussagen, die das Video nicht macht, Verwechslungen von Sprechern/Produkten, Hype-Rahmung statt tatsächlichem Inhalt, fehlerhafte Erklärungen in Einleitung und Glossar.
2. **Hinzugefügte Web-Informationen:** Alles, was der Schreib-Agent aus dem Web ergänzt oder als „geprüft" markiert hat (Plausibilitätsprüfung, Querverweise, Glossar-Erklärungen), selbst per WebSearch/WebFetch an den **Primärquellen** erneut prüfen — nicht den Angaben des Schreib-Agents glauben. Zitierte Quellen müssen existieren und das Behauptete tatsächlich belegen.

Auftrag an den Prüf-Agent: aktiv nach Fehlern suchen, nichts erfinden, nichts raten; Unprüfbares als UNABLE TO VERIFY benennen. Pro Aussage (bzw. Aussagengruppe) ein Verdikt: CONFIRMED / PARTIALLY CONFIRMED (mit genauer Angabe, was falsch war) / NOT SUPPORTED (steht so nicht im Video bzw. in der Quelle) / UNABLE TO VERIFY. Bericht kompakt (unter 400 Wörter), Fehler zuerst. Der Prüf-Agent prüft nur und ändert keine Dateien.

Danach:
- Bei Fehlern schickt der Orchestrator sie per `SendMessage` an den Schreib-Agent zur Korrektur (gleiche Agent-ID, kein Neustart) und lässt die korrigierten Stellen kurz nachprüfen.
- Verdikte UNABLE TO VERIFY und strittige Punkte landen im Abschnitt „Zu prüfen" der Datei.
- Erst nach abgeschlossener Prüfung wird das Arbeitsverzeichnis gelöscht und der Todo als erledigt abgehakt.
- Im Abschlussbericht (Schritt 7) kommt pro Video eine Zeile zum Prüfergebnis, Fehler und Korrekturen zuerst.

## Schritt 6 — Wellen fortsetzen

Sobald ein Slot frei wird (Video verifiziert und geprüft fertig), das nächste Video aus der Warteschlange starten — Konkurrenz bei ~3 halten, bis die Liste abgearbeitet ist.

## Schritt 7 — Abschlussbericht im Chat

Kein Roh-Dump aller Einzelberichte. Stattdessen kompakt zusammenfassen:
1. **Echte Widersprüche zu bestehenden Notizen zuerst**, falls welche gefunden wurden — klar benennen, aber NICHT selbst löschen/überschreiben ohne Zustimmung des Nutzers (nur meist veraltete Angaben markieren/korrigieren, bestehende Inhalte nicht kommentarlos entfernen).
2. Inhaltliche Lücken, die mehrfach auffielen (z.B. ein wiederkehrendes Thema ohne eigenen Übersichtsartikel) — anbieten, sie zu entwerfen, nicht ungefragt anlegen (gleiches Prinzip wie beim `notes-audit`-Skill).
3. Kurzer Hinweis, dass jede neue Datei ihren eigenen "Zu prüfen"-Abschnitt mit offenen Detailfragen hat — nicht einzeln auflisten, außer etwas ist wirklich blockierend.
4. Nichts automatisch committen/pushen — nur auf explizite Anfrage.

## Hinweis zur Wiederholung

Dieser Skill ist für einen erneuten Durchlauf gedacht, sobald der Nutzer neue Videos in die Playlist gelegt hat — einfach erneut aufrufen (Playlist-URL und Themenkontext müssen nur beim allerersten Mal pro Projekt geklärt werden, danach reicht ein Blick in bestehende `video-summaries/*.md`), Schritt 2 filtert automatisch nur die wirklich neuen Videos heraus.
