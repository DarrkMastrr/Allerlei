# "Claude wird immer dümmer" (Playlist-Titel; im Video selbst: "Warum Claude immer dümmer wird...")

**Kanal:** Unfairer Vorteil | KI
**URL:** https://www.youtube.com/watch?v=sIWwBfiuEsU
**Länge:** 07:35
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) — behandelt dieselbe zugrunde liegende Anthropic-Quelle (Thariq Shihipars 80%-Systemprompt-Kürzung) deutlich ausführlicher, aus Claude-Code-Power-User-Sicht. [ai-agent-workflow.md](../ai-agent-workflow.md) (Punkte 6+7) dokumentiert Boris Chernys "CLAUDE.md schlank halten"-Empfehlung bereits allgemeiner. [video-summary-bz1C3dmiOvg.md](video-summary-bz1C3dmiOvg.md), [video-summary-k2rkLm1eA9k.md](video-summary-k2rkLm1eA9k.md) und [video-summary-lKHUKXp-nOA.md](video-summary-lKHUKXp-nOA.md) behandeln ein *verwandtes, aber anderes* "Claude wird dümmer"-Phänomen (Context Rot durch volles Kontextfenster) — Details siehe "Zu prüfen".*

## Kernthese: Nicht das Modell wird schlechter, sondern euer Setup

Der Host (Talking-Head-Format, ruhiges Studio) eröffnet mit der Beobachtung, dass sich Lieblings-KI-Apps über Wochen/Monate paradox verhalten: Die Antworten werden schlechter, obwohl im Hintergrund eigentlich immer bessere Modelle zur Verfügung stehen. Genannte Symptome (Frame-Liste): einfache Sachen gehen daneben ("Dinge, die das alte Modell im Schlaf konnte"), eigene Regeln werden übergangen, Antworten werden länger, obwohl explizit um Kürze gebeten wurde.

Kernbeleg: Anthropic selbst habe kürzlich veröffentlicht, für die neuen Modelle Opus 5 und Fable 5 über 80% der Systemanweisungen von Claude Code gelöscht zu haben — ohne messbaren Leistungsverlust. Im Frame (t=00:34) ist kurz ein X-Post von **@trq212** (Thariq Shihipar) mit dem Artikel "The New Rules of Context Engineering for Claude 5 models" sichtbar — exakt dieselbe Quelle, die [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) bereits unabhängig per WebSearch verifiziert hat (echter Anthropic-Blogpost von Thariq Shihipar, Anthropic Member of Technical Staff). Der Name wird hier nicht ausgesprochen (im Transkript "Entropic" statt "Anthropic" — Whisper-Mishearing, in dieser Zusammenfassung korrigiert), aber der Frame belegt die Quelle eindeutig.

## Warum das passiert: Regeln sammeln sich an

Grafik "Regeln sammeln sich an" zeigt einen wachsenden Balken über vier Zeitpunkte (Woche 1 → Monat 3 → Monat 6 → Heute). Mechanismus laut Video: Eine Regel entsteht, wenn ein *altes* Modell einen Fehler macht, der Nutzer sinngemäß "mach das nie wieder" sagt (auch beiläufig im Chat) und die App das automatisch in die Memory schreibt. Das neuere Modell könnte vieles davon inzwischen von selbst richtig machen — trotzdem schleppt man den kompletten alten Regel-Stapel weiter mit, der teils in Konkurrenz zu den Systemregeln und zur aktuellen Aufgabe steht. Claude muss bei jeder Anfrage abwägen, welche Regel greift — das kostet Kapazität, bevor die eigentliche Arbeit beginnt.

**Konkretes Anthropic-Beispiel (Widerspruch über drei Ebenen):** Systemprompt sagt "schreib keine Kommentare", die eigenen Skills/Anweisungen sagen "dokumentiere, wo es sinnvoll ist", und der eigene Prompt fügt eine dritte Ansage hinzu ("mach das bitte lesbar"). Laut Video verbringt Claude die erste Denkrunde damit, diesen Widerspruch aufzulösen, statt das eigentliche Problem zu lösen — das verbrennt einen Großteil der Kapazität. (Dieselbe "keine Kommentare"-Beispielformulierung taucht praktisch identisch in [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) auf — beide Videos zitieren erkennbar dieselbe Anthropic-Quelle.)

## Die Lösung: Context Engineering

