# "Warum du bei KI nicht mehr mitkommst (und wie du's sofort änderst)"

**Kanal:** Loris Galler
**URL:** https://www.youtube.com/watch?v=SFtiPOTLBHA
**Länge:** 09:44
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [ai-agent-workflow.md](../ai-agent-workflow.md) und [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) — beide behandeln bereits Teile der hier gezeigten "Loop"-Stufe (Boris Cherny) ausführlicher.*

## Der Aufhänger: ein Tweet, den man nicht mehr versteht

Ausgangspunkt ist ein Tweet/Meme ("Reden wir noch über Loops oder sind wir schon bei den Graphen?"), gemeint eher als Insider-Scherz von Peter Steinberger, der sich selbst über das Tempo der KI-Begriffs-Inflation lustig macht. Loris (arbeitet laut eigener Aussage bei "einem der erfolgreichsten Startups Europas", nutzt dort KI, um KI zu programmieren) leitet daraus die These ab: Es handelt sich nicht um Moden, die sich ablösen, sondern um **Schichten, die aufeinander aufbauen** — jede neue Stufe umschließt die vorherige.

## Die fünf Stufen (mit im Video genannten Zeitpunkten)

Eine im Video gezeigte Grafik (5 Karten in einer Reihe) fasst die Leiter zusammen:

1. **Prompt Engineering** (groß seit 2022, ChatGPT) — die Formulierung der Eingabe optimieren (Chain-of-Thought, Rollen-Prompts wie "Du bist ein erfahrener Anwalt..."). Grenze: funktioniert nur für einzelne, isolierte Texte, nicht für mehrstufige Agenten-Läufe.
2. **Context Engineering** (Mitte 2025, geprägt laut Video von Andrej Karpathy und Shopify-CEO Tobi Lütke) — nicht mehr nur der Prompt, sondern das gesamte Kontextfenster wird kuratiert: welche Infos, Dokumente, Tools bekommt das Modell wann. Konkretes Beispiel: `CLAUDE.md`/`AGENTS.md` mit Projektregeln, die der Agent bei jedem Start automatisch lädt.
3. **Harness Engineering** (Anfang 2026) — alles um das Modell herum: Tools, Sandbox, Tests, Rechte, Guardrails, Logging. Kernthese: dasselbe Modell wird durch einen besseren Harness spürbar besser, ohne dass am Modell selbst etwas geändert wird.
4. **Loop Engineering** (Juni 2026, laut Video ausgelöst u. a. durch Boris Cherny — im Transkript als "Czerny" verschriftet, siehe unten) — man promptet den Agenten nicht mehr selbst, sondern baut eine Schleife, die ihn wiederholt anstößt, prüft und neu startet, bis ein Ziel erreicht ist (z. B. `/loop` in Claude Code). Zitiert wird die aus [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) bereits bekannte Aussage "Ich prompte Claude nicht mehr selbst, ich habe Loops laufen, die Claude prompten." Nachteil: Loops geben dem Modell volle Kontrolle, verzichten aber auf Determinismus — bei jedem Durchlauf kann etwas anderes rauskommen.
5. **Graph Engineering** (laut Video "frisch aus dem Ofen", eher als Steinbergers Scherz entstanden, "noch nicht wirklich bewiesen und erprobt") — das Agentensystem wird als expliziter Graph modelliert: Knoten sind Arbeitsschritte/Agenten, Kanten die erlaubten Übergänge mit Verzweigungen und Kontrollpunkten. Ziel: Kontrollfluss wieder vorhersehbar und reproduzierbar machen, z. B. garantieren, dass ein Review-Schritt immer erst nach dem Coding-Schritt läuft.

## Belegte Beispiele im Video

- **LangChain/Terminal-Bench:** Ein Screenshot zeigt ein Leaderboard, in dem ein LangChain-Agent ("Deep Agents", Modell GPT-5.2-Codex) rein durch Harness Engineering (System-Prompt-Anpassungen, Selbstverifikations-Loops, Middleware gegen "Doom Loops") von 52,8 % auf 66,5 % Genauigkeit springt und von Platz 30 auf Platz 5 klettert — **ohne das Modell zu wechseln**.
- **Google ADK 2.0:** Screenshots zeigen Codebeispiele, in denen ein Workflow aus Recherche-, Schreib- und Review-Agent als Graph mit wenigen Zeilen Python (`SequentialAgent`, `sub_agents=[...]`) definiert wird — Output des einen Agenten wird garantiert zum Input des nächsten.
- Claude-Code-Features wie "Workflows" werden als Beispiele genannt, die in dieselbe Richtung (Orchestrierung statt freies Agieren) gehen.

## Die Kernthese: der Hebel wandert nach oben

Loris' zentrales Argument: Alle Begriffe (Prompt, Context, Harness, Loop, Graph) sind im Kern **Workarounds für die jeweils aktuelle Schwäche der Modelle** — und Workarounds verschwinden wieder, sobald die Schwäche behoben ist. Was bleibt, ist das Muster: Der Hebel (der Ort, an dem der eigentliche Mehrwert entsteht) wandert immer weiter weg vom reinen Tippen/Prompten hin zu Urteilsvermögen, Architektur und Orchestrierung. Wer dieses Muster verinnerlicht, muss laut Video keinem einzelnen Trend/Buzzword mehr hinterherlaufen, sondern kann neue Stufen sofort einordnen.

