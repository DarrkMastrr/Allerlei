# "5 Minuten Pause, 10-facher Preis: die Token-Falle, die keiner kennt"

**Kanal:** Benjamin Thorstensen (kylo.at)
**URL:** https://www.youtube.com/watch?v=XEbR5qmxGQ0
**Länge:** 18:57
**Zusammenfassung erstellt:** 2026-08-01

**Fact-Check-Status: durchgeführt am 2026-08-01 per vier parallelen Recherche-Agenten + einem unabhängigen Prüfer-Agenten (Live-Abgleich gegen offizielle Anthropic-/OpenAI-Doku sowie das echte DeepSWE-Leaderboard). Die konkretesten, prüfbarsten Zahlen im Video halten einer direkten Gegenprobe stand — siehe Fact-Check-Abschnitt unten.**

---

## Die Ausgangsgeschichte

Der Host macht eine kurze Kaffeepause mitten in einer Coding-Agent-Session — die nächste Nachricht danach kostet ihn ohne Vorwarnung fast das Zehnfache. Grund: der Prompt-Cache seiner Konversation war zwischenzeitlich abgelaufen.

## Token-Typen

- **Input-Tokens** — was man selbst eingibt
- **Output-Tokens** — die Antwort der KI, inklusive unsichtbarer **Reasoning-Tokens** (werden gleich abgerechnet wie sichtbare Output-Tokens, sind aber selbst meist nicht zu sehen) — Output-Tokens sind üblicherweise deutlich teurer als Input-Tokens
- **Cached-Input-Tokens** — bereits einmal gesendeter Kontext (System-Prompt, bisherige Konversation), der beim nächsten Request erneut mitgeschickt, aber deutlich günstiger verrechnet wird, wenn er unverändert ist

## Cache-Hit vs. Cache-Miss

Ein Cache-Hit spart massiv Geld, ein Cache-Miss kostet den vollen Input-Preis statt des Cached-Preises. Gezeigte Auslöser für einen Cache-Miss:
1. Wechsel des KI-Modells (auch z. B. Opus → Sonnet)
2. Wechsel des Reasoning-Levels (z. B. extra-high → high → medium)
3. Ein neues Tool/MCP wird der Konversation hinzugefügt
4. Die Konversation wird zu lange nicht fortgesetzt — der Cache hat eine Time-to-Live (TTL) und verfällt danach automatisch (Beispiel im Video: ein Anbieter hält den Cache standardmäßig nur 5 Minuten, gegen Aufpreis bis zu 1 Stunde; bei manchen OpenAI-Modellen bis zu 24 Stunden, bei neueren Modellen kürzer)

## Gezeigte Preistabellen

- **GPT-5.5** (kurzer Kontext, pro 1M Tokens): Input $5,00, Cached Input $0,50, Output $30,00
- **Claude-Prompt-Caching** (Anthropic-Doku): Claude Fable 5 & Mythos 5 je $10 Basis-Input / $12,50 (5-Min-Cache-Write) / $20 (1-Std-Cache-Write) / $1 (Cache-Hit); Claude Opus 4.8: $5 / $6,25 / $10 / $0,50

## Praktische Tipps zum Tokensparen