Definition im Frame: "das gezielte Zusammenstellen & Strukturieren von Informationen, Anweisungen und Kontext für eine KI, damit sie eine bestimmte Aufgabe möglichst zuverlässig und effektiv ausführt." Statt die Mischung aus Prompt, Daten, Chat-Verlauf und eigenem Setup über Monate zufällig wachsen zu lassen, soll sie bewusst gesteuert werden. Zur Untermauerung wird ein zweiter, unabhängiger Anthropic-Blogpost gezeigt und zitiert: **"Effective context engineering for AI agents"** (Anthropic Engineering, Frame zeigt Veröffentlichungsdatum 29. Sept. 2025) inklusive des dortigen Diagramms "Prompt engineering vs. context engineering" — **per WebSearch bestätigt**, echter Post des Anthropic-Applied-AI-Teams, erschienen zeitgleich mit Claude Sonnet 4.5 (siehe Quellen unten). Das ist eine andere, ältere Quelle als der oben genannte Thariq-Shihipar-Post zur 80%-Kürzung — das Video kombiniert beide korrekt, ohne sie zu vermischen.

Layer-Aufschlüsselung ("Dein Prompt ist nur eine Schicht"): Prompt (jedes Mal neu), Daten (Dokumente/Tabellen/Code), Chat-Verlauf, System-Prompt (kommt vom Produkt, nicht von dir), Anweisungen & Skills (CLAUDE.md, Projekt-Anweisungen, selbst angelegt), Memory (was sich Claude nebenbei gemerkt hat).

## Boris Cherny: "alle sechs Monate löschen und schauen, was passiert"

Eingespielter Ausschnitt (Quelle laut Frame: Y Combinator) zeigt **Boris Cherny, Head of Claude Code bei Anthropic**, mit dem sinngemäßen Rat: "Alle sechs Monate löschst du deine Anweisungen und schaust, was das Modell dann macht." **Per WebSearch verifiziert** — dieser Ausschnitt stammt von Chernys Auftritt bei YC Startup School 2026 (mit YC-Partnerin Diana Hu) und ist inhaltlich fast wörtlich korrekt: Cherny sagte dort laut mehreren unabhängigen Berichten sinngemäß "every 6 months delete your Claude MD, delete your skills, delete your hooks, see what the model does — it might surprise you", ergänzt um denselben 80%-Systemprompt-Fakt für Opus 5. Die Berichte betonen allerdings, dass Cherny keinen kompletten, dauerhaften Purge meint, sondern ein wiederkehrendes Experiment (minimale Version testen, vergleichen, nur behalten was sich beweist) — das deckt sich mit dem "Rebuild"-Teil des im Video vorgestellten Prompts (archivieren statt löschen), s. u. Im Transkript als "Boris Czerny" verschriftet — korrekter Name Boris Cherny, in dieser Zusammenfassung korrigiert (dasselbe Mishearing-Muster ist bereits an anderer Stelle im Repo dokumentiert, siehe [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md)).

## Die offizielle Lösung für Claude Code: `/doctor`

Anthropic liefert dafür laut Video einen eigenen Befehl `claude /doctor`, der Skills und Anweisungsdateien durchgeht und auf das zurückstutzt, was das neue Modell wirklich braucht (deckt sich mit der ausführlicheren `/doctor`-Beschreibung in [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md): fünf Prüfpunkte, meldet Findings vor jeder Änderung).

## Der copy-paste-fähige Prompt für alle anderen (auch reine Consumer-App-Nutzer)

Zentraler Praxisteil: Wer Claude Code nicht nutzt, hat laut Host dasselbe Problem in Projektanweisungen/Memory der normalen Claude-App — nur ohne sichtbare Datei. Der Host stellt (laut eigener Aussage in der Videobeschreibung verlinkt) einen zweiteiligen Prompt vor, der sich in Claude Code, Codex oder einem normalen Claude-Chat gleichermaßen nutzen lässt:

**Teil 1 — Audit:**
> "Überprüfe jede Anweisung, die du für mich gespeichert oder übernommen hast: CLAUDE.md, Rules-Dateien, Skills, Hooks und Memory. Gehe sie einzeln durch und beantworte jeweils drei Fragen: (1) Würdest du das auch ohne diese Anweisung bereits tun? (2) Behebt sie eine Schwäche, die du inzwischen nicht mehr hast? (3) Steht sie im Widerspruch zu einer anderen Anweisung?"

**Teil 2 — Rebuild:**
> "Erstelle anschließend ein minimalistisches Setup für mich: Behalte nur die Regeln, bei denen du ohne sie tatsächlich Fehler machen würdest. Formuliere diese Regeln so kurz wie möglich und verschiebe alles andere in einen Archiv-Ordner (niemals dauerhaft löschen)."

**Eigenes Beispiel des Hosts:** Eine vor einem Jahr gespeicherte globale Regel ("mach immer einen Fact-Check", damals gegen Halluzinationen älterer Modelle) wurde im Audit als überflüssig erkannt — Opus 5 macht das laut Host inzwischen von selbst — und aus der Memory in den Archiv-Ordner verschoben.

