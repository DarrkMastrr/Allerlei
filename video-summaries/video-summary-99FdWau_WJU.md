# "Was ist los bei GOOGLE? Gemini, Agents und die große KI-Wette"

**Kanal:** Christoph Magnussen
**URL:** https://www.youtube.com/watch?v=99FdWau_WJU
**Länge:** 15:07
**Zusammenfassung erstellt:** 2026-09-08

---

*Siehe auch: [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) (selber Kanal, breiterer KI-Markt-Überblick vom 08.08.2026 mit eigenem Gemini-Abschnitt), [video-summary-v23C9Z9nr8Y.md](video-summary-v23C9Z9nr8Y.md) und [video-summary-8hBXDntBQaQ.md](video-summary-8hBXDntBQaQ.md) (weitere Magnussen-Videos im Repo) sowie [video-summary-mtFsQeyeADc.md](video-summary-mtFsQeyeADc.md) (anderer Kanal, klare thematische Überschneidung zu Hassabis-Abgang und Alphabet-Aktienkurs — siehe "Zu prüfen"). Dieses Video ist ein fokussierter Deep-Dive speziell zu "Was ist bei Google los", nicht nur ein weiterer Markt-Überblick.*

## Format

Talking-Head-Video (Christoph Magnussen, Büro-/Loft-Setting mit Glaswänden und Pflanzen, gleiches Sprecher-Setup wie in anderen Repo-Videos desselben Kanals), durchgehend deutschsprachig, ohne Screen-Recording-Demo. Bebildert mit zahlreichen eingeblendeten Screenshots realer Presseartikel und Produkt-UIs (u. a. ComputerBase, BBC, Wirtschaftswoche, TIME, t3n, tagesschau, sowie Google-Produktoberflächen wie Notebook LM, ein Codex-Fenster und ein Gemini-Chat-Fenster). Ab ca. 08:47 ein kurzer, klar als "Werbung" markierter Eigenwerbeblock (nicht Drittanbieter-Sponsoring) für die hauseigene Blackboat AI Summer School/Academy, danach zurück zum inhaltlichen Teil.

## These: Ist Google auf dem absteigenden Ast?

Aufhänger: kaum noch klassisches "Googeln" (Klick auf Suchergebnis-Link) statt KI-Zusammenfassung/Chatbot, mehrere prominente Abgänge von Top-Researchern, das lang erwartete Gemini 3.5 Pro "kommt nicht", und die Frage "wo sind die Agents?". Magnussens Rahmenthese vorab: Die Antwort ist komplexer als ein einfaches Ja/Nein.

## Teil 1 — Die Menschen: prominente Abgänge

Google war laut Magnussen historisch die KI-Firma schlechthin (Transformer-Paper "Attention Is All You Need", größtenteils von Google-Autoren), verpasste dann aber den Produktanschluss (Bard vs. frühes ChatGPT), bevor in den letzten Monaten ein spürbarer Schub kam (Notebook LM, bessere/schnellere Modelle). Jetzt aber mehrere auffällige Abgänge, im Video benannt (Namen im Whisper-Transkript teils verhört — korrigiert, siehe "Zu prüfen"):

- **Noam Shazeer** (im Transkript als "im Chaisier" verschriftet) — Mitautor des Attention-Papers, war Gemini-Co-Lead/VP Engineering bei Google, wechselte im Juni 2026 zu OpenAI für Architekturforschung.
- **John Jumper** (Nobelpreis für AlphaFold) — im Transkript als "jetzt Bayern Tropic" verschriftet, gemeint ist: jetzt bei **Anthropic**.
- **Jeff Dean** — der prominenteste Abgang, 27 Jahre bei Google, an praktisch allen zentralen Produkten beteiligt (Suche, Maps u. a.), ging mit einem ganzen Team, um eine eigene Firma zu gründen (im Video "Discovery Group" genannt, korrekt: **Discovery Loop**).
- **Demis Hassabis** — laut Magnussen jetzt "eher Chairman" innerhalb von DeepMind statt CEO.

