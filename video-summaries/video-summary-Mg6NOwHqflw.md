# "Gewinnt China den KI Krieg?"

**Kanal:** Loris Galler
**URL:** https://www.youtube.com/watch?v=Mg6NOwHqflw
**Länge:** 09:36
**Zusammenfassung erstellt:** 2026-09-07

---

## Ausgangsthese und Host

Loris Galler (nach eigener Aussage angestellt bei "einem der erfolgreichsten AI-Startups Europas", wo er KI nutzt, um KI zu programmieren — Firma nicht genannt) stellt die These auf: Bei Open-Source-/Open-Weight-Modellen ist China aktuell "das mit Abstand wichtigste Land der Welt". Chinesische Modelle könnten mit US-Frontier-Modellen nicht nur mithalten, sondern sie in manchen Kategorien übertreffen — und das mit deutlich weniger Geld und offiziell schlechterer Hardware. Die im Video ebenfalls aufgestellte Behauptung, Microsoft, Nvidia und Amazon würden diese chinesischen Modelle sogar "als Basis für ihre eigenen" nutzen, ließ sich per WebSearch nicht eindeutig bestätigen (siehe "Zu prüfen").

## Benchmarks: Wo China auf dem Papier steht

Datenquelle ist der Artificial-Analysis-Intelligence-Index (unabhängiger Evaluator, bündelt 9 Benchmarks, davon 58 % Agentic/Coding-Anteil). Wichtiger Einschub des Hosts: Benchmark-Werte ohne Angabe des "Effort Level" (Reasoning-Aufwand) seien wenig aussagekräftig — als Beispiel nennt er Kimi K3, das im Benchmark ARC-AGI-2 allein durch höhere Reasoning-Stufe von 12,4 % auf 60,4 % springt. Nach Laboren sortiert steht China auf Platz 4. In der LMArena (Menschen stimmen blind über bessere Antworten ab) liegt Moonshots Kimi K3 aktuell auf Platz 2; im Juli stand es laut Video 8 Tage auf Platz 1 — als erstes offenes Modell überhaupt.

## Preis: Warum der Tokenpreis täuscht

Kernpunkt: Relevant ist nicht der Preis pro Million Tokens, sondern die Kosten pro erledigter Aufgabe. Beispiel GPT: 30 $ pro Million Output-Tokens, fünfmal so teuer wie Qwen — trotzdem trennen beide bei einer konkreten Benchmark-Aufgabe nur 4 Cent, weil GPT für dieselbe Arbeit ca. 7.000 Tokens braucht, Qwen 38.000 und Opus 40.000. Der Tokenpreisvorteil verschwindet, wenn ein Modell doppelt so viel "redet".

## Eigener Test: Tanzender Bär mit Musik

Für 3,07 $ (davon 1,93 $ allein für Claude Opus 5 als Kontrollmodell) hat der Host über OpenRouter fünf Modelle mit einem selbst geschriebenen ~200-Zeilen-Coding-Agenten (Werkzeuge: Datei schreiben, Datei lesen, Shell-Befehl ausführen) getestet: Kimi K3, GLM 5.2, Qwen 3.8 Max, DeepSeek V4 Pro und Claude Opus 5. Gleicher Prompt, gleicher Harness, ein Durchlauf pro Modell.

- **Runde 1** — Aufgabe: Website mit einem tanzenden gelben Bären (HTML/CSS/SVG, freie Wahl der Technik). 4 von 5 Modellen lieferten einen erkennbaren Bären; GLM 5.2 scheiterte sichtbar (Frame zeigt eine unklare Form).
- **Runde 2** (gleicher Chat) — Aufgabe: passende Musik hinzufügen, ohne dass explizit gesagt wurde, sie solle zur Animation passen. Alle fünf Modelle synchronisierten die Musik trotzdem, vier davon exakt auf 100 BPM, und alle komponierten die Musik selbst direkt als Code (Noten). Notenzahl als grobes Komplexitätsmaß: GLM 5.2 = 16, DeepSeek V4 Pro = 8, Kimi K3 = 48, Qwen 3.8 Max = 27 (Favorit des Hosts unter den chinesischen Modellen — klar erkennbarer Bär, hübscher Hintergrund, guter Musik-Button), Claude Opus 5 = 55 (laut Host optisch und musikalisch auf Platz 1).

Der Host selbst relativiert: Der Test misst weder Agentic Coding noch logisches Denken, sondern ist ein bewusst anderer, ergänzender Vergleich.

## Was heißt "Open Source" bei KI-Modellen?

Drei Definitionen mit unterschiedlichem Ergebnis:
1. **Lizenz-Definition** (Gewichte öffentlich + echte OSS-Lizenz wie MIT/Apache 2.0): Qwen, DeepSeek und GLM gelten danach als Open Source.
2. **EU-Definition** (AI Act: freie Lizenz, öffentliche Gewichte, Architektur und Nutzungsinformation) — im Kern dasselbe Ergebnis.
3. **OSI-Definition** (Open Source Initiative, strengste Variante: zusätzlich müssen Trainingsdaten offengelegt werden, damit ein gleichwertiges Modell nachbaubar wäre) — danach gilt **keines** der chinesischen Modelle als Open Source. Der Host findet diesen Maßstab "deutlich zu hart".

