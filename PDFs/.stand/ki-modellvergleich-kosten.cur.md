# KI-Modellvergleich & -kosten (2026)

Quellen: [video-summary-G3Ed-J_DE5s.md](video-summaries/video-summary-G3Ed-J_DE5s.md) ("ChatGPT vs. Claude vs. Gemini - Welcher €20 Plan lohnt sich wirklich?"), [video-summary-OUIxlLG8yO0.md](video-summaries/video-summary-OUIxlLG8yO0.md) ("Was kostet KI im Büro wirklich?"), [video-summary-cse3QV90YpE.md](video-summaries/video-summary-cse3QV90YpE.md) ("Gemini 3.8, Fable 5.1, ChatGPT Astra Leak"), [video-summary-zNuynCOm5Mc.md](video-summaries/video-summary-zNuynCOm5Mc.md) ("Welche KI in 2026?"), [video-summary-1ID_VcwzIo8.md](video-summaries/video-summary-1ID_VcwzIo8.md) (OpenAI DevDay 2026, Nachtrag 2026-10-12), [video-summary-eDCd4UJParE.md](video-summaries/video-summary-eDCd4UJParE.md) (Meta Muse Wonder Full/Standard, Nachtrag 2026-10-17), [video-summary-iVxubkOM4gA.md](video-summaries/video-summary-iVxubkOM4gA.md) (Nachtrag 2026-10-24, Gemini 4 Argon/Grok Voice), [video-summary-5pc-GWI9k1Q.md](video-summaries/video-summary-5pc-GWI9k1Q.md) (Nachtrag 2026-10-24, S&P-Gewinne)

## Kein Universalsieger bei den Consumer-Abos

G3Ed-J_DE5s testet ChatGPT Plus, Claude Pro und Google AI Pro (alle ~20 €/Monat) in zehn Testrunden:

| Anbieter | Stärke | Schwäche |
|---|---|---|
| Google AI Pro | Medien (Video), großzügigstes Allround-Paket | — |
| ChatGPT Plus | Bilder, Dateizugriff ("Work"-Feature), vorhersehbarste Limits | tatsächlicher DE-Preis 23 €, nicht 20 € |
| Claude Pro | Coding, App-Integrationen, (knapp) Dateiarbeit | härteste Nutzungsgrenzen, kein Fallback-Modell |

Kernaussage bleibt unabhängig von Einzelpreisen gültig: Die Wahl hängt vom Nutzungsprofil ab, nicht vom Preis allein.

## Büro-Kosten: eine Kombinationsrechnung, kein Einzelpreis

OUIxlLG8yO0 zeigt: Die Kosten eines KI-gestützten Büro-Workflows hängen an der Kombination aus Anzahl der Werkzeuge (Text-KI, Medien-KI), Anzahl der lizenzierten Personen, bereits vorhandenen Lizenzen (z. B. Google Workspace mit inkludiertem Gemini — Doppelkäufe vermeiden) und der Frage, ob sich langfristig auf günstigere API-Automatisierung umstellen lässt. Strukturelle Kernaussage: erst Vorhandenes testen, dann gezielt zubuchen, dann ggf. automatisieren.

**Wichtig für Aktualität:** Die im Video genannte, bevorstehende Claude-Sonnet-5-API-Preiserhöhung im September war zum Prüfzeitpunkt bereits überholt — die Erhöhung wurde im August 2026 zurückgenommen. Einzelpreise in diesem Themenfeld veralten schnell.

## Drei-Stufen-Modell des Marktes (zNuynCOm5Mc)

Christoph Magnussen gliedert den KI-Markt 2026 in drei Kategorien:

1. **Chatbots** (ChatGPT, Claude, Gemini, Copilot) — Wahl nach vorhandenem Ökosystem/Stärke
2. **Agent-Harnesses** (Claude Code/Cowork, Codex, Cursor) — die eigentlich transformative Kategorie, tiefes Investment lohnt sich
3. **Spezialtools** (Perplexity, NotebookLM) — punktgenau für Recherche/dokumentenbasiertes Arbeiten

