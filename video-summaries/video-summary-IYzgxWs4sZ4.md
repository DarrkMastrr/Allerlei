# "KI-Videos haben eine GRENZE überschritten: DAS kann Seedance 2.5! + Claude Code & Codex Updates"

**Kanal:** Everlast AI (Host: Leonard Schmedding, mit Kollegen Phil und Marcel als Co-Presenter)
**URL:** https://www.youtube.com/watch?v=IYzgxWs4sZ4
**Länge:** 28:22
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) für den allgemeinen Claude-Funktionsüberblick.*

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429, die Zusammenfassung basiert auf dem Whisper-Fallback (Replicate, 403 transkribierte Segmente über 6 Audio-Chunks) plus 80 sparse verteilten Frames (Vollvideo-Modus, ca. alle 21s) über die vollen 28 Minuten. Der Whisper-Fallback verhörte den Host-Namen als "Leonhard Schwerding" — ein im Frame bei t=25:53 sichtbarer Tweet zeigt den korrekten Namen "Leonard M. Schmedding" (@derleomartin), auch der Kanal-Banner bei t=27:18 bestätigt "Everlast AI, 325.000 Abonnenten".

## Teil 1: Seedance 2.5 (kurz — für den Zielleser eher Kapazitäts-Marker als Kernthema)

ByteDances Video-Generierungsmodell Seedance 2.5 ist seit Kurzem global über die Plattform Dreamina verfügbar. Der Co-Host "Phil" testet es live:

- **Kernzahlen laut Video:** bis zu 50 multimodale Referenzen pro Generierung (30 Bilder/10 Videos/10 Audios laut Produktseite), native 4K angekündigt, bis zu 30 Sekunden pro Clip in einer Generierung, per "Long Video"-Funktion (automatische Verkettung mehrerer Clips im Hintergrund) bis zu 3 Minuten am Stück
- **Widerspruch im Video selbst:** Zu Beginn wird "natives 4K" als Ansage genannt (t=00:16), beim eigentlichen Live-Test sagt Phil dann aber explizit: "Zum Launch gibt es auch nur 480 oder 720p, also noch keine 1080 oder 4K" (t=02:45) — die 4K-Fähigkeit ist demnach (noch) nicht live nutzbar, nur angekündigt
- **Preis-Demo:** Ein 20-Sekunden-Clip mit 16 gleichzeitigen Referenzbildern (Charaktere, Fahrzeuge, Gegenstände) kostete im Test knapp 6 €; ein 3-Minuten-"Long Video" in 720p verbraucht mit 7.000 Credits mehr als den kompletten Standardplan (3.600 Credits) — dafür wäre der teurere "Advanced"-Plan nötig
- **Ergebnis des Live-Tests:** Alle 16 Referenzobjekte wurden erkennbar ins generierte Video eingebaut, laut Phil "sieht auch genauso aus wie in den Bildern" — visuell im Frame bei t=05:19 bis t=06:23 nachvollziehbar (Fantasy-Setting mit Ork, Samurai, Roboterhund etc., alle Referenzelemente wiedererkennbar)
- **Konkurrenz in derselben Woche:** MiniMax H3 (natives 2K, 15s, bis zu 15 Referenzen inkl. Audio) und Flux 3 von Black Forest Labs (deutsches Unternehmen; einziges Modell der drei, das Bild, Video UND Audio über dieselben Gewichte abdeckt, bis 20s)

**Plausibilitätscheck (durchgeführt):** Seedance 2.5 ist real. Laut mehreren unabhängigen Quellen (Hedra, TechTimes, MindStudio, Morphic) wurde es am 23. Juni 2026 auf der Volcano-Engine-FORCE-Konferenz angekündigt, der volle Trial-Center-/API-Zugang öffnete am 7. August 2026 — passt zeitlich exakt zum "gerade global verfügbar"-Framing des Videos. Die genannten Eckdaten (30s native Länge pro Pass, bis zu 50 Referenzen: 30 Bilder/10 Video/10 Audio, In-Video-Editing) decken sich mit den unabhängigen Produktbeschreibungen. "KI-Videos haben eine Grenze überschritten" ist als Marketing-Zuspitzung zu lesen — konkret neu ist vor allem die Referenzmenge (50 statt vorher 9 Bilder/3 Clips bei Seedance 2.0) und die native 30s-Generierung ohne Stitching.

