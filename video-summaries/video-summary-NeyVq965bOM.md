# "Prompten ist tot. Nutze lieber Loops... (der komplette Guide)"

**Kanal:** Unfairer Vorteil | KI
**URL:** https://www.youtube.com/watch?v=NeyVq965bOM
**Länge:** 15:59
**Zusammenfassung erstellt:** 2026-08-08

---

*Siehe auch: [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) (5-Stufen-Leiter Prompt→Context→Harness→Loop→Graph), [ai-agent-workflow.md](../ai-agent-workflow.md) (Punkt 8) und [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) — alle drei behandeln bereits das "Loops statt Prompts"-Konzept inkl. desselben Boris-Cherny-Zitats. Diese Zusammenfassung konzentriert sich daher nur auf das, was hier neu bzw. deutlich detaillierter ist: ein vollständiges, eigenständiges Erklärvideo (kein Aufhänger-Zitat, sondern ein "kompletter Guide"), das die Loop-Mechanik strukturell viel tiefer aufbricht als die bisherigen Notizen.*

**Hinweis zum Ablauf:** Native Untertitel wurden erfolgreich per yt-dlp gezogen — allerdings nur als **englische** Spur, obwohl das Video erkennbar deutschsprachig ist (Kanalname, alle Folien-Overlays sind auf Deutsch, z. B. "DAS ALTE MODELL", "WIE MAN EINEN LOOP BAUT", "DIE VERTRAUENSLEITER"). Es handelt sich also um eine automatisch übersetzte/generierte englische Untertitelspur zu deutschem Originalton, nicht um O-Ton. Für diese Zusammenfassung wurden alle 80 Frames gesichtet und dienen als primäre, verlässlichere Quelle für Begriffe und Struktur; das Transkript wurde nur ergänzend für Wortlaut/Zitate herangezogen.

## Aufbau des Videos (4 Kapitel, laut Kapitelmarken im Video selbst)

Das Video ist explizit als Lehrvideo strukturiert (Kapitel-Anzeige unten im Frame sichtbar): **1. Das alte Modell — 2. Der Wendepunkt — 3. Die Mechanik — 4. Die Vertrauensleiter.**

## 1. Das alte Modell: "Ihr wart der Loop"

Der Erklär-Kern (Kapitel 1, ab t≈01:15): Ein LLM wird als "Genie mit Amnesie" beschrieben — brillant bei jeder Einzelaufgabe, aber ohne Gedächtnis zwischen Sitzungen ("sein Gedächtnis ist ein Whiteboard"). Weil das Kontextfenster mit jedem Versuch voller/unübersichtlicher wird, musste der Mensch bisher manuell die Rolle von Manager, Sekretär und Qualitätsprüfer gleichzeitig übernehmen: prompten → Antwort bekommen → kontrollieren → erneut prompten. Zentrale Pointe: **"Ihr wart der Loop"** — Prompt Engineering (2024/2025) war im Kern nur Ersatz dafür, dass der Mensch selbst die fehlende Feedback-Schleife des Modells manuell schließen musste.

## 2. Der Wendepunkt (Kapitel 2, ab t≈04:30)

Zwei parallele technische Verschiebungen werden als Auslöser genannt: (1) **"Agenten haben Hände bekommen"** — Modelle führen Code selbst aus, sehen Fehler direkt, lesen Dateien selbst; (2) Modelle wurden fähig genug, bei Misserfolg die **Strategie zu wechseln statt denselben Fehler zu wiederholen**. Als Beleg werden zwei Screenshots realer Tweets gezeigt (neu gegenüber den bisherigen Notizen, die das Zitat nur als Text kannten):

- **Boris Cherny selbst** (@bcherny), Original-Tweet-Screenshot: *"Two of the most powerful features in Claude Code: /loop and /schedule. Use these to schedule Claude to run automatically at a set interval, for up to a week at a time. I have a bunch of loops running locally: /loop 5m /babysit, to auto-address code review, auto-rebase, and shepherd my PRs to production — /loop 30m /slack-feedback, to automatically put up PRs for Slack feedback every 30 mins — /loop /post-merge-sweeper to put up PRs to address code review comments I missed — /loop 1h /pr-cruiser to close out stale and no longer necessary PRs — lots more! Experiment with turning workflows into skills + loops. It's powerful."*
- **Peter Steinberger** (@steipete), zitiert dazu: *"Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."* — plus ein Repost/Zitat von "Avid", der Cherny mit *"I don't prompt Claude anymore... my job is to write loops"* zitiert.

