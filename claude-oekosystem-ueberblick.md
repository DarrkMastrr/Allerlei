# Claude-Ökosystem im Überblick: Code, Cowork, Features, Hacks

Quellen: [video-summary-sQBinJA_zxU.md](video-summary-sQBinJA_zxU.md) ("Claude Code vs. Claude Co-Work"), [video-summary-B_OqkMRFonM.md](video-summary-B_OqkMRFonM.md) ("Jede Claude Funktion erklärt"), [video-summary-wZeOwqmSw84.md](video-summary-wZeOwqmSw84.md) ("Learn 97% of Claude in Under 16 Minutes")

Drei Videos decken sich stark in ihrem Ziel — einen vollständigen Überblick über Claudes Funktionsumfang zu geben — nutzen aber unterschiedliche Gliederungen. Hier zusammengeführt statt dreifach redundant.

## Die zwei Philosophien: Claude Code vs. Claude Cowork

Aus sQBinJA_zxU, mit der treffendsten Kernaussage: **"Code ist der Maschinenraum, Cowork die Chefetage."**

- **Claude Code** — Terminal-basiert, voller Systemzugriff, für tiefe technische Eingriffe (Datenbanken aufsetzen, Git, Netzwerk). Sehr token-effizient, da keine grafische Oberfläche geladen wird — relevant, weil ein Agent-Loop teils 50-100 Iterationen brauchen kann.
- **Claude Cowork** — nicht zum Software-Bauen gedacht, sondern zur Orchestrierung von Alltags-Workflows (Mail, Kalender, Dateisortierung). Hat persistentes Gedächtnis über Sessions hinweg.

Der zugrundeliegende Mechanismus in beiden ist der **Agent Loop**: Kontextualisierung → Planung → Ausführung → Validierung.

## Die Bauteile, geordnet (Roboter-Metapher aus B_OqkMRFonM)

**Arbeitsplatz** — Workspace-Ordner, Claude.md (projektspezifisch), globale Anweisungen (app-weit), Projects (Ordner mit eigenem Memory/Kontext)

**Gehirn** — Memory (Langzeitgedächtnis, automatisch + manuell), Kontextfenster (Kurzzeitgedächtnis, für neue große Aufgaben lieber neuen Chat starten), Extended Thinking (mehr Nachdenkzeit gegen mehr Nutzungskontingent)

**Augen/Sensorik** — Multimodal (Screenshots, PDFs, Tabellen; kein Video laut Video), Websuche, Recherche (Deep-Research-artige Reports mit Quellen), Connectors (Gmail, Calendar, Notion, Slack), MCP (die offene Schnittstelle dahinter — "der USB-Anschluss für KI-Tools")

**Hände** — Artifacts (interaktive Mini-Apps im Chat), Chrome-Erweiterung (Browser-Steuerung), Computer Use (volle Rechnersteuerung, laut beiden Videos noch nicht sehr schnell)

**Autopilot** — Skills (wiederverwendbare Arbeitsabläufe, laut B_OqkMRFonM "der wichtigste Punkt"), Slash-Commands (Skill-Trigger), Plugins (Skill-Bündel), Scheduled Tasks/Automations, Dispatch Mode (Mobile → Desktop-Steuerung)

## Ergänzende Hacks aus wZeOwqmSw84 (nicht in den anderen beiden enthalten)

- **Memory Import** — ChatGPT-Verlauf/Präferenzen exportieren und in Claude importieren
- **Model Selector** — Haiku (schnell/günstig) vs. Sonnet (Alltag) vs. Opus (komplexe Analysen), alternativ "Adaptive Thinking"
- **Voice Mode** — Diktieren statt Tippen
- **Claude Channels** — Anbindung an iMessage/Telegram/Discord (nicht gegengecheckt)
- **Claude Design** (claude.ai/design) — Pitch-Decks, Landingpages, Mockups, Motion Graphics, mit Adobe-Partnerschaft (nicht gegengecheckt)

## Praktische Einordnung

Skills sind laut sQBinJA_zxU technisch mehr als Custom Instructions: echte lokale Ordner mit Markdown + Skripten. Das Kontextfenster-Problem wird über **Progressive Disclosure** gelöst — nur die per semantischer Suche passende Skill-Datei wird geladen, nicht das ganze "Firmenhandbuch" auf einmal.

## Offene Fragen (nicht gegengecheckt)
- Genaue aktuelle Modellnamen/-versionen, wie in den Videos gezeigt (Screenshots sind Momentaufnahmen)
- Existenz/Funktionsweise von "Claude Dispatch", "Claude Channels" und "Claude Design" als eigenständige, benannte Produktfeatures — Videos könnten informelle Namen für tatsächliche Anthropic-Features verwenden
- Wissensstand-Cutoff "Mai 2025", den B_OqkMRFonM nennt
