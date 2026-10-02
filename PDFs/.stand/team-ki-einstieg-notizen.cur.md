# Team-KI-Einstieg — Notizen

Persönliche Auswahl einzelner Punkte aus den Video-Zusammenfassungen, die sich eignen könnten, um Team und Kollegen den Einstieg und das professionelle Vorwärtskommen mit KI leichter zu machen. Wird laufend ergänzt, wenn ein Punkt genannt wird.

Format pro Eintrag: Punkt, Quelle, kurze Einordnung, warum/wie das dem Team helfen könnte.

---

## Punkte

### 1. Beim Projektstart kurz festhalten, wofür das Projekt da ist — auch "nur herumspielen" zählt

**Quelle:** [ai-agent-workflow.md](ai-agent-workflow.md), Punkt 6 ("Plan Mode als Standardeinstieg", Boris Cherny) — dort geht es um Boris' Interview-Prompt vor dem Bauen ("What are the core problems this solves? Who is this for? What does success look like?").

**Eigene Idee dazu:** Die volle Interview-Vorlage aus Punkt 6 ist für ein "richtiges" Projekt gedacht. Für den Teameinstieg reicht eine sehr viel leichtere Version davon: beim Anlegen eines neuen Projekts/Chats kurz in einem Satz festhalten, wofür es gedacht ist — und ausdrücklich zulassen, dass "ich will nur herumspielen, sonst nichts" eine vollwertige, gültige Antwort ist, keine Verlegenheitslösung.

**Warum das dem Team helfen könnte:**
- Nimmt Einsteigern den Druck, KI-Tools immer "richtig" bzw. zielgerichtet einsetzen zu müssen — reines Ausprobieren wird explizit legitimiert statt implizit als unprofessionell empfunden.
- Trotzdem ein Mini-Anker für den Agenten (und für einen selbst beim späteren Wiederfinden): ein Satz reicht, um später zu verstehen "warum habe ich das damals angefangen" — ohne die Hürde eines vollständigen vision.md.
- Lässt sich als eine Zeile in einer Team-Vorlage/einem Onboarding-Snippet festhalten, z. B.: *"Kurz: was willst du hier erreichen? ('nur ausprobieren' ist eine gültige Antwort)"* — niedrigschwelliger Einstieg in die Plan-Mode-Denke aus Punkt 6, ohne dessen volle Formalität von Anfang an zu verlangen.

### 2. Wiederkehrender Check-in-Task statt "einmal einrichten und vergessen"

**Quelle:** [ai-agent-workflow.md](ai-agent-workflow.md), Punkt 7 ("CLAUDE.md schlank halten statt endlos anreichern") — Kernargument dort: Modelle werden von Version zu Version besser, alte Regeln werden überflüssig, deshalb gelegentlich aufräumen statt nur anhäufen.

**Eigene Idee dazu:** Weil sich KI praktisch täglich weiterentwickelt, wäre ein wiederkehrender Task sinnvoll, der werktags zu einer festen Uhrzeit **nachfragt**, ob er die Aufräum-/Review-Aufgabe (z. B. CLAUDE.md-Pflege, aber potenziell auch andere "auf aktuellem Stand halten"-Aufgaben) jetzt erledigen soll — also ein Anstoß mit Rückfrage, kein stillschweigendes Automatisch-Ausführen.

**Warum das dem Team helfen könnte:**
- Löst genau das Problem, das Punkt 7 beschreibt, aber ohne dass es jemand aktiv im Kopf behalten muss — die Erinnerung kommt von selbst, statt dass Bloat sich unbemerkt ansammelt, bis es stört.
- Die Rückfrage-statt-Automatik-Form ist für den Teameinstieg wichtig: niemand soll das Gefühl haben, dass im Hintergrund unbeaufsichtigt Änderungen passieren — das würde Vertrauen kosten, gerade bei Kolleg:innen, die KI-Tools noch nicht lange nutzen.
- **Offener Punkt, den ich beim Umsetzen gegenchecken würde:** Wir hatten das Thema feste Zeitpläne schon einmal verworfen, weil der lokale Rechner nicht durchgehend läuft. Der `schedule`-Skill, der inzwischen zur Verfügung steht, legt aber Cloud-Agenten auf Cron-Basis an — die liefen dann unabhängig davon, ob der lokale Rechner an ist. Das würde die frühere Einschränkung aufheben, müsste aber vor der Umsetzung geprüft werden.
