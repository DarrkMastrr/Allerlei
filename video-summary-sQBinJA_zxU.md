# "Claude Code vs. Claude Co-Work"

**Kanal:** Prompt mich mal
**URL:** https://www.youtube.com/watch?v=sQBinJA_zxU
**Länge:** 19:05
**Zusammenfassung erstellt:** 2026-07-04

---

## Vom reaktiven Chat zum autonomen Kollegen

- Bisherige KI-Tools waren rein reaktiv: Prompt rein, Antwort raus, System stoppt danach ("Ära der reinen Assistenz")
- Agentische Systeme arbeiten dagegen auf Task-Ebene statt nur auf Wort-Ebene (Next-Token-Vorhersage) — man gibt ein Endziel vor, das System findet den Weg selbstständig
- Der zentrale Mechanismus heißt "Agent Loop" und läuft in vier Phasen:
  1. **Kontextualisierung** — das Modell "schaut sich um" (z.B. `ls`, Grep) bevor es irgendetwas tut
  2. **Planung** — der Agent erstellt ein internes Dokument (JSON), zerlegt die Hauptaufgabe in einen Baum von Subtasks und berechnet Abhängigkeiten ("dynamic task routing")
  3. **Ausführung** — Dateien öffnen, schreiben, speichern
  4. **Validierung** — der Agent führt Code selbst aus, liest Fehlermeldungen/Crashes und korrigiert sich eigenständig, ohne dass der Mensch die Fehlermeldung manuell zurückkopieren muss

## Zwei Werkzeuge, zwei Philosophien

**Claude Code**
- Läuft direkt im Terminal, wirkt archaisch, hat aber vollen Systemzugriff
- Kann tausende Dateien in Projektordnern blitzschnell indexieren, Git-Kommandos ausführen, Netzwerkanfragen stellen, Datenbanken aufsetzen
- Beispiel: Aus einem rohen Ordner mit Audio-Transkripten baut es selbstständig eine Suchmaschine — erkennt, dass Vector Embeddings nötig sind, schreibt ein Python-Skript, entscheidet sich für PostgreSQL, richtet Docker ein, baut ein Web-Frontend
- Sehr ressourcenschonend/token-effizient, da keine grafische Oberfläche geladen wird — wichtig, da ein Agent-Loop teils 50-100 Iterationen braucht

**Claude Cowork**
- Nicht zum Software-Bauen gedacht, sondern zur Orchestrierung bestehender Alltags-Workflows
- Hat ein persistentes Gedächtnis: speichert Kontext aus früheren Gesprächen, offenen Dokumenten und verbundenen Tools in einem "semantischen Graphen"
- Beispiele: Newsletter direkt im Mailing-Tool (z.B. Klaviyo) aufsetzen ohne das Tool je geöffnet zu haben; Download-Ordner automatisch nach Projekten sortieren (Bilderkennung + PDF-Texterkennung); aus einem technischen Datenblatt parallel unterschiedlich zugeschnittene E-Mails für verschiedene Zielgruppen generieren

Fazit der Hosts: Code ist der "Maschinenraum", Cowork die "Chefetage".

## Skills, MCP und Progressive Disclosure

- **Skills** sind keine simplen Custom-Instructions, sondern echte lokale Ordner mit strukturierten Markdown-Dateien und kleinen Skripten — quasi das maschinenlesbare Firmenhandbuch
- Problem: begrenztes Kontextfenster — man kann nicht bei jedem Prompt das komplette Firmenhandbuch mitgeben
- Lösung: **Progressive Disclosure** — das System sucht per semantischer Suche im Hintergrund nur die eine passende Skill-Datei heraus und lädt nur diese ins aktive Gedächtnis
- **MCP (Model Context Protocol)** verbindet Skills mit der realen Welt, indem es KI-Absichten in konkrete API-Aufrufe übersetzt. Analogie: MCP ist der Autoschlüssel, die Skill ist die Fahrstunde

## Grenzen und Risiken

- **Website-Crawling**: Bot-Schutzmaßnahmen (z.B. Cloudflare) blockieren Agenten zuverlässig
- **Sicherheit/Governance**: Voller Terminalzugriff ist gefährlich (Beispiel `rm -rf`); nötig sind Guardrails, Sandboxes/isolierte Container und ein "Human in the Loop" bei kritischen Aktionen
- **Vendor-Lock-in**: Wer hunderte Skills/MCP-Interfaces speziell für Anthropic/Claude schreibt, bindet sich stark an einen Anbieter
- **Vibecoding-Warnung**: Vage, unstrukturierte Prompts führen zu unstrukturiertem "Spaghetticode"

## Neue Arbeitsteilung: Mensch als Architekt

- Empfehlung: erst eine Konzeptphase mit dem Agenten durchlaufen, bevor die eigentliche Implementierung freigegeben wird
- Der Mensch bleibt Architekt; die KI wird zum Handwerker, der erst nach Plan-Freigabe tausende Zeilen Code schreibt
- Perspektivischer Ausblick: Reine Ausführungsfähigkeit wird zur Commodity; die wertvollste Fähigkeit wird intellektuelle Präzision

---

## Kernbotschaft
KI-Werkzeuge verlassen die rein reaktive Chat-Phase und werden zu autonomen, aufgabenbasierten Agenten mit einem klar definierten vierphasigen Loop (Kontext, Planung, Ausführung, Validierung). Claude Code (Terminal, für tiefe technische Eingriffe) und Claude Cowork (persistentes Gedächtnis, für alltägliche Büro-Workflows) bedienen dabei zwei unterschiedliche Philosophien, werden aber beide durch Skills (Firmenwissen) und MCP (Werkzeugzugriff) ergänzt.

## Themen-Tags
Agentic Coding, Claude Code, Claude Cowork, MCP, Skills, Automatisierung, KI-Sicherheit, Vendor-Lock-in

## Zu prüfen (falls zutreffend)
- Behauptung, dass ein Agent-Loop teils "50 oder 100 Iterationen" braucht, um einen hartnäckigen Bug zu finden
- Aussage, dass Claude Cowork Kontext aus früheren Gesprächen, offenen Dokumenten und verbundenen Tools in einem "semantischen Graphen" speichert
- Konkrete Feature-Beschreibungen von Claude Cowork gegen offizielle Anthropic-Dokumentation abgleichen
