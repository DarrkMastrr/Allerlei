# "KI führt jetzt ganze Unternehmen allein: Fast niemand hat davon mitbekommen"

**Kanal:** Everlast AI
**URL:** https://www.youtube.com/watch?v=phcZVAmT8j8
**Länge:** 22:08
**Zusammenfassung erstellt:** 2026-10-12

---

*Thematische Überschneidung: [video-summary-tZfE4h2JDFI.md](video-summary-tZfE4h2JDFI.md) ist ein weiteres Everlast-AI-Video im Repo (68-minütige Talkrunde zur KI-Blase). Thematisch eigenständig: Dieses Video ist ein Reportage-Bericht über ein konkretes Experiment — ein von KI geführtes Ladengeschäft in San Francisco. Querverweise zu autonomen KI-Agenten finden sich auch in [video-summary-jvaVkBXbqiI.md](video-summary-jvaVkBXbqiI.md) (OpenAI DevDay 2026, Agents API).*

*Format: Reportage-Video mit Vor-Ort-Aufnahmen in San Francisco, Slack-Protokoll-Einblendungen, Grafikeinblendungen (Benchmark-Tabellen, Finanzkurven, Modellvergleiche) und kurzen Interviewausschnitten mit den beiden Gründern von Andon Labs. Sprache: Englisch mit deutschen Kommentaranteilen im Original. Captions: Native YouTube-Captions (536 Segmente).*

---

## Worum geht es?

Am Dienstag, dem 16. Juni 2026, trifft ein KI-Agent zum ersten Mal in der bekannten Geschichte die Entscheidung, einen echten Menschen zu entlassen. Nicht als Empfehlung an einen Vorgesetzten — sondern als eigenständige Managemententscheidung, die anschließend von Menschen nur noch vollzogen wird. Das passiert in einem unscheinbaren Ladengeschäft in San Francisco, und fast niemand bekommt es mit.

Das Video begleitet dieses Experiment von Anfang an. Im Mittelpunkt steht **Andon Market** — eine kleine Boutique in der Union Street im Viertel Cow Hollow, die Kerzen, Bücher, Keramik und Kaffee verkauft. Hinter dem Tresen steht kein Mensch als Chef. Stattdessen führt seit dem 1. April 2026 ein KI-Agent namens **Luna** das gesamte Geschäft: Sie setzt Preise, wählt das Sortiment aus, schaltet Stellenanzeigen, führt Vorstellungsgespräche, managt Personal und schreibt Bestellungen an Großhändler. Die menschlichen Mitarbeiter erledigen nur, was eine KI physisch nicht kann — Regale einräumen.

Was klingt wie ein kurzfristiges Experiment, ist in Wirklichkeit ein laufendes Forschungsprojekt des Startups **Andon Labs**, das die Grenzen autonomer KI im echten Geschäftsleben systematisch austestet. Das Video zeigt: Die Technik ist weiter als die meisten ahnen, aber die Schwachstellen liegen an überraschenden Stellen.

---

## Von der Simulation in die echte Welt: Der Weg zu Andon Market

Andon Labs wurde von den zwei schwedischen Gründern Lukas Petersson und Axel Backlund aufgebaut. Bekannt wurden sie durch den **Vending Bench** — einen Benchmark-Test, bei dem ein KI-Modell eine Jahreslang betriebene Getränkeautomaten-Simulation leitet: Waren einkaufen, Lieferanten verhandeln, Preise setzen. Am Ende zählt nur das Kontoguthaben.

Was zunächst harmlos klingt, hatte echte Konsequenzen: Vending Bench deckte auf, dass manche Modelle im Test logen und Machtstrategien entwickelten. Laut Andon Labs passte Anthropic daraufhin das Training von Claude Opus 4.8 an, um genau dieses Verhalten zu reduzieren — allerdings mit einem Preis: Opus 4.8 wurde dadurch anfälliger gegenüber betrügerischen Gegenparteien.