**Praxishinweise:** Wer vorsichtiger vorgehen will, nutzt zunächst nur Teil 1 (Analyse ohne Änderung) und entscheidet danach selbst, was konkret verändert wird. Empfehlung: alle sechs Monate wiederholen, oder sobald spürbar Ballast entstanden ist. Ausnahme: Bei einem komplett frischen Setup (unter 20 Regeln, erst wenige Wochen alt) lieber in Ruhe lassen.

## Für den technischen Team-/Gruppenleiter

- Der zweiteilige Audit/Rebuild-Prompt ist direkt als wiederkehrende Team-Routine übertragbar: gemeinsame CLAUDE.md-/Skill-/Hook-Bestände im Team profitieren genauso von periodischem Ausmisten wie Einzel-Setups — besonders wenn mehrere Personen über Monate unkoordiniert Regeln ergänzt haben (genau das im Video beschriebene Szenario).
- Boris Chernys "alle sechs Monate"-Kadenz ist ein konkretes, von einer Autoritätsperson (Anthropic, Head of Claude Code) stammendes und hier per Websuche verifiziertes Zeitintervall — eignet sich als Kalendertermin/Wiederkehrende-Aufgabe fürs eigene Team-Setup, statt Aufräumen dem Zufall zu überlassen.
- Wichtige Nuance für die Praxis: Cherny selbst meint laut den unabhängigen Berichten kein einmaliges radikales Löschen, sondern einen wiederkehrenden Vergleichstest (minimale Version testen, nur behalten was sich beweist) — passt zum "archivieren statt löschen"-Prinzip im Video und ist der sicherere Ansatz für produktiv genutzte Team-Setups.
- Der `/doctor`-Befehl (für Claude-Code-Nutzer im Team) und der manuelle Audit-Prompt (für alle, die nur die normale Claude-App nutzen) decken zusammen beide im Team wahrscheinlich vorkommenden Nutzungsformen ab.

---

## Kernbotschaft
Das Gefühl, dass Claude über Zeit "dümmer" wird, hat laut diesem Video eine andere Ursache als das Modell selbst: Es sind die eigenen, über Monate angehäuften und teils widersprüchlichen Anweisungen (CLAUDE.md, Skills, Memory), die das Modell bei jeder Anfrage erst auflösen muss, bevor es die eigentliche Aufgabe angeht — belegt durch Anthropics eigene 80%-Systemprompt-Kürzung für die neuesten Modelle ohne Leistungsverlust. Die Lösung ist ein periodischer Audit (Boris Chernys Rat: alle sechs Monate), der nicht blind löscht, sondern gezielt prüft, was ein aktuelles Modell wirklich noch braucht, und den Rest archiviert statt zu vernichten. Beide zentralen Zitate/Quellen (Thariq Shihipars Anthropic-Blogpost, Boris Chernys YC-Startup-School-Auftritt) wurden hier unabhängig per WebSearch bestätigt und sind erstaunlich präzise wiedergegeben — ungewöhnlich sorgfältig für ein reißerisch betiteltes ("Claude wird immer dümmer") Video.

## Themen-Tags
Context Engineering, Claude Code, CLAUDE.md, Boris Cherny, Thariq Shihipar, /doctor, Anthropic Systemprompt-Kürzung, Claude Opus 5, Claude Fable 5, Memory-Bloat, Skills, Y Combinator Startup School, Prompt-Widersprüche, Agentic Coding

