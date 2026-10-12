# "Das neue ChatGPT ist da: DAS ändert sich jetzt für dich! Alle 20+ Updates | KI-NEWS"

**Kanal:** Everlast AI (Leonard Schwedding)
**URL:** https://www.youtube.com/watch?v=1ID_VcwzIo8
**Länge:** 31:04
**Zusammenfassung erstellt:** 2026-10-12

---

*Thematische Überschneidung: Dasselbe Ereignis (OpenAI DevDay 2026, 29.09.2026) wurde bereits aus zwei anderen Perspektiven im Repo zusammengefasst: [video-summary-jvaVkBXbqiI.md](video-summary-jvaVkBXbqiI.md) (Christoph Magnussen, Top 5 aus Nutzerperspektive) und [video-summary-A4lIdVtVBeg.md](video-summary-A4lIdVtVBeg.md) (Kris AI2ROI, technisch-kompaktere Einordnung). Das vorliegende Video ist inhaltlich breiter: Leonard Schwedding war persönlich vor Ort in San Francisco und kombiniert eine ausführlichere DevDay-Einordnung mit einem Vor-Ort-Bericht über chinesische Humanoide in Deutschland sowie Nebenthemen (Gemini 4 Argon, Figure-2-Ausmusterung, KI-Avatare). Inhaltliche Abweichungen von den anderen DevDay-Zusammenfassungen: siehe "Zu prüfen".*

---

## Worum geht es?

Am 29. September 2026 hat OpenAI seinen jährlichen Developer Day in San Francisco abgehalten — die Konferenz, auf der das Unternehmen seine wichtigsten Neuheiten für Entwicklerinnen und Entwickler ankündigt. In diesem Jahr wurden über zwanzig Neuheiten präsentiert, davon mehr als ein Dutzend mit praktischen Auswirkungen für alle, die Apps mit KI bauen oder täglich mit ChatGPT arbeiten. Leonard Schwedding, Host des deutschsprachigen Kanals Everlast AI, war persönlich vor Ort, besuchte auch Räumlichkeiten abseits der Livestreams und fasst alle wesentlichen Ankündigungen für sein Publikum zusammen.

Die zentrale Botschaft des Abends war nicht ein einzelnes Modell oder ein einzelnes Feature, sondern eine grundlegende Richtungsänderung: ChatGPT soll sich von einem Werkzeug, das man einzeln befragt, zu einem dauerhaft laufenden persönlichen Assistenten wandeln — einem, der Kalender liest, Apps kennt, proaktiv Ideen einbringt und im Hintergrund weiterarbeitet, auch wenn man selbst nicht am Rechner sitzt. Das klingt zunächst abstrakt, hat aber konkrete technische Implikationen, die im Folgenden erläutert werden.

Neben dem DevDay berichtet das Video über eine zweite Entwicklung, die für Deutschland besonders relevant ist: chinesische Humanoid-Roboter (UBTECH) sind über den deutschen Distributor TerraRobotics erstmals regulär im deutschsprachigen Raum erhältlich und wurden bei einer Veranstaltung in Deutschland live vorgeführt. Dazu kommen kurze Einordnungen zu Gemini 4 Argon (Google), der Ausmusterung des Roboters Figure 2, einem KI-Avatar-Modell namens Tavus sowie zur KI-gestützten Neugestaltung der amerikanischen Regierungswebsite.

---

## OpenAI DevDay 2026: Die wichtigsten Ankündigungen

### Dots: Der dauerhafte KI-Agent

Das Herzstück der diesjährigen Ankündigungen heißt **Dots** (manchmal als "Alfred" referenziert, nach dem im Demo genutzten Agenten-Namen). Dots sind dauerhafte KI-Agenten innerhalb von ChatGPT, vergleichbar mit dem, was andere Dienste als "Bots" oder "Assistenten" kennen — mit dem Unterschied, dass sie selbstständig handeln, Aufgaben im Hintergrund erledigen und proaktiv auf den Nutzer zugehen.

Was das konkret bedeutet: Ein Dot verbindet sich mit E-Mail, Kalender, Cloud-Speicher und anderen Apps. Wenn man dem System mehrfach fragt, wie die eigenen Unternehmens-KPIs stehen, schlägt der Dot vor, ein KPI-Dashboard zu bauen. Er schickt Erinnerungen via iMessage, führt Telefongespräche im Namen des Nutzers und arbeitet weiter, auch wenn der Laptop geschlossen ist. Die Demo zeigte, dass die meisten Eingaben nicht mehr getippte Prompts sind, sondern Sprachbefehle — was das Werkzeug erheblich zugänglicher macht. OpenAI nennt dieses Konzept die "Intention Economy": Die KI antizipiert, was man als nächstes braucht, statt auf Befehle zu warten.

