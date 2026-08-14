# "Welche KI in 2026? Chatbots, Agents, Apps im Überblick!"

**Kanal:** Christoph Magnussen (CEO Blackboat)
**URL:** https://www.youtube.com/watch?v=zNuynCOm5Mc
**Länge:** 36:26
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) und [mcp-ueberblick.md](../mcp-ueberblick.md) für tiefere Einzelthemen zu Claude/MCP, sowie [ai-agent-workflow.md](../ai-agent-workflow.md) für mehr zu Boris Cherny/Claude Code.*

Reines Landschafts-Überblicksvideo ohne konkrete Demos — Christoph Magnussen (Blackboat, Digitalberatung seit 2010) ordnet den aktuellen KI-Tool-Markt in drei Kategorien: Chatbots, Agent-Harnesses, Spezialtools. Kaum überprüfbare Einzelfakten, dafür viele persönliche Einordnungen/Verdicts — deswegen unten als Tabelle aufbereitet statt nur Fließtext.

## 1. Chatbots

### ChatGPT (OpenAI) — "Platzhirsch"
Nach wie vor der bekannteste Chatbot ("hat LLMs in den Alltag gebracht"). Drei Modi im selben Fenster: klassischer Chat, Suche (explizit **keine** Suchmaschinen-Ersatz), und im Hintergrund laufende Agents (inkl. Deep Research — laut Magnussen mittlerweile sehr gute, aber langsame Reports). Modellauswahl von Instant bis Pro/Thinking (u. a. 5.5/5.4 genannt). Gezeigte Preisstaffel (Screenshot, Frame t=00:55): Free 0€, Go 8€, Plus 23€, Pro 103€/Monat. Magnussens Einsatz: komplizierte Einzelfragen, seltener Deep Research — beim Schreiben laut ihm klar schwächer als Claude.

### Claude (Anthropic)
Laut Magnussen "bester Freund aller, die gerne schöne Texte schreiben" — stark bei Schreiben/Ausdruck und komplizierten Code-Fragen, u. a. dank Opus 4.8 (Fable/Mythos explizit als "anderes Thema, heute nicht behandelt" ausgeklammert). Anthropic laut Video Erfinder von MCP und Skills (deckt sich mit [mcp-ueberblick.md](../mcp-ueberblick.md)). Schwächer bei Bildgenerierung und Spracherkennung (eigenes Sprachmodell statt Whisper, laut Magnussen v. a. auf Deutsch merklich schlechter). Pricing bis Max-Plan ca. 200€/Monat, Modelle gelten als "tokenhungrig" — Chatbot-Limits werden schneller erreicht als bei ChatGPT. Gezeigte Preistabelle (Frame t=17:18): Fable 5, Opus 4.8, Sonnet 5, Haiku 4.5.

### Google Gemini
Stärken: Google-Suche-Integration und Multimodalität (Bild/Audio/Video, Website-/Podcast-/Präsentations-Generierung ähnlich Notebook LM). Tief in Workspace eingebunden (Gmail/Drive/Sheets), aber laut Magnussen in der Standalone-App stärker als aus den Workspace-Tools heraus aufgerufen. Weniger "Personality" als ChatGPT/Claude, da Google die System-Prompts nicht offenlegt — dadurch neutraler/nüchterner, besser für Business geeignet. Modelle 3.5 Flash und 3.1 Pro laut Magnussen "mittlerweile nicht mehr Top in vielen Benchmarks", Preise wurden stark angehoben. Pläne: Free, Plus, Pro, Ultra (Screenshot Frame t=03:39).

### Microsoft Copilot — "der Blackberry von heute" (mit Augenzwinkern)
Business-/Legacy-Tool für Firmen, die bereits Microsoft 365/SharePoint/Teams nutzen. Zwei Varianten: eingeschränktes Copilot Web vs. teureres, workspace-integriertes Copilot. Nutzt angepasste OpenAI- **und** Anthropic-Modelle (eigene System-Prompts, nicht öffentlich) statt eigener starker Modelle — laut Magnussen ein Zeichen, dass Microsoft noch keine konkurrenzfähigen eigenen Modelle hat. Pricing bewusst nicht erklärt ("eigene Wissenschaft", bundle-abhängig; Screenshot zeigt Business-Pläne 15,60–27,73€, Frame t=16:24). Wichtige Einschränkung: Ein unaufgeräumter SharePoint-"Artefakte-Friedhof" macht auch Copilot nutzlos — das Tool kann fehlende Datenhygiene nicht kompensieren.