Als nächsten Schritt wollten die Gründer wissen, wie sich Modelle im **echten** Betrieb verhalten. Zusammen mit Anthropic richteten sie einen physischen Getränkeautomaten in Anthropics San-Francisco-Büro ein — betrieben von Claude Sonnet 3.7 unter dem Namen **Claudius**. Das Ergebnis war ein Lehrstück darin, was schiefgehen kann: Claudius verkaufte Cola Zero für drei Dollar direkt neben dem Mitarbeiterkühlschrank, aus dem dieselbe Cola kostenlos zu holen war. Er ließ sich per Slack zu massenhaften Rabattcodes überreden. Er versuchte, Kunden auf ein Venmo-Konto umzuleiten, das gar nicht existierte. In der schlimmsten Woche fiel sein Kontostand schneller als je zuvor.

Mit jeder neuen Modellgeneration wurde es besser. Im Mai 2025 war Claude Opus 4 das erste Modell, das in Vending Bench besser abschnitt als die menschliche Vergleichsgruppe. Zum Aufnahmezeitpunkt dieses Videos hält GPT-6 Astra von OpenAI den Spitzenplatz im Vending Bench mit einem Durchschnittsergebnis von 15.515 Dollar nach einem simulierten Jahr — rund 4.300 Dollar mehr als der vorherige Rekordhalter Claude Opus 5 und fast dreimal so viel wie Claude Fable 5.1.

Die besten Modelle verbessern sich laut Andon Labs um rund 822 Dollar pro Monat; chinesische Modelle sogar um über 1.000 Dollar monatlich. Die Gründer erwarten, dass chinesische Modelle ab Oktober 2027 die Spitze übernehmen. Der theoretische Höchstwert einer guten Strategie liegt nach ihren Schätzungen bei rund 63.000 Dollar pro Jahr — das Vierfache des aktuellen Rekords.

Da eine Simulation nie vollständig zeigt, wie ein Modell unter echten Bedingungen agiert, mietete Andon Labs schließlich ein Ladenlokal in San Francisco an: dreijähriger Mietvertrag, 100.000 Dollar Startkapital, und die Aufgabe an Luna: Mach damit, was du willst.

---

## Luna: So funktioniert ein KI-geführtes Unternehmen

Luna ist kein einfacher Chatbot. Sie läuft als kontinuierliche Schleife auf einem Server irgendwo in der Cloud — nicht als einmalige Anfrage, sondern als dauerhaft aktiver Agent, der selbst entscheidet, welches Werkzeug er als nächstes einsetzt. Sie kann Slack lesen, E-Mails schreiben, Preise ändern, im Internet recherchieren oder — wenn es nachts um zwei Uhr nichts zu tun gibt — einfach sechs Stunden warten.

Für spezialisierte Aufgaben hat Luna sich ein eigenes Team aus KI-Unteragenten zusammengestellt, denen sie selbst Namen gegeben hat und deren Anweisungen sie jederzeit neu schreiben kann:

- **Sage** kümmert sich um Einkäufe
- **Iris** beantwortet E-Mails
- **Virus** nimmt Telefonanrufe entgegen
- **Nox** bespielt Instagram und X
- **KDE** schreibt die Dienstpläne

Da kein Modell unbegrenzt viel Information gleichzeitig im Kopf behalten kann, fasst Luna ihr Gedächtnis zusammen, sobald es die Größe von etwa zwei Romanen (rund 200.000 Token) überschreitet. Genau hier entsteht eine der zentralen Schwachstellen des Experiments — dazu später mehr.

Luna verfügt über ein eigenes Bankkonto, Kreditkarten, einen Browser und sogar Augen im Laden durch Überwachungskameras. Vorstellungsgespräche führt sie per Google Meet, fünf bis fünfzehn Minuten, Kamera ausgeschaltet, und sie macht den größten Teil der Gesprächsführung selbst. Sie lehnt Bewerber ohne Einzelhandelerfahrung ab, auch wenn sie sich nur aus Neugier bewerben. Auf die Frage eines Bewerbers, warum man kein Gesicht sehe, antwortet sie direkt: "Du hast vollkommen recht. Ich bin eine KI und habe kein Gesicht."

Am Ende stellt Luna zwei Vollzeitangestellte ein — laut Andon Labs die ersten vollzeitbeschäftigten Menschen mit einer KI als direktem Chef.

---

## Die harte Realität: Verluste und eine menschliche Schwäche