Schwedding sieht in Dots eine direkte Antwort auf den Druck durch Konkurrenzprodukte — insbesondere Meta Muse, das zwischenzeitlich den App-Store-Platz 1 in den USA von ChatGPT übernommen hatte. Grok (von X) wird als weiterer Vergleichspunkt für Dots genannt.

### Spaces: Gemeinsam mit Agenten arbeiten

**Spaces** sind kollaborative Arbeitsbereiche, in denen Menschen und KI-Agenten gleichzeitig an Dokumenten arbeiten können. Das Konzept ist vergleichbar mit Notion oder Google Docs — aber mit einer Kommentarfunktion, über die man Aufgaben an Agenten delegieren kann. Präsentationen, Dokumente, Mini-Apps und Webseiten können gemeinsam bearbeitet, in Echtzeit kommentiert und als Team geteilt werden. OpenAI positioniert das als Konkurrenz zu Claude's Artifacts-Funktion und als Antwort auf das Arbeiten mit Agenten über Slack.

### GPT-6.1 Sol: Das günstigere Spitzenmodell

OpenAI hat mit **GPT-6.1 Sol** ein neues Modell für die API vorgestellt. Es kostet laut anderen Quellen rund 2 Dollar pro Million Eingabe-Token und 10 Dollar pro Million Ausgabe-Token — das Vorgängermodell **GPT-6 Astra** (OpenAIs bisheriges Spitzenmodell) kostet 10 bzw. 50 Dollar. Für Entwickler bedeutet das: nahezu gleiche Qualität für ein Fünftel des Preises, beim Caching sogar für ein Zehntel. Benchmarks wurden auf der Veranstaltung selbst nicht gezeigt; der praktische Vergleich mit Modellen wie Claude Sonnet 5.5 steht noch aus. Schwedding hebt hervor, dass Sol sich besonders für Code-Aufgaben eignet — er verweist auf Benchmarks auf der Plattform Artificial Analysis, die Sol bei rund 72 Cent pro erledigter Aufgabe verorten.

*Hinweis zur Namensschreibung: Die automatischen YouTube-Captions schreiben konsistent "Astra" für GPT-6 Astra und lassen den "Sol"-Namen im Rauschen verschwinden; die tatsächlichen Modellnamen ("GPT-6 Astra" und "GPT-6.1 Sol") wurden aus den bestehenden Repo-Einträgen und Plausibilitätschecks ergänzt.*

### Ultra Fast und der Pro 500 Plan

Neben Sol hat OpenAI einen neuen Inferenz-Modus namens **Ultra Fast** angekündigt: 300 Token pro Sekunde, laut OpenAI achtmal schneller als bisher — aber sechsmal so teuer. Der Saal reagierte auf diesen Punkt laut Schwedding mit einem hörbaren Raunen. Dazu passend gibt es den neuen **Pro 500**-Plan für 500 Dollar monatlich, der Ultra Fast einschließt, die bisherige 5-Stunden-Nutzungsgrenze aufhebt und das 25-fache des Plus-Kontingents liefert. Schwedding hält das für gerechtfertigt und nennt sich selbst als jemanden, der bereit wäre, diesen Betrag zu zahlen.

### Decisions API, Agents API und Agentic Computing

Die **Decisions API** ist eine neue Schnittstelle für Entwickler, die Agenten-Workflows bauen. Sie ermöglicht es Agenten, schneller und zuverlässiger Entscheidungen in komplexen Mehrstufenprozessen zu treffen — relevant zum Beispiel für Model-Routing (welches Modell löst welche Teilaufgabe?) oder für Echtzeit-Entscheidungen in autonomen Systemen. Die Demo auf der Bühne zeigte, wie der Mikro-Roboter **MicroDuck** (von Hugging Face) diese API nutzt — ein Signal, dass OpenAI-Modelle zunehmend für physische Roboter-Steuerung eingesetzt werden sollen.

### Der "Research Intern": Rekursive Selbstverbesserung

