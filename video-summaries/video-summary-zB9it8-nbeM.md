# "Claude Fable 5.1 getestet"

**Kanal:** AI mit Arnie
**URL:** https://www.youtube.com/watch?v=zB9it8-nbeM
**Länge:** 25:35
**Zusammenfassung erstellt:** 2026-09-08

---

*Siehe auch: [fable-5-modell-sperre.md](../fable-5-modell-sperre.md) für den Vorgänger Fable 5/Mythos 5 (Export-Sperre Juni/Juli 2026), [video-summary-cse3QV90YpE.md](video-summary-cse3QV90YpE.md) und [video-summary-AOgUqb62WUQ.md](video-summary-AOgUqb62WUQ.md) für weitere Fable-5.1-Erwähnungen.*

Arnold (Kanal "AI mit Arnie", im Video per Claude-Begrüßung "Good afternoon, Arnold" bildlich bestätigt) testet das frisch gelaunchte Claude Fable 5.1 anhand eigener Standard-Benchmarks, ordnet die offiziellen Anthropic-Benchmarks ein und rechnet die Kosten gegen die Konkurrenz (GPT-5.6 Sol, Grok 4.6) durch. Jeder gezeigte Modelltest sei laut Host bewusst ein einziger Prompt ohne Nachjustieren gewesen, um fair zu vergleichen.

## Verfügbarkeit und Zugriff

- Nutzbar in Claude (Chat und Cowork) — dort ist Fable 5.1 auf **Medium** die neue Standardeinstellung.
- In Claude Code ist Fable 5.1 auf **High** die Standardeinstellung.
- **Nicht verfügbar in den kleinsten Abo-Plänen** (20-€-Plan) — dort nur gegen zusätzlichen API-Preis nutzbar. Erst ab dem 100-€-Plan aufwärts ohne Zusatzkosten. Der Host kritisiert das ausdrücklich als "nervig" — er hätte sich zumindest eingeschränkten Zugriff für alle Plan-Stufen gewünscht.
- Auch in Cursor integriert (direkt auswählbar) sowie ganz normal über die API.
- Eigene Tests liefen im Terminal (Claude Code) auf einem 200-€-Plan.

## Test 1: ARES-4-Katastrophenroboter-Simulator

Wiederkehrender eigener Test des Kanals (Web-Robotersimulator mit Lauf-, Scan-, Greif- und Failure-Modus, im Frame sichtbar als "ARES-4 Disaster Rescue Mission"). Verglichen: Fable 5.1, Fable 5, GPT-5.6 Sol.

- Laut Host **bisher das mit Abstand beste Ergebnis, das er je in diesem Test bekommen hat** — Fable 5 lag bislang auf Platz 2.
- Beinbewegung/Höhenanpassung: Beine kehren bei Fable 5.1 zuverlässig in Neutralstellung zurück, wirken bei Drehungen deutlich geschmeidiger als bei Fable 5 (dort "starrer").
- GPT-5.6 Sol schneidet im direkten Vergleich klar schlechter ab: Roboter "versinkt im Boden", Kippbewegungen ergeben keinen Sinn, Füße "fliegen umher". Auch bei der Greifzangen-Logik (Open/Close Claw) hat GPT-5.6 Sol Aussetzer, während Fable 5 das laut Host fair betrachtet ebenfalls gut hinbekommen hat.
- Autonomer Modus, Debug-Wireframes, Sensor-Anzeige und Drohnen-Kamerafeed (inkl. Lichtreflexionen) funktionieren nach Hosts Einschätzung "auf einem komplett neuen Level".
- Fazit des Hosts zu diesem Test: Er ist sich nicht sicher, ob dieser eigene Benchmark mit einem zukünftigen Modell noch spürbar besser ausfallen kann — der Test sei damit fast "ausgereizt".

## Test 2: Spiele- und Kreativ-Demos

