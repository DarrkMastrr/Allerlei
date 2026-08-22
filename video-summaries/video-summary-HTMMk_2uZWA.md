# "Qwen 3.8 27B gegen Claude: Schlägt das lokale Modell wirklich Opus? Test auf RTX 5090"

**Kanal:** IAmFabian
**URL:** https://www.youtube.com/watch?v=HTMMk_2uZWA
**Länge:** 22:33
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-9lyg9m8D3q0.md](video-summary-9lyg9m8D3q0.md) — dort wurde bereits der große Bruder aus derselben Modellfamilie behandelt (Qwen3.8-2.4T-A95B, Cloud-MoE-Version). Dieses Video testet die kleine, lokal lauffähige Schwester Qwen3.8-27B.*

## Aufhänger und Einordnung des Titels

Fabian zeigt zu Beginn eine Zahl (67,7 gegen 69,2 auf SWE-Bench Pro), stellt aber mitten im Video selbst richtig, dass das die falsche Tabelle war ("Mir ist gerade aufgefallen, die Tabelle ganz am Anfang vom Video, das war die falsche"). Die korrekten Zahlen aus Qwens eigener Modellkarte: SWE-Bench Pro 61,7 Punkte für Qwen3.8-27B. Kernthese des Videos: Die Überschrift "schlägt Claude Opus" ist nicht falsch, aber deutlich übertrieben — Qwen gewinnt nur in einem Teil der Disziplinen, und der Vergleich hinkt beim verwendeten Opus-Modell.

## Was Qwen3.8-27B ist

- Release am selben Tag wie das Video, Gewichte direkt auf Hugging Face verfügbar
- Lizenz: Apache 2.0 — vollständig offen, auch kommerziell nutzbar ohne Rückfrage
- Laut Hugging-Face-Modellkarte (im Frame sichtbar) "28B params" — Fabian rundet im Video durchgehend auf "27 Milliarden" (passend zum Modellnamen "27B"); Whisper transkribierte diese Zahl mehrfach fälschlich als "27 Billion" statt "27 Milliarden" — im Deutschen ist "Milliarde" gemeint, nicht die englische "Billion"/deutsche "Billion" (Billion), was klar ein Transkriptionsfehler ist
- Vier Repos auf Hugging Face: zweimal das kleine 27B, zweimal der "große Bruder" mit 2,4 Billionen (2,4T) Parametern — die Cloud-Variante, die auf keiner normalen Maschine läuft (siehe verlinktes Schwester-Video oben)
- Multimodal: neben Text auch Vision (Bilder, laut Qwen auch stundenlange Videos) über einen eigenen "Vision Tower" — im Video nicht weiter getestet, nur die Architektur gezeigt

## Architektur (per HF-Diagramm-Tool "HF Viewer")

- Hybrides Aufmerksamkeitsmuster: ein sich wiederholender "Decoder Cycle"-Block aus 3 Layern mit linearer Attention, gefolgt von 1 Layer mit voller Attention, 16-mal wiederholt
- Macht zusammen 48 lineare + 16 volle Attention-Layer = 64 Layer insgesamt
- Begründung im Video: lineare Attention merkt sich nur einen festen Zustand statt bei jedem Wort den kompletten Text neu zu betrachten — dadurch bleibt das Modell auch bei langem Kontext schnell und günstig
- Per Diff-Ansicht (Vergleich Qwen3.6-27B vom Mai gegen Qwen3.8-27B vom August) ist die Architektur laut Fabian 1:1 identisch geblieben — einziger Unterschied zwischen den Versionen seien die Trainingsdaten

## Die Benchmark-Zahlen und der Haken

- SWE-Bench Pro (echte Bugfixes in echten Repos): Qwen3.8-27B 61,7 Punkte, verglichen mit Claude **Opus 4.6** (laut Fabian aus Februar, also mehrere Monate alt)
- LiveCodeBench: 90,3 (Qwen) gegen 88,8 (Opus 4.6) — knapp vorne
- Terminal-Bench: 73 (Qwen) gegen 78 (Opus 4.6) — hier liegt Opus vorne, also kein pauschaler Sieg auf ganzer Linie
- Wichtige Einschränkung, die Fabian explizit hervorhebt: Qwen hat alle Zahlen selbst gemessen, auch die der Konkurrenz, und laut Fußnote im eigenen Benchmark sogar Testaufgaben selbst korrigiert — unabhängige Nachmessungen fehlten zum Videozeitpunkt
- Fabian zitiert Hacker-News-Kommentare, die "Benchmaxing" (Überoptimierung auf Testaufgaben) unterstellen und behaupten, im echten Alltag schlage das Modell Opus in keiner Weise
- Zusätzlicher Kritikpunkt: Opus 4.6 ist bereits das Vergleichsmodell aus Februar; neuere Versionen (Opus 4.7, 4.8, "Opus 5") existieren laut Fabian schon und liegen klar davor — der Vergleich nutzt also bewusst oder unbewusst ein älteres Anthropic-Modell