Ein für Fachleute bemerkenswerter Meilenstein: OpenAI erklärt, das Niveau des sogenannten **Research Intern** erreicht zu haben — ein Ziel, das beim letzten DevDay 2025 angekündigt worden war. Was das bedeutet: KI-Systeme bei OpenAI sind inzwischen an ihrer eigenen Weiterentwicklung beteiligt. Konkret nannte Schwedding Computer Use als Beispiel: Die OpenAI-Forscher schreiben den entsprechenden Code für die "Computer Use"-Funktion nicht mehr selbst, sondern nutzen KI, um diesen Code zu verbessern. Das Ergebnis: Computer Use läuft jetzt doppelt so schnell wie zuvor.

### Computer Use: Von 15 Minuten auf 8–16 Stunden

**Computer Use** bezeichnet die Fähigkeit, einem KI-Agenten Zugriff auf den gesamten Computer zu geben — Maus, Tastatur, Browser, alle Anwendungen. Seit Anfang des Jahres konnten OpenAI-Agenten damit eigenständig Aufgaben von bis zu 15 Minuten Länge erledigen. Nach den Verbesserungen durch die rekursive Selbstoptimierung sind es jetzt 8 bis 16 Stunden. Schwedding betont, dass OpenAI dabei auch explizit den Aspekt der Sicherheit hervorhebt: Computer Use sei jetzt signifikant sicherer als bei der Konkurrenz — eine direkte Spitze gegen Anthropic, das sich selbst regelmäßig als führend in Sachen KI-Sicherheit positioniert.

### Codex in der Cloud: Kein offener Laptop mehr nötig

**Codex**, OpenAIs KI-Tool für das Schreiben, Überprüfen und Debuggen von Code, kann ab sofort remote in der Cloud ausgeführt werden. Was das bedeutet: Bisher musste man den eigenen Computer laufen lassen, wenn man einen Codex-Agenten auf einem lokalen Entwicklungsprojekt arbeiten lassen wollte. Viele Nutzer haben ihren Laptop einfach geöffnet im Büro gelassen und ihn per Fernzugriff genutzt. Jetzt entfällt das: Die Agenten laufen in OpenAIs Cloud, 24/7 verfügbar, während man selbst weg ist. Zusätzlich gibt es einen neuen **Codex Security Cloud**-Dienst, der automatisch Sicherheitslücken in eigenem Code findet — und das kostenlos.

### Sign in with ChatGPT: KI-Authentifizierung für eigene Apps

Wer eine eigene App baut und darin KI-Funktionen anbieten will, musste bisher über die OpenAI-API und eigene API-Schlüssel gehen — mit eigenen Kosten, eigener Infrastruktur, ohne Zugang zu den Modell-Subventionen, von denen reguläre ChatGPT-Nutzer profitieren. Die neue Funktion **Sign in with ChatGPT** ändert das: Nutzer können sich mit ihrem bestehenden ChatGPT-Abo (auch dem kostenlosen Gratis-Plan) bei Drittanbieter-Apps anmelden und so die Rechenleistung ihres eigenen Abos einbringen. Schwedding demonstriert das an seiner eigenen Plattform "Relation Flow", einem Corporate Learning Management System.

Für Entwickler bedeutet das eine neue Möglichkeit, KI-Apps ohne eigene API-Kosten zu bauen — die Rechenkosten trägt der jeweilige Endnutzer über sein Abo.

### Plugin-Ökosystem und OpenAI Marketplace

OpenAI hat außerdem ein erweitertes Plugin-Ökosystem angekündigt, mit Partnerschaften u. a. mit **Adobe** und **Figma** — Tools, die direkt aus dem ChatGPT-Interface heraus bedient werden sollen. Dazu gibt es erstmals einen offiziellen **OpenAI Marketplace**, auf dem Entwickler eigene Apps und Agents veröffentlichen und vermarkten können — ein Konzept, das OpenAI seit 2023 immer wieder angekündigt, bisher aber nie wirklich umgesetzt hatte. Schwedding ist vorsichtig optimistisch und hofft, dass es diesmal mit der Umsetzung klappt.

### Private Intelligence und AWS-Partnerschaft

Für Unternehmen, die aus Datenschutzgründen keine externen Dienste nutzen wollen (insbesondere relevant für DACH, EU, und regulierte Branchen), hat OpenAI **Private Intelligence** angekündigt: Zero Data Retention bedeutet, dass keine Konversationsdaten auf OpenAI-Servern gespeichert werden, kombiniert mit Confidential Computing (verschlüsselte Verarbeitung). Dazu kommt eine Partnerschaft mit **AWS Bedrock**, die es ermöglicht, OpenAI-Modelle über die bestehende AWS-Infrastruktur der meisten Unternehmen zu nutzen.

