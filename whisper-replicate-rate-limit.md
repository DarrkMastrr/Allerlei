# Warum die Whisper-Transkription beim watch-Skill mit HTTP 429 fehlschlägt

Aufgetreten bei mehreren der 14 Videos in dieser Batch (u.a. [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md), [video-summary-889tcWGEnP0.md](video-summary-889tcWGEnP0.md), [video-summary-AL391nkWGIc.md](video-summary-AL391nkWGIc.md)).

## Kurzantwort

Das Rate-Limit liegt an **Replicate** (dem Hosting-Layer), nicht an Whisper selbst. Ein Sub-Agent bekam die konkrete Fehlermeldung:

> "rate limit... while you have less than $5.0 in credit"

Das ist eine Replicate-spezifische Kontostand-Sperre — Replicate throttelt/blockiert Accounts, deren Prepaid-Guthaben unter einer Schwelle liegt, unabhängig davon, wie oft man tatsächlich anfragt.

## Root-Cause-Analyse (Code: `claude-skills/watch/scripts/whisper.py`)

Der `watch`-Skill unterstützt drei Backends für die Transkription, in Prioritätsreihenfolge:

1. `GROQ_API_KEY` → Groq Whisper-API (`api.groq.com`)
2. `REPLICATE_API_TOKEN` → Replicate-gehostetes `openai/whisper` (`api.replicate.com`)
3. `OPENAI_API_KEY` → OpenAI Whisper-API (`api.openai.com`)

Auf diesem Rechner ist der **Replicate-Fallback-Patch** des watch-Skills aktiv (siehe Commit "Add watch skill (with Replicate whisper fallback) for sandbox sync") — vermutlich weil kein Groq/OpenAI-Key hinterlegt ist und stattdessen ein Replicate-Token genutzt wird.

Replicate ist dabei kein Whisper-Anbieter im eigentlichen Sinn, sondern eine allgemeine Modell-Hosting-Plattform, die Whisper als eines von vielen Modellen bereitstellt (`_replicate_whisper()` in `whisper.py:314`). Replicate erzwingt **kontostandbasierte Rate-Limits**: Accounts mit wenig/keinem Guthaben werden auf einer sehr niedrigen Anfragerate gedeckelt, unabhängig vom Whisper-Modell selbst — das ist Replicates eigene Plattform-Policy, keine Whisper-/OpenAI-Eigenschaft.

Zusätzlich beobachtet: Bei einigen Videos scheiterte parallel auch der **native YouTube-Untertitel-Abruf** mit HTTP 429 (z. B. bei 889tcWGEnP0, AL391nkWGIc) — das ist ein komplett separates Rate-Limit von yt-dlp/YouTube selbst, nicht von Replicate, und wurde in der Analyse nicht mit dem Whisper-429 verwechselt.

## Praktische Konsequenz

- Um das zu beheben: Guthaben auf dem Replicate-Account auf mindestens 5 $ aufladen (behebt die Sperre direkt), oder
- einen `GROQ_API_KEY` hinterlegen (Groq hat laut `SKILL.md` ein großzügigeres kostenloses Kontingent und wird vom Skill ohnehin bevorzugt, wenn beide Keys vorhanden sind) — dann greift der Replicate-Fallback gar nicht erst.
- Der Skill selbst degradiert bereits automatisch auf frames-only, wenn Whisper nach 2 Rate-Limit-Versuchen weiter fehlschlägt (`MAX_429_RETRIES = 2` in `whisper.py:152`) — kein Bug, sondern beabsichtigtes Verhalten.