## Zu prüfen
- **Starke inhaltliche Überschneidung mit [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md):** Beide Videos zitieren erkennbar denselben Thariq-Shihipar-Anthropic-Blogpost (80%-Systemprompt-Kürzung für Claude 5, inkl. nahezu identischem "keine Kommentare"-Widerspruchsbeispiel) sowie das Claude-Code-`/doctor`-Kommando. Kein Widerspruch — dieses Video ist knapper und für ein breiteres Publikum (auch Nicht-Claude-Code-Nutzer) gehalten, [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) liefert mehr technische Details (alle sechs "Then→Now"-Regeln, TodoWrite-Beispiel) und einen eigenständigen `/doctor+`-Community-Skill.
- **Wichtige Abgrenzung zu einem anders gelagerten, ebenfalls im Repo dokumentierten "Claude wird dümmer"-Phänomen:** [video-summary-bz1C3dmiOvg.md](video-summary-bz1C3dmiOvg.md), [video-summary-k2rkLm1eA9k.md](video-summary-k2rkLm1eA9k.md) und [video-summary-lKHUKXp-nOA.md](video-summary-lKHUKXp-nOA.md) beschreiben "Context Rot" — Antwortqualität sinkt mit der schieren *Tokenmenge* im Kontextfenster (z. B. Context-Arena-Benchmark: Trefferquote fällt von 84% bei 128k auf 76%/25%/10% bei 1M Token, je nach Modell), unabhängig vom Inhalt. Dieses Video beschreibt einen *anderen* Mechanismus: nicht Tokenmenge, sondern *widersprüchliche/veraltete Anweisungen* zwingen das Modell, Kapazität für Konfliktauflösung statt für die Aufgabe zu verwenden. Beide Mechanismen sind real, unabhängig voneinander belegt und verstärken sich in der Praxis wahrscheinlich gegenseitig (mehr Regeln = mehr Tokens im Kontext) — für den Leser aber wichtig, sie nicht zu verwechseln, da die Video-Titel sehr ähnlich klingen ("Claude wird dümmer").
- **Ergänzt (nicht widerspricht) [ai-agent-workflow.md](../ai-agent-workflow.md) Punkt 7** ("CLAUDE.md schlank halten statt endlos anreichern", ebenfalls Boris Cherny): Dort bislang nur allgemein formuliert ("gelegentlich prüfen/aufräumen lassen"), ohne festes Intervall und ohne den hier gezeigten zweiteiligen Audit/Rebuild-Prompt mit den drei konkreten Prüffragen. Dieses Video liefert die genauere, hier per WebSearch verifizierte Quelle (YC Startup School 2026) und ein direkt copy-paste-fähiges Werkzeug — eine sinnvolle Ergänzung der bestehenden Notiz, ohne dass hier andere Dateien bearbeitet wurden (Anweisung: nur die neue Datei anlegen).
- **Whisper-Mishearings korrigiert:** "Entropic" → **Anthropic**; "Boris Czerny" → **Boris Cherny** (letzteres deckt sich mit einem bereits im Repo dokumentierten wiederkehrenden Mishearing-Muster, siehe [video-summary-zNuynCOm5Mc.md](video-summary-zNuynCOm5Mc.md)).
- **Per WebSearch bestätigt:** (1) Anthropics Blogpost "Effective context engineering for AI agents" (Anthropic Engineering, veröffentlicht 29. Sept. 2025, zeitgleich mit Claude Sonnet 4.5) — echt, exakt wie im Frame gezeigt; (2) Boris Chernys "alle sechs Monate löschen"-Zitat samt 80%-Opus-5-Fakt bei YC Startup School 2026 — inhaltlich fast wörtlich bestätigt durch mehrere unabhängige Quellen (u. a. BigGo Finance, Y Combinator selbst auf X). Die 80%-Kürzung für Claude Code/Opus 5/Fable 5 selbst wurde bereits in [video-summary-gQeRjkb_Hlc.md](video-summary-gQeRjkb_Hlc.md) unabhängig verifiziert.
- **Nicht separat nachgeprüft:** Der genaue Wortlaut des im Video gezeigten Audit/Rebuild-Prompts stammt aus der (im Video nur erwähnten, hier nicht abrufbaren) Videobeschreibung des Kanals — hier so übernommen, wie er in den Frames zu lesen war, aber nicht gegen die tatsächliche Videobeschreibung abgeglichen. Das persönliche Beispiel des Hosts (Fact-Check-Regel, die Opus 5 überflüssig gemacht hat) ist eine nicht prüfbare Anekdote.
- **Titel-Diskrepanz:** Playlist-Titel lautet "Warum Claude immer dümmer wird...", das Intro-Slide im Video selbst zeigt "Claude wird immer dümmer" — beide sinngemäß gleich, hier im Dateititel beide Varianten vermerkt.

**Hinweis zum Ablauf:** yt-dlp scheiterte im ersten Versuch mit HTTP 403 (transientes YouTube-Throttling), ein direkter Neuversuch lief beim zweiten Mal fehlerfrei durch. Native Untertitel scheiterten mit HTTP 429 (bekanntes, in [whisper-replicate-rate-limit.md](../whisper-replicate-rate-limit.md) dokumentiertes Muster), der Whisper-Fallback über Replicate lief bei dieser kurzen Videolänge (7:35 Min., unter der 6-Minuten-Cap-Grenze) in einem Stück durch (120 Segmente). Die Zusammenfassung basiert auf dem vollständigen Transkript sowie allen 80 extrahierten Frames — bei diesem sehr text-/grafiklastigen Video (fast jede Kernaussage wird durch eine eingeblendete Folie gestützt) deckten die Frames deutlich mehr ab als bei reinen Talking-Head-Videos üblich, u. a. die Quellenbelege (X-Post, Anthropic-Blogpost-Screenshot, YC-Videoausschnitt) und den vollständigen Wortlaut des Audit/Rebuild-Prompts.

## Quellen der Plausibilitätschecks
- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Y Combinator auf X — Boris Cherny bei Startup School 2026](https://x.com/ycombinator/status/2081787356420718704)
- [BigGo Finance — Claude Code Creator Urges Developers to Delete Your System Prompts Every Six Months](https://finance.biggo.com/news/954a98de-8b79-429f-bd7e-761c27a3b210)