---

## Robotik: Von San Francisco nach Deutschland

### Figure 2 Abschied mit Arnold Schwarzenegger

Wenige Tage vor dem DevDay veröffentlichte das amerikanische Robotik-Unternehmen **Figure** ein Video, das weltweit für Aufmerksamkeit sorgte: der Abschied vom Modell **Figure 2 (F.02)**. Das Unternehmen bat die Community um Vorschläge, wie der Roboter ausgemustert werden sollte, und **Arnold Schwarzenegger** — eine klare Anspielung auf den Film Terminator 2 — schlug vor, die Maschinen in einem Schmelzofen zu vernichten. Figure führte das wörtlich aus: Die F.02-Einheiten sprangen eigenständig in einen 75-Tonnen-Elektrolichtbogenofen, gefilmt von einem Team in Imatra, Finnland. Schwarzenegger selbst trat im Video auf und rief "Hasta la vista, Figure 2". Figure begründete die Maßnahme mit der wachsenden F.03-Flotte, die das Weiterentwickeln der alten Hardware unwirtschaftlich mache — und mit dem Schutz proprietärer Technologie.

Schwedding wertet das als Zeichen einer wachsenden Kluft: Während die großen amerikanischen Unternehmen beeindruckende Marketing-Demos produzieren, bleiben Besuche bei Firmen wie OneX (Roboter "Neo") und anderen US-Robotik-Startups für externe Besucher weitgehend abgeschlossen. Sein Eindruck: Wirklich transparente Einblicke in den tatsächlichen Stand der Technik gibt es derzeit am ehesten von chinesischen Anbietern.

### UBTECH-Roboter im DACH-Raum: Erstes Rollout in Deutschland

Das zweite große Robotik-Thema des Videos ist eine Vor-Ort-Reportage: Leonard Schwedding besuchte eine Veranstaltung des deutschen Unternehmens **TerraRobotics** (gegründet April 2025, CEO Murad Apaci), das seit Januar 2026 exklusiver Distributor für **UBTECH**-Roboter im DACH-Raum ist. UBTECH ist ein chinesischer Hersteller von Humanoid-Robotern; ihr Modell **Walker S2** läuft bereits seit März 2026 in einer Pilotphase bei Rossmanns Logistikzentrum in Burgwedel.

Die Veranstaltung zeigte verschiedene Roboter-Konzepte: Transportaufgaben (Kisten von A nach B — standardisierte KLT-Behälter in der Logistik), einen kleinen tanzenden Lernroboter ("Alpha Mini 2"), der spielerisch an Robotik heranführen soll (Konzept vergleichbar mit Lego Mindstorms), und den großen **Tienkung**-Humanoiden, der per VR-Brille und Teleoperations-Controllern gesteuert wurde. Interviewte Personen auf der Veranstaltung kamen aus Intralogistik-Hintergründen (Lagersysteme für Mercedes, Porsche, Intersport) und nannten als Hauptmotivation für den Einsatz von Robotern den Fachkräftemangel sowie die Übernahme von Aufgaben, die niemand machen möchte.

Schweddings Einordnung: China ist hier derzeit das einzige Land, das wirklich Transparenz über den Stand der Technik zeigt und tatsächlich liefert — mit echten Use-Cases in der Industrie, nicht nur Messedemonstratoren.

---

## Gemini 4 Argon: Vielversprechend, aber noch nicht für alle

Am 30. September 2026, einen Tag nach dem DevDay, hat Google DeepMind **Gemini 4 Argon** angekündigt. Das Modell richtet sich laut Google primär an Cybersicherheitsexperten und wird im Rahmen des "Fairwind"-Programms zunächst nur an registrierte Verteidigungspartner und staatliche Institutionen ausgerollt — eine breitere Verfügbarkeit ist angekündigt, aber ohne festes Datum.

Schwedding warnt vor zu schnellen Schlüssen aus den präsentierten Benchmarks: Modelle wie Gemini neigen seiner Einschätzung nach dazu, für Benchmarks optimiert ("bench-maxed") zu werden, ohne dass das direkt auf reale Alltagstauglichkeit schließen lässt. Bloomberg hat kurz nach der Ankündigung berichtet, dass Google-interne Quellen die Praxisleistung differenzierter einschätzen als die Benchmark-Tabellen. Für die breite Öffentlichkeit ist Gemini 4 Argon aktuell nicht zugänglich.

---