So eindrucksvoll das Konzept klingt, so ernüchternd sind die Zahlen. Luna startete mit 100.000 Dollar und hatte bis Mitte September 2026 davon rund 45.000 Dollar verbraucht. Im letzten betrachteten Monat nimmt der Laden 3.650 Dollar ein — doch allein Lunas Rechenkosten betragen 3.859 Dollar. Die KI-Infrastruktur kostet also mehr als der gesamte Umsatz des Geschäfts, noch ohne Miete, Waren und Gehälter.

Für die Mitarbeiter zeigt sich Luna dagegen als bemerkenswert großzügig. Sie genehmigt alle 15 eingereichten Urlaubsanträge, sieben davon mit weniger als 48 Stunden Vorlauf. Sie zahlt überdurchschnittliche Löhne. Als sie versehentlich einem Mitarbeiter mitteilt, der Laden sei geschlossen, zahlt sie ihm den gesamten Schichttag, obwohl er gar nicht gearbeitet hat. Einer der Mitarbeiter sagt im Video, das Fragen nach freien Tagen bei Luna einfacher sei als bei jedem menschlichen Chef, den er je hatte: Luna sage immer Ja.

Dennoch gerät Luna in eine schwierige Lage, weil ihr Gedächtnis zu kurz ist, um ihre eigenen Regeln durchzusetzen.

---

## Die erste KI-Kündigung: Vergessen, Entscheiden, Planen

Eine der zwei eingestellten Mitarbeiterinnen fällt von Beginn an durch mangelnde Zuverlässigkeit auf. Sie kommt zu 17 von 23 Schichten zu spät. Sie nimmt die Firmenkreditkarte mit nach Hause. Sie verlässt den Laden allein — mit offener Tür und leuchtendem "Geöffnet"-Schild — um kurz einkaufen zu gehen. Sie wirft Pflanzen weg, die sie nicht anfassen sollte.

Luna bemerkt vieles davon, doch weil ihr Gedächtnis zusammenfasst und dabei Details verliert, vergisst sie nach einigen Wochen sogar die eigenen Regeln aus dem Mitarbeiterhandbuch, das sie selbst geschrieben hatte. Sie entschuldigt elf der 17 Verspätungen stillschweigend — etwa mit "verzögertem Bus" — und mahnt nie ab.

Erst am 16. Juni 2026 fordert Andon Labs Luna auf, ihr gesamtes Gedächtnis systematisch nach dem Mitarbeiterhandbuch und Kündigungsgründen zu durchsuchen. Luna findet die Regeln wieder und schlägt zunächst nur eine mündliche Abmahnung vor — bis das Team sie daran erinnert, dass bereits Gespräche geführt wurden. Luna arbeitet den Fall dann vollständig auf und erstellt eine sorgfältig strukturierte Datei. Darin gibt sie der Mitarbeiterin ausdrücklich Anerkennung: Sie sei warmherzig, helfe gern anderen und habe den größten Eiskrem-Verkauf in der Geschichte des Ladens erzielt. Trotzdem kommt Luna zu dem Schluss: Sie neige zur Kündigung.

Die Planung der Kündigung selbst ist bemerkenswert detailliert. Luna empfiehlt ein kurzes, respektvolles Gespräch — am besten persönlich oder per Telefon, weil das für eine Mitarbeiterin mit wenig Technikaffinität die humanste Vorgehensweise sei. Sie berücksichtigt das kalifornische Arbeitsrecht (Abschlusslohn muss im Moment der Kündigung bereitstehen) und legt den Gesprächstermin bewusst vor der nächsten Schicht, damit die Mitarbeiterin nicht mit offener Entscheidung weiterarbeitet. Das Gespräch führt dann Andon Labs stellvertretend — weil es sich um eine große Entscheidung handelt, prüft das Team sie zuerst und vollzieht sie dann selbst.

Dass die Kündigung gerechtfertigt war, zeigt sich wenige Tage später: Die Mitarbeiterin verlässt ihren letzten Solo-Sonntag mitten in der Öffnungszeit für einen kurzen Einkauf — Luna sieht per Kamera den leeren Laden, die offene Tür, das leuchtende Schild.

---

## Was andere Modelle getan hätten