- **Eigener Nachbau von Super Mario Bros. (Welt 1-1)** per One-Shot-Prompt: Host hat die komplette Welt durchgespielt — Physik, Blockverhalten (Pilz-Block, Münzblock, Sprungphysik mit Schwung-Notwendigkeit), Gegner-Kollision funktionierten laut ihm "eins zu eins" wie in Kindheitserinnerung.
- **Fremdbeispiele von X (nicht selbst nachgetestet, nur eingeordnet):**
  - Ein Ego-Shooter, laut Post-Text mit nur 3 Prompts gebaut, kostete ca. 200 $ (API-Preis; bei Abo-Nutzung stark subventioniert).
  - Ein GTA-artiges Spiel — sieht laut Host optisch gut aus, aber Interaktionen wirken noch nicht vollständig stimmig; wurde nach Einschätzung des Hosts mit mehreren Prompts iterativ erstellt, nicht One-Shot.
  - Ein Halloween-/Konzert-Video, das laut Post rein aus Code generiert wurde ("having a ton of fun with is generating videos through code").
- **Eigener Test:** Foto eines Zimmers hochgeladen, Claude sollte per Code eine begehbare 3D-Rekonstruktion des Raums bauen — laut Host funktionierte das "relativ gut", auch wenn ein paar Details nicht perfekt saßen; insgesamt einer der besten Modell-Outputs, die er bisher gesehen hat.
- **Warnung des Hosts:** Auf X kursieren viele Beschwerden, dass man bei diesen kreativen Aufgaben sehr schnell in Nutzungslimits läuft. Eigene Anekdote: Auf **Ultra Code** hochskaliert hat ein einzelner Test 3,5–4 Stunden gelaufen, ohne fertiges Ergebnis, und den kompletten Plan/das Limit gesprengt — ausdrückliche Empfehlung, **Ultra Code nicht zu verwenden**.

## Fable 5.1 vs. Mythos 5.1 — dasselbe Modell, unterschiedliche Schutzstufen

Laut eingeblendetem Anthropic-Blogpost ("Claude Fable 5.1 and Mythos 5.1"):

- Fable 5.1 und Mythos 5.1 sind **exakt dasselbe Modell**, unterscheiden sich nur in den Safeguards. Fable 5.1 ist allgemein verfügbar, Mythos 5.1 nur über geprüfte Zugangsprogramme (u. a. für Cybersecurity- und Life-Sciences-Anwendungen).
- Wer Fable 5.1 nutzt, wird bei bestimmten Anfragen automatisch auf ein schwächeres Modell umgeleitet bzw. abgeblockt (z. B. Fragen zu Biologie/Cybersecurity). Eigener Test des Hosts mit einer Mitochondrien-Frage wurde tatsächlich blockiert — trotz Anthropics Angabe, die Blockquote gesenkt zu haben, empfindet der Host das noch als zu aggressiv.
- Anthropic nennt in der System Card (dort eingeblendet, S. 160–180) auch Fortschritte in Molekulardesign/Wissenschaft (Protein-Binder-Design mit ~50 % Trefferquote über 12 Ziele, deutlich über dem branchenüblichen 10–15 %) sowie verbesserte Chemical/Biological- und Cyber-Risk-Evaluationen.

## Preise und Kosten

