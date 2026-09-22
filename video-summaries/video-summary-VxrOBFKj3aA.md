# "#182 News: AGI mit GPT-6 Astra, Snickers für AI, Kimi nutzt heimlich Claude, iPhone Duo, OpenMouse"

**Kanal:** todo:cast Developer Podcast
**URL:** https://www.youtube.com/watch?v=VxrOBFKj3aA
**Länge:** 57:00
**Zusammenfassung erstellt:** 2026-09-22

---

*Siehe auch: [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md) (ARC-AGI-3-Harness-Widerspruch bereits dokumentiert, passt exakt), [ki-risiko-warnungen.md](../ki-risiko-warnungen.md) (Jacob-Coxon-Kündigung bereits dokumentiert), [video-summary-qLju_dxuuVs.md](video-summary-qLju_dxuuVs.md) (Coxon/Pachocki-Einordnung), [video-summary-9lyg9m8D3q0.md](video-summary-9lyg9m8D3q0.md) (Astra-Pause, Model 2), [video-summary-TpVwEDF-p04.md](video-summary-TpVwEDF-p04.md) (nennt denselben Pacing-Brief).*

**Hinweis zum Ablauf:** Native englische YouTube-Untertitel lagen vor (automatisch übersetzt/generiert, Kanal und Sprecher sind deutsch, Untertitel-Spur aber Englisch), Whisper wurde nicht gebraucht. Alle 80 Frames wurden gesichtet (Upload: 14.09.2026, laut Metadaten). Format: reines Talking-Head-Podcast-Interview zwischen zwei Sprechern (Split-Screen), **keinerlei eingeblendete Grafiken, Charts oder Text** in den gesichteten Frames — die im Aufhänger/Intro angeteaserte Geschichte über "Kimi nutzt heimlich Claude" taucht im gesamten Transkript nicht mehr auf (siehe Zu prüfen). Die beiden Sprecher: Malte Lantin (Strategic Solutions Engineer bei GitHub) und ein zweiter Sprecher, der sich als "Director for AI and Cloud" beim E-Commerce-Softwareunternehmen JTL vorstellt (Name im Transkript nicht klar verständlich, vermutlich Robin-Manuel Thiel laut Kanalkontext).

## GPT-6 Astra und die "AGI"-Debatte (0:00–10:00)

- GPT-6 Astra wird als großer Sprung beschrieben, besonders bei Computer-Use (3D-Tools wie Blender/Unreal Engine, Spieleentwicklung in Roblox Studio/Unity). Ein Sprecher demonstriert, ein kleines Roblox-Spiel mit ChatGPT „Work"-Modus gebaut zu haben.
- Nvidia-CEO Jensen Huang postete auf X: "AGI has arrived" — von den Podcastern als überwiegend Marketing eingeordnet.
- Der ARC-AGI-3-Benchmark: Astra erreicht "99-irgendwas Prozent", aber nur mit OpenAIs eigenem Codex-Harness; ohne diesen liegt der Wert bei nur 63%. Die Podcaster kritisieren, dass ARC-AGI diesen Harness-unterstützten Wert überhaupt veröffentlicht, weil das kein fairer Modellvergleich mehr sei.
- OpenAI hat den $200-Pro-Plan wegen Überlastung durch Astra-Nachfrage pausiert (keine neuen Anmeldungen/Upgrades).

## Anthropic Fable/Mythos 5.1 und Datenspeicherung (10:00–17:00)

- Anthropic habe mit Fable 5.1 und Mythos 5.1 nachgezogen, vor allem beim Preis (mehr Leistung fürs gleiche Geld).
- Neu: Möglichkeit, Data Retention (bisher 30 Tage auf Anthropic-Servern) für Enterprise-Kunden selbst zu hosten — als Reaktion auf Kritik, v. a. aus Europa. "Know Your Customer" wird als eigentlicher Grund genannt: Anthropic will wissen, wer über die API zugreift.

## KI-Sicherheitsdebatte: Amodei-Brief, Kongress-Anfrage, Hubinger/Coxon (17:00–24:00)

