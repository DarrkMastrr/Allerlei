# "KI-Agenten landen im Müll"

**Kanal:** Sebastian Claes | Claude Code & KI-Agenten
**URL:** https://www.youtube.com/watch?v=o4QbZf_2DK4
**Länge:** 06:20
**Zusammenfassung erstellt:** 2026-10-17

---

*Siehe auch: [video-summary-jAobzuCNIR8.md](video-summary-jAobzuCNIR8.md) — darin nennt Statista-CEO Marc Berg "Forward Deployed Engineers" als wachsenden Trend, den Statista selbst mit acht eigenen "Sales Consultants" testet. Die Perspektiven ergänzen sich: Berg schildert, wie Anbieter dieses Modell verwenden, Claes erklärt, warum Unternehmen dabei eine Abhängigkeitsfalle bauen. Kein Widerspruch, aber deutlich unterschiedliche Einordnung.*

## Worum geht es?

KI-Agenten klingen nach einer verlockenden Idee: Man beauftragt einen Dienstleister, der einen Agenten für das eigene Unternehmen baut, und danach läuft alles automatisch. Ein Beispiel: Ein Agent liest Kundenanfragen und erstellt passgenaue Angebote. Klingt gut — aber Marktforscher wie Gartner zeichnen ein ernüchterndes Bild. Ihre Prognose: Sieben von zehn Unternehmen, die sich KI-Agenten von einem externen Anbieter bauen lassen, werden diese Agenten bis 2028 wieder aufgeben. Die Investition landet im Müll.

Warum? Weil ein KI-Agent kein Softwareprodukt ist, das man einmal installiert und dann Jahre lang benutzt. Er muss laufend aktualisiert werden — wenn sich Produkte ändern, wenn Rabattregeln sich ändern, wenn das zugrundeliegende KI-Modell vom Anbieter abgeschaltet wird. Wer das Wissen für diese Pflege nicht im eigenen Unternehmen aufgebaut hat, sitzt in einer Zwickmühle: entweder immer wieder teuer beim Dienstleister anklopfen oder den Agenten einfach so laufen lassen, bis niemand mehr seinen Ergebnissen traut. Sebastian Claes erklärt anhand aktueller Berichte von Gartner und Anthropic, was den Unterschied macht — und gibt konkrete Hinweise, worauf man achten sollte, bevor man einen Vertrag unterschreibt.

## Zwei Meldungen, eine Botschaft

Das Video steigt mit zwei fast gleichzeitigen Neuigkeiten ein, die auf den ersten Blick nichts miteinander zu tun haben:

**Meldung 1 (Gartner):** Das Marktforschungsunternehmen Gartner prognostiziert, dass 70 % der Unternehmen, die sich KI-Agenten von einem Anbieter direkt vor Ort bauen lassen (*Forward Deployed Engineering*, dazu unten mehr), diese Agenten bis 2028 wieder aufgeben werden. Als Hauptgrund nennt Gartner eine Kostenfalle: Die laufenden Ausgaben steigen, während das Unternehmen selbst nie gelernt hat, den Agenten weiterzuentwickeln.

**Meldung 2 (Anthropic):** Nur drei Tage später kündigt Anthropic — das Unternehmen hinter dem KI-Modell Claude — an, 100 Millionen US-Dollar einzusetzen, um 10.000 Ingenieure auszubilden. Diese Ingenieure werden nicht bei Anthropic arbeiten, sondern in Banken, Pharmaunternehmen und Unternehmensberatungen. Hintergrund: Menschen, die KI in echten Unternehmen zum Funktionieren bringen können, sind laut Anthropic gerade am schwersten zu finden.

Claes' Kernthese: Beide Meldungen zeigen dieselbe Lücke. Der entscheidende Faktor für den Erfolg eines KI-Agenten ist nicht die Technologie selbst — sondern die Menschen im eigenen Unternehmen, die sie verstehen und am Laufen halten.

## Das Abhängigkeitsproblem: Warum Agenten im Müll landen

Um das Problem greifbar zu machen, beschreibt Claes einen typischen Fall: Ein Unternehmen beauftragt einen Dienstleister, der einen *Angebots-Agenten* baut. Der Agent liest Kundenanfragen und erstellt automatisch Angebote — zugeschnitten auf die Produkte und Rabattregeln des Unternehmens. Solange der Dienstleister dabei ist, funktioniert das gut.