## Tavus und America.gov: Wenn KI unsichtbar wird

Zum Schluss des Videos greift Schwedding zwei Nebenthemen auf, die er als Zeichen eines tiefgreifenderen Wandels interpretiert:

**Tavus** ist laut Schwedding das erste KI-Modell, das den Turing-Test im Video-Bereich bestanden hat: Bei Videocalls mit einem KI-Avatar von Tavus konnten 48 Prozent der Gesprächspartner nicht erkennen, dass sie mit einem KI-Avatar und nicht mit einem Menschen sprachen. Die Implikation: Wenn man eine Marketingagentur beauftragt oder an einem Meeting teilnimmt, kann man heute nicht mehr sicher sein, ob am anderen Ende ein Mensch sitzt — oder ein KI-Agent.

Die **America.gov**-Website wurde mit einem KI-gestützten Chatbot neugestaltet, über den US-Bürger Behördengänge per Sprachinteraktion erledigen können — vergleichbar mit einem Apple-Demo in Ton und Qualität, laut Schwedding. Er zieht den Vergleich mit deutschen Behörden-Websites, lobt die amerikanische Umsetzung als vorbildlich für Bürokratieabbau und stellt fest, dass "Prompt Injections" (gezielte Angriffe auf KI-Chatbots durch manipulierte Eingaben) auch dort ein Thema sind.

Das übergeordnete Thema, das Schwedding in beiden Beispielen sieht: Nicht Modellnamen oder Benchmarks sind das entscheidende Feld der nächsten Jahre — sondern **Distribution** und **Marketing-Automatisierung**. Mit 1,2 Milliarden wöchentlichen Nutzern ist ChatGPT heute das mächtigste Vertriebsnetz in der Geschichte des Internets. Wer Zugang zu diesem Netzwerk bekommt (über Sign in with ChatGPT, den OpenAI Marketplace oder vergleichbare Mechanismen), gewinnt Reichweite auf eine Weise, die keine menschliche Marketing-Abteilung reproduzieren kann.

---

## Plausibilitätscheck

**OpenAI DevDay 2026 (29.09.2026) mit 20+ Ankündigungen:** Bestätigt durch OpenAIs eigene Recap-Seite (openai.com/index/devday-2026-recap/) sowie mehrere unabhängige Berichte. **Suchtreffer.**

**GPT-6.1 Sol: ein Fünftel des Preises von GPT-6 Astra:** Bestätigt durch andere Repo-Einträge und externe Quellen; konkret $2/$10 vs. $10/$50 pro Million Token. **Suchtreffer.**

**1,2 Milliarden wöchentliche Nutzer bei ChatGPT:** Die Zahl erscheint im Video und in einer früheren Stelle im Transkript als "wöchentlich". Tatsächlich sprach OpenAI im August 2026 selbst von "1 Milliarde wöchentliche Nutzer". Viele Quellen nennen 1,2 Milliarden als monatliche Schätzung (MAU), nicht wöchentlich. Die im Video genannte Zahl könnte eine gerundete oder geringfügig veraltete Angabe sein. **Einschränkung: die 1,2-Milliarden-Zahl ist plausibel als Monatsangabe, aber als Wochenzahl leicht übertrieben laut aktuellem Recherchestand.** Quellqualität: Suchtreffer.

**Figure 2-Ausmusterung mit Arnold Schwarzenegger, Oktober 2026:** Bestätigt durch Dexerto, Notebookcheck, Forbes Spanien und weitere Quellen; die Vernichtung in einem finnischen Schmelzofen und Schwarzeneggers Auftritt sind dokumentiert. **Suchtreffer.**

**UBTECH / TerraRobotics: exklusiver DACH-Distributor:** Bestätigt durch Gasgoo Autonews, Jiemian und Boerse Express; Walker S2 läuft in Rossmann-Logistikzentrum Burgwedel. Signing-Datum: April/Juli 2026. **Suchtreffer.**

**Gemini 4 Argon: eingeschränkter Zugang, nur für Regierungen und Cybersicherheitspartner:** Bestätigt; Rollout über "Fairwind"-Programm am 30.09.2026, keine Breitverfügbarkeit. Bloomberg-Berichte über intern skeptischere Einschätzung ebenfalls bestätigt. **Suchtreffer.**

