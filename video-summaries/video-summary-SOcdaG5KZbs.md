# "KI aus Deutschland! Was steckt hinter Kolibri von Aleph Alpha?"

**Kanal:** Christoph Magnussen
**URL:** https://www.youtube.com/watch?v=SOcdaG5KZbs
**Länge:** 09:55
**Zusammenfassung erstellt:** 2026-10-13

---

## Worum geht es?

Seit Jahren dominieren amerikanische Firmen den Markt für große Sprachmodelle: OpenAI mit ChatGPT, Anthropic mit Claude, Google mit Gemini. Deutschland — oder Europa insgesamt — war in diesem Feld bisher nicht wirklich mit eigenen Produkten vertreten. Das ändert sich mit **Kolibri**, dem neuen Sprachmodell des deutschen Unternehmens **Aleph Alpha**, das am 3. Oktober 2026 veröffentlicht wurde.

Christoph Magnussen (Tech-CEO, Gründer der Blackboat Academy) stellt in diesem Video vor, was Kolibri ist, wer Aleph Alpha ist und was hinter der strategischen Wandlung des Unternehmens steckt. Sein Fokus liegt auf einer praktischen Frage: Kann man Kolibri als Unternehmen oder Privatperson tatsächlich einsetzen — und wenn ja, wie? Das Ergebnis ist ernüchternd-realistisch: Kolibri ist kein fertiges Produkt zum einfachen Ausprobieren, sondern ein Werkzeug für Organisationen, die bereit sind, erheblichen technischen Aufwand zu betreiben, um vollständige Kontrolle über ihre KI-Infrastruktur zu gewinnen. Trotzdem ist allein das Erscheinen eines deutschen, offen zugänglichen Sprachmodells mit starkem Deutschen-Anteil ein Meilenstein.

## Aleph Alpha: Vom Konkurrenten zu OpenAI zum Sovereign-AI-Spezialisten

Aleph Alpha wurde 2019 gegründet und hatte ursprünglich das Ziel, ein europäisches Gegengewicht zu OpenAI und Anthropic aufzubauen — also ein eigenes Frontier-Modell zu entwickeln, das mit den amerikanischen Angeboten mithalten kann. Dieses Vorhaben kam nicht ohne Turbulenzen: Der Host erwähnt Bewertungsrunden und Kurswechsel, ohne Details zu nennen. Ein Capital-Artikel (in einem Frame sichtbar: "Neuordnung bei Aleph Alpha – der Abschied von der globalen Ambition") beschreibt diesen Wandel.

Seit 2024 oder 2025 — der genaue Zeitpunkt ist laut Magnussen selbst unklar — hat Aleph Alpha die Strategie grundlegend geändert. Das Unternehmen versucht nicht mehr, global mit den US-Giganten zu konkurrieren. Stattdessen ist die Kernausrichtung jetzt **"Sovereign AI"**: KI-Systeme, die vollständig unter der Kontrolle des Betreibers laufen, ohne Abhängigkeit von amerikanischen Cloud-Diensten, mit bekannten Trainingsdaten und anpassbarem Quellcode. Die Zielkunden sind Behörden, Krankenhäuser, Verteidigungseinrichtungen und kritische Infrastruktur — überall dort, wo Datenschutz und Nachvollziehbarkeit keine Kompromisse erlauben.

Kurz vor dem Videodrehtermin hatte Aleph Alpha außerdem eine Fusion mit dem kanadischen Unternehmen **Cohere** angekündigt. Die Vereinbarung wurde im September 2026 unterzeichnet und steht noch unter dem Vorbehalt der Regulierungsbehörden. Finanziert wird der Zusammenschluss u. a. durch die Schwarz Group (Lidl/Kaufland), die 600 Millionen US-Dollar als Leitinvestor in die Cohere-Finanzierungsrunde einbringt. Das gemeinsame Unternehmen soll Hauptsitze in Toronto und Berlin haben.

