# "Warum LLMs gegen eine Wand laufen (MIT-Studie)"

**Kanal:** Tjark Harjes
**URL:** https://www.youtube.com/watch?v=m4azyWbTQ0c
**Länge:** 8:37
**Zusammenfassung erstellt:** 2026-09-22

---

*Siehe auch: [video-summary-dVnPw6or5UI.md](video-summary-dVnPw6or5UI.md) (Scaling Laws anhand der GPT-Reihe, andere Parameterzahlen), [video-summary-pb5cMmdQVJo.md](video-summary-pb5cMmdQVJo.md) (Bauckhage: kleinere, spezialisierte Modelle statt immer größerer), [video-summary-0bcwU3gUv6w.md](video-summary-0bcwU3gUv6w.md) (derselbe Kanal), [ki-forschungsdurchbrueche-2026.md](../ki-forschungsdurchbrueche-2026.md), [openai-krise-ki-blase.md](../openai-krise-ki-blase.md).*

**Hinweis zum Ablauf:** Native YouTube-Untertitel lagen nicht vor. Das Transkript stammt vom Whisper-Fallback über Replicate (142 Segmente, gut verständlich, einzelne Verhörer wie "JGPT"/"JetGPT" für ChatGPT/GPT). Alle 80 Frames wurden gesichtet (Upload: 11.09.2026). Format: Talking-Head (Tjark Harjes spricht frei in die Kamera) mit einigen eingeblendeten Animationen: eine Leistungskurve über Modellgröße mit gestrichelter "Grenze", ein Balkendiagramm GPT-3 vs. GPT-4 ("175 Milliarden" vs. "über 1 Billion, geschätzt"), ein 3D-Vektorraum (Brandenburger Tor/Berlin "nah", Meer/Strand "weit"), eine 2D-Wortkarte mit Abständen ("Brandenburger–Tor 0,76", "Brandenburger–Meer 6,98"), eine Würfel-Projektion (3D auf 2D) und ein leeres log-log-Diagramm "Fehler vs. Modellgröße". Bei ca. 6:15 blendet der Creator selbst eine Korrektur ein: **"\*Dimensionen statt Parametern"**.

## Aufhänger

Alle großen KI-Firmen setzten Milliarden auf eine einzige Strategie: immer weiter skalieren. Das funktioniere, aber *warum* größer besser sei, habe bisher niemand erklären können. Eine MIT-Studie "aus diesem Jahr" habe das nun mathematisch geklärt. Die Mathematik zeige zugleich, dass wir dem Limit dessen, was LLMs lernen können, näher sein könnten als gedacht.

## Skalierungsgesetze (0:39–1:50)

- GPT-1 habe "ein paar Millionen Dollar" gekostet. Größe verdoppelt, GPT-2 deutlich besser. Dieses Muster heiße Skalierungsgesetz: Modell verdoppeln bringt x % bessere Ergebnisse, nicht unbedingt doppelt so gut, aber immer besser.
- Über hunderte Experimente, Architekturen und Firmen hinweg bestätigt. Deshalb das Wettrüsten um Rechenzentren.
- GPT-3 habe ca. 175 Mrd. Parameter, GPT-4 "geschätzt über eine Billion" (gesprochen: "eine Million", die Grafik zeigt "über 1 Billion").

## Wie LLMs Wörter repräsentieren (1:50–3:20)

- Wörter/Tokens werden zu Koordinaten in einem hochdimensionalen Raum (Vergleich mit GPS: 2 Koordinaten reichen für jeden Ort auf der Erde, bei LLMs "2000 Dimensionen").
- Verwandte Begriffe liegen nah beieinander (Brandenburger–Tor), unverwandte weit entfernt (Tor–Meer). So "lerne" das Modell Bedeutung.

## Das MIT-Experiment und "starke Superposition" (3:20–5:25)

- Die Forscher hätten GPT-2 untersucht: ca. 50.000 Tokens in "4.000 Dimensionen".
- Bisherige Annahme: Bei dieser Kompression würden nur die wichtigen/häufigen Begriffe sauber abgelegt, seltene Fachbegriffe fielen weg (Analogie: Foto eines 3D-Raums verliert Information, man kann nicht hinter Objekte sehen). Größere Modelle hätten dann einfach mehr Platz für mehr Bedeutungen.
- Tatsächlicher Befund laut Video: **Alle** 50.000 Begriffe werden gespeichert, aber sie teilen sich überlappend denselben Raum. Das nennen die Forscher **starke Superposition**.

## Interferenz als Ursache falscher Antworten (5:25–6:00)

- Die Überlappung erzeuge "massives Chaos": Wenn z. B. "Brandenburger" und "Kölner"/"Eiffel" sich Raum teilen, wird beim Abruf der falsche Anteil ausgelesen. Das sei der Grund, warum ChatGPT manchmal selbstbewusst falsche Antworten gibt.
- Fachbegriff: **Interferenz**. Lange habe man das für einen unvermeidlichen Nebeneffekt gehalten.

