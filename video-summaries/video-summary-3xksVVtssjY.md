# "Claude Opus 5.5 ist unfassbar! Alles was du jetzt wissen musst | KI-NEWS"

**Kanal:** Everlast AI (Host: Leonard Schmedding, live aus San Francisco)
**URL:** https://www.youtube.com/watch?v=3xksVVtssjY
**Länge:** 33:34
**Zusammenfassung erstellt:** 2026-09-29

*Hinweis zum Ablauf: Keine nativen Untertitel. Transkript per Whisper (Replicate), in 7 Häppchen à ca. 5 Min. transkribiert und zusammengesetzt (348 Segmente; einzelne Stellen verstümmelt, z. B. "GBT" = GPT, "Soul" = Sol, "Cloud" = Claude, "Andon/Anden" = Andon, "Muse" teils falsch erkannt). 80 Frames vorhanden, davon nur eine Stichprobe (ca. 5) angesehen; Kernzahlen stammen aus dem Transkript und wurden nur punktuell mit Frames abgeglichen.*

---

## Aufhänger

Wöchentliches News-Format: Claude Opus 5.5 erscheint, OpenAI kontert laut Host "nur zwei Stunden später" mit GPT-6 Sol und GPT-6 Luna. Opus 5.5 sei "seit langem mal wieder ein richtig großes Update" und schlage Fable 5.1 bei niedrigeren Kosten. Danach: Praxistests, Andon Market, Claude-Biologie-Entdeckung, China-Open-Weights, Meta Muse Charm, USA/China-Politik, Regulierungsdebatte. Siehe auch [video-summary-9EOqBiMR3z4.md](video-summary-9EOqBiMR3z4.md) (anderer Kanal, gleiche Modell-Welle).

## Opus 5.5 laut Anthropic und Benchmarks (~01:41–03:15)

- Erstes Modell der neuen Claude-5.5-Familie (Sonnet/Haiku 5.5 erwartet, Host-Spekulation). Anthropic: Niveau von Fable 5.1, im Betrieb rund **40 % günstiger als Opus 5**.
- **Terminal-Bench 4.0:** Opus 5.5 66,4 % vs. Fable 5.1 55,8 % vs. GPT-6 Astra 57,9 %. Cursor Bench 57,8 % vs. 51,8 % (Fable). Vorne auch bei GDPval, Humanity's Last Exam und OSWorld 2.0; Astra bleibt bei automatisierten Business-Workflows und agentischer Forschung leicht vorne.
- Frame: Terminal-Bench-Diagramm (Genauigkeit über Kosten pro Versuch, log) zeigt Opus 5.5 auf jeder Effort-Stufe über den Vorgängern.
- Host-Stimmung: Opus 4.7/4.8/5 waren für ihn kein echtes Upgrade gegenüber 4.6; 5.5 fühle sich wieder wie 4.6 an ("nach Hause kommen").

## Praxisbeispiele Community (~03:15–04:25)

- "Sketch to Simulation": von der Handzeichnung zur Simulation. Host-These: Bild-/Videomodelle werden an Bedeutung verlieren, weil Modelle Szenen per Three.js/Blender selbst bauen.
- Frame: Ein X-Post zeigt einen Cartoon-Animationsfilm in Three.js mit Opus 5.5 (Max Effort), **7 h 58 min und 173,23 $**.
- Mehrere Agents bauen ein komplettes CRM; vier Agents produzieren 1,5 h autonom ein Erklärvideo.

## Andon Labs: Benchmarks und Andon Market (~04:25–10:55)

- **Vending-Bench:** GPT-6 Sol schneidet laut Host mit Abstand am besten ab und ist günstig; Opus 5.5 ist hier *schlechter als Opus 5*. **Blueprint Bench** (aus ca. 20 Innenfotos je Wohnung einen 2D-Grundriss erzeugen, 50 Wohnungen): Opus 5.5 am besten.
- **Andon Market** (Boutique in San Francisco, Betreiber-Agent "Luna", derzeit vermutlich Opus 5.5, davor Opus 4.8): Agent kauft ein, setzt Preise, schaltet Stellenanzeigen, stellt Menschen ein und steuert sie per Slack, betreibt Social Media. Bestseller Kerzen ("möglicher Move 37"). Startkapital 100.000 $, nach ca. vier Monaten (April bis August) nur noch ca. **53.000 $** Kontostand, also klar im Minus, Tokenkosten kommen dazu. Menschen (z. B. Kassiererin) noch vor Ort, laut Host eher aus Sicherheitsgründen. Zweites Projekt: Andon Café in Stockholm, in Woche 1 ca. 44.000 SEK Umsatz.

## Tipps zu Effort und Token (~11:11–12:40)