## Praxistest 1: Snake-Spiel (Python/Pygame) auf gemieteter RTX 5090

- Fabian mietet für den Test eine RTX 5090 bei RunPod (Cloud, nicht eigene Hardware) per SSH
- Erster Anlauf scheiterte: das Modell lief komplett auf der CPU statt auf der gemieteten GPU (Fabian musste die Session neu starten) — dieser Stolperstein soll in einem Setup-Folgevideo genauer erklärt werden
- Nach dem Fix: voll funktionsfähiges Snake-Spiel nach mehreren Denk-/Korrekturrunden, Gesamtdauer 1:47 min bei 75,5 Token/s, ca. 8.000 Token (inklusive Reasoning/Thinking)

## Praxistest 2: Physik-Simulation (hüpfende Bälle, HTML/CSS/JS) — Thinking-Modus-Fallstrick

- Vorgängermodell Qwen3.6-27B hatte laut Fabian im Snake-Test am besten abgeschnitten, bei einer Physik-Simulation aber als einziges Modell versagt (chaotische, unnatürliche Bewegungen)
- Mit Standard-Denkmodus (höchste Stufe) plant sich Qwen3.8-27B bei dieser offenen Aufgabe "zu Tode": 3:39 min reines Nachdenken, 16.000 Token, Abbruch mitten im Satz ohne fertigen Code — weil der Kontext auf einer einzelnen RTX 5090 bewusst auf ca. 20.000–30.000 Token begrenzt wurde (der volle Kontext von ca. 200.000 Token passt laut Fabian nicht auf eine einzelne 5090)
- Mit komplett ausgeschaltetem Denkmodus: fertiges, funktionierendes Ergebnis nach 1:47 min
- Ergebnis optisch überzeugend (Gravitations-/Luftwiderstands-Regler, Reset, Burst-Funktion), aber physikalisch nicht perfekt — Bälle prallen nicht immer sauber voneinander ab, werden teils oval, drehen sich unnatürlich
- Fabians Einschätzung trotzdem positiv: für ein lokales Modell, das z. B. offline im Flugzeug läuft, "eine Waffe"

## RTX 5090 vs. Mac Mini M4 Pro — eigenes Messwerte-Dashboard

Fabian hat die Zahlen in einem separaten Dashboard ("Qwen3.8-27B selbst gemessen", datiert 14.08.2026) aufbereitet. Wichtig für den Hardware-Vergleich: unterschiedliche Quantisierung auf beiden Maschinen (RTX 5090: Q4_K_M über Ollama; Mac Mini M4 Pro: MLX 8-Bit über mlx-vlm) — kein 1:1-fairer Vergleich, da der Mac in höherer Genauigkeit rechnet.

| Metrik | RTX 5090 (32 GB, Q4) | Mac Mini M4 Pro (48 GB, 8-Bit) | Faktor |
|---|---|---|---|
| Schreibgeschwindigkeit (Token/s, über 4 Kontextgrößen) | ~79,3 → 75,5 (bleibt stabil) | ~8,4 → 8,1 (auch stabil, aber langsam) | ca. 9,5x |
| Lesegeschwindigkeit / Prompt-Verarbeitung (Token/s) | 489 → 4.066 | 58 → 92 | ca. 40x |
| Time-to-first-token bei großem Prompt | 3,4 s | 90,3 s | ca. 26x |
| Speicherbelegung | 19,6 / 32 GB (61 %) | 40,1 / 48 GB (84 %) | — |

Fabians Fazit-Folie: "Schreiben kann der Mac. Lesen nicht." — die Karte schreibt 9,5x schneller, liest aber sogar 40x schneller ein, was gerade beim Programmieren (viele Dateien einlesen) den entscheidenden Unterschied macht. Die stabile Schreibgeschwindigkeit über wachsenden Kontext hinweg wird explizit auf die 48 linearen Attention-Layer zurückgeführt.