Als konkrete neue Modellgeneration (Stand des Videos, "Juni 2026") werden **Claude Fable 5** und **"GPT-5.6"** nebeneinander als Beispiele für die "neue Generation" genannt, die 8+ Stunden unbeaufsichtigt laufen und Strategie wechseln kann, statt denselben Ansatz 20-mal zu wiederholen.

## 3. Die Mechanik: die vier Teile eines Loops (Kapitel 3, ab t≈07:00)

Das ist der Kernbeitrag dieses Videos gegenüber den bereits vorhandenen Notizen — eine **strukturelle Zerlegung**, die in den bisherigen drei Quellen so nicht vorkommt:

1. **Die Spec** — was gebaut werden soll
2. **Die Checkliste** — was "fertig" konkret bedeutet (laut Video der wichtigste, meist übersehene Teil)
3. **Der Inspektor** — im Idealfall ein *separates* Modell, das die Arbeit bewertet; der "Handwerker" (Ausführungs-Agent) darf sich nicht selbst abnehmen ("Vier-Augen-Prinzip")
4. **Das Budget** — harte Obergrenze an Versuchen/Token, weil ein Loop per Definition sonst unendlich weiterlaufen würde ("Kostenbremse")

Praxisbeispiel aus dem Video: `/goal "Baue eine Landingpage"`, "fertig wenn: läuft auf Mobilgeräten, alle Links funktionieren" oder "stoppe nach 20 Minuten" — Spec, Checkliste und Budget in einer Zeile.

**Zwei Loop-Arten, dieselbe Vokabel:**
- **Innerer Loop** — Auftrag mit Wiederholungen (versuchen → prüfen → ausbessern → fertig), endet selbst, sobald der Inspektor zufrieden ist, nicht nach fester Zeit.
- **Äußerer Loop** — eine Dauerroutine, die auf festem Zeitplan läuft und dabei ein **Logbuch** liest/schreibt, damit nicht jeder Durchlauf bei null anfängt. Endet erst, wenn der Mensch ihn stoppt.

**Vier Fragen, ob sich ein Loop überhaupt lohnt** (explizit als Checkliste gezeigt): (1) Wiederholt sich die Aufgabe? (2) Gibt es ein klares "fertig"? (3) Könnt ihr euch ein paar Fehlversuche/Tokens leisten? (4) Hat der Agent die nötigen Werkzeuge? Bei einem "Nein" gehört die Aufgabe laut Video **nicht** in einen Loop, sondern bleibt ein einmaliger Prompt.

Ergänzender Grundsatz: **erst Skill, dann Loop** — ein Loop wiederholt nur, was dem Agenten bereits beigebracht wurde; ohne vorher manuell getesteten, funktionierenden Ablauf ("Skill") ergibt Automatisierung keinen Sinn.

**Namensverwirrung explizit adressiert:** Dieselbe Sache heißt je nach Tool anders — Claude Cowork: "Scheduled Tasks"; Claude Code: `/goal` und `/loop`; "Routinen"/`/schedule`. Prinzip überall gleich: Ziel setzen, laufen lassen, prüfen lassen.

## 4. Die Vertrauensleiter (Kapitel 4, ab t≈14:00)

Vier Eskalationsstufen, mit Mitarbeiter-Analogie ("man gibt einem neuen Mitarbeiter am Tag eins nicht die Firmenkreditkarte"):

1. **Rundbasiert** — normaler Chat, jeder Prompt einzeln freigegeben (wie neuer Mitarbeiter, Tag eins)
2. **Zielbasiert** (`/goal`) — läuft bis zur Ziellinie durch, Mensch sieht nur das Endergebnis (wie Mitarbeiter im ersten Monat)
3. **Zeitbasiert** (`/loop`, `/schedule`) — läuft nach festem Zeitplan, Mensch überfliegt Ergebnisse (wie Mitarbeiter nach halbem Jahr)
4. **Proaktiv** — Agent sucht sich Arbeit selbst, Mensch prüft/justiert nur noch (höchste Autonomie, höchstes Risiko)