## Offener Schluss

Loris spekuliert unverbindlich, dass die Abstraktion irgendwann so weit gehen könnte, dass man wieder nur noch sagt, was man will (zurück zum "Prompt", nur mit sehr viel dazwischen, das niemand mehr versteht) — betont aber ausdrücklich, dass er das nicht vorhersagen kann und die Richtung eher von Leuten wie Boris Cherny oder Peter Steinberger bestimmt wird als von ihm selbst.

---

## Kernbotschaft
KI-Workflow-Begriffe wie Prompt-, Context-, Harness-, Loop- und Graph-Engineering sind keine sich ablösenden Trends, sondern aufeinander aufbauende Schichten, die jeweils eine aktuelle Modell-Schwäche kompensieren. Der praktische Nutzen liegt nicht darin, jeden neuen Begriff zu lernen, sondern das dahinterliegende Muster zu erkennen: Der Hebel für bessere Ergebnisse wandert von der reinen Prompt-Formulierung hin zu Kontext-Kuratierung, Tooling/Guardrails (Harness), autonomen Verifikationsschleifen (Loop) und zuletzt zu explizit modelliertem, deterministischem Kontrollfluss (Graph) — mit klaren, im Video belegten Beispielen (LangChain-Terminal-Bench-Sprung, Google ADK 2.0), dass bessere Orchestrierung mehr bringen kann als ein besseres Modell.

## Themen-Tags
Prompt Engineering, Context Engineering, Harness Engineering, Loop Engineering, Graph Engineering, Agentic Engineering, Claude Code, Google ADK, LangChain, Boris Cherny, Peter Steinberger, Terminal-Bench

## Zu prüfen (falls zutreffend)
- **Whisper-Transkriptionsfehler bestätigt:** Das Transkript schreibt durchgehend "Boris Czerny" — laut den bereits vorhandenen Repo-Notizen ([ai-agent-workflow.md](../ai-agent-workflow.md), [video-summary-KWrsLqnB6vA.md](video-summary-KWrsLqnB6vA.md), [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md)) heißt der Claude-Code-Erfinder korrekt **Boris Cherny**. In dieser Zusammenfassung entsprechend korrigiert. Ebenso wurde "Andrej Kapafi" im Transkript zu Andrej Karpathy korrigiert (Whisper-Verhörer, plausibel angesichts des Kontexts).
- **Inhaltliche Überschneidung mit vorhandenen Notizen:** Die "Loop Engineering"-Stufe und das Boris-Cherny-Zitat ("ich prompte Claude nicht mehr selbst...") sind inhaltlich fast deckungsgleich mit dem bereits vorhandenen [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) und Punkt 8 in [ai-agent-workflow.md](../ai-agent-workflow.md). Kein Widerspruch, aber deutliche Redundanz — dieses Video ordnet den Loop-Gedanken zusätzlich in eine größere 5-Stufen-Leiter ein (Prompt → Context → Harness → Loop → Graph), was in den bestehenden Notizen so noch nicht dokumentiert war und den eigentlichen Mehrwert dieses Videos ausmacht.
- **Plausibilitätscheck durchgeführt (WebSearch), beide Kernbelege bestätigt:** (1) LangChains Terminal-Bench-2.0-Sprung von 52,8 % auf 66,5 % (Platz 30 → Platz 5) durch reines Harness-Engineering am Modell GPT-5.2-Codex ist durch mehrere unabhängige Artikel (u. a. langchain.com/blog, Medium) bestätigt. (2) Googles ADK 2.0 als Umbau von einem hierarchischen Agent-Runner zu einer Graph-basierten Workflow-Engine (GA seit Mai 2026) ist ebenfalls durch mehrere Quellen bestätigt (google.github.io/adk-docs, developers.googleblog.com). Peter Steinberger als realer OpenClaw-Schöpfer und Prägungsfigur für "Agentic Engineering" ebenfalls bestätigt.
- Die im Video genannten Datierungen der einzelnen Stufen (Prompt Engineering 2022, Context Engineering Mitte 2025, Harness Engineering Anfang 2026, Loop Engineering Juni 2026) sind Loris' eigene, nicht weiter belegte Einordnung/Erinnerung — nicht unabhängig verifiziert, wirken aber plausibel als grobe Chronologie.
- **Für Team-/Gruppenleiter-Kontext relevant:** Das Video liefert vor allem einen Denkrahmen (nicht nur einzelne Tricks), um zu beurteilen, wo man als Team/Lead investieren sollte — z. B. ob ein schwaches Agenten-Ergebnis eher an fehlendem Kontext (CLAUDE.md/Projektregeln), fehlendem Harness (Tools/Guardrails/Tests) oder fehlender Verifikationsschleife liegt, statt vorschnell "das Modell ist schlecht" zu schließen. Passt inhaltlich gut als Ergänzung zu den bereits vorhandenen praktischen Punkten in [ai-agent-workflow.md](../ai-agent-workflow.md).

**Hinweis zum Ablauf:** Native Untertitel scheiterten mit HTTP 429, der Whisper-Fallback (Replicate) lief diesmal erfolgreich durch (in 2 Chunks à ~330s, 155 Segmente gesamt). Die Zusammenfassung basiert auf vollständigem Transkript plus stichprobenartig gesichteten Frames (Grafiken/Screenshots von Terminal-Bench-Leaderboard und ADK-2.0-Code wurden geprüft).
