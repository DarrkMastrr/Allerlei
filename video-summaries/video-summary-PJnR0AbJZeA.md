# "Der EINZIGE Claude Code Kurs Den Du Brauchst (Von Null Zum KI-Profi)"

**Kanal:** Garrit Wilson (KI-Pionier Akademie / "AI Pioneer Academy")
**URL:** https://www.youtube.com/watch?v=PJnR0AbJZeA
**Länge:** 1:02:58
**Zusammenfassung erstellt:** 2026-08-08

---

*Hinweis zum Ablauf: Native Untertitel waren nur auf Englisch verfügbar (automatisch generiert/übersetzt, das Video selbst ist auf Deutsch). Die Transkription enthält durchgehende Fehltranskriptionen — "Claude Code" wird fast überall als "Cloud Code" erkannt, "Skool Community" (die reale Plattform Skool.com) als "Frechool"/"Freeschool Community", der Instruktor als "Garett/Garet/Gereck Wilson" statt Garrit Wilson. Namen wurden unten anhand der yt-dlp-Metadaten und der eingeblendeten Screenshots korrigiert. Zusätzlich: yt-dlp scheiterte zunächst mit YouTubes Bot-Check ("Sign in to confirm you're not a bot") — behoben durch ein globales `--force-ipv4` in der yt-dlp-Konfiguration, kein Problem des Videos selbst. Bei 63 Minuten Länge sind die 80 Frames sehr sparse verteilt (Standardwarnung des Watch-Skills bei >10-Minuten-Videos); die Zusammenfassung stützt sich primär auf das (vollständig gelesene) Transkript, Frames dienten zur Verifikation von UI/Screenshots.*

## Worum es geht

Ein als "Masterclass" angelegter Rundum-Kurs von Garrit Wilson (Psychologe, Data Scientist, seit 2022 selbstständig im Prompt-Engineering, Gründer der "AI Pioneer Academy"/KI-Pionier Akademie). Aufbau: kurzer Motivationsteil (warum jetzt einsteigen) → Installation → ein selbst entwickeltes "Workspace-Template" als Framework um Claude Code herum → Live-Demo (eine Landingpage komplett bauen lassen) → Kurzüberblick über vier fortgeschrittene Konzepte (Commands, Skills, Agents, MCP) → GitHub-Hosting des Workspace → Business-/Karriere-Pitch mit Einladung in seine kostenlose Skool-Community.

## 1. Warum-jetzt-Teil (erste ~5 Minuten)

Aufhänger: Ein Zitat/Artikel-Screenshot von Anthropic-CEO Dario Amodei ("AI may cause unusually painful disruption to jobs") sowie ein Diagramm zu gesunkener Nachfrage nach Freelance-Diensten seit ChatGPTs Release (Screenshot, laut Video bis ~31 % Rückgang, Datenstand bis Mai 2025). Dazu eine METR-artige Grafik zum "Zeithorizont" von KI-Modellen (autonome Aufgabenlänge), mit dem Vergleich GPT-3.5 (Nov. 2022, ~36 Sekunden) vs. Claude Opus 4.6 (~15 Stunden). Kernbild: Claude Code sei kein Chatbot mehr, sondern ein Agent, der Aufgaben eigenständig zu Ende bringt — die "Ferrari"-Metapher (mächtiges, aber ungewohntes Werkzeug) zieht sich durchs ganze Video.

## 2. Installation & IDE

Verweis auf die offizielle Claude-Code-Quickstart-Doku (`docs.claude.com`, im Frame sichtbar: `npm install -g @anthropic-ai/claude-code` bzw. die plattformspezifischen curl/PowerShell-Installer) statt eigener Anleitung — bei Problemen wird empfohlen, sich per ChatGPT durchs Setup helfen zu lassen. Als IDE empfiehlt er wahlweise **Google Antigravity** (Googles neue agentische IDE, die er selbst nutzt, im Video durchgehend im Einsatz) oder **VS Code** — ausdrücklich ohne Präferenz zwischen beiden.

## 3. Das eigene "Workspace-Template" (Kernstück des Kurses)

Statt eines leeren Projektordners nutzt Wilson ein selbst gebautes, wiederverwendbares Vorlagenverzeichnis (kostenlos über seine Community herunterladbar) mit fester Struktur:
- **`context/`** — vier Markdown-Dateien (u. a. Business Info, Personal Info) mit Hintergrundinformationen zu Person/Unternehmen, damit Claude Code nicht bei jeder neuen Session bei null anfängt
- **`reference/`** — Ablage für Bild-/Logo-/Screenshot-Dateien, die Claude Code als visuellen Kontext einbeziehen soll
- **`planning/`** — wird automatisch mit den von Claude Code erzeugten Plan-Dokumenten befüllt
- **`CLAUDE.md`** — die von Anthropic vorgesehene, automatisch bei Sessionstart geladene Steuerdatei

