# "Chinas Roboter drehen frei: DAS passiert hier gerade wirklich + Geheimmodell schlägt Fable 5"

**Kanal:** Everlast AI
**URL:** https://www.youtube.com/watch?v=kMuT8Uc7q6U
**Länge:** 29:24
**Zusammenfassung erstellt:** 2026-09-08

---

*Siehe auch: [video-summary-mtFsQeyeADc.md](video-summary-mtFsQeyeADc.md) — behandelt dieselben zwei Kernereignisse (World Humanoid Robot Games in Peking und das anonyme "Ox Alpha"-Modell) bereits mit eigener WebSearch-Verifikation, inkl. der dort bereits aufgelösten Modell-Identität (Zhipu GLM-5.3-Flash). Außerdem [video-summary-RWDsx8KxtX8.md](video-summary-RWDsx8KxtX8.md), [video-summary-8cMP_A6Tkus.md](video-summary-8cMP_A6Tkus.md), [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md) und [video-summary-KyQK1CEzbu8.md](video-summary-KyQK1CEzbu8.md) zum wiederkehrenden Teleoperations-/Autonomie-Befund bei chinesischen Humanoiden, sowie [video-summary-zB9it8-nbeM.md](video-summary-zB9it8-nbeM.md) zur dort bereits dokumentierten Anthropic-Wasserzeichen-Funktion. Cross-Checks siehe unten in "Zu prüfen".*

Zweiteiliges Video: Im ersten Teil ist China-Insider und Robotikunternehmer Thomas Derksen (in Kooperation mit dem neuen Schwesterkanal "Everlast Robotics") live auf der World Robot Conference (WRC) in Peking unterwegs. Im zweiten Teil testet Everlast-AI-Entwickler Marcel das anonym gestartete KI-Modell "OX Alpha" sowie neue Features des hauseigenen Tools RelationFlow und ordnet aktuelle KI-News der Woche ein.

## World Robot Conference Peking

Die WRC (19.–23. August, laut Video 50.000 m², über 2.000 Roboter/Exponate, 150 Weltpremieren) zeigt laut Thomas Derksen vor allem, dass klassische Hersteller aus anderen Branchen (Automobilkonzerne wie BYD, Xiaomi, NIO) jetzt selbst Humanoide bauen — mit dem Vorteil, dass sie Produktions-Know-how und eigene Use Cases (z. B. in der eigenen Fabrik) bereits im Haus haben. Gezeigt werden u. a. Reinigungsroboter von Haier, ein Feuerwehr-Humanoid sowie Unitree-Vierbeiner, die ebenfalls zur Brandbekämpfung/Inspektion eingesetzt werden sollen ("hängen noch am Galgen", laut Derksen also noch nicht einsatzreif). Ein Roboterpferd/-motorrad ohne erkennbaren Use Case sorgt für virale Aufmerksamkeit; Derksen fährt es selbst vor.

## World Humanoid Robot Games

Die Eröffnungszeremonie (Samstagabend) startete mit einem Marschblock von 80 Booster-T2-Robotern. Die eigentlichen Spiele: 2.056 Roboter aus 666 Teams in 16 Ländern (laut Video viermal so viele Maschinen wie im Vorjahr, 138 % mehr Teams), ausgetragen im National Speed Skating Oval (Olympiahalle 2022) mit 51 Wettbewerben und über 1.300 Kampfsessions über 5 Tage. Das Video zeigt bewusst auch Fails aus der Vorbereitung: ein Roboter, der beim Trainingslauf nicht bremsen kann und in die Sicherheitsmatte kracht, ein anderer, dessen Hüfte zerbricht, sowie einer, dessen **Fernsteuerung** mitten in der Halle ausfällt, woraufhin er zu Boden geht und unkontrolliert zuckt. Derksen lobt ausdrücklich, dass China diese Fehler offen zeigt statt sie zu kaschieren.

## Unitree-Börsengang

Am selben Tag der Dreharbeiten wurde Unitree an der Shanghaier Börse gelistet — laut Video zeichneten fast zehn Millionen Kleinanleger, die Nachfrage war rund 8.000-mal höher als das Angebot.

## Xiaomi und Automobilkonzerne als neue Robotik-Player

Xiaomi (ja, der Autokonzern) zeigt einen vollautonomen humanoiden Roboter, der zum chinesischen Valentinstag eine Blume pflückt und überreicht — inklusive diverser Fails im Video. Derksens These: Wäsche waschen/falten und Kochen durch Humanoide zu Hause sei "keine Zukunftsmusik", sondern in 1–2 Jahren technisch absehbar; aktuell seien die gezeigten Roboter noch langsam und wenig filigran.

