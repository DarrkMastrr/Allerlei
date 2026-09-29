# "Es beginnt: KI verbessert sich jetzt selbst"

**Kanal:** Everlast AI (Leonard Schmedding)
**URL:** https://www.youtube.com/watch?v=SRvVdEoRnew
**Länge:** 22:26
**Zusammenfassung erstellt:** 2026-09-29 (Neufassung mit Transkript; die erste Fassung vom selben Tag beruhte nur auf Frames)

**Hinweis zum Ablauf:** Keine YouTube-Untertitel. Der erste Whisper-Lauf scheiterte am Replicate-Timeout (6 Minuten, bekannter Fehler bei langem Audio), der zweite Lauf mit 5-Minuten-Chunks (5 Chunks, 318 Segmente) lieferte ein vollständiges deutsches Transkript. Einzelne Segmente sind Whisper-Wiederholungsartefakte, Eigennamen teils verhört (z. B. "Colonel" = Kernel, "Diebsieg" = DeepSeek, "Entropic" = Anthropic, "METER" = METR, "Norm Brown" = Noam Brown). Frames wurden für diese Fassung nicht erneut gesichtet; die Frame-Auswertung der ersten Fassung ist nur dort übernommen, wo sie das Transkript ergänzt.

---

## Aufhänger: Liu Shengyu und "mein Talent im Gestern begraben" (0:00-4:30)

Der 23-jährige DeepSeek-Forscher Liu Shengyu (Turing-Klasse Peking-Universität, seit April 2025 bei DeepSeek, schreibt GPU-Kernel, zuletzt den Attention-Kernel von DeepSeek V4.1) veröffentlichte einen ca. 3.000 Zeichen langen Text, der binnen 48 Stunden Platz 1 auf der Plattform Zhihu erreichte. Kernaussage: In sechs bis zwölf Monaten werden von KI geschriebene Kernel mit hoher Wahrscheinlichkeit so gut sein wie seine oder besser. Er nutzt die Stricken-Parabel (Handwerker, den die Strickmaschine "zermalmt") und will, wenn schon gestürzt, sich selbst stürzen. Am Abend nach der Veröffentlichung stellte er klar, es gehe nicht um Angst vor Arbeitslosigkeit, er müsse vom Handwerker zum "Piloten eines Mechs" umsatteln, der Agenten steuert.

Belege des Sprechers für den Trend:
- **Anthropic:** Claude führe inzwischen 26 % der eigenen KI-Forschung eigenständig (im Februar unter 1 %).
- **OpenAI:** 3,1 Agenten-Arbeitstage pro menschlichem Arbeitstag; seit Juni laufe die Rechenzeit der Agenten länger als die Arbeitszeit der Menschen.
- Bei Google arbeiteten laut Reuters über 1.000 Forschende auf dieses Ziel hin.
- **Dario Amodei** fordert seit dem 12. September ein Tempolimit für genau diese Fähigkeit; Altman, Hassabis und Musk stimmten am selben Tag öffentlich zu.

## Was "rekursive Selbstverbesserung" bedeutet (4:30-9:30)

- Nicht die KI verbessert sich, sondern "das Verbessern selbst": Mehr Geld und Compute in Forschung führen zu mehr Effizienz, und die Beschleunigung beschleunigt den nächsten Schritt.
- **Jürgen Schmidhuber** führt das Konzept (Meta-Lernen, Selbstverbesserung) auf seine Diplomarbeit von 1987 zurück: ein System, das seinen eigenen Lernalgorithmus anschauen und austauschen darf.
- **Google DeepMind unterscheidet vier Schleifen:** (1) Code: KI schreibt besseren Code für den Nachfolger, (2) **Hardware**: KI entwirft bessere Chips bis in die Fertigung, Beispiel OpenAIs erster Inferenzchip **Jalapeño**, in rund neun Monaten fertig, weil ein internes Modell am Entwurf mitgearbeitet hat, (3) Daten: KI erzeugt und wählt ihr Trainingsmaterial (AlphaZero-Analogie), (4) Arbeitsteilung: Agenten-Kollektive, die sich spezialisieren. Beim "Hugging-Face-Vorfall" sei aus 1.200 Agenten eine Fähigkeit entstanden, die keiner allein hatte, ohne dass sich ein Modellgewicht änderte.
- **DeepMind ist bei der vierten Schleife skeptisch:** Menschliche Spezialisierung kostet Jahre, ein Modell wird per Prompt zum Spezialisten. **Marcus Hutter:** eine Frage der Agentenzahl (1.000 Menschen könnten keine moderne Zivilisation aufbauen, 7 Milliarden schon). **Noam Brown (OpenAI):** publiziert bis ca. 16 Agenten gemessen; 10.000 Agenten zu untersuchen sei zu teuer. Der Engpass sind also Kosten, die laut Sprecher (Zitat Schmidhuber: alle fünf Jahre 10x billiger) von selbst sinken.

