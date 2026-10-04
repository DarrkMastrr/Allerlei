# "How Meta tried to replace its employees with AI"

**Kanal:** Frank (deutschsprachiger KI-News-Kanal; YouTube-Titel auf Deutsch: "Wie Meta versucht hat seine Angestellten mit KI zu ersetzen"; kommentierende Nachrichtenzusammenfassung mit leicht ironischem Ton, stützt sich nach eigener Angabe hauptsächlich auf eine Reuters-Recherche)
**URL:** https://www.youtube.com/watch?v=C27fNEFQLic
**Länge:** ca. 19:30 (laut Metadaten 1169 Sekunden), veröffentlicht 27.09.2026
**Zusammenfassung erstellt:** 2026-10-04

*Hinweis zum Ablauf: Transkript aus den YouTube-Captions (Datei "en-orig", Englisch; die Captions wirken maschinell erzeugt oder übersetzt, YouTube-Metadaten weisen die Sprache als de-DE aus; komplettes Video abgedeckt, kein Whisper nötig). Der Videodownload scheiterte zweimal mit HTTP 403, daher wurden **keine Frames gesichtet** (Einblendungen wie Zeitleiste, Karten- und Grundbuchansicht, Meta-Video kenne ich nur aus der Erzählung). Eine Passage mit eingespielten Originalaussagen von Mark Zuckerberg bei Joe Rogan (ca. 0:33-0:55 und 1:15-1:35) ist in den Captions nicht transkribiert; was dort gesagt wird, ist nur aus der Zusammenfassung des Sprechers bekannt. Die Captions sind teils fehlerhaft (z. B. "Mark Hackerberg", verstümmelter Liedtext um 17:44).*

**Prüfstatus:** Nach 3 Prüfdurchläufen nur noch Detailfehler gefunden; die letzte Korrektur wurde nicht mehr nachgeprüft.

---

## Worum geht es?

Das Video erzählt, wie der Meta-Konzern (Facebook, Instagram, WhatsApp) unter Mark Zuckerberg versuchte, einen großen Teil seiner Programmierer durch KI-Agenten (selbstständig arbeitende KI-Programme) zu ersetzen, und warum dieser Plan laut der Quelle des Videos, einer Reuters-Recherche, "spektakulär" scheiterte. (Eigene Einordnung: Neu ist weniger die Idee als die Einsicht von innen.) Meta hat die Auswirkungen in eigenen Testgruppen gemessen, und die Zahlen sahen schlecht aus. Es gab zwar viel mehr Änderungen am Code, aber deutlich weniger Nutzen als Aktivität (laut Video +220 % Änderungen, aber nur +36 % echte Verbesserung), dazu mehr Sicherheits- und Stabilitätsprobleme (die genaue Bedeutung der Zahlen ist offen, siehe "Zu prüfen").

Eigene Einordnung (nicht aus dem Transkript): Häufig wird erwartet, dass KI-Agenten Entwicklerteams bald deutlich verkleinern können. Dieses Video liefert dazu ein Gegenbeispiel aus einem Konzern, der sehr viel Geld in KI steckt und laut Video intern einige Kennzahlen erhoben hat. Das ist wichtig für alle, die verstehen wollen, wie weit KI bei der Arbeit tatsächlich trägt. Laut Video setzte Meta die erste Entlassungswelle trotz der schlechten Testwerte noch um und sagte erst die zweite ab. Wichtig zur Einordnung: Der Kanal erzählt das pointiert und mit Spott, die Zahlen stammen aus einem Reuters-Bericht, den das Video nur wiedergibt.

## Was das Video sagt

Alles Folgende ist die Darstellung des Videos. Eigene Erklärungen und Prüfhinweise sind als solche gekennzeichnet. Zeitangaben sind Näherungen aus den Captions.

### Die Vision: Programmieren per KI (0:00-2:10)

Das Video beginnt mit Zuckerbergs Aussagen im Podcast von Joe Rogan Anfang 2025. Laut Sprecher geht es dort um "Engineers", womit nicht Maschinenbauer gemeint sind, sondern Programmierer: Leute, die verstehen, wie Apps wie Instagram oder WhatsApp im Hintergrund aufgebaut sind, und diese ändern. Die Vision laut Video: Die **Mehrzahl der durchschnittlichen ("Mid-Level") Programmierer** soll durch KI ersetzt werden. Am Ende steht eine KI, die sowohl die Abläufe bei Meta verbessert als auch die KI entwickelt, die Meta selbst veröffentlicht, also "KI, die andere KI entwickelt".

