# Physik-KI für die Industrie

Quellen: [video-summary-9D5MV-4UWcM.md](video-summaries/video-summary-9D5MV-4UWcM.md) (vollständiges 47-Min-Interview mit Johannes Brandstetter), [video-summary-z8OocncaeEs.md](video-summaries/video-summary-z8OocncaeEs.md) (ca. 9,5-minütiger Ausschnitt desselben Interviews in einem anderen Kompilationsvideo)

Beide Quellen dokumentieren dasselbe Gespräch zwischen Host Leonard Schmedding und Prof. Dr. Johannes Brandstetter (Co-Founder/Chief Scientist Emmi AI, seit Mai 2026 VP AI for Science bei Mistral) — einmal als vollständiges Original, einmal als kurzer Ausschnitt in einem News-Kompilationsvideo. Kein inhaltlicher Widerspruch zwischen beiden Fassungen, das vollständige Video liefert lediglich deutlich mehr Tiefe (Werdegang, Wetter-Exkurs, Daten-Diskussion, Europa-Teil).

## Die Mistral-Übernahme von Emmi AI

Emmi AI (Spin-off der JKU Linz/NXAI, gegründet Ende 2024) wurde im Mai 2026 nach nur rund 17 Monaten von Mistral übernommen — per WebSearch unabhängig bestätigt: Bewertung bis zu 330 Mio. €, Brandstetter wird VP AI for Science direkt unter CEO Arthur Mensch und Chief Science Officer Guillaume Lample, Linz wird offizieller Mistral-Standort neben Paris/London/San Francisco (Ausbau von 15–20 auf 40–50 Mitarbeiter). Die im Video kolportierte Einordnung als "größter Startup-Exit Österreichs" ist dagegen ein wiederkehrendes, nicht eindeutig verifizierbares Marketing-Superlativ (Vergleichsgrößen: has.to.be-Exit 250 Mio. €, Tractive-Exit 2026 unbeziffert) — beide Quellen relativieren das bereits selbst.

## Was Physik-Foundation-Modelle sind

Kernunterscheidung zu klassischen LLMs: Alles, was sich als "Instrumentierung" (Aktionen am Computer, z. B. Coding-Agents) abbilden lässt, kann ein LLM übernehmen. Alles, was ein eigenes physikalisches Simulationsprogramm braucht (Auto-, Flugzeug- oder Materialsimulationen), braucht dagegen neue, auf strukturierten Simulationsdaten trainierte Modelle — die Community nutzt laut Brandstetter uneinheitlich Begriffe wie "Physics AI", "Surrogates" oder "Foundation-Modelle für Physik"; eine generalisierende, übergreifend übertragbare Modellklasse existiert noch nicht. Machine Learning ersetzt dabei nicht die klassische Numerik, sondern macht aus numerischen Simulationsdaten schnellere, teils echtzeitfähige Modelle.

Genannte Einsatzfelder: Automotive (Windwiderstand, Crash-/Deformationsverhalten), Aerospace, Halbleiter/Wärmeübertragung, Data-Center-Cooling, Subsurface Modeling. Größte Gewinne dort, wo Simulationen sehr oft wiederholt werden müssen (z. B. Crashtesting, 50–1000 Durchläufe) — reine Solver-Laufzeiten selbst (teils 1–2 Tage) bleiben dagegen oft grundsätzlich schwer beschleunigbar. Kopplung mit Text-to-CAD ist möglich, weil CAD-Geometrie/Meshing sich als Sequenz repräsentieren lässt — die eigentliche Physik-Simulation (große Matrixoperation über das gesamte Mesh) ist dagegen eine grundsätzlich andere, nicht sprachmodellartige Anwendung.

## Der eigentliche Flaschenhals: Daten, nicht Skalierung

Zentrale These: Die Wahl, welche Trainingsdaten wie erzeugt werden, ist wichtiger als reine Modellskalierung. Simulation ist immer eine Abstraktion der Realität mit Annahmen/Vereinfachungen; werden Modelle mit Daten aus unterschiedlichen Annahmen gefüttert, lernt das Modell nur einen Durchschnitt der Physik statt echter Präzision. Datenerzeugung auf industriellem Genauigkeitsstandard ist teils schlicht zu teuer — hier sieht Brandstetter noch viel offene Forschung.