## Wo KI schon übermenschlich ist: prüfbare Aufgaben (10:00-13:30)

- Liu Shengyus Fall gehört zur ersten Schleife, der schnellsten und einzigen, die sich heute schon nachprüfen lässt.
- **Anthropics Kernel-Test** (Code eines kleinen Trainingsmodells möglichst schnell machen, ohne Korrektheitsprüfungen zu verlieren): Claude Opus 4 (Mai 2025) ca. 3x, **Mythos (April 2026) laut gesprochener Aussage 250x**, ein erfahrener Mensch brauche 4-8 Stunden für 4x. Anthropic: "in weniger als einem Jahr von sehr hilfreich zu übermenschlich". Einschränkung des Sprechers: Das gilt nur, wo die Maschine selbst messen kann, ob sie besser wurde ("entweder schneller oder nicht").
- **METR-Studie** (61 menschliche Experten, sieben reale Forschungsumgebungen vs. beste Agenten): bei 2 Stunden Zeitbudget erreichten Agenten das Vierfache der Menschen, bei 8 Stunden zogen die Menschen vorbei, bei 32 Stunden lagen sie beim Doppelten. Grund: KI probiert schnell viele Varianten, erkennt aber schlecht, wenn ein ganzer Ansatz in die Irre führt. "Kernelschreiben ist die 2-Stunden-Aufgabe, KI-Forschung die 32-Stunden-Aufgabe."
- **Autonomie-Skala (5 Stufen), 491 ausgewertete Arbeiten:** Stufe 1 43,8 %, Stufe 2 31,6 %, Stufe 5 nur 5,9 %. Selbst AlphaEvolve steht auf Stufe 2: 4x4-Matrixmultiplikation mit 48 statt 49 Multiplikationen (erste Verbesserung seit 1969), gewinnt im Schnitt 0,7 % der weltweiten Google-Rechenkapazität zurück und beschleunigte einen Gemini-Trainings-Kernel um 23 %; Zielbewertung und Auswahlregeln kommen von Menschen.
- **Sakana AI (Robert Lange):** verbessert wird nur Scaffolding und Agenten-Loop, nicht die Modellgewichte. **Dream RSI (Google):** Agenten verbessern ihre Suchstrategie durch "Träumen" (Replay früherer Versuche), sparen bis zu 162x Agenten-Aufrufe; Abnahmekriterien bleiben menschlich.
- Ein Überblickspaper unterscheidet strukturelle von wirksamer Selbstverbesserung; für Softwareentwicklung sei die wirksame nie demonstriert worden. Evolutionäre Systeme mit Sprachmodellen konvergieren und bleiben stehen; niemand weiß, wie man sie offen hält.

## Grenzen: kein plötzlicher Sprung (15:46-17:45)

