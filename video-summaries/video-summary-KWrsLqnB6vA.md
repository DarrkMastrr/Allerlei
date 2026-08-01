# "How Claude Code's Creator Starts EVERY Project"

**Kanal:** Austin Marchese
**URL:** https://www.youtube.com/watch?v=KWrsLqnB6vA
**Länge:** 12:16
**Zusammenfassung erstellt:** 2026-07-04

---

## Ausgangspunkt

Austin Marchese hat öffentliche Interviews, Threads und Podcast-Auftritte von Boris Cherny (Erschaffer von Claude Code) ausgewertet, um dessen persönlichen Workflow zu rekonstruieren. Cherny beschreibt sein Setup als "surprisingly vanilla" — er passt Claude Code kaum an. Aus den gesammelten Aussagen leitet Marchese sechs wiederkehrende Prinzipien ab.

## 1. Plan Mode zuerst
- Boris startet ca. 80% seiner Sessions im Plan Mode (Shift+Tab zweimal)
- Prinzip: "Move slow to move fast"
- Empfohlener Prompt: *"Before we start building, interview me about this. What are the core problems this solves? Who is this for? What does success look like? And what should this not do? Summarize it back to me before we write any code."*

## 2. CLAUDE.md möglichst schlank halten
- Boris' eigene Datei ist laut ihm nur "ein paar tausend Tokens" lang
- Seine radikale Empfehlung bei Bloat: die Datei komplett löschen und neu anfangen
- Vorsichtigerer Mittelweg: *"Update my CLAUDE.md to remove anything that's no longer needed, contradictory, duplicate information, or unnecessary bloat impacting effectiveness."*

## 3. Verifikation als Feedback-Loop
- Zitat: *"Give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."*
- Zwei Schritte: (1) Claude ein Tool geben, mit dem es das Ergebnis seiner Arbeit sehen kann, (2) Claude darüber informieren
- Generelle CLAUDE.md-Zeile: *"Before you do any work, mention how you could verify that work."*
- Zusätzlich: *"Please go back and verify all your work so far. Make sure you used best practices, were efficient, and didn't introduce any issues."*

## 4. Sich selbst multiplizieren (parallele Sessions)
- Boris nutzt Git Worktrees, um 3-5 Claude-Sessions parallel laufen zu lassen, jede auf eine klar abgegrenzte, nicht überlappende Aufgabe fokussiert
- Zitat: *"Two context windows that don't know about each other tend to get better results."*

## 5. "Inner Loops" systematisieren
- Wiederkehrende Alltagsaufgaben werden über Slash Commands automatisiert (`.claude/commands/`, versioniert in Git)
- Claude Skills: dokumentierte, wiederholbare Prozesse (Analogie: Prompt = "dribble the ball", Skill = "der einstudierte Spielzug")
- Einstiegs-Prompt: *"Based on the project I'm working on, what Claude Skills should I create?"*

## 6. Für die Zukunft bauen
- Boris zitiert "The Bitter Lesson" (Rich Sutton): das allgemeinere Modell schlägt langfristig immer das spezifischere/handgetunte — "Never bet against the model"
- Praktische Konsequenz: Zeit nicht in mikro-optimierte Prompts stecken, sondern in den "Information Moat" investieren

---

## Kernbotschaft
Boris Chernys Arbeitsweise basiert auf sechs einfachen Gewohnheiten: gründlich planen bevor gebaut wird, Kontext-Dateien schlank halten, dem Modell eine Verifikationsmöglichkeit geben, mehrere unabhängige Sessions parallel laufen lassen, wiederkehrende Aufgaben als Skills/Slash-Commands dokumentieren, und langfristig in Kontext/Systeme statt in Prompt-Feinschliff investieren.

## Themen-Tags
Claude Code, Agentic Coding, Plan Mode, CLAUDE.md, Prompt-Strategien, Produktivität, Boris Cherny, Claude Skills

## Zu prüfen (falls zutreffend)
- "CLAUDE.md nur ein paar tausend Tokens" — Selbstauskunft, nicht extern verifizierbar
- "2-3x Qualitätssteigerung" durch Verifikations-Loop — anekdotisch, nicht mit Daten unterlegt
- "80% seiner Sessions im Plan Mode" — Selbstauskunft, nicht unabhängig bestätigt
- "3-5 Git Worktrees parallel" als Team-Praxis — Einzelaussage