- **API-Basispreis unverändert** gegenüber Fable 5: gleicher Preis für Input- und Output-Token wie beim Vorgänger.
- **Cache-Reads werden günstiger:** neu ca. ein Viertel des bisherigen Preises (laut Anthropic 75 % billiger) — relevant vor allem bei agentischer Arbeit (z. B. Claude Code, wo der System-Prompt ständig neu gecacht gelesen wird). Cache-**Writes** bleiben unverändert teuer.
- Anthropics eigene Angabe: **25 % günstiger** bei normalen Aufgaben, bis zu **45 % günstiger** bei stark agentischen Aufgaben (bezogen auf die API). Der Host bestätigt das nur eingeschränkt: Abo-Nutzer merken laut ihm keinen Unterschied (gleicher Token-Verbrauch), nur API-Nutzer profitieren spürbar.
- **Cost-per-Task (Artificial Analysis, Screenshot):** Fable 5.1 auf Max verbraucht laut gezeigtem Chart ca. 3,69 € pro Aufgabe — teurer als Fable 5 in denselben Aufgaben und fast viermal so teuer wie GPT-5.6 Sol (unter 1 $ pro Aufgabe), weil Fable 5.1 auf Max sehr viele Output-Token generiert (im Video genannt: 45.000 Token vs. 21.000 Token bei GPT-5.6 Sol für dieselbe Aufgabe).
- **CursorBench 3.2 (Screenshot):** Fable 5.1 führt bei Extra-High/Max mit dem laut Host bisher höchsten je erreichten Wert (73,4 %). Bei den Standardeinstellungen (High) liegt Fable 5.1 bei ca. 69,4 % für 4,80 €, während Grok 4.6 auf Extra High mit 70,8 % für 2,81 € ähnlich gut, aber deutlich günstiger abschneidet. Erst auf Extra High/Max wird Fable 5.1 klar besser als die Konkurrenz — kostet dann aber auch deutlich mehr.
- **Intelligenz-gegen-Kosten-Chart (Artificial Analysis):** Auf **Medium**-Einstellung liegt Fable 5.1 laut Host kostenmäßig etwa gleichauf mit GPT-5.6 Sol und Grok 4.6 bei vergleichbarer Intelligenz — die Aussage "jede Einstellung ist unglaublich teuer" stimmt laut Host also nicht pauschal.
- **Abo-Limits:** Aktuell laut Host ca. 17 % weniger Nutzungslimit als noch vor einigen Wochen (Anthropic hatte eine 50-%-Bonusaktion laufen, die wieder zurückgenommen wurde).

## Data Retention und EU AI Act

- Neues **Enterprise Frontier Safeguards (EFS)**-System: Zero-Data-Retention-Option, Daten bleiben in kundenkontrollierter Cloud-Infrastruktur statt bei Anthropic. Rollout in Phasen, ab Herbst 2026 breiter verfügbar (laut Blogpost-Screenshot).
- Bisher habe Anthropic laut Host Chats bis zu 30 Tage einsehen/behalten können (auch bei Unternehmenskunden) — daran werde nun gearbeitet.
- **Wasserzeichen wegen EU AI Act:** Seit ca. 2–3 Wochen (Stand Video) fügt Claude allen Ausgabetexten laut Anthropic-Blogpost ein unsichtbares numerisches Wasserzeichen hinzu, um die Herkunft nachweisbar zu machen (Detection-API für berechtigte Stellen wie Regulatoren, Strafverfolgung, Medien, Forschung).

## Offizielle Anthropic-Benchmarks (eingeblendet)

- **Terminal-Bench-Science:** Fable 5 lag in bester Einstellung bei ca. 25 %, Fable 5.1 auf Max bei **52,6 %** — sogar Fable 5.1 auf Low schlägt laut Chart Fable 5 auf High/X-High/Max.
- **Agentic Terminal Coding:** ähnlich großer Sprung von 5 auf 5.1.
- Im Vergleich zu GPT-5.6 Sol laut Host der größte Sprung bei wissenschaftlicher Recherche (mehr als doppelte Performance) und bei agentischem Coding; bei anderen Kategorien nur noch geringe Unterschiede.
- **Auffällige Ausreißer nach unten:** Auf **DeepSWE** erreicht Fable 5.1 nur 67,4 % (andere Modelle teils über 70 %) und auf **FrontierCode Extended** wird das Modell mit steigendem Thinking-Effort sogar schlechter. Anthropics eigene Erklärung laut Video: Das Modell sei so gründlich, dass es "über das Ziel hinausschießt" (Over-Engineering/übermäßige Validierung).
- **Artificial-Analysis-Intelligenz-Index:** Fable 5.1 Max auf Platz 1 (66 Punkte), dahinter Grok X-High, dann Opus 5.1 High, danach wieder ein Fable-5.1-Modell. Unter den ersten 11 Plätzen ist Anthropic laut Host 7-mal vertreten.

## Randnotizen aus dem News-Teil

