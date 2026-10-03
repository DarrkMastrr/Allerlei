# KI-Modellvergleich & -kosten (2026)

Quellen: [video-summary-G3Ed-J_DE5s.md](video-summaries/video-summary-G3Ed-J_DE5s.md) ("ChatGPT vs. Claude vs. Gemini - Welcher €20 Plan lohnt sich wirklich?"), [video-summary-OUIxlLG8yO0.md](video-summaries/video-summary-OUIxlLG8yO0.md) ("Was kostet KI im Büro wirklich?"), [video-summary-cse3QV90YpE.md](video-summaries/video-summary-cse3QV90YpE.md) ("Gemini 3.8, Fable 5.1, ChatGPT Astra Leak"), [video-summary-zNuynCOm5Mc.md](video-summaries/video-summary-zNuynCOm5Mc.md) ("Welche KI in 2026?")

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

## Kernbotschaft

Modellvergleiche und Preisangaben sind in diesem Themenfeld die am schnellsten veraltenden Inhalte im ganzen Repo — mehrere Quellen selbst weisen darauf hin, dass Einzelzahlen zum Lesezeitpunkt bereits überholt sein können. Die strukturellen Entscheidungsregeln (nach Nutzungsprofil wählen, Doppellizenzen vermeiden, ein Harness-Tool wirklich lernen) sind dagegen stabil und der eigentliche Mehrwert dieser Artikel-Zusammenfassung.

## Zu prüfen
- Alle konkreten Preis-/Benchmarkzahlen: Momentaufnahme zum jeweiligen Videodatum, vor Verwendung neu prüfen
- Höre bei Vergleichsvideos primär auf die *Methodik* (Testkategorien, Kombinationslogik), nicht auf einzelne Euro-Beträge