## Was ist Kolibri?

Kolibri ist ein sogenanntes **Open-Weight-Modell**: Die trainierten Modellgewichte werden öffentlich zugänglich gemacht (auf Hugging Face, unter Apache-2.0-Lizenz). Das bedeutet, man kann prüfen, was im Modell steckt, es verändern und ohne Lizenzgebühren für eigene Anwendungen nutzen.

Der Host nutzt eine Analogie: Ein großes Sprachmodell ist wie ein gigantisches DJ-Mischpult, bei dem jeder Regler eine winzige Stellgröße im Modell darstellt. Bei Closed-Weight-Modellen (OpenAI, Anthropic) sieht man von außen nur das Ergebnis, nicht wie die Regler stehen. Bei Kolibri kann man alle Regler einsehen.

**Technische Eckdaten** (aus Transkript und den im Video eingeblendeten technischen Spezifikationen):
- **Architektur:** Mixture-of-Experts-Modell (MoE), 50-schichtiger Transformer, 384 Experten pro Schicht (1 gemeinsamer, 6 geroutete)
- **Parameterzahl:** ~78–80 Milliarden total; pro Token sind nur ca. 3,46 Milliarden aktiv
- **Kontextfenster:** 262.000 Token nativ, validiert bis zu 1 Million Token
- **Trainingsdaten:** ~20 Billionen Token; ca. 62,5 % Englisch, ca. 23,9 % Deutsch, ca. 13,6 % Code
- **Trainingsort:** Auf 768 NVIDIA-B200-GPUs trainiert (auf europäischer Hardware, laut Aleph Alpha)
- **Veröffentlichung:** 3. Oktober 2026

Der im Video genannte Anteil von "etwa einem Viertel Deutsch" (also ~25 %) ist eine leichte Überschätzung gegenüber den tatsächlich publizierten ~21–24 %, liegt aber in der richtigen Größenordnung.

### Warum Deutsch-Anteil wichtig ist

Das klingt technisch, ist aber inhaltlich bedeutsam: Die meisten Texte im Internet sind auf Englisch. Modelle, die überwiegend auf englischem Text trainiert wurden, "denken" oft auf Englisch — auch wenn man sie auf Deutsch anspricht. Bei Reasoning-Modellen, also Modellen, die sich Probleme Schritt für Schritt erarbeiten (wie ein inneres Monolog), führt das dazu, dass der interne Denkprozess auf Englisch stattfindet. Ein hoher Deutsch-Anteil im Training soll das verringern und das Modell besser für deutschsprachige Fachdomänen (Recht, Medizin, Verwaltung) machen.

## Für wen ist Kolibri gedacht, und was braucht man dafür?

Kolibri ist **kein fertiges Produkt zum Soforteinsatz**. Es ist kein Abonnementdienst für 20 Euro im Monat — dafür ist es nicht gemacht. Aleph Alpha richtet sich ausdrücklich an Unternehmen und Institutionen, die:
- keine Daten an externe Cloud-Dienste schicken dürfen oder wollen,
- die Kontrolle über das gesamte Modell (Training, Anpassung, Betrieb) behalten müssen,
- bereit sind, erhebliche Infrastruktur dafür aufzubauen.

Typische Einsatzfälle, die Magnussen nennt: Besprechungsprotokolle in der Verwaltung, CRM-Systeme, interne Dokumentenbearbeitung, Cyber-Verteidigung, Gesundheitswesen — überall, wo schützenswerte Daten nicht das eigene Rechenzentrum verlassen dürfen.

### Hardware-Hürde

Das Haupthindernis ist die Hardware. Um Kolibri in voller Qualität lokal zu betreiben, benötigt man mindestens eine **NVIDIA H100** oder **B200** GPU. Diese Profi-Grafikkarten kosten 30.000 bis 40.000 Euro pro Stück — und je nach Anwendung braucht man mehrere davon (die vollständigen FP8-Gewichte benötigen laut unabhängigen Quellen etwa 78 GB GPU-Speicher, was einem einzelnen H100 mit 80 GB entspricht). Das ist kein Privatnutzer-Budget, sondern Unternehmensinfrastruktur.

