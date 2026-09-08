# "KI-Loops reichen nicht mehr: Jetzt kommt Graph Engineering!"

**Kanal:** KI Schritt-für-Schritt (Cristian Gebauhr)
**URL:** https://www.youtube.com/watch?v=zBI2bWO7RLc
**Länge:** 09:26
**Zusammenfassung erstellt:** 2026-09-07

---

*Siehe auch: [loop-engineering-ueberblick.md](../loop-engineering-ueberblick.md), [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) und [video-summary-4NqKZerJpk8.md](video-summary-4NqKZerJpk8.md) — alle drei behandeln bereits dieselbe Begriffskette Prompt/Loop/(Harness)/Graph Engineering. Einordnung siehe "Zu prüfen" unten.*

## Aufhänger

Der Host eröffnet direkt mit der Beobachtung, dass kaum ein Begriff ("Loop Engineering") verstanden ist, schon der nächste ("Graph Engineering") auftaucht, und stellt die Ausgangsfrage, ob es sich dabei um eine wirklich neue Stufe handelt oder nur um ein neues Wort für etwas Bekanntes. Ziel des Videos: die Unterschiede zwischen Prompt Engineering, Loop Engineering und Graph Engineering "leicht verständlich" erklären.

## Prompt Engineering vs. Loop Engineering

Der Host führt die Unterscheidung über die Frage ein, *wer im Loop ist*:

- **Mensch im Loop (= Prompt Engineering):** Der Mensch ist die Schleife — Befehl geben, warten, prüfen, erneut prompten, so lange bis das Ergebnis passt. "Mega umständlich und sehr zeitintensiv."
- **KI im Loop (= Loop Engineering):** Der Mensch gibt Ziel und Abnahmeregel vor, die KI wiederholt selbst **Reason → Act → Observe**, bis die Zielbedingung erfüllt ist. Zentral: die **Stopp-Bedingung** ist laut Video "eine Prüfung, kein Timer" — z. B. "schreibe so lange, bis der Text 500 Wörter hat / zwei H2- und drei H3-Überschriften hat / zwei Bilder eingebunden sind." Ohne erfüllte Prüfung läuft die Schleife eine weitere Runde statt einfach nach Zeit abzubrechen.

Dieser Teil deckt sich inhaltlich mit dem bereits ausführlich im Repo dokumentierten Loop-Konzept (siehe [loop-engineering-ueberblick.md](../loop-engineering-ueberblick.md): "Kontrollsatz vs. objektives Kriterium", Abbruchbedingung/Budget) — hier kompakter und ohne neue Details.

## Graph Engineering: "Der Graph ersetzt den Loop nicht — er umschließt ihn"

Kernaussage des Videos, textlich im Frame bei t≈03:00 hervorgehoben: Ein Graph ist **kein Upgrade, das Loops überflüssig macht**, sondern eine übergeordnete Schicht — die Elemente sind geschichtet:

- **Graph = der Bauplan** (Knoten + Kanten). Ein Knoten kann ein KI-Agent, ein Tool-Aufruf oder eine normale Funktion sein.
- **Innerhalb eines Knotens** kann ein **Loop** laufen (z. B. "schreibe, bis eine Bedingung erfüllt ist").
- **Innerhalb eines Loops** laufen wiederum **Prompts** (einzelne Schritte/Anweisungen, z. B. Kontext → Modell → Antwort).

Der Graph legt laut Video *nicht* fest, was innerhalb eines Knotens passiert, sondern **wie oft, in welcher Reihenfolge und innerhalb welcher Grenzen** die Knoten ablaufen — also den erlaubten Kontrollfluss, nicht den Inhalt der einzelnen Schritte. Der Host betont ausdrücklich, dass die Grundidee (Abläufe aus verbundenen Knoten) "in der Softwareentwicklung schon lange" existiert und Graph Engineering insofern keine völlig neue Erfindung ist.

## Praxisbeispiel: YouTube-Video-Produktion als Graph