## Die Kernaussage der Studie (6:00–7:00)

- Die Interferenz sei **umgekehrt proportional zur Breite des Modells**: Verdoppelt man die Breite (im Video zunächst fälschlich "Parameter", per Einblendung korrigiert zu "Dimensionen"), halbiert sich die Überlappung.
- Größere Modelle lernen also nicht unbedingt neue Fähigkeiten, sondern können vorhandenes Wissen sauberer abrufen. Sie werden nicht "klüger", aber die Fehlerrate sinkt.
- Tests an verschiedenen Modellen hätten die Vorhersage bestätigt.

## Folgerungen laut Video (7:00–8:25)

1. **Erklärt die Milliarden-Wette der Labore:** Sie wissen nicht, wie gut genau ein Modell wird, aber dass es mit mehr Breite besser werden *muss*. Haken: Rechenleistung und Stromkosten steigen beim Verdoppeln schneller als die Leistung.
2. **Zeigt das Limit:** Die Skalierungsgesetze brechen dort, wo sich die Tokens nicht mehr sinnvoll in noch mehr Dimensionen unterbringen lassen.
3. **Eröffnet neue Strategien:** Information effizienter packen, damit kleinere Modelle ähnliche Leistung bei geringerem Aufwand erreichen.

Zum Schluss folgt ein Aufruf zu Like, Follow und Kommentar. Es gibt keinen Sponsor-Hinweis.

## Einordnung

Die zugrunde liegende Studie ist real und seriös (siehe Zu prüfen): *"Superposition Yields Robust Neural Scaling"* von Yizhou Liu, Ziming Liu und Jeff Gore (MIT), arXiv 2505.10465, NeurIPS 2025. Die Kernaussage (bei starker Superposition skaliert der Loss umgekehrt proportional zur Modellbreite) gibt das Video im Wesentlichen korrekt wieder, und die Vektorraum-Erklärung ist für Laien gut gemacht. Schwächen:

- **Der Titel übertreibt.** "Gegen eine Wand laufen" ist im Video nur ein kurzer Ausblick, kein belegtes Ergebnis. Die Studie erklärt vor allem, *warum* Skalierung funktioniert, und nennt eine theoretische Grenze (Breite erreicht die Zahl der zu repräsentierenden Merkmale). Eine aktuell erreichte Wand behauptet sie nicht.
- **"Fehlerrate halbiert" ist verkürzt.** Die Studie betrachtet den Loss (Vorhersagefehler beim nächsten Token), nicht die Halluzinationsrate. Die direkte Gleichsetzung von Interferenz mit "ChatGPT antwortet selbstbewusst falsch" ist eine plausible Veranschaulichung des Videos, kein Ergebnis der Studie.
- **Mehrere Detailfehler** bei Zahlen und Chronologie (siehe Zu prüfen).
- **"Dieses Jahr"** stimmt nicht: Das Paper ist vom Mai 2025, das Video vom September 2026.

## Für den technischen Team-Lead

- **Gutes Denkmodell für Erwartungsmanagement im Team:** Größere Modelle machen weniger Fehler, weil sich gespeichertes Wissen weniger überlagert, nicht weil sie grundsätzlich neue Fähigkeiten haben. Seltenes Fachwissen (Bauteil-Parameter, Normverweise, firmenspezifische Begriffe) ist genau das, was bei Überlagerung am ehesten falsch "ausgelesen" wird. Das stützt die Regel aus [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md), solche Angaben immer gegen Datenblatt oder Norm zu prüfen, auch bei großen Modellen.
- **Für Hardware-Leute intuitiv:** Das Bild entspricht Übersprechen/Crosstalk bzw. nicht-orthogonalen Basisvektoren. Mehr Dimensionen heißt mehr "Abstand" zwischen den Kanälen und damit weniger Störung, aber mit abnehmendem Ertrag pro Kosten.
- **Kostenseite:** Wenn die Fehlerreduktion nur ~1/Breite ist, die Rechenkosten aber stärker steigen, sind kleinere, gezielt eingesetzte Modelle (lokal, spezialisiert, mit Retrieval aus eigenen Dokumenten) für viele Team-Anwendungen die wirtschaftlichere Wahl. Das passt zu [lokale-ki.md](../lokale-ki.md) und zur Bauckhage-Argumentation in [video-summary-pb5cMmdQVJo.md](video-summary-pb5cMmdQVJo.md).
- Direkt umsetzbare Handlungsempfehlungen liefert das Video nicht, es ist ein reines Erklärvideo.

---

## Kernbotschaft

