# Claude Skills — das Grundkonzept im Überblick

Quellen: [video-summary-sQBinJA_zxU.md](video-summaries/video-summary-sQBinJA_zxU.md), [claude-oekosystem-ueberblick.md](claude-oekosystem-ueberblick.md), [video-summary-B_OqkMRFonM.md](video-summaries/video-summary-B_OqkMRFonM.md), [video-summary-KWrsLqnB6vA.md](video-summaries/video-summary-KWrsLqnB6vA.md), [video-summary-TP73qyFWDcY.md](video-summaries/video-summary-TP73qyFWDcY.md), [video-summary-rRF3pAEQuzM.md](video-summaries/video-summary-rRF3pAEQuzM.md), [video-summary-AL391nkWGIc.md](video-summaries/video-summary-AL391nkWGIc.md), [video-summary-wZeOwqmSw84.md](video-summaries/video-summary-wZeOwqmSw84.md)

Skills tauchen in praktisch jedem zweiten der angeschauten Videos auf, aber immer nur am Rand. Dieser Artikel bündelt das Grundkonzept, das in keiner Einzel-Zusammenfassung vollständig steht (siehe [notes-audit-report.md](notes-audit-report.md)).

## Was ein Skill technisch ist

Ein Skill ist kein simpler Custom-Instruction-Text, sondern ein echter lokaler Ordner mit strukturierten Markdown-Dateien und ggf. kleinen Skripten (sQBinJA_zxU) — im Kern eine Datei, die festlegt, was Claude tun soll, welche Schritte es befolgen muss und wie das Ergebnis aufgebaut sein soll (rRF3pAEQuzM). Ein kompletter, wiederverwendbarer Arbeitsablauf, der per Triggerwort gestartet wird — laut B_OqkMRFonM "wahrscheinlich der wichtigste Punkt" im gesamten Funktionsumfang von Claude.

## Wie Skills mit anderen Bauteilen zusammenspielen

- **Slash-Commands** sind die Trigger für einen Skill (`/stichwort`) — nicht der Skill selbst (B_OqkMRFonM)
- **Plugins** bündeln mehrere Skills zu einem installierbaren Paket (B_OqkMRFonM)
- **Scheduled Tasks** lassen Skills automatisch zu festen Zeiten laufen (B_OqkMRFonM, wZeOwqmSw84)
- **MCP** ist etwas anderes als ein Skill: Skill = Wissen ("die Fahrstunde"), MCP = der Werkzeugzugriff, der KI-Absichten in konkrete API-Aufrufe übersetzt ("der Autoschlüssel") — Details dazu in [mcp-ueberblick.md](mcp-ueberblick.md)

## Das Kontextfenster-Problem und seine Lösung

Man kann nicht bei jedem Prompt das komplette "Firmenhandbuch" mitgeben. Die Lösung heißt **Progressive Disclosure**: das System sucht per semantischer Suche im Hintergrund nur die eine passende Skill-Datei heraus und lädt nur diese ins aktive Gedächtnis (sQBinJA_zxU, claude-oekosystem-ueberblick.md).

## Wie man gute Skills baut

- **Nie abstrakt planen, immer aus einer konkreten Konversation heraus** (TP73qyFWDcY): Der Use Case ist bereits validiert, weil man die Arbeit gerade manuell gemacht hat. Prompt-Muster: *"Based on this conversation, build me a skill"*
- **Nach dem Bauen einen "Gotchas"-Abschnitt ergänzen**, der Fehler und Edge Cases dokumentiert, damit sie sich nicht wiederholen (TP73qyFWDcY)
- **Faustregel für Kandidaten:** Ein manueller Schritt, der mehr als 1-2x nervt, ist der Kandidat für einen Skill — nicht eine hypothetische Idee (ai-agent-workflow.md, destilliert aus Peter Steinbergers Workflow)
- **Einstiegs-Prompt, falls unklar was sich lohnt:** *"Based on the project I'm working on, what Claude Skills should I create?"* (KWrsLqnB6vA, Boris Chernys Workflow) — Analogie dort: ein Prompt ist "dribble the ball", ein Skill der "einstudierte Spielzug"
- Erstellt werden Skills über den offiziellen `/skill-creator`, der per Rückfragen durch den Prozess führt (rRF3pAEQuzM)

## Beispiele aus den Videos

- **rRF3pAEQuzM** zeigt fünf konkrete Wissensarbeits-Skills im Detail: Präsentationsarchitekt (SCR-Framework), Aufgabenextraktor (5W1H aus Meeting-Transkripten), Qualitätsprüfer (systematisches Output-Review), Kompaktmodus (kürzere Antworten, spart Output-Tokens) und Kontext-Kompressor (verdichtet lange Chats zu einem "Context Pack", spart Input-Tokens)
- **AL391nkWGIc** zeigt einen domänenspezifischen Skill: "home-assistant-best-practices", installierbar via `npx skills add` oder Plugin-Marketplace, mit Entscheidungsworkflows und Namenskonventionen für Smart-Home-Automatisierungen

## Spannungsfeld: Skills als Produktivitätsgewinn vs. Vendor-Lock-in

Zwei der Videos ziehen aus Skills gegensätzliche Schlüsse, ohne sich direkt zu widersprechen — es sind einfach unterschiedliche Blickwinkel: [video-summary-6LVB3mpPvB4.md](video-summaries/video-summary-6LVB3mpPvB4.md) empfiehlt den Aufbau eigener Skills explizit als **Resilienz-Strategie** gegen den Ausfall eines einzelnen KI-Anbieters (siehe [fable-5-modell-sperre.md](fable-5-modell-sperre.md)). [video-summary-sQBinJA_zxU.md](video-summaries/video-summary-sQBinJA_zxU.md) warnt umgekehrt: Wer hunderte Skills/MCP-Interfaces speziell für einen Anbieter baut, bindet sich gerade dadurch stark an diesen. Auflösung: Die Skill-Definition selbst (Markdown + Beschreibung) ist meist anbieterunabhängig übertragbar — die Bindung entsteht eher durch anbieterspezifische Trigger-Mechanik/Slash-Commands als durch den Skill-Inhalt selbst.

---

## Kernbotschaft
Skills sind Claudes wichtigster Baustein für wiederholbare Arbeitsabläufe: echte Ordner mit Markdown-Anweisungen, per Progressive Disclosure kontextfenster-schonend geladen, am besten aus einer bereits geführten Konversation heraus gebaut statt abstrakt geplant. Sie lösen ein reales Produktivitätsproblem, sollten aber nicht blind auf einen einzigen Anbieter zugeschnitten werden.

## Themen-Tags
Claude Skills, Skill-Creator, Progressive Disclosure, Slash-Commands, Plugins, Produktivität, Vendor-Lock-in