Befüllt werden die Context-Dateien per **Whisper Flow** (Diktier-Tool, explizit ohne Affiliate-Interesse empfohlen): Man lässt sich von Claude Code gezielte Rückfragen stellen und beantwortet sie mündlich statt zu tippen.

## 4. Eigene Slash-Commands: `/prime`, `/create-plan`, `/shutdown`

Wichtig zur Einordnung: Das sind **selbst geschriebene** Custom Commands, keine eingebauten Claude-Code-Befehle (er sagt das im Video selbst — "die ersten vier sind meine").
- **`/prime`** — liest beim Sessionstart gezielt alle Dateien in `context/` plus `CLAUDE.md` und fasst zusammen, wer der Nutzer ist und worum es im Workspace geht (Analogie: "der Schlüssel im Zündschloss"). Wird als Muskelgedächtnis-Ritual am Anfang jeder Session verkauft. Funktioniert nur, wenn die IDE exakt auf Ordnerebene des Workspace geöffnet ist — sonst "Unknown skill"-Fehler (im Video als häufiger Anfängerfehler vom eigenen Live-Event genannt).
- **`/create-plan`** — erzeugt aus einer kurzen, ungefähren Anweisung (z. B. gesprochen statt getippt) einen sehr ausführlichen, mehrdimensionalen Plan (visuell/Copy/technisch), der vor Umsetzung geprüft werden kann, statt Claude Code direkt drauflosbauen zu lassen.
- **`/shutdown`** — räumt am Sessionende auf: scannt den Workspace, aktualisiert/konsolidiert Dokumente, fasst zusammen, was erledigt/offen ist.

## 5. Live-Demo: Landingpage bauen

Ziel: eine kostenlose Skool-Community bewerben. Ablauf: CLAUDE.md per Fragerunde befüllen → `/create-plan` → Plan sichten → Umsetzung freigeben (inkl. Demo von `--dangerously-skip-permissions`, mit ausdrücklicher Warnung: nur bei risikoarmen Aufgaben wie Website-Code, nicht bei destruktiven Dateioperationen) → Claude Code wählt eigenständig den Tech-Stack (Astro + Tailwind CSS, Hosting via Vercel) → erste Version mit sichtbaren Fehlern (falsches Logo, doppelte Elemente, nicht funktionierender Button) → eine weitere Iterationsrunde (~45–60 Min., im Video zeitgerafft) → fertiges Ergebnis.

## 6. Vier Konzepte im Schnelldurchlauf (explizit nicht vertieft, "sonst 6 Stunden Video")

- **Commands** — Slash-Befehle, "Single-Shot-Prompt" (Analogie zu ChatGPT-GPTs)
- **Skills** — mächtiger als reine Prompts, es gibt Marktplätze dafür (im Frame sichtbar: eine Seite "skillsmp"/"Agent Skills Marketplace" mit Zähler "400.856" Skills — Name/Zahl nicht unabhängig verifiziert). **Ausdrückliche Sicherheitswarnung**: Auf einem Marktplatz seien bereits Skills mit eingeschleuster Malware aufgetaucht, die den Agenten zu unerwünschten Aktionen anwies. Seine eigene Einschätzung: Im Alltag kaum nötig, Context + CLAUDE.md + Commands decken laut ihm "80 % der Fälle".
- **Agents/Subagents** — kurz erwähnt als Möglichkeit, spezialisierte Subagenten einzurichten (Beispiel: einer für Marktrecherche, einer fürs Reporting). Explizit relativiert: "Alle auf YouTube wollen dir verkaufen, dass du jetzt Agent Teams brauchst" — Pareto-80/20-Einordnung, für den Einstieg nicht nötig.
- **MCP-Server** — Standardschnittstelle zwischen Claude Code und externen Anwendungen. Praxisbeispiel: eine komplette n8n-Automatisierung, die Claude Code über MCP "one-shot" (beim ersten Versuch funktionierend) erstellt hat.

## 7. Workspace auf GitHub sichern