**Zwei Erklärungen für die Wechselwelle laut Magnussen:** (1) Ein Unternehmen mit so viel "Legacy" wie Google trägt automatisch Unternehmenskultur mit sich, die Vorsicht statt freiem Forschen erzwingt — Vergleich mit Nokia gegen Apple ("Innovator's Dilemma"). (2) Manche Top-Forscher (Beispiel im Video: Gäste aus Magnussens eigenem "AI to the DNA"-Podcast wie Richard Socher) glauben, dass klassische Business-Probleme bald relativ trivial gelöst sind, und wollen sich stattdessen großen Problemen (Medizin, Energie) widmen — über Modelle, die andere Modelle verbessern ("Loop"-Gedanke, im Kleinen vergleichbar mit Agent-Heartbeat-Mechanismen wie bei OpenClaw oder dem Gedächtnis-Aufbau bei Hermes Agent).

## Teil 2 — Die Produkte: fragmentierte Experience

Kernkritik: "Welches Gemini?" — eingebaut, in der Suche, in Notebook LM — Produktstrategie ist bei einer derart gewachsenen Legacy nicht trivial. Google hat laut Magnussen nicht Microsofts Extremproblem ("acht Knöpfe für dieselbe Funktion"), kann aber auch nicht auf der grünen Wiese wie ein ChatGPT starten. Offen als eigener Bias benannt: Magnussen bevorzugt aktuell Codex/ChatGPT als App, weil sie Agents gut einbindet; Googles Agent-Harnesses im Terminal seien "buggy", Tool-Use innerhalb der Modelle nicht so griffig wie bei Claude Code/Codex. Google Antigravity wird eher als IDE-Ansatz (Integrated Development Environment) eingeordnet, nicht als zentrales Arbeits-Interface für Agents — bewusst kritisch formuliert, mit explizitem Appell an mitschauende Google-Mitarbeitende ("wir müssen daran"). Am besten funktioniere aus seiner Sicht aktuell **Notebook LM** (komplexes RAG einfach übersetzt). Die Google-Suche selbst wird als über 25 Jahre gewachsenes, weiterhin erfolgreichstes Internetprodukt gewürdigt — Magnussen nutzt selbst regelmäßig die KI-Zusammenfassung in der Suche, weil er "Google vertraut", und wechselt nur zu ChatGPT, wenn er eine andere Antwortquelle für wahrscheinlicher hält.

**Google Spark:** vorgestellt als Hintergrund-Agent, der Aufgaben eigenständig erledigt — laut eingeblendetem Screenshot zum Zeitpunkt der Aufnahme nur für **Google-AI-Ultra-Abonnenten in den USA** verfügbar, nicht in Europa. Magnussens Einschätzung: Google hat enorm viel Datenzugriff (Mail, YouTube-Verlauf, freigegebene Dokumente — explizit **nicht** Workspace/Enterprise-Daten), aber ob ein solcher Agent funktioniert, hängt an Tool-Use-Qualität des Modells und sauberer Kontextaufbereitung — beides laut ihm keine triviale Aufgabe (eigene Erfahrung aus der täglichen Arbeit bei Blackboat: Datenbereinigung, Zugriffsrechte pro Agent). Fazit: "verhalten optimistisch".

## Teil 3 — Geschäftsmodell, Marktanteile und die große Wette

Sorge um Googles Werbegeschäft: Klicks auf Anzeigen sinken, wenn Nutzer stattdessen Chatbot-Antworten übernehmen. Laut im Video genannten Zahlen bleibt ChatGPT Marktführer bei Chatbots, ist aber unter 50 % Marktanteil gerutscht (~40 %); Google hat mit 20–30 % (nahe 30 %) stark aufgeholt, Claude liegt bei 15–20 %. Wichtiger Nebeneffekt laut Magnussen: Ein "Normalisierungseffekt" (einmal an Chatbot-Nutzung gewöhnt, bleibt man dabei) verschiebt Nutzungsgewohnheiten weg von der klassischen Google-Suche, ohne dass das Google "umhaut".