- Dario Amodei (Anthropic-CEO) habe "diese Woche" einen offenen Brief veröffentlicht, der ein Innehalten bei noch leistungsfähigeren/schnelleren Modellen vorschlägt, bis belastbare Sicherheitsmaßnahmen existieren. Elon Musk repostete zustimmend ("Dario is right").
- OpenAI habe den US-Kongress gefragt, ob ein industrieweites Verlangsamen überhaupt rechtlich durchsetzbar wäre.
- Bezug auf einen ehemaligen Anthropic-Mitarbeiter, der das Unternehmen aus Sorge über die Risiken verlassen habe (Kündigung, keine offizielle Dementierung, mehrere aktive Mitarbeiter hätten sich angeschlossen) — passt zu Jacob Coxon (9.9.2026, im Repo bereits bestätigt).
- Namentlich genannt: "Even Hubinger" (Verhörer für Evan Hubinger), Alignment Lead bei Anthropic, mit einer öffentlich genannten Zahl von über 10% Wahrscheinlichkeit, dass KI die Menschheit auslöscht.
- Die Podcaster äußern offen Skepsis, ob hinter dem Slowdown-Aufruf nicht auch finanzielle Motive stecken (Anthropic vor möglichem IPO, OpenAI vor IPO 2027, Musk "hinkt hinterher").

## Meta Muse Code, Cognition SWE-2, offene Modelle (24:00–30:00)

- Meta positioniert Muse Code als günstigen Terminal-Coding-Agenten (ca. $50 für vergleichbare Kontingente wie $200 bei der Konkurrenz); zwei Preisstufen, günstiger wenn man Meta Trainingsdaten überlässt.
- Cognition (Devin, Windsurf) hat SWE-2 vorgestellt, basierend auf Kimi K3 (Moonshot AI), mit Leistung nahe Fable 5.1 bei bis zu 64% geringeren Kosten (spezialisiert auf Coding, u. a. Frontier Code 1.1-Benchmark).
- GLM 5.3 und DeepSeek V4.1 sind jetzt auch als "Flash"-Version verfügbar (offene Gewichte, MoE-Architektur; DeepSeek lädt laut Podcast nur ca. 16 Mrd. von mehreren hundert Milliarden Parametern pro Anfrage).
- OpenClaw (selbst gehosteter Agent) hat Version 2 mit Multiplayer-Modus, Channel-Struktur und tieferer MCP-Integration veröffentlicht; ein Sprecher berichtet von Update-Problemen (Neuinstallation nötig).

## Snickers-Marketingkampagne als Prompt-Injection (30:00–33:00)

- Snickers/Mars hat eine Website (digitalsnickers/snickers-Domain) mit einem versteckten HTML-Element gestartet, das als Prompt-Injection funktioniert: Ein Agent, der die Seite besucht, soll sich "wie nach einem Snickers" verhalten und Antworten schärfer/sorgfältiger geben. Laut Podcast funktioniert der Trick inzwischen nicht mehr zuverlässig (ChatGPT habe den Versuch als Prompt-Injection erkannt und explizit abgelehnt). Als reiner Marketing-Gag eingeordnet, aber als PR-Erfolg gewürdigt.

## Shopify, Notion, AGENTS.md und GitHub Agentic Workflows (33:00–41:00)

- Shopify und Notion wollen ihre mobilen Apps von React Native auf native Implementierungen umstellen — laut Podcast auch deshalb machbar, weil Coding-Agenten den Mehraufwand für mehrere native Plattformen abfedern.
- Shopify-CEO Tobias Lütke erwägt laut eigenem X-Post, Claude Code im Unternehmen zu verbieten, bis Anthropic das herstellerübergreifende AGENTS.md-Format unterstützt (Claude Code nutzt bisher eine eigene CLAUDE.md-Datei).
- GitHub hat "Agentic Workflows" vorgestellt: GitHub-Actions-ähnliche, aber promptbasierte (statt YAML-Schritt-für-Schritt) Automatisierungen mit eingebautem Sandboxing und Secret-Management, auslösbar per Trigger (neues Issue, PR, Zeitplan).

## Europäische digitale Souveränität (41:00–43:00)

- Die Schwarz-Gruppe (Mutterkonzern von Lidl/Kaufland) investiert laut Podcast 5,5 Mrd. US-Dollar (in Quellen: 5,5–5,6 Mrd. Euro) in ein weiteres Rechenzentrum bei Rostock, zusätzlich zu einem früheren 11-Mrd.-Projekt.
- Mistral habe erneut rund 3 Mrd. an Finanzierung erhalten.
- Die Schweiz starte ein Experiment, von Microsoft 365 auf lokal hostbare Alternativen umzusteigen.
- Weitere genannte europäische Anbieter: StackIT, T-Systems, Ionos, Hetzner.

## OpenAI Agents API und Microsoft/Rust (43:00–47:00)

