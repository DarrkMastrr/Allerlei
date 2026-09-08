# "Alle schauen auf die Roboter. Ich auf etwas anderes"

**Kanal:** Marc De Fanti
**URL:** https://www.youtube.com/watch?v=mtFsQeyeADc
**Länge:** 10:12
**Zusammenfassung erstellt:** 2026-09-08

---

*Siehe auch: [video-summary-RWDsx8KxtX8.md](video-summary-RWDsx8KxtX8.md) und [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md) — beide bereits ausführlich fact-gecheckte China-Robotik-/KI-Folgen desselben Themenfelds. Cross-Checks siehe unten in "Zu prüfen".*

## Aufhänger und Format

Marc De Fanti (durchgehend im Talking-Head-Format, ruhiger Podcast-Stil) testet hier laut eigener Aussage am Videoende ein neues Format: Statt seiner sonst üblichen "sehr taktischen Videos" zu KI-Nutzung will er die Marktereignisse einer Woche einordnen. Kernthese: Die Roboter-Schlagzeilen aus Peking waren diese Woche "die Show", das eigentlich wichtige Ereignis lag aber woanders — bei einem anonym gestarteten KI-Modell und den damit verbundenen Marktverschiebungen.

## Robotik: World Humanoid Robot Games in Peking

Vom 22. bis 26. August fanden die zweiten World Humanoid Robot Games in Peking statt: über 600 Teams, 2.000 Roboter, 16 Länder, 51 Disziplinen, fünf Wettkampftage. Meistdiskutiert: der 100-Meter-Lauf.

- **Tiangong Ultra** (Beijing Humanoid Robot Innovation Center, Marke "X-Humanoid") lief die 100 Meter am Eröffnungstag in 9,39 s, am Dienstag in 8,86 s, im Finale am Mittwoch in 8,64 s — Usain Bolts Weltrekord liegt bei 9,58 s. Wichtige Einordnung des Hosts: Es waren nicht drei verschiedene Roboter, sondern derselbe, der sich innerhalb von fünf Tagen um fast eine Dreiviertelsekunde verbesserte.
- Nach dem Zieleinlauf können die Sprint-Roboter nicht bremsen und werden auf Tragen von der Bahn getragen (im Video als virale, halb komische Szene gezeigt) — laut Host kein Software-Bug, sondern Physik: Ein rennender Roboter hält die Balance, indem er den Druckpunkt ständig unter der Fußfläche hält; Elektromotor + Getriebe haben zu wenig Drehmoment und reagieren zu langsam, um Geschwindigkeit wie menschliche Hüften/Knie/Gelenke abzufedern. Aus demselben Grund seien enge Kurven bei Tempo weiterhin sehr schwierig.
- Beim Standweitsprung (Frame bei t≈01:35, "Standing High Jump") wurden 2,88 m erreicht, im Vorjahr nur 95 cm — der menschliche Rekord liegt bei rund 1,65 m.
- **Wichtigster Einwand des Hosts:** Ein Großteil der Roboter war ferngesteuert (ein Mensch sitzt in der Nähe und steuert), Autonomie war für die Spiele keine Voraussetzung. Experten schätzen die Branche aktuell bei rund 500.000 Stunden nutzbarer Trainingsdaten, während für "echte physische Intelligenz" (menschliches Fähigkeitsniveau) rund 100 Millionen Stunden nötig seien — genau diese Lücke zwischen Sprint-Show und tatsächlichem Entwicklungsstand ist der Kern seiner Robotik-Kritik. Kurzer Seitenhieb: Der Host hält es für ein "offenes Geheimnis", dass diese Roboter irgendwann bewaffnet werden könnten, auch wenn das öffentlich selten so kommuniziert werde.

## Das eigentliche Ereignis: Ox Alpha / GLM-Stealth-Launch

Am 20. August erschien auf OpenRouter (einer Plattform für gebündelten Zugriff auf viele KI-Modelle) ein Modell namens **"Ox Alpha"** ohne Herstellerangabe ("Stealth model, developed and operated by a third party that wishes to remain anonymous"): kostenlos, 1 Mio. Token Kontextfenster, für Coding und lange Agenten-Aufgaben ausgelegt, versteht auch Bilder/Video. Sechs Tage lang wusste niemand, wer dahintersteckt; in dieser Zeit wurden über 20 Billionen Tokens verarbeitet — laut OpenRouter das größte je auf der Plattform gelaufene Modell. Vor zwei Tagen (bezogen auf den Videozeitpunkt) wurde aufgelöst: **Zhipu AI** steht dahinter, das Modell nennt der Host "GLM 4".

Der Host ordnet ein: Öffentliche Tests zeigen Ox Alpha besser als Claude 3.5 — aber das sind Hersteller-eigene Tests/Stichproben, Gegentests könnten anders ausfallen. Seine nüchterne Zusammenfassung: Ox Alpha schlägt Claude 3.5 nicht klar, sondern ist etwa gleich gut bei einem Bruchteil des Preises — und genau das (Parität zu einem Fünftel des Preises), nicht Überlegenheit, sei die eigentliche Nachricht. Der Anbieter habe zudem erklärt, nicht mit den Eingaben zu trainieren (Ausnahme vom sonst üblichen "kostenlos = Trainingsdaten"-Tausch) — der Host weist aber darauf hin, dass "nicht trainieren" nicht dasselbe ist wie "nicht speichern".