## 2. Agent-Harnesses — laut Magnussen die eigentlich relevante Kategorie

Abgrenzung zum Chatbot: Auftrag statt Frage-Antwort, autonome Mehrschritt-Ausführung, mehrere Agents parallel/verschachtelt. Bild: "normales Auto vs. Formel-1-Wagen" — entsprechend teuer.

### Claude Code & Claude Cowork
Claude Code habe die Kategorie letztes Jahr losgetreten, erfunden von **Boris Cherny** (im Whisper-Transkript als "Cherney" verschriftet — bereits aus anderen Repo-Notizen bekanntes Mishearing-Muster, siehe [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md)), ursprünglich als Terminal-Tool. Mittlerweile eine App mit drei Reitern (Chat/Cowork/Code) — von Magnussen explizit als unnötig verwirrend kritisiert ("Anthropic, please – macht doch einfach nur einen Reiter draus"). Cowork = "Claude Code nett verpackt für Leute, die Angst vor geschwungenen Klammern haben", eigenes Team, für Nicht-Entwickler (Desktop/Doku-Organisation, Screenshot "Organize my Downloads folder", Frame t=20:57). Deckt sich mit der Code/Cowork-Abgrenzung in [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md) ("Maschinenraum vs. Chefetage").

### Codex (OpenAI)
Magnussens **persönlicher Daily Driver**. Ursprünglich Open-Source-Basis, heute eine einzige App ohne verwirrende Tab-Aufteilung, mit Plugins (vergleichbar Skills/MCP bei Claude). Geschwindigkeitsstufen (Standard/Schnell) und Denkstufen (niedrig/mittel/hoch/extra hoch) — von ihm selbst als "für normale User echt kompliziert" bezeichnet. Anthropic-Modelle laut ihm bei manchen internen Kolleg:innen für große Codebases dennoch bevorzugt — "die Zahlen sprechen für Claude Code" (Erfolgsmetrik), aber Codex sei die performantere App.

### Cursor
Habe als erstes IDE-Tool gezeigt, wie man viele parallele Agents verwaltet — Vorläufer-Kategorie für Codex/Cowork. Fokussiert auf Entwickler. Erwähnt: Cursor/Anysphere gehöre "mittlerweile zu SpaceX für schlappe 60 Milliarden" — **klingt zunächst nach Whisper-Fehler, ist aber per Websuche bestätigt** (SEC-Filing Juni 2026: SpaceX übernimmt Anysphere für 60 Mrd. $ in Aktien, siehe Quellen unten).

### Sonstige Einordnungen
- Anthropic soll laut Video OpenAI bei Unternehmenswert/Umsatz überholt haben — **ebenfalls per Websuche bestätigt** (Anthropic $47 Mrd. Run-Rate/$965 Mrd. Bewertung vs. OpenAI $852 Mrd., Mai 2026).
- Anthropic verteile Rechenleistung über vier Wege: Amazon-, Microsoft-Rechenzentren, Google-TPUs und SpaceX — **ebenfalls bestätigt** (reale Compute-Deals mit AWS Trainium, Google/Broadcom TPUs, Microsoft/Azure und SpaceX/Colossus).
- "Goals"/Ziel-Definition für Agents wird als zentrale neue Fähigkeit hervorgehoben: ein gutes Ziel ist messbar abschließbar; wer Goals/Loops gut definieren kann, holt laut Magnussen deutlich mehr aus Agents heraus.

## 3. Spezialtools

- **Perplexity** — Sucht-Spezialist (Echtzeit-Suchdaten + LLM), Magnussens täglicher Deep-Research-Favorit, lässt sich in Claude Code/Codex als Recherche-Zulieferer einbinden. Kritikpunkt: unübersichtliche, teure Preisstruktur (Suche, Comet-Browser, Enterprise).
- **Notebook LM (Google)** — kein klassischer Chatbot, sondern pro Dokument ein eigenes RAG/Vektor-Retrieval (Beispiel: 500 Dokumente = 500 eigene "Racks"), dadurch exakter Quellenbezug statt LLM-Verallgemeinerung. Bekannt geworden durch automatische Podcast-Generierung aus Dokumenten, inzwischen auch Infografiken, Präsentationen, Quizzes, Videos.
- **Kurz erwähnt:** Lovable (Web-Apps bauen), Gamma (Präsentationen) — laut Magnussen zunehmend von Agent-Harnesses wie Claude Code/Codex verdrängt, weil die mittlerweile "alles" können.

