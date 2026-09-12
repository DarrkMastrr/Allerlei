# GPT-6 Astra: Launch, Fähigkeiten und offene Fragen

Quellen: [video-summary-AOgUqb62WUQ.md](video-summaries/video-summary-AOgUqb62WUQ.md) (Digitale Profis, ohne Video-Zugriff erstellt), [video-summary-zQcatAdqjko.md](video-summaries/video-summary-zQcatAdqjko.md) (Christoph Magnussen), [video-summary-WXqB5U2I_4g.md](video-summaries/video-summary-WXqB5U2I_4g.md) (Eike Diestelkamp), [video-summary-XCn05-EVZdI.md](video-summaries/video-summary-XCn05-EVZdI.md) (iKnowReview), [video-summary-aWvtHsx0u1Y.md](video-summaries/video-summary-aWvtHsx0u1Y.md) (Julian Ivanov, eigene One-Shot-Tests), Vorgeschichte: [video-summary-9lyg9m8D3q0.md](video-summaries/video-summary-9lyg9m8D3q0.md) und [video-summary-t3Tb9HOiwSw.md](video-summaries/video-summary-t3Tb9HOiwSw.md)

Fünf unabhängige Videos befassen sich im Repo inzwischen mit demselben Launch (3./4. September 2026) — Anlass genug für einen eigenen Übersichtsartikel statt fünf isolierter Einzelnotizen. Zwischen den Kanälen bestätigen sich zentrale Fakten mehrfach unabhängig (Preise, Preparedness-Framework-Einstufung), an einer Stelle löst ein späteres Video sogar einen Zahlen-Widerspruch zwischen zwei früheren auf (siehe Benchmark-Tabelle unten).

## Launch-Fakten

- **Datum:** OpenAI kündigte GPT-6 Astra am 3. September 2026 an, gestaffelter Rollout (zunächst Cybersecurity-Programmpartner, dann ChatGPT Plus/Pro/Business/Enterprise, API, AWS) — per WebSearch über mehrere unabhängige Quellen bestätigt (CNBC, Axios, 9to5Mac, Fox Business, Wikipedia, OpenAIs eigene Ankündigung/System Card).
- **Preise:** 10 $ / 1 Mio. Input-Token, 50 $ / 1 Mio. Output-Token — identisch in allen fünf Videos genannt und unabhängig bestätigt; das 2,5-Fache des Vorgängers GPT-5.6 Sol, laut mehreren Sprechern in etwa auf Höhe von Anthropics Claude Fable 5.1. Zum Vergleich: OpenAI o1 Pro kostete historisch 150 $/600 $ pro 1 Mio. Token.
- **Rollout nach Tarif (Christoph Magnussen):** Plus-Accounts sehen Astra zunächst nur in Codex und "ChatGPT Work", nicht im normalen Chat; Pro (auf "Max"), Business und Enterprise erhalten volles Astra im Chat. Nur über Blog-Aggregatoren bestätigt, nicht erstklassig verifiziert.
- Enterprise-Flaggschiffmodelle laufen weiterhin unter "Zero Data Retention".

## Benchmarks — und eine aufgelöste Widerspruchskette

| Benchmark | Astra | GPT-5.6 Sol | Bestätigungsstatus |
|---|---|---|---|
| ARC-AGI-3 | 99,9 % (Provider-Adapter-Harness) / 62,7 % (neutraler Standard-Harness) | 7,8 % | OpenAI-eigene Zahl bestätigt, aber mit Vorbehalt: die 99,9 % hängen an einem teuren, providerspezifischen Test-Harness — Video XCn05-EVZdI benennt diesen Vorbehalt nicht klar, das eingeblendete Chart deutet ihn nur visuell an |
| OSWorld 2.0 (Computer-Use) | 72,6 % | 65,7 % | **Widerspruch aufgelöst:** XCn05-EVZdI behauptete zunächst, Astra schneide mit 62,6 % *schlechter* ab als Sol (65 %) — WXqB5U2I_4g und aWvtHsx0u1Y bestätigen unabhängig per WebSearch 72,6 %/65,7 % (Astra klar besser). Die 62,6-%-Zahl gilt damit als wahrscheinlicher Fehler in einem einzelnen Video, nicht als alternative gültige Testkonfiguration |
| AutomationBench | 41,4 % | 18,1 % | Bestätigt (WXqB5U2I_4g) |
| Zielüberschreitungsrate ("Goal-Hijacking") | 0 % | 48,2 % (ohne Produktions-Guardrails) | OpenAIs eigener Text verknüpft diesen Wert explizit mit dem Hugging-Face-Vorfall (siehe [ki-sicherheitsvorfaelle-sandbox-escapes.md](ki-sicherheitsvorfaelle-sandbox-escapes.md)) |
| Terminal-Bench Science 0.1 | 64,6–64,9 % | — (Claude Fable 5.1: 52,6–52,8 %, Claude Opus 5: 30,2 %) | Bestätigt (aWvtHsx0u1Y), in keinem anderen Repo-Video zu diesem Launch erwähnt |

