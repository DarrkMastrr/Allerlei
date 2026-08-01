# "Vibe Coding hat ein Sicherheitsproblem (mein Security-Workflow)"

**Kanal:** Benjamin Thorstensen
**URL:** https://www.youtube.com/watch?v=AGZnfT7O7rw
**Länge:** 14:22
**Zusammenfassung erstellt:** 2026-07-04

---

## Ausgangslage

- KI-generierter Code gilt als Sicherheitsrisiko: hardcodierte API-Keys, Klartext-Passwörter, massenhaft ungeprüfter Code
- Gleichzeitig sinkt die Einstiegshürde für Angreifer, da diese ebenfalls KI-Agenten einsetzen können
- Die meisten Einzelentwickler/kleinen Teams haben kein eigenes Security-Team
- Der Video-Autor stellt einen eigenen, wiederverwendbaren 4-Phasen-Workflow vor, den KI-Agenten (Codex, Claude Code) zum eigenen "Security-Team" macht

## Phase 1: Audit (statische Analyse mit Open-Source-Tools)

- Der Main-Agent analysiert die Codebasis, wählt passende Tools (z.B. Semgrep, CodeQL, Gitleaks, OSV-Scanner, Trivy) und spawnt dafür mehrere Sub-Agenten, die parallel arbeiten
- Bewusst ein **Prompt statt eines Skills**: Skills führt der Agent selbstständig aus, ein Prompt muss explizit angestoßen werden
- Live-Demo mit Codex an einer Next.js-Codebasis: nach ca. 18 Minuten liefert der Agent eine gerankte Schwachstellenliste (Severity, Risk, Evidence, empfohlene Fixes)

## Phase 2: Hunt (der Agent liest den Code wirklich)

- **Weg 1 – Prompt-Methode nach Nicolas Carlini**: einfacher CTF-artiger Prompt ("finde eine Sicherheitslücke, schreibe die schwerwiegendste in einen Report"). Bei großen Codebasen: Prompt um konkrete Hinweise ergänzen und mehrere parallele Agenten auf unterschiedliche Bereiche ansetzen
- **Weg 2 – Deepsec-CLI**: Open-Source-Tool, analysiert Datenfluss, ein zweiter KI-Agent reviewt die Funde. Demo-Ergebnis: 10 Critical, 37 High, 10 Medium, 1 Normal Bug

## Phase 3: Break (Agent testet die Anwendung wie ein Angreifer)

- Web-App → Agent-Browser CLI; native App → Computer Use (z.B. Peekaboo CLI)
- White-Box (Agent kennt Code) vs. Black-Box (Agent kennt nur URL) — beide haben Vorteile
- Codex/Claude Code können bei sicherheitsnahen Prompts eine "flagged for possible cybersecurity risk"-Meldung zeigen

## Phase 4: Automate

- Erkenntnisse aus Phase 1 im Audit-Ordner ablegen, für wiederkehrende Scans nutzen
- Automatisierung z.B. täglicher Scan über Codex-/Claude-Code-Automations
- Zusätzlich empfohlen: KI-Code-Reviewer für laufende PRs (Greptile, CodeRabbit)

## False Positives

- Gemeldete Bugs immer mit einem Beweis (reproduzierbare Umgebung) belegen — bestätigt den Fund und erlaubt späteres Nachprüfen

## Wichtiger Vorbehalt und Ausblick

- Der Workflow ist nur das Minimum — Verantwortung für Fehler trägt am Ende der Mensch
- Neues Risiko: Dependencies/Supply-Chain-Angriffe — externe Frameworks können selbst kompromittiert sein

---

## Kernbotschaft
KI-Agenten lassen sich über vier Phasen (Audit, Hunt, Break, Automate) zu einem eigenen "Security-Team" ausbauen — auch ohne eigenen Security-Hintergrund. Das ersetzt kein professionelles Audit, erhöht aber massiv den Aufwand für Angreifer, während Dependency-/Supply-Chain-Risiken mitgedacht werden müssen.

## Themen-Tags
Vibe Coding, Security-Workflow, KI-Agenten, Agentic Coding, Codex, Claude Code, Penetration Testing, Supply-Chain-Security

## Zu prüfen (falls zutreffend)
- Aussage, dass KI-Agenten laut Nicolas Carlini bereits besser Sicherheitslücken finden können als er selbst
- Konkrete Demo-Ergebnisse (Zeitangaben, Bug-Zahlen) — projektspezifisches Einzelbeispiel
- Existenz und genaue Konditionen von OpenAIs "Trusted Access for Cyber"-Programm
- Zuordnung "Peekaboo CLI" zu Peter Steinberger (Transkript evtl. fehlerhaft). **Cross-Check (Notes-Audit 2026-08-01):** [ai-agent-workflow.md](../ai-agent-workflow.md), unabhängig aus Steinbergers eigenem Talk destilliert, listet seine Tools als ClawSweeper/Crabbox/GOG CLI und erwähnt Peekaboo CLI nicht — stützt den Verdacht auf einen Transkriptionsfehler, löst ihn aber nicht abschließend auf.
