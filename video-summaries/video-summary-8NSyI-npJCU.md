# "The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)"

**Kanal:** Jay E | RoboNuggets
**URL:** https://www.youtube.com/watch?v=8NSyI-npJCU
**Länge:** 21:38
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) — selber Kanal/Host (Jay, RoboNuggets), zeigt bereits denselben `/robo`-Skill mit `brandbook.html`/`brand.html` als Referenz-Skill sowie dieselbe CLAUDE.md-als-Router-Struktur (dort: ~57.000 Dateien, hier: ~60.600 Dateien im selben Workspace) — starke direkte Überschneidung, siehe "Zu prüfen". [claude-skills-ueberblick.md](../claude-skills-ueberblick.md), Abschnitt "Vier-Bereiche-Modell für Agent-Arbeit", für ein strukturell ähnliches, aber anders benanntes Vier-Bausteine-Schema eines anderen Kanals. [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) und [video-summary-UZr4lLHBKyo.md](video-summary-UZr4lLHBKyo.md) für weitere "Second Brain"/Vault-Konzepte anderer Creator.*

## Aufhänger und Host

Jay (Kanal "Jay E | RoboNuggets", laut Selbstauskunft über ein Jahrzehnt Markenarbeit, Master in Data Science, betreibt eine eigene AI-Business und -Community) präsentiert sein persönliches "Agentic OS" – ein Setup rund um Claude Code, das er anhand eines selbst erfundenen Ordnungsschemas namens **ARMS-Framework** erklärt. Verkaufsversprechen: Wer die vier ARMS-Bausteine richtig einrichtet, arbeite "besser als 99 % der anderen Agentic-AI-Nutzer".

## Das Dashboard "Rubric Agentic OS"

Gezeigt wird zuerst eine visuelle Kommandozentrale namens **Rubric** (Frame-Titel "RUBRIC Agentic OS", per Websuche als reales, eigenständiges Produkt aus dem RoboNuggets-Umfeld bestätigt, siehe Zu prüfen) mit Widgets für Kalender, E-Mail-Zusammenfassung (inkl. von Claude markierten wichtigen Mails), Micro-Apps, YouTube-Studio-Kennzahlen, einer "Skills Deck" (Skills mit wählbarem Modell/Effort-Level direkt aus dem Dashboard startbar) und einer Routinen-Übersicht. In der Bildmitte ein rotierendes Partikel-Diagramm, das beim Draufklicken zu einem zweiten, node-basierten "Second Brain"-Graphen wird (Kreis-/Force-/Hex-/Ring-Layouts, laut UI-Text "60.601 files"). Zwei weitere, andersfarbige Beispiel-Dashboards ("stropro Agentic OS", "Beetogreen Agentic OS") werden kurz gezeigt – Hinweis, dass Jay dieses Dashboard-Format offenbar auch für Kunden baut/verkauft ("if you're into AI consulting … creating something like this for a client is also a service you can package and sell").

## Das ARMS-Framework

Kernstruktur (als Pyramide gezeichnet, von unten nach oben): **Skills → Memory → Routines → Apps**. Jay empfiehlt, die vier Bausteine in genau dieser Reihenfolge zu lernen, und für jeden Baustein drei Ausbaustufen ("Level 1–3").

### Skills
- **Level 1:** vorgefertigte Anthropic-Skills (Claude-Desktop-App, Customize → Skills, z. B. `skill-creator`) oder eigene, einfache `skill.md`-Dateien. Faustregel: Aufgabe zweimal manuell gemacht → als Skill festhalten.
- **Level 2 – "Thin Skills, Rich References":** `skill.md` fungiert nur als Router zu weiteren Referenzdateien statt alles in eine Markdown-Datei zu packen. Demo: sein `/robo`-Skill-Ordner mit u. a. `brandbook.html`/`brand.html`, das Schriften und Farbpalette der eigenen Marke definiert.
- **Level 3 – headlose Ausführung:** Skills lassen sich über den Claude-Code-Befehl **`claude -p`** (per Websuche als reales, dokumentiertes Nicht-interaktiv-/Headless-Feature von Claude Code bestätigt) ohne offene Chat-Session auslösen, z. B. per Button im eigenen Dashboard. Im Frame sichtbar: `claude -p /clean-up --model fable --effort xhigh --permission-mode …`.

