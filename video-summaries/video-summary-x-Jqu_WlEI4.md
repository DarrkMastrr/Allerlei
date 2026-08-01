# "This Free File Makes Claude Code 10x Cleaner (Karpathy Skills)"

**Kanal:** AI Stack Engineer
**URL:** https://www.youtube.com/watch?v=x-Jqu_WlEI4
**Länge:** 09:04
**Zusammenfassung erstellt:** 2026-07-04

---

## Ausgangspunkt: Karpathys Beobachtung

- Andrej Karpathy postete einen viel beachteten Thread auf X über seinen veränderten Coding-Workflow: von 80% manuellem Coding / 20% Autocomplete (November) zu 80% Agent-Coding / 20% Edits (Dezember) — er "programmiert jetzt hauptsächlich in Englisch"
- Der eigentlich interessante Teil des Threads waren nicht die Produktivitätsgewinne, sondern die **Fehlermuster von Coding-Agenten**: keine Syntaxfehler mehr, sondern tiefere, unauffällige Fehler
- Agenten treffen stillschweigend Annahmen, wählen eine von mehreren möglichen Interpretationen aus und ziehen sie durch, ohne nachzufragen

## Die vier Kernprobleme

- **Silent Assumptions:** Bei einer mehrdeutigen Aufgabe wählt der Agent automatisch die komplexeste Interpretation statt nachzufragen
- **Over-Engineering:** Aus einer einfachen Funktion wird eine 200-Zeilen-Utility-Klasse mit Builder-Pattern für nie eintretende Edge Cases
- **Scope Creep bei Edits:** Ein Bugfix wird begleitet von Reformatierung, Umbenennungen und Refactoring benachbarter Funktionen
- **Fehlende Verifikation:** Der Agent meldet "fertig", ohne getestet zu haben, ob Edge Cases wirklich funktionieren

## Die Lösung: claude.md von Forrest Chang

- Entwickler Forrest Chang destillierte Karpathys Beobachtungen in eine einzige Markdown-Datei ("claude.md", ca. 50 Zeilen) im GitHub-Repo **"andrej-karpathy-skills"**
- Vier Prinzipien, je einem der obigen Probleme zugeordnet:
  - **Think Before Coding** — Annahmen explizit benennen, bei Unklarheit nachfragen statt raten
  - **Simplicity First** — nur den minimal nötigen Code schreiben, keine spekulativen Features/Abstraktionen
  - **Surgical Changes** — nur anfassen, was nötig ist; keine Refactorings an unbeteiligtem Code
  - **Goal-Driven Execution** — Aufgaben in verifizierbare Ziele umwandeln, mit Erfolgskriterien statt vager Anweisungen

## Installation (zwei Wege)

- **Option A (empfohlen): Claude Code Plugin** — `/plugin marketplace add forrestchang/andrej-karpathy-skills`, dann `/plugin install andrej-karpathy-skills@karpathy-skills`
- **Option B: CLAUDE.md pro Projekt** — Datei per `curl` direkt ins Projektverzeichnis laden

## Praxisdemo: E-Commerce-Dashboard

- Prompt: "Build an e-commerce dashboard page that shows total revenue, order count, top products, and a recent orders table. Use React and Tailwind. Keep it simple."
- Mit aktivierten Guidelines fragt der Agent zuerst nach: echte API oder Hardcoded-Daten? Responsive oder Desktop-only? Filter/Datumsauswahl nötig?
- Nach Klärung baut der Agent genau das Angeforderte: eine Datei, ca. 120 Zeilen, ohne Router, State-Management, Auth-Wrapper oder Dark-Mode-Toggle
- Der Diff entspricht exakt der Anfrage — keine überraschenden Änderungen an anderen Dateien

## Trade-off

- Die Guidelines priorisieren Vorsicht über Geschwindigkeit — für triviale Aufgaben ist die volle Rigorosität nicht nötig

---

## Kernbotschaft
Coding-Agenten treffen stille Annahmen, bauen zu viel, greifen unnötig in fremden Code ein und verifizieren ihre Arbeit nicht. Eine einzige, rund 50-zeilige CLAUDE.md-Datei mit vier klaren Prinzipien (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) korrigiert diese Muster spürbar.

## Themen-Tags
Claude Code, Agentic Coding, CLAUDE.md, Karpathy, Prompt Engineering, Coding Guidelines

## Zu prüfen — GEPRÜFT (2026-07-04)
- Repo-Sternezahl "über 26.000" — **veraltet/zu niedrig.** Das echte Repo ist `multica-ai/andrej-karpathy-skills` (auch via `github.com/forrestchang/andrej-karpathy-skills` erreichbar), erstellt von Forrest Chang am 27.01.2026, MIT-Lizenz, Stand Anfang Juli 2026 bei ca. 165.000–187.000 Stars. Owner-Name und Install-Befehl (`forrestchang/...`) in diesem Video sind korrekt, nur die Sternezahl ist überholt. Siehe [karpathy-claude-md-guidelines.md](karpathy-claude-md-guidelines.md) für den vollständigen Abgleich gegen [video-summary-5DuHZrtmwoY.md](video-summary-5DuHZrtmwoY.md).
- Karpathys angegebene Verschiebung von 80%/20% zu 20%/80% manuell/Agent — beruht auf seinem eigenen X-Post, nicht unabhängig verifiziert, aber plausibel/bekannt.