## Nvidia vs. Alphabet/DeepMind

Nvidia meldete am Mittwoch 96,2 Mrd. $ Quartalsumsatz (+106 %) und gab erstmals einen Jahresausblick: 70 % erwartetes Wachstum (Analysten hatten ~44 % erwartet). Im Kontrast dazu verlor Alphabet seit seinem Allzeithoch am 13. Mai 15 % seines Aktienwerts — umgerechnet 692 Mrd. $. Zusätzlich: Demis Hassabis, laut Host "der eigentliche Kopf hinter AlphaFold" und bis vor Kurzem CEO von DeepMind, ist nicht mehr CEO, sondern nur noch im Alphabet-Board. Weitere leitende Forscher haben DeepMind verlassen (Richtung OpenAI, Anthropic oder eigene Gründungen); 2023 kamen bei DeepMind noch 12 Neueinstellungen pro Abgang, aktuell nur noch zwei — bei Anthropic dagegen 22 Neueinstellungen pro Abgang.

## Einordnung: Chinesische Modelle im Preiskampf

Chinesische Modelle machen laut Host mittlerweile 30–46 % der Token-Nutzung aus, die US-Firmen über OpenRouter fahren (vor einem Jahr nur 4–5 %) und sind 60–90 % günstiger als die Topmodelle von OpenAI/Anthropic. Seine Schlussfolgerung für die Praxis: Top-Modelle dürften teurer werden (Nvidia-Preiserhöhungen, steigende Speicherkosten, engere Provider-Partnerschaften), während Standardarbeit (Zusammenfassen, Sortieren, Kategorisieren, Datenextraktion) drastisch billiger wird. Empfehlung: Aufgaben aufteilen statt alles über einen Anbieter/ein teures Modell laufen zu lassen — das teure Modell für wirklich Schwieriges, das billige für den Rest.

## Für den Hardware-Entwickler/Team-Lead: Praktische Relevanz

Zwei Punkte sind direkt übertragbar: Erstens der Modell-Split-Ratschlag (teures Modell nur für schwierige Aufgaben, günstiges chinesisches Modell für Routinearbeit) als konkrete Kostenoptimierung für Tool-Ketten im Team — inhaltlich deckungsgleich mit der bereits in [video-summary-Mg6NOwHqflw.md](video-summary-Mg6NOwHqflw.md) dokumentierten Erkenntnis "Preis pro Token ist nicht Preis pro Aufgabe". Zweitens die Warnung zu "kostenlos aber anonym" bei KI-Diensten (Ox Alpha) — relevant für die Bewertung, welche externen Modelle/Tools mit welchen (Firmen-)Daten gefüttert werden dürfen, bevor der Anbieter überhaupt bekannt ist.

---

## Kernbotschaft

Der reißerische Titel wird eingelöst: Der Host argumentiert, dass die viral gegangenen Roboter-Rekorde aus Peking zwar beeindruckende Fortschritte zeigen, aber vor allem "Show" sind (ein einzelner Roboter, teils ferngesteuert, riesige Lücke zwischen 500.000 und benötigten 100 Mio. Trainingsstunden) — während in derselben Woche ein chinesisches Labor (Zhipu/GLM) sechs Tage lang anonym ein Spitzenmodell verschenkte, es zu einem Bruchteil der US-Preise anbot und damit den eigentlichen Angriff auf die Preisstruktur der Frontier-Modelle startete, parallel zu Nvidias Rekordzahlen und einem sichtbaren Führungs-/Talent-Exodus bei Googles DeepMind. Praktische Konsequenz laut Host: nicht den Anbieter wechseln, sondern Aufgaben nach Schwierigkeit auf teure und günstige Modelle aufteilen.

## Themen-Tags
World Humanoid Robot Games, Tiangong Ultra, Roboter-Autonomie/Fernsteuerung, Physical Intelligence/Trainingsdaten-Lücke, Ox Alpha, Zhipu AI/GLM, OpenRouter, Stealth-Model-Launch, Nvidia-Quartalszahlen, Alphabet-Kursverlust, Demis Hassabis, DeepMind-Abwanderung, Chinesische Modelle vs. US-Preise, Multi-Modell-Strategie

## Zu prüfen