## Sicherheitseinstufung: "Critical" Cyberfähigkeiten

Astra ist das erste Modell, das im OpenAI-Preparedness-Framework die "Critical"-Schwelle für Cyberfähigkeiten erreicht — mit entsprechenden Zugriffsbeschränkungen für den Cybersecurity-Bereich. Das ist keine neue Überraschung: [video-summary-9lyg9m8D3q0.md](video-summaries/video-summary-9lyg9m8D3q0.md) dokumentierte bereits einen Monat zuvor die deswegen verhängte Trainingspause (RL-Training zwei Wochen gestoppt, ca. 20 % Mehr-Rechenleistung für zusätzliches Monitoring), teils ausgelöst durch den in [video-summary-t3Tb9HOiwSw.md](video-summaries/video-summary-t3Tb9HOiwSw.md) und [ki-sicherheitsvorfaelle-sandbox-escapes.md](ki-sicherheitsvorfaelle-sandbox-escapes.md) dokumentierten GPT-5.6-Sol-Sandbox-Escape. Astra wurde trotz bestätigter "Critical"-Einstufung veröffentlicht, mit den damals angekündigten zusätzlichen Schutzmaßnahmen.

**Auffällige Lücke:** Nur zwei der fünf Videos (AOgUqb62WUQ, zQcatAdqjko teilweise als reiner Screenshot) erwähnen diese Einstufung überhaupt. Die beiden praxisorientierten Videos (WXqB5U2I_4g, aWvtHsx0u1Y) zeigen zwar die eng verwandte Zielüberschreitungs-Kennzahl, ordnen sie aber nicht in den Preparedness-Framework-Kontext ein — wer nur diese Videos sieht, bekommt den Eindruck eines rein produktivitätsgetriebenen, unbedenklichen Rollouts.

## Blackbox-Reasoning und Governance

Mehrere Sprecher (Magnussen, iKnowReview) berichten übereinstimmend, dass Astras Denkschritte (Reasoning-Trace) deutlich schlechter nachvollziehbar seien als bei Vorgängermodellen — laut iKnowReview auf eine neue "recurrent depth"/"looped transformers"-Architektur zurückzuführen (per WebSearch bestätigt). Magnussen leitet daraus eine konkrete Konsequenz ab: Unternehmen bräuchten neue Logging-/Governance-Prozesse, um ein solches Modell verantwortungsvoll einzusetzen — ausdrücklich keine Empfehlung, das Modell deshalb nicht zu nutzen.

## Praxis-Tests (Julian Ivanov, One-Shot, kein Nachbessern)

Als bislang einziges Video mit tatsächlich selbst durchgeführten Tests (nicht nur Presseschau) zeigt aWvtHsx0u1Y drei Ergebnisse:
1. **Videoproduktion:** vollautonome Erstellung eines ~3-minütigen Videos inkl. Avatar-/Stimmklon (HeyGen, ElevenLabs) — vom Host als sehr überzeugend bewertet.
2. **CAD-Konstruktion (FreeCAD, Computer-Use):** 5-Gang-Schaltgetriebe nach echtem Lastenheft — gemischtes Ergebnis, die im Video sichtbare Abgleichtabelle zeigt einen offenen Nachweis und eine Abweichung; der Host selbst ("kein CAD-Experte") kann die Korrektheit nicht abschließend beurteilen.
3. **3D-Rekonstruktion (Blender, MCP):** Wohnung aus einem echten Immobilieninserat sowie die Hamburger Hauptkirche St. Michaelis rein aus Web-Recherche — überwiegend gelungen, mit einem nachvollziehbaren Web-Recherche-Fehler (verwechselte Rettungsringe/Spendenaktion mit Adventskranz).

