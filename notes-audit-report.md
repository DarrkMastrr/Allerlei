# Notes Health Check — 2026-08-01

**Status:** Alle vier Punkte unten wurden am 2026-08-01 umgesetzt — die zwei Widersprüche sind mit Cross-Check-Vermerken in den betroffenen Dateien versehen, und für beide Themen-Kandidaten existieren jetzt eigene Artikel ([claude-skills-ueberblick.md](claude-skills-ueberblick.md), [mcp-ueberblick.md](mcp-ueberblick.md)). Der offene Platzhalter in `ki-guidelines-hardware-unit.md` bleibt bewusst offen — das ist eine unitspezifische Ergänzung, keine Notes-Pflege.

Geprüfter Bestand: 16 Video-Zusammenfassungen (`video-summaries/`) + 7 Themen-Übersichtsartikel im Root (23 Dateien). Vendored Plugin-Doku unter `claude-skills/watch/` und dieser Report selbst sind ausgeschlossen.

## Widersprüche

- **Modellname-Inkonsistenz „Opus 4.7" vs. „Opus 4.8":** [video-summary-wZeOwqmSw84.md](video-summaries/video-summary-wZeOwqmSw84.md) nennt „Opus 4.7", während [video-summary-B_OqkMRFonM.md](video-summaries/video-summary-B_OqkMRFonM.md), [video-summary-WVHfDaawIRk.md](video-summaries/video-summary-WVHfDaawIRk.md) und [fable-5-modell-sperre.md](fable-5-modell-sperre.md) übereinstimmend „Opus 4.8" nennen. Da 3 von 4 unabhängigen Quellen „4.8" bestätigen, spricht einiges für einen veralteten/falschen Wert in wZeOwqmSw84 — beide Dateien haben das aber bereits einzeln als „Zu prüfen" markiert, nur nicht gegeneinander abgeglichen.
- **Unbestätigter Verdacht, aber gestützt durch Cross-Reference:** [video-summary-AGZnfT7O7rw.md](video-summaries/video-summary-AGZnfT7O7rw.md) vermutet selbst einen Transkriptionsfehler bei der Zuordnung „Peekaboo CLI" → Peter Steinberger. [ai-agent-workflow.md](ai-agent-workflow.md), das unabhängig aus Steinbergers eigenem Talk destilliert wurde, listet seine Tools als ClawSweeper/Crabbox/GOG CLI und erwähnt Peekaboo CLI nicht. Das stützt den Verdacht, löst ihn aber nicht abschließend auf — beide Dateien bereits mit Verweis aufeinander sinnvoll, ein Eintrag in AGZnfT7O7rw als „vermutlich falsch, siehe ai-agent-workflow.md" würde das festschreiben.

## Unbelegte Behauptungen

Die meisten offenen Behauptungen sind bereits pro Datei im jeweiligen `## Zu prüfen`-Abschnitt erfasst (z. B. Sternezahlen, Zitate, Selbstauskünfte von YouTubern). Datei-übergreifend fiel nur ein zusätzlicher Punkt auf, der kein Faktencheck-, sondern ein Vollständigkeits-Thema ist:

- [ki-guidelines-hardware-unit.md](ki-guidelines-hardware-unit.md), Abschnitt 6 („Vertraulichkeit und Datenklassifizierung"), enthält den offenen Platzhalter *„[hier unitspezifisch ergänzen, sobald die Regelung von IT/Compliance vorliegt]"*. Kein Fehler, aber bei Weitergabe/Veröffentlichung des Dokuments sollte das nicht übersehen werden.

## Themen-Kandidaten für einen eigenen Artikel

- **Claude Skills** — erwähnt in mindestens 8 Dateien ([video-summary-sQBinJA_zxU.md](video-summaries/video-summary-sQBinJA_zxU.md), [claude-oekosystem-ueberblick.md](claude-oekosystem-ueberblick.md), [video-summary-B_OqkMRFonM.md](video-summaries/video-summary-B_OqkMRFonM.md), [video-summary-KWrsLqnB6vA.md](video-summaries/video-summary-KWrsLqnB6vA.md), [video-summary-TP73qyFWDcY.md](video-summaries/video-summary-TP73qyFWDcY.md), [video-summary-rRF3pAEQuzM.md](video-summaries/video-summary-rRF3pAEQuzM.md), [video-summary-AL391nkWGIc.md](video-summaries/video-summary-AL391nkWGIc.md), [video-summary-wZeOwqmSw84.md](video-summaries/video-summary-wZeOwqmSw84.md)) — aber es gibt keinen konsolidierten Übersichtsartikel dazu, wie es ihn für Fable 5 oder die Karpathy-Guidelines bereits gibt. rRF3pAEQuzM kommt dem am nächsten, deckt aber nur 5 Beispiel-Skills ab, nicht das allgemeine Konzept (Progressive Disclosure, Skill vs. Custom Instructions, Skill vs. MCP).
- **MCP (Model Context Protocol)** — erwähnt in [video-summary-sQBinJA_zxU.md](video-summaries/video-summary-sQBinJA_zxU.md), [claude-oekosystem-ueberblick.md](claude-oekosystem-ueberblick.md), [video-summary-B_OqkMRFonM.md](video-summaries/video-summary-B_OqkMRFonM.md) sowie einem eigenen Deep-Dive-Video ([video-summary-AL391nkWGIc.md](video-summaries/video-summary-AL391nkWGIc.md), Home-Assistant-MCP) — bislang keine allgemeine Übersicht, die das Grundkonzept und das HA-Beispiel zusammenführt.

Kein Kandidat trotz mehrfacher Erwähnung: **Agent Loop / Verifikations-Feedback-Loop** taucht ebenfalls oft auf, ist aber bereits über [ai-agent-workflow.md](ai-agent-workflow.md) + [karpathy-claude-md-guidelines.md](karpathy-claude-md-guidelines.md) + [ki-guidelines-hardware-unit.md](ki-guidelines-hardware-unit.md) mit gegenseitigen Verweisen abgedeckt.