Was damals nach Gedankenspiel klang, sei gut ein Jahr später tatsächlich versucht worden.

### Januar 2026: Das Treffen auf Hawaii und das Projekt "OT" (2:10-4:50)

Im Januar 2026 traf sich laut Video die Meta-Führung zum jährlichen Spitzentreffen auf Zuckerbergs privatem Anwesen auf der Hawaii-Insel Kauai. Der Sprecher schweift hier bewusst ab (Grundstück laut Landregister 325 Acres, also etwa 1,3 Millionen Quadratmeter; stark verpixelte Street-View-Aufnahmen). Das ist unterhaltsam, aber für das Thema ohne Bedeutung.

Beschlossen wurde laut Video: Meta soll **"AI-native"** werden, also ein Unternehmen, das sich konsequent an KI ausrichtet. Viele Produktteams sollen dazu **um 60 % verkleinert** werden. (Das Video stellt die 60 % als Beschluss dar; die Presse formuliert laut Suchtreffer/TNW eher "potenziell bis zu 60 %", also als erwogen.) Geplant waren **zwei Entlassungswellen**, eine im Mai 2026 und eine im November 2026, je etwa **10 % der Belegschaft**. Das Projekt lief intern unter dem Namen **"OT"** für "Organizational Transformation" (Umbau der Organisation), "ziemlich genau der langweiligste Titel, den man wählen kann".

### Wie Teams vorher aussahen und wie sie nachher aussehen sollten (4:50-8:30)

Das Video erklärt ausführlich den Unterschied, und er ist der Kern des Plans:

- **Bisher:** Ein Team hat 10 bis 20 Leute, etwa für Instagram Reels. Ein Product Manager trägt die Verantwortung (er bestimmt, was gebaut wird). Dazu kommen 7 bis 14 Engineers (Programmierer), ein Designer, ein Data Scientist (wertet aus, ob eine Änderung etwas bringt, z. B. ob ein größerer Knopf mehr genutzt wird), ein Data Engineer (liefert verlässliche Daten) und je nach Projekt weitere Rollen wie User-Experience-Forscher. Alle arbeiten fachlich für den Product Manager, berichten aber disziplinarisch an eigene Managerlinien. Daraus entstehen viele Management-Ebenen. Die vielen Engineers gibt es laut Video auch deshalb, weil jede Änderung an so einer Plattform sorgfältig abgesichert sein muss, schließlich hängt viel Geld daran.
- **Neu:** Ein "Pod" besteht nur aus **3 bis 5 Personen**: ein **Direction Lead** (gibt die Richtung vor) und 3 bis 4 **Builders**, meist die früheren Programmierer mit deutlich mehr Verantwortung, weil sie Aufgaben der anderen Rollen mitübernehmen. Zusätzlich gehören **viele KI-Agenten** zum Team. Designer, Data Scientists und Data Engineers sitzen in einem gemeinsamen Pool und werden je nach Bedarf zugeteilt. 10 bis 15 Pods berichten an einen **Organization Lead**. Die mittleren Management-Ebenen werden stark reduziert.

### Warum? Zwei Kostenblöcke (8:30-9:45)

Das Video erklärt die Motivation so: Meta habe im Wesentlichen nur zwei große Kostenblöcke, **Server/IT-Infrastruktur** und **Personal**. Wer stark in das eine investiert, muss beim anderen sparen. Meta plane laut Geschäftsbericht (Seite 47, so der Sprecher) für 2026 Investitionsausgaben von **rund 130 bis 145 Milliarden Dollar**, vor allem für KI-Rechenzentren und deren Chips. Das sei "deutlich mehr als Meta pro Jahr für Gehälter ausgibt", werde aber trotzdem als Begründung genutzt, beim Personal zu sparen.

### Die undichte Stelle und die ersten Anzeichen (9:45-12:10)

Am 14. März 2026 berichtete Reuters über die geplante Entlassungswelle. Das löste laut Video große Empörung aus, auch bei Führungskräften bis zur Vize-Präsidenten-Ebene, die teils gar nicht eingeweiht waren; nur der kleine Kreis auf Hawaii habe Bescheid gewusst. Die Führung tat das Ganze als "Spekulation, haltlose Gerüchte" ab, doch Metas Handeln deutete laut Video in dieselbe Richtung:

1. Ein Teil der Engineers wurde in eine neue Abteilung **"Applied AI Engineering"** versetzt. Ihre Aufgabe: **Übungsaufgaben für die KI** zu entwickeln, an denen sie das Programmieren lernen kann. Die meisten fanden das laut Video sehr langweilig.
2. Meta ordnete auf den Rechnern **aller US-Engineers eine Überwachungssoftware** an, die Maus- und Tastaturbewegungen aufzeichnet. Zweck laut Video, ausdrücklich so kommuniziert: Die KI soll daraus lernen, wie ein guter Engineer bei Meta arbeitet. Das kam sehr schlecht an: Man werde überwacht, damit man ersetzt werden kann.

Die Belegschaft organisierte sich, schrieb Petitionen, die internen Mitarbeiterumfragen "stürzten ab", und im internen Chat gab es viel Kritik.

### Die Messzahlen: viel Aktivität, wenig Ergebnis (12:10-15:50)

Das Video nennt vier Kennzahlen, die laut Reuters intern bei Meta erfasst wurden. Laut Video: Vergleich der neuen KI-Teams vorher/nachher. Laut Sekundärquellen (Suchtreffer, TNW) eher ein Vorjahresvergleich ("year on year") mit Zahlen aus einem Beitrag des CTO im Juni, nicht ausdrücklich nur der KI-Teams; **offen**. Die 40 % und 70 % sind unten in der Video-Lesart wiedergegeben, die Quellen formulieren abweichend (siehe "Zu prüfen"):

- **220 % mehr Änderungen am Code** der Plattformen. Der Sprecher rechnet das als "dreieinhalb mal so viele"; nach üblicher Rechnung wären +220 % rund das 3,2-Fache (siehe "Zu prüfen").
- Aber nur **36 % mehr echte Verbesserung**, die Meta als sehr datengetriebenes Unternehmen messen kann (zum Beispiel: Wie viel mehr Nutzung bringt ein Knopf, der einen Millimeter größer ist?).
- **40 % mehr Sicherheitslücken** (so das Video; Quellen laut Suchtreffer: "major technical and security incidents", also Zwischenfälle).
- **70 % mehr Notfalleinsätze** der menschlichen Engineers, die vom KI-System verursachte Schäden beheben mussten (so das Video; Quellen laut Suchtreffer: Zeitanteil für "firefighting").

Der Sprecher erklärt das mit einem bekannten KI-Verhalten: KI produziere viel (er nennt "100-seitige Präsentationen"), doch der eigentliche Gehalt sei geringer, als es aussieht. Dazu komme ein Unterschied im Vorgehen: Menschliche Meta-Engineers machen eher **kleine Änderungen, die sie überblicken**. Die KI-Agenten seien "grobschlächtiger" und schreiben bei Bedarf gleich den Code einer ganzen Funktion um, den sich ein Mensch nicht anzufassen getraut hätte. Das kann große Probleme machen.

Als Beispiel nennt das Video den **KI-Bot von Instagram**, der von Hackern so ausgetrickst worden sei, dass sie Zugriff auf Daten fremder Konten bekamen und etwa Passwörter ändern konnten, genannt wird ein Konto, das Barack Obama während seiner Präsidentschaft nutzte. Die betroffene Funktion sei teilweise mit KI-Hilfe entstanden. Das Fazit der internen Untersuchungen laut Video: Das System, in dem KI sehr viel übernehmen soll, funktioniere "nicht besonders gut".

### Rückzieher und Imagepflege (15:50-18:40)

Am **19. Mai 2026**, einen Tag vor der ersten Entlassungswelle, setzte sich Zuckerberg laut Video noch einmal mit seinen Leuten zusammen und beschloss, die **zweite Welle im November abzusagen** und die Belegschaft zu beruhigen. Die erste Welle lief trotzdem: Am Folgetag verloren rund **10 % der Belegschaft** ihre Stelle. Kurz danach habe Zuckerberg erklärt, weitere Entlassungen seien nicht geplant, man wolle mehr Stabilität. Das Tracking der Mitarbeiter werde **vorerst pausiert**. Laut Sprecher (nach eigener Aussage zusammengetragen, ohne Beleg) werde zur Beruhigung die Snack-Auswahl in der Büroküche verbessert; den zweiten Obstkorb und die Frage der Wirkung kommentiert er ironisch.

