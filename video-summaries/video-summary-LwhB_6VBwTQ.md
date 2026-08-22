# "So musst du KI jetzt prompten: Was ist Loop Engineering (Deutsch)"

**Kanal:** Shakeela ZQ
**URL:** https://www.youtube.com/watch?v=LwhB_6VBwTQ
**Länge:** 09:59
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-rRF3pAEQuzM.md](video-summary-rRF3pAEQuzM.md) — selbe Kreatorin (Shakeela ZQ). Der hier erwähnte "Kontextkompressor" ist identisch mit Skill 5 ("Kontext-Kompressor") aus jenem Video.*

## Einleitung: Ein neuer Begriff, aber ist er auch neu?

Die Autorin greift den gerade überall auftauchenden Begriff "Loop Engineering" auf. Ihr erster Gedanke: schon wieder ein neues Wort für etwas, das man längst macht. Ihre These für das Video: Es geht nicht darum, bessere Prompts zu schreiben, sondern darum, wann die KI selbst merkt, dass ihr Ergebnis noch nicht gut genug ist. Sie verweist explizit auf ihr eigenes vorheriges Video (im Frame sichtbar als Thumbnail "Opus 5 — Diese Sätze musst du löschen"), in dem sie empfohlen hatte, bestimmte Kontrollsätze aus Prompts zu streichen — und grenzt das bewusst ab: Kontrollsätze und das, was in diesem Video gezeigt wird, seien nicht dasselbe, der Unterschied sei entscheidend.

## Herkunft des Begriffs

Laut Video kommt "Loop Engineering" aus dem Entwicklerumfeld, aufgebracht von **Boris Cherny** (Erfinder von Claude Code) und **Peter Steinberger**, im Transkript als Entwickler von "Open Cloud" bezeichnet (siehe Korrektur unten). Am 26. Juni habe **Andrew Ng** in seinem Newsletter "The Batch" (DeepLearning.AI) einen ganzen Beitrag dazu geschrieben — als Zeichen dafür, dass mehr dahintersteckt als ein Trend. Wichtig: Andrew Ng beschreibe das Prinzip für Software-Entwicklung: Die Autorin zeigt im Video, warum es genauso für normale Textarbeit gilt. Ein Frame zeigt kurz einen Ausschnitt des zugehörigen DeepLearning.AI/The-Batch-Artikels (Text über "Developer feedback loop" und Coding-Agenten).

## Die drei Stufen: Prompt → Context → Loop Engineering

**Stufe 1 — Prompt Engineering:** Prompts so formulieren, dass man bekommt, was man will (Rolle, Aufgabe, Format, Beispiele). Wichtig, weil ältere Modelle starr waren — ein anderes Wort führte zu spürbar anderem Ergebnis. Daher existieren Prompt-Formeln und Vorlagen. Modelle wurden besser und verstehen auch unpräzise Formulierungen; damit hängt das Ergebnis nicht mehr an der Formulierung allein, sondern daran, was das Modell überhaupt vor sich hat.

**Stufe 2 — Context Engineering:** Nicht mehr *wie* man fragt, sondern *womit* das Modell arbeitet — Dateien, eigene Anweisungen, Projekte, Gedächtnis. Ersetzt Stufe 1 nicht, sondern ergänzt sie (Kontext ist ein Baustein einer guten Prompt-Formel; Context Engineering macht diesen Baustein zur eigentlichen Arbeit). Da Modelle sich mittlerweile selbst Teile der Grundlage holen (suchen, Dateien lesen), hängt der Erfolg nicht mehr nur am Kontext, sondern an dem, was zwischen den einzelnen Runden passiert.

**Stufe 3 — Loop Engineering:** Den Ablauf gestalten, in dem die KI arbeitet — nicht nur die eine Antwort, sondern auch die Runden davor/danach. Drei Leitfragen: Wie oft geht die KI eine Sache durch? Woran misst sie das Ergebnis? Woran erkennt sie, dass sie fertig ist? Auch hier gilt: die vorherigen Stufen fallen nicht weg, es kommt nur eine Ebene obendrauf. Ausdrücklicher Hinweis der Autorin: Das sind keine offiziellen, irgendwo festgeschriebenen Epochen, sondern nur eine Art, die Entwicklung zu sortieren.

## Praxisbeispiel: Produktbeschreibung mit vier Kriterien