**Tavus: 48 % können KI-Avatar nicht von Mensch unterscheiden:** Nicht durch externe Quellen überprüft. "Tavus" als Produktname konnte in dieser Suche nicht unabhängig verifiziert werden; die Zahl (48 %) wurde nicht in unabhängigen Berichten gefunden. **Nicht verifiziert.** Das Konzept (Turing-Test im Video-Sektor durch KI-Avatare) ist grundsätzlich technologisch plausibel, die konkrete Zahl und der Anbieter-Name sollten mit Vorsicht behandelt werden.

**Research Intern erreicht / rekursive Selbstverbesserung bei OpenAI:** Die Formulierung ist korrekt im Sinne des DevDay-Narrativs; OpenAI selbst kommunizierte diesen Meilenstein auf der Veranstaltung. Die genaue technische Bedeutung bleibt von außen schwer überprüfbar — "Research Intern" ist ein internes Benchmark-Level, keine extern validierte Kategorie. **Tool-Zusammenfassung.**

---

## Cross-Referenz zu bestehenden Notizen

**Direkte Überschneidung:** Gleiche Veranstaltung (OpenAI DevDay 2026) bereits abgedeckt in:
- [video-summary-jvaVkBXbqiI.md](video-summary-jvaVkBXbqiI.md) — Christoph Magnussen, Top 5; nennt GPT-6.1 Sol ebenfalls als zentrales Feature, auch Dots, Ultrafast, Sign in with ChatGPT. Komplementär, kein Widerspruch.
- [video-summary-A4lIdVtVBeg.md](video-summary-A4lIdVtVBeg.md) — Kris AI2ROI; technisch kompakter, mit Preis-Tabellen. Kein Widerspruch.

**Robotik-Kontext:** Humanoide Roboter in Deutschland als Thema taucht in mehreren Zusammenfassungen auf; direkte Überschneidung zu UBTECH-Walker-S2-Deployment nicht gefunden, aber Gesamtkontext der Humanoid-Robotik-Entwicklung ist gut etabliert im Repo.

**Claude Sonnet 5.5** wird im Video kurz erwähnt als teurer als das neue GPT-6.1 Sol, weshalb es sich weniger für Routine-Aufgaben eigne. Kein Widerspruch zu bestehenden Repo-Einträgen, die Claude Sonnet 5.5 als leistungsstärkstes, aber preisintensives Modell einordnen.

---

## Für Hardware-Entwickler und Team-Leads

**Decisions API und Agents API:** Wer Agenten-Workflows oder autonome Prozesse baut, bekommt mit der Decisions API jetzt eine dedizierte Schnittstelle für schnelle Entscheidungen in Multistep-Prozessen — relevant für Modell-Routing, Aktionsketten, Echtzeit-Steuerung (inkl. Roboter). Die Agents API bietet einen strukturierten Rahmen für langlebige Agenten, die über Stunden hinweg arbeiten.

**Codex Security Cloud (kostenlos):** Teams, die produktiven Code entwickeln, können diesen jetzt kostenfrei automatisch auf Sicherheitslücken prüfen lassen. Das ist für jedes Team relevant, das intern oder für Kunden Code ausliefert.

**Sign in with ChatGPT:** Für Teams, die interne KI-Tools oder Kundenapplikationen bauen, eröffnet dieses Feature eine neue Architektur: KI-Kosten werden auf den Endnutzer verlagert (der sein eigenes Abo mitbringt), statt zentral über eigene API-Schlüssel budgetiert zu werden. Das ändert Make-or-Buy-Kalkulationen grundlegend.

**Private Intelligence / Zero Data Retention:** Für Unternehmen in regulierten Branchen (Finanzdienstleistung, Gesundheit, öffentlicher Sektor) ist das der erste ernsthafte Schritt, OpenAI-Modelle ohne Datenschutz-Bedenken zu nutzen. Die AWS-Bedrock-Integration macht das mit vorhandener Infrastruktur kompatibel.

**UBTECH in Deutschland:** Teams, die Automatisierungsprojekte in Logistik, Fertigung oder Facility Management planen, haben jetzt einen deutschen Ansprechpartner (TerraRobotics) für Humanoid-Roboter des chinesischen Herstellers UBTECH. Das Walker-S2-Modell ist bereits in produktivem Einsatz (Rossmann Burgwedel). Das ist kein Labor-Projekt mehr.

**Tavus und KI-Avatare in Business-Meetings:** Teams, die Video-Calls für Kundengespräche, Bewerbungen oder externe Kooperationen nutzen, sollten die zunehmende Realitätsnähe von KI-Avataren kennen. Es ist heute technisch möglich, dass ein Gesprächspartner in einem Video-Call ein KI-Agent ist — das hat Implikationen für Prozesse, die auf persönlicher Identifikation beruhen.