Aber dann passiert, was immer passiert: Ein neues Produkt kommt hinzu. Für Großkunden gilt plötzlich eine andere Rabattstaffelung. Jemand muss diese Änderungen in die Anweisungen des Agenten einpflegen — und danach prüfen, ob die Angebote noch stimmen. Wer macht das, wenn der Dienstleister nicht mehr vor Ort ist?

Hinzu kommt ein technisches Problem: Die KI-Modelle, auf denen solche Agenten laufen, sind keine ewigen Dienste. Anthropic etwa schaltet am Ende November eine Claude-Version ab, die erst vor einem Jahr erschienen ist (Claude Sonnet 4.5, erschienen September 2025, geplantes Abschaltdatum 30. November 2026). Ein Agent, der auf dieser Version läuft, bekommt danach einfach keine Antworten mehr. Auch das Migrieren auf eine neue Version, und anschließend das Testen, ob alles noch funktioniert, ist Arbeit — Arbeit, die irgendjemand leisten muss.

Solange der Dienstleister noch dabei ist, erledigt er beide Aufgaben. Was passiert, wenn das Projekt endet? Entweder holt man ihn für jede Änderung wieder zurück und zahlt jedes Mal neu. Oder man lässt den Agenten so, wie er ist. Dann schreibt er weiter Angebote nach veralteten Rabattregeln — so lange, bis die Kollegen aufhören, seinen Ergebnissen zu vertrauen. Das ist die Falle, die Gartner beschreibt.

## Was Forward Deployed Engineering wirklich bedeutet

Gartner gibt dieser Praxis einen Namen: *Forward Deployed Engineering* (FDE). Gemeint ist ein Modell, bei dem Entwickler eines Anbieters direkt beim Kunden vor Ort arbeiten und den Agenten im Unternehmen aufbauen. Das klingt nach intensiver Betreuung — und das ist es auch. Das Problem: Viele Anbieter verwenden diesen Begriff inzwischen für ganz normale Implementierungsprojekte oder KI-Beratung, manchmal nur, weil es strategischer klingt. Claes weitet die Warnung deshalb aus: Sie gilt für jeden Dienstleister, der einen Agenten aufbaut und dann das Unternehmen verlässt — unabhängig vom Namen des Modells.

Außerdem macht er auf einen oft übersehenen Punkt aufmerksam: Weniger als jedes fünfte Kundenprojekt dieser Art fließt laut Gartner in das Standardprodukt des Anbieters ein. Das heißt: Der Agent, den ein Dienstleister für das eigene Unternehmen baut, ist in der Regel ein Einzelstück — kein Produkt, für das automatisch Updates kommen. Einzelstücke bekommen nur dann Weiterentwicklung, wenn jemand dafür bezahlt oder wenn die eigene Mannschaft es kann.

## Drei Phasen für eine Zusammenarbeit, die nicht endet im Müll

Gartner beschreibt nicht nur das Problem, sondern auch, wie es lösbar ist — in drei Phasen:

**Phase 1: Vor der Vertragsunterschrift.** Bevor überhaupt ein Angebot eingeholt wird, sollte feststehen: Wer im eigenen Unternehmen trägt die inhaltliche Verantwortung für das Ergebnis — nicht nur für das Budget? Der Vertrag selbst muss klären, was genau geliefert wird, wie Wissen an das eigene Team weitergegeben wird, wem am Ende der fertige Agent mit allen Anweisungen gehört, und wie die Übergabe abläuft, wenn der Dienstleister geht.

**Phase 2: Während des Aufbaus.** Eigene Mitarbeiter sitzen mit am Tisch. Gartner nennt sie "Technicians" (Fachleute aus dem eigenen Haus). Nur so bleibt das Wissen im Unternehmen, statt beim Dienstleister. Wer keine eigene IT-Abteilung hat, sollte jetzt jemanden an Bord holen, der die Technologie später betreut. Nach jedem Zwischenschritt prüft man gemeinsam: Bringt der Agent schon einen messbaren Nutzen? Und: Was darf der Agent allein entscheiden — und wofür braucht es immer noch einen Menschen?

**Phase 3: Die Übergabe.** Sie sollte so verlaufen, wie von Anfang an vereinbart. Gartner warnt ausdrücklich davor, die Zusammenarbeit einfach zu verlängern, weil das eigene Team noch nicht bereit ist. Das Projekt gilt nicht als Erfolg, weil der Agent fertig ist — sondern erst dann, wenn das eigene Team ihn selbstständig betreiben, verbessern und an neue Prozesse anpassen kann.