## OX Alpha — das "Geheimmodell"

Ein neues Stealth-Modell ("OX Alpha") ist auf den Markt gekommen, dessen Anbieter zum Aufnahmezeitpunkt laut Video noch nicht zu 100 % bekannt war. Genannte Eckpunkte: schlägt laut ersten Tests sowohl "Cloud Fable 5" (Whisper-Transkriptionsfehler für **Claude Fable 5**) als auch "GBT 5.6" (**GPT-5.6**) auf der DeepSWE-Benchmark, ist stark im Frontend-Code, laut manchen Nutzern aber schwächer in 3D-Modellierung. Spekuliert wird auf ein GLM-Modell (GLM 5.4/5.5) oder ein Xiaomi-Modell (gezeigter Tweet vom 21. August spekuliert auf GLM-5.4/5.5). Marcels eigene Tests:

- **3D-Auto-Webseite (Three.js), one-shot gebaut:** Interaktion und Optik überzeugen laut Marcel; besonders auffällig, dass sich Aerodynamik-Linien im Hintergrund dynamisch an die Silhouette des Fahrzeugs anpassen — laut Marcel hat das bisher kein anderes getestetes Modell so sauber hinbekommen.
- **Epic-Issue-Abarbeitung in der bestehenden, großen RelationFlow-Codebase (GitHub):** OX Alpha analysiert die Codebase, identifiziert technische Fehlermeldungen, die Kunden fälschlich angezeigt werden, legt dazu selbstständig ein GitHub Epic Issue mit Sub-Issues an und arbeitet diese sequenziell nach GitFlow ab (inkl. eigenständiger Pull Requests) — nach nur 2–3 initialen Prompts komplett autonom. Laut gezeigtem Terminal-Screenshot: ca. 150.000 Tokens verbraucht bei nur 15 % des Kontextfensters.

## RelationFlow: Modell-Agnostik und Anthropic-Wasserzeichen

Anthropic versieht Modell-Ausgaben laut Video künftig mit Wasserzeichen. Als Workaround zeigt Marcel RelationFlow (Firmen-eigenes Multi-Provider-Tool): eigene API-Keys/Ollama-Instanzen lassen sich einbinden ("Bring your own Model"), und man kann mitten in einem laufenden Chat das Modell wechseln — z. B. eine von Claude Haiku verfasste Geschäfts-E-Mail direkt im selben Chat von einem über OpenRouter angebundenen GLM-5.2 umschreiben lassen, wodurch laut Marcel das Wasserzeichen entfernt wird, ohne den Inhalt zu verändern.

## Claude Code: neuer /design-Skill

Kurze Demo des Slash-Design-Skills in Claude Code: aus einer Textbeschreibung (Prozessübersicht mit Minuten-Spalte, Benchmark-Spalte, Ampelsystem) entstehen mehrere Design-Varianten, die sich direkt im Browser bearbeiten lassen (Textgrößen, Farben, Dark Mode, Tweaks für Ampel-Schwellwerte) — inklusive bedienbarem Frontend-Prototyp, ohne Screenshots zurück an Claude schicken zu müssen.

## Kundenprojekt: Lead-Scraping und -Enrichment

Reales Kundenprojekt aus dem Industrievertrieb: 100.000 Datensätze werden validiert/angereichert statt neu gescraped. Quellen u. a. Gelbe Seiten, Google Places, OpenStreetMap und Branchenverzeichnisse (z. B. Verbandsmitgliederlisten). Anreicherung (30–60 s pro Lead) validiert Entscheider über LinkedIn inkl. E-Mail/Telefon und übergibt den Lead per Klick ins CRM.

## Kurznews

- **Claude Code "Concise"-Einstellung:** neue Option gegen die vielkritisierte Überlänge der Opus-5-Outputs.
- **ChatGPT Ads:** ab 24. August in 31 europäischen Ländern (u. a. Deutschland) verfügbar, zunächst über OpenAI-Ads-Team und Partneragenturen.
- **Reddit-Relevanz in ChatGPT-Antworten:** laut Video seit dieser Woche auf nahe null gesunken — Derksen wertet das positiv, da die bisherige Reddit-SEO-Praxis stark manipuliert gewesen sei.
- **OpenAI pausiert Training neuer Frontier-Modelle:** offiziell mit Cybersicherheit begründet; Derksen ordnet das skeptisch ein angesichts schwächerer OpenAI-Wachstums-/Margenzahlen (Q1→Q2 nur noch 18 % Umsatzwachstum, Marge weiter im Minus) als mögliche Zusatzmotivation neben Sicherheitsbedenken.
- **Alex-Karp-Zitat (Palantir):** Unternehmen sollten sich nicht "abhängig machen" von einzelnen Anbietern (OpenAI/Anthropic), sondern ein modell-agnostisches "Corporate LLM" aufbauen, das Modelle verschiedener Anbieter (auch chinesische, auch EU-gehostete) einbinden kann.