## VRAM-Empfehlungen für eigene Hardware

Aus dem Video (Unsloth-GGUF-Seite als Quelle genannt, "ANSLOV" im Transkript ist ein Whisper-Fehlhörer für "Unsloth"):
- RTX 3090/4090 (24 GB): komfortabel, Q4-Format mit rund 15 GB passt locker
- Ab 12 GB VRAM: läuft noch, aber mit stärkerer Komprimierung und spürbarem Qualitätsverlust, besonders beim Programmieren
- Unter Q4-Quantisierung zu gehen spart zwar weiter Speicher, führt laut Fabian aber zu echten Fehlern im Output — davon rät er ab

## Kosten

- RunPod-Miete für die RTX 5090: 0,69 $/Stunde (Community Cloud) — Fabian: "ungefähr ein Kaffee für den ganzen Abend basteln"
- Kernargument: zum Ausprobieren muss man sich keine 3.000–4.000-€-Karte kaufen, sondern kann stundenweise testen, bevor man sich für einen Kauf entscheidet

## Datenschutz und Herkunft

- Ausdrücklich als chinesisches Modell von Alibaba benannt
- Vorteil beim lokalen Betrieb: Gewichte liegen komplett auf der eigenen Platte, es geht nichts nach außen — datenschutztechnisch laut Fabian "das Beste, was geht"
- Verhalten bei politisch heiklen Fragen wurde von Fabian ausdrücklich noch nicht getestet, soll aber noch untersucht werden

## Fazit des Hosts

Starkes Modell, "die Codingzahlen sind kein Fake mehr", aber die reißerische Überschrift ("schlägt Claude") stimmt so nicht — es gewinnt nur in einem Teil der Disziplinen gegen ein bereits älteres Opus-Modell, und die Zahlen sind selbstgemessen. Überzeugt haben Fabian dagegen die eigenen, unabhängig gemessenen Werte: knapp 80 Token/s auf der RTX 5090, stabil auch bei vollem genutztem Kontext. Empfehlung: ab 24 GB VRAM oder stundenweise Cloud-Miete lohnt sich der Einsatz; auf dem Mac Mini M4 Pro mit 8 Token/s dagegen "kein Spaß" — hier werden aber noch optimierte MLX-Quantisierungen erwartet, die laut Fabians Einschätzung 30–40 Token/s bei akzeptabler Qualität bringen könnten. Ein Folgevideo zum kompletten Selbst-Setup (inkl. des CPU-statt-GPU-Stolpersteins) ist angekündigt.

---

## Kernbotschaft

Qwen3.8-27B ist ein am Erscheinungstag als Apache-2.0-Open-Weights veröffentlichtes, multimodales 27B/28B-Parameter-Modell mit einer hybriden Attention-Architektur (48 lineare + 16 volle Attention-Layer), die auf einer einzelnen RTX 5090 (32 GB VRAM, gemietet für 0,69 $/Stunde) rund 80 Token/s bei stabiler Geschwindigkeit über wachsenden Kontext liefert — ein Mac Mini M4 Pro mit 48 GB Unified Memory ist dabei nur beim Lesen von Kontext bis zu 40x langsamer. In Qwens eigenen Benchmarks schlägt das Modell Claude Opus 4.6 in einem Teil der Disziplinen (SWE-Bench Pro, LiveCodeBench), verliert aber in anderen (Terminal-Bench) — und da Opus 4.6 bereits mehrere Monate alt ist und die Zahlen komplett selbstgemessen sind, relativiert der Host die reißerische "schlägt Claude"-Überschrift deutlich, ohne die grundsätzliche Stärke des lokal lauffähigen Modells infrage zu stellen.

## Themen-Tags

Qwen, Qwen3.8-27B, Alibaba, Lokale KI, Open Weights, Apache 2.0, RTX 5090, RunPod, Cloud-GPU-Miete, VRAM, Mac Mini M4 Pro, MLX, Ollama, Benchmarks, SWE-Bench Pro, Claude Opus 4.6, Hybrid Attention, Linear Attention, Quantisierung, Coding-Agent, Datenschutz

## Zu prüfen