Empfehlung: nicht einem Tool treu bleiben ("Nokia-Zeit der KI-Modelle"), sondern bewusst zwischen Kategorien wechseln und mindestens ein Harness-Tool wirklich beherrschen — dort liegt der größte Hebel.

## Release-Tempo als Kostenfaktor

cse3QV90YpE dokumentiert vier Modell-Releases allein in der ersten Septemberwoche 2026 (Gemini 3.8 Flash, Claude Fable 5.1, Meta Muse Spark 1.3, GPT-6-Astra-Teaser) — ungewöhnlich präzise recherchiert (alle geprüften Zahlen stimmen exakt mit Primärquellen überein). Zeigt praktisch: Wer heute eine Kaufentscheidung anhand von Preis/Leistung trifft, sollte mit einem sehr kurzen Halbwertszeit der Zahlen rechnen.

## Opus 5.5 vs. GPT-6 Sol/Luna: Token-Preis vs. Kosten pro Aufgabe (9EOqBiMR3z4, 3xksVVtssjY)
Zwei Videos zur Modellwelle vom September 2026. Opus 5.5 (Release 22.09.2026, per WebSearch bestätigt) kostet laut Anthropic 4 $ / 20 $ pro Mio. Token (Cache Reads 0,20 $) und soll bei typischen Workloads ca. 40 % billiger sein. Laut Artificial Analysis (Angabe in 9EOqBiMR3z4, nicht selbst geprüft) sind die Kosten *pro Aufgabe* wegen hohen Token-Verbrauchs aber etwa gleich geblieben — beides kann stimmen (Token-Preis vs. Verbrauch). 3xksVVtssjY liefert dazu den Praxisbefund: Effort-Stufe Medium statt Max spart deutlich; ein Effort-Wechsel mitten in der Session soll seit Claude Code v2.1.280 ohne Cache-Verlust gehen — das relativiert die frühere Warnung aus den Kostenoptimierungs-Videos (KZAJeq5n-m8, XEbR5qmxGQ0). Der Terminal-Bench-Vergleich (Opus 5.5 66,4 % xhigh vs. Astra 57,9 % high) ist nicht effort-gleich.
- **Für Hardware-Teams:** Kostensteuerung über Effort-Stufe und Caching ist relevanter als der Listenpreis; Modellwahl nach Kosten pro erledigter Aufgabe bewerten.
- **Nicht geprüft / Einzelfälle:** Roboter-Simulator- und 3D-Grundriss-Tests sind subjektive Einzelläufe der Hosts; "EQ 151"-Aussage in 3xksVVtssjY unplausibel. GPT-6 Sol/Luna sind in [gpt-6-astra-ueberblick.md](gpt-6-astra-ueberblick.md) noch nicht dokumentiert.

*Nachtrag Faktencheck (2026-09-29):* Anthropic-Claim (40 % billiger bei Standardeinstellungen) und AA-Befund (pro Aufgabe gleichauf bei Max-Effort, ca. 119k vs. 73k Output-Tokens) sind bestätigt; konkrete Dollarwerte unbestätigt. Terminal-Bench: Anthropic 66,4 % (xhigh laut zwei Prüfern, max laut einem) vs. Astra 57,9 % (high); Vals AI (29.09.2026) Opus 5.5 65,15 %, Astra 59,60 %. Sol/Luna (2 $/10 $ bzw. 0,10 $/0,50 $) nur über Sekundärquellen. "EQ 151" meint den Mensa-Norway-IQ-Test, der als saturiert gilt. Effort-Wechsel ohne Cache-Verlust: nur X-Post einer Anthropic-Mitarbeiterin. Details in [video-summary-9EOqBiMR3z4.md](video-summaries/video-summary-9EOqBiMR3z4.md) und [video-summary-3xksVVtssjY.md](video-summaries/video-summary-3xksVVtssjY.md).

## Nachtrag DevDay 2026: Dots, Ultrafast und neue Preisstufen (Stand 2026-10-03)

