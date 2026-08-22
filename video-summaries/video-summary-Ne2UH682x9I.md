# "Wahnsinn: Hermes-Agent + Qwen"

**Kanal:** c't 3003
**URL:** https://www.youtube.com/watch?v=Ne2UH682x9I
**Länge:** 29:14
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [lokale-ki.md](../lokale-ki.md) für das übergeordnete Thema "lokale KI", [video-summary-_Z8W21qUCjo.md](video-summary-_Z8W21qUCjo.md) für eine Hardware-Benchmark-Serie zu lokalen KI-Boxen (DGX Spark/Strix Halo/Mac Studio), sowie [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md), [video-summary-8NSyI-npJCU.md](video-summary-8NSyI-npJCU.md) und [video-summary-4NqKZerJpk8.md](video-summary-4NqKZerJpk8.md) für frühere Hermes-Agent-Erwähnungen im Repo. Details siehe "Zu prüfen".*

## Worum es geht

Moderator ist Jan-Keno Janßen ("Keno", c't 3003 — bestätigt durch im Video sichtbare Terminal-Pfade wie `/home/keno3003` und den Telegram-Bot-Namen "DemKenoSeinHermes"). Das Video ist explizit Antwort auf zwei häufig wiederkehrende Zuschauerwünsche aus den Kommentaren: mehr zu Hermes Agent und mehr zu lokalen KI-Modellen — beide Themen werden hier kombiniert.

Zentrale Demo direkt zu Beginn: Keno zieht sein Internetkabel physisch aus dem Router, während ihm der KI-Agent Hermes live weiter Aufgaben erledigt (Bild im Netz suchen, als Desktop-Hintergrund setzen, Desktop-Umgebung wechseln) — als Beweis, dass das Sprachmodell komplett lokal läuft, ohne Cloud-Anbindung.

## Was ist Hermes Agent?

- Ein KI-**Agent** (nicht nur Chatbot): kann selbst Dinge auf dem Rechner tun statt nur Text/Bilder zurückzugeben — komplette Computerbedienung.
- Kommunikation in natürlicher Sprache, auch per Sprachnachricht, ankoppelbar an Messenger (im Video: Telegram, laut Keno am schnellsten eingerichtet — "drei Sekunden").
- Läuft auf Linux, macOS, Windows; per Kommandozeile oder optionaler grafischer Oberfläche. Keno nutzt im Video primär die CLI und Telegram.
- Funktioniert am besten bei textbasierten/Terminal-Aufgaben; bei grafischen Oberflächen/Websites (Screenshot machen → ans LLM schicken → Klickposition bestimmen) deutlich schwächer und sehr tokenhungrig.
- Entwickelt von **Nous Research** (New York, aus der Krypto-Welt kommend, seit längerem in der lokalen-LLM-Szene aktiv, u. a. mit unzensierten Modellen) — laut Keno noch eine kleine Firma. Open Source, MIT-Lizenz, laut Keno "permanent selbstverbessernd" (merkt sich erfolgreiche Werkzeugaufrufe, baut sich bei Bedarf selbst neue Skills).

## Hermes Agent vs. OpenClaw

Keno vergleicht Hermes explizit mit OpenClaw (das er nach eigener Aussage in einem früheren, hier nicht näher spezifizierten Video schon behandelt hat):

| Aspekt | Hermes Agent | OpenClaw |
|---|---|---|
| Lizenz | Open Source, MIT | Open Source, MIT |
| Autonomie | laut Keno autonomer, bringt Dinge öfter selbstständig zu Ende | öfter manuelles Nachsteuern nötig ("versuch's nochmal") |
| Token-Sparsamkeit | stärker optimiert | weniger optimiert |
| Skills | schreibt sich Skills lieber selbst | mehr vorgefertigte Skills über eigene "ClawHub"-Datenbank |
| Auftreten | "technischer", zeigt Terminal-Aufrufe offen im Messenger | versteckt technische Schritte eher, "cosplayt einen Menschen" |
| Security-Ansatz | von Anfang an mitgedacht (neueres Projekt) | ursprünglich privates Hobbyprojekt ohne Security-Fokus, inzwischen verbessert |
| Interne Technik | nutzt intern bevorzugt Python | eigene, im Transkript unklar wiedergegebene Detailaussage zu Custom-Syntax/Tool-Calling (siehe "Zu prüfen") |

Wichtiger Kontext, den Keno selbst einordnet: OpenClaw-Entwickler **Peter Steinberger** (Österreicher) arbeitet inzwischen bei OpenAI; OpenClaw bleibt offiziell kein OpenAI-Projekt und Open Source, wird von manchen Nutzern seitdem aber skeptischer gesehen. **Per Websuche bestätigt:** Steinberger ist im Februar 2026 tatsächlich zu OpenAI gewechselt, OpenClaw wurde laut mehreren Quellen in eine von OpenAI unterstützte Stiftung überführt und bleibt Open Source.

## Testumgebung und Sicherheitshinweis

- Getestet auf einem **komplett blanken System** (CachyOS/Linux) auf einem Framework Desktop — explizit NICHT auf einem Produktivsystem mit wichtigen Daten, weil Hermes vollen Systemzugriff hat.
- Mehrfach im Video wiederholte Warnung: agentische Systeme mit vollem Zugriff nur auf Rechnern verwenden, bei denen Datenverlust oder Datenabfluss egal wäre — Stichwort **Prompt Injections** (versteckte Anweisungen aus dem Netz). Keno selbst sind im Test keine (bewusst wahrgenommenen) Prompt Injections begegnet.
- Kleinere lokale Modelle wie das hier verwendete 27B-Modell gelten laut Keno als anfälliger für Prompt Injection als große Cloud-Modelle.

## Demos im Video

- **Wetterabfrage** über Telegram — Hermes ruft `curl wttr.in/Hannover` auf und antwortet mit aktuellem Wetter (das Sprachmodell selbst hat kein Internet, Hermes als Agent schon — Kombination aus lokaler "Intelligenz" und Internetzugriff über den Agenten).
- **Mitarbeiterschulung/Compliance-Test** (Multiple-Choice-Fragen auf einer externen Website) automatisiert durchgeklickt — funktionierte am Ende, aber sehr umständlich: durch die screenshot-basierte Websiteanalyse lief der Kontextspeicher ständig voll und musste wiederholt komprimiert werden (im Frame sichtbar: "Session compressed 11 times"), wodurch Hermes teils von vorn ansetzte.
- **Musikgenerierung + Sonos-Wiedergabe**: "Installiere ACE-Step zur Musikgenerierung, generiere ein Lied über fliegende Oktopusse und spiel das auf meiner Sonos-Box ab" — ohne weitere Detailangaben fand Hermes die Sonos-Box im Netzwerk und erledigte die komplette Kette selbstständig.
- **Browser-Spiele selbst gecodet**: ein Schneemann-Shooter ("Warmwasser-Schneemänner zum Schmelzen bringen") und ein "3003 Cyber Run"-Autospiel; Soundeffekte dafür lokal generiert mit einem im Transkript unklar wiedergegebenen Tool ("Hardmula", vermutlich Whisper-Fehlhörung eines realen Audio-Tools), ohne dass Keno das Tool selbst installiert hatte.
- **Desktop-Wallpaper generieren und setzen**: Bildgenerierung lokal über ComfyUI + das Bildmodell Flux (z. B. ein Oktopus-Motiv), automatisches Setzen als Hintergrund — inkl. sichtbarem Gefrickel mit KDE/Wayland-Eigenheiten.
- **Desktop-Umgebung wechseln** (KDE → Cosmic) auf CachyOS — lief laut Keno "nur so halb gut", am Ende aber erfolgreich.
- **Hannover-Sehenswürdigkeiten-Liste**: Hermes liefert 20 kuriose "Geheimtipps" für Hannover (u. a. "Leibnizens letzter Hausschuh", "Hannovers erste Telefonzelle in einer Hauswand", "Das grüne Herz" aus recycelten Fahrrädern). **Keno bestätigt im Video selbst explizit, dass jeder einzelne Punkt zu 100 % halluziniert ist** — bewusst als unterhaltsames Negativbeispiel für die Halluzinationsneigung kleiner lokaler Modelle ohne Internetzugriff gezeigt.
- **Sprachgefühl schwächer als bei großen Cloud-Modellen**: Anekdote, bei der Hermes/Qwen eine unbeholfene Formulierung ("timings sie selbst") mit "das war schwul formuliert" kommentiert (regionaler/generationstypischer Slang für "umständlich/schlecht", von Keno direkt hinterfragt: "wie schwul?") — vom Modell selbst korrigiert zu "schlecht ausgedrückt". Zeigt vor allem: kleinere lokale Modelle kommunizieren merklich unnatürlicher als große Cloud-Modelle.

## Hardware- und Modellwahl

- **Sweet Spot laut Keno:** Qwen3.6, 27 Mrd. Parameter, 4-Bit-Quantisierung (Gewichte ca. 17 GB). **Per Websuche bestätigt:** Qwen3.6-27B ist ein am 22. April 2026 von Alibabas Qwen-Team veröffentlichtes, dichtes ("dense") Open-Weight-Modell unter Apache-2.0-Lizenz, das laut Herstellerangaben auf mehreren Coding-/Agenten-Benchmarks sogar größere MoE-Modelle (397B Parameter) übertrifft — passt zur im Video gezeigten Hugging-Face-Modellseite (Lizenz, Downloadzahlen, "quantized_by: Unsloth").
- Getestet auf drei Rechnern: Framework Desktop (128 GB Unified Memory, AMD Strix Halo/Ryzen AI Max+ 395), Gaming-PC mit RTX 4090, MacBook Air M2 (24 GB Unified Memory). Qwen lief dabei vom RTX-4090-PC (der bei ihm zufällig unter Windows lief) über Netzwerk zum Linux-Hermes-Rechner — "Linux wird von Windows gesurft".
- Faustregel: ca. 24 GB schneller Speicher nötig (idealerweise GPU-Speicher) für Modell + Kontext + Puffer; läuft auch auf 32 GB normalem DDR5-RAM, dann aber "extrem lahm". Auf dem MacBook Air M2 nur mit max. 16K Kontext praktikabel — für Hermes zu wenig (Minimum laut Keno ca. 64K, besser 100K+, bis hin zum von ihm genannten Qwen3.6-Maximum).
- **Eigener Benchmark (llama-bench/llama.cpp)** — konkrete, im Video als Screenshot gezeigte Zahlen:

| Maschine | Prompt-Verarbeitung (pp512) | Token-Generierung (tg128) |
|---|---|---|
| PC mit RTX 4090 (24 GB VRAM + 128 GB DDR5) | 2.985,7 t/s | 47,2 t/s |
| Framework Desktop / Strix Halo (Ryzen AI Max+ 395, 128 GB unified) | 364,0 t/s | 12,2 t/s |
| MacBook Air M2 (24 GB unified) | 41,2 t/s | 3,6 t/s |

  Prompt-Verarbeitung ist rechenlimitiert (RTX-4090-Vorsprung bis 72×), Token-Generierung ist speicherbandbreitenlimitiert (Vorsprung schrumpft auf 3,9–13×). Wichtiger Nebenaspekt, den Keno explizit nennt: die RTX-4090-Maschine zieht im LLM-Betrieb über 500 Watt, der Framework Desktop nur ca. 140 Watt.
- **Praxis-Einstieg:** Ollama installieren → `ollama` auf der Kommandozeile → "Launch Hermes Agent (install)" → als Provider Qwen3.6 wählen (nicht die von Ollama beworbenen Cloud-Abos) — laut Keno "quick & dirty", explizit NICHT der beste Weg, aber der einfachste Einstieg. Für ernsthafte Setups installiert er llama.cpp lieber über einen Coding-Agenten (Claude Code/Codex, alternativ auch GLM 5.2) und lässt diesen automatisch passende Modelle/Quantisierungen recherchieren und gegeneinander benchmarken.
- Empfohlene GGUF-Variante laut "Mainstream-Konsens": UD-Q4_K_XL mit MTP (Multi-Token Prediction, laut im Video gezeigtem Unsloth-Blogpost ca. 1,5–2× schnellere Inferenz ohne Genauigkeitsverlust) — passt inkl. Kontext in 24 GB VRAM. Für multimodale Bildfähigkeiten zusätzlich MMPROJ-Datei von Hugging Face nötig.
- Kurzer Exkurs zu Googles **Gemma 4** (Variante 26B-A4B) auf einer neuen Valve Steam Machine (8 GB GPU + 16 GB RAM) — lief, aber sehr langsam, da nicht komplett in den GPU-Speicher passte; sprachlich etwas besser als Qwen, bei Computerbedienung/Coding aber schlechter — deshalb Fokus im Video auf Qwen.

## Für den technischen Team-/Gruppenleiter

- Konkrete, aktuelle Hardware-Dimensionierungsregel für lokale Agentic-AI-Pilotprojekte: ~24 GB schneller GPU-Speicher als Einstiegspunkt für ein praxistaugliches Modell (Qwen3.6-27B, Q4) mit ausreichend Kontext für agentische Workloads (min. 64K, besser 100K+ Token).
- Klare, direkt in Beschaffungs-/Energiekostenentscheidungen einfließende Zahl: RTX-4090-Setup >500 W vs. Strix-Halo-Mini-PC ~140 W im Dauerbetrieb bei gleichzeitig deutlich geringerem Geschwindigkeitsvorteil bei der Token-Generierung (3,9–13×) als bei der Prompt-Verarbeitung (bis 72×) — relevant für die Frage "eigener Server vs. Mini-PC" je nach Workload-Profil (viele lange Prompts vs. viel Chat-Antwortlänge).
- Praktischer Hinweis, lokale LLM-Serving-Infrastruktur (llama.cpp-Setup, Modell-/Quantisierungswahl) über einen Coding-Agenten recherchieren und benchmarken zu lassen statt manuell — spart Einarbeitungszeit bei einem naturgemäß schnell veraltenden Themenfeld.
- Deutliche, wiederholte Sicherheitswarnung zu vollzugriffsfähigen Agentensystemen: nur auf Systemen ohne kritische Daten einsetzen, Prompt-Injection-Risiko ernst nehmen — direkt übertragbar auf die Frage, ob/wie man solche Agenten im eigenen Team pilotiert (z. B. isolierte Testsysteme statt Produktivumgebung).
- Lokale KI als Compliance-/Datenschutz-Hebel: firmeninterne Workflows (im Video am Beispiel eines Schulungs-/Zertifizierungstests gezeigt) lassen sich ohne Datenabfluss an US-Cloud-Anbieter bearbeiten — relevant für Teams mit EU-Datenresidenz-Anforderungen oder Zertifizierungsauflagen, die Cloud-KI ausschließen.
- Ehrliche Grenze, die der Host selbst mehrfach benennt: kleine lokale Modelle sind noch fehleranfälliger/halluzinationsanfälliger und kommunikativ schwächer als Top-Cloud-Modelle — wichtiges Erwartungsmanagement, bevor man "lokal statt Cloud" im Team als generelle Strategie vorschlägt.

## Werblicher Teil

Ca. 1:56–2:56: NordVPN-Sponsoring (Antivirus-Suite inkl. Darknet-Monitor, Rabattcode "CT3003" für vier Zusatzmonate, 30-Tage-Geld-zurück-Garantie) — im Video klar als Werbung gekennzeichnet. Am Ende Hinweis auf zweiwöchige Sommerpause von c't 3003/Podcast "c't 4004" und Werbung für den kostenlosen Newsletter "c't 3003 Hype".

---

## Kernbotschaft

Keno demonstriert live und mit physisch abgezogenem Internetkabel, dass die Kombination aus dem Open-Source-Agenten Hermes Agent (Nous Research) und dem lokalen 27-Milliarden-Parameter-Modell Qwen3.6 inzwischen praxistaugliche agentische KI auf bezahlbarer, aber nicht billiger Consumer-Hardware ermöglicht — von Musikgenerierung über Smart-Home-Steuerung bis zu selbstgecodeten Spielen, alles ohne Cloud-Anbindung des Sprachmodells. Er ordnet Hermes im direkten Vergleich zum bekannteren OpenClaw ein (autonomer, token-sparsamer, von Anfang an sicherheitsbewusster konzipiert) und liefert einen ungewöhnlich detaillierten technischen Leitfaden zu Hardwareanforderungen, Quantisierung und eigenen Benchmark-Zahlen (RTX 4090 schlägt Strix-Halo-Mini-PC und MacBook Air M2 deutlich, allerdings bei auch deutlich höherem Stromverbrauch). Gleichzeitig bleibt er trotz des reißerischen Titels ungewöhnlich ehrlich: Das Setup ist noch "Rabbit-Hole"-komplex, kleine lokale Modelle halluzinieren nachweislich (100 % erfundene Hannover-"Sehenswürdigkeiten" als Negativbeispiel) und kommunizieren merklich schlechter als Spitzen-Cloud-Modelle — für den Massenmarkt ist das noch nichts, wohl aber für alle, die aus Datenschutz-, Zensur- oder Zuverlässigkeitsgründen (Stichwort Fable-5-Exportkontroll-Sperre) unabhängig von US-Cloud-Anbietern experimentieren wollen.

## Themen-Tags

Hermes Agent, Nous Research, Qwen3.6-27B, OpenClaw, Peter Steinberger, Lokale KI, llama.cpp, Ollama, GGUF-Quantisierung, RTX 4090, Strix Halo/Framework Desktop, MacBook Air M2, Prompt Injection, Agentic AI, c't 3003, Sonos, ComfyUI, Telegram-Bot, Gemma 4, Valve Steam Machine

## Zu prüfen

- **Peter Steinberger/OpenAI-Wechsel und OpenClaw-Foundation-Status:** per WebSearch bestätigt (TechCrunch, Forbes, euronews, alternativeto.net — Steinberger wechselte im Februar 2026 zu OpenAI, OpenClaw wurde laut diesen Quellen in eine von OpenAI unterstützte Stiftung überführt und bleibt Open Source; Steinbergers österreichische Herkunft ebenfalls bestätigt).
- **Qwen3.6-27B Existenz/Specs/Lizenz:** per WebSearch bestätigt (MarkTechPost, Alibaba-Cloud-Blog, offizieller Qwen-Blog — Release 22. April 2026, dense 27B-Modell, Apache-2.0-Lizenz, laut Hersteller-Benchmarks Übertreffen größerer MoE-Modelle bei Coding-/Agenten-Aufgaben).
- **Nous Research als Entwickler von Hermes Agent:** nicht erneut per Websuche geprüft, aber bereits in mehreren anderen Repo-Notizen unabhängig bestätigt (siehe [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md), [video-summary-8NSyI-npJCU.md](video-summary-8NSyI-npJCU.md)) — konsistent mit den Angaben in diesem Video.
- **Cross-Referenz zu [video-summary-_Z8W21qUCjo.md](video-summary-_Z8W21qUCjo.md):** dort wurden "Hermes" und "OpenClaw" bei einem anderen Video nur akustisch erwähnt und ausdrücklich als "nicht per Websuche verifiziert, könnten Whisper-Fehltranskriptionen sein" markiert. **Dieses Video löst die damalige offene Frage auf:** Hermes Agent und OpenClaw sind real existierende, konkurrierende lokale Agentensysteme, keine Fehltranskriptionen.
- **Cross-Referenz zu [lokale-ki.md](../lokale-ki.md):** ergänzt die dortige Übersicht (Odysseus + Gemma als Beispiel) um ein aktuelleres, deutlich detaillierteres Beispiel (Hermes + Qwen3.6 mit konkreten Hardware-/Benchmark-Angaben) — kein Widerspruch, eher Vertiefung.
- **Cross-Referenz zu [video-summary-_Z8W21qUCjo.md](video-summary-_Z8W21qUCjo.md)** (Hardware-Benchmark-Serie DGX Spark/Strix Halo/Mac): dortige Strix-Halo-Zahlen (339,87 t/s pp / 34,13 t/s tg, anderes Modell/Setup) sind nicht direkt mit den hier gezeigten Strix-Halo-Zahlen (364,0 pp / 12,2 tg) vergleichbar — unterschiedliche Modelle, Quantisierungen und Benchmark-Parameter. Kein Widerspruch, aber auch nicht kreuzvalidierbar; auffällig ist vor allem die deutlich niedrigere tg-Zahl hier, könnte am größeren/dichteren Modell (27B dense vs. dort vermutlich kleinere/andere Modelle) liegen.
- **Tool-Name "Hardmula"** für die lokale Soundeffekt-Generierung: Whisper-Transkript unklar, im Frame nicht lesbar/nicht gezeigt — welches reale Tool gemeint ist, wurde nicht identifiziert.
- Die Detailaussage zu OpenClaws interner Technik (ca. Minute 6, Transkript "Cinema-Modell, ONE-WORD-Nexus-Scritten, JavaScript-Geschmacksschrift") ist eine erkennbar unklare Whisper-Transkription — der genaue technische Sachverhalt bleibt offen und wurde in der Tabelle entsprechend vorsichtig/vage wiedergegeben statt spekulativ interpretiert.
- Die 20 "Hannover-Sehenswürdigkeiten" sind laut Video selbst zu 100 % Halluzinationen — bewusst nicht als Fakten übernommen, sondern nur als Demonstrationsbeispiel referenziert.
- Kontextfenster-Maximum von Qwen3.6: Transkript nennt "226.144" Token, was zahlenmäßig ungewöhnlich wirkt (kein typischer Zweierpotenz-Wert). Ein separat im Video gezeigter Frame nennt für die verwandte Qwen3.6-35B-A3B-Variante "262k Kontext (bis 1M erweiterbar)" — 262.144 = 2^18 ist ein typischer LLM-Kontextfenster-Wert. Spricht dafür, dass "226.144" ein Whisper-Zahlendreher ist, aber nicht abschließend im Frame zur 27B-Variante selbst bestätigt — mit Vorsicht zu genießen.
- Eigene Benchmark-Zahlen (RTX 4090/Strix Halo/MacBook Air M2, Stromverbrauchsangaben 500 W/140 W) sind Kenos eigene Messungen mit llama-bench, im Video als Screenshot gezeigt (Parameter `-fa 1 -ngl 99`, MacBook zusätzlich `-ub 32`) — nicht unabhängig nachgestellt, aber methodisch nachvollziehbar dokumentiert.
- Community-Zahlen/Empfehlungen zu weiteren Modellen (Qwen3-Coder-Next, MiniMax-M2.5, GLM-5.1/5.2, Kimi-Linear-480-A3B, MiniMax-M3) stammen aus einem im Video gezeigten Recherche-Chat mit einem Coding-Agenten (Claude Code) — nicht unabhängig gegengecheckt, wirken aber intern konsistent und technisch plausibel begründet.

## Quellen der Plausibilitätschecks

- [TechCrunch — OpenClaw creator Peter Steinberger joins OpenAI](https://techcrunch.com/2026/02/15/openclaw-creator-peter-steinberger-joins-openai/)
- [Forbes — OpenAI Hires OpenClaw Creator Peter Steinberger And Sets Up Foundation](https://www.forbes.com/sites/ronschmelzer/2026/02/16/openai-hires-openclaw-creator-peter-steinberger-and-sets-up-foundation/)
- [euronews — Austrian creator of viral OpenClaw joins OpenAI](https://euronews.com/next/2026/02/16/austrian-creator-of-viral-openclaw-joins-openai-to-build-next-generation-of-ai-agents)
- [MarkTechPost — Alibaba Qwen Team Releases Qwen3.6-27B](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/)
- [Alibaba Cloud Community — Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model](https://www.alibabacloud.com/blog/603063)
- [Qwen Blog — Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b)

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten wiederholt mit HTTP 429 (auch nach mehreren Wartezeiten/Retries). Da der einzelne Replicate-Whisper-Aufruf für die volle 29-Minuten-Datei nach 6 Minuten Poll-Timeout abbrach, wurde die Audiospur eigenständig in 7 Chunks à 280s zerlegt und einzeln über Replicate/Whisper transkribiert (453 Segmente gesamt, Zeitstempel korrekt versetzt). Alle 80 extrahierten Frames wurden gesichtet; bei diesem stark bildschirmlastigen Video (Terminal-Screenshots, Benchmark-Tabellen, Modell-Metadaten, Telegram-Chats) lieferten Frames und Transkript zusammen ein deutlich vollständigeres Bild als jede Quelle allein.
