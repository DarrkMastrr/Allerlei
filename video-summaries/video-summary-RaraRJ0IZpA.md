# "So arbeitet Claude Code den GANZEN Tag alleine (ohne Rückfragen)"

**Kanal:** Sebastian Claes | N8N & KI-Agenten
**URL:** https://www.youtube.com/watch?v=RaraRJ0IZpA
**Länge:** 08:28
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md) und [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md) für zwei unabhängige, frühere Umsetzungen desselben Karpathy-"LLM-Wiki"-Grundkonzepts; [ai-agent-workflow.md](../ai-agent-workflow.md) und [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) für verwandte Autoreview-Loop-/Loops-statt-Prompts-Konzepte; [video-summary-TP73qyFWDcY.md](video-summary-TP73qyFWDcY.md) für Boris Chernys Zitat zu "Hooks, Schedule, Loops" als den drei stärksten Claude-Code-Automatisierungsfeatures.*

## Ausgangsthese: Reaktiv statt autonom

Sebastian (laut Eigenaussage seit über 7 Jahren Softwareentwickler, schult Unternehmen in KI/Automatisierung) beschreibt den Status quo der meisten KI-Nutzung als reines Prompt-Antwort-Pingpong: Aufgabe geben, Antwort bekommen, korrigieren — "wirklich autonom ist das nicht". Sein Gegenentwurf: der KI einen kompletten Arbeitstag am Stück übergeben, statt durchgehend präsent sein zu müssen. Grund für den heutigen Zeitverlust laut Video: die KI kommt mit Rückfragen und "vergisst etwas, weil Wissen nicht ordentlich persistiert wird".

## Baustein 1: Das LLM-Wiki als Wissensgrundlage (Andrej Karpathy)

Damit ein Agent ("Agent Harness" — die Umgebung, in der eine KI Dinge ausführen kann, genannt werden Claude Code und Codex) ein Projekt versteht, braucht er laut Video eine saubere Struktur statt eines unsortierten Dokumentenhaufens — Analogie: ein Lexikon lohnt sich erst mit Inhaltsverzeichnis. Zitiert wird dafür explizit **Andrej Karpathy** (im Whisper-Transkript als "Andrew Capafi" verschriftet — im Bild eindeutig als GitHub-Gist `karpathy/llm-wiki` zu sehen, siehe Frame t=01:59; passt zum bereits im Repo dokumentierten Muster von Whisper-Fehlhörungen bei bekannten KI-Namen, vgl. "Cherney" für Boris Cherny in [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md)). Das Prinzip läuft über drei Ordner:
1. **RAW** — unveränderliche Rohdaten (Dokumente, Verträge, E-Mails)
2. **Wiki** — hier darf die KI sich frei austoben, alles als Markdown-Dateien, primär für die KI lesbar, nicht zwingend hübsch für Menschen
3. **Schema-Dateien** (`CLAUDE.md`/`AGENTS.md`) — werden von der KI automatisch eingelesen, sobald sie auf den Ordner stößt, enthalten Regeln und ein Inhaltsverzeichnis

Dieses Konzept deckt sich inhaltlich fast vollständig mit zwei bereits im Repo dokumentierten, unabhängigen Videos zum selben Karpathy-Pattern: [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md) (Inbox→Wiki→Output-Variante) und [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md) (konkretes Obsidian-Plugin dazu) — dieses Video ist die dritte unabhängige Umsetzung desselben Grundprinzips im Repo-Bestand.

## Baustein 2: Die "Assembly Line" — ein Arbeitsauftrag wird zu einem Arbeitstag

Kernstück des Videos, per Whiteboard-Zeichnung erklärt (ab ca. t=03:45):
1. **Arbeitsauftrag** — roher, diktierter/unformatierter Text als Ausgangspunkt
2. **Aufteilung in Arbeitspakete** (AP1, AP2, AP3, …) durch die KI selbst
3. Pro Arbeitspaket: ein eigener **Bau-Agent** setzt das Paket um
4. Ein zweiter, unabhängiger **Prüf-Agent** kontrolliert Code, Design/UI und Vorgaben — laut Video "sehr sensibel"
5. Ist der Prüf-Agent nicht zufrieden, geht es in einer **Nachbesserungsschleife** zurück zum Bau-Agenten ("mach das bitte nochmal")
6. Mehrere solcher Durchläufe werden zu **"Wellen"** gebündelt und nacheinander abgearbeitet (Welle A, B, C, …), am Ende ein **Abschlussagent**
7. Alle Erkenntnisse werden zuletzt ins Wiki aus Baustein 1 zurückgeschrieben

