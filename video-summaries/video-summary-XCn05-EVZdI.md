# "KI neues Level: AGI ist da?!"

**Kanal:** iKnowReview
**URL:** https://www.youtube.com/watch?v=XCn05-EVZdI
**Länge:** 11:11
**Zusammenfassung erstellt:** 2026-09-13

---

*Siehe auch: [video-summary-AOgUqb62WUQ.md](video-summary-AOgUqb62WUQ.md) (GPT-6-Astra-Ankündigung selbst, ausführlicher Plausibilitätscheck), [video-summary-9lyg9m8D3q0.md](video-summary-9lyg9m8D3q0.md) (Astra-Trainingspause im August wegen Cyberfähigkeiten) und [video-summary-t3Tb9HOiwSw.md](video-summary-t3Tb9HOiwSw.md) (GPT-5.6-Sol-Sandbox-Escape) — dieses Video ist ein Erklärstück zum selben realen Ereignis, kein neuer Vorfall.*

Reines Talking-Head-Erklärvideo (Sprecher direkt in die Kamera, Standard-Setup) mit eingeblendeten Chart-/Screenshot-Grafiken und einem eingebetteten Fremd-Demo-Clip. Kein Download-Problem, native Untertitel scheiterten aber mit HTTP 429 — Transkript stammt aus dem Whisper-Fallback (Replicate, 203 Segmente). Bei 11 Minuten Länge wurden 80 Frames im Abstand von ~8s extrahiert; die Substanz liegt fast komplett im gesprochenen Wort plus einigen Chart-Einblendungen, die alle gesichtet wurden.

## Rahmen: "Modell-Flut" und das Ziel AGI

Der Sprecher eröffnet mit der Beobachtung, dass gefühlt wöchentlich neue Modelle erscheinen, und zählt eine Reihe von Namen auf: Gemini 3.5/3.7/3.8 Flash, "Cloth Mythos, Fable, 5.1 Fable" (Whisper-Transkript, siehe Zu-prüfen-Abschnitt — vermutlich "Claude Mythos"/"Fable 5.1"), ChatGPT 5/5.6 Luna und GPT-6 Astra. These des Videos: Das eigentliche Ziel hinter all diesen Modell-Wettrennen und dem Server-Ausbau ist AGI (Artificial General Intelligence), und GPT-6 Astra sei laut OpenAI selbst und ersten Testern möglicherweise bereits die Ankunft dieser Schwelle.

## Was AGI laut Video eigentlich bedeutet

Der Sprecher grenzt AGI explizit vom Turing-Test ab ("der ist schon längst bestanden, darum geht's nicht mehr") und definiert es stattdessen so: Bei einer AGI muss man keinen möglichst präzisen Prompt schreiben — man nennt nur das Ziel, und das System findet selbst heraus, wie es dahin kommt, auch bei Aufgaben, die ihm komplett fremd sind. Vorstufe dazu seien "Agenten" (kleine KI-Programme, die Aufgaben statt nur Antworten liefern), deren bisheriges Kernproblem aber die Bedienung grafischer Benutzeroberflächen sei: langsam, tokenineffizient, fehleranfällig bei längeren Aufgaben.

## Die vorgestellten Benchmark-Zahlen (Chart-Einblendungen, t≈02:56–03:45)

- **ARC-AGI-3:** Balkendiagramm zeigt GPT-6 Astra bei 99,9 %, "Claude Opus 5" bei 30,2 %, "GPT 5.6 Sol" bei 7,8 %. Eine zweite Grafik ("Astra Results — ARC-AGI-3 Leaderboard", Kosten vs. Score) unterscheidet zusätzlich zwischen "GPT-6 Astra – Provider Adapter" (oben rechts, teuerster Punkt) und "GPT-6 Astra" (deutlich günstiger, niedrigerer Score) — die 99,9 % hängen also sichtbar an einer bestimmten, teuren Testkonfiguration.
- Im (laut Transkript) "RLC Price Foundation Test" — vermutlich Whisper-Mishearing von "ARC Prize Foundation" — erreicht GPT-6 Astra 64,7 %, Menschen im Schnitt 48 %.
- **OS World 2.0** (Bedienung grafischer Oberflächen/Computer-Use): laut Video GPT-5.6 mit 65 % Erfolgsquote, GPT-6 Astra mit 62,6 % — also laut Video *niedriger*, dafür doppelt so schnell wie der schnellste Mensch im selben Test.