- OpenAI hat die "Agents API" vorgestellt: ein vollständig gemanagter Agenten-Service (inkl. Sandbox) in OpenAIs eigener Infrastruktur, primär für interne Unternehmensagenten gedacht.
- Microsoft hat Rust intern zur Tier-1-Sprache erklärt, gleichrangig mit C++, C# und TypeScript, mit Verweis auf Speichersicherheit bei gleichzeitig hoher Performance.

## Shopify kauft Tailwind Labs, Apple-Neuigkeiten (47:00–52:00)

- Shopify hat Tailwind Labs (Tailwind CSS) übernommen; das Kern-Framework bleibt laut Ankündigung MIT-lizenziert und Open Source.
- Apple erlaubt Entwicklern künftig, Intel-Support für ihre Mac-Apps optional wegzulassen.
- iPhone Duo (Apples faltbares Gerät): Die Podcaster sehen es eher als iPad-Mini-Ersatz denn als Telefon-Ersatz, kritisieren Dicke/Formfaktor, verweisen auf Multitasking-Demos (z. B. Netflix-App im Laptop-Modus) und betonen, dass Entwickler ihre Apps für den neuen Formfaktor anpassen sollten (kein eigenes iPadOS, aber Split-View-artige Layouts möglich).

## OpenMouse / OpenLogi und Filmtipp (52:00–57:00)

- Frustration über Hersteller-Bloatware (konkret: Logitech Options+, ca. 300 MB RAM, Konto-Pflicht, gelegentliche Ausfälle durch abgelaufene Zertifikate) habe zu zwei Open-Source-Projekten geführt: OpenMouse 1.0 (herstellerunabhängige Web-Oberfläche für Maus-Einstellungen) und ein Projekt namens "openlogi" (Nachbau des Logitech-Treibers ohne Logitech-Software).
- Filmtipp zum Schluss: "The Story of VS Code", eine ca. 90-minütige offizielle Dokumentation zur Entstehungsgeschichte von VS Code, kostenlos auf YouTube.

## Einordnung

Die im Video selbst überprüfbaren Fakten sind überwiegend korrekt und decken sich mit unabhängigen Quellen (siehe Zu prüfen): der ARC-AGI-3-Harness-Unterschied (63% vs. 99,x%) ist im Repo bereits mit denselben Zahlen dokumentiert, die OpenAI-Pro-Plan-Pause, Amodeis Brief vom 12.9., Microsofts Rust-Tier-1-Ankündigung, die Schwarz-Gruppen-Investition und die Shopify-Tailwind-Übernahme sind alle unabhängig bestätigbar und stimmen in den Kernzahlen. Auffällig ist der Bruch zwischen Ankündigung und Inhalt: Der Titel und das Intro versprechen eine Geschichte über "Kimi K3, das heimlich Anfragen an Claude weiterleitet" — diese Geschichte kommt im ganzen Transkript nicht vor (siehe Zu prüfen). Insgesamt ein informationsdichter, meinungsstarker News-Recap ohne Bildmaterial zur Untermauerung; die Einordnungen der beiden Sprecher (z. B. Skepsis gegenüber Marketing-Framing von "AGI", Verdacht auf finanzielle Motive hinter Sicherheits-Slowdown-Forderungen) sind erkennbar eigene Meinung, nicht als Fakten präsentiert.

## Für den technischen Team-Lead

- **AGENTS.md-Konflikt konkret relevant:** Wer im Team mehrere Coding-Agenten (Claude Code, Copilot, Codex, OpenCode) parallel einsetzt, sollte die AGENTS.md-vs-CLAUDE.md-Fragmentierung im Auge behalten — Shopifys öffentlicher Unmut könnte Druck auf Anthropic erhöhen, das Format zu unterstützen.
- **GitHub Agentic Workflows** ist für Gruppenleiter mit GitHub-Infrastruktur direkt einsetzbar: promptbasierte, sandboxed Automatisierung (z. B. Doku-Drift-Erkennung bei PRs, Issue-Validierung) ohne eigene Runner-/Secret-Verwaltung – konkretes Beispiel im Video: automatische Prüfung, ob ein PR undokumentierte Änderungen einführt oder Vorentscheidungen widerspricht.
- **ARC-AGI-3-Zahlen mit Vorsicht kommunizieren:** Die 99%-Zahl für Astra ist harness-abhängig (Codex-Harness von OpenAI selbst) und nicht als reine Modellfähigkeit zu verstehen — wichtig, falls im Team Benchmark-Vergleiche für Tool-Entscheidungen herangezogen werden. Deckt sich mit der bereits im Repo dokumentierten Einordnung.
- **Snickers-Prompt-Injection als Lehrbeispiel:** Gute, leicht erklärbare Illustration für Awareness-Schulungen, wie Prompt-Injection über versteckte HTML-Elemente funktioniert und wie moderne Modelle teils schon dagegen resistent sind.
- **Kostendruck bei Coding-Agenten sinkt:** Meta Muse Code, Cognition SWE-2 und die Fable/Mythos-5.1-Preissenkung zeigen einen klaren Trend zu günstigeren, spezialisierten Coding-Modellen — relevant für Tooling-Budget-Entscheidungen im Team.
- **OpenMouse/openlogi:** Konkreter, kleiner Produktivitäts-Tipp für alle im Team mit Logitech- oder anderer Bloatware-Maus-Software.