Quelle: [video-summary-a_jihWpd8cc.md](video-summaries/video-summary-a_jihWpd8cc.md) (Satire-Video, Zusammenfassung mit Prüfvermerk "nur noch Detailfehler, letzte Korrektur nicht nachgeprüft"); Zahlen stammen aus dort geprüften Webquellen (dev.to, Latent Space als WebFetch-Zusammenfassungen; Futurism, Startup Fortune, pymnts als Volltext). Details und Vorbehalte: [gpt-6-astra-ueberblick.md](gpt-6-astra-ueberblick.md).

- **Ultrafast = Preisstaffelung nach Tempo:** "bis zu 8x" schneller (Codex) bzw. 6x (API) bei 6-fachem Preis — Astra dann 60 $/300 $ statt 10 $/50 $ je 1 Mio. Token. Für die Kostenrechnung gilt dasselbe wie bei Effort-Stufen: Tempo nur dort bezahlen, wo es Wartezeit spart (interaktives Arbeiten), nicht bei Nachtläufen.
- **Dots (OpenAI-Agenten):** laut Quellen in Pro/Business Premium/Enterprise enthalten, Tarifpreise in den Quellen widersprüchlich (u. a. 100 $/200 $/500 $-Stufen) — vor jeder Budgetplanung bei OpenAI direkt prüfen.
- **Sol:** Das Video nennt "GPT-6.1 Sol"; die oben genannten Sol-Preise (2 $/10 $) stammen von "GPT-6 Sol/Luna" — Zuordnung ungeklärt.

## Vending Bench: Modellvergleich in der Geschäftssimulation

Quelle: [video-summary-phcZVAmT8j8.md](video-summaries/video-summary-phcZVAmT8j8.md) (Everlast AI, 2026-10-12). Andon Labs' Vending Bench misst Modellleistung als Getränkeautomaten-Manager über ein simuliertes Jahr (Endguthaben als Score) — kein rein akademischer Harness, sondern wirtschaftliches Handeln unter echtem Druck (Lieferanten, Preisstrategien, Wettbewerb). Stand September 2026:

| Modell | Vending-Bench-Ergebnis |
|---|---|
| GPT-6 Astra | 15.515 $ (Spitzenreiter) |
| Claude Opus 5 | ~11.200 $ (vorheriger Rekord; abgeleitet: Astra +4.300 $) |
| Claude Fable 5.1 | ~5.200 $ (ca. ein Drittel von Astra; abgeleitet) |

Verbesserungsrate laut Andon Labs: ~822 $/Monat (Top-Modelle), >1.000 $/Monat (chinesische Modelle); Prognose: chinesische Modelle ab Oktober 2027 führend. Konkrete Zahlen aus Video, nicht über öffentliche Primärquellen verifiziert (**Suchtreffer**). Für die Kostenrechnung gilt das Umgekehrte wie bei Token-Preisen: Das teuerste Modell (Astra: 10 $/50 $ je Mio. Token) liefert hier die höchste wirtschaftliche Leistung — ob das den Mehrpreis rechtfertigt, hängt vom konkreten Einsatzfall ab.

## OpenAI DevDay 2026: GPT-6.1 Sol als günstigere Spitzenklasse (1ID_VcwzIo8, Nachtrag 2026-10-12)

[1ID_VcwzIo8](video-summaries/video-summary-1ID_VcwzIo8.md) ("Das neue ChatGPT ist da: Alle 20+ Updates") bringt Preiszahlen aus dem OpenAI DevDay vom 29.09.2026: **GPT-6.1 Sol** kostet $2/$10 pro Million Token (Input/Output) — ein Fünftel des Preises von **GPT-6 Astra** ($10/$50). Damit bietet OpenAI erstmals ein qualitativ hochwertiges Modell deutlich unterhalb von Claude Sonnet 5.5 an, was laut Video zur direkten Wettbewerbsreaktion auf Meta Muse und Grok-Angebote entstand. Weitere kostensenkende Ankündigungen: "Ultra Fast"-Modus (doppelte Geschwindigkeit, gleicher Preis) und Computer-Use-Erweiterung auf 8–16 Stunden autonome Aufgaben (vorher max. 15 Minuten). Preisangaben durch externe Quellen bestätigt (**Suchtreffer**).