- **Robotik-Fakten (Tiangong Ultra, Peking): bestätigt.** Per WebSearch unabhängig verifiziert (Al Jazeera, Global Times, Tech Times, CGTN): Tiangong Ultra vom Beijing Humanoid Robot Innovation Center lief bei den World Humanoid Robot Games (22.–26. August 2026) tatsächlich 9,39 s → 8,86 s → 8,64 s im 100-Meter-Finale, deutlich innerhalb von Usain Bolts 9,58-s-Weltrekord. Zeitraum und Ablauf decken sich exakt mit dem Video.
- **Ox Alpha / GLM: im Kern bestätigt, aber eine Modellbezeichnung im Video ist ungenau.** Per WebSearch (u. a. TheNextWeb, CoderSera, DigitalApplied) bestätigt: Ox Alpha war tatsächlich Zhipu/Z.ai, lief 20.–26. August 2026 kostenlos auf OpenRouter mit 1M-Kontext, wurde am 26. August aufgelöst. Der Host nennt das Modell im Transkript "GLM 4" — laut mehreren unabhängigen Quellen war es jedoch präzise **GLM-5.3-Flash** (320B Gesamt-/18B aktive Parameter, MoE), inzwischen offiziell als `z-ai/glm-5.3-flash` gelistet, MIT-lizenzierte Gewichte auf Hugging Face. Der im Frame bei t≈06:15 gezeigte Benchmark-Vergleich (DeepSWE Pass@1: Ox Alpha 80 %, Fable-5 65 %, GPT-5.6-Sol 52 %) deckt sich mit unabhängig zitierten Zahlen — die Kernaussage "in etwa gleichauf mit Claude, deutlich günstiger" ist damit gut belegt, nur die Versionsbezeichnung "GLM 4" im gesprochenen Text ist eine Ungenauigkeit/Vereinfachung.
- **Nvidia-Zahlen, Alphabet-Kursverlust, Hassabis: alle bestätigt.** Nvidia Q2 FY2027: 96,2 Mrd. $ Umsatz (+106 % YoY), 70 %-Wachstumsziel für FY2028 (Analystenerwartung: ~44 %) — exakt wie im Video (Gurufocus, CNBC, StockTitan). Alphabet: Allzeithoch am 13. Mai 2026, seither -15 % / -692 Mrd. $ Marktwert — exakt wie im Video (Bloomberg, Fortune). Demis Hassabis trat am 5. August 2026 tatsächlich als DeepMind-CEO zurück (jetzt Chairman von GDM + Chief Scientist Alphabet), Nachfolger für das Tagesgeschäft ist Koray Kavukcuoglu — Kernaussage des Videos bestätigt, die genannten Abwerbe-Verhältniszahlen (12:1 → 2:1 bei DeepMind, 22:1 bei Anthropic) wurden nicht einzeln nachverifiziert.
- **OpenRouter-Token-Anteile chinesischer Modelle: Größenordnung bestätigt.** Mehrere unabhängige Quellen (Dealroom, Yahoo Finance, Wanda Builds, Tech Times) bestätigen, dass chinesische Modelle seit Anfang 2026 stark auf 30–46 % (teils bis 60 %+) der OpenRouter-Token-Nutzung gestiegen sind, ausgehend von rund 4,5–11 % im Vorjahr — passt zur Video-Aussage. Die "60–90 % günstiger"-Angabe ist ebenfalls plausibel und deckt sich mit Beispielzahlen (z. B. DeepSeek V4 Flash 0,14 $ vs. GPT-5.5 5,00 $ pro Mio. Input-Tokens).
- **Cross-Check mit [video-summary-RWDsx8KxtX8.md](video-summary-RWDsx8KxtX8.md) und [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md) — Bestätigung statt Widerspruch:** Beide bereits im Repo dokumentierten China-Robotik-Folgen fanden unabhängig belegt, dass humanoide Roboter trotz Autonomie-Marketing überwiegend ferngesteuert/teleoperiert sind (1X Neo, URKL-Kampfliga). Die hier im Video selbst gemachte Aussage "ein Großteil der Peking-Roboter war ferngesteuert" ist eine dritte, unabhängige Bestätigung genau desselben Musters — auffällig konsistent über drei verschiedene Videos/Quellen hinweg.
- **Thematische Parallele (kein Widerspruch) zu [video-summary-JH_NRbnbC1s.md](video-summary-JH_NRbnbC1s.md):** Dort wird Kimi K3 (Moonshot AI) als "DeepSeek Moment 2.0" beschrieben — ein anderes Modell, aber dieselbe Grundstruktur wie hier (chinesisches Labor liefert überraschend ein kostenloses/günstiges Spitzenmodell und verschiebt damit die Preis-/Leistungswahrnehmung). Zwei unabhängige Ereignisse mit demselben Muster innerhalb weniger Wochen, keine inhaltliche Überschneidung der konkreten Modelle.
- **Ablauf-Hinweis:** Native YouTube-Untertitel (Englisch, captions) liefen ohne Whisper-Fallback durch, 266 Segmente für die vollen 10:12 Minuten, durchgehend klar verständlich. Alle 80 extrahierten Frames über die volle Videolänge gelesen; Bildmaterial (Renn-Aufnahmen, Balkendiagramme zu den 100-Meter-Zeiten, OpenRouter-/Ox-Alpha-Screenshots, Benchmark-Tabelle, Nvidia-Pressemitteilung) deckt sich durchgehend mit dem gesprochenen Text.