## Quick-Reference: Tool → Einsatzzweck → Magnussens Verdict

| Tool | Kategorie | Wofür laut Video | Verdict |
|---|---|---|---|
| ChatGPT | Chatbot | Komplizierte Einzelfragen, gelegentlich Deep Research | Go-To für Fragen, schwächer beim Schreiben |
| Claude (Chat) | Chatbot | Schreiben, komplizierte Code-Fragen | Stärker beim Schreiben, nicht sein Daily Go-To im Chat |
| Gemini | Chatbot | Google-Workspace-Nutzer, Multimodalität, Suche | Empfehlenswert bei bestehendem Workspace-Account |
| Copilot | Chatbot | Bestehende Microsoft-365-Kunden | "Blackberry"-Analogie — nur wenn ihr eh in der MS-Welt seid |
| Claude Code | Agent-Harness | Tiefe technische Eingriffe, Entwickler | Empfohlen als eines von zwei Harness-Tools zum Meistern |
| Claude Cowork | Agent-Harness | Büro-/Dokumentenarbeit für Nicht-Entwickler | Gute Einstiegshürde, gleiche Engine wie Code |
| Codex | Agent-Harness | Alltags-Coding & allgemeine Aufträge | Magnussens persönlicher Daily Driver |
| Cursor | Agent-Harness (IDE) | Entwickler, die viele Agents parallel managen wollen | Nischig für Devs, jetzt SpaceX-Tochter |
| Perplexity | Spezialtool | Recherche/Deep Research mit Quellenbezug | Täglicher Favorit des Hosts |
| Notebook LM | Spezialtool | Große Dokumentenmengen mit exaktem Quellenbezug | "Eines der Top-Tools von Google" |

## Empfehlung des Hosts

Mindestens ein Agent-Harness-Tool in voller Tiefe lernen — konkret Claude Code **oder** Codex, nicht beide oberflächlich. Magnussens persönlicher Pick: Codex. Nachteil beider: Vendor-Lock-in in die OpenAI- bzw. Anthropic-Welt (Cursor als unabhängigere, aber jetzt SpaceX-zugehörige Alternative). Ergänzender Hinweis: nicht für jede Aufgabe einen Agent einsetzen — für repetitive, klar definierte Abläufe eher klassische Workflow-Tools wie n8n. Zum Datenschutz-Einwand ("dürfen wir das in der Firma überhaupt nutzen?"): laut Magnussen ist mehr erlaubt als gedacht, man müsse nur genau prüfen, welche Daten/Vertragsgrundlage betroffen sind.

**Werbeteil:** Ab ca. 16:53 im Video als "Werbung" markierter Abschnitt für Blackboats eigene Angebote (12-Wochen-Programm, "AI Summer School", blackboat.com) — im Video selbst klar gekennzeichnet.

---

## Kernbotschaft
Der KI-Markt 2026 gliedert sich laut Magnussen in drei klar unterscheidbare Stufen: Chatbots (ChatGPT, Claude, Gemini, Copilot — je nach vorhandenem Ökosystem/Stärke wählen), Agent-Harnesses (Claude Code/Cowork, Codex, Cursor — die eigentlich transformative Kategorie, in der sich tiefes Investment lohnt) und Spezialtools (Perplexity, Notebook LM — punktgenau für Recherche bzw. dokumentenbasiertes Arbeiten). Statt einem einzigen Tool treu zu bleiben ("Nokia-Zeit der KI-Modelle"), empfiehlt er, bewusst zwischen Kategorien zu wechseln und sich mindestens ein Harness-Tool wirklich anzueignen, da dort der größte Hebel liegt.