## Nachtrag 2026-10-17: Meta Muse Wonder Full/Standard als neue Frontier-Konkurrenz (eDCd4UJParE)

Quelle: [video-summary-eDCd4UJParE.md](video-summaries/video-summary-eDCd4UJParE.md) (Everlast AI, 12. Oktober 2026). **Prüfstatus:** Benchmarkzahlen durch mehrere Sekundärquellen bestätigt (Suchtreffer); SWE-Marathon-Werte aus Metas eigenem Bericht, nicht unabhängig verifiziert.

Meta veröffentlichte am 12. Oktober 2026 zwei Modelle unter dem Namen **Muse Wonder**:

- **Muse Wonder Full** (kein API-Zugang): 56 Punkte auf dem *Artificial Analysis Intelligence Index* — gleichauf mit Claude Sonnet 5.5, knapp unter Claude Opus 5.5 (58). API-Preis entspricht dem von Opus 5.5 ($4/$20 pro Mio. Token Input/Output).
- **Muse Wonder Standard**: 52 Punkte — gleichauf mit GPT-6.1. API-Preis: ebenfalls $4/$20 pro Mio. Token.

| Benchmark | Wonder Full | Wonder Standard | Claude Opus 5.5 | GPT-6 Astra |
|---|---|---|---|---|
| Artificial Analysis Index | 56 | 52 | 58 | ~53 |
| SWE-Marathon (lang. Coding) | 42,5 % | – | ~3 % | ~5 % |
| DeepSWE (113 Tasks) | 79 % | 78,8 % | ~74 % | ~74 % |
| Halluzination (unsichere Fragen) | 23 % | – | 59 % | 51 % |

**Preisstrategie:** Standard Wonder kostet denselben API-Preis wie Opus 5.5 ($4/$20), liefert aber in manchen Benchmarks (besonders langer Code, Recht, Finanzen) vergleichbare oder bessere Ergebnisse. Praxistest: Muse Code (Standard Wonder) brauchte 3:42 min für ein programmierprojekt; Claude Code (Opus 5.5) 11:40 min.

**Einordnung:** Wonder Full ist nicht per API verfügbar und hat kein öffentliches Datum. Wonder Standard ist der direkte GPT-6.1-Sol-Konkurrent. Beide Modelle stammen aus dem Muse-Team unter Alexander Wang (ehemals Scale AI, seit Juni 2025 Metas Chief AI Officer), das mit 14,3 Mrd. USD aufgebaut wurde.

## Nachtrag 2026-10-24: Gemini 4 Argon, Grok Voice 3.0 und S&P-Gewinnwachstum

### Gemini 4 Argon im Praxistest und Apollo-7-Robotik (iVxubkOM4gA)

Quelle: [video-summary-iVxubkOM4gA.md](video-summaries/video-summary-iVxubkOM4gA.md) (Everlast AI / Leonard Schweding, Oktober 2026). **Prüfstatus:** Benchmark-Vergleich DataCamp-Quelle (extern, nicht im Video; Suchtreffer). Preisangaben Monday.com-Test aus Video.

**Gemini 4 Argon — Kernfähigkeiten:**
- **1 Million Output-Tokens in einem einzigen Schritt:** Sergey Brin beschreibt das im Video als Äquivalent zu "einer Woche menschlichen Nachdenkens". Bisherige Modelle konnten diese Gesamtmenge über mehrere Schritte erreichen, aber nicht in einem Durchgang.
- **Benchmark vs. Claude Opus 5.5:** Laut einer DataCamp-Analyse (externe Quelle, nicht im Video; Suchtreffer) gewinnt Argon in 14 von 18 gemeinsamen Tests. Opus 5.5 liegt vorne in Terminal-basierten Coding-Aufgaben (FrontierSWE, Terminal-Bench).

**Monday.com-Klonversuch (16 Stunden, drei Modelle):**