- **Grok:** Host würde Grok 4.6 auf Basis dieser Benchmarks (v. a. Cursor Bench) nicht unterschätzen — v. a. bei Kosten/Leistung führend. Persönliche Erfahrung des Hosts weicht aber leicht ab: er bevorzugt in der Praxis eher GPT-Modelle, trotz schlechterer Benchmark-Werte — als Reminder, dass Benchmarks nicht alles sind. Auf X kündigt Elon Musk (Screenshot) Grok 4.7 "in 10 Tagen" an.
- **OpenAI-Modelle werden aus Cursor entfernt**, nachdem SpaceX Cursor/Anysphere übernommen hat (siehe bereits im Repo dokumentiert, [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md)) — OpenAI misstraut laut Host offenbar Elon Musk. Cursor kontert, nur 5 % der Nutzung kämen ohnehin von OpenAI-Modellen; OpenAI hält dagegen, das sei wegen höherer Token-Effizienz ihrer Modelle irreführend gemessen.
- **GPT Astra (OpenAI):** Blogpost "Path to Astra: critical capabilities and frontier safeguards", datiert 1. September 2026, im Frame gezeigt — passt zu bereits im Repo dokumentiertem Material ([video-summary-AOgUqb62WUQ.md](video-summary-AOgUqb62WUQ.md)).
- **Gemini 3.8 Flash / 3.8 Flash Cyber** (Google) kurz gezeigt und in die Kosten-Leistungs-Grafik eingeordnet — Host hat sich das Modell zum Aufnahmezeitpunkt noch nicht im Detail angesehen.

## Fazit des Hosts

Laut eigenen Tests aktuell das beste verfügbare Modell — aber auf den hohen Einstellungen (v. a. Ultra Code) sehr teuer und tokenhungrig. Bei High/Medium/Low bekomme man ein sehr starkes, noch kostenerträgliches Modell. Kritikpunkt bleibt die fehlende Verfügbarkeit in kleinen Abo-Plänen.

---

## Kernbotschaft
Claude Fable 5.1 setzt sich laut Host in eigenen praktischen Tests (Robotersimulator, Spiele-Nachbau, 3D-Raumrekonstruktion) klar von Fable 5 und GPT-5.6 Sol ab und führt auch in mehreren unabhängigen Benchmarks (Artificial Analysis, CursorBench) das Feld an — dieser Vorsprung wird aber auf den höchsten Effort-Einstellungen (X-High/Max, insbesondere Ultra Code) durch sehr hohen Token-Verbrauch und entsprechend hohe Kosten erkauft, während günstigere Cache-Reads (–75 %) vor allem agentischen API-Workloads zugutekommen. Auf mittleren Einstellungen ist das Modell laut Host dagegen kostenmäßig konkurrenzfähig zu GPT-5.6 Sol und Grok 4.6 bei vergleichbarer Intelligenz — die Wahl der Effort-Stufe ist damit der entscheidende Kostenhebel, nicht das Modell an sich.

## Themen-Tags
Claude Fable 5.1, Claude Mythos 5.1, Anthropic, Benchmarks, API-Preise, Cache-Pricing, CursorBench, Terminal-Bench-Science, DeepSWE, Enterprise Frontier Safeguards, EU AI Act Wasserzeichen, Grok 4.6, GPT-5.6 Sol, GPT Astra, Gemini 3.8 Flash, Claude Code, Ultra Code