- Engpass ist nicht das Denken, sondern das Ausprobieren: Experimente brauchen Zeit, Chips und Strom; ein dreiwöchiges Training beschleunigt keine Maschine.
- Studie vom Juli 2026: Agenten bekamen sechs Tage und mehrere tausend Dollar für zwei echte unveröffentlichte Forschungsarbeiten; das Engineering gelang, die Forschungsfrage nicht, beide Ergebnisse wurden von den Original-Autoren abgelehnt. Nature-Überschrift (August): "KI ist noch nicht so weit, sich selbst zu erforschen."
- Diskussionsrunde vom 11. September (u. a. John Schulman): KI-Forscher könnten in etwa zwei Jahren 10x Produktivität erreichen, Fortschritt sich ab 2028 dramatisch beschleunigen; Spitzenleistung in jedem Computerfeld in 3 bis 10 Jahren. Es gebe keine Gesetzmäßigkeit, wann eine Selbstverbesserungskurve flacher wird.

## Risiken und Tempo-Debatte (17:45-20:30)

- Amodei fordert am 12. September, das Tempo zu drücken, ausdrücklich wegen rekursiver Selbstverbesserung. OpenAIs Chefwissenschaftler (Jakub Pachocki) schrieb sechs Tage vorher, man wisse noch nicht, wie man sicher den ganzen Weg zu ausgerichteter, vollständiger rekursiver Selbstverbesserung gehe.
- **Schmidhuber unterschrieb das Bremsen nicht:** Waffenforscher, Geheimdienste und Firmen würden weitermachen (Wettbewerb mit China; "die kann man nicht auslöschen durch irgendwelche Briefe"). Unvorhersagbarkeit sei kein Argument (auch bei Kindern unbekannt), das Universum werde seit Milliarden Jahren komplexer, es sei "nicht aufzuhalten". Die Grenze sieht er woanders: Seine Selbstverbesserung laufe bisher nur "hinter dem Bildschirm"; ernst werde es, wenn der Kreislauf die Hardware erfasst.

## Folgen für Arbeit (20:30-22:26)

Automatisiert wird zuerst nicht das Schwierige, sondern das **Prüfbare**. Markus Hutter/Sutter (Namen im Transkript unsicher) schätzt, heutige Systeme könnten im Prinzip die Hälfte aller Bürotätigkeiten übernehmen, was bei Unternehmen noch nicht angekommen sei (bestätigt der Sprecher aus eigener Projekterfahrung). Übrig bleibt, was keine Maschine für sich bewerten kann: entscheiden, was getan werden soll, und beurteilen, ob das Ergebnis taugt (Schulman: "Ziele definieren" bleibt am längsten beim Menschen). Empfehlung: operative Arbeit an Agenten abgeben, selbst Aufgabenauswahl und Ergebnisbeurteilung lernen. Schluss mit Kommentar-Aufruf an die Zuschauer.

---

## Für den Hardware-Team-Lead: Relevanz

- **Jalapeño (neun Monate bis Tape-out mit KI-Unterstützung)** ist das direkteste Hardware-Beispiel; ein Halbleiter-Konzernfall mit eigenem Modellzugang, nicht ohne Weiteres auf Board-/Systementwicklung übertragbar (eigene Einordnung).
- **Kriterium für KI-Einsatz:** Sie lohnt dort, wo Ergebnisse schnell und objektiv messbar sind (Auswertungsskripte, Simulationsläufe, Optimierung gegen Kennzahlen), nicht bei offenen Entwurfs- und Urteilsfragen. Das deckt sich mit METR-Befund (Kurzaufgaben schlagen KI die Menschen, Langzeitaufgaben nicht) und mit der Rollenaussage am Ende.
- **Teamkompetenzen:** Spezifizieren und Prüfen werden wichtiger als Ausführen; für die Team-Planung relevant.
- Konkrete Handlungsempfehlungen für Hardware-Teams enthält das Video nicht (Frontier-Lab-Perspektive).

---

## Kernbotschaft

Rekursive Selbstverbesserung hat begonnen, aber gestuft: Wo die Maschine ihr Ergebnis selbst messen kann (Kernel, Optimierung, Chip-Design-Teilaufgaben), übertrifft sie Menschen schon deutlich; bei offener Forschung scheitert sie an Urteil und Richtungswechseln, und die meisten Selbstverbesserungs-Arbeiten sind stark menschengeführt. Ob die Kurve steil bleibt oder abknickt, weiß laut Video niemand. Die Lab-Chefs fordern ein Tempolimit, Schmidhuber hält es für nicht durchsetzbar. Für Menschen bleibt vor allem Zielsetzung und Bewertung.