Für die konkrete Umsetzung nutzt Sebastian nach eigener Aussage bereits bestehende Claude-Skills — in dieser Version heißt der zentrale Skill **"Loop"**; jeder einzelne Bau-/Prüf-/Nachbesserungs-Schritt ist ein **Subagent**, die Gesamtheit ein **Workflow** aus bereits vorhandenen Skills, in einen Prompt gepackt.

## Live-Demo: 24 Arbeitspakete, ~2 Stunden autonome Laufzeit

Gezeigt wird ein Terminal-Screenshot (Frame ab t=06:08) eines eigenen Tools namens **"matrix-Desktop-Client"**: "Rückmeldungsrunde 5", 24 Punkte in 24 Arbeitspaketen, Modell **Opus 5**, Gesamtlaufzeit zum Aufnahmezeitpunkt **1 Stunde 50 Minuten**. Welle A zeigt 30 einzelne Agenten-Einträge (`bau:AP27`, `kontrolle:AP28M1`, `nachbesserung:AP28M1` usw.) mit Modell, Tokenverbrauch und Laufzeit pro Schritt, 29/30 abgeschlossen; Welle B–D sind zu diesem Zeitpunkt noch "Not started yet". Sebastian betont ausdrücklich: **kein selbst gebautes Programm**, sondern die ganz normale Claude-Code-CLI im Terminal — funktioniert genauso in Claude Desktop oder "jeglicher anderen Agent Harness", explizit auch mit Codex genannt. Nötig sei nur, den eigenen Input (Features/Aufgaben) zu liefern und den (kostenlos verlinkten) Prompt zu kopieren, oder sich daraus einen eigenen Skill zu bauen.

## Ausblick / Marketing-Teil

Am Ende (ab t=08:09) weist Sebastian darauf hin, dass diese "Assembly Line" nur ein Baustein eines größeren, in seinem eigenen Projekt genutzten Systems namens **"Matrix"** sei, und bittet um das Kommentar-Stichwort "Matrix" für ein mögliches Folgevideo dazu — reiner Teaser, keine weiteren Details im Video selbst.

---

## Für den technischen Team-Lead: Praktische Übertragung

- **Arbeitspaket-Zerlegung mit Build+Review+Nachbesserungsschleife** ist strukturell dasselbe Muster wie die im Repo bereits dokumentierte "Autoreview-Loop" ([ai-agent-workflow.md](../ai-agent-workflow.md), Punkt 2) — hier aber explizit mit zwei getrennten Agenten-Rollen (Bau vs. Kontrolle) statt einem einzelnen sich selbst review-enden Agenten. Für Team-Workflows interessant als Vorlage, wie man große, mehrteilige Aufträge (z. B. eine Serie von Testreihen, eine Sammlung offener Doku-Lücken) in parallel bearbeitbare, einzeln prüfbare Pakete zerlegt — deckt sich mit der bereits im Repo festgehaltenen Empfehlung "Teilziele definieren, die einzeln prüfbar sind" ([ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md), Punkt 4).
- **Das LLM-Wiki als Team-Wissensbasis** ist der direkt relevanteste Teil für eine Gruppenleiter-Rolle: eine strukturierte, von der KI gepflegte Markdown-Wissensbasis (RAW/Wiki/Schema) ist im Kern dasselbe Muster, das dieses Repo selbst für die Video-Notizen anwendet (root-`.md`-Übersichtsartikel als "Wiki", `video-summaries/` als Rohnotizen-Sammlung, CLAUDE.md als Schema/Regel-Datei) — siehe auch [notes-audit-report.md](../notes-audit-report.md) als Beispiel für den dort schon eingeführten "Health-Check"-Gedanken, der sich fast wörtlich mit dem Pflege-Schritt in [video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md) deckt.
- **Governance-Frage bleibt offen, wird im Video aber nicht thematisiert:** Fast zwei Stunden komplett unbeaufsichtigte Laufzeit mit 24 parallelen Arbeitspaketen wirft dieselbe Frage auf, die [video-summary-sQBinJA_zxU.md](video-summary-sQBinJA_zxU.md) unter "Human in the Loop bei kritischen Aktionen" bereits aufwirft — dieses Video zeigt zwar eine automatisierte Qualitätskontrolle (Prüf-Agent), aber keine Stelle, an der ein Mensch vor Abschluss eingreifen müsste. Für sicherheits- oder kundenrelevante Aufgaben (vgl. [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md), Punkt 2) wäre das unverändert nicht geeignet, für interne/unkritische Großaufträge (Punkt 5 dort) aber plausibel übertragbar.