| Modell | Geklonte Seiten | Kosten | Ergebnis |
|---|---|---|---|
| Meta Muse Wonder | 49 Seiten | unbekannt (CLI-Abo) | Funktionen liefen, Oberfläche abweichend |
| Gemini 4 Argon | 67 Seiten | $64 | Gut, aber farbige Emojis statt Original-Icons |
| Claude Opus 5.5 | vergleichbar | $257 | Kaum vom Original zu unterscheiden — klarer Sieger |

**Einordnung:** Argon ist günstiger, Opus besser in Reverse Engineering. Der eigentliche Befund des Tests: Was früher Wochen dauerte, erledigt ein KI-Modell in 16 Stunden.

**Apollo-7-Robotik mit Argon:** Argon verarbeitet ein einziges Foto einer Tischoberfläche zu einer physikalischen Simulation und generiert daraus über 4.500 Trainingsläufe für einen Roboter. Ergebnis: Erfolgsrate im realen Einsatz von 56 % auf **75 %** gestiegen. Der humanoide Roboter Apollo (Apptronik) traf nach diesem Training sieben Cornhole-Würfe in Folge. Ergänzt den Handhabungs-Flaschenhals-Befund in [humanoide-roboter-2026.md](humanoide-roboter-2026.md).

**Grok Voice 3.0:** 20.000 Starlink-Kundenanrufe täglich; Kosten **7–8 Cent/Minute** (historisch ca. 30 Cent/Sekunde für vergleichbare Sprach-KI-Dienste; Faktor >13x günstiger als menschliche Call-Center nach Hochrechnung im Video). Zeigt, wo Sprachmodelle heute im Produktionseinsatz Kosten transformieren.

### KI-Infrastrukturgewinne vs. Dotcom — S&P +29 % (5pc-GWI9k1Q)

Quelle: [video-summary-5pc-GWI9k1Q.md](video-summaries/video-summary-5pc-GWI9k1Q.md) (wallstreetONLINE / Stefan Risse, Oktober 2026). **Prüfstatus:** S&P-500-Gewinnzahl +29 % Q3 2026 durch FactSet-Daten bestätigt.

Stefan Risse (Acatis Investment) liefert das Gegenargument zu Blasen-Warnungen: **S&P 500 Gewinnwachstum 2026 ~29 % (Q3 blended)**, während Kurse nur ~13 % stiegen — Bewertungen sind relativ günstiger geworden. Der entscheidende Unterschied zu Dotcom 2000: KI-Infrastrukturunternehmen (Nvidia, Hyperscaler) verdienen **heute real Geld**, nicht nur auf Papier. TSMC: sechstes Rekordquartal, Gewinn +69 % — die Chip-Nachfrage ist fundamental.

Für die Kostenrechnung in diesem Themenfeld gilt: Starke Unternehmensgewinne erklären, warum Preisniveaus für KI-Dienste stabil bleiben, während Einzelpreise gleichzeitig fallen. Das strukturelle Entscheidungsprinzip — nach Aufgabe wählen, nicht nach Listenpreis — bleibt unverändert gültig.

## Kernbotschaft

Modellvergleiche und Preisangaben sind in diesem Themenfeld die am schnellsten veraltenden Inhalte im ganzen Repo — mehrere Quellen selbst weisen darauf hin, dass Einzelzahlen zum Lesezeitpunkt bereits überholt sein können. Die strukturellen Entscheidungsregeln (nach Nutzungsprofil wählen, Doppellizenzen vermeiden, ein Harness-Tool wirklich lernen) sind dagegen stabil und der eigentliche Mehrwert dieser Artikel-Zusammenfassung.

## Zu prüfen
- Alle konkreten Preis-/Benchmarkzahlen: Momentaufnahme zum jeweiligen Videodatum, vor Verwendung neu prüfen
- Höre bei Vergleichsvideos primär auf die *Methodik* (Testkategorien, Kombinationslogik), nicht auf einzelne Euro-Beträge
- Gemini 4 Argon "14 von 18"-Benchmark: DataCamp-Analyse (extern, nicht im Video), nicht unabhängig nachgeprüft
- Grok Voice 3.0: 7–8 ct/min aus Videobeschreibung; historischer Vergleichswert "30 ct/s" nicht verifiziert