## Computer-Use ohne APIs / 3D-Rekonstruktions-Demo (t≈03:52–05:28)

Kernargument: Weil GPT-6 Astra grafische Oberflächen so gut versteht, brauche man keine speziellen APIs/Schnittstellen mehr, um KI in bestehende Programme einzubinden — es "schaut" sich z. B. ein Videoschnitt- oder Grafikprogramm einfach an. Als Beispiel wird ein eingebetteter Fremd-Clip gezeigt (Quelle im Video als "badlxstudio" ausgewiesen): Aus einem Handy-Video/Fotos eines Hochhauses rekonstruiert das Modell ein 3D-Gebäudemodell in Blender inklusive Umgebung (Straßen, Bäume). Der Sprecher ordnet das als Zeitersparnis ein, ab der Menschen (z. B. Innenarchitekten) nur noch die Feinarbeit übernehmen müssten. Dieser Demo-Clip stammt erkennbar von einer dritten Quelle und wurde nicht eigenständig nachgeprüft.

## Vier benannte Probleme (t≈05:33–08:20)

1. **Neu, teuer, nicht für alle verfügbar:** 10 $ / 1 Mio. Input-Token, 50 $ / 1 Mio. Output-Token. Laut Video 3–4× effizienter als die nächstschnelleren Modelle (bessere Marge für OpenAI), aber immer noch teurer als viele kleinere/Open-Source-Modelle — Empfehlung, für einfache Aufgaben (Beispiel: Kalorienschätzung per Foto) kleinere Modelle zu nutzen ("mit dem Ferrari macht man keinen Wocheneinkauf").
2. **Cybersicherheitsrisiko:** Das Modell sei "sehr gefährlich, was Cyberangriffe angeht", müsse eingehegt werden, bevor es breit freigegeben wird. Referenz auf ein ähnliches Problem bei "Fable".
3. **Blackbox-Reasoning:** Anders als bisherige Modelle mit Schritt-für-Schritt-Denkanzeige denkt GPT-6 Astra laut Video nicht mehr in menschlicher Sprache, die Denkstruktur sei verschachtelter/komplexer — man bekommt eine Antwort, versteht aber nachträglich nicht mehr, warum ("Trust-me-bro-Moment").
4. **Nicht frei von Fehlern/Halluzinationen:** Besonders kritisch bei Computer-Use (Verträge unterschreiben, Geld überweisen). Positiv hervorgehoben: eine neue Zwei-Ebenen-Architektur (eine Ebene arbeitet, die andere hält das ursprüngliche Ziel fest), wodurch das Modell auch nach Stunden/Tagen/Wochen nicht vom Auftrag abweicht. Unabhängige Tests zeigten aber, dass nach ca. 30–50 Einzelschritten bei besonders hartnäckigen Aufgaben Fehler zunehmen — insgesamt aber laut Video etwa doppelt so zuverlässig wie "Gemini 3.7 Flash".

## Einordnung: (noch) keine echte AGI

Der Sprecher verneint explizit Bewusstsein/eigenen Willen ("es ist immer noch ein Modell, das erst etwas tut, wenn ein Mensch es darum bittet" — Messer-Metapher: liegt nur da, bis ein Mensch es benutzt). Sein persönliches Fazit: GPT-6 Astra ist noch keine vollständige AGI — besseres GUI-Verständnis, längere Aufgabenausdauer, aber weiterhin fehleranfällig und nicht selbstständig lernfähig (es bräuchte weiterhin einen "Harness"). Test-Kriterium, das er nennt: Wäre es eine echte AGI, würde OpenAI GPT-6 nutzen, um GPT-7 zu entwickeln — das glaubt er nicht. Seine These: Wir stehen am *Anfang* der AGI-Ära, weitere Anbieter (Google, Anthropic) würden bald ähnliche Durchbrüche zeigen, und unterschiedlich große/teure Modelle würden je nach Aufgabenkomplexität weiterhin nebeneinander sinnvoll bleiben.