Danach folgte laut Video eine "Entschuldigungskampagne": ein langer Aufsatz Zuckerbergs darüber, wie KI die Zukunft der Menschheit prägen solle, mit der Aussage, Meta sei das einzige Unternehmen, das wirklich Menschen in den Mittelpunkt stelle, sowie ein Imagevideo, in dem der Mensch stets im Zentrum stehe. Der Sprecher findet es ironisch, dass im Hintergrund "Five Years" von David Bowie läuft, ein Lied über das Ende der Welt in fünf Jahren. Das ist seine Deutung, keine Aussage von Meta.

### Folgen: Klagen (18:40-19:30)

Mehrere ehemalige Mitarbeiter haben laut Video Meta verklagt. Ihr Vorwurf: Bei der Entlassungswelle im Mai 2026 sei **KI zur Auswahl** eingesetzt worden, und betroffen gewesen seien auffällig oft Menschen, die gerade ein Kind bekommen hatten oder länger krank waren. Aus KI-Sicht sei das "nicht dumm", weil diese Personen theoretisch ein höheres Ausfallrisiko haben, in den USA aber trotzdem **diskriminierend**. Die Gerichte werden sich damit befassen. Zum Schluss schätzt der Sprecher, Meta werde seinen Plan "wahrscheinlich in weniger als 10 Jahren" doch umsetzen.

## Einordnung und Plausibilität

Eigene Einordnung, mit Quellenkennzeichnung. Hinweis: Der Titel klingt nach Sensation, tatsächlich beschreibt das Video einen **teilweise gescheiterten Umbau und eine Rücknahme**, keinen Ersatz aller Angestellten. Real entlassen wurde nach Video-Darstellung rund ein Zehntel der Belegschaft; Ziel war die Verkleinerung von Teams, nicht der vollständige Ersatz durch KI.

- **Rahmen des Plans (60 %, Pods mit 3-5 Personen, Projekt OT, zwei Wellen):** Der **Pragmatic Engineer** (Artikel "Meta wanted to reduce teams by 60% because of AI") nennt laut Suchtreffer die Überschrift "reduce teams by 60 %". Ein WebFetch-Ergebnis dazu lieferte eine Tool-Zusammenfassung mit weiteren Details (Projekt OT, Pods, zwei Wellen, Absage November, 10 % im Mai, 20-30 % der Engineers auf KI-Datenaufbereitung, Obama-Konto-Vorfall); da ein Prüfer bezweifelt, dass der Artikel selbst (statt einer Übersichtsseite) abgerufen wurde, gelten diese Details als **nicht belegt**. Was das Video in diesen Punkten sagt, ist deshalb nur teilweise (60 %, Pods) durch Suchtreffer gestützt. Eine Suchtreffer-Zusammenfassung (Engadget, Computerworld, TNW, CNBC in den Treffern) nennt ebenso 60 %, Pods, rund 8.000 Entlassungen am 20. Mai und den Rückzieher um den 19. Mai (Video: "19. Mai, einen Tag vor der ersten Welle"; "in der Nacht" ist in den Treffern nicht belegt). Beachte: Die Treffer stammen aus Suchergebnissen (**Suchtreffer**), nicht aus gelesenen Volltexten.
- **Reuters-Quelle:** Die Hauptquelle des Videos (Reuters-Recherche vom 26.08.2026, Katie Paul, laut Suchtreffer auf Basis interner Dokumente, Aufzeichnungen und über 20 Interviews) war für mich **nicht abrufbar** (Fetch blockiert). Das Datum 26.08.2026 steht in der URL aus der Videobeschreibung.
- **Kennzahlen (220 %, 36 %, 40 %, 70 %):** Ein Suchtreffer (Forbes, SmarterArticles; **Suchtreffer**, nicht gelesen) nennt 220 % mehr Code-Änderungen, 36 % mehr Features beim Nutzer und je 40 % mehr "technische und Sicherheits-Zwischenfälle" und einen auf 70 % gestiegenen Zeitanteil für "Firefighting". Das **weicht in der Formulierung vom Video ab**: Das Video spricht von 40 % mehr "Sicherheitslücken" und 70 % mehr "Notfalleinsätzen". Ob die Quelle von Vorfällen (Incidents) oder Lücken spricht und ob die 70 % ein Anstieg um 70 % oder ein Anteil von 70 % sind, konnte ich nicht klären. Daher: Die Größenordnung ist durch einen Suchtreffer gestützt, die genaue Bedeutung offen.
- **Rechenfehler im Video:** +220 % entspricht dem 3,2-Fachen, nicht dem "3,5-Fachen" (Eigene Rechnung). Kleiner Fehler des Sprechers, ohne Folgen für die Aussage.
- **Investitionsausgaben 130-145 Mrd. Dollar:** Ein Suchtreffer (TNW) nennt "$145 billion on AI infrastructure". Das Video nennt die Spanne 130-145 Mrd. aus dem Geschäftsbericht; nicht selbst geprüft (**Suchtreffer**, nur Obergrenze bestätigt).
- **Überwachungssoftware für US-Engineers:** Siehe bestehende Notiz [video-summary-KjNp6CbHUSY.md](video-summary-KjNp6CbHUSY.md), die Fortune und TechSpot (April 2026) als Quellen nennt. Das Video ordnet das Tracking dem Zweck "KI soll lernen" zu, was zu dieser Notiz passt. Nicht erneut geprüft.
- **Hawaii-Details, Klage wegen KI-gestützter Auswahl (Eltern/Krankgeschriebene), Bowie-Lied, Aufsatz Zuckerbergs:** nicht geprüft. Die Klage-Aussage ist im Video keine belegte Tatsache, sondern der **Vorwurf** der Kläger; ob KI wirklich zur Auswahl eingesetzt wurde, ist offen.
- **Tonfall:** Der Sprecher wertet stark ("Hackerberg", "brillanter Plan", Spott über Snacks). Seine Deutung, Zuckerberg wiederhole das Muster "erst erwischt werden, dann die Gegenposition beziehen", ist Meinung. Auch "in weniger als 10 Jahren" ist eine persönliche Schätzung.

