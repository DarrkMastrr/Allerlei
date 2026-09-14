# "So schlecht steht es wirklich um den deutschen Mittelstand (Falsche Glaubenssätze von KI-Agenturen)"

**Kanal:** Leonard Schmedding (Co-Founder/Chief AI Officer, Everlast AI GmbH)
**URL:** https://www.youtube.com/watch?v=PjzaN04GEy8
**Länge:** 19:29
**Zusammenfassung erstellt:** 2026-09-14

---

**Hinweis zum Ablauf:** Der reguläre `watch`-Skill-Download scheiterte zunächst zweimal mit `HTTP 403 Forbidden` (Videodatenabruf) bzw. `HTTP 429` (Untertitel). Ein manueller yt-dlp-Test zeigte den eigentlichen Grund: ein fehlgeschlagener JS-Challenge-Solve ("The page needs to be reloaded") — behoben mit `--remote-components ejs:github` (lädt den offiziellen yt-dlp-Challenge-Solver nach) kombiniert mit `--cookies-from-browser firefox`. Damit lief der Video-Download sauber durch, native Untertitel (en) blieben aber wegen anhaltendem `429` unerreichbar. Es wurde daher auf Whisper via **Replicate** zurückgegriffen; da das Video mit 1169s über der 330s-Chunk-Schwelle liegt, transkribierte `whisper.py` automatisch in 4 Chunks (0–330s, 330–660s, 660–990s, 990–1169s) und lieferte 271 zeitversetzt gemergte Segmente. Ein erster Transkriptionsversuch brach mit einem reinen Netzwerk-Timeout beim allerersten Chunk ab (kein Zeichen für ein Duration-Problem); der zweite Versuch lief vollständig durch. Zusätzlich wurden 100 automatisch über die volle Länge verteilte Frames gesichtet (Stichproben + gezielte Frames an Grafik-Übergängen).

## Rahmen und Format

Reines Talking-Head-Video: Leonard Schmedding sitzt an einem Laptop auf einer Terrasse/Poolanlage (mediterranes Ambiente, Palmen, Pool) und spricht direkt in die Kamera. Keine zweite Person. Vereinzelt werden kurze Grafik-Inserts eingeblendet:
- Eine Europakarte mit Markierung DACH-Region und der Überschrift "10.000+ Gespräche mit dem Mittelstand" (Intro).
- Ein Beispiel-Dashboard "Customer Development" (Corporate/Retail Business, Net Income, Deposit-/Loan-Kennzahlen) als Illustration für professionelles Management-Controlling, das laut Schmedding im Mittelstand oft fehlt.
- Ein Balkendiagramm "Strompreise in Privathaushalten, 1. Halbjahr 2025" (europäischer Länder-Vergleich, Quelle laut Einblendung Statistisches Bundesamt/Destatis), in dem Deutschland ganz oben steht — zur Untermauerung der Aussage zu hohen Energiekosten.
- Ein Screenshot des Tools **Voicely** ("Schreibe 5x schneller in jeder App") als Beispiel für ein einfaches, wirkungsvolles KI-Tool.
- Eine 3-Schritte-Grafik "Gutes Onboarding": Klare Verantwortung → SOS-Kontakt zum Chef → Monatlicher Report.

## Die fünf "falschen Glaubenssätze" (Kernstruktur des Videos)

Schmedding präsentiert das Video als persönliche Learnings aus eigenen Angaben zufolge über 10.000 Gesprächen mit mittelständischen Unternehmen aus DACH plus vereinzelt Kanada, gewonnen über die eigene KI-Beratungsfirma (im Video "Everlast" genannt).

1. **"Der Mittelstand hat tolle, effiziente Prozesse" — falsch.** Kernprozesse (Produktion, Lieferketten, Lagermanagement, Investitionen) seien tatsächlich sehr gut, aber alles andere (Administration, Backoffice, Angebotserstellung, HR, Marketing, Vertrieb, Controlling, Digitalisierung) laufe oft "dilettantisch", basiere auf Excel und Wissen in den Köpfen einzelner Mitarbeiter. Fehlende Digitalisierung mache KI-Einführung teils unmöglich, ohne vorher überhaupt zu digitalisieren. Abwanderung von Wissensträgern sei teils existenzbedrohend für diese Unternehmen.

2. **"Der deutschen Wirtschaft geht es schlecht, also handeln Unternehmen entsprechend radikal" — falsch.** Viele Unternehmen säßen noch auf großen Ersparnispolstern aus früheren Jahrzehnten und behandelten die aktuelle Lage als vorübergehende Krise, die sich von selbst löse. Bildhafter Vergleich mit der Titanic: Das Orchester spielt weiter, während das Schiff sinkt — der Mittelstand spiele dabei "die zweite Geige" nach der Politik. Konkrete Symptome: Geschäftsführer schicken fachfremde Mitarbeiter in KI-Gespräche vor, schieben Entscheidungen monatelang auf, geben teure Beratungsstudien (200.000–500.000 €, genannt werden EY, KPMG) in Auftrag, ohne die Ergebnisse umzusetzen.