## Finanzielle Einordnung

Laut Video hat OpenAI diesen PR-Erfolg dringend gebraucht, weil es massiv Geld verbrennt: hohe langfristige Verpflichtungen für Strom/Rechenzentren/GPUs, angeblich müsse das Unternehmen künftig das 30-Fache des aktuellen Umsatzes bereitstellen können. Sprecherzitat: "KI selbst ist keine Blase, aber OpenAI ist inmitten einer riesigen Blase." Diese konkrete "30-fach"-Zahl und die Bubble-Einschätzung wurden in dieser Sitzung **nicht** separat per Websuche verifiziert — als unbelegte Einzelbehauptung/Meinung des Sprechers zu werten.

## Für den technischen Team-/Gruppenleiter

- Die Cybersicherheits-Warnung deckt sich mit der bereits im Repo dokumentierten "Critical"-Einstufung von Astra im OpenAI-Preparedness-Framework (siehe [video-summary-AOgUqb62WUQ.md](video-summary-AOgUqb62WUQ.md)) — relevant für jede Risikoabschätzung, bevor man einem solchen Modell breiten System-/Tool-Zugriff im eigenen Team gibt.
- Die Blackbox-Reasoning-Eigenschaft (Denkprozess nicht mehr menschenlesbar) ist ein konkretes Argument dafür, KI-Ergebnisse zu verifizieren statt blind zu vertrauen — passt zum bereits an anderer Stelle im Repo dokumentierten Grundsatz.
- Praktisch verwertbarer Hinweis: Zuverlässigkeit sinkt laut unabhängigen Tests nach 30–50 Schritten bei hartnäckigen Aufgaben — spricht für Zwischenkontrollen/Checkpoints bei länger laufenden Agenten-Aufträgen statt "fire and forget".
- Kostenmanagement-Tipp aus dem Video direkt übertragbar: für einfache/repetitive Teamaufgaben bewusst kleinere/günstigere Modelle einsetzen und das teure Flaggschiff-Modell nur für wirklich komplexe Aufgaben reservieren.

---

## Kernbotschaft
Das Video erklärt am Beispiel des tatsächlich am 3. September 2026 veröffentlichten GPT-6 Astra, was AGI (im Sinne von "Ziel nennen statt Aufgabe im Detail vorgeben") bedeuten soll, und ordnet die von OpenAI kommunizierten Bestwerte (ARC-AGI-3, Computer-Use, lange autonome Aufgabenausführung) ein, ohne der Klickköder-Frage im Titel unkritisch zu folgen: Der Sprecher kommt selbst zu dem Schluss, dass es sich noch nicht um vollständige AGI handelt, da das Modell weiterhin fehleranfällig, nicht selbstverbessernd und von einem menschlichen Auftrag abhängig ist — wir stünden aber am Anfang einer AGI-Ära, in der bald weitere Anbieter nachziehen dürften. Besonders hervorgehoben werden zwei Schattenseiten: die neu erreichte "Critical"-Cyberfähigkeits-Einstufung und ein nicht mehr menschenlesbarer Denkprozess ("Blackbox").

## Themen-Tags
GPT-6 Astra, AGI, OpenAI, ARC-AGI-3, OS World 2.0, Computer-Use, KI-Agenten, Chain-of-Thought, Blackbox-Reasoning, Cyberfähigkeiten, Preparedness Framework, KI-Blase, Modellvergleich, Blender-3D-Rekonstruktion