## Themen-Tags

Rekursive Selbstverbesserung, R&D Automation Index, Anthropic, OpenAI, DeepSeek, Liu Shengyu, Kernel-Optimierung, Claude Mythos, Jalapeño, KI-Chipdesign, AlphaEvolve, Dream RSI, METR, Jürgen Schmidhuber, Marcus Hutter, John Schulman, Noam Brown, Pacing/Tempo bremsen, KI-Arbeitsmarkt, Everlast AI

## Zu prüfen

- **Widerspruch zur ersten Fassung (Frames):** Die Einblendung zeigte für Mythos ca. **52x**, gesprochen wird **250x** (mit Einordnung "Mensch braucht 4-8 h für 4x"). Nicht geklärt, welche Zahl stimmt (Frame: eventuell Zwischenstand oder andere Metrik); Anthropic-Originaltext prüfen, bevor eine Zahl weiterverwendet wird. Die erste Fassung nannte außerdem irrtümlich "Strassen 2x2 mit 7 statt 8 Multiplikationen"; laut Transkript geht es um AlphaEvolve (4x4, 48 statt 49).
- **Per WebSearch bestätigt (erste Fassung):** Anthropic "R&D Automation Index" (Claude 26 % "AI leads", Selbstmessung, Epoch-AI-Skala; Anthropic betont, dass Claude in keiner Kategorie vollständig autonom arbeitet) sowie Amodeis Essay "We Must Pace the Frontier" (12.09.2026); Jalapeño in neun Monaten bestätigt in [video-summary-fmMCg6dyWpQ.md](video-summary-fmMCg6dyWpQ.md).
- **Nicht geprüft:** OpenAI "3,1 Agenten-Arbeitstage pro Tag" (Selbstangabe eines Labors), METR-Zahlen (61 Experten, 2/8/32 h), Survey n = 491 und Stufenverteilung, AlphaEvolve-Zahlen (0,7 %, 23 %, 162x Dream RSI), Studie vom Juli 2026 und Nature-Überschrift, Aussagen der Diskussionsrunde vom 11. September, Liu-Shengyu-Text (Herkunft: Zhihu, laut Sprecher).
- **Namen im Transkript unsicher:** "Markus Sutter/Hutter" (Marcus Hutter im Bild), "Jakub Batschotzki" (= Pachocki), "Modhi" (= Amodei). Zuordnung "Zitate Schwituba/Schmidhuber" nicht verifiziert.
- **Eigeninteresse:** Der Sprecher ist Gründer von Everlast AI (KI-Projekte für Unternehmen) und verweist auf eigene Gespräche mit Forschern; die Interview-Ausschnitte sind Zuspielungen, deren Originalkontext unbekannt ist. Der Titel "Es beginnt" ist als Tendenz belegt, nicht als autonome Selbstverbesserung.
- **Cross-Referenz:** Überschneidung mit [ki-forschungsdurchbrueche-2026.md](../ki-forschungsdurchbrueche-2026.md) (Abschnitt "Selbstverbesserung: real, aber eng begrenzt", n_lYxc5WUlQ, Sakana AI) und [video-summary-kvy01SpQp8s.md](video-summary-kvy01SpQp8s.md) (Paper "From AGI to ASI"). Kein Widerspruch; das Video liefert neue Zahlen (26 %, Kernel-Speedup, METR) und stützt die "eng begrenzt"-Einordnung. Die Schmidhuber-Position (Tempolimit nicht durchsetzbar) steht im Kontrast zu [ki-risiko-warnungen.md](../ki-risiko-warnungen.md) und zur Regulierungs-Kritik in 38qNMuPd0eo.

## Nachtrag Faktencheck (2026-09-29)