3. **"Der Mittelstand hat schon viel KI-Know-how" — falsch.** Gerade IT-Abteilungen/IT-Entscheider würden sich massiv überschätzen (Referenz auf Prof. Gunter Dück und dessen Konzept "Mount Stupid" aus einem früheren Interview mit Schmedding). Schon einfache Maßnahmen (KI-Agents in Outlook, Teams-Automatisierung, Cloud Code als privater Assistent, Corporate-LLM-Setups wie CorporateLLM.de, Transkriptionstools wie Voicely) hätten oft großen Impact, ohne dass komplexe Use Cases nötig seien. Anekdote: Bei einem Sicherheitsaudit (Kostenrahmen genannt: 20.000–40.000 €) sei eine kritische Sicherheitslücke gefunden worden, durch die Wettbewerber Angebotsdaten hätten abgreifen können — der zuständige IT-Sicherheitsmitarbeiter sei danach entlassen worden. These: "Ein einfaches Google-Setup wäre sicherer als die meisten Microsoft-Setups."

4. **"Der Mittelstand nutzt dieselben Tools wie in YouTube-Tutorials gezeigt" — falsch.** Laut Video nutzen nur 58% der US-Unternehmen Microsoft 365, in Deutschland dagegen 85%, während nur 10% Google Workspace nutzen. Daraus leitet Schmedding ab, dass US-lastiger YouTube-Content (Google/Claude/Notion-Setups) an der Praxis vieler deutscher Kunden vorbeigeht und empfiehlt, sich stärker mit Microsoft-Ökosystemen auseinanderzusetzen.

5. **"Projekte scheitern an Datenschutz oder Technik" — falsch.** Laut Schmedding scheitern KI-Projekte in der Praxis weit häufiger an schlechtem Onboarding, unklaren Verantwortlichkeiten und schlechter Kommunikation als an rechtlichen oder technischen Hürden. Empfehlung: klare Verantwortlichkeiten und SOS-Eskalationskontakt zur Geschäftsführung definieren, monatliche Fortschrittsreports liefern, Projekte über Lastenhefte und strukturierte Onboarding-Prozesse "an der Kandare" halten.

## Werblicher/Kontext-Hinweis

Das Video ist inhaltlich kein reiner Sales-Pitch (anders als laut Cross-Referenz einige andere Videos desselben Kanals im Repo), sondern liest sich als Positionierungs-Content für die eigene KI-Beratungsagentur Everlast AI. Am Ende wird auf ein weiteres, separates Video zur Kundengewinnung als KI-Agentur verwiesen, ohne im Video selbst einen Kurs oder ein Produkt explizit zu bewerben.

---

## Kernbotschaft

Leonard Schmedding (Everlast AI) widerlegt anhand eigener Beratungserfahrung fünf verbreitete Annahmen über den deutschen Mittelstand: Prozesse sind nur in Kernbereichen gut, nicht in Verwaltung/Vertrieb/Marketing; die wirtschaftliche Lage wird trotz Warnsignalen selten mit Konsequenz angegangen, weil viele Unternehmen noch von alten Polstern zehren; KI-Kompetenz ist selbst in IT-Abteilungen oft nur oberflächlich vorhanden; die tatsächlich genutzte Software-Landschaft (mehrheitlich Microsoft) unterscheidet sich stark von dem, was auf YouTube gezeigt wird; und Projekte scheitern in der Praxis überwiegend an Projektmanagement- und Kommunikationsdefiziten, nicht an Datenschutz oder Technik. Die übergeordnete Botschaft an KI-Agenturen: Diese Lücken sind eine Chance, erfordern aber Fingerspitzengefühl, Grundbildungsarbeit beim Kunden und straffes Onboarding/Projektmanagement statt technischer Bestleistung allein.

## Themen-Tags

Deutscher Mittelstand, KI-Agentur, KI-Beratung, Everlast AI, Leonard Schmedding, Digitalisierung, Prozessoptimierung, Change Management, Mount Stupid, Gunter Dück, IT-Sicherheit, Sicherheitsaudit, Microsoft 365, Google Workspace, Corporate LLM, Voicely, Onboarding-Prozesse, Projektmanagement, Energiekosten Deutschland, deutsche Wirtschaftskrise, KI-Adoption Unternehmen

## Für den technischen Team-/Gruppenleiter