Durchgehendes Beispiel: Produkttext für einen Online-Shop mit vier objektiv prüfbaren Kriterien — maximal 300 Zeichen, Material muss vorkommen, keine Superlative, Pflegehinweis am Ende. Bewusst simpel gewählt, weil (a) jedes Kriterium objektiv erfüllt/nicht erfüllt ist und (b) Modelle einfache Aufgaben oft schon im ersten Anlauf treffen — bei komplexeren Aufgaben mit mehreren Dokumenten sieht man den Effekt laut Autorin deutlicher über mehrere Runden.

Erster, "normaler" Prompt liefert eine auf den ersten Blick gute Version, die aber nicht ganz stimmt: Text zu lang, ein Superlativ drin, Pflegehinweis fehlt trotz ausdrücklicher Nennung. Der übliche Weg (den laut Autorin die meisten Nutzer gehen): selbst gegenlesen, Stellen finden, zurückschreiben, wieder gegenlesen — der Mensch bleibt der Prüfer. Bei einem Text kein Problem, bei 20 Produkten potenziell mehrere Stunden Aufwand.

*Hinweis: Der Transkriptabschnitt zwischen ca. 04:58 und 06:26 ist durch ein deutliches Whisper-Transkriptions-Artefakt unbrauchbar (unzusammenhängende deutsch/spanisch/nonsense-Wortfetzen). Die folgende Rekonstruktion stützt sich auf die Frames in diesem Bereich sowie auf den ab ca. 06:26 wieder klaren Transkriptteil.*

Ein erster Reflex wäre, dem Prompt einen generischen Kontrollsatz hinzuzufügen ("Prüfe deine Antwort noch einmal. Füge am Ende einen Verifikationsschritt ein."). Ein gezeigtes Frame demonstriert die Folge: Der Tokenverbrauch steigt (0 → 2.480), es entstehen zwei separate Prüfdurchgänge — "doppelte Wartezeit, doppelte Tokens" — ohne dass die eigentlichen vier Kriterien dadurch zuverlässiger erfüllt werden.

## Kontrollsatz vs. Qualitätskriterium: der entscheidende Unterschied

Ein Kontrollsatz sagt dem Modell, dass es (sich selbst) prüfen soll — ein Kriterium sagt ihm, **woran** es misst. Im Video an drei Paaren gezeigt:
- "Kontrolliere den Text noch mal auf Länge" → **"unter 300 Zeichen"**
- "Achte darauf, dass alles Wichtige drin ist" → **"Material genannt, Pflegehinweis am Ende"**
- "Sei kritisch mit deinem eigenen Entwurf" → **"keine Superlative"**

Begründung: Das Modell kann sich zwar selbst prüfen, aber nur gegen seinen eigenen Maßstab — und der eigene Maßstab des Nutzers steht nirgendwo, solange er ihn nicht hinschreibt.

## Ablauf mit Abbruchbedingung: das Beispiel in drei Runden

Aus dem Prompt wird ein Ablauf mit klarer Fertig- und Abbruchbedingung: *"Schreibe eine Produktbeschreibung für eine Leinenschürze. Die fertige Version erfüllt diese vier Kriterien: unter 300 Zeichen, Material genannt, keine Superlative, Pflegehinweis am Ende. Fertig bist du, wenn alle vier Kriterien erfüllt sind. Wenn du nach fünf Anläufen nicht alle erfüllst, brich ab und sag mir, welches Kriterium fehlt."*

In den gezeigten Frames läuft das Beispiel so:
- **Runde 1:** Entwurf mit 328 Zeichen, Superlativ ("unvergleichlich") enthalten → 2 von 4 Kriterien nicht erfüllt (Länge, keine Superlative)
- **Runde 2:** 238 Zeichen, Superlativ entfernt, aber Pflegehinweis fehlt → 3 von 4 erfüllt
- **Runde 3:** 226 Zeichen, alle vier Kriterien erfüllt → fertig

Erst wenn alle Kriterien erfüllt sind, bekommt der Nutzer überhaupt wieder etwas zu sehen — das ist die Schleife: schreiben, messen, korrigieren, wieder messen, bis die Bedingung erfüllt ist. Wichtig laut Autorin: Im Prompt steht kein einziges Mal das Wort "prüfen" — nur woran gemessen wird und wann es fertig ist. Das eigentliche Prüfen übernehmen viele moderne Modelle mittlerweile von selbst, aber jede Schleife braucht eine Bedingung, die sie auch wieder beendet. Fehlt diese Abbruchbedingung, hört das Modell dann auf, wenn *es selbst* der Meinung ist, dass es reicht — was nicht dasselbe ist wie der Maßstab des Nutzers. Ein separates Frame illustriert das Risiko einer unbegrenzten Schleife plakativ als "Endlosschleife"-Animation mit wachsendem Rundenzähler (Runde 4 nach 7 Sekunden, Runde 11 nach 14 Sekunden, "104 Runden/Minute") bei gleichzeitig schrumpfender Token-Reserve — jede zusätzliche Runde kostet Tokens und Wartezeit.