- Nach Nathan Lambert: bei agentischem Coding ist **Medium Effort** effektiver als High/Extra High; selbst Max bringe laut Host keinen Mehrwert bei deutlich höheren Kosten. Gleiches war schon bei Astra so.
- **Neu in Opus 5.5:** Effort lässt sich mitten in der Session wechseln, ohne den Prompt-Cache zu verlieren (Frame: Post mit Hinweis "Claude Code v2.1.280+", gilt nicht bei Bedrock/Vertex). Der Host widerruft damit seinen früheren Rat "nie den Effort innerhalb einer Session wechseln".
- Claude Code wählt bei Erreichen des 5-Stunden-Limits einen sauberen Stoppunkt statt mitten in der Aufgabe abzubrechen.

## OpenAI, Ausblick, "EQ" (~12:43–13:44)

- Gerücht: OpenAI wurde von Opus 5.5 überrascht; Host erwartet beim OpenAI Developer Day (nächste Woche) größere Updates (z. B. Astra 6.1, Muse-Konkurrent).
- Behauptung: Modelle erreichen "EQ 151 im Mensa-Norway-Test", der Test sei saturiert. Unklare Einordnung (Mensa Norway ist ein IQ-Test).

## Gast-Test: Grundriss zu begehbarem 3D-Modell (~13:44–24:00)

Gastbeitrag (Marcel): Opus 5.5 vs. GPT-6 Sol, gleicher Prompt: aus einem Maklergrundriss (2-Zimmer-Bungalow) in Blender ein 3D-Modell bauen, per Unreal Engine begehbar machen, mit Ikea-Möbeln ausstatten, Deadline 8 Uhr früh.

| | Opus 5.5 | GPT-6 Sol |
|---|---|---|
| Laufzeit | ca. 3 h (Angabe im Transkript uneinheitlich) | 13 h 46 min (bis zur Deadline) |
| Tokens gesamt | 803 Mio. | 167 Mio. (ca. 4,8x weniger) |
| selbst geschriebene Tokens | ca. 1,36 Mio. | ca. 94.000 (ca. 14x weniger) |
| Kosten | 199,13 $ | 68,36 $ (ca. 3x günstiger, nicht 5x) |

- Kostengrund: OpenAI berechnet ab 272.000 Tokens pro Anfrage den doppelten Satz für die gesamte Anfrage; 338 von 436 Anfragen lagen darüber (Frame bestätigt die Tabelle).
- **Ergebnis:** Opus: Grundriss korrekt, Außenbereich frei, Ikea-Preise/Maße/Namen je Möbel, Bibliothek, Möbel per Tastatur verschiebbar und ersetzbar, zusätzlich natives Fenster auf dem Mac; leichtes Wand-Flackern. Sol: Wand im Eingangsbereich gebaut, Raumstruktur nicht sauber, schwebende Tischplatte, keine Preise, keine Möbelinteraktion, deutlich mehr Nacharbeit nötig. Fazit: Opus deutlich besser, aber teurer.

## Claude findet molekulare Maschine (~24:16–26:00)

- Anthropic (neues Biolab in SF): Claude habe nach Literatur- und Genomdaten-Recherche eine "molekulare Maschine" entdeckt, die laut Dario Amodei ein neuer Gen-Editing-Mechanismus sein könnte; Claude schlug Experimente vor, das Team führte sie durch. Funktion und Nutzen noch vage.
- Amodeis These: Mathe-Kurve 2023 (Schülerniveau) über 2024/2025 bis zu offenen Problemen 2026, dieselbe Kurve jetzt in der Biologie; Ziel aus "Machines of Loving Grace": die meisten Krankheiten in 5 bis 10 Jahren heilbar.
- Ausrede-Einwand (Biologie braucht Experimente) zählt für Anthropic nicht, da Ergebnisse binnen Wochen geprüft werden.

## China, Open Weights, Meta, Politik (~26:04–33:20)

- **Xiaomi MiMo 2.6 Pro:** Open Weights, laut Benchmarks knapp hinter GPT-5.6 Max, deutlich günstiger. Alibaba stellt Qwen4 (Max, Flash, Plus, 27B) vor.
- Host (unter Berufung auf einen Artikel des Investors David Cheng): Abstand zwischen Open-Weights- und US-Frontier-Modellen ist größer als in Benchmarks; wegen fehlender Chips/Rechenleistung, Benchmaxxing-Verdacht auch chinesischer Researcher; mit Opus 5.5 ca. 6 Monate Vorsprung. Bei Long-Horizon-Agenten klar zurück, für E-Mail-Automation/First-Level-Support genügten lokal gehostete chinesische Modelle (Kosten, Datenschutz).
- **Meta Muse Charm:** handflächengroßes 5G-Hardwaregerät (Schlüsselanhänger) mit Sprachverbindung zum Muse Agent, dazu neue VR-Brille, Audio-Glasses, Ray-Ban Meta Gen 3, FDA-zertifizierte Hörgeräte.
- **Politik:** Trump-Xi-Treffen; beide Seiten wollen laut Host nicht verlangsamen (Huawei: "müssen weiter beschleunigen"); "KI" soll in den USA künftig "Superintelligenz" heißen, Xi habe angeblich zugestimmt (unbelegte Host-Aussage).
- **Regulierung (Meinungsteil):** Prinz Harry fordert Regulierung, Hillary Clinton warnt vor Open-Weights-Modellen aus der Garage. Host lehnt Regulierung ab, Analogie Spam-E-Mail (offene Standards DKIM/DMARC/SPF statt Gesetze), verweist auf einen "Huggingface-Vorfall", bei dem GLM-Open-Weights zur Abwehr halfen. Position: "Defensive Co-Scaling" statt staatlicher Regulierung. Klar als Meinung des Hosts.