Das Video richtet sich primär an KI-Agenturen im Vertrieb, enthält aber einige übertragbare Punkte für eine Gruppenleiter-/Führungsrolle in einem Hardware-Unternehmen:
- **"Mount Stupid" als Warnsignal in der eigenen IT/Technik-Organisation:** Die These, dass gerade technikaffine Mitarbeitende KI-Fähigkeiten am ehesten überschätzen und mit oberflächlichen Einwänden (z. B. pauschale Datenschutzbedenken) echte Fortschritte blockieren, ist ein nützlicher Realitätscheck für die eigene Teamdynamik bei KI-Einführung.
- **Prozess-Realismus abseits der Kernkompetenz:** Die Beobachtung, dass deutsche Mittelständler oft exzellente Kernprozesse (Produktion, Lieferketten) haben, aber in Backoffice/Controlling/Digitalisierung weit zurückliegen, ist ein brauchbarer Prüfpunkt für die eigene Organisation — wo genau laufen intern noch Excel-/Kopfwissen-Prozesse, die bei Personalwechsel riskant werden?
- **Onboarding-/Eskalationsstruktur für Projekte** (klare Verantwortlichkeiten, definierter Eskalationskontakt, regelmäßige Fortschrittsreports) ist ein direkt übertragbares, einfaches Muster für jedes interne oder extern vergebene Digitalisierungs-/KI-Projekt, unabhängig von der Branche.
- **Microsoft-vs.-Google-Realität:** Falls im eigenen Unternehmen oder bei Zulieferern/Kunden Microsoft-365-Umgebungen dominieren (laut Video die Norm im deutschen Mittelstand), ist das ein Hinweis, KI-Tooling-Entscheidungen nicht an US-YouTube-Tutorials mit Google-/Notion-Fokus auszurichten, sondern am tatsächlich vorhandenen Software-Ökosystem.

## Zu prüfen

- **Eigenangaben des Sprechers nicht unabhängig verifizierbar:** Die Zahl "10.000+ Gespräche" ist eine unbelegte Eigenangabe. Cross-Referenz: [video-summary-1guudCDr0H4.md](video-summary-1guudCDr0H4.md) verweist bereits allgemein auf "Everlast-AI-Kanäle im Repo" als reißerisch, und mindestens ein weiteres bereits im Repo dokumentiertes Video desselben Umfelds nennt andere, teils höhere Zahlen ("100.000 Gespräche", "6.500 umgesetzte KI-Projekte", laut Notiz in einem verwandten Summary als "unbelegte Eigenangaben, nicht weiter geprüft" vermerkt). Per WebSearch bestätigt wurde nur die Existenz und Rolle der Firma: Leonard Schmedding ist tatsächlich Co-Founder/Chief AI Officer von Everlast AI GmbH (Sitz Neu-Ulm), die sich selbst als größte/schnellstwachsende KI-Beratung Deutschlands positioniert (laut Firmenwebsite, nicht unabhängig extern verifiziert) — die genauen Gesprächs-/Projektzahlen schwanken zwischen den Videos des Kanals und sollten nicht als belastbare Statistik behandelt werden.
- **"Höchste Energiekosten der Welt"-Behauptung leicht überzeichnet:** Per WebSearch liegt Deutschland bei Strompreisen für Privathaushalte aktuell auf Platz 4–5 weltweit (u. a. hinter Bermuda, Dänemark, Irland, Belgien je nach Quartal/Quelle), nicht auf Platz 1. Die Kernaussage (sehr hohe Preise im internationalen Vergleich) stimmt der Richtung nach, "höchste der Welt" ist aber eine Übertreibung. Die im Video gezeigte Grafik selbst vergleicht zudem nur europäische Länder, nicht die Welt — passt also nicht exakt zur mündlichen Behauptung.
- **Microsoft-365- vs. Google-Workspace-Zahlen uneindeutig:** Die im Video genannten 85% (Deutschland, Microsoft 365) und 10% (Google Workspace) decken sich mit einer älteren, im Zuge der Recherche gefundenen Quelle. Eine neuere Statista-Auswertung (Stand Ende 2023) zeigt dagegen ein deutlich ausgeglicheneres Bild von je rund einem Drittel für Deutschland. Welche Zahl aktuell zutrifft, ließ sich nicht abschließend klären — die 58%-US-Zahl aus dem Video wurde nicht separat verifiziert.
- **Sicherheitsaudit-Anekdote (Kündigung eines IT-Sicherheitsmitarbeiters nach gefundener Lücke)** ist ein anonymisiertes Einzelbeispiel aus der eigenen Beratungspraxis des Sprechers, naturgemäß nicht unabhängig überprüfbar — hier nur als Erzählung aus dem Video wiedergegeben.
- **Cross-Referenz-Suche im Repo:** Eine Grep-Suche nach "Mittelstand", "Schmedding" und "Everlast" ergab keine inhaltlichen Widersprüche zu bestehenden Notizen, nur die oben genannte Konsistenz-Problematik bei den Eigenangaben-Zahlen des Kanals. Das Thema "deutscher Mittelstand und KI-Adoption" taucht in mehreren anderen Video-Summaries am Rande auf (z. B. Empfehlungen zu Pain-Point-Identifikation und Förderprogrammen wie KI NRW in [video-summary-pb5cMmdQVJo.md](video-summary-pb5cMmdQVJo.md)), aber ohne direkten inhaltlichen Widerspruch zu diesem Video.
- Die Gunter-Dück-"Mount-Stupid"-Referenz stammt aus einem laut Sprecher bereits vor rund zwei Jahren geführten eigenen Interview — dieses frühere Interview selbst wurde nicht separat recherchiert oder verifiziert.