---

## Begriffe

**Dots** — neue dauerhafte KI-Agenten in ChatGPT, die rund um die Uhr laufen und proaktiv Aufgaben übernehmen, ohne dass der Nutzer aktiv sein muss. Vergleichbar mit einem persönlichen Assistenten, der eigenständig handelt und sich mit allen genutzten Apps verbindet.

**Spaces** — kollaborative Arbeitsbereiche in ChatGPT, in denen Menschen und KI-Agenten gemeinsam an Dokumenten, Präsentationen und Apps arbeiten. Das Konzept ist vergleichbar mit Notion oder Google Docs, aber KI-Agenten können über Kommentare direkt Aufgaben erhalten.

**GPT-6 Astra** — OpenAIs bislang leistungsstärkstes Modell (Ankündigung September 2026). Preisklasse API: 10 Dollar Eingabe / 50 Dollar Ausgabe pro Million Token. Maßstab für alle Preisvergleiche im Video.

**GPT-6.1 Sol** — günstigeres Nachfolgemodell (gleiche Entwicklungsfamilie wie Astra); laut OpenAI nahezu vergleichbare Qualität für 2 Dollar Eingabe / 10 Dollar Ausgabe pro Million Token. Besonders attraktiv für Coding-Anwendungen und Massenabfragen über die API.

**Token** — die Recheneinheit, in der Sprachmodelle Text verarbeiten und abrechnen. Grob ein Wortstück (ca. 4 Zeichen). Bei KI-APIs zahlt man getrennt für Eingabe (was man eingibt) und Ausgabe (was das Modell zurückschreibt).

**Ultra Fast** — neuer Inferenz-Modus von OpenAI mit 300 Token pro Sekunde; laut OpenAI achtmal schneller als bisher, aber sechsmal so teuer. Für Anwendungen gedacht, bei denen Latenz entscheidend ist (z. B. Echtzeit-Steuerung, Sprachinterfaces).

**Computer Use** — Fähigkeit, einem KI-Agenten vollständigen Zugriff auf einen Computer zu geben (Maus, Tastatur, alle Anwendungen). OpenAI-Agenten können damit inzwischen eigenständig Aufgaben von bis zu 16 Stunden Länge erledigen.

**Decisions API** — neue OpenAI-Schnittstelle für Entwickler, die KI-Agenten schnelle Entscheidungen in komplexen mehrstufigen Prozessen ermöglicht — relevant für Modell-Routing, autonome Workflows und Robotersteuerung.

**Confidential Computing / Private Intelligence** — Methode, bei der die KI-Verarbeitung so verschlüsselt stattfindet, dass selbst der Anbieter (OpenAI) keinen Zugriff auf die verarbeiteten Daten hat. Für Unternehmen mit hohen Datenschutzanforderungen.

**Teleoperations** — Fernsteuerung eines Roboters durch einen menschlichen Operator in Echtzeit, meist über VR-Brille und Handcontroller. Der Roboter repliziert die Bewegungen des Operators. Dient heute als Methode zur Trainings-Datengenerierung für autonome Roboter-KI.

---

## Kernbotschaft

OpenAI hat beim Developer Day 2026 keine einzelne Killer-Funktion präsentiert, sondern eine konsistente Richtung: ChatGPT wird zur Infrastruktur. Dots machen die KI dauerhaft aktiv; Spaces integrieren sie in kollaborative Workflows; Sign in with ChatGPT macht sie zur Authentifizierungsplattform für Drittanbieter-Apps; der OpenAI Marketplace soll sie zum Distribution-Kanal machen. GPT-6.1 Sol senkt die Einstiegskosten für Entwickler drastisch, während Ultra Fast und Computer Use die Möglichkeiten für autonome, zeitintensive Aufgaben enorm erweitern. In Deutschland beginnt parallel dazu das erste echte Rollout chinesischer Humanoid-Roboter (UBTECH/TerraRobotics), und KI-Avatare sind jetzt gut genug, um in Video-Calls nicht mehr als KI erkannt zu werden. Der Host zieht daraus eine Schlussfolgerung, die er für die eigentliche Nachricht hält: Wer heute in der KI-Welt gewinnt, gewinnt nicht unbedingt auf der Ebene der Modelle — sondern auf der Ebene der Distribution.

## Themen-Tags