Tjark Harjes erklärt in knapp neun Minuten eine reale MIT-Arbeit (Liu, Liu, Gore, NeurIPS 2025): LLMs speichern deutlich mehr Begriffe, als sie Dimensionen haben, indem sie diese überlappend ablegen ("starke Superposition"). Die dabei entstehende Interferenz sinkt umgekehrt proportional zur Modellbreite. Damit liefert die Arbeit eine mechanistische Erklärung, warum Skalierung funktioniert: Größere Modelle rufen vorhandenes Wissen sauberer ab, statt grundsätzlich klüger zu werden, und das zu steigenden Kosten pro Verbesserung. Die Erklärung ist didaktisch gut, der Titel ("gegen eine Wand") aber zugespitzt. Die Gleichsetzung von Interferenz mit Halluzinationen ist eine Vereinfachung, und mehrere Zahlen (GPT-1-Jahr, GPT-2-Dimensionen, "Verdopplung" zwischen GPT-Generationen) stimmen nicht.

## Themen-Tags

Scaling Laws, Skalierungsgesetze, Superposition, Interferenz, Embeddings, Vektorraum, Modellbreite, Loss-Skalierung, Halluzinationen, MIT, Yizhou Liu, Ziming Liu, Jeff Gore, NeurIPS 2025, GPT-2, GPT-3, GPT-4, Rechenkosten, KI-Wettrüsten, Mechanistische Interpretierbarkeit, Tjark Harjes

## Zu prüfen

- **Studie per WebSearch bestätigt:** "Superposition Yields Robust Neural Scaling", Yizhou Liu, Ziming Liu, Jeff Gore (MIT), [arXiv 2505.10465](https://arxiv.org/abs/2505.10465), NeurIPS 2025 (laut Suchergebnissen Oral und Best-Paper-Runner-up). Bestätigt ist die Kernaussage: Bei starker Superposition skaliert der Loss umgekehrt mit der Modelldimension, offene LLMs liegen in diesem Regime, und die Chinchilla-Skalierung ist damit konsistent. Das Video nennt Autoren und Titel nicht, die Zuordnung ergibt sich aus der Übereinstimmung der Inhalte. Das Paper selbst wurde nicht im Volltext gelesen.
- **"Dieses Jahr"** ist falsch, das Paper erschien im Mai 2025 (arXiv) bzw. auf der NeurIPS im Dezember 2025.
- **GPT-2 mit "4.000 Dimensionen" ist unplausibel** (aus Vorwissen, nicht per Web geprüft): Das GPT-2-Vokabular hat ~50.257 Tokens (passt zu "50.000"), die Embedding-Breite liegt aber je nach Größe bei 768 bis 1.600. Ob das Paper an anderer Stelle mit ~4.000 Dimensionen rechnet oder der Creator Modelle verwechselt, blieb offen. Auch "2000 Dimensionen" im GPS-Vergleich ist nur als Größenordnung zu verstehen.
- **Chronologie und Größen der GPT-Reihe fehlerhaft** (aus Vorwissen): GPT-1 erschien 2018, nicht 2020 (2020 kam GPT-3). GPT-2 war ~13-mal so groß wie GPT-1 (117 Mio. → 1,5 Mrd.), nicht "verdoppelt". Die Parameterzahlen von GPT-4/5/6 sind offiziell nicht veröffentlicht, "immer größer" ist eine Annahme.
- **GPT-4-Parameterzahl:** Das Video sagt "über eine Million", die Grafik zeigt "über 1 Billion, geschätzt". Gemeint ist offensichtlich die Billion. [video-summary-dVnPw6or5UI.md](video-summary-dVnPw6or5UI.md) nennt "1,7 Billionen". Das ist kein echter Widerspruch, beide sind inoffizielle Schätzungen.
- **"Fehlerrate halbiert sich bei doppelter Breite":** Laut Paper geht es um den Loss-Anteil aus der Repräsentation, nicht um eine Halluzinations- oder Fehlerquote bei Antworten. Die Verbindung Interferenz → "selbstbewusst falsche Antworten" ist eine plausible, aber nicht belegte Vereinfachung des Videos.
- **"Wand"/Limit:** Das Video formuliert die Grenze unscharf ("wenn Tokens nicht mehr in mehr Dimensionen passen"). Ob und wann heutige Frontier-Modelle an diese Grenze stoßen, belegt das Video nicht.
- **Cross-Check mit bestehenden Notizen:** Im Repo gibt es noch keinen Beitrag zu Superposition bzw. einer mechanistischen Erklärung der Scaling Laws, das Thema ist neu. Überschneidungen: [video-summary-dVnPw6or5UI.md](video-summary-dVnPw6or5UI.md) (Scaling Laws, GPT-Reihe; kein Widerspruch, nur andere Schätzwerte), [video-summary-pb5cMmdQVJo.md](video-summary-pb5cMmdQVJo.md) (kleinere, spezialisierte Modelle; passt zu Folgerung 3), [openai-krise-ki-blase.md](../openai-krise-ki-blase.md) (Kosten des Skalierungs-Wettrüstens). Derselbe Kanal ist mit [video-summary-0bcwU3gUv6w.md](video-summary-0bcwU3gUv6w.md) vertreten. Thematisch passt das Video am ehesten in [ki-forschungsdurchbrueche-2026.md](../ki-forschungsdurchbrueche-2026.md), ist aber kein 2026er-Durchbruch.