Aleph Alpha verdient hier vermutlich über Beratung und Implementierung: Das Unternehmen hilft beim Aufsetzen der Infrastruktur, ohne das Modell selbst zu "verkaufen".

## Kann man Kolibri trotzdem ausprobieren?

Ja, aber mit Einschränkungen. Magnussen zeigt zwei inoffizielle Zugangswege:

**1. tesseracted.com** — Eine Firma aus dem Raum München hat Kolibri auf ihrer Plattform verfügbar gemacht (im Video als "Kolibri-1 Chat" sichtbar mit dem Slogan "A little curiosity. A new perspective."). Die Anfragen sind begrenzt, der Hosting-Standort ist unklar. Wichtig: Wer tesseracted.com nutzt, nutzt **nicht automatisch** ein datenschutzkonformes Setup — das Modell läuft auf deren Servern, und man weiß nicht, welche Daten wohin fließen.

**2. Hugging Face** — Die Gewichte sind auf der Modellplattform Hugging Face herunterladbar. Jemand hat außerdem eine quantisierte Version (GGUF-Format) bereitgestellt, die für normale Computer kleiner gemacht wurde. Als Faustregel gilt: Man benötigt etwa so viel RAM, wie die Datei Gigabyte hat. Magnussen testet es mit LM Studio auf seinem MacBook Air mit 32 GB RAM — das Programm meldet "likely too large" (wahrscheinlich zu groß). Ein MacBook Pro kann mit bis zu 128 GB RAM konfiguriert werden, Mac Studios mit noch mehr. Für echten lokalen Betrieb müsste man über Laptops hinausgehen.

Eine dritte Option, die Magnussen kurz erwähnt: Hugging Face Spaces — dort kann man Mietrechner buchen und das Modell betreiben. Das wird technisch, ist aber machbar.

## Die größere Perspektive: Europa und die KI-Lücke

Magnussen schließt mit einer Einordnung, die über das Produkt hinausgeht. Der Wettlauf um die besten Frontier-Modelle (die absolut leistungsstärksten Modelle) ist für Europa möglicherweise nicht mehr gewinnbar — die USA und China haben zu viel Vorsprung. Aber dieser Wettlauf ist nicht der einzige, der zählt.

**Was zählt, ist Kompetenz beim Betrieb lokaler Modelle.** In sicherheitskritischen Bereichen (Verteidigung, Behörden, kritische Infrastruktur) werden immer leistungsfähigere lokale Modelle gebraucht. Wer heute lernt, solche Modelle zu betreiben und anzupassen, baut Kompetenz auf, die später wertvoll sein wird — auch wenn man das Modell nicht selbst erfunden hat.

Außerdem: Sprache ist kulturelle Infrastruktur. Wenn Sprachmodelle hauptsächlich auf Englisch "denken", besteht die Gefahr, dass deutsch-sprachige Konzepte, Nuancen und rechtliche Strukturen in KI-Systemen schlechter repräsentiert sind. Kolibri ist ein Versuch, dem entgegenzuwirken.

## Begriffe

**Open-Weight-Modell:** Ein KI-Modell, dessen trainierte Gewichte (die internen Parameter, die das Verhalten des Modells bestimmen) öffentlich zugänglich gemacht werden. Damit kann jeder das Modell herunterladen, selbst betreiben, anpassen und in eigene Produkte einbauen. Gegenteil: Closed-Weight-Modell (OpenAI, Anthropic), bei dem nur eine API verfügbar ist.