Ein im Intro genanntes Detail — "nahtlos aus Claude Code heraus" Seedance-Videos erstellen (t=00:07) — wird im Video selbst **nicht gezeigt**: Die komplette Demo läuft über die Dreamina-Web-UI, nicht über ein Terminal/Claude Code. Recherche bestätigt aber, dass community-gebaute MCP-Server für Seedance-Anbindung an Claude Code existieren (z. B. auf Glama.ai, AceDataCloud) — die Behauptung ist also technisch plausibel, aber nicht das, was im Video tatsächlich demonstriert wird.

## Teil 2: Claude Code & Codex Updates (Kernabschnitt für den Zielleser)

### Opus 5: Medium-Reasoning-Effort schlägt Extra-High bei Coding-Benchmarks

Ein im Frame bei t=13:28 vollständig lesbarer Chart ("FrontierCode extended set: test-time compute scaling", Figure 8.4.B — Formatierung/Nummerierung deutet auf ein offizielles Anthropic-System-Card-Dokument hin) zeigt: Claude Opus 5 erreicht seinen besten Score (63,6 %) bei **Medium**-Reasoning-Effort, nicht bei High oder Max. Erklärung im Video (untermauert durch eingeblendeten Fließtext, vermutlich aus einem Blogartikel, t=13:50–14:16): Bei höherem Reasoning-Aufwand führt Opus 5 zusätzliche, nicht angeforderte Aufgaben aus und wird dafür in der Bewertung "bestraft" — tendiert also zu Over-Engineering, wenn man ihm mehr Denkzeit gibt. Praktische Empfehlung des Hosts: Für die meisten Agentic-Coding-Aufgaben Medium-Effort nutzen, Extra-High/Max nur gezielt bei Bedarf.

**Fact-Check (durchgeführt, bestätigt):** Mehrere unabhängige Tech-Blogs (Sitepoint, MindStudio, Vellum, MarkTechPost, AIToolsReview) bestätigen unabhängig voneinander genau diesen Befund aus Anthropics eigenen Opus-5-Benchmark-Daten: Peak-Performance auf FrontierCode bei Medium-Effort, Verschlechterung (und höhere Kosten) bei höheren Reasoning-Stufen. Die Video-Aussage ist damit korrekt wiedergegeben.

### GPT-5.6-Preissenkungen wirken sich direkt auf Codex-Kosten aus

Ein im Frame bei t=04:15 vollständig lesbarer OpenAI-Tweet-Screenshot bestätigt wörtlich: Preissenkung für GPT-5.6 Luna um 80 %, für GPT-5.6 Terra um 20 %, plus eine schnellere Option für GPT-5.6 Sol in der API. Zitat aus dem Tweet: *"Die niedrigeren Preise für Luna und Terra werden in der Abrechnung der Nutzung in Codex und ChatGPT Work berücksichtigt, sodass Ihre Nutzung weiter reicht."* — die Preissenkung betrifft also explizit auch Codex-Nutzer. Konkrete neue Preise laut Video: GPT-5.6 Luna ca. 20 Cent/Mio. Input-Token, ca. 1,20 €/Mio. Output-Token. Eingeordnet wird das mit einem Accuracy-vs.-Cost-Chart (t=04:37, Quelle vermutlich OpenAIs eigener Agent-Benchmark): GPT-5.6 Luna (xhigh) kommt an Opus 5 heran, bei laut Video ca. 17-fach günstigerem Preis — relevant speziell für den Einsatz günstigerer Modelle in Sub-Agent-Rollen.

