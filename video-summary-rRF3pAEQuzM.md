# "5 Claude Skills, die jeder kennen sollte"

**Kanal:** Shakeela ZQ
**URL:** https://www.youtube.com/watch?v=rRF3pAEQuzM
**Länge:** 12:42
**Zusammenfassung erstellt:** 2026-07-04

---

## Einleitung: Was sind Claude Skills?

Die Autorin erklärt zunächst das Grundprinzip: Claude Skills sind wiederverwendbare Arbeitsanweisungen, technisch im Kern Markdown-Dateien, die festlegen, was Claude tun soll, welche Schritte es befolgen muss und wie das Ergebnis aufgebaut sein soll. Statt in jedem Chat dieselben Anweisungen zu wiederholen, ruft man einmal den passenden Skill auf. Erstellt werden die Skills über den offiziellen `/skill-creator` von Anthropic, der per Rückfragen durch den Erstellungsprozess führt.

## Skill 1 — Präsentationsarchitekt

- Ziel: professionelle Präsentationen nach dem SCR-Framework (Situation, Complication, Resolution) strukturieren
- Der Skill-Creator stellt Rückfragen (Art der Präsentation, Detailtiefe, Zielformat) und baut daraus den Skill
- Test: einfacher Prompt "Präsentation zum Thema Produktivität steigern mit KI" — Claude fragt zunächst gezielt nach fehlenden Kontextinformationen, bevor es liefert
- Ergebnis: vollständige Outline mit Hauptpunkten, Unterpunkten, Timing pro Abschnitt und Sprechernotizen — direkt in ein Präsentationstool übertragbar

## Skill 2 — Aufgabenextraktor

- Löst das Problem: Meeting-Notizen/Transkripte/Sprachnotizen bleiben oft ohne klaren Aufgabenplan
- Basiert auf dem 5W1H-Prinzip; da der Prompt bereits sehr detailliert war, entfielen Rückfragen
- Trennt Hintergrundinfos von handlungsrelevanten Punkten, erkennt Entscheidungen, überführt Action-Items in eine Tabelle, markiert offene Fragen/Abhängigkeiten/Blocker
- Test mit einem bewusst chaotischen, neunseitigen Meeting-Transkript ergab eine strukturierte Tabelle mit Entscheidungen, Deadlines, Verantwortlichen, Prioritäten und nächsten Schritten

## Skill 3 — Qualitätsprüfer (Output-Review)

- Prüft und verbessert bereits erstellte Ergebnisse systematisch statt nur oberflächlich Feedback zu geben
- Zwei Rückfragen: universeller Einsatz + Anzeige konkreter Textstellen, Begründungen und Verbesserungsvorschläge bei erkannten Problemen
- Kategorisiert Probleme nach Typ/Priorität (kritische Fehler, wichtige Verbesserungen, kleine Optimierungen) und listet Punkte, die Claude nicht selbst zuverlässig prüfen kann, separat als "manuelle Prüfpunkte"
- Test am zuvor erstellten Präsentations-Outline deckte u.a. eine Zeitplan-Inkonsistenz (4 Wochen Plan vs. 3 Wochen Next Steps) sowie Timing-, Übergangs- und Konsistenzprobleme auf und lieferte direkt eine verbesserte Endversion

## Skill 4 — Kompaktmodus

- Adressiert unnötig lange Claude-Antworten, die Lesezeit und Output-Tokens kosten
- Antworten werden kürzer/direkter formuliert, ohne Inhalte, technische Details oder nötige Handlungsschritte zu verlieren; drei Abstufungen stehen zur Verfügung
- Wichtige Ausnahme: bei Sicherheitswarnungen, irreversiblen Aktionen oder Schritt-für-Schritt-Anleitungen darf nicht so stark gekürzt werden, dass Missverständnisse entstehen
- Test: Zusammenfassung eines 256-seitigen PDF-Buchs (~77.000 Wörter) — Ergebnis liefert Kernkonzept, die vier Hauptprinzipien und praxisnahe Methoden kompakt statt einer Kapitel-für-Kapitel-Zusammenfassung (Hinweis: das PDF selbst belegt weiterhin Kontextfenster-Platz, nur die Antwortlänge wird reduziert)

## Skill 5 — Kontext-Kompressor

- Für lange Chats/Projekte, die unübersichtlich werden bzw. bei Neustart eines Chats den bisherigen Kontext verlieren würden
- Arbeitet in drei Stufen: Behalten (Ziel, Entscheidungen, Anforderungen, Status, offene Fragen), Verdichten (lange Diskussionen auf Kernaussagen reduzieren) und Entfernen (Smalltalk, veraltete Zwischenstände, verworfene Ideen)
- Erstellt ein strukturiertes "Context Pack" (Projektziel, Hintergrund, Entscheidungen inkl. Begründungen, Anforderungen, aktueller Stand, offene Punkte) inklusive eines fertigen Start-Prompts für einen neuen Chat
- Spart primär Input-Tokens (im Gegensatz zum Kompaktmodus, der Output-Tokens spart)

---

## Kernbotschaft
Das Video zeigt praktisch, wie man mit dem `/skill-creator` fünf konkrete, wiederverwendbare Claude Skills baut, die typische Wissensarbeits-Probleme lösen: Präsentationsstruktur, Aufgabenextraktion aus Meetings, Qualitätskontrolle von Outputs, kürzere Antworten (Output-Token-Ersparnis) und Kontext-Kompression für lange Projekte (Input-Token-Ersparnis). Wer Skills nutzt statt wiederholt dieselben Prompts zu schreiben, baut sich dauerhafte, personalisierte Workflows und kommt schneller zu besseren, konsistenteren Ergebnissen.

## Themen-Tags
Claude Skills, Skill-Creator, Produktivität, Prompt-Engineering, Meeting-Notizen-Analyse, Token-Effizienz

## Zu prüfen (falls zutreffend)
- Das im Video verwendete PDF-Buch wird mit "ungefähr 77.000 Wörtern" auf 256 Seiten beziffert — Plausibilität/Quelle nicht überprüfbar aus dem Video allein
- Konkrete Zahlen aus dem Beispiel-Meeting-Transkript sind fiktive Demo-Daten der Autorin, keine externen Fakten — keine Prüfung nötig

**Hinweis:** Die Whisper-Transkription (via Replicate) enthielt an mehreren Stellen erkennbare Wiederholungsschleifen/Artefakte (u.a. bei 04:58, 08:26, 10:23, 12:22) — die Zusammenfassung stützt sich dort zusätzlich auf die Frames.