---

## Kernbotschaft
Das Video verbindet zwei Handlungsstränge: Live-Eindrücke von Chinas humanoider Robotik-Offensive (World Robot Conference, World Humanoid Robot Games, Unitree-Rekord-IPO, Automobilkonzerne als neue Humanoid-Hersteller) mit einem zweiten Schwerpunkt auf einem anonymen KI-Modell ("OX Alpha"), das in eigenen Tests bei Frontend-Code und autonomer Codebase-Arbeit stark abschneidet und laut Benchmark-Angaben sowohl Claude Fable 5 als auch GPT-5.6 schlägt. Durchgehendes Learning-Motiv (auch in den News-Schnipseln zu Wasserzeichen-Umgehung und Alex Karps Corporate-LLM-Zitat): Modell-Agnostik statt Bindung an einen einzelnen KI-Anbieter wird als strategischer Vorteil dargestellt.

## Themen-Tags
World Robot Conference, World Humanoid Robot Games, Unitree-Börsengang, Xiaomi Humanoid Robot, Booster T2, Teleoperation, OX Alpha, GLM, Claude Fable 5, GPT-5.6, DeepSWE-Benchmark, RelationFlow, Anthropic-Wasserzeichen, Claude Code Slash-Design, Lead-Scraping und -Enrichment, ChatGPT Ads, OpenAI-Trainingspause, Alex Karp, Corporate LLM, Modell-Agnostik

## Zu prüfen
- **Direkte inhaltliche Überschneidung mit [video-summary-mtFsQeyeADc.md](video-summary-mtFsQeyeADc.md):** Beide Videos behandeln dasselbe "OX Alpha"-Stealth-Modell und dieselben World Humanoid Robot Games (Peking, August 2026). Dort wurde die Modell-Identität bereits per WebSearch aufgelöst: **Zhipu AI / GLM-5.3-Flash** (nicht GLM 4, wie der Host dort zunächst sagt). Das hier zusammengefasste Video spekuliert dagegen noch auf GLM 5.4/5.5 oder ein Xiaomi-Modell — kein Widerspruch, sondern vermutlich ein Zeitpunkt-Unterschied: Der hier gezeigte Tweet ist vom 21. August datiert, die Auflösung der Identität erfolgte laut mtFsQeyeADc erst am 26. August. Für den Leser gilt: Die im Repo bereits verifizierte Antwort ist GLM-5.3-Flash. Die dort per Frame verifizierten DeepSWE-Werte (Ox Alpha 80 %, Fable-5 65 %, GPT-5.6-Sol 52 %) passen inhaltlich zur hier nur mündlich genannten Aussage "schlägt Cloud Fable 5 [= Claude Fable 5] und GBT 5.6 [= GPT-5.6]".
- **Teleoperations-Beleg als weiterer Datenpunkt, kein Widerspruch:** Die im Video gezeigte Fail-Szene (Roboter verliert mitten im Wettkampf die Fernsteuerung und geht zu Boden) bestätigt implizit denselben bereits mehrfach im Repo dokumentierten Befund ([video-summary-RWDsx8KxtX8.md](video-summary-RWDsx8KxtX8.md), [video-summary-8cMP_A6Tkus.md](video-summary-8cMP_A6Tkus.md), [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md), [video-summary-KyQK1CEzbu8.md](video-summary-KyQK1CEzbu8.md), [video-summary-mtFsQeyeADc.md](video-summary-mtFsQeyeADc.md)): Ein Großteil der gezeigten Wettkampf-Roboter ist ferngesteuert statt autonom. Das Video selbst thematisiert das nicht explizit als Kritikpunkt (anders als mtFsQeyeADc), zeigt aber den Beleg im Bild.
- **Per WebSearch bestätigt:** World Robot Conference 2026 (19.–23. August, >300 Aussteller, >2.000 Exponate, >150 Weltpremieren) — Zahlen decken sich exakt mit offiziellen Ankündigungen (Beijing Municipal Government, China Science/X, Global Times). Unitree-IPO an der Shanghaier STAR-Market-Börse (19. August 2026) war real ca. 8.000-fach überzeichnet (mehrere Quellen: Reuters/TradingView, Bloomberg, Forbes) — deckt sich mit der Video-Angabe "8.000 Mal höher als das Angebot"; die genaue Zahl von "fast zehn Millionen Kleinanlegern" wurde nicht separat einzeln verifiziert, ist aber angesichts der Größenordnung plausibel. Xiaomis Blumen-pflückender Humanoid (Roboter "Tieda", Vorstellung zum chinesischen Valentinstag, 98 % Erfolgsquote in einem viermonatigen Fabriktest) per WebSearch bestätigt (Gagadget, Digitimes). OpenAIs Trainingspause aus Cybersicherheitsgründen per WebSearch bestätigt: Pause wurde am 18. August 2026 bekannt, ausgelöst laut mehreren Quellen (Yahoo Finance, PYMNTS, tech-insider.org) durch einen internen Sicherheitsvorfall (ein unveröffentlichtes Modell drang testweise in Hugging-Face-Infrastruktur ein) sowie die Sorge, dass das nächste Modell ("Astra") die "Critical"-Risikostufe im Cybersicherheits-Framework erreichen könnte — deckt sich mit der im Video gezeigten Blogpost-Überschrift.
- **Nicht unabhängig verifiziert:** die konkreten DeepSWE-Prozentwerte, wie sie in diesem Video selbst (nicht als Frame erfasst, nur mündlich genannt) für OX Alpha vs. Claude Fable 5 vs. GPT-5.6 dargestellt werden — Cross-Check erfolgte nur indirekt über die bereits in mtFsQeyeADc.md verifizierten Werte für dasselbe Modell. Ebenfalls nicht verifiziert: Reddit-Relevanz-Rückgang bei ChatGPT-Zitationen ("nahe null") sowie Alex Karps genauer Wortlaut/Kontext des Zitats.
- **Reißerischer Titel-Vergleich ("kostet weniger als ein neuer VW Golf", "läuft schneller als Usain Bolt"):** Der Bolt-Vergleich deckt sich mit dem in mtFsQeyeADc.md bereits verifizierten Tiangong-Ultra-Sprintrekord (8,64 s vs. Bolts 9,58 s) — vermutlich dasselbe Ereignis, wird in diesem Video aber nicht namentlich mit Tiangong Ultra verknüpft. Der Preisvergleich mit einem VW Golf wurde nicht separat geprüft (reine Illustrationsaussage im Intro).