## Für Hardware-Entwickler und Team-Lead

- **Effort-Steuerung im Team:** Medium als Standard, Effort-Wechsel in laufender Session ist jetzt cache-schonend (Claude Code ab v2.1.280, nicht bei Bedrock/Vertex). Direkt in [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md) übernehmbar; ergänzt frühere Warnung vor Effort-Wechsel in [claude-oekosystem-ueberblick.md](../claude-oekosystem-ueberblick.md).
- **Kosten realistisch messen:** Der 3D-Vergleich zeigt: Listenpreis (5x) vs. Realkosten (3x) wegen Tokenverbrauch und OpenAIs Aufschlag ab 272k Tokens. Lange Kontexte (Datenblätter, Spezifikationen) können bei OpenAI die Rechnung verdoppeln. Vor Modellwahl eigene Referenzaufgabe messen.
- **Grundriss/Zeichnung zu 3D:** Der Test (2D-Plan zu Blender/Unreal-Modell) und Blueprint Bench sind für Mechanik-/Gehäuse-/Layout-nahe Aufgaben inspirierend. Aber: Anwendungsfall Immobilie, keine Toleranzen, keine Normen. Kein Beleg für Eignung bei Schaltungs- oder Fertigungszeichnungen.
- **Autonomie ist teuer:** Ein 8-h-Lauf kostete rund 173 $ (Cartoon) bzw. 199 $ (3D-Modell). Bei unbeaufsichtigten Läufen Budgetgrenzen setzen.
- **Andon Market als Warnung:** Vollautonomer Betrieb verbrennt Kapital (100k auf 53k) und braucht weiter Menschen für physische Aufgaben.
- **Meta Muse Charm:** dedizierte Agent-Hardware im Schlüsselanhänger-Format, interessant als Produktbeispiel für KI-Wearables (Formfaktor, 5G, Sprache).
- Team schreibt keine Software: Der Nutzen liegt eher bei Skripting, Auswertung, Dokumentation und Visualisierung als bei Coding-Benchmarks.

---

## Kernbotschaft
Opus 5.5 ist laut Benchmarks und den gezeigten Praxistests ein starkes Update (bestes Modell im 3D-Grundriss-Test), aber nicht billiger im Ergebnis: hoher Token-Verbrauch, in Vending-Bench schlechter als Opus 5. Praktisch wichtig: Medium Effort als Standard und Effort-Wechsel ohne Cache-Verlust. Der Rest ist Mix aus News (Claude-Biologie-Fund, MiMo, Muse Charm) und stark meinungsgefärbter Host-Politik (gegen Regulierung).

## Themen-Tags
Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, GPT-6 Astra, Fable 5.1, Terminal-Bench 4.0, Vending-Bench, Blueprint Bench, Andon Labs, Andon Market, Thinking Effort, Prompt Caching, Token-Kosten, Blender/Unreal, Claude Biologie-Entdeckung, Gen-Editing, MiMo, Qwen4, Open Weights, China, Meta Muse Charm, KI-Regulierung, Everlast AI