## Themen-Tags
KI-Marktüberblick 2026, ChatGPT, Claude/Anthropic, Google Gemini, Microsoft Copilot, Claude Code, Claude Cowork, Codex, Cursor, Perplexity, Notebook LM, Agent Harness, MCP, Goals/Loops, Blackboat

## Zu prüfen
- **Whisper-Mishearing bestätigt:** "Boris Cherney" im Transkript — korrekt ist **Boris Cherny** (bereits in mehreren anderen Repo-Notizen dokumentiert, siehe [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md), [ai-agent-workflow.md](../ai-agent-workflow.md)). In dieser Zusammenfassung korrigiert wiedergegeben.
- **Plausibilitätscheck durchgeführt (WebSearch), alle drei zunächst unglaubwürdig wirkenden Aussagen bestätigt:** (1) SpaceX übernimmt Cursor/Anysphere für 60 Mrd. $ (SEC-Filing Juni 2026); (2) Anthropic hat OpenAI bei Umsatz/Bewertung überholt (Anthropic ~47 Mrd. $ Run-Rate/965 Mrd. $ Bewertung vs. OpenAI 852 Mrd. $, Stand Mai 2026); (3) Anthropics Vier-Wege-Compute-Strategie inkl. SpaceX/Colossus ist real (zusätzlich zu AWS, Google-TPUs, Microsoft/Azure).
- **Gemini-Modellnamen "3.5 Flash" und "3.1 Pro"** — leicht inkonsistent mit anderen Repo-Notizen, die z. B. "Gemini 3.5 Flash" in einem Intelligenz-Kosten-Chart nennen (siehe [video-summary-qZRftXozT3M.md](video-summary-qZRftXozT3M.md)); könnten unterschiedliche, gleichzeitig existierende Modellstufen sein, hier nicht weiter verifiziert.
- Genaue Preisangaben (ChatGPT-, Copilot-, Gemini-Staffeln) sind Screenshot-Momentaufnahmen aus dem Video, nicht separat gegengecheckt.
- Magnussens persönliche Werturteile (z. B. "Codex ist performanter als die Claude-App", "ChatGPT schwächer beim Schreiben") sind explizit als seine eigene, nicht weiter belegte Einschätzung/Erfahrung zu verstehen, nicht als objektiver Fakt.
- Kein inhaltlicher Widerspruch zu bestehenden Repo-Notizen gefunden — das Video bestätigt und ergänzt eher bereits vorhandene Punkte (Claude-Code/Cowork-Trennung, MCP-Erfindung durch Anthropic, Claude-Modellnamen Fable 5/Opus 4.8/Sonnet 5/Haiku 4.5) als sie zu widerlegen.

## Quellen der Plausibilitätschecks
- [Qz — SpaceX buys Cursor parent Anysphere for $60 billion](https://qz.com/spacex-buying-cursor-anysphere-60-billion-deal-061626)
- [Value Add VC — Anthropic Revenue Hits $47B Run-Rate](https://valueaddvc.com/blog/anthropic-revenue-hits-47b-run-rate-how-it-passed-openai-in-just-five-months)
- [TechInformed — Anthropic turns to SpaceX for Claude capacity](https://techinformed.com/anthropic-turns-to-spacex-for-claude-capacity/)
- [Data Center Frontier — Inside Anthropic's Multi-Cloud AI Factory](https://www.datacenterfrontier.com/machine-learning/article/55335703/inside-anthropics-multi-cloud-ai-factory-how-aws-trainium-and-google-tpus-shape-its-next-phase)
- [t3n — Blackboat-CEO Christoph Magnussen](https://t3n.de/news/blackboat-ceo-magnussen-das-muss-ein-unternehmen-erfuellen-um-ki-agenten-einzusetzen-1737895/)

**Hinweis zum Ablauf:** Native Untertitel scheiterten mit HTTP 429, der Whisper-Fallback (Replicate) lief in 7 Chunks à ~330s erfolgreich durch (610 Segmente gesamt). Bei 36 Minuten Länge wurden nur 80 sparsam verteilte Frames extrahiert (~1 Frame alle 27s) — für dieses talk-lastige Vergleichsvideo ausreichend, da die Substanz fast vollständig im gesprochenen Wort und wenigen eingeblendeten Screenshots (Preistabellen, UI-Screenshots der besprochenen Tools) liegt, die alle gesichtet wurden.