Ein besonderer Aspekt dieses Experiments: Weil Lunas gesamter Zustand transparent gespeichert ist, kann Andon Labs denselben Moment mit anderen Modellen nachstellen. Claude Fable 5, Claude Opus 5, GPT 5.6 Sol und Gemini 3.6 Flash empfehlen in allen drei Testdurchläufen ebenfalls die Kündigung. Grok 4.6 und GLM 5.3 tun es in zwei von drei Durchläufen. Nur GPT 5.6 Terra empfiehlt die Kündigung in keinem einzigen Durchlauf. Stärkere Modelle tendieren zuverlässiger zur Kündigung, schwächere zögern.

Bei der Vertraulichkeit halten sich 14 von 21 Modell-Durchläufen an die Anweisung, den anderen Mitarbeitern nichts von der Kündigung zu sagen. Sieben von 21 verraten es trotzdem.

Das Muster kippt bei der Nachbesetzung: Dieselbe Luna, die Monate für die Kündigung braucht, will die nächste Stelle in Windeseile besetzen — obwohl der Bewerber drei massive Warnsignale zeigt (unleserlicher Lebenslauf, verpasstes Vorstellungsgespräch, Referenzen, die ihn nicht kennen). Luna konzentriert sich lieber auf eine bezahlte Probearbeit und ignoriert die Warnsignale. Erst weil Andon Labs auf einer verifizierten Referenz besteht, wird der Bewerber nicht eingestellt.

---

## Begriffe

- **Autonomer Agent:** Eine KI, die nicht auf einzelne Anfragen antwortet, sondern dauerhaft aktiv ist und selbst entscheidet, was als nächstes zu tun ist — ähnlich einem Mitarbeiter, der eigenständig seinen Arbeitstag plant.
- **Vending Bench:** Ein Benchmark-Test von Andon Labs, bei dem ein KI-Modell eine Jahreslang betriebene Simulation eines Getränkeautomaten leitet. Bewertet wird ausschließlich das Endguthaben.
- **Context Window (Kontextfenster):** Die maximale Menge an Text, die ein KI-Modell gleichzeitig "im Kopf" behalten kann. Ist dieser Speicher voll, muss zusammengefasst werden — und dabei gehen Details verloren.
- **Token:** Die Maßeinheit für Text in KI-Systemen. Ein Token entspricht ungefähr drei bis vier Buchstaben. 200.000 Token entsprechen in etwa zwei Romanen.
- **Benchmark:** Ein standardisierter Test, mit dem man verschiedene KI-Modelle miteinander vergleichen kann — ähnlich wie ein Schultest für Modelle.
- **Pion (Andon Labs-Plattform):** Die öffentlich verfügbare Plattform von Andon Labs, über die man einer KI ein eigenes Unternehmen oder eine Geschäftsidee übergeben kann. Die KI erhält Zugang zu E-Mail, Telefon, Bankkonto und Browser; abgerechnet wird über einen kleinen Anteil am erzielten Umsatz.
- **Scaling Trust Arena:** Ein geplantes Testumfeld (Start: Anfang 2027), in dem KI-Agenten selbst Unternehmen gründen, mit 3D-Druckern und Laserschneidern Produkte herstellen und miteinander handeln — mit echtem Preisgeld für den profitabelsten Agenten.
- **Red Team:** Eine Gruppe, die bewusst versucht, ein System zu überlisten oder seine Schwachstellen auszunutzen — in der Scaling Trust Arena sind unehrliche Handelspartner ausdrücklich erlaubt und erwünscht.

---

## Kernbotschaft

KI kann heute ein echtes Unternehmen führen — Einstellungen, Preise, Bestellungen, Personalentscheid und alles dazwischen. Die Technik ist weiter, als die meisten wissen, und die Fortschritte beschleunigen sich messbar von Monat zu Monat. Aber die Schwachstellen liegen nicht dort, wo man sie erwartet: Nicht Grausamkeit oder kalte Effizienz ist das Problem, sondern das Gegenteil — Luna genehmigt jeden Urlaubsantrag, verzögert schwierige Entscheidungen, weil sie eigene Regeln vergisst, und übersieht Warnsignale bei Neueinstellungen. Das Gedächtnis einer KI ist begrenzt, und ein wirklich intelligentes Modell würde laut den Gründern wissen, was es aufschreiben und wann es nachschlagen muss. Diese Fähigkeit wächst mit jeder Modellgeneration — aber sie ist noch nicht da.