Am Beispiel des Angebots-Agenten bedeutet das konkret: Irgendjemandem im Team muss klar sein, wie er eine neue Rabattregel eigenständig einpflegt — und wie er danach prüft, ob die Angebote noch stimmen.

## Die entscheidende Frage vor der Beauftragung

Claes destilliert den gesamten Gartner-Befund auf eine einzige Frage, die man einem potenziellen Dienstleister stellen sollte, bevor man unterschreibt:

**"Was kann mein Team alleine, wenn ihr als Anbieter wieder weg seid?"**

Wenn der Dienstleister auf diese Frage keine klare Antwort hat, macht man sich von ihm abhängig. Nicht böswillig — aber strukturell.

## Der menschliche Faktor: Gartner und Anthropic im Gleichklang

Claes stellt am Ende eine Verbindung her: Gartner warnt vor dem Scheitern von extern gebauten Agenten, Anthropic steckt 100 Millionen Dollar in die Ausbildung von Menschen, die KI in echten Unternehmen betreuen können. Beide Organisationen kommen von verschiedenen Seiten zum selben Punkt: Ein Agent ist immer nur so gut wie die Person im Unternehmen, die ihn versteht und weiterentwickeln kann.

Anthropic meldet, dass in den Partnerunternehmen oft eine kleine Gruppe hochmotivierter Menschen den Löwenanteil des KI-Wertes liefert. Claes' Schlussfolgerung daraus: Man muss nicht das gesamte Team zu KI-Experten machen. Der sinnvolle erste Schritt ist deshalb — in seiner Interpretation — ein oder zwei Personen, die die eigenen Prozesse in- und auswendig kennen und lernen möchten, wie man Agenten aufbaut und pflegt.

## Begriffe

**KI-Agent:** Ein Computerprogramm, das mithilfe eines KI-Sprachmodells selbstständig Aufgaben ausführt — zum Beispiel Anfragen lesen, Entscheidungen treffen und Angebote erstellen — ohne dass ein Mensch jeden Schritt steuern muss.

**Forward Deployed Engineering (FDE):** Ein Arbeitsmodell, bei dem Entwickler eines Softwareanbieters direkt beim Kundenunternehmen vor Ort eingesetzt werden, um Systeme aufzubauen. Gartner beschreibt es als eine Branche mit echtem Hype — viele Anbieter verwenden den Begriff inzwischen ungenau für normale Beratungs- oder Implementierungsprojekte.

**Gartner:** Ein amerikanisches Marktforschungsunternehmen, das Unternehmen und IT-Entscheider mit Prognosen und Analysen berät. Gartner-Zahlen sind Prognosen (Hochrechnungen auf Basis von Befragungen und Modellen) — keine gemessenen Fakten.

**Anthropic:** Das US-Unternehmen hinter der KI namens Claude. Neben Modellentwicklung investiert Anthropic gezielt in die Ausbildung von Fachleuten, die KI in Unternehmen einsetzen.

**Frontier Deployed Engineers:** Anthropics Bezeichnung für Ingenieure, die KI-Systeme direkt in Unternehmen einführen und betreiben. Das Ausbildungsprogramm (Claude Frontier Academy, gestartet Oktober 2026) soll bis Ende 2027 10.000 solcher Ingenieure ausbilden.

**Modell-Deprecation:** Das planmäßige Abschalten einer älteren KI-Modellversion. Wer einen Agenten auf einer abgekündigten Version betreibt, bekommt danach keine Antworten mehr — der Agent hört auf zu funktionieren.

**Angebots-Agent:** Im Video das durchgehende Beispiel: ein KI-Agent, der Kundenanfragen liest und automatisch Angebote mit den passenden Produkten und Rabatten erstellt.

**Custom Build:** Ein Softwaresystem, das speziell für ein einzelnes Unternehmen entwickelt wurde und nicht als allgemeines Produkt verkauft wird. Es bekommt keine automatischen Updates; Weiterentwicklung kostet immer extra.

---

## Kernbotschaft

