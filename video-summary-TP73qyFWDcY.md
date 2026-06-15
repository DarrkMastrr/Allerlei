# "Type This Into Claude, It'll Make You Build 10x Faster"

**Kanal:** Austin Marchese  
**URL:** https://www.youtube.com/watch?v=TP73qyFWDcY  
**Länge:** 15:12  
**Zusammenfassung erstellt:** 2026-06-15

---

Das Video stellt **6 "Power Phrases"** vor — Formulierungen, die man in Claude Code eintippen soll, um strukturierter und schneller zu bauen.

## Phrase 1: "Launch sub agents"

Statt einem Claude-Chat sequenziell zu arbeiten, lässt man mehrere Claude-Instanzen parallel laufen. Nützlich für:
- Parallele Perspektiven auf dasselbe Problem (jeder Agent sieht die anderen nicht → unabhängige Ergebnisse)
- Tasks, die unabhängig voneinander sind
- Dinge, die man alleine nie angehen würde (Beispiel: 10 Agenten prüfen 10.000 Domains gleichzeitig)

## Phrase 2: "Write me an implementation spec"

Bevor man irgendetwas baut, lässt man Claude einen detaillierten Spec schreiben. Argument: ohne Spec muss Claude Annahmen treffen — bei 3 Schritten mit je 5 Optionen gibt es 125 Kombinationen, mit Spec nur noch 1. Referenz auf Andrej Karpathy, der einen detaillierten Spec-Prozess über Plan Mode stellt.

Wichtigste Zeile im Prompt: *"For each step, show me the key decisions you'd make."* — zwingt Claude, Entscheidungen offenzulegen, bevor es baut.

## Phrase 3: "Interview me"

Statt selbst zu versuchen, Claude genug Kontext zu geben, lässt man Claude einen interviewen. Claude stellt die Fragen, die man selbst nicht kennt. Am Ende fasst es das Interview als Implementation Spec zusammen.

Falle: Nur funktioniert, wenn man die Fragen wirklich durchdenkt — nicht einfach mit Ja/Nein durchklicken. Tipp: Spracheingabe (Hex oder WhisperFlow) macht es natürlicher.

## Phrase 4: "Verify before you build"

Drei Schichten:
1. **Claude.md updaten** — Claude nennt immer erst seinen Verifikationsplan, bevor es baut
2. **Verifikations-Tools aktivieren** — z.B. Hostinger MCP für Deploy-Checks, Brand-Voice-Validator für Content
3. **Human Validation Zones definieren** — hochriskante Bereiche (Zahlungssystem) brauchen menschliche Freigabe; risikoarme Bereiche (UI) können schnell iterieren

## Phrase 5: "Based on this conversation, build me a skill"

Skills nie abstrakt planen — immer aus einer Konversation heraus, die man gerade geführt hat. Der Use Case ist bereits validiert, weil man die Arbeit gerade manuell gemacht hat.

Nach Erstellung: einen **"Gotchas"-Abschnitt** hinzufügen, der Fehler und Edge Cases dokumentiert, damit sie sich nicht wiederholen.

## Phrase 6: "Automate this" ⚠️

Mit Vorsicht verwenden. Zwei Filter vor der Automatisierung:

1. **Taste Test** — braucht der Output menschliches Urteilsvermögen? → augmentieren, nicht automatisieren
2. **80/20 Output Analysis** — wäre 80% Qualität okay? Ja → automatisieren. Nein → augmentieren

Warnung: Zu viele schlecht durchdachte Automationen erzeugen "AI Slop at Scale" und kosten Tokens ohne Mehrwert. Augmentation (KI unterstützt den Prozess) ist oft besser als vollständige Automation.

Die drei mächtigsten Claude-Code-Features für Automation laut Boris Cherney (Creator of Claude Code): **Hooks, Schedule, Loops**.

---

## Kernbotschaft

Nicht bessere Prompts oder größere Modelle sind der Schlüssel — sondern strukturierte Workflows:

**Spec → Interview → parallele Agents → Verifikation → Skills → gezielt automatisieren**