- Neues Thema → neuer Chat statt einer immer länger werdenden Konversation
- Vor einer Pause: **Compaction** (Zusammenfassung) oder — bevorzugt vom Host — ein **Handover**-Markdown-Dokument, in dem gezielt die wirklich relevanten Infos für die nächste Aufgabe stehen, statt der KI die Auswahl bei einer automatischen Compaction zu überlassen
- Modell schon zu Beginn passend wählen (bei bekannt anspruchsvollen Aufgaben direkt starke Modelle statt Hochstufen im Nachhinein), bei Unsicherheit Kosten/Leistungs-Benchmarks wie DeepSWE konsultieren
- Wiederkehrende Aufgaben als **Skills** festhalten statt die Anweisungen jedes Mal neu zu formulieren
- Frameworks, die Agenten zu kürzeren Antworten zwingen (Beispiel **Caveman**), sparen laut eigener Erfahrung des Hosts vor allem bei der sichtbaren Chat-Antwort — nicht bei den eigentlichen Kostentreibern (Code-Generierung, Reasoning)
- Aufgeblähte System-Prompts von manchen Coding-Agenten verwirren das Modell zusätzlich, nicht nur Kostenfrage — gezeigter Vergleich: Copilot CLI (10.127 Wörter) vs. VS Code Copilot Agent (4.471 Wörter) vs. "Pi Agent" (341 Wörter)
- **Codebase agent-ready machen** (Lieblingstipp des Hosts): etablierte statt exotische Frameworks verwenden, Monorepo-Struktur, maschinenlesbare Dokumentation mit Progressive Disclosure (Agents.md verweist auf db.md/vision.md/api.md statt alles in eine Datei zu packen), wiederkehrende Fehler durch Tests/Linter/CI wegautomatisieren, den Agenten Lösungen beweisen statt nur behaupten lassen (Screenshots, End-to-End-Tests, Performance-Messungen)

---

## Fact-Check (vier Recherche-Agenten + ein unabhängiger Prüfer, 2026-08-01)

**Bestätigt, live gegen Primärquellen geprüft:**
- GPT-5.5-Preise exakt wie im Video gezeigt (offizielle OpenAI-Preisseite)
- Claude-Prompt-Caching-Preistabelle exakt wie gezeigt, inkl. der 1,25×/2×/0,1×-Multiplikator-Struktur (vom Prüfer-Agenten selbst live gegen die Anthropic-Doku gegengefetcht, nicht nur einem anderen Agenten geglaubt)
- Alle vier genannten Cache-Miss-Auslöser (Modellwechsel, Reasoning-Level, neues Tool/MCP, TTL-Ablauf) für Anthropic explizit dokumentiert
- DeepSWE-Benchmark-Zahl sogar präziser bestätigt als im Video behauptet: Claude Sonnet 5 im Max-Modus 53,85 % Erfolgsquote bei 26,40 $/Task vs. x-high-Modus 49,67 % bei 11,89 $/Task — direkt von der echten Leaderboard-API abgerufen
- "Caveman"-Framework real (github.com/JuliusBrussee/caveman); unabhängige Tests bestätigen die Skepsis des Hosts (beworbene 65 % Ersparnis vs. real eher ~8,5 %)

**Plausibel, aber nicht exakt nachvollzogen:**
- Exakte System-Prompt-Wortzahlen der drei Agenten — Größenordnung über unabhängige Leak-Archive bestätigt, die genauen Zahlen (10.127/4.471/341) nicht wortgenau nachprüfbar
- OpenAI-seitige TTL-Details (24-Std-Cache bei älteren Modellen, kürzeres Fenster bei neueren) — plausibel, aber schwächer belegt als die Anthropic-Seite

**Nichts wurde als falsch oder irreführend eingestuft.**

## Kernbotschaft
Prompt-Caching kann die Kosten pro Anfrage massiv senken (bis zu 10× bei den geprüften Anbietern) — aber der Rabatt verfällt bei Modellwechsel, Reasoning-Level-Wechsel, neuen Tools oder schlicht zu langer Inaktivität. Wer das nicht kennt, zahlt unbemerkt ein Vielfaches. Die wirksamsten Gegenmaßnahmen sind aber nicht Mikro-Optimierungen wie kürzere Antworten, sondern strukturelle: passende Modellwahl von Anfang an, Handover-Dokumente statt automatischer Compaction, schlanke statt aufgeblähte System-Prompts, und vor allem eine für KI-Agenten gut aufbereitete Codebase.

## Themen-Tags
LLM-Pricing, Prompt Caching, Token-Kosten, Claude/Anthropic, OpenAI, DeepSWE-Benchmark, Agentic Coding, System-Prompt-Bloat, Agent-Ready Codebase