Zur Sorge um Googles (laut Video) "Börsengang"/Aktienkurs: Magnussen widerspricht der These vom Abstieg — das Geschäftsmodell (AdSense, AdWords, YouTube) sei "eines der genialsten im Internet" und stärker denn je; die Personalwechsel seien eine branchenweite Dynamik (Vergleich mit Spielertransfers im Profifußball, auch bei Meta, xAI, OpenAI, Anthropic). Google habe zudem gerade zusätzliches Kapital für Rechenzentren freigemacht — im Video genannt: **fast 200 Milliarden US-Dollar für ein Jahr**, committed für Hardware; ein Großteil der bestehenden Cloud-Infrastruktur sei bereits ausgelastet. Magnussens persönliches Bauchgefühl (eigene KI-/Agent-Nutzung radikal gestiegen) stützt seine Einschätzung, dass die Wette eher aufgehen als ein strategischer Fehler sein wird.

**Vollständig integrierter Stack:** Google sei der einzige Player, der die komplette "Cloud-Ära" von oben nach unten selbst bedient — Top-Consumer-Produkt (Suche, Gmail, Drive), starkes Firmenkundengeschäft (Google Workspace, laut Magnussen "Top-Top-Top-Produkt" gerade für schnell wachsende Firmen — explizit auch als Aussage eines gleichzeitigen Google- **und** Microsoft-Partners eingeordnet), darunter die Cloud-Layer (GCP) und ganz unten die eigene TPU-Chip-Produktion, optimiert für KI und Suche. Kein anderer Anbieter integriere das so durchgängig.

**Warum Google kein neues eigenes Spitzenmodell herausbringt:** Magnussens Deutung — das Modell ist schlicht (noch) nicht gut genug, und Google mache bewusst kein Marketing um ein unfertiges Produkt (anders als von ihm kritisierte Fälle bei Anthropic). Er begrüßt diese Zurückhaltung, wünscht sich aber mehr Transparenz über die Gründe. Solche "Innovator's Dilemma"-Lücken seien gleichzeitig Chancen für andere Firmen und Einzelpersonen.

## Für den Hardware-Entwickler/Team-Lead

Dieses Video ist eher ein strategischer Marktüberblick als eine praktische Anleitung — direkt übertragbar sind vor allem zwei Punkte: (1) die beiläufig erwähnte, aber praxisrelevante Einschätzung, dass gutes **Agent-Design an sauberer Kontextaufbereitung und klaren Zugriffsrechten pro Agent hängt** ("welche Agenten dürfen worauf zugreifen") — deckt sich mit der bereits im Repo dokumentierten Anatomie eines Agenten-Auftrags in [video-summary-JAszmnL5fyk.md](video-summary-JAszmnL5fyk.md) (Ziel/Grenzen/Format/Notfall); (2) die Region-Einschränkung von Google Spark (aktuell nur USA/Google AI Ultra) ist relevant, falls das Team Googles native Agent-Angebote für den deutschen/europäischen Einsatz evaluieren will — im Video selbst nicht als Einschränkung benannt, nur im eingeblendeten Screenshot sichtbar. Die Google-Workspace-Einschätzung (Top-Infrastruktur für wachsende Firmen, auch aus Sicht eines gleichzeitigen MS-Partners) kann als Datenpunkt für eine interne Tool-Entscheidung dienen, falls Workspace vs. Microsoft 365 zur Debatte steht.

---

## Plausibilitätscheck (per WebSearch, 2026-09-08)