Lizenz-Detail: DeepSeek und GLM stehen unter MIT, Qwen unter Apache 2.0 (praktisch keine Auflagen). Kimi K3 — ausgerechnet das Modell mit der höchsten Punktzahl — hat dagegen eine eigene Lizenz mit einer Sonderklausel für große Firmen (im Frame lesbar: Umsatz-/Nutzerschwellen, ab denen eine separate Vereinbarung mit Moonshot AI nötig wird) und ist damit nicht uneingeschränkt Open Source.

Downloads: Qwen wird auf Hugging Face laut Video 5,5-mal so oft heruntergeladen wie Googles komplette Gemma-Familie zusammen. Neu (zum Videozeitpunkt): Z.ai hat GLM 5.3 veröffentlicht.

## Offene vs. geschlossene Modelle: Wer führt wo?

Bei geschlossenen Modellen liegt laut Video die USA rund 3 Punkte vor China. Bei offenen (Open-Weight-)Modellen liegt China dagegen deutlich vorn. Genannte aktuelle US-Reaktionen: Google veröffentlichte im April Gemma 4, Nvidia im Juni Nemotron 3 Ultra (550 Mrd. Parameter, Gewichte und Trainingsdaten offen — per WebSearch bestätigt, siehe "Zu prüfen"), und laut Host ist auch Meta/Llama wieder aktiver geworden. Fazit des Hosts: China liegt insgesamt ein paar Monate hinter dem amerikanischen Frontier, der Abstand schrumpft aktuell nicht wirklich — hängt aber stark davon ab, wo genau man hinschaut (offen vs. geschlossen). Für die praktische Nutzung reiche der aktuelle Stand aber "easy": Ein Modell wie Qwen 3.8 27B liege ungefähr auf dem Niveau von Opus 4.6, laufe aber auf einem gut ausgestatteten Laptop statt auf GPUs im Wert mehrerer tausend Euro.

## Finanzielle Realität: Z.ai als Beispiel

Z.ai (Entwickler von GLM) ist seit Januar an der Börse in Hongkong gelistet und muss deshalb Zahlen offenlegen. Laut Jahresabschluss: rund 100 Mio. $ Umsatz bei 655 Mio. $ Verlust. Der Host merkt an, dass es bei anderen chinesischen Laboren finanziell ähnlich oder schlechter aussehen könnte, da diese Zahlen nicht öffentlich sind.

## Für den Hardware-Entwickler/Team-Lead: Praktische Relevanz

Zwei Punkte sind für einen technischen Team-Lead direkt umsetzbar: Erstens die Kernbotschaft "Preis pro Token ist nicht Preis pro Aufgabe" — bei der Modellauswahl für interne Tools zählt die tatsächliche Token-Menge pro gelöster Aufgabe, nicht das Preisschild pro Million Tokens. Zweitens die konkrete Lauffähigkeit offener chinesischer Modelle (z. B. Qwen 3.8 27B) auf normaler Laptop-Hardware statt teurer GPU-Cluster — relevant für Teams, die aus Datenschutz-/Kostengründen lokale statt Cloud-Inferenz evaluieren (Anschluss an das bereits im Repo dokumentierte Thema "lokale KI", siehe [lokale-ki.md](../lokale-ki.md)). Drittens die Lizenz-Nuance bei Kimi K3 (Sonderklausel für große Firmen) — praktisch relevant, bevor ein Unternehmen ein "offenes" chinesisches Modell produktiv einsetzt, sollte die konkrete Lizenz statt nur des Open-Source-Labels geprüft werden.

---

## Kernbotschaft

Das Video argumentiert differenziert statt reißerisch: Bei geschlossenen Frontier-Modellen liegt die USA weiterhin klar vorn (ca. 3 Indexpunkte, ein paar Monate Vorsprung), bei offenen/Open-Weight-Modellen führt China dagegen deutlich — Kimi K3 stand im Juli 2026 tatsächlich kurzzeitig als erstes offenes Modell auf Platz 1 der LMArena. Der reißerische Titel ("Krieg") wird durch den eigentlichen Inhalt nicht eingelöst; das Video liefert stattdessen eine nüchterne, mit eigenem (kleinem, transparent offengelegtem) Experiment unterlegte Einordnung, inklusive der wichtigen Relativierung, dass "billiger pro Token" nicht automatisch "billiger pro Aufgabe" bedeutet und dass "Open Source" bei chinesischen Modellen je nach Definition (Lizenz/EU/OSI) sehr unterschiedlich ausfällt.