## "Agentic Engineering" als nächste Beschleunigungswelle

Brandstetter prägt den Begriff **"Agentic Engineering"** als Analogie zu Agentic Coding: Wie beim Coding (verifizierbare Aufgaben als Treiber der jüngsten Durchbrüche) erwartet er binnen ein bis zwei Jahren eine ähnlich rasante Beschleunigung technischer Entwicklungsprozesse. Für die Vision eines "Artificial General Engineer" (Analogie zu Jeff Bezos' Project Prometheus, laut WebSearch real mit ca. 18 Mrd. $ Gesamtfinanzierung) nennt er drei nötige Bausteine: (1) Sprachmodelle/Orchestrierung, (2) Physikmodelle/Datengenerierung, (3) reale industrielle Partnerschaften/Echtzeitdaten. Er sieht aktuell kein anderes Lab, das alle drei wie Mistral+Emmi vereint.

## Europa

Brandstetter sieht die Gefahr, dass Europa Produktion/Manufacturing "entgleitet", wenn keine eigene KI-Infrastruktur aufgebaut wird — Investitionen dürften nicht auf Rechenzentren beschränkt bleiben, sondern müssten auch in Produktion, Labore und Testzentren fließen. Er sieht im deutschsprachigen Raum historische Ingenieurs-Stärke als Chance, gerade weil Ingenieurwesen nicht nur Software, sondern auch Manufacturing erfordert — ein Bereich, in dem die USA (Fokus eher auf Agentic Coding, Anthropic z. B. auf Biologie) tendenziell schwächer aufgestellt seien.

## Kernbotschaft

Physik-Foundation-Modelle sind ein eigenständiger, von klassischen LLMs klar abgegrenzter KI-Zweig: Sie beschleunigen/ergänzen numerische Ingenieurssimulationen (Automotive, Aerospace, Halbleiter, Strukturmechanik), ersetzen sie aber nicht — mit Datenqualität/-auswahl statt Rechenleistung als eigentlichem Flaschenhals. Die real bestätigte Mistral-Übernahme des Linzer Startups Emmi AI (bis 330 Mio. €) bündelt drei laut Brandstetter nötige Bausteine (LLM-Orchestrierung, Physikmodelle, echte Industriepartnerschaften) unter einem Dach und markiert für ihn den Beginn von "Agentic Engineering" als nächster, dem Agentic Coding vergleichbarer Beschleunigungswelle.

## Für den technischen Team-/Gruppenleiter

Die Drei-Säulen-These (Sprachmodell-Orchestrierung + Physikmodelle + echte Industriedaten) ist eine nützliche Landkarte für die Einordnung eigener KI-Investitionsentscheidungen im Hardware-/Engineering-Kontext — insbesondere die wiederholt betonte These, dass Datenqualität/-auswahl (nicht Rechenleistung) der eigentliche Flaschenhals für brauchbare Simulationsmodelle ist. Brandstetters expliziter Rat am Ende des Interviews ("kein Kochrezept", erst Assessment der eigenen Bereiche, dann Investitionsentscheidung) ist direkt übertragbar auf eigene KI-Tooling-Investitionen.

## Themen-Tags

Mistral AI, Emmi AI, Johannes Brandstetter, Physik-Foundation-Modelle, Physics AI, Agentic Engineering, Agentic Coding, Text-to-CAD, Fluid Dynamics, Strukturmechanik, Crash-Testing, Project Prometheus, Jeff Bezos, Artificial General Engineer, Europas KI-Souveränität, Arthur Mensch, Leonard Schmedding, JKU Linz, NXAI

## Zu prüfen

- Beide Quellenvideos verwenden identisches Zahlenmaterial und widersprechen sich nicht — die Detailprüfungen (Mistral/Emmi-Bewertung, Bezos' Project Prometheus, Arthur Mensch "Vasallenstaat"-Zitat-Datierung) stehen bereits ausführlich in den jeweiligen Video-Summary-Dateien.
- Die "größter Startup-Exit Österreichs"-Behauptung ist ein wiederkehrendes, nicht eindeutig belegbares Marketing-Muster in der österreichischen Startup-Berichterstattung — hier bewusst nicht als Fakt übernommen.