OpenAI DevDay 2026, Dots, GPT-6.1 Sol, GPT-6 Astra, Ultra Fast, Pro 500, Spaces, Agents API, Decisions API, Computer Use, Codex Cloud, Sign in with ChatGPT, OpenAI Marketplace, Private Intelligence, Confidential Computing, AWS Bedrock, Humanoid Roboter, UBTECH, TerraRobotics, Walker S2, Figure 2, Arnold Schwarzenegger, Gemini 4 Argon, Claude Sonnet 5.5, Tavus, America.gov, Leonard Schwedding, Everlast AI, KI-Agenten, Distribution, Marketing-Automatisierung

## Zu prüfen

- **GPT-6.1 Sol: Modellname in den Captions nicht sichtbar** — die automatischen YouTube-Captions schreiben durchgehend nur "GBT 6.1", ohne den Zusatz "Sol". Aus bestehenden Repo-Einträgen ([video-summary-A4lIdVtVBeg.md](video-summary-A4lIdVtVBeg.md)) und Plausibilitätschecks ist der vollständige Modellname "GPT-6.1 Sol" bekannt und wurde hier verwendet.
- **1,2 Milliarden wöchentliche Nutzer:** Laut Websuche sprach OpenAI im August 2026 von "1 Milliarde wöchentlich"; die 1,2-Milliarden-Zahl ist eher eine monatliche Schätzung. Das Video nennt beide Zahlen an verschiedenen Stellen. Die Präzision dieser Angabe ist gering — Quellqualität: Suchtreffer, mit Einschränkung.
- **Tavus (KI-Avatar, 48 %):** Name und Zahl konnten durch Websucheergebnisse in dieser Session nicht unabhängig verifiziert werden. Der Name könnte in den Captions falsch transkribiert sein. Diese Angabe sollte mit Vorsicht behandelt werden. Quellqualität: nicht abrufbar.
- **"Research Intern" als Meilenstein:** OpenAI kommuniziert das als interne Benchmark-Stufe ("AI Research Intern level"). Was das im Detail bedeutet und wie es überprüfbar wäre, ist von außen nicht vollständig nachvollziehbar. Suchtreffer für das DevDay-Narrativ, aber die technische Substanz ist opak.
- **MicroDuck (Hugging Face Roboter):** Die automatischen Captions schreiben "Micro Duck" und "MicroDuck"; der genaue Produktname des bei DevDay demonstrierten Hugging-Face-Roboters konnte in dieser Zusammenfassung nicht unabhängig verifiziert werden.
- **Gemini 4 Argon: "Benchmarks bench-maxed"** — Schweddings Einschätzung, dass Gemini zu Benchmark-Optimierung neigt, ist eine persönliche Meinung, die von Bloomberg-Berichten (interner Dissens bei Google über die Praxis-Performance) eine gewisse Stütze bekommt. Suchtreffer für Bloomberg-Bericht.

## Quellen der Plausibilitätschecks

- [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [aiidelist.com — 25 Biggest Announcements DevDay 2026](https://aiidelist.com/blog/openai-devday-2026-announcements)
- [rohitai.com — Every Announcement and What Builders Should Do Next](https://rohitai.com/blog/openai-devday-2026-announcements)
- [Dexerto — Arnold Schwarzenegger Terminates Figure 2 in Molten Steel](https://www.dexerto.com/entertainment/arnold-schwarzenegger-terminates-real-ai-robots-judgment-day-style-using-molten-steel-3414772/)
- [Notebookcheck — Figure 2 Abschied (Deutsch)](https://www.notebookcheck.com/Echtes-Video-Arnold-Schwarzenegger-laesst-Roboter-in-Schmelzofen-springen.1413317.0.html)
- [Gasgoo Autonews — UBTECH signs Partnership with Terra Robotics](https://autonews.gasgoo.com/articles/market-industry/ubtech-signs-partnership-with-terra-robotics-humanoid-robots-deployed-in-european-retail-logistics-scenarios-2046501821030326273)
- [Boerse Express — Ubtech: Terra Robotics wird DACH-Distributor](https://www.boerse-express.com/news/articles/ubtech-terra-robotics-wird-dach-distributor-898139)
- [Betanews — Gemini 4 Argon Cyber Defenders Fairwind](https://betanews.com/article/gemini-4-argon-cyber-defenders-fairwind/)
- [Google Blog — Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- [quashbugs.com — ChatGPT Statistics 2026](https://quashbugs.com/blog/chatgpt-statistics-users-revenue-downloads-and-usage)