## Themen-Tags
China vs. USA KI-Rennen, Open-Weight-Modelle, Open-Source-Definition, Kimi K3, GLM 5.2/5.3, Qwen 3.8 Max, DeepSeek V4 Pro, Claude Opus 5, Artificial Analysis Intelligence Index, LMArena, Token-Kosten vs. Aufgabenkosten, Z.ai IPO, Nvidia Nemotron 3 Ultra, EU AI Act, Lokale KI

## Zu prüfen

- **Plausibilitätscheck per WebSearch — im Kern bestätigt:** Kimi K3 (Moonshot AI, 2,8 Bio. Parameter MoE, veröffentlicht 16./27. Juli 2026) landete real auf Platz 1 der LMArena-"Frontend Code Arena" als erstes offenes Modell überhaupt — die genannten "8 Tage auf Platz 1" ließen sich nicht exakt gegenprüfen, die Kernaussage (erstes offenes Modell auf Platz 1) ist aber unabhängig bestätigt. Nvidia Nemotron 3 Ultra (550 Mrd. Gesamt-/55 Mrd. aktive Parameter, Release 4. Juni 2026, Gewichte + Trainingsdaten unter offener Lizenz) exakt bestätigt. Z.ai-Finanzzahlen liegen in der Größenordnung des Videos (Suchergebnisse: für das Geschäftsjahr 2025 ca. 105 Mio. $ Umsatz bei ca. 686 Mio. $ Verlust, IPO an der Hongkonger Börse am 8. Januar 2026) — Video nennt "100 Mio. $ Umsatz, 655 Mio. $ Verlust", also nah dran, nicht exakt deckungsgleich (evtl. andere Berichtsperiode/Währungsumrechnung).
- **Nicht bestätigt/unklar:** Die Behauptung, Microsoft, Nvidia und Amazon würden chinesische Modelle "als Basis für ihre eigenen" nutzen, ließ sich per WebSearch nicht eindeutig belegen. Gut dokumentiert ist, dass diese Konzerne chinesische Open-Weight-Modelle (v. a. DeepSeek) über eigene Plattformen anbieten/hosten (Azure AI Foundry, AWS Bedrock, Nvidia NIM) — das ist aber etwas anderes als "als Basis für eigene Modelle nutzen". Hier möglicherweise eine Verkürzung/Zuspitzung des Hosts.
- **"5,5× mehr Downloads als Gemma-Familie" (Qwen, Hugging Face):** Suchergebnisse bestätigen die Richtung (Qwen ist die mit Abstand meistheruntergeladene offene Modellfamilie, deutlich vor Gemma), aber der exakte Faktor variiert je nach Quelle/Zeitpunkt teils stark — ein Artikel (TheNextWeb) weist sogar darauf hin, dass Alibabas eigene Download-Zahlen für Qwen möglicherweise höher liegen als unabhängige Hugging-Face-Zählungen. Die "5,5×"-Zahl selbst konnte nicht exakt verifiziert werden, die Grundaussage (Qwen klar vorn) schon.
- **Cross-Check mit [lokale-ki.md](../lokale-ki.md):** Direkte inhaltliche Bestätigung statt Widerspruch — dort wird dokumentiert, dass US-Exportkontrollen für KI-Chips chinesische Labore (u. a. DeepSeek) zu besonders starker Effizienzoptimierung treiben; das deckt sich mit der hier im Video genannten These "China schafft mit weniger Geld und offiziell schlechterer Hardware ähnlich viel".
- **Cross-Check mit [video-summary-qZRftXozT3M.md](video-summary-qZRftXozT3M.md):** Dort wird ein Epoch-AI-Trendchart zitiert, wonach offene Modelle den besten geschlossenen Modellen "ca. 4 Monate" hinterherhinken — praktisch identisch mit der hier im Video gezogenen Schlussfolgerung ("China liegt ein paar Monate hinter dem amerikanischen Frontier"), eine unabhängige Bestätigung derselben Größenordnung aus anderer Quelle.
- **Kein Widerspruch, aber Ergänzung zu [video-summary-4NqKZerJpk8.md](video-summary-4NqKZerJpk8.md):** Dort werden für Qwen 3.8 (2,4 Bio. Gesamt-/95 Mrd. aktive Parameter, 262.144 Context-Token) bereits harte Zahlen dokumentiert und per WebSearch bestätigt — passt zur hier im Video gezeigten "Qwen 3.8 Max"-Variante, ohne dass die Parameterzahl im aktuellen Video selbst genannt wurde.
- **Ablauf-Hinweis:** Kein Whisper-Fallback über Groq/OpenAI, sondern Replicate-Whisper (167 Segmente, deutschsprachig, durchgehend klar verständlich). Alle 80 extrahierten Frames über die volle Videolänge gelesen; Bildmaterial (Benchmark-Screenshots, Preis-Charts, Lizenztext, Bär-Animationen) deckt sich durchgehend mit dem Transkript.