**Fact-Check (durchgeführt):** Die grundsätzliche Preissenkung ist plausibel und passt zum allgemeinen Preisverfalltrend bei Frontier-Modellen; der Screenshot selbst ist die Primärquelle (echter OpenAI-Tweet, im Frame lesbar). Die genauen Rabatt-Prozentsätze wurden nicht per unabhängiger Zweitquelle gegengecheckt (kein separater Treffer außerhalb des Video-Screenshots gefunden) — siehe Zu prüfen.

### Buzz: Ein "Slack für Menschen und Agenten" mit Claude Code, Codex & Co.

Marcel demonstriert **Buzz**, eine neue Team-Chat-Plattform, die im Video akustisch wie "BAS" transkribiert wurde (Whisper-Fehler, im Frame bei t=00:43 als "Buzz Agent" eindeutig lesbar). Kernpunkte aus Demo und Frames:

- Optik/Bedienung stark an Slack angelehnt: Channels, Threads, Inbox, @-Erwähnungen von Agenten
- **Modell-/Harness-agnostisch:** Im "Create Agent"-Dialog (Frame t=16:40) wählbare Harnesses sind **Claude Code, Codex, "Oh My Pi"**, dazu (laut UI grau/"nicht installiert") Goose, Amp, Cursor — Buzz bindet also mehrere Coding-Agent-Harnesses parallel im selben Team-Chat ein
- Baut laut Video auf dem "ACP-Protocol" auf; jeder Agent und jeder Mensch bekommt ein kryptographisches Schlüsselpaar (im Video als "Nostr-Protokoll" benannt), wodurch jedes Event signiert und nachvollziehbar/durchsuchbar ist
- Arbeitet in einem eigenen Ordner und rührt lokale Worktrees/Branches nie direkt an, sondern erstellt Kopien
- Einschränkung laut Marcel: Man sieht aktuell nur den finalen Response eines Agenten, nicht was im Terminal/Hintergrund passiert — soll laut Ankündigung in künftigen Updates nachgereicht werden

**Fact-Check (durchgeführt, bestätigt und ergänzt):** Buzz ist real — von Jack Dorseys Firma Block gebaut, aufbauend auf dessen Open-Source-Agent-Framework Goose, quelloffen (Apache 2.0), auf dem Nostr-Protokoll basierend, und unterstützt bestätigt Claude Code, Codex und Goose als Agent-Harnesses. Diese Herkunft (Jack Dorsey/Block) wird im Video selbst nicht erwähnt — für den Zielleser relevant, falls er das Tool nachschlagen möchte. Die im Video gezeigten Detail-Screenshots (Beispiel-Thread mit den Agenten "Bumble", "Fizz", "Honey" zu einem Flutter-Migrationsprojekt, t=07:27–t=07:48) wirken wie Teil der offiziellen Produkt-Demo/Doku von Buzz, nicht wie selbst erstellter Content der Hosts.

### ChatGPT vs. Codex: Nutzerzahlen-Vergleich

Leonard nennt: ChatGPT hat kürzlich 1 Milliarde wöchentlich aktive Nutzer geknackt, während "Codex" nur bei 10 Millionen Nutzern liegt — daraus die These, dass nur ca. 1 % der ChatGPT-Nutzer den Hebel von Agenten (statt reinem Webchat) verstanden haben. Ein im Frame bei t=13:07 sichtbarer Text-Screenshot nennt ergänzend eine ChatGPT-App-Wachstumsrate von 62 % (Jahresvergleich) gegenüber 640 % bei Claude laut Sensor Tower, sowie 56 Mio. monatlich aktive Claude-App-Nutzer.