## Zu prüfen
- **Per WebSearch bestätigt:** (a) Claude-Entdeckung eines neuen Enzymsystems ("ART", in Staphylococcus-Phagen), Anthropic-Meldung und Amodei-Post vom ca. 24.09.2026; Funktion und Nutzen laut Berichten weiter unklar, passt zur vorsichtigen Darstellung im Video. (b) Andon-Labs-Beitrag "Opus 5.5, GPT-6 Sol and Grok 4.7 on Vending-Bench": Sol sehr gut und billig, Opus 5.5 schlechter als Opus 5. Abweichung: Dort schlägt **Grok 4.7** (10.537 $) auch Opus 5.5 (9.235 $), im Video nicht erwähnt.
- **Zahlenspannung Terminal-Bench:** Suchergebnisse nennen für Opus 5.5 auf Vals AI 61,6 % (Astra 57,1 %); die 66,4 % im Video/Anthropic-Chart gelten laut Suche für xhigh-Effort, Astra-Wert 57,9 % für high. Vergleich also nicht bei gleichem Effort. Nicht selbst nachgeprüft.
- **Nicht geprüft:** 40 % Kostenreduktion (im Video-Vergleich Realkosten höher, vgl. Widerspruch in 9EOqBiMR3z4), Cursor-Bench-Zahlen, Angaben zu Andon Market (53k $), Stockholm-Café (44.000 SEK), Claude Code v2.1.280 und Cache-Verhalten (nur per Frame gesehen), "EQ 151 / Mensa Norway" (unplausibel formuliert), MiMo/Qwen4-Aussagen, Muse Charm, Trump-Xi-Treffen, "KI heißt jetzt Superintelligenz", Prinz Harry/Clinton-Zitate, "Huggingface-Vorfall", David-Cheng-Artikel, Marcels 3D-Test (einzelner Lauf, nicht reproduzierbar, Laufzeit-Angabe im Transkript uneinheitlich: "2 Stunden" bzw. "nach drei Stunden").
- **Framing:** Reißerischer Titel ("unfassbar"), Host bewirbt eigene Reports/Zweitkanal; Regulierungs- und China-Aussagen sind Meinung. Frame-Diagramm nennt "GPT-5.6 Sol" während Sprecher "GPT-6 Sol" sagt (Bezeichnung in den Notizen uneinheitlich).
- **Querverweise (nicht editiert):** [video-summary-9EOqBiMR3z4.md](video-summary-9EOqBiMR3z4.md) (gleiches Modell-Update, Artificial-Analysis-Sicht: Kosten pro Aufgabe ähnlich wie Opus 5; konsistent mit hohem Token-Verbrauch hier). Effort-Tipp deckt sich mit [video-summary-IYzgxWs4sZ4.md](video-summary-IYzgxWs4sZ4.md). [china-ki-macht.md](../china-ki-macht.md) und [lokale-ki.md](../lokale-ki.md) zum Open-Weights-Vorsprung/Benchmaxxing; [ki-forschungsdurchbrueche-2026.md](../ki-forschungsdurchbrueche-2026.md) zur Claude-Biologie-Entdeckung (dort bisher nicht enthalten); [ki-risiko-warnungen.md](../ki-risiko-warnungen.md) und [ki-sicherheitsvorfaelle-sandbox-escapes.md](../ki-sicherheitsvorfaelle-sandbox-escapes.md) zum Regulierungs-Streit. Opus 5.5 selbst ist in den Root-Übersichten noch nicht behandelt.

## Nachtrag Faktencheck (2026-09-29)

Unabhängiger Faktencheck (Recherche-Agents plus skeptische Prüf-Agents, Primärquellen per WebFetch). Der bisherige Text oben bleibt unverändert; Abweichungen und Bestätigungen stehen hier. Konfidenz jeweils in Klammern.

- **Enzymsystem (hoch):** Anthropic-Meldung vom 23.09.2026: Reverse-Transkriptase-System ("array-associated reverse transcriptases") in Bakteriophagen-DNA, CRISPR-ähnliche Architektur, Funktion unbekannt; ca. 950 Claude-Agenten, 21 Stunden, 210 Mio. Tokens.
- **Vending-Bench 2 (hoch):** Sol 14.428 $, Grok 4.7 10.537 $, Opus 5 11.182 $, Opus 5.5 9.235 $ (Durchschnitt über 6 Läufe); Opus 5.5 also schlechter als Opus 5. Grok 4.7 vor Opus 5.5 fehlt im Video.
- **"EQ 151 / Mensa Norway" (mittel):** Gemeint ist ein IQ-Wert; TrackingAI bewertet den Mensa-Norway-Test (35 Fragen), mehrere Modelle erreichen das Maximum 151, der Test gilt als saturiert; Quellen schwach.
- **Terminal-Bench:** siehe Nachtrag in [video-summary-9EOqBiMR3z4.md](video-summary-9EOqBiMR3z4.md); der Vergleich ist nicht effort-gleich.
- **Effort-Wechsel ohne Cache-Verlust ab Claude Code v2.1.280 (mittel):** Belegt nur durch einen X-Post einer Anthropic-Mitarbeiterin (Lydia Hallie); Changelog und Doku sagen dazu nichts, Drittquellen deuten auf uneinheitliches Verhalten hin. Als "laut Anthropic-Mitarbeiterin auf X" lesen.
- **Nicht geprüft:** 40 %-Kostenclaim im Detail (siehe 9EOqBiMR3z4), Andon-Market-Zahlen, MiMo/Qwen4, Muse Charm, Trump-Xi-Aussagen, 3D-Grundriss-Test.