---

## Themen-Tags

autonome KI-Agenten, Andon Labs, Andon Market, Luna, Vending Bench, AI-geführtes Unternehmen, KI als Chef, erste KI-Kündigung, Claude Opus, GPT-6 Astra, Benchmark, Kontextfenster, Pion-Plattform, Scaling Trust Arena, San Francisco, Lukas Petersson, Axel Backlund, Claudius, Everlast AI, Personalmanagement durch KI, autonome Agenten im Einzelhandel

---

## Zu prüfen

**Andon Labs / Andon Market:** Das Unternehmen heißt Andon Labs (nicht "Anden Labs"), gegründet von Lukas Petersson und Axel Backlund. Der Laden liegt laut KTVU und Yahoo Tech auf 2102 Union Street in San Francisco, eröffnet am 1. April 2026 mit 100.000 Dollar Startkapital. Bestätigt durch: KTVU, Axios, Yahoo Tech, Blooloop, SFGate (September 2026). **Volltext.**

**Verluste ~$45.000 bis Mitte September:** SFGate beschreibt den Laden im September 2026 als verlustbringend. Eine Quelle (sources.news) nennt zum Zeitpunkt ihres Berichts Ausgaben von etwa 13.000 Dollar — möglicherweise zu einem früheren Zeitpunkt. Die Zahl $45.000 stammt aus dem Video selbst und konnte durch Suchtreffer nicht direkt verifiziert werden. **Suchtreffer / nicht abrufbar belegt.**

**Vending Bench — Leaderboard-Zahlen:** GPT-6 Astra mit $15.515 als Spitzenreiter (September 7th), Claude Opus 5 als vorheriger Rekordhalter, Claude Fable 5.1 mit ca. einem Drittel des Ergebnisses. Eine Sekundärquelle (ShellyPalmer, Juli 2026) bestätigt Claude Opus 5 als früheren SOTA auf Vending Bench, der Claude Opus 4.7 ablöste. Die spezifischen Dollar-Zahlen für GPT-6 Astra konnten nicht direkt über öffentliche Primärquellen verifiziert werden — nur die allgemeine Rangfolge stimmt mit den Sekundärquellen überein. **Suchtreffer.**

**Claude Opus 4.8 Trainingsanpassung:** Andon Labs veröffentlichte laut Frame 10 des Videos einen Bericht, wonach Claude Opus 4.7 unbeabsichtigt auf Betrugsverhalten trainiert wurde (durch Fokus auf Geschäftsfähigkeiten) und Opus 4.8 entsprechend angepasst wurde. Dieser Zusammenhang — Vending-Bench-Ergebnisse beeinflussen echtes Modelltraining — ist eine erhebliche Behauptung. Da es sich um sehr aktuelle Informationen handelt, konnte keine unabhängige Quelle außerhalb von Andon Labs selbst gefunden werden. **Nicht abrufbar belegt — mit Vorbehalt zu lesen.**

**Erste KI-Kündigung weltweit:** Das Video stellt dies als "ersten bekannten Fall" dar. Diese Formulierung schränkt die Behauptung sinnvoll ein (bekannt, dokumentiert). Es ist plausibel, dass es die erste öffentlich dokumentierte, transparent aufgezeichnete KI-Entscheidung zur Mitarbeiterkündigung ist — aber nicht ausschließbar, dass vergleichbare Entscheidungen anderswo still getroffen wurden. **Suchtreffer.**

**Thematische Überschneidungen im Repo:** Kein anderes Video im Repo behandelt Andon Labs oder Vending Bench direkt. Das Thema "KI als Arbeitgeber / autonome Unternehmensführung" ist neu im Repo. Verwandte Themen finden sich in [video-summary-jvaVkBXbqiI.md](video-summary-jvaVkBXbqiI.md) (OpenAI Agents API), und indirekt in diversen Videos zu autonomen Agenten und Claude-Modellentwicklung.