- **Noam Shazeer bestätigt:** VP Engineering/Gemini-Co-Lead bei Google DeepMind, Mitautor des Transformer-Papers, wechselte im Juni 2026 zu OpenAI zur Leitung der Architekturforschung. Deckt sich mit der im Video beschriebenen (aber verhörten) Person.
- **John Jumper bestätigt:** AlphaFold-Nobelpreisträger, verließ DeepMind im Juni 2026 — Ziel ist **Anthropic**, nicht wie im Video missverständlich klingend eine neue eigene Firma.
- **Jeff Dean bestätigt:** 27 Jahre bei Google, letzter Arbeitstag 6. August 2026, Mitgründer von **Discovery Loop** (im Video "Discovery Group" genannt) zusammen mit Sanjay Ghemawat, Oriol Vinyals und Quoc Le; Google ist Gründungsinvestor. Ziel: KI zur Automatisierung wissenschaftlicher/technischer Forschung, später auch Hardware-Design, Medikamentenentwicklung, Energie.
- **Demis Hassabis bestätigt:** trat als CEO von Google DeepMind zurück, wurde Chairman von DeepMind **und** Chief Scientist bei Alphabet; Koray Kavukcuoglu übernimmt das Tagesgeschäft als SVP mit Berichtslinie an Sundar Pichai. Grund laut mehreren Quellen (Fortune, TIME, Axios): wiederholte Verzögerungen bei Gemini-Modellen, niedrige Moral, Talentabwanderung.
- **Alphabet-Investitionsvolumen bestätigt:** Aktuelle Capex-Guidance für 2026 liegt bei rund 200 Mrd. US-Dollar (teils sogar 205 Mrd. genannt) für Rechenzentren, Server, Chips — deckt sich mit der im Video genannten Zahl.
- **Gemini 3.5 Pro real verzögert, aber "kommt nie" ist Magnussens eigene Zuspitzung:** Mehrfach bestätigte Verzögerungen (mindestens drei Verschiebungen seit Juni 2026), Hauptgrund laut Bloomberg/9to5google Coding-Performance-Probleme sowie Zuverlässigkeits-/Halluzinationsprobleme. Ein Google-Statement, das Modell werde **nie** erscheinen, ist per Suche nicht belegt — im Video ist das erkennbar Magnussens zugespitzte eigene Formulierung, nicht ein zitiertes Google-Statement.
- **Marktanteile im Kern bestätigt, Claude-Zahl im Video etwas zu hoch:** App-Marktanteil Mai 2026 laut Sensor Tower: ChatGPT 46,4 % (erstmals unter 50 %), Google Gemini 27,7 %, Anthropic Claude 10,3 %. Die im Video genannte Spanne "15–20 % für Claude" liegt spürbar über den recherchierten ca. 10 %; Google-Zahl ("20 bis fast 30 %") und ChatGPT-Zahl ("Richtung 40 %, unter 50 %") passen dagegen gut zu den Zahlen.

## Kernbotschaft