---

## Kernbotschaft

Ein 57-minütiger deutschsprachiger News-Recap-Podcast (reines Talking-Head-Format, keine Grafiken) behandelt in dichter Folge rund 15 Kurzmeldungen aus zwei Wochen KI- und Entwicklerwelt: GPT-6 Astras Computer-Use-Fähigkeiten und die umstrittene 99%-ARC-AGI-3-Zahl (nur mit OpenAIs eigenem Harness erreicht, sonst 63%), Anthropics Fable/Mythos-5.1-Update mit selbst hostbarer Datenspeicherung, eine hitzige KI-Sicherheitsdebatte um Dario Amodeis Slowdown-Brief, die Kündigung eines Anthropic-Mitarbeiters und eine öffentlich genannte >10%-Auslöschungswahrscheinlichkeit durch den Alignment Lead, günstigere Coding-Agenten von Meta und Cognition, eine Snickers-Marketingkampagne per Prompt-Injection, Shopifys Drohung, Claude Code wegen fehlender AGENTS.md-Unterstützung zu verbannen, GitHub Agentic Workflows, milliardenschwere europäische Rechenzentrums-Investitionen, Microsofts Rust-Tier-1-Status, Shopifys Tailwind-Übernahme, Apples iPhone Duo sowie zwei Open-Source-Alternativen zu Logitechs Maustreiber-Software. Die überprüften Fakten stimmen weitgehend mit unabhängigen Quellen überein; auffällig ist, dass die im Titel/Intro angekündigte "Kimi nutzt heimlich Claude"-Geschichte im eigentlichen Gespräch nicht mehr vorkommt.

## Themen-Tags

GPT-6 Astra, ARC-AGI-3, AGI, OpenAI, Codex, ChatGPT Pro, Anthropic, Fable 5.1, Mythos 5.1, Data Retention, Dario Amodei, Pacing the Frontier, Evan Hubinger, Jacob Coxon, KI-Sicherheit, Existenzielles Risiko, Meta Muse Code, Cognition SWE-2, Kimi K3, GLM 5.3, DeepSeek V4.1, OpenClaw, Snickers, Prompt Injection, Shopify, Notion, React Native, AGENTS.md, CLAUDE.md, GitHub Agentic Workflows, Digitale Souveränität, Schwarz Gruppe, Mistral, StackIT, OpenAI Agents API, Microsoft Rust Tier-1, Tailwind CSS, Apple iPhone Duo, Intel-Support, OpenMouse, VS Code Dokumentation, todo:cast

## Zu prüfen