- **Grundplausibilität per Websuche bestätigt:** Qwen3.8-27B existiert, wurde laut mehreren unabhängigen Quellen am 14.08.2026 von Alibaba veröffentlicht (dense, multimodal, Apache 2.0, nativ 262K Kontext-Token, erweiterbar auf 1M via YaRN, Zielhardware ca. 24 GB VRAM) — Details unter [Qwen/Qwen3.8-27B auf Hugging Face](https://huggingface.co/Qwen/Qwen3.8-27B) und [Alibaba Cloud Community Blog](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463).
- **Architektur-Angabe (48 lineare + 16 volle Attention-Layer, 3:1-Verhältnis, Gated-DeltaNet-Stil) per Websuche bestätigt**, u. a. über [kie.ai-Blogpost](https://kie.ai/blog/qwen-3-8-27b-27b-dense-multimodal-local-model) und [MindStudio-Analyse](https://www.mindstudio.ai/blog/qwen3-8-27b-architecture-benchmarks).
- **SWE-Bench-Pro-Zahl 61,7 für Qwen3.8-27B per Websuche bestätigt**; eine gefundene Quelle nennt für Claude Opus 4.6 "Max" konkret 53,4 Punkte (im Video selbst wurde dieser Opus-Wert akustisch nicht klar genannt/verstanden) — passend zur im Video geäußerten Kritik, dass der Opus-Vergleichswert importiert statt unabhängig nachgemessen wurde. Quelle: [kie.ai-Blogpost zum SWE-Bench-Pro-Vergleich](https://kie.ai/blog/qwen-3-8-27b-release).
- **RunPod-Preis 0,69 $/Stunde für die RTX 5090 (Community Cloud) per Websuche bestätigt** — passt exakt zur im Video genannten Zahl.
- **Nicht unabhängig geprüft:** die konkreten Dashboard-Messwerte (Token/s, Zeit-bis-erstes-Zeichen, Speicherbelegung) stammen aus Fabians eigenem, selbst gebautem Dashboard und wurden nur als Screenshot übernommen, nicht selbst nachgestellt.
- **Terminal-Bench-Zahlen (73 gegen 78) und LiveCodeBench (90,3 gegen 88,8)** stammen ebenfalls aus Qwens eigener Modellkarte/Fußnote — laut Video selbst unabhängig noch nicht nachgemessen; das deckt sich mit dem allgemeinen Befund, dass Qwen alle Vergleichswerte (auch die der Konkurrenz) selbst gemessen hat.
- **Whisper-Transkriptionsfehler:** An mehreren Stellen wurde "27 Milliarden" als "27 Billion" transkribiert (z. B. bei 04:00, 04:34, 13:19) — im Fließtext oben korrigiert. Umlaute erschienen im rohen Transkript teils als Encoding-Artefakte, wurden für die Zusammenfassung normalisiert.
- **Whisper-Fehlhörer "ANSLOV"** ist mit hoher Wahrscheinlichkeit "Unsloth" (bekanntes Open-Source-Projekt für Quantisierung/lokale Modelle, passt zum GGUF-Frame bei ca. 18:57) — im Text oben entsprechend aufgelöst.
- **Querverweis/Ergänzung zu bestehenden Notizen:** [video-summary-9lyg9m8D3q0.md](video-summary-9lyg9m8D3q0.md) behandelt bereits die große MoE-Cloud-Version derselben Modellfamilie (Qwen3.8-2.4T-A95B, 2,4 Billionen Gesamt-/95 Mrd. aktive Parameter) — kein Widerspruch, sondern Ergänzung um die kleine, lokal lauffähige 27B-Variante. [lokale-ki.md](../lokale-ki.md) und [video-summary-qZRftXozT3M.md](video-summary-qZRftXozT3M.md) (VRAM-Faustregeln, Speicherbedarf-Tabellen) liefern zusätzlichen Kontext für die Hardware-Einordnung, ohne inhaltlich zu widersprechen. [fable-5-modell-sperre.md](../fable-5-modell-sperre.md) dokumentiert Anthropics Vorwurf, Alibaba habe Qwen per Distillation aus Claude-Anfragen aufgewertet — passt thematisch zur im Video zitierten "Benchmaxing"-Kritik aus den Hacker-News-Kommentaren, wird im Video selbst aber nicht erwähnt.
- Keine erkennbare Sponsoring-/Werbekennzeichnung im Video (im Unterschied zum bereits im Repo vorhandenen Higgsfield-Video desselben Kanals) — wirkt wie eine redaktionelle Eigenrecherche, nicht wie ein bezahltes Werbevideo.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; die Zusammenfassung basiert auf dem Whisper-Fallback (Replicate, 426 Segmente) plus 80 Frames über die volle Videolänge.