## Was gehört in die Schleife — und was nicht?

Zentrale Regel des Videos: Alle vier Beispielkriterien haben genau eine richtige Antwort (erfüllt/nicht erfüllt) und brauchen kein Urteil. Als Gegenbeispiel zwei nicht objektiv messbare Vorgaben: der Text solle "zur Marke passen" und die Materialangabe solle stimmen. Beides kann die KI nicht zuverlässig selbst beurteilen — beim Ton fehlt ihr der Maßstab, und ob die Schürze wirklich aus Leinen ist, weiß sie schlicht nicht, solange man es ihr nicht sagt.

Daraus die Faustregel: Alles objektiv Messbare kann als Kriterium in die Schleife (die KI korrigiert sich selbst, bevor der Mensch überhaupt draufschaut); alles, wo Urteil, Geschmack oder Faktenwissen nötig ist, bleibt beim Menschen. Eigenes Beispiel der Autorin: Bei Design-Aufgaben lässt sie nie 30 Entwürfe auf einmal automatisch durchlaufen, sondern arbeitet in kleinen Blöcken, weil Design Geschmack ist und kein messbares Kriterium.

## Warum lange Abläufe schlechter werden: das Kontextfenster

Neben dem reinen Tokenverbrauch nennt die Autorin einen zweiten Grund, Runden knapp zu halten: das Kontextfenster als "Arbeitsspeicher des Modells". Alles, was im Chat steht — Anfrage, hochgeladene Dateien, jede Antwort, jeder Zwischenstand — muss dort hineinpassen. In einem mehrrundigen Ablauf füllt sich dieser Speicher schnell, weil jeder Entwurf und jede Korrektur mit drinbleibt. Ein Frame visualisiert das mit einer sinkenden "Antwortqualität"-Anzeige: Runde 1 bei 94 %, Runde 5 bei 34 %, während sich der Kontext-Behälter füllt. Praktische Konsequenz laut Video: Abläufe so kurz wie möglich halten (nicht 20 Runden, wenn 3 reichen) und bei wirklich langen Chats lieber neu anfangen und nur das Ergebnis mitnehmen statt des ganzen Verlaufs — dafür verweist sie explizit auf ihren eigenen "Kontextkompressor" aus dem Skills-Video.

## Für den technischen Team-/Gruppenleiter

Das Kernprinzip lässt sich unmittelbar auf Team-Prozesse übertragen, nicht nur auf einzelne KI-Prompts: Die Unterscheidung "Kontrollsatz vs. objektives Kriterium" beschreibt letztlich den Unterschied zwischen einer vagen Anweisung ("bitte nochmal drüberschauen") und einem echten Abnahme-/Qualitätskriterium (messbare Checkliste) — ein Muster, das aus Code-Reviews, Spezifikations-Abnahmen oder Prüfprotokollen im Hardware-Umfeld bekannt ist. Übertragen auf Agenten-gestützte Arbeitsabläufe im Team ist die im Video gezeigte Struktur (klare messbare Kriterien + explizite Abbruchbedingung nach n Versuchen + Rückmeldung, welches Kriterium fehlt) ein direkt einsetzbares Muster, um zu verhindern, dass automatisierte Prüf-/Korrekturschleifen unkontrolliert Tokens/Zeit verbrauchen oder scheinbar "fertige" Ergebnisse liefern, die gegen einen impliziten, nirgends dokumentierten Maßstab laufen. Ebenso verwertbar: die klare Trennung, was ein Modell selbst zuverlässig prüfen kann (objektiv messbare Fakten) und was zwingend menschliches Urteil braucht (Geschmack, Markenkonsistenz, Faktenwissen außerhalb des Kontexts) — relevant für die Frage, welche QS-Schritte man in Team-Workflows tatsächlich an einen Agenten delegieren sollte.

---