Anhand einer Skizze (Google-Drawings-artige Oberfläche, im Frame mit rotem Freihand-Kreis nachträglich hervorgehoben) erklärt der Host den Ablauf für ein YouTube-Video:

1. **Thema** → **Thema recherchieren** (ein Knoten)
2. Danach teilt sich der Pfad: **Agent 1 (Skript schreiben)** — mit internem Loop "Qualität erreicht? → ja/nein → Skript verbessern" — läuft **parallel** zu **Agent 2 (Titel & Thumbnail)** mit eigenem Prüf-Loop ("Titel und Thumbnail passen zusammen?")
3. Beide Zweige laufen in einem Knoten **"Menschliche Freigabe"** zusammen
4. Erst danach: **"YouTube-Video fertig"**

Der Host empfiehlt ausdrücklich (nicht zwingend), am Ende noch einmal menschlich zu prüfen, bevor freigegeben wird — die einzige explizite Human-in-the-loop-Empfehlung im Video.

## Die drei Ebenen im Vergleich (Tabelle im Video, t≈07:22)

| | **Prompt Engineering** | **Loop Engineering** | **Graph Engineering** |
|---|---|---|---|
| Kernobjekt | Instruktion | Kontrollzyklus | Topologie |
| Zuverlässig wird … | ein einzelner Modellaufruf | das Verhalten eines Agenten | die Zusammenarbeit vieler Agenten |
| Mensch bestimmt | Kontext, Formate, Verbote | Ziel- und Qualifikationskriterien | den kompletten Pfad (Bauplan) |
| KI bestimmt | nichts, sie antwortet nur | den Weg zum Ziel | nur das Innere einzelner Knoten |
| Bausteine | Kontext, Ausgabeformat, Verbote | Trigger, Tools, Status, Validatoren, Stopp-Bedingungen | Knotenkanten, Rechte, Beobachtung, Versionen |

Abschließende Ein-Satz-Zusammenfassung des Hosts: "Beim Prompt wird bestimmt, was gesagt wird. Beim Loop wird bestimmt, wie oft und wie lange es gesagt wird. Beim Graphen wird bestimmt, wer mit wem, in welcher Reihenfolge und mit welcher Freigabe etwas wird."

## Für den technischen Team-/Gruppenleiter

Der direkt nutzbare Kern für eine Lead-Rolle ist die Spalte "Mensch bestimmt" der Tabelle: Sie liefert eine einfache Checkliste, auf welcher Ebene ein Team gerade Kontrolle ausübt (nur Prompt-Formulierung? Ziel+Kriterien für einen Agenten? Oder der komplette Freigabe-/Reihenfolge-Pfad für mehrere Agenten?) und wo im eigenen Workflow noch menschliche Freigabepunkte fehlen könnten. Das YouTube-Produktions-Beispiel mit explizitem "Menschliche Freigabe"-Knoten vor Abschluss ist ein direkt übertragbares Muster für jeden mehrstufigen Agenten-Workflow mit Team-Verantwortung (Parallelisierung zweier Teilaufgaben, Zusammenführung, Freigabe-Gate).

---

## Kernbotschaft
Graph Engineering ist laut Video keine Ablösung, sondern eine zusätzliche, übergeordnete Schicht über Loop und Prompt Engineering: Ein Graph (Bauplan aus Knoten/Agenten und Kanten) legt fest, in welcher Reihenfolge, mit welchen Grenzen und mit welcher Freigabe mehrere Agenten/Loops zusammenarbeiten — ohne selbst zu bestimmen, was innerhalb eines einzelnen Knotens passiert (dort laufen weiterhin Loops, und innerhalb der Loops weiterhin Prompts). Der praktische Kernpunkt für die eigene Arbeit: Je höher die Ebene (Prompt → Loop → Graph), desto mehr Entscheidungsmacht behält der Mensch über die Gesamtstruktur, während die KI mehr Freiraum innerhalb der von ihr verantworteten Teile bekommt.