Magnussens Antwort auf die Ausgangsfrage ist ein differenziertes "Nein, aber": Googles Geschäftsmodell (Werbung, Cloud, TPU-eigene Chips) ist so stark integriert wie bei keinem anderen Player und wird durch die aktuelle Investitionswelle (~200 Mrd. $/Jahr) eher gestärkt als geschwächt — die Personalabgänge (Shazeer, Jumper, Dean, Hassabis' Rollenwechsel) sind real und durch Legacy-Kultur sowie unterschiedliche Forschungsprioritäten erklärbar, aber Teil einer branchenweiten Wechseldynamik, keine Google-spezifische Krise. Die eigentliche berechtigte Kritik liegt bei den **Produkten**: eine fragmentierte, teils "buggy" Agent-Experience, die hinter Codex/Claude Code zurückbleibt, obwohl Google mit Notebook LM, Suche und der Datentiefe eigentlich die besten Voraussetzungen hätte.

## Themen-Tags

Google, Gemini, Google DeepMind, Demis Hassabis, Jeff Dean, Discovery Loop, Noam Shazeer, John Jumper, Anthropic, OpenAI, Google Spark, Google Antigravity, Notebook LM, Google Workspace, TPU, Alphabet-Investitionen, KI-Chatbot-Marktanteile, Innovator's Dilemma, Blackboat

## Zu prüfen

- **Whisper-Verhörer korrigiert (siehe Plausibilitätscheck):** "im Chaisier" → Noam Shazeer; "Bayern Tropic" → (bei) Anthropic; "Discovery Group" → Discovery Loop; "Messer Sabis" → Demis Hassabis. Alle in dieser Zusammenfassung mit den korrekten Namen wiedergegeben.
- **"Gemini 3.5 Pro kommt nie"** ist erkennbar Magnussens eigene zugespitzte Formulierung/Prognose, keine bestätigte Google-Aussage — die realen, mehrfachen Verzögerungen sind aber gut belegt (siehe Plausibilitätscheck).
- **Claude-Marktanteil im Video ("15–20 %") liegt über dem recherchierten Wert (~10,3 %, Mai 2026)** — möglicherweise andere Messmethode/Zeitpunkt oder ungenaue Angabe im Video; nicht weiter aufklärbar aus dem Transkript allein.
- **"Börsengang runter" im Transkript** — Google ist seit 2004 börsennotiert, ein neuer "Börsengang" 2026 ist nicht plausibel; gemeint ist erkennbar der gefallene Aktienkurs/Börsenwert, nicht ein IPO-Ereignis. Möglicherweise Sprech-Ungenauigkeit des Sprechers oder ein Whisper-Artefakt.
- **Cross-Check mit bestehenden Notizen — Ergänzung, teils andere Nuancen, kein echter Widerspruch:** [video-summary-mtFsQeyeADc.md](video-summary-mtFsQeyeADc.md) (anderer Kanal, 08.09.2026 zusammengefasst) behandelt denselben Themenkomplex mit zusätzlichen, hier nicht genannten Details: Alphabet-Aktie ist seit ihrem Allzeithoch am 13. Mai 2026 um 15 % (692 Mrd. $) gefallen; DeepMind hatte 2023 noch 12 Neueinstellungen pro Abgang, aktuell nur noch 2 (Anthropic: 22 pro Abgang) — ein konkreter Beleg für die in diesem Video nur allgemein beschriebene "Legacy/Kultur"-These. Kleine Nuance: Jenes Video beschreibt Hassabis knapper als "nicht mehr CEO, nur noch im Alphabet-Board", während per WebSearch die präzisere Rolle **Chairman von DeepMind + Chief Scientist Alphabet** ist (deckt sich mit der Formulierung in diesem Video, "eher Chairman"). [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) (selber Kanal, früherer Überblick) beschreibt Gemini aus Nutzerperspektive (Workspace-Integration, "weniger Personality", Modellnamen "3.5 Flash"/"3.1 Pro") — ergänzt dieses Video um die Produktsicht, ohne es zu widersprechen.
- **Nicht separat verifiziert:** Die genaue Aussage, dass Google bei Werkspace-Daten "nicht reinguckt" (Datenschutz-Zusicherung), stammt allein aus Magnussens eigener Aussage im Video, nicht aus einer externen Quelle.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429 (Rate-Limit), der Whisper-Fallback (Replicate) lief erfolgreich durch (275 Segmente). Alle 80 automatisch verteilten Frames (Vollvideo-Modus, 0,088 fps über die volle Länge) wurden gesichtet — bei 15 Minuten Länge laut Skill-Warnung an der Grenze der Frame-Abdeckung, aber ausreichend, da die eingeblendeten Presse-/Produkt-Screenshots klar lesbar waren. Das Arbeitsverzeichnis (`watch-tel0aw1d` unter dem Windows-Temp-Verzeichnis) wird nach Fertigstellung dieser Zusammenfassung gelöscht.
