# "Anthropic hat 7 neue Regeln fürs Prompten von Claude verraten"

**Kanal:** Marc De Fanti
**URL:** https://www.youtube.com/watch?v=hEWqRbQe6z4
**Länge:** 9:02
**Zusammenfassung erstellt:** 2026-09-29

**Hinweis zum Ablauf:** yt-dlp scheiterte im ersten Versuch (PO-Token-Provider-Timeout), der zweite Versuch lief durch. Verwendet wurden die (offenbar maschinell ins Englische übersetzten) Untertitel; sie enthalten erkennbare Übersetzungs-/Erkennungsfehler ("Boris Journey"/"Jornada" statt Boris Cherny, "Claude 3/3.5 Opus" statt Opus 5, "Haiku 5.1" — siehe "Zu prüfen"). Von den 80 Frames wurden 16 stichprobenartig angesehen: überwiegend Sprecher im Bild, dazwischen ein Ausschnitt aus einem YC-Talk (Boris Cherny), ein Interview-Prompt-Test in Claude und Screenshots der offiziellen Anthropic-Doku (u. a. Abschnitt "Steuerung des Startens von Subagenten" mit den Variablen `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` / `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`).

---

*Siehe auch: [claude-skills-ueberblick.md](../claude-skills-ueberblick.md) und [context-rot-ueberblick.md](../context-rot-ueberblick.md) (80%-Kürzung des Claude-Code-Systemprompts), [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 6 (Boris Chernys Interview-Prompt) sowie [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md). Cross-Checks siehe "Zu prüfen".*

## Worum es geht

Der Host fasst Anthropics offizielle Prompting-Leitfäden für die Claude-5-Modelle (Opus 5, dazu ein zweites Modell, dessen Name im Transkript als "Haiku 5.1" erscheint) und Aussagen von Boris Cherny (Erfinder von Claude Code) zu sieben Regeln zusammen. Kernthese: Cherny sagt, man promptet die Claude-5-Modelle "falsch" — nämlich zu kleinteilig. Anthropic habe über 80 % des Claude-Code-Systemprompts für diese Modellgeneration entfernt, ohne dass die Coding-Benchmarks schlechter wurden; ein großer Teil der früher nötigen Prompt-Regeln sei damit überflüssig. Der Host betont, dass die Regeln für Opus 5 (und das zweite Modell) offiziell dokumentiert sind, für Sonnet 5 (eigener Guide, Unterschiede bei Antwortlänge und Tool-Nutzung) aber **nicht** 1:1 bestätigt.

## Die sieben Regeln

1. **Die ganze Aufgabe auf einmal geben.** Statt Schritt-für-Schritt-Anweisungen ("erst 1, dann 2, dann 3") Aufgabe, Leitplanken (Guardrails) und Abbruch-/Exit-Kriterien beschreiben und das Modell laufen lassen ("check back later"). Micromanagement kostet Zeit und Tokens ohne bessere Ergebnisse. Zitiert wird Boris Cherny aus einem Y-Combinator-Talk; Anthropic beschreibe es in der Doku genauso.
2. **Claude zuerst interviewen lassen** (laut Host *keine* offizielle Anthropic-Regel, sondern Community-Technik). Bei komplexen Aufgaben nicht den fertigen Auftrag geben, sondern gezielte Fragen stellen lassen, aus denen der eigentliche Prompt entsteht — sinnvoll, wenn man selbst noch nicht genau weiß, was man will. Im Video wird das kurz live getestet (Palindrom-Beispielaufgabe, Claude fragt Sprache und Ablauf ab).
3. **Das "Warum" nennen.** Laut Anthropic hilft der Hintergrund ("Claude is smart enough to generalize from the explanation"): wofür, für wen, was danach mit dem Ergebnis passiert. Bei nicht vorhergesehenen Zwischenentscheidungen entscheidet Claude dann eher so, wie man selbst entschieden hätte.
4. **"Definition of Done" festlegen** — inkl. was ausdrücklich *nicht* zur Aufgabe gehört. Bei langen autonomen Läufen erweitert das Modell sonst den Umfang, schreibt mehr Text als nötig oder ändert Ungefragtes. Entspricht Chernys "exit criteria".
5. **Begründete Regeln statt starrer Verbote ("richtige Flughöhe").** Zu starre Wenn-dann-Regelwerke sind fehleranfällig, zu vage Prompts unklar. Besser: nicht "nie X", sondern "tu Y, weil Z".
6. **Alte Prompting-Tricks weglassen.** Explizite Verifikationsanweisungen ("prüf am Ende alles nochmal", "nutze einen Subagenten zum Review") führen laut Anthropic zu Über-Verifikation und verschwendeten Tokens, da das Modell eigene Fehler von selbst findet. "Think step-by-step" sei oft schlechter als allgemeines "denke gründlich"; GROSSBUCHSTABEN-Befehle ("CRITICAL: YOU MUST ...") solle man durch normale Sprache ersetzen.
7. **Die Claude-Stimme einmal zentral festlegen.** Opus 5 antworte standardmäßig ausführlicher; statt in jedem Chat Kürze zu verlangen, gehört eine Vorgabe (Beispiel laut Video: "Keep responses focused, brief, and concise.") einmalig in die CLAUDE.md bzw. die Systemanweisung.

**Bonus:** Opus 5 delegiert deutlich bereitwilliger an Subagenten. Lohnt sich bei großen, wirklich unabhängigen Aufgaben, bei kleinen kostet es schnell Zeit und Tokens. Anthropic stellt Umgebungsvariablen bereit, mit denen sich die Zahl der Subagenten hart begrenzen lässt.

**Schlussbild des Hosts:** Prompten wird mehr wie *Mitarbeiter führen* als wie *Suchmaschine bedienen* — Kontext, Ziel, Leitplanken und Zweck vorgeben, den Rest macht das Modell.

## Für den Hardware-Team-Lead: Relevanz

Das Video ist Coding-lastig (Claude Code, CLAUDE.md, Subagenten), aber vier Regeln sind direkt auf Nicht-Software-Aufgaben übertragbar und decken sich mit [ki-guidelines-hardware-unit.md](../ki-guidelines-hardware-unit.md):

- **Regel 3 + 4 (Warum + Definition of Done)** sind eine gute Vorlage für Auftrags-Prompts im Team-Alltag (z. B. Recherche zu Bauteil-Alternativen, Datenblatt-Vergleich, Normen-Zusammenfassung): Zweck, Empfänger, Fertig-Kriterium und explizite Nicht-Ziele nennen. Das adressiert das in den Guidelines beschriebene Problem "KI hat keinen Begriff von fertig / liefert mehr als verlangt".
- **Regel 2 (Interview zuerst)** entspricht den Guidelines-Punkt "Scope klären statt raten lassen" und Boris Chernys Interview-Prompt aus [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 6 — geeignet als Team-Standard für unscharfe Aufgaben.
- **Regel 7 (Stimme einmal zentral setzen)** ist direkt nutzbar: Ein kurzer Stilblock (knapp, Annahmen und Unsicherheiten kennzeichnen) in Custom Instructions / Projekt-Anweisungen spart Wiederholung im Team.
- **Vorsicht bei Regel 6:** "Verifikation weglassen" gilt laut Video für *Coding-Agenten mit eigener Selbstkorrektur*. Für Hardware-Kontexte (Zahlenwerte, Toleranzen, Normverweise) ist unabhängiges menschliches Gegenprüfen weiterhin nötig — das Video gibt keinen Anlass, dies zu lockern; die Aussage betrifft nur redundante Prompt-Anweisungen, nicht die Verantwortung für das Ergebnis. (Eigene Einordnung, nicht Videoaussage.)

Regeln 1, 5 und das Subagenten-Limit sind vor allem für Claude-Code-Nutzer relevant; das Hardware-Team schreibt keine Software, daher nachrangig.

---

## Plausibilitätscheck

**Im Kern bestätigt (per WebSearch):** Anthropic hat einen offiziellen Leitfaden "Prompting Claude Opus 5" (platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5). Gemäß Suchergebnissen und mehreren Sekundärquellen enthält er tatsächlich: komplette Aufgabe vorab statt tröpfchenweise, Definition of Done, Subagenten nicht für Selbstverifikation oder Kleinaufgaben nutzen, sowie die beiden Umgebungsvariablen `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (Default 3) und `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (Default 20). Die Variablennamen sind zusätzlich im Video-Screenshot der Doku lesbar. Die 80%-Kürzung des Claude-Code-Systemprompts ist bereits in [context-rot-ueberblick.md](../context-rot-ueberblick.md) per WebSearch bestätigt.

**Nicht bestätigt / auffällig:**
- **"Haiku 5.1 ... am 1. September, das leistungsfähigste und am breitesten verfügbare Modell"**: Die Suche fand *kein* Haiku 5.1; Haiku 5.5 wurde laut Ergebnissen erst am 28.09.2026 als "in den kommenden Wochen" angekündigt, Haiku 4.5 gilt als aktuelles Haiku. Am 1. September erschienen laut Suche Fable 5.1 und Mythos 5.1. Die Behauptung, Haiku sei das stärkste Modell, ist in sich unplausibel — vermutlich Übersetzungs-/Erkennungsfehler im Transkript (gemeint wohl Fable 5.1) oder Fehler des Hosts. **Nicht abschließend geklärt.**
- **Opus-5-Release "Ende Juli 2026"**: nicht selbst geprüft.
- **Regeln 2, 3, 5, 6 (Wortlaut-Zitate, "think step-by-step oft schlechter", Caps-Empfehlung)** wurden nicht einzeln gegen die Originaldoku abgeglichen (Doku selbst nicht abgerufen, nur Suchergebnis-Zusammenfassungen). Regel 2 ist laut Host ohnehin keine offizielle Regel.
- **Chernys YC-Zitat** nicht gegen das Original geprüft; im Frame ist ein YC-Setting mit einem Sprecher zu sehen, der Name ist dort nicht eingeblendet.
- Titel ("Anthropic hat 7 neue Regeln verraten") ist leicht clickbaitig: Es sind keine "verratenen Geheimnisse", sondern öffentliche Doku; "7" ist eine Zählung des Hosts, eine der sieben ist zudem Community-Technik.

## Kernbotschaft

Für die Claude-5-Modelle gilt laut Anthropic-Doku und Boris Cherny: weniger Mikromanagement, mehr Führung — vollständigen Auftrag mit Zweck, Leitplanken und Definition of Done geben, begründete statt starre Regeln nutzen, redundante Verifikations- und Schrittanweisungen sowie Caps-Befehle weglassen, den Antwortstil einmal zentral festlegen und Subagenten-Delegation bei Bedarf hart begrenzen. Der Kern ist durch die offizielle Opus-5-Doku gedeckt; einzelne Modell-/Datumsangaben im Video sind fehlerhaft oder unklar.

## Themen-Tags
Prompting, Claude Opus 5, Claude 5, Anthropic Prompting Guide, Boris Cherny, Definition of Done, Exit Criteria, Subagenten, CLAUDE.md, Systemprompt-Kürzung, Verbosity, Interview-Prompt

## Zu prüfen

- **"Haiku 5.1"**: laut WebSearch existiert dieses Modell nicht (1.9.2026: Fable 5.1 / Mythos 5.1; Haiku 5.5 nur angekündigt). Transkriptfehler oder Host-Fehler? Videoton/Originalaudio nicht geprüft.
- **Originaldoku direkt lesen** (Prompting-Guide Opus 5 und ggf. Sonnet-5-Guide), um Wortlaut von Regeln 3, 5, 6, 7 und den Umgebungsvariablen-Defaults zu bestätigen; hier nur über Suchergebnisse verifiziert.
- **Cross-Check mit bestehenden Notizen:** Kein Widerspruch. Überschneidung mit [context-rot-ueberblick.md](../context-rot-ueberblick.md) (80%-Systemprompt-Kürzung, Chernys 6-Monats-Audit), [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 6 (Interview-Prompt) und [loop-engineering-ueberblick.md](../loop-engineering-ueberblick.md) (Exit-Kriterien/Abbruchbedingung, Guardrails). Verwandt: [video-summary-sIWwBfiuEsU.md](video-summary-sIWwBfiuEsU.md), [video-summary-VKMNP_5vOmM.md](video-summary-VKMNP_5vOmM.md) (Opus-5-Verbosity/Output-Styles — passt zu Regel 7), [video-summary-IYzgxWs4sZ4.md](video-summary-IYzgxWs4sZ4.md) (Reasoning-Effort).
- **Mögliche Spannung:** Regel 6 ("keine Verifikationsanweisungen") vs. die Guidelines-Linie "immer gegenprüfen" und die Loop-Engineering-Regel "unabhängige Prüfinstanz". Auflösung wahrscheinlich: Selbstverifikation im Prompt ist redundant, unabhängige Prüfung durch Mensch/anderes System bleibt sinnvoll — nicht durch das Video geklärt.
- **Übertragbarkeit auf Nicht-Coding-Aufgaben** (Hardware-Recherche, Datenblätter): vom Video nicht belegt, nur aus den Prinzipien abgeleitet.

## Nachtrag Faktencheck (2026-09-29)

Unabhängiger Faktencheck (Recherche-Agents plus skeptische Prüf-Agents, Primärquellen per WebFetch). Der bisherige Text oben bleibt unverändert; Abweichungen und Bestätigungen stehen hier. Konfidenz jeweils in Klammern.

- **Prompting-Guide (hoch):** Der offizielle Opus-5-Guide belegt: Verifikationsanweisungen entfernen, Scope klar benennen, Verbosity per Beispiel steuern, Subagent-Limits. Die "7 Regeln" sind die Zählung des Hosts; "Think step-by-step"-Verbot, GROSSBUCHSTABEN und "Definition of Done" standen im abgerufenen Guide nicht.
- **Subagent-Variablen (hoch):** Sie heißen `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (Default 3) und `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (Default 20); Voraussetzung Claude Code ab 2.1.219 (die Doku nennt an anderer Stelle 2.1.217).
- **"Haiku 5.1" (mittel):** Vermutlich nicht existent. Am 01.09.2026 erschienen laut Anthropic Fable 5.1 und Mythos 5.1; Haiku 5.5 und Sonnet 5.5 wurden angekündigt, Sonnet 5.5 kam am 28.09. Beleg nur indirekt, Krieger-Post nicht abrufbar.