**Fact-Check (durchgeführt, präzisiert):** ChatGPT nähert sich laut The Information tatsächlich der 1-Milliarden-WAU-Marke (offiziell von OpenAI zuletzt mit 900 Mio. im Februar 2026 bestätigt). Die "10 Millionen"-Zahl ist im Video leicht ungenau dargestellt: Laut OpenAIs eigener Angabe sind das 10 Millionen **kombiniert** aus Codex UND ChatGPT Work (das separate Business-Task-Agent-Produkt, gestartet 9. Juli 2026) — nicht Codex allein. Codex allein lag Anfang Juni 2026 bei über 5 Millionen wöchentlich aktiven Nutzern. Der Kernpunkt des Videos (Agenten-Adoption ist trotz Massen-Reichweite von ChatGPT noch ein Nischenphänomen) bleibt aber im Kern zutreffend.

## Weitere News der Woche (kurz erwähnt)

- **Kimi K3:** Moonshot AI veröffentlicht Modellgewichte + technischen Report; 2,8T-Parameter-MoE-Modell mit 1M-Token-Kontextfenster, laut Ankündigung "2,5-fache Intelligenz pro Recheneinheit" ggü. Vorgänger. Ein Frame (t=09:56) zeigt eine Chart "Open frontier model size over time" mit Kimi K3 als aktuell größtem offenem Flaggschiff-Modell.
- **Google Ask Advisor:** Angekündigtes agentisches Workflow-Tool, das Google Analytics, Ads und Merchant Center in einem Agenten verbindet (t=08:53).
- **Gemini Robotics 2 (Google DeepMind):** Neues Robotic-Foundation-Modell (VLA), steuert laut Video erstmals Beine, Rumpf, Arme und Hände mit einem einzigen Modell; On-Device-Variante soll sich laut Ankündigung mit weniger als 200 Beispielen an neue Roboterkörper anpassen können (t=21:29–22:10).
- **Open-Weights-Debatte:** Nvidia-CEO Jensen Huang veröffentlicht einen offenen Brief (mitgezeichnet von Microsoft, Meta, später OpenAI und Google — außer Anthropic) für Open-Weights-Modelle als Antwort auf Diskussionen um ein mögliches US-Verbot chinesischer Open-Weights-Modelle. Anthropic-CEO Dario Amodei antwortet öffentlich (im Frame bei t=23:45 im Volltext lesbar), dass Anthropic sich nie für ein Verbot ausgesprochen habe, aber weiterhin Sicherheits-/Cybersecurity-Bedenken bei offenen Gewichten habe.
- **EU AI-Gigafactories / deutsche Regulierung:** Ursula von der Leyen kündigt per Tweet (Frame t=25:32) 30 Mrd. € für "AI-Gigafactories" an (10 Mrd. EU-Mittel + 20 Mrd. private Investitionen erhofft) — vom Host scharf kritisiert im Vergleich zu China (258 Mrd. laut gezeigtem Chart) und den USA (551 Mrd.). Zusätzlich: Die deutsche Bundesnetzagentur wird ab 29. Juli 2026 zentrale Aufsichtsbehörde für den EU AI Act in Deutschland, inkl. neuem "KI-Service Desk" (Frames t=26:14–26:35).

## RelationFlow-Demo (Werbung in eigener Sache)

Marcel zeigt zusätzlich RelationFlow, offenbar das eigene Produkt/die eigene Plattform des Kanals (Corporate-LLM/Wissensdatenbank-Tool mit vorgefertigten Agenten, Community-Vorlagen, RAG über eigene Dokumente). Wird im Video als Ergänzung zu Buzz positioniert, mit Praxisbeispielen (First-Level-Support-Agent für einen Marken-Distributor, Lead-Scraping für Industrievertrieb). Werblicher Charakter deutlich erkennbar — Einordnung entsprechend mit Vorsicht zu genießen.

---