Das Video benennt ein strukturelles Problem, das viele Unternehmen erst merken, wenn es zu spät ist: KI-Agenten, die von externen Dienstleistern gebaut werden, verfallen ohne internes Wissen im Unternehmen. Gartners Prognose — 70 % dieser Agenten landen bis 2028 wieder im Müll — klingt drastisch, ist aber erklärbar: Produkte ändern sich, Rabattregeln ändern sich, KI-Modelle werden abgeschaltet. Wer das nicht selbst managen kann, zahlt entweder immer wieder teuer nach oder benutzt einen Agenten, dem die Kollegen irgendwann nicht mehr trauen. Anthropics 100-Millionen-Programm zeigt dieselbe Lücke aus der Angebotsseite: Die Menschen, die KI wirklich in Unternehmen zum Laufen bringen, sind gerade die knappste Ressource überhaupt. Die praktische Konsequenz: Bevor man unterschreibt, eine Frage stellen — "Was kann mein Team alleine, wenn der Anbieter weg ist?" — und wer keine klare Antwort bekommt, sollte die Zusammenarbeit überdenken.

## Themen-Tags

KI-Agenten, Anbieter-Abhängigkeit, Forward Deployed Engineering, Gartner-Prognose, Anthropic Claude Frontier Academy, Modell-Deprecation, Wissensverlust, In-House-Kompetenz, Agenten-Pflege, Unternehmensberatung KI

## Zu prüfen

- **Gartner 70 %-Prognose: Suchtreffer — Scope bestätigt.** Eine Suche bestätigte die 70 %-Zahl für das FDE-Modell (Suchtreffer: cxtoday.com). Wichtig: Diese Zahl gilt *spezifisch* für Agenten, die Anbieter direkt beim Kunden aufbauen und dann verlassen (FDE). Gartners *allgemeine* Prognose für agentic-AI-Projekte lautet "über 40 % bis Ende 2027" — das ist ein anderer, breiterer Befund. Das Video nennt die 70 % korrekt als Prognose (nicht Messung) und schränkt sie selbst auf den FDE-Kontext ein. Kein Widerspruch, nur ein Scope-Unterschied, den der Host selbst anspricht.
- **Anthropic $100M / 10.000 Ingenieure: Suchtreffer — bestätigt.** Die Claude Frontier Academy wurde laut mehreren Quellen am 2. Oktober 2026 mit genau dieser Ankündigung gestartet. Erste Absolventen werden für Anfang 2027 erwartet. Partner der ersten Kohorte: Accenture, Bain, Capgemini, Deloitte, McKinsey, Morgan Stanley, Novo Nordisk. Die meisten Quellen stützen sich auf Anthropics eigene Ankündigung, keine unabhängige Verifikation der Zielzahlen gefunden.
- **Claude-Abschaltung Ende November: Suchtreffer — wahrscheinlich korrekt.** Claude Sonnet 4.5 (erschienen 29. September 2025, also knapp ein Jahr alt) hat laut mehreren Drittquellen ein geplantes Retirement-Datum von 30. November 2026. Anthropics Dokumentation bezeichnet das Datum als "tentative" (vorläufig). Das Video nennt das Datum nicht explizit, aber die Beschreibung ("Ende November, vor einem Jahr erschienen") passt exakt auf Claude Sonnet 4.5.
- **"Weniger als 1 von 5 Kundenprojekten wird zum Standardprodukt": Nicht geprüft.** Diese Gartner-Aussage stammt aus dem Video und wurde nicht separat gegengeprüft. Plausibel im Kontext von Custom-Build-Projekten, aber die Zahl ist nicht belegt.
- **Cross-Check mit [video-summary-jAobzuCNIR8.md](video-summary-jAobzuCNIR8.md):** Statista-CEO Marc Berg beschreibt im selben Zeitraum "Forward Deployed Engineers" als Trend, den Statista selbst mit acht eigenen "Sales Consultants" testet. Kein Widerspruch, aber unterschiedliche Perspektive: Berg sieht FDE als Chance zur Kundennähe, Claes sieht es als Abhängigkeitsrisiko für den Kunden. Beide Perspektiven sind gleichzeitig richtig — aus verschiedenen Blickwinkeln.
- **Transkript-Herkunft:** Native YouTube-Untertitel auf Englisch (206 Segmente, via captions), kein Whisper-Fallback nötig. Das Video ist auf Deutsch gesprochen (Infografiken und Onscreen-Texte durchgehend Deutsch: "ZWEI MELDUNGEN", "WAS GARTNER MEINT" usw.), die YouTube-Untertitel liegen automatisch auf Englisch vor. Diese Zusammenfassung stützt sich auf den englischen Untertitel-Text, sinngemäß ins Deutsche übertragen; einzelne Formulierungen können vom gesprochenen deutschen Original leicht abweichen. Im Transkript steht mehrfach "Entropic" statt "Anthropic" — ein typischer ASR-Fehler, der durch die Onscreen-Grafiken und den Kontext eindeutig korrigierbar ist.
