# "Verstehe Agent Harness, Loop und Graph Engineering und überhole 90%"

**Kanal:** Sascha Hoffmann | KI ohne Team
**URL:** https://www.youtube.com/watch?v=4NqKZerJpk8
**Länge:** 11:34
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) — behandelt exakt dieselbe Begriffskette Harness → Loop → Graph Engineering (dort als Stufen 3–5 einer fünfteiligen, Peter-Steinberger-inspirierten Leiter), aber mit anderer Grundlage und mit belegten Praxisbeispielen (LangChain-Terminal-Bench, Google ADK). [claude-skills-ueberblick.md](../claude-skills-ueberblick.md), Abschnitt "Vier-Bereiche-Modell für Agent-Arbeit", und [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) für eine dritte, wiederum abweichende Definition von "Harness". [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 8 und [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) für das allgemeine Loop-Konzept.*

## Aufhänger: Drei Buzzwords, aber angeblich zu wenig Praxisnutzen

Der Host (Sascha Hoffmann, betreibt die Community "KI ohne Team") stellt fest, dass "Agent Harness", "Loop Engineering" und – als neuester Begriff – "Graph Engineering" aktuell in praktisch jedem KI-Video auf YouTube auftauchen. Sein Beobachtung aus Gesprächen: Die meisten halten die Begriffe für Experten-Kram, optimieren stattdessen stundenlang an einzelnen Prompts und erreichen damit nur 10–15 % Verbesserung statt eines "richtigen Sprungs". Sein Versprechen: Wer zuerst den Harness versteht, dann den Loop richtig einsetzt und zuletzt den Graph darüberlegt ("genau in der Reihenfolge"), kommt weiter als reine Prompt-Optimierung.

## Die Basis: KI-Modell plus vier Engineering-Bausteine

Aufgebaut wird das Ganze live in einem Figma-Whiteboard, Baustein für Baustein. Ausgangspunkt ist das reine KI-Modell (im Frame als rotes Kästchen mit ChatGPT-Logo, dann als "KI Modell" beschriftet) – laut Video das, worüber am meisten gesprochen wird ("neues Modell, besser in allen Benchmarks"), aber aus Agenten-Sicht nicht das Wichtigste. Um das Modell herum werden vier violette Kästchen gruppiert:

- **Prompt Engineering** – die Formulierung der Eingabe
- **Context Engineering** – zusätzliches Domänenwissen, z. B. über ChatGPT-Projekte
- **Tool Engineering** – angebundene Konnektoren/MCPs (Beispiel: Manus mit breiter Tool-Palette, Claude/ChatGPT mit eigenen Remote-MCPs)
- **Skill Engineering** – feste, dem Agenten mitgegebene Abläufe/Prozesse

## Harness Engineering: Die Umgebung, die alles zusammenhält

Diese fünf Elemente (Modell + vier Bausteine) werden im Frame (t≈04:34) mit einem hellblauen Rahmen umschlossen und als "Harness" beschriftet – die Umgebung, in der der Agent läuft, und laut Video die erste Entscheidung, die man treffen muss. Als konkrete Beispiele für Harnesses nennt der Host: **Claude Code, Codex, OpenClaw, Hermes, Manus AI**. Wichtige Auswahlkriterien nach eigener Aussage: Bietet der Harness Befehle wie `/goal`, `/loop`, `/hooks` an (ein Frame zeigt genau diese Liste als Sticky Note)? Und: Lassen sich mehrere KI-Modelle anbinden (nicht nur verschiedene Claude-Varianten wie Opus/Fable, sondern auch fremde Anbieter wie Kimi)? Harnesses ohne Skill-Engineering-Unterstützung fallen für ihn z. B. schon raus.

## Loop Engineering: Wiederkehrende, zielverfolgende Prozesse

Um den Harness-Kasten wird ein zweiter Rahmen gelegt und als "Loops" beschriftet (t≈06:39): innerhalb eines gewählten Harness lassen sich wiederkehrende Prozesse definieren, die ein Ziel verfolgen – Beispiel-Prompt-Fragment im Video: *"/loop alle fünf Minuten, verfolge Ziel A"*. Der Loop kann lokal oder in der Cloud laufen und nutzt dabei die zuvor festgelegten Prompts, Kontext, Tools, Skills und das Modell.

## Graph Engineering: Mehrere Loops zu einem Ökosystem verbinden

Laut Video entstand dieser, "neueste" Begriff aus einem konkreten Problem von Einzel-Loops: Ein Loop läuft dauerhaft mit demselben (oft teuren) Modell, etwa durchgehend mit Opus – unnötig teuer, wenn manche Teilaufgaben viel einfacher sind. Lösung: mehrere Loops parallel, die geteiltes Wissen haben, miteinander interagieren können und im Idealfall jeweils einen eigenen Harness und ein eigenes (günstigeres oder passenderes) Modell nutzen – als Beispiel nennt der Host **Haiku, GPT-5-Sol und "Kimiko K3"** (im Frame nicht zu sehen, vermutlich Whisper-Verhörer von "Kimi K3", siehe Zu prüfen) für die drei Loops. Diese Gesamtarchitektur aus mehreren verknüpften Loop-plus-Harness-Einheiten nennt das Video "Graph Engineering".

**Konkretes Beispiel (t≈09:00–09:46, im Frame mit drei nebeneinander liegenden Loop-Kästen und grünem Rahmen "graph" gezeigt):**
1. **Research-Loop** – recherchiert, um das eigene Produkt weiterzuentwickeln, Erkenntnisse werden als Tickets angelegt
2. **Bau-Loop** – baut aus den Ticket-Infos die Umsetzung
3. **Review-Loop** – prüft das Ergebnis

Drei verschiedene Loops, potenziell drei verschiedene Harnesses, drei verschiedene Modelle – die Gesamtarchitektur dahinter ist laut Video der Graph. Zusammenfassung des Hosts: "Kannst du als Mensch eine Architektur schaffen, die in sich selbst läuft" – mit beliebig vielen Sub-Agents und Möglichkeiten.

## Fazit: Ein Meta-Skill statt Werkzeugkunde

Der Host fasst zusammen: Man müsse nicht alle Harnesses beherrschen, sondern den, der am besten zum eigenen Anwendungsfall passt; danach müsse man verstehen, wie Loops funktionieren; und wer es schaffe, Loops als Gesamtkonzept für ein ganzes Unternehmen aufzubauen, besitze "den Skill für 2027" (seine persönliche, nicht weiter belegte Einschätzung). Am Ende Eigenwerbung: ein eigener Newsletter-Artikel zu "allen vier Arten von Loops" wird beworben (Link nur in den – hier nicht einsehbaren – Shownotes).

## Für den technischen Team-/Gruppenleiter

Zwei Punkte sind für eine Gruppenleiter-Rolle direkt greifbar: Erstens die **Kostensteuerung über Modellwahl pro Teilaufgabe** – die im Video gezeigte Idee, nicht jeden Loop-Schritt mit dem teuersten Modell laufen zu lassen, sondern günstigere Modelle für einfache Teilaufgaben und teurere nur für anspruchsvolle Schritte zu reservieren, ist ein direkt umsetzbares Muster für Teams, die KI-Tooling-Budgets im Blick behalten müssen. Zweitens die **Entscheidungsvereinfachung "einen Harness beherrschen, nicht alle"** – eine nützliche Leitlinie, wenn im Team die Frage aufkommt, wie viel Zeit in die Evaluierung verschiedener Agent-Umgebungen investiert werden soll. Das konkrete Drei-Loop-Beispiel (Research → Ticket-Bau → Review) ist strukturell vergleichbar mit dem bereits im Repo dokumentierten Bau-Prüf-Muster in [video-summary-RaraRJ0IZpA.md](video-summary-RaraRJ0IZpA.md), dort aber als reale, live gezeigte Laufzeit-Demo statt als reine Whiteboard-Skizze.

---

## Kernbotschaft
Das Video ordnet drei aktuell kursierende Buzzwords in eine gebaute, live gezeichnete Diagramm-Hierarchie: Ein KI-Modell plus vier Bausteine (Prompt-, Context-, Tool-, Skill-Engineering) bilden zusammen den **Harness** (die Umgebung, in der ein Agent läuft, z. B. Claude Code, Codex, OpenClaw, Hermes, Manus AI); ein **Loop** ist ein innerhalb eines Harness wiederkehrender, zielverfolgender Prozess; **Graph Engineering** verbindet mehrere solcher Loop-plus-Harness-Einheiten (potenziell mit unterschiedlichen, kostenoptimierten Modellen) zu einem größeren, selbstlaufenden Ökosystem. Der Host präsentiert das als eigene, unbelegte Einordnung ("Meta-Skill", "der Skill für 2027") ohne Verweis auf die anderswo im Repo bereits dokumentierten Ursprungsfiguren (Boris Cherny, Peter Steinberger) oder externe Belege.

## Themen-Tags
Agent Harness, Loop Engineering, Graph Engineering, Prompt Engineering, Context Engineering, Tool Engineering, Skill Engineering, Claude Code, Codex, OpenClaw, Hermes, Manus AI, Multi-Modell-Strategie, Kostenoptimierung, Kimi K3

## Zu prüfen
- **Starke inhaltliche Überschneidung mit [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md):** Dieses Video ist im Kern eine eigenständige, unabhängige Illustration derselben "Harness → Loop → Graph"-Begriffskette, die dort bereits als Stufen 3–5 einer fünfstufigen Leiter (Prompt → Context → Harness → Loop → Graph Engineering) mit externen Belegen (LangChain-Terminal-Bench-Sprung, Google-ADK-2.0-Umbau) dokumentiert ist. Auffälliger Unterschied: Dieses Video nennt weder Boris Cherny noch Peter Steinberger als Urheber der Begriffe (obwohl SFtiPOTLBHA und weitere Repo-Videos beide explizit als Prägungsfiguren für "Loop Engineering" nennen) und liefert keine externen Belege/Screenshots realer Systeme – die gesamte Erklärung ist eine reine, selbst gezeichnete Whiteboard-Konstruktion ohne Live-Demo oder Zitat. Kein Widerspruch in der Substanz, aber deutlich schwächer belegt als die Referenzquelle.
- **Neuer, in dieser Form noch nicht dokumentierter Aspekt:** Die konkrete Graph-Engineering-Beispielkette "Research-Loop → Bau-Loop → Review-Loop" mit jeweils potenziell unterschiedlichem Modell (Haiku/GPT/Kimi) pro Loop-Rolle als Kostenoptimierungs-Argument ist so im Repo noch nicht festgehalten – ergänzt die eher abstrakte Google-ADK-Erklärung aus SFtiPOTLBHA um ein konkreteres (wenn auch nicht live demonstriertes) Szenario.
- **Widersprüchliche "Harness"-Definition, dritter Datenpunkt:** In diesem Video umschließt "Harness" alle vier Bausteine (Prompt/Context/Tool/Skill-Engineering) als Container. In [video-summary-tK9C3Skskws.md](video-summary-tK9C3Skskws.md) (zitiert in [claude-skills-ueberblick.md](../claude-skills-ueberblick.md)) ist "Harness Engineering" dagegen selbst nur einer von vier gleichrangigen Bausteinen (neben Context/Tool/Skill Engineering) – keine Container-Beziehung. Bestätigt und verschärft die dort bereits notierte Beobachtung, dass sich der Harness-Begriff 2026 im Repo-Bestand noch nicht einheitlich gesetzt hat.
- **Kimi K3 / "Kimiko K3":** Per WebSearch bestätigt, dass Moonshot AI im Juli 2026 tatsächlich ein Modell namens **Kimi K3** veröffentlicht hat (Open-Weight-MoE, ca. 2,7–2,8 Bio. Parameter, laut Berichterstattung u. a. bei Bloomberg, CNBC, Fortune nahe an Anthropic/OpenAI-Spitzenmodellen). Die Transkriptform "Kimiko K3" ist daher wahrscheinlich ein Whisper-Verhörer von "Kimi K3", nicht ein eigenständiges Modell – im Frame nicht sichtbar, daher nicht zu 100 % auflösbar.
- **Hermes als Harness:** Per WebSearch bestätigt, dass "Hermes Agent" ein reales, seit Februar 2026 quelloffenes autonomes Agentensystem von Nous Research ist (Terminal/Desktop-App, Multi-Provider-Modellunterstützung, Skills, geplante Jobs) – passt zur Einordnung als "Harness" im Video.
- **Sascha Hoffmann / "KI ohne Team":** Per WebSearch bestätigt als realer YouTube-Kanal/reale Community für KI-Agenten-Systeme; der Host bewirbt am Ende des Videos einen eigenen Newsletter – wie bei anderen Solo-Creator-Videos im Repo entsprechend als Kanal-Eigenwerbung einzuordnen, keine unabhängige Bestätigung des Community-Angebots vorgenommen.
- Die Aussage "der Skill für 2027" sowie die generelle Behauptung, die meisten Nutzer würden "stundenlos" nur an Prompts optimieren und dabei nur 10–15 % Verbesserung erreichen, sind unbelegte, persönliche Einschätzungen des Hosts ohne Studien/Zahlen dahinter.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; der Whisper-Fallback (Replicate) lief in einem Durchgang durch und lieferte 153 saubere, durchgehend verständliche Segmente für die vollen 11:34 Minuten (keine erkennbaren Transkriptions-Artefakte). Die Zusammenfassung basiert auf dem vollständigen Transkript sowie 19 gezielt ausgewählten der 80 extrahierten Frames (Rest überwiegend redundante Talking-Head-Aufnahmen oder Zwischenschritte desselben, sich schrittweise aufbauenden Figma-Whiteboard-Diagramms).