## Kernbotschaft
Das Video verbindet zwei bereits im Repo bekannte Bausteine zu einem konkreten Workflow: eine von der KI selbst gepflegte, dreischichtige Wissensbasis nach Andrej Karpathys "LLM-Wiki"-Pattern (RAW/Wiki/Schema) als Gedächtnis, plus eine "Assembly Line" aus automatisch generierten Arbeitspaketen, die jeweils von einem Bau-Agenten umgesetzt und von einem unabhängigen Prüf-Agenten mit Nachbesserungsschleife kontrolliert werden, gebündelt in sequenziellen "Wellen". In der gezeigten Live-Demo lief ein solcher Auftrag mit 24 Arbeitspaketen fast zwei Stunden komplett unbeaufsichtigt in der normalen Claude-Code-CLI. Das eigentliche, größere System dahinter ("Matrix") wird nur angeteasert, nicht erklärt.

## Themen-Tags
Claude Code, Agent Harness, LLM-Wiki, Andrej Karpathy, Autonome Agenten, Subagenten, Arbeitspakete, Bau-Prüf-Loop, Nachbesserungsschleife, Opus 5, Codex, Claude Skills, Wissensmanagement, N8N

## Zu prüfen
- **Per WebSearch bestätigt:** Der Gist `karpathy/llm-wiki` ist real (u. a. direkt über `gist.github.com/karpathy/442a6bf555914893e9891c11519de94f` sowie mehrere unabhängige Tutorial-/Blogartikel gefunden) und beschreibt exakt das im Video gezeigte Drei-Schichten-Prinzip (Raw/Wiki/Schema) — die inhaltliche Wiedergabe im Video ist zutreffend. Die Fehlhörung "Andrew Capafi" statt "Andrej Karpathy" im Whisper-Transkript ist durch den GitHub-Screenshot im Bild (Frame t=01:59) eindeutig aufgelöst.
- **Nicht unabhängig verifizierbar:** Das eigene Tool "matrix-Desktop-Client"/"matrix-Desktop-node-4" sowie das größere System "Matrix" sind offenbar proprietäre, nicht öffentlich verfügbare Eigenentwicklungen des Kanals — im Video nur als Screenshot gezeigt, keine Möglichkeit zur externen Prüfung. Die konkrete Demo (24 Arbeitspakete, 1:50 h Laufzeit, "Opus 5") ist ein nicht nachprüfbares Einzelbeispiel.
- **Cross-Check gegen bestehende Notizen:** Kein inhaltlicher Widerspruch gefunden. Deutliche thematische Überschneidung mit zwei bereits vorhandenen Videos zum selben Karpathy-LLM-Wiki-Konzept ([video-summary-meZirzrbqXM.md](video-summary-meZirzrbqXM.md), [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md)) — alle drei bestätigen sich gegenseitig im Kernprinzip, unterscheiden sich nur in der konkreten Umsetzung (manueller CLAUDE.md-Workflow vs. Obsidian-Plugin vs. hier: kombiniert mit der Arbeitspaket-Assembly-Line). Ebenfalls Überschneidung mit dem in [video-summary-TP73qyFWDcY.md](video-summary-TP73qyFWDcY.md) dokumentierten Boris-Cherny-Zitat zu "Hooks, Schedule, Loops" als stärkste Automatisierungsfeatures — dieses Video zeigt mit dem "Loop"-Skill eine konkrete praktische Anwendung davon, ohne Hooks oder Schedule selbst zu erwähnen. Der Begriff "Agent Harness" wird hier in etwa deckungsgleich mit der Verwendung in [video-summary-sQBinJA_zxU.md](video-summary-sQBinJA_zxU.md) benutzt (Umgebung, in der eine KI Aktionen ausführt) — passt zur in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) bereits notierten Beobachtung, dass sich der "Harness"-Begriff 2026 noch nicht einheitlich gesetzt hat.
- Die Selbstauskünfte des Sprechers (7+ Jahre Erfahrung, Firmenschulungen) sind nicht unabhängig geprüft, wie bei anderen Solo-Creator-Videos in diesem Repo üblich unkritisch als Kanal-Selbstdarstellung zu behandeln.

**Hinweis zum Ablauf:** Native Untertitel scheiterten zweimal mit HTTP 429 (sowohl beim ersten als auch beim zweiten Versuch), zusätzlich schlug der erste komplette Download-Versuch mit HTTP 403 fehl. Beim zweiten Versuch lief der Video-Download durch, der Whisper-Fallback (Replicate) lieferte in einem Durchgang 135 Segmente für die vollen 8:28 Minuten. Alle 80 extrahierten Frames (0,158 fps, volle Videolänge) wurden gesichtet — davon ca. 55 Talking-Head-Aufnahmen ohne zusätzliche Information, plus die für die Zusammenfassung zentralen Whiteboard-Skizzen (t=01:48–06:21) und zwei Screenshots (Karpathy-Gist, Matrix-Terminal-Demo).