### Memory
- **Level 1:** reiner Dateidump – ein Workspace-Ordner ohne Struktur. Jay beschreibt, wie sein eigener "Robo"-Ordner unbemerkt auf ca. 60.000 Dateien anwuchs, bis Abruf und Plan-Verbrauch spürbar litten.
- **Level 2 – Router-Dateien + Dateibaum:** `CLAUDE.md` als zentraler Router, darunter Abteilungs-Router (Beispiel im Frame: `CONTENT.md`) mit Verweisen auf die jeweils relevanten Skills/Dateien statt klassischer Ordner-für-Menschen-Organisation.
- **Level 3 – visuelles "Second Brain":** derselbe node-basierte Graph wie im Dashboard, zum schnelleren Auffinden/Verstehen der Dateibeziehungen.

### Routines
- **Level 1 – lokale Routinen:** über die Claude-Code-Desktop-App (Sidebar "Routines") in natürlicher Sprache erstellt, laufen aber nur, während der eigene Rechner an ist. Demo: eine tägliche 8-Uhr-Routine "YouTube to Substack daily", die neue Kanal-Videos automatisch in einen Substack-Newsletter-Entwurf im eigenen Tonfall umwandelt.
- **Level 2 – dauerhaft laufend über Hermes:** Für 24/7-Betrieb nutzt Jay **Hermes** (bereits in [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) als reales Open-Source-Agentensystem von Nous Research bestätigt) auf einem eigenen Cloud-Rechner. Damit Hermes Zugriff auf dieselben Skills/Memory-Dateien wie die lokale Claude-Code-Installation hat, synchronisiert er beide Maschinen über **Syncthing** (reales, kostenloses Open-Source-Sync-Tool).
- **Level 3 ("Coming Soon"):** Jay spekuliert unverbindlich, dass Anthropic/OpenAI künftig eigene VPS-artige Cloud-Umgebungen für Claude Code/Codex anbieten könnten, sodass Sync-Tools wie Syncthing überflüssig würden – ausdrücklich als eigene Vermutung markiert, nicht als angekündigtes Feature.

### Applications
- **Level 1:** Connectors-Browser in der Claude-Desktop-App (Customize → Connectors: u. a. Slack, Notion, Microsoft 365, GitHub, Gmail, Google Calendar/Drive).
- **Level 2 – Connector-Suche per Skill:** ein selbstgebauter "search connectors"-Skill durchsucht das Web nach offiziellen oder community-gebauten CLI/MCP/API-Connectoren. Demo: Suche nach einem Adobe-Premiere-Pro-Connector, Ergebnis ist ein empfohlenes MCP-Repo auf GitHub.
- **Level 3 – eigene Connectoren/Apps bauen:** genutztes Werkzeug ist die **"CLI Printing Press"** von **Matt Van Horn** (per Websuche bestätigt: real existierendes Open-Source-Projekt, `github.com/mvanhorn/cli-printing-press`, printingpress.dev; Van Horn ist tatsächlich Mitgründer von Zimride/Lyft, Bio-Angabe im Video also korrekt). Jay nennt als eigene Beispiele Connectoren für MyFitnessPal und "School" (ohne Zeigen im Bild) sowie selbstgebaute Micro-Apps: eine Bilder-/Video-Generierungs-Galerie, ein Teleprompter und ein Excalidraw-"Landing Pad" für von Claude erzeugte Artefakte.

## Werbliche Elemente

Mehrfach eingestreut: ein neunseitiger PDF-Guide zum ARMS-Framework (herunterladbar, per Prompt an Claude Code fütterbar) sowie wiederholte Werbung für die eigene RoboNuggets-Community (Claude-Living-Masterclass, Agents-as-a-Service-Kurs, Hermes-Agent-Masterclass) – strukturell vergleichbar mit der bereits in [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) dokumentierten Eigenwerbung desselben Kanals.

## Für den technischen Team-/Gruppenleiter

Direkt brauchbar sind zwei Ideen unabhängig vom Rubric-Markenprodukt: Erstens das **Router-Datei-Prinzip** (CLAUDE.md/Abteilungs-Router statt wachsendem, unstrukturiertem Dateidump) als konkrete Gegenmaßnahme, bevor ein Team-Workspace wie im Video auf 60.000+ Dateien anwächst und Abrufe/Kosten spürbar leiden. Zweitens der **`claude -p`-Headless-Mechanismus**, um Skills als Buttons in interne Tools/Dashboards statt nur im Chat einzubinden – ein Muster, das sich auf Team-interne Reporting- oder Freigabe-Workflows übertragen lässt, ohne dass jede Ausführung eine offene Chat-Session braucht. Die Hermes+Syncthing-Kombination für 24/7-Routinen ist dagegen mit spürbarem Infrastruktur-/Betriebsaufwand (eigener Cloud-Rechner, Sync-Setup, Sicherheitsverantwortung) verbunden und dürfte für die meisten Team-Kontexte eher ein Ausblick als ein kurzfristig empfehlenswerter Schritt sein.

---