## Kernbotschaft
Diese Woche gab es laut Video "verhältnismäßig wenig echte Modell-Updates" — der eigentliche Aufreger ist Seedance 2.5 (mehr Referenzen, längere native Clips, aber 4K trotz Ankündigung noch nicht live). Für den Coding-/Agenten-Alltag relevanter sind drei bestätigte Fakten: Opus 5 performt bei Coding-Benchmarks besser mit Medium- statt Extra-High-Reasoning-Effort (Over-Engineering-Risiko bei zu viel Denkzeit), OpenAI hat die Codex-relevanten GPT-5.6-Preise drastisch gesenkt, und mit Buzz etabliert sich eine neue, offene "Slack für Agenten"-Kategorie, die Claude Code und Codex gleichberechtigt nebeneinander in Team-Chats einbindet — ein Hinweis darauf, dass Multi-Harness-/Multi-Agent-Orchestrierung zum nächsten Software-Kategorie-Trend wird.

## Themen-Tags
Seedance 2.5, KI-Videogenerierung, ByteDance, Claude Code, Codex, Claude Opus 5, Reasoning Effort, GPT-5.6, OpenAI-Preissenkung, Buzz, Agent-Chat-Plattform, Nostr-Protokoll, Kimi K3, Open-Weights-Debatte, Jensen Huang, Dario Amodei, Gemini Robotics 2, EU AI Act, Bundesnetzagentur

## Zu prüfen
- **Genaue GPT-5.6-Rabatt-Prozentsätze (80 %/20 %) und Token-Preise** — Primärquelle ist ein im Video eingeblendeter OpenAI-Tweet-Screenshot, keine zusätzliche unabhängige Zweitquelle gefunden; Momentaufnahme, ändert sich erfahrungsgemäß häufig.
- **"Codex: 10 Millionen Nutzer"** — laut Recherche eigentlich eine kombinierte Zahl aus Codex UND ChatGPT Work, nicht Codex allein (Codex allein: über 5 Mio. WAU Anfang Juni 2026). Das Video stellt es leicht vereinfacht/ungenau als reine Codex-Zahl dar.
- **Seedance-2.5-Preisangaben aus der Live-Demo** (32 Cent/Sekunde, 7.000 Credits für 3-Min.-Long-Video) — Stand zum Aufnahmezeitpunkt, Dreamina-Preise/Credit-Systeme ändern sich erfahrungsgemäß schnell, nicht unabhängig gegengecheckt.
- **Buzz-Herkunft (Jack Dorsey/Block, Goose-Basis)** — im Video selbst nicht erwähnt, stammt aus eigener Zusatzrecherche; sollte bei Bedarf direkt an der Quelle (buzz.chat o. ä.) verifiziert werden, falls das Tool operativ eingesetzt werden soll.
- **"Oh My Pi" als Harness-Option im Buzz-Dialog** — Name aus dem Frame bei t=16:40 abgelesen, nicht unabhängig verifiziert, ob das ein etabliertes Tool oder ein Rechtschreib-/OCR-Artefakt aus einem kleinen UI-Element ist.
- **Kreuzcheck gegen bestehende Notizen:** Passt konsistent zur bestehenden Timeline in diesem Repo (z. B. [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md) nennt bereits Opus 5, [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) nennt bereits "Claude Fable 5" als Flaggschiff-Codename, das hier im FrontierCode-Chart bei t=13:28 erneut auftaucht). Kein Widerspruch zu bestehenden Notizen gefunden — dieses Video ergänzt die Timeline eher um die Buzz-Plattform und den Opus-5-Reasoning-Effort-Befund, die in den bisherigen Zusammenfassungen im Repo noch nicht vorkamen.
- **Frame bei t=03:54** (PowerPoint-Editor mit Bar-Chart "Q4 marks the growth inflection point") lässt sich weder eindeutig einer im Transkript genannten Stelle noch einem bekannten Produkt zuordnen — vermutlich kurz eingeblendetes B-Roll/Beispielmaterial, nicht weiter eingeordnet.
