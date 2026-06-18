# KI-Agent-Workflow — destilliert aus Peter Steinbergers Build-Talk

Quelle: [video-summary-TP73qyFWDcY.md](video-summary-TP73qyFWDcY.md) ("1,3 Mio. $ in 30 Tagen: So sieht KI Coding ohne Limits aus")

Zugeschnitten auf Solo-Entwicklung mit Claude Code — nur die Prozesse, die sich direkt umsetzen lassen.

## 1. Closing the Loop — Agent erst melden lassen, wenn er selbst verifiziert hat

Nicht: Prompt geben → Ergebnis bekommen → selbst testen → Bug melden → wiederholen.
Stattdessen: dem Agenten die Mittel geben, sich selbst zu verifizieren, bevor er sich meldet.

**Umsetzung:**
- Vor "fertig" melden lassen: Dev-Server starten, Browser öffnen, Feature manuell durchklicken (passt zum `/run`- und `/verify`-Skill, die hier schon verfügbar sind)
- Bei UI-Änderungen: Screenshot/Browsertest einfordern statt "sollte funktionieren" zu akzeptieren
- Permissions so setzen, dass der Agent Server starten, Tests laufen lassen und Debugging-Tools nutzen darf, ohne jedes Mal nachzufragen

## 2. Autoreview-Loop — Review-Zyklus an den Agenten abgeben

Nicht: einmal reviewen lassen, Bugs fixen, fertig.
Stattdessen: der Agent reviewt sein eigenes Ergebnis so lange, bis er nichts mehr findet.

**Umsetzung:**
- Nach größeren Changes `/code-review` (oder bei wichtigeren Branches `/code-review high`/`ultra`) nicht nur einmal, sondern als Schleife verstehen: Findings fixen lassen → erneut reviewen lassen → erst dann als fertig betrachten
- Diese Schleife explizit einfordern statt nach dem ersten Fix zufrieden zu sein

## 3. vision.md neben CLAUDE.md führen

`agents.md`/`CLAUDE.md` beschreibt *wie* gearbeitet wird. `vision.md` beschreibt *wohin* das Projekt soll — hilft dem Agenten bei Entscheidungen, die nicht eindeutig aus dem Code ableitbar sind (z. B. "welche Features passen rein, welche nicht").

**Umsetzung:**
- Bei Projekten, die über ein Wochenend-Experiment hinausgehen, ein kurzes `vision.md` anlegen: Projektziel, Richtung, offene Diskussionspunkte
- Nicht für Wegwerf-Skripte oder einmalige Spielereien — lohnt sich erst, wenn das Projekt über mehrere Sessions wächst

## 4. Ideen aus eigener Reibung statt aus der Luft

Peters Tools (ClawSweeper, Crabbox, GOG CLI) entstanden alle aus echtem, wiederkehrendem Ärger — nicht aus Spekulation.

**Umsetzung:**
- Wenn ein manueller Schritt mehr als 1-2x nervt → das ist der Kandidat für ein eigenes Skill/Script, nicht eine hypothetische Idee
- Konkret im Claude-Code-Kontext: wiederkehrende manuelle Abläufe als Skill unter `~/.claude/skills/` festhalten (wie es mit `watch` schon existiert)

## 5. Nicht alles muss systemkritisch sauber sein

Vieles an internen Tools/Skripten ist nicht geschäftskritisch → bewusst "vibe-coden" erlauben, ohne jede Zeile zu prüfen.

**Umsetzung:**
- Bei persönlichen Tools/Automatisierungen (nicht bei production-facing Code) Review-Tiefe bewusst reduzieren — Zeit sparen für die Dinge, die wirklich Fehler kosten dürfen

## Bewusst nicht übernommen

- **ClawSweeper/Crabbox als Cloud-Infrastruktur** — macht nur bei Projekten mit hohem Issue-/Test-Volumen Sinn (35k+ Issues, große Testsuiten), nicht für Solo-Projekte in diesem Maßstab
- **Token-Maxing-Mentalität** — laut Video wird Token-Sparsamkeit zunehmend wichtiger; Ankündigung eines Folgevideos zu Prompt Caching — bei Gelegenheit gegenchecken, ob das neue Erkenntnisse für den eigenen Workflow bringt