**Mixture of Experts (MoE):** Eine Modellarchitektur, bei der nicht alle Parameter bei jeder Anfrage aktiv sind. Stattdessen leitet ein Routing-Mechanismus jede Eingabe an eine Teilmenge von "Experten" weiter. Kolibri hat ~80 Milliarden Parameter insgesamt, aber pro Anfrage sind nur ~3,46 Milliarden aktiv. Das spart Rechenzeit beim Betrieb.

**Sovereign AI:** KI-Betrieb, bei dem die gesamte Infrastruktur (Hardware, Software, Daten) unter der Kontrolle des Betreibers liegt — ohne Abhängigkeit von ausländischen Cloud-Diensten oder Drittanbietern. Besonders relevant für Behörden, Verteidigung und kritische Infrastruktur.

**Parameter:** Die numerischen Stellgrößen in einem neuronalen Netz, die beim Training angepasst werden und das Verhalten des Modells festlegen. Mehr Parameter bedeuten in der Regel höhere Modellkapazität, aber auch mehr Rechen- und Speicherbedarf.

**Inferenz:** Der Betrieb eines trainierten Modells zur Erzeugung von Ausgaben (im Gegensatz zum Training). Wenn man Kolibri lokal "laufen lässt", führt man Inferenz durch. Das erfordert eine GPU, die das Modell in ihren Arbeitsspeicher laden kann.

**Hugging Face:** Die größte Plattform zum Teilen und Herunterladen von KI-Modellen. Ähnlich wie GitHub für Code. Aleph Alpha hat Kolibri dort unter Apache-2.0-Lizenz veröffentlicht.

**GGUF:** Ein Dateiformat für quantisierte Modellgewichte (komprimierte Versionen), das besonders für den Betrieb auf Consumer-Hardware (MacBooks, PCs ohne Profi-GPU) geeignet ist. Die Qualität sinkt etwas, aber der Speicherbedarf ist deutlich geringer.

**Apache 2.0:** Eine offene Software-Lizenz, die kommerzielle Nutzung, Veränderung und Weitergabe erlaubt, solange der Ursprung angegeben wird. Für KI-Modelle bedeutet das: keine Lizenzgebühren, freie Anpassbarkeit.

## Kernbotschaft

Kolibri von Aleph Alpha ist das erste deutsche Large Language Model mit öffentlichen Gewichten und erheblichem Deutsch-Anteil in den Trainingsdaten (~21–24 %). Technisch handelt es sich um ein MoE-Modell mit ~78–80 Milliarden Gesamtparametern und ~3,5 Milliarden aktiven Parametern pro Anfrage, veröffentlicht unter Apache-2.0-Lizenz. Der Fokus des Produkts liegt nicht auf dem Massenmarkt, sondern auf souveränem Betrieb in regulierten Sektoren (Behörden, Gesundheitswesen, Verteidigung), wo vollständige Datenkontrolle und Nachvollziehbarkeit entscheidend sind. Für Endnutzer gibt es zwei inoffizielle Zugangswege (tesseracted.com und Hugging Face), die beide mit Einschränkungen verbunden sind. Aleph Alpha befindet sich gleichzeitig in einem Fusionsprozess mit dem kanadischen Unternehmen Cohere, dessen Abschluss noch unter Vorbehalt regulatorischer Genehmigung steht. Das Video ist kein Werbevideo für Kolibri, sondern eine nüchterne Einordnung: Das Modell ist ein wichtiger Schritt für Europa, aber kein einfach nutzbares Produkt.

## Themen-Tags

Aleph Alpha, Kolibri, Kolibri-1, Open-Weight-Modell, Mixture of Experts, Sovereign AI, deutsches KI-Modell, Cohere-Fusion, Hugging Face, H100, B200, GGUF, Datenschutz, lokale KI, Christoph Magnussen

## Zu prüfen