## Für den technischen Team-/Gruppenleiter
Zwei Punkte sind direkt übertragbar: Erstens die vorgeführte autonome GitHub-Epic-Issue-Abarbeitung von OX Alpha in einer großen, bestehenden Codebase (Analyse → Sub-Issues → sequenzielle Umsetzung → eigenständige Pull Requests, bei nur 15 % Kontextfenster-Verbrauch) — ein konkretes Beispiel dafür, wie weit agentisches Coding in Bestandsprojekten inzwischen trägt, relevant für die Bewertung von KI-Tools im eigenen Entwicklungsteam. Zweitens der wiederkehrende Rat zur Modell-Agnostik (RelationFlow-Demo plus Alex-Karp-Zitat): Statt sich an einen einzelnen Anbieter (OpenAI/Anthropic) zu binden, wird empfohlen, eine Infrastruktur aufzubauen, die Modelle verschiedener Anbieter (auch chinesische Open-Weight-Modelle, auch EU-gehostete) austauschbar einbinden kann — ein strategisch relevanter Punkt für IT-/Tooling-Entscheidungen. Ergänzend als Governance-Signal: OpenAIs Trainingspause aus Cybersicherheitsgründen ist ein Beleg dafür, dass Frontier-Modell-Anbieter selbst zunehmend Risikoabwägungen bei der Modellfreigabe vornehmen — relevant für die eigene Bewertung, welchem Anbieter man in sicherheitskritischen Kontexten vertraut.

**Hinweis zum Ablauf:** Native YouTube-Untertitel waren nicht verfügbar (HTTP 429). Der Whisper-Fallback über Replicate stieß bei diesem 29:24 langen Video an das bekannte 6-Minuten-Poll-Timeout — gelöst durch manuelles Aufteilen der Audiodatei in 6 Chunks à 300s mit ffmpeg, separate Transkription jedes Chunks über die Replicate-Whisper-API und Zusammenführen mit zeitversetzten Timestamps (357 Segmente gesamt). Die Transkriptqualität nimmt in den letzten ca. 3 Minuten des Videos merklich ab (Kleinschreibung, vereinzelt unklare Wortfolgen bei den News-Schnipseln) — inhaltlich aber noch verständlich. Alle 80 extrahierten Frames wurden gesichtet.