Motivation: Backup-Sicherheit ("was, wenn Laptop kaputtgeht/gestohlen wird"), nicht primär Versionierung als Argument. Ablauf: kostenloser GitHub-Account → `gh auth login` (per Terminal oder von Claude Code angeleitet) → Anweisung an Claude Code, den Workspace zu pushen → private Repos, Verlauf/History nutzbar zum Zurückspringen auf ältere Versionen.

## 8. Abschluss: Fazit & Business-Pitch

Zusammenfassung (Slide "Zusammengefasst"): Claude Code ist ein KI-Agent, der eigenständig plant & ausführt; es gibt online nichts, was man mit diesen Agenten nicht tun kann; die Kunst liegt im Context-Management; die Auswirkungen sind enorm — jetzt anfangen. Anschließend die "2 Realitäten"-Slide: Nachfrage nach den meisten (Wissensarbeiter-)Dienstleistungen werde dramatisch fallen, gleichzeitig die Nachfrage nach KI-Transformationspartnern drastisch steigen (Analogie: industrielle Revolution, Landwirte −97 %, Ingenieure +2000 %). Einladung in die kostenlose Skool-Community (Q&A alle zwei Wochen, Workspace-Template zum Download) als Einstieg in seine kostenpflichtige Akademie.

---

## Abgleich mit bestehenden Notizen im Repo

Dieses Video überschneidet sich stark mit bereits vorhandenem Material — hier die Einordnung:

**Redundant (nicht neu, nur andere Verpackung):**
- Die MCP-Definition ("Standardschnittstelle zwischen KI und externen Anwendungen") deckt sich wortwörtlich mit [mcp-ueberblick.md](../mcp-ueberblick.md) — keine neue Information.
- Skills als "mehr als reine Prompts", Marktplatz-Konzept, Slash-Commands als Trigger — bereits ausführlich in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) und [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) dokumentiert.
- CLAUDE.md als automatisch geladene Steuerdatei — Grundwissen, deckungsgleich mit [karpathy-claude-md-guidelines.md](../karpathy-claude-md-guidelines.md) und [ai-agent-workflow.md](../ai-agent-workflow.md).

**Genuinly neu / andere Perspektive:**
- Das konkrete, benannte **Workspace-Template mit `context/`/`reference`/`planning`-Unterordnern plus drei eigenen Slash-Commands (`/prime`, `/create-plan`, `/shutdown`)** ist eine sehr konkrete, praktische Umsetzung des Prinzips "vision.md neben CLAUDE.md" aus [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 3 — dort abstrakter beschrieben, hier als fertiges, kopierbares Muster gezeigt.
- Die **Sicherheitswarnung zu Malware in Skill-Marktplätzen** ist neu — taucht in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) bisher nicht auf und wäre ein sinnvoller Ergänzungspunkt dort (hier nur vermerkt, Datei absichtlich nicht editiert).
- Die **Whisper-Flow-Diktier-Workflow** zum Befüllen von Kontextdateien ist eine neue praktische Idee, die so in anderen Notizen nicht vorkommt.
- Die **GitHub-Backup-Argumentation für Workspaces** (Datenschutz/Ausfallsicherheit statt Versionierung als Hauptargument) ist ein neuer, pragmatischer Blickwinkel.