- **Gründungsjahr Aleph Alpha:** Video nennt 2019 — per WebSearch (Suchtreffer) bestätigt.
- **Kolibri-Release-Datum:** Video zeigt in einem eingeblendeten Frame "3rd of October 2026" — per WebSearch (Suchtreffer, mehrere unabhängige Quellen) bestätigt.
- **~80 Mrd. Parameter, ~3–4 Mrd. aktiv:** Video nennt "roughly 78, almost 80 billion" total, "three to four billion" aktiv — per WebSearch (Suchtreffer) bestätigt: ~78 Mrd. total, ~3,46 Mrd. aktiv pro Token. Korrekte Aussage.
- **Deutsch-Anteil ~25 %:** Video sagt "I believe around a quarter" — technische Spezifikation im Video-Frame zeigt 23,9 %, Websuche nennt 21,3 % (Aleph Alpha-eigene Angaben). Leichte Überschätzung im Video, aber vertretbare Annäherung. `Suchtreffer`
- **Cohere-Fusion:** Im Video: "A few weeks ago, they announced a merger" — per WebSearch (Suchtreffer) bestätigt: Erstankündigung April 2026, definitiver Vertrag September 2026, noch nicht vollzogen (Regulierungsgenehmigung ausstehend). Die Einschätzung "hasn't closed yet" ist korrekt.
- **GPU-Kosten 30.000–40.000 Euro für H100/B200:** Plausibel (entspricht bekanntem Marktpreisniveau), nicht separat per WebSearch nachgeschlagen. Nicht verifiziert.
- **MacBook Pro bis 128 GB RAM:** Entspricht dem aktuell konfigurierbaren Maximum bei Apple-Geräten — nicht gesondert nachgeschlagen, aber allgemein bekannt. Nicht unabhängig verifiziert.
- **GGUF-Frame: "700 Millionen Parameter":** Frame 53 (Hugging Face-Seite für die quantisierte GGUF-Version) zeigte laut Bildbeschreibung "700-Millionen-Parameter" — das widerspricht dem Transkript (~80 Mrd.) und den per WebSearch bestätigten Werten. Wahrscheinlichste Erklärung: Die lokale Vision-KI hat einen anderen GGUF-Eintrag falsch gelesen oder verwechselt. Dies ist kein inhaltlicher Widerspruch im Video selbst.
- **Cross-Check gegen bestehende Notizen:** Keine früheren Zusammenfassungen im Repo behandeln Aleph Alpha oder Kolibri direkt. Zwei Dateien enthalten "Sovereign AI" oder "open-weight" in anderem Kontext (video-summary-aTaKM8FSy2k.md: Community-Plugin "EU-Router" für EU-souveräne KI; video-summary-Ne2UH682x9I.md: Qwen3.6-27B als open-weight-Modell) — kein Widerspruch, keine thematische Überschneidung, die eine Korrektur erfordern würde. Kein sonstiger Widerspruch zu bestehenden Notizen gefunden.
- **Anzahl Abonnenten Christoph Magnussen:** Frame 79 zeigt 132K Abonnenten, 513 Videos — nicht per WebSearch verifiziert; nur für Kontext relevant.

## Quellen der Plausibilitätschecks

- [Datacamp — Aleph Alpha Kolibri-1](https://www.datacamp.com/de/blog/aleph-alpha-kolibri-1) — `Suchtreffer`
- [testingcatalog.com — Aleph Alpha releases open-weight Kolibri with 1M context](https://www.testingcatalog.com/aleph-alpha-releases-open-weight-kolibri-with-1m-context.md) — `Suchtreffer`
- [Leaders League — Cohere and Aleph Alpha sign definitive agreement](https://www.leadersleague.com/en/news/cohere-and-german-ai-company-aleph-alpha-sign-definitive-agreement-to-create-transatlantic-sovereign-ai-group) — `Suchtreffer`
- [Pulse2 — Cohere and Aleph Alpha: $600 Million Financing Commitment](https://pulse2.com/cohere-and-aleph-alpha-600-million-financing-commitment-from-schwarz-group-anchors-transatlantic-sovereign-ai-merger/amp/) — `Suchtreffer`