## Themen-Tags
Graph Engineering, Loop Engineering, Prompt Engineering, Reason-Act-Observe, Stopp-Bedingung, Multi-Agenten-Workflow, Knoten und Kanten, Human-in-the-Loop, Kontrollfluss

## Zu prüfen (falls zutreffend)
- **Cross-Check gegen bestehende Notizen: kein Widerspruch, aber deutlich schmaleres Modell.** [loop-engineering-ueberblick.md](../loop-engineering-ueberblick.md) dokumentiert bereits zwei Fassungen derselben Begriffskette: (1) [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) mit einer fünfstufigen Leiter Prompt → Context → Harness → Loop → Graph Engineering (Graph = Knoten/Kanten, Kontrollfluss vorhersehbar machen, mit realen Belegen wie LangChain-Terminal-Bench und Google ADK 2.0) und (2) [video-summary-4NqKZerJpk8.md](video-summary-4NqKZerJpk8.md), wo Graph Engineering primär als **mehrere parallele Loops mit potenziell unterschiedlichen, kostenoptimierten Modellen** definiert wird. Dieses Video hier lässt Context- und Harness-Engineering als eigene Stufen komplett weg (nur Prompt → Loop → Graph) und erwähnt weder Boris Cherny noch Peter Steinberger als Urheber der Begriffe noch irgendein reales Framework (kein LangChain/ADK/Kimi-Beispiel) — die "Graph = Bauplan aus Knoten/Kanten, der Loops organisiert"-Definition selbst deckt sich aber inhaltlich fast exakt mit SFtiPOTLBHA und ist mit dessen belegten Beispielen (Google ADK 2.0: `SequentialAgent`, `sub_agents=[...]`) kompatibel. Kein Sachwiderspruch, aber die Begriffsbreite bei "wie viele Stufen gibt es" bleibt repo-weit uneinheitlich — passt zur bereits im Loop-Überblick notierten Beobachtung, dass sich die Begriffswelt 2026 noch nicht gesetzt hat.
- **Plausibilitätscheck (WebSearch) durchgeführt:** Die Grundaussage des Videos ("Abläufe aus Knoten/Kanten gibt es in der Softwareentwicklung schon lange") ist über die reale Existenz von **LangGraph** (LangChain) bestätigt — ein verbreitetes Open-Source-Framework, das Agenten-Workflows exakt als Graph aus Knoten (Agenten/Funktionen/Entscheidungspunkte) und Kanten (statisch oder bedingt/dynamisch geroutet) modelliert, inkl. Fan-out/Fan-in-Mustern. Die im Video gezeigte Struktur (Knoten mit internem Loop, bedingte Kanten zur Verzweigung) entspricht dem gängigen DAG-/State-Graph-Muster realer Orchestrierungs-Frameworks. Konfidenz: hoch, aber nur allgemeine Plausibilität geprüft — das Video selbst nennt kein konkretes Framework, keine Studie und keine Zahl, die einzeln verifizierbar wäre.
- Datierungen, Urheberschaft des Begriffs "Graph Engineering" oder Vergleich zu anderen Frameworks (LangGraph, Google ADK, Temporal etc.) werden im Video selbst an keiner Stelle genannt — die Einordnung oben stammt ausschließlich aus dem Repo-Kontext, nicht aus dem Video.
- Kanalname laut Skript-Metadaten "KI Schritt-für-Schritt", Uploader-Feld "Cristian Gebauhr" — nicht unabhängig gegengeprüft, aber unproblematisch (Kanalname vs. Klarname des Betreibers).

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429 (Rate-Limit), der Whisper-Fallback (Replicate) lief in einem Durchgang durch und lieferte 147 Segmente für die vollen 09:26 Minuten. Alle 80 extrahierten Frames wurden gesichtet (durchgehend animierte Textslides/Diagramme mit Sprecher-Bild-in-Bild, keine erkennbaren Transkriptionsartefakte).