## Nutzen für dich (Allround, Code, lokale KI)

- **Lehre für KI beim Programmieren:** Das Video bestätigt ein Muster, das man auch im Kleinen kennt: KI-Agenten erzeugen viel Code, aber **Menge ist nicht Qualität**. Wer selbst mit Coding-Agenten arbeitet, sollte die Wirkung messen (läuft es, ist es sicherer/besser?) statt die Zahl der Änderungen zu zählen, und große, schwer überblickbare Umbauten vom Agenten besonders kritisch prüfen.
- **Kleine, überprüfbare Schritte:** Der Unterschied "Mensch macht kleine überblickbare Änderungen, Agent ändert gleich ein ganzes Feature" ist eine praktische Regel für den eigenen Umgang mit Agenten: Aufgaben klein schneiden und jedes Ergebnis prüfen.
- **Sicherheit:** Das Instagram-Beispiel (KI-Bot ausgetrickst, fremde Konten erreichbar) ist ein Warnbeispiel für Agenten mit weitreichenden Rechten. Bei lokalen Agenten gilt dasselbe: so wenig Rechte wie möglich.
- **Lokale KI / Hardware:** Keine Aussagen im Video.

## Begriffe

- **Engineer (Programmierer):** Im Video: Person, die Code schreibt und ändert, nicht Maschinenbauer.
- **KI-Agent:** KI-Programm, das selbstständig Aufgaben erledigt (z. B. Code ändern), statt nur Fragen zu beantworten.
- **AI-native:** Im Video: ein Unternehmen, das "wirklich auf KI ausgerichtet" ist. (Eigene Erläuterung: bei Meta hieß das konkret kleinere Teams mit Agenten, siehe Pods.)
- **Pod:** Meta-Bezeichnung für die neuen KI-Kleinteams (3 bis 5 Menschen plus Agenten), geleitet von einem Direction Lead.
- **Builder:** Rolle im Pod; meist ein früherer Programmierer, der jetzt mehr Aufgaben übernimmt.
- **Projekt OT (Organizational Transformation):** Interner Name des Umbaus von Meta.
- **Investitionsausgaben (Capex):** Geld für langlebige Anschaffungen, hier vor allem KI-Rechenzentren und Chips.
- **Sicherheitslücke:** Fehler im Code, den Angreifer ausnutzen können, z. B. um fremde Konten zu übernehmen.

## Kernbotschaft