Ausdrückliche Warnung: Man solle **eine Stufe nach der anderen** erklimmen, nicht direkt bei Stufe 4 einsteigen — "Vertrauen ist, was sich der Loop verdienen muss." Zusätzliches Sicherheitsnetz für den Einstieg: den Loop in den ersten Durchläufen nach jedem Schritt anhalten und nachfragen lassen, um frühzeitig zu merken, wenn er "im Kreis läuft". Ein Loop, der etwas missversteht, verbrennt sonst Tokens und liefert am Ende Unsinn, der wie Arbeit aussieht.

---

## Kernbotschaft
Das Video liefert keine neue Grundthese gegenüber den bereits vorhandenen Notizen (Loops statt Prompts, Boris-Cherny-Zitat) — sein Mehrwert liegt in der **strukturellen Bauanleitung**: Ein Loop besteht aus vier konkreten Bausteinen (Spec, Checkliste, separater Inspektor, Budget), es gibt zwei technisch unterschiedliche Loop-Typen (innerer Loop mit selbstbestimmtem Ende vs. äußerer Loop als zeitgesteuerte Dauerroutine mit Logbuch), eine Vier-Fragen-Checkliste, ob eine Aufgabe überhaupt in einen Loop gehört, und eine vierstufige Vertrauensleiter, um Autonomie schrittweise statt abrupt zu vergeben. Diese Bausteine sind direkt in konkrete Team-Praxis übersetzbar, unabhängig vom übergeordneten "Loop Engineering ist eine Stufe von vielen"-Rahmen, den [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) bereits liefert.

## Themen-Tags
Loop Engineering, Claude Code, Boris Cherny, Peter Steinberger, /goal, /loop, /schedule, Agentic Coding, Claude Fable 5, Vertrauensstufen, Prompt Engineering

## Zu prüfen
- **Boris-Cherny-Tweet-Screenshot: per WebSearch bestätigt.** Der im Video gezeigte Tweet (`/loop 5m /babysit`, `/loop 30m /slack-feedback`, `/loop /post-merge-sweeper`, `/loop 1h /pr-cruiser`) deckt sich mit einem realen Tweet von @bcherny (x.com/bcherny/status/2038454341884154269, laut Suchergebnis vom 30.03.2026). Frühere Suchtreffer zeigen eine kürzere Tweet-Version mit "lots more!.." am Ende — die im Video gezeigte Version mit den vier ausgeschriebenen Beispielen ist plausibel eine längere/vollständigere Fassung desselben Threads, nicht unabhängig Zeile für Zeile gegen den Originaltweet geprüft (kein direkter Zugriff auf X/Twitter).
- **Peter-Steinberger-Zitat und "Avid"-Zitat von Cherny: als real existierende Tweets bestätigt** (per WebSearch gefunden, x.com/Av1dlive/status/2063592868581978517 u.a.). Inhaltlich deckungsgleich mit dem bereits in [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) dokumentierten Zitat.
- **"Claude Fable 5" und "GPT-5.6" als Modellbeispiele:** Fable 5 ist ein real existierendes Anthropic-Modell (siehe [fable-5-modell-sperre.md](../fable-5-modell-sperre.md) in diesem Repo, inkl. Exportkontroll-Kontroverse Juni/Juli 2026). "GPT-5.6" bzw. der im Frame sichtbare Zusatz "SOL" wurde nicht unabhängig verifiziert — plausibel als OpenAI-Modellbezeichnung zum Zeitpunkt der Videoerstellung, aber nicht gegengecheckt.
- **Datierung "seit Mitte 2026" für den Wendepunkt:** eigene, unbelegte Einordnung des Video-Autors, nicht unabhängig geprüft — passt aber grob zur in [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md) genannten Chronologie (dort: Loop Engineering "Juni 2026").
- **Sprachpfad:** Wie oben vermerkt, basiert das Transkript auf einer automatisch generierten/übersetzten englischen Untertitelspur zu deutschem Originalton — exakte deutsche Wortwahl im Video kann von der hier paraphrasierten Fassung leicht abweichen, die Kernaussagen selbst sind durch die deutschen Folien-Overlays (Frames) gegengeprüft und konsistent.
- **Vier-Teile-Modell (Spec/Checkliste/Inspektor/Budget) und Vertrauensleiter:** eigene didaktische Systematisierung des Video-Autors, keine zitierte Quelle/Standard — plausibel und in sich konsistent, aber nicht als "offizielles" Framework von Anthropic o. ä. zu verstehen.