**Auffällige Lücke gegenüber bestehenden Notizen (kein Widerspruch, aber bemerkenswert):**
- **Plan Mode wird im gesamten Kurs nicht erwähnt.** [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 6 hebt Plan Mode (Boris Cherny: ~80 % der Sessions) als zentrales Werkzeug hervor; dieser Kurs ersetzt das faktisch komplett durch den eigenen `/create-plan`-Command plus manuelles Review — ein alternativer, aber unabhängig entstandener Ansatz zum gleichen Problem (Ergebnis vor Umsetzung prüfen).
- **Hooks werden nicht erwähnt** — keine Lücke gegenüber diesem Repo (auch dort bisher kein eigener Hooks-Artikel), aber auffällig für einen "Masterclass"-Anspruch.
- Ein leichter Stilkonflikt: [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 7 rät (nach Boris Cherny), CLAUDE.md **schlank** zu halten; dieser Kurs treibt das Gegenteil — möglichst viele, möglichst detaillierte Kontextdateien. Kein echter Widerspruch (unterschiedliche Anwendungsfälle: generischer Coding-Agent vs. persönlicher Business-Assistent), aber erwähnenswert, falls beide Ratschläge im selben Projekt kombiniert werden sollen.

**Kein inhaltlicher Widerspruch zu bereits verifizierten Fakten gefunden.** Die zentrale Zahlenbehauptung (Claude Opus 4.6 ≈ 15 Stunden autonomer Aufgabenhorizont) wurde stichprobenartig gegengecheckt und deckt sich mit unabhängig auffindbaren METR-Berichten (~14,5 Stunden bei 50 % Erfolgsrate, Stand Februar 2026) — die Rundung auf "15 Stunden" ist vertretbar. Das zitierte Dario-Amodei-Statement ("unusually painful disruption to jobs") ist ebenfalls real und stammt aus einem am 27.01.2026 veröffentlichten Essay (CNBC-Berichterstattung).

## Eignung für Teameinsteiger

Für den Zielleser (Hardware-Entwickler/technischer Teamleiter, der Claude Code selbst bereits nutzt) bringt dieses Video **persönlich wenig Neues** — die technischen Kernkonzepte sind hier bereits ausführlicher und präziser dokumentiert. Als **Onboarding-Material für Teammitglieder ohne Coding-Hintergrund** ist es dagegen gut geeignet: Der Kurs ist bewusst nicht-technisch gehalten ("du musst nicht programmieren können"), zeigt einen kompletten End-to-End-Workflow an einem greifbaren Beispiel (Website bauen) und vermittelt das Kontext-Management-Prinzip sehr anschaulich über die Workspace-Template-Idee. Abzuziehen sind die recht ausgedehnten Marketing-/Community-Pitch-Anteile (geschätzt 10–15 Minuten reine Werbung für die eigene, kostenpflichtige Akademie) sowie die fehlende Vertiefung von Plan Mode, Hooks und produktionsreifen Subagent-Setups — für reine Coding-Teams eher als motivierender Einstieg denn als technische Referenz zu empfehlen.

## Kernbotschaft
Der Kurs verpackt Standard-Claude-Code-Konzepte (CLAUDE.md, Slash-Commands, Skills, Subagents, MCP) in ein sehr konkretes, sofort kopierbares "Workspace-Template" mit eigenen Ritual-Commands (`/prime`, `/create-plan`, `/shutdown`) für Kontext-Management über Sessions hinweg — demonstriert End-to-End am Beispiel einer selbst gebauten Landingpage. Fachlich korrekt und mit einem plausiblen, unabhängig bestätigten Kernbeleg (METR-Zeithorizont, Amodei-Zitat), aber ohne Vertiefung von Plan Mode oder Hooks, und mit einem substanziellen Eigenwerbungs-/Community-Anteil am Ende.

## Themen-Tags
Claude Code, Onboarding/Einsteigerkurs, CLAUDE.md, Workspace-Template, Context-Engineering, Slash-Commands, Skills-Marktplatz, Subagents, MCP, Google Antigravity, GitHub-Hosting, Dario Amodei, METR Time Horizon, Business-Pitch

## Zu prüfen
- Konkrete Zahl "Upwork-Nachfrage seit Nov. 2022 um bis zu 31 % gefallen" — Screenshot im Video, nicht unabhängig nachrecherchiert.
- Konkrete Zahl "GPT-3.5 konnte im Nov. 2022 nur ~36-Sekunden-Aufgaben autonom lösen" — Screenshot/Grafik im Video, nicht unabhängig nachgerechnet (die Trendrichtung selbst — exponentiell wachsender Zeithorizont — ist über METR-Berichte gut belegt, der exakte Startwert nicht geprüft).
- Existenz/Seriosität der im Frame gezeigten Skill-Marktplatz-Seite "skillsmp" und die genannte Zahl "400.856 Skills" — nicht unabhängig verifiziert.
- Die konkrete Malware-in-Skills-Anekdote (welcher Marktplatz genau, wann) — im Video nur vage als "OpenPC" referenziert, nicht identifizierbar/gegengecheckt.
- Zahl "97 % Rückgang bei Landwirten / +2000 % bei Ingenieuren" (industrielle Revolution) — als grobe historische Illustration im Video genannt, nicht gegengecheckt.
- Genaue aktuelle Marktposition/Funktionsumfang von Google Antigravity als IDE — im Video nur als von ihm bevorzugtes, aber gleichwertiges Tool neben VS Code dargestellt, nicht weiter geprüft.
- "KI-Pionier Akademie"/Skool-Community-Mitgliederzahlen (Frame zeigt "2.000+ Mitglieder", "50+ Stunden Aufnahmen", "wöchentlich") — Eigenangaben auf der beworbenen Landingpage, nicht unabhängig verifiziert.