## Zu prüfen
- **Verhältnis zu [fable-5-modell-sperre.md](../fable-5-modell-sperre.md):** Jene Datei dokumentiert die Export-Kontroll-Sperre von **Fable 5/Mythos 5** (Juni/Juli 2026) — ein anderes, vorheriges Ereignis. Dieses Video behandelt den **Nachfolger Fable 5.1/Mythos 5.1** (Launch Anfang September 2026). Kein Widerspruch, aber wichtig für Leser: nicht verwechseln, unterschiedliche Modellversionen mit demselben Namensschema (öffentlich zugängliches "Fable" vs. eingeschränktes "Mythos").
- **Plausibilitätscheck per WebSearch durchgeführt, Kernaussagen bestätigt:** Launch von Fable 5.1/Mythos 5.1 real und auf Anfang September 2026 datiert (u. a. VentureBeat, Neowin, tech-insider.org). Preis $10/$50 pro Mio. Input/Output-Token bestätigt, ebenso die 75 %-Senkung bei Cache-Reads (VentureBeat: "arrive with a 75% cost reduction for Fable cache reads") — deckt sich exakt mit dem Video und mit der bereits im Repo vorhandenen Notiz [video-summary-cse3QV90YpE.md](video-summary-cse3QV90YpE.md).
- **CursorBench-Zahlen per WebSearch groß bestätigt:** Fable 5.1 führt mit 73,4 % (Max), Grok 4.6 bei Extra High mit 70,8 % für 2,81 $/Aufgabe. Die im Video genannten Zahlen für die High-Einstellung (69,4 % / 4,80 €) konnten nicht separat gegengeprüft werden (Suchergebnisse nennen primär die Extra-High/Max-Werte) — vermutlich korrekt, da die übrigen Zahlen exakt stimmen, aber nicht 1:1 verifiziert.
- **Nicht verifiziert, nur aus dem Video übernommen:** genaue Cost-per-Task-Werte aus dem Artificial-Analysis-Screenshot (3,69 € für Fable 5.1 Max, Token-Zahlen 45.000 vs. 21.000), DeepSWE-/FrontierCode-Ausreißer-Werte, sowie sämtliche X/Twitter-Beispiele (Ego-Shooter für 200 $, GTA-artiges Spiel, Halloween-Musikvideo) — das sind Fremdbeispiele Dritter, vom Host selbst nicht nachgeprüft und hier entsprechend nur als "laut Post" wiedergegeben.
- **Grok-4.7-Ankündigung** ("in 10 Tagen", Elon Musk auf X, Stand Aufnahmezeitpunkt Anfang September 2026) ist eine Zukunftsankündigung zum Aufnahmezeitpunkt — zum Zeitpunkt dieser Zusammenfassung (2026-09-08) nicht separat verifiziert, ob das Modell inzwischen erschienen ist.
- Keine inhaltlichen Widersprüche zu bestehenden Repo-Notizen gefunden — das Video bestätigt und ergänzt vorhandene Punkte zu Fable 5.1 (Preisstruktur, Cache-Rabatt, Mythos-Beziehung) eher, als sie zu widerlegen.

## Für den technischen Team-/Gruppenleiter
Direkt praxisrelevant: Die Effort-Stufe (Low/Medium/High/X-High/Max/Ultra Code) ist der zentrale Kostenhebel — für Teams mit Budgetverantwortung lohnt sich die explizite Empfehlung, **Ultra Code zu meiden** (im Video ein Einzeltest von 3,5–4 Stunden ohne Ergebnis, kompletter Plan gesprengt) und auf Medium/High zu bleiben, wo Fable 5.1 laut den gezeigten Charts kostenmäßig mit GPT-5.6 Sol/Grok 4.6 mithält. Für Planungsentscheidungen relevant: Fable 5.1 ist in kleinen Abo-Stufen (20 €) nicht enthalten — bei Teamausstattung mit knappem Budget also ggf. API-Einzelabrechnung statt Abo-Upgrade prüfen. Die neuen Enterprise Frontier Safeguards (kundenkontrollierte Zero-Data-Retention-Infrastruktur) sind zudem für Unternehmen mit Compliance-Anforderungen (Datenschutz, ggf. auch EU-Kontext) ein potenziell relevanter Prüfpunkt, sobald der Rollout abgeschlossen ist.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429. Der Whisper-Fallback über Replicate stieß bei diesem 25:35 langen Video zunächst zweimal an das 6-Minuten-Poll-Timeout (bekannter Bug bei langen Audiodateien) — erfolgreich gelöst durch manuelles Aufteilen der Audiodatei in 6 Chunks à 300s mit ffmpeg, separate Transkription jedes Chunks über die Replicate-Whisper-API und Zusammenführen mit zeitversetzten Timestamps (482 Segmente gesamt). Alle 80 extrahierten Frames wurden gesichtet.