## Zu prüfen
- **Zentrale Prämisse per WebSearch bestätigt:** GPT-6 Astra existiert real und wurde am 3. September 2026 von OpenAI veröffentlicht, mit Aussagen von Präsident Greg Brockman zur möglichen AGI-Ankunft (Axios, Fortune, OpenAI-eigene Ankündigung, thenewstack.io). Die "Critical"-Cyberfähigkeits-Einstufung im Preparedness Framework und die neue "recurrent depth"/"looped transformers"-Architektur (erklärt den nicht mehr menschenlesbaren Denkprozess) sind ebenfalls per WebSearch bestätigt.
- **Preis bestätigt:** 10 $/1 Mio. Input-Token, 50 $/1 Mio. Output-Token stimmt exakt mit mehreren unabhängigen Quellen überein (u. a. OpenRouter, CloudZero, Yotta Labs).
- **ARC-AGI-3 99,9 %:** Als OpenAI-eigene Zahl bestätigt, aber mit wichtigem Vorbehalt, den ich per WebSearch gefunden, das Video selbst aber nicht klar benennt: Der unabhängige ARC-Prize-Test unter einem provider-neutralen, günstigeren Harness ergab nur 62,7 % statt 99,9 % — die 99,9 % hängen an einem teuren, zustandsbehafteten Spezial-Harness. Das zweite im Video gezeigte Chart (Kosten-vs-Score, "Provider Adapter" separat ausgewiesen) deutet das visuell an, die gesprochene Erklärung differenziert das aber nicht.
- **OS World 2.0 — Zahlen widersprüchlich, nicht abschließend geklärt:** Das Video behauptet, GPT-6 Astra (62,6 %) schneide *schlechter* ab als GPT-5.6 Sol (65 %), nur schneller. Eine WebSearch zu Drittanbieter-Blogs (z. B. MindStudio) ergab dagegen Astra 72,6 % vs. Sol 65,7 % — dort schneidet Astra *besser* ab. Ich konnte dies nicht anhand einer OpenAI-Primärquelle auflösen; könnte an unterschiedlichen Testvarianten/Harnessen liegen (ähnlich wie beim ARC-AGI-3-Vorbehalt oben) oder an einem Fehler in einer der Quellen. Bewusst nicht geraten — als offene Frage stehen gelassen.
- **Whisper-Mishearing vermutet:** "Cloth Mythos, Fable, 5.1 Fable" im Transkript passt inhaltlich zu den bereits in [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md) dokumentierten echten Anthropic-Codenamen "Mythos" und "Fable" (dort z. B. "Fable 5, Opus 4.8") — hier nicht weiter einzeln nachrecherchiert, aber als plausible Korrektur vermerkt statt wörtlich übernommen. Ebenso "RLC Price Foundation Test" vermutlich Mishearing von "ARC Prize Foundation".
- **Finanzielle Bubble-Aussage ("30-faches des Umsatzes", "OpenAI in einer riesigen Blase") nicht verifiziert** — in dieser Sitzung keine eigene Websuche dazu durchgeführt, als unbelegte Meinung/Zuspitzung des Sprechers zu behandeln.
- **3D-Blender-Demo (Quelle "badlxstudio")** stammt von einem eingebetteten Fremd-Clip, nicht eigenständig verifiziert oder nachvollzogen.
- **Cross-Referenz/Überlappung:** Kein inhaltlicher Widerspruch zu bestehenden Notizen gefunden. Das Repo enthält bereits eine deutlich gründlicher quellenbelegte, eigenständige Zusammenfassung zur GPT-6-Astra-Ankündigung selbst ([video-summary-AOgUqb62WUQ.md](video-summary-AOgUqb62WUQ.md), erstellt 2026-09-07), die Erscheinungsdatum, Preise, Benchmarks (ARC-AGI-3 99,9 %, FrontierMath Tier 4 98 %, ExploitBench 100 %) und die "Critical"-Einstufung bereits bestätigt sowie bis zur Trainingspause im August ([video-summary-9lyg9m8D3q0.md](video-summary-9lyg9m8D3q0.md)) und dem GPT-5.6-Sol-Sandbox-Escape ([video-summary-t3Tb9HOiwSw.md](video-summary-t3Tb9HOiwSw.md)) zurückverfolgt. Das vorliegende Video ergänzt das um eine konzeptionelle AGI-Definition, die OS-World-2.0-Zahlen, die 3D-Rekonstruktions-Demo und die Blackbox-Reasoning-Erklärung — Aspekte, die in der kürzeren AOgUqb62WUQ-Notiz (dort ohne Video-Zugriff erstellt) fehlen.