## Kernbotschaft
Der Titel "the NEW Agentic OS standard" ist Marketing-Framing für Jays eigenes, unbelegtes Ordnungsschema (ARMS: Apps, Routines, Memory, Skills) und sein eigenes, real existierendes Dashboard-Produkt "Rubric" – kein offizieller Anthropic-Standard. Inhaltlich ist das Video aber eine solide, in drei Ausbaustufen pro Baustein gegliederte Anleitung, die mehrere bereits im Repo dokumentierte Einzelkonzepte desselben Kanals (CLAUDE.md als Router, `/robo`-Skill mit Rich References, siehe [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md)) zu einem größeren Gesamtbild zusammenführt und um neue, unabhängig verifizierte Bausteine ergänzt: den headlosen `claude -p`-Modus, das reale Hermes+Syncthing-Setup für Dauerbetrieb und die reale "CLI Printing Press" von Matt Van Horn für selbstgebaute Connectoren.

## Themen-Tags
ARMS-Framework, Agentic OS, Claude Code, Rubric, Skills, Memory, Routines, Applications, claude -p, Headless Mode, CLAUDE.md-Router, Second Brain, Hermes, Syncthing, CLI Printing Press, Matt Van Horn, Connectoren/MCP, RoboNuggets

## Zu prüfen
- **Starke direkte Überschneidung mit [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) (selber Kanal):** Der dort bereits dokumentierte `/robo`-Skill mit `brandbook.html` und die CLAUDE.md-als-Router-Struktur tauchen hier identisch wieder auf (nur die dortige Dateizahl von ~57.000 ist hier auf ~60.600 gewachsen – plausible Weiterentwicklung desselben Workspace über zwei Wochen, kein Widerspruch). Das "ARMS-Framework" wirkt wie eine spätere, umfassendere Verpackung von Konzepten, die Jay im August-Video bereits einzeln erklärt hatte.
- **"the NEW Agentic OS standard" per Websuche eingeordnet:** Es gibt keinen Beleg für einen offiziellen, herstellerübergreifenden "Standard" – **Rubric** ist ein reales, aber eigenes/kommerzielles Produkt aus Jays RoboNuggets-Umfeld (bestätigt: getrubric.app, "Command Centre for AI Agents"). Titel-Framing ist Eigenwerbung, keine erfundene Tatsache, aber überzeichnet.
- **`claude -p` (Headless-/Print-Modus) per Websuche bestätigt:** reales, dokumentiertes Claude-Code-Feature (`code.claude.com/docs/en/headless`), Nutzung im Video (Modell-/Effort-Flags, Permission-Mode) passt zur offiziellen Doku.
- **"CLI Printing Press" / Matt Van Horn per Websuche bestätigt:** reales Open-Source-Projekt (`github.com/mvanhorn/cli-printing-press`, printingpress.dev), Van Horn tatsächlich Mitgründer von Zimride/Lyft (heute u. a. CEO von June/Weber) – Bio-Angabe im Video korrekt.
- **Hermes erneut als reales Nous-Research-Agentensystem bestätigt** (siehe bereits [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md)) – hier zusätzlich mit dem konkreten Betriebsdetail "eigener Cloud-Rechner + Syncthing-Sync zum lokalen Workspace", das in den bisherigen Repo-Notizen zu Hermes noch nicht dokumentiert war.
- **Nicht unabhängig geprüft:** Jays persönliche Bio-Angaben (Jahrzehnt Markenarbeit, Data-Science-Master), die genaue Dateizahl "60.601" (nur aus dem UI-Screenshot übernommen) sowie die Behauptung, GrockBot sei "sehr teuer" – alles unbelegte Eigenaussagen des Hosts, nicht gegengecheckt.
- **Vier-Bausteine-Muster wiederholt sich kanalübergreifend:** Wie bereits in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) notiert, erfinden mehrere Creator eigene Vier-Teile-Schemata für Agent-Arbeit (dort: Harness/Context/Tool/Skill Engineering von Sascha Hoffmann; hier: Apps/Routines/Memory/Skills von Jay) – strukturell ähnliches Muster, aber unabhängig entstanden und terminologisch nicht deckungsgleich, kein Widerspruch.
- **Ablauf-Hinweis:** Native englische YouTube-Untertitel liefen ohne Probleme über yt-dlp (706 Segmente), kein Whisper-Fallback nötig. Die Zusammenfassung basiert auf dem vollständigen Transkript sowie allen 80 extrahierten Frames (bei 21:38 Länge mit dem im Skill-Report vermerkten Sparse-Coverage-Hinweis, aber die Frames waren durchgehend klar lesbar und deckten alle vier ARMS-Abschnitte sowie die Dashboard-/Screenshot-Demos ab).