## Kernbotschaft
"Loop Engineering" beschreibt laut Video keine neue Prompt-Technik, sondern eine dritte Entwicklungsstufe nach Prompt Engineering (wie man fragt) und Context Engineering (womit das Modell arbeitet): das Gestalten des gesamten Ablaufs, in dem eine KI arbeitet — mit expliziten, objektiv messbaren Kriterien statt vager Kontrollsätze und mit einer klaren Abbruchbedingung, damit Schleifen nicht unkontrolliert Tokens, Zeit und Kontextfenster-Qualität verbrauchen. Nicht alles gehört in eine automatische Schleife: nur was sich objektiv messen lässt: Urteil, Geschmack und Faktenwissen bleiben beim Menschen.

## Themen-Tags
Loop Engineering, Prompt Engineering, Context Engineering, KI-Prompting, Qualitätskriterien, Kontextfenster, Andrew Ng, Boris Cherny, Peter Steinberger, Agentische Workflows

## Zu prüfen
- **Peter Steinbergers Projekt "Open Cloud" — vermutlich Whisper-Fehltranskription:** Per WebSearch bestätigt, dass Peter Steinberger tatsächlich einer der beiden viral gegangenen Namen hinter "Loop Engineering" ist — sein Projekt heißt aber **"OpenClaw"**, nicht "Open Cloud". Boris Cherny (Claude Code) und Peter Steinberger (OpenClaw) werden in mehreren unabhängigen Quellen (u. a. Andrew Ngs eigenem X-Post, thenewstack.io) übereinstimmend als Ursprung des viral gegangenen Begriffs genannt — inhaltlich korrekt, nur der Produktname im Transkript ist wahrscheinlich verhört.
- **Datum "26. Juni" für Andrew Ngs Newsletter-Beitrag — leicht abweichend:** Recherche deutet auf eine Veröffentlichung um den **30. Juni 2026** hin (Titel laut Suchtreffern u. a. "Three Key Loops for Building Great Software" auf deeplearning.ai/the-batch), nicht exakt 26. Juni. Kleine Diskrepanz von ca. 4 Tagen, nicht abschließend gegen die Originalquelle geprüft (Artikel selbst wurde nicht direkt aufgerufen) — die grundsätzliche Aussage (Andrew Ng widmete "Loop Engineering" tatsächlich einen eigenen Beitrag in The Batch) ist aber bestätigt.
- **Cross-Check gegen [video-summary-rRF3pAEQuzM.md](video-summary-rRF3pAEQuzM.md):** Kein Widerspruch, sondern direkte Bestätigung/Fortsetzung — der hier erwähnte "Kontextkompressor" ist derselbe Skill 5 ("Kontext-Kompressor") aus dem dortigen Video derselben Kreatorin, für exakt den dort beschriebenen Zweck (langer Chat wird unübersichtlich, Ergebnis statt Verlauf mitnehmen).
- **Verweis auf eigenes Video "Diese Sätze musst du löschen" (Opus 5):** Nur als Thumbnail im Frame sichtbar, im Repo bisher nicht als eigene Zusammenfassung vorhanden — keine Prüfung auf Widerspruch möglich, da Quellvideo nicht im Bestand.
- Die Aussage, dass Modelle "mittlerweile" das Selbst-Prüfen von sich aus übernehmen (ohne expliziten Kontrollsatz), ist eine allgemeine, nicht mit Zahlen/Studien belegte Beobachtung der Autorin — plausibel im Kontext moderner Agenten-Modelle, aber nicht unabhängig verifiziert.
- Die "Kontextfenster füllt sich, Antwortqualität sinkt"-Kernaussage deckt sich inhaltlich mit bereits im Repo dokumentierten Kontext-Engineering-Konzepten (z. B. Empfehlung, Chats bei nachlassender Qualität neu zu starten) — keine neuen Widersprüche gefunden, eher zusätzliche Bestätigung eines wiederkehrenden Repo-Themas.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; zusätzlich schlug der Video-Download selbst zunächst zweimal mit HTTP 403 fehl (behoben durch Update von yt-dlp auf die aktuelle Version). Der Whisper-Fallback lief über Replicate und lieferte 218 Segmente, enthielt aber zwischen ca. 04:58 und 06:26 ein deutliches Transkriptions-Artefakt (nicht-deutscher Wortsalat) — dieser Abschnitt wurde stattdessen anhand der Frames rekonstruiert. Die Zusammenfassung basiert auf allen 80 extrahierten Frames plus dem übrigen, klaren Transkript.