## Ist das jetzt AGI?

Keine Einigkeit zwischen den Sprechern: Magnussen und iKnowReview kommen unabhängig voneinander zum selben vorsichtigen Schluss — teilweise AGI-artige Fähigkeiten, aber keine vollständige AGI (iKnowReview: Modell bräuchte weiterhin einen menschlichen Auftrag und einen "Harness", wird nicht selbst zur Entwicklung des nächsten Modells eingesetzt). Der Host von WXqB5U2I_4g bricht OpenAIs eigene "AGI-Zeitalter"-Rhetorik am deutlichsten herunter (Vergleich mit "erster Mensch auf dem Mond").

## Für den technischen Team-/Gruppenleiter

1. **Lizenz-/Rollout-Stolperstein:** Bei gemischten Tarifstufen im Team sieht nicht jeder dieselbe Astra-Version (Plus vs. Pro/Business/Enterprise) — relevant für Erwartungssteuerung.
2. **Governance vor Rollout klären:** Die schlechtere Nachvollziehbarkeit des Reasoning-Trace ist ein konkreter Anknüpfungspunkt an den bereits in [ki-guidelines-hardware-unit.md](ki-guidelines-hardware-unit.md) dokumentierten Grundsatz, Ergebnisse zu verifizieren statt zu glauben — hier verschärft, weil der Denkweg selbst schwerer prüfbar ist.
3. **"Critical"-Cyberfähigkeits-Einstufung** ist eine belastbare Information für jede Risikoabschätzung bei weitreichenden Tool-/Systemzugriffen — unabhängig davon, ob ein einzelnes Praxisvideo das erwähnt oder nicht.
4. **FreeCAD-Test als konkretestes Signal für mechanische Konstruktion:** vielversprechend, aber laut Video selbst nicht abschließend geprüft — vor echtem Einsatz durch einen Fachingenieur gegenprüfen lassen, nicht ungeprüft übernehmen.
5. **Kostenkontrolle:** Mehrere Sprecher empfehlen ausdrücklich, nicht automatisch das teuerste Modell/die höchste Denkstufe zu nutzen, sondern nach Aufgabenkomplexität zu staffeln.

## Kernbotschaft

GPT-6 Astra wurde am 3. September 2026 real veröffentlicht und in fünf unabhängigen, im Repo dokumentierten Videos aus unterschiedlichen Blickwinkeln behandelt (reine Presseschau, Praxiserfahrung, Erklärstück, Computer-Use-Fokus, eigene One-Shot-Tests) — die Kernfakten (Preise, Benchmarks, "Critical"-Cyberfähigkeits-Einstufung) bestätigen sich dabei mehrfach unabhängig, ein anfänglicher Zahlen-Widerspruch bei OSWorld 2.0 zwischen zwei Videos ließ sich durch ein drittes, unabhängig verifiziertes auflösen. Auffällig ist eine wiederkehrende Lücke: Praxisorientierte Videos mit Fokus auf Produktivität erwähnen die sicherheitsrelevante "Critical"-Einstufung durchgehend nicht, obwohl sie eng verwandte Kennzahlen (Zielüberschreitungsrate) zeigen — für eine vollständige Risikoeinschätzung lohnt sich daher der Blick über ein einzelnes Video hinaus.

## Themen-Tags

GPT-6 Astra, OpenAI, ChatGPT, Codex, Preparedness Framework, Critical Cyberfähigkeiten, ARC-AGI-3, OSWorld 2.0, AutomationBench, Terminal-Bench Science 0.1, Zielüberschreitung/Goal-Hijacking, API-Pricing, Blackbox-Reasoning, Governance, Computer-Use, FreeCAD, Blender, MCP, AGI, Digitale Profis, Christoph Magnussen, Eike Diestelkamp, iKnowReview, Julian Ivanov