Laut diesem Video (das sich auf Reuters beruft) wollte Meta Anfang 2026 Produktteams um 60 % verkleinern (die Presse spricht laut Suchtreffer von "bis zu 60 %") und durch kleine Pods mit KI-Agenten ersetzen, ließ Mitarbeiter dafür überwachen und entließ im Mai rund 10 %. Die genannten Messwerte zeigten viel mehr Code-Änderungen, aber deutlich weniger Nutzen und laut Video mehr Sicherheitslücken und Notfalleinsätze (Quellen formulieren das als Zwischenfälle bzw. Firefighting-Zeitanteil), woraufhin die zweite Welle abgesagt wurde. Der Plan ist also eher teilweise gescheitert und zurückgenommen als vollständig durchgezogen; die Rahmendaten sind durch Presse gestützt, die genauen Kennzahlen nur per Suchtreffer, und das Video wertet pointiert.

## Themen-Tags
Meta, Mark Zuckerberg, KI-Agenten, Entlassungen, Projekt OT, AI-native, Pods, Mitarbeiter-Tracking, Code-Qualität, Sicherheitslücken, Instagram, Reuters-Recherche, Diskriminierungsklage

## Zu prüfen

- **Reuters-Originalbericht:** **nicht abrufbar** (Fetch blockiert). Alle Kennzahlen stammen deshalb nur aus dem Video bzw. aus Suchtreffern.
- **Kennzahlen 40 % / 70 %:** Video sagt "Sicherheitslücken" bzw. "Notfalleinsätze"; ein **Suchtreffer** (Forbes/SmarterArticles) sagt "technische und Sicherheits-Zwischenfälle" und "70 % Zeitanteil für Firefighting". Genaue Bedeutung offen, nicht raten.
- **Pragmatic Engineer:** nur als Suchtreffer (Überschrift "reduce teams by 60 %") belegt; die Details aus dem WebFetch-Ergebnis (Tool-Zusammenfassung, kein Volltext) sind nicht belegt, da nicht gesichert ist, dass der Artikel selbst abgerufen wurde. Messzahlen kamen im Abruf nicht vor.
- **60 % "beschlossen" oder "erwogen":** Video stellt es als Beschluss dar, Presse (Suchtreffer/TNW) eher als potenzielle Obergrenze; offen.
- **Zeitbezug der Kennzahlen:** Video: KI-Teams vorher/nachher; Sekundärquellen: eher Vorjahresvergleich; offen.
- **Entlassungszahl:** Video: "rund 10 %". Suchtreffer (Engadget, SF Chronicle, CNBC, Fox Business laut Hinweis aus Prüfdurchlauf): rund 8.000 am 20.05.2026, entspricht etwa 10 %, passt zum Video.
- **Klage ehemaliger Mitarbeiter (KI bei der Auswahl, Eltern/Kranke):** nicht geprüft; Vorwurf, kein Befund.
- **Offen: Sprache des Videos:** Captions englisch, Titel deutsch; ohne Ton/Frames nicht entschieden.
- **Querverweise (nicht editiert):**
  - [video-summary-KjNp6CbHUSY.md](video-summary-KjNp6CbHUSY.md): Meta-Tracking von Mitarbeiter-Bildschirmen und Tastatureingaben zum KI-Training (Fortune/TechSpot/WION), passt zum Video; keine Widersprüche.
  - [video-summary-Tk9klcnaVRg.md](video-summary-Tk9klcnaVRg.md): Tech-Entlassungen und Gegenreaktion, inkl. Meta-Petition gegen KI-Training; ergänzt dieses Video, die Meta-Details dort nicht gegengeprüft.
  - [video-summary-0bcwU3gUv6w.md](video-summary-0bcwU3gUv6w.md): behandelt Meta "Token-Maxing" und KI-ROI-Scheitern; thematisch verwandt (KI-Einsatz bringt weniger als erhofft).
  - [video-summary-CdgYmlxGHCo.md](video-summary-CdgYmlxGHCo.md): Zuckerberg/Meta Superintelligence Labs, anderer Zusammenhang.
  - [ki-risiko-warnungen.md](../ki-risiko-warnungen.md) und [ki-sicherheitsvorfaelle-sandbox-escapes.md](../ki-sicherheitsvorfaelle-sandbox-escapes.md) erwähnen Meta; nicht im Detail verglichen.
  - Widersprüche zu bestehenden Notizen: keine harten gefunden.