- **ARC-AGI-3-Zahlen (63% vs. 99%) per WebSearch bestätigt:** ARC Prize selbst bestätigt 62,7% im neutralen Standard-Harness vs. 99,9% mit OpenAIs providereigenem Adapter-Harness (arcprize.org/blog/astra, X-Post @arcprize). Deckt sich mit den bereits im Repo dokumentierten Zahlen in [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md). **Kein Widerspruch, sondern Bestätigung.**
- **OpenAI-Pro-Plan-Pause per WebSearch bestätigt:** OpenAI pausierte ab 10.9.2026 neue Anmeldungen/Upgrades für den $200-ChatGPT-Pro-Plan wegen Astra-bedingter Serverlast (TechCrunch, Fortune, CIO, Computerworld, übereinstimmend).
- **Dario Amodeis Brief per WebSearch bestätigt und präzisiert:** Am 12.9.2026 veröffentlichte Amodei einen ca. 3.800 Wörter langen Essay, der ein "Pacing" (Verlangsamen) der Fähigkeitsentwicklung fordert; Elon Musk, Demis Hassabis und Sam Altman reagierten zustimmend (Gizmodo, Boston Globe). **Wichtig:** Dies ist ein separates Ereignis vom früheren "Pacing the Frontier"-Mitarbeiterbrief (28.7.2026, ca. 1.300–1.324 Unterschriften), der bereits in [video-summary-TpVwEDF-p04.md](video-summary-TpVwEDF-p04.md) und [video-summary-qLju_dxuuVs.md](video-summary-qLju_dxuuVs.md) dokumentiert ist. Das Video im aktuellen Task unterscheidet die beiden Ereignisse nicht klar und könnte bei Hörern den Eindruck erwecken, es handle sich um denselben Brief — hier eine neue, eigenständige Wortmeldung des CEOs selbst, sieben Wochen später.
- **Jacob Coxon / Evan Hubinger per WebSearch bestätigt:** Coxons Kündigung (9.9.2026) ist bereits in [ki-risiko-warnungen.md](../ki-risiko-warnungen.md) dokumentiert. Neu bestätigt: Evan Hubinger (Alignment-Science-Lead bei Anthropic, weiterhin dort tätig, keine Kündigung) postete daraufhin öffentlich eine persönliche Einschätzung von >10% Wahrscheinlichkeit, dass KI innerhalb eines Jahrzehnts die Menschheit auslöscht — ausdrücklich seine private Meinung, keine offizielle Anthropic-Position (CNBC, CBS News, AI Weekly). Das Video stellt die Herkunft der Zahl richtig dar (Alignment Lead, nicht CEO), der Name wird im Transkript nur als "Even Hubinger" verhört.
- **Microsoft-Rust-Tier-1 per WebSearch bestätigt:** Ankündigung vom 11.9.2026 auf der RustConf, Rust gleichrangig mit C++, C# und TypeScript für interne Microsoft-Entwicklung (Rust Foundation, Slashdot, The Register).
- **Schwarz-Gruppe-Rechenzentrum per WebSearch bestätigt, Zahl leicht abweichend:** Mehrere deutsche Quellen (ZDF, Tagesspiegel, Handelsblatt, Ostdeutsche Zeitung) nennen 5,6 Mrd. Euro (nicht Dollar) für das Rechenzentrum in Dummerstorf bei Rostock, geplante Fertigstellung 2033. Das Video sagt "5,5 Milliarden Dollar" — nahe an den 5,6 Mrd. Euro der Primärquellen, aber Währung und Nachkommastelle weichen leicht ab; keine grundsätzliche Falschmeldung.
- **Shopify/Tailwind-Übernahme per WebSearch bestätigt:** Akquisition am 9.9.2026, Tailwind-CSS-Kernframework bleibt MIT-lizenziert Open Source, Premium-Dienste (Tailwind Plus, ui.sh) stellen Neuanmeldungen ein (CMSWire, Dealroom, Seeking Alpha).
- **"Kimi nutzt heimlich Claude" — im Transkript nicht auffindbar:** Titel und Intro kündigen diese Geschichte an ("scandal with Kimi K3, who apparently secretly forwarded requests to Claud[e]"), sie taucht aber im weiteren 57-minütigen Gespräch nicht mehr auf. Die Videobeschreibung verlinkt einen TechCrunch-Artikel ("Anthropic details distillation campaigns from Alibaba, Moonshot AI and DeepSeek", 10.9.2026), der thematisch passen könnte, aber im gesprochenen Inhalt fehlt die Story komplett. Möglich: Schnittfehler, ausgelassenes Segment, oder die Untertitel-Spur hat einen Abschnitt verloren. Nicht per WebSearch verifiziert, ob und was inhaltlich dazu tatsächlich im Original-Upload gesagt wurde — für den Leser als offene Lücke markiert.
- **Zweiter Sprecher/Name nicht sicher identifiziert:** Die Automatik-Untertitel geben den Namen des zweiten Podcasters unklar wieder ("Robin Manuel Teel" o. ä.); nicht separat verifiziert.
- **Cross-Check mit bestehenden Notizen:** Keine inhaltlichen Widersprüche gefunden. Größte Überschneidung mit [gpt-6-astra-ueberblick.md](../gpt-6-astra-ueberblick.md) (ARC-AGI-3-Zahlen decken sich exakt) und [ki-risiko-warnungen.md](../ki-risiko-warnungen.md)/[video-summary-qLju_dxuuVs.md](video-summary-qLju_dxuuVs.md) (Coxon-Kündigung, Pacing-Brief-Kontext). Für Schwarz-Gruppe, Mistral-Funding, Shopify/Tailwind, Rust-Tier-1, Snickers-Kampagne, Meta Muse Code, Cognition SWE-2 und OpenMouse/openlogi gibt es im Repo bislang keine eigene Dokumentation — alles neue Themen ohne Widerspruchspotenzial.