Unabhängiger Faktencheck (Recherche-Agents plus skeptische Prüf-Agents, Primärquellen per WebFetch). Der bisherige Text oben bleibt unverändert; Abweichungen und Bestätigungen stehen hier. Konfidenz jeweils in Klammern.

- **Korrektur zur Mythos-Zahl (hoch):** Die Anthropic-Seite (anthropic.com/institute/recursive-self-improvement) nennt für Claude Mythos Preview (April 2026) **~52x**, für Opus 4 (Mai 2025) ~3x, Mensch 4-8 h für 4x. Die im Video gesprochene "250x" ist falsch; die Frame-Angabe 52x stimmt. Anthropic warnt selbst, das absolute Vielfache sei nicht der Anker.
- **R&D Automation Index (hoch):** Claude "leads" (AL4) 26 % der AI-R&D-Arbeit im August 2026, Februar <1 %; Selbstmessung, nicht extern verifiziert.
- **OpenAI 3,1 Agenten-Arbeitstage (mittel):** Essay der CFO Sarah Friar vom 08.09.2026 ("The Work Now Within Reach"), Verhältnis der Agenten-Laufzeit zur Arbeitszeit der Forschungsorganisation (Stand Mitte August), keine 3,1-fache Forschungsproduktivität; bestätigt über unite.ai, OpenAI-Original nicht abrufbar.
- **METR RE-Bench (hoch):** 7 Umgebungen, 61 Experten (71 Versuche à 8 h); der beste Agent erreicht bei 2 h das 4-Fache der Experten, bei 32 h liegen Menschen beim ca. 2-Fachen. Studie von 2024/25, nicht neu.
- **Survey (hoch):** arXiv 2609.11873 "The Last AI Built by Humans" (10.09.2026, 35 Autoren), Rahmenpapier mit Survey-Anhang; 491 Arbeiten, L1 43,8 / L2 31,6 / L3 13,0 / L4 5,7 / L5 5,9 %. Einordnung von AlphaEvolve auf Stufe 2 dort nicht auffindbar.
- **AlphaEvolve/Dream RSI (mittel bis hoch):** 48 statt 49 Multiplikationen (4x4 komplex), 0,7 % Rechenleistung, 23 % Kernel-Beschleunigung bestätigt. Dream RSI: "bis zu 162x weniger Agenten-Aufrufe" bestätigt; das Paar "51.200 auf 317" (Recherche-Agent) ist falsch zusammengesetzt, nur die 162x als "bis zu" verwenden.
- **Open-ended-Research-Paper (hoch):** arXiv 2607.27191, v1 am 29.07.2026 (nicht 10.08.), sechs Tage, zwei NeurIPS-2026-Einreichungen, Autoren lehnen beide Ergebnisse ab; Nature-Titel "AI isn't ready to research itself" (Text nicht abgerufen).
- **Dwarkesh-Runde 11.09.2026 (mittel):** Schulman, Millidge, O'Neill; ca. 10x Produktivitätsgewinn und "Ziele definieren" als letzter menschlicher Job belegt; "~2 Jahre" und "3-10 Jahre" sind eine Panel-Bandbreite und nicht als Einzelaussage Schulmans verifiziert; "ab 2028" steht dort nicht als Zitat, die Runde zweifelt eher an baldiger rekursiver Selbstverbesserung.
- **Liu Shengyu (hoch):** Essay am 14.09.2026, Platz 1 der Zhihu-Hot-Liste, Kernel von DeepSeek V4.1-Flash; Alter 23 und exakter Titel nicht verifiziert.
- **Amodei-Essay (hoch):** "We Must Pace the Frontier" 12.09.2026; Altman ("we will do the same" bei unabhängigen Evaluatoren), Musk ("Dario is right"), Hassabis (vorsichtig zustimmend) belegt, aber nur mit "12./13.09. (Wochenende)" datierbar. Jalapeño siehe [video-summary-fmMCg6dyWpQ.md](video-summary-fmMCg6dyWpQ.md).
