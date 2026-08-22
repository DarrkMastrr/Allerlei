# "Claude Loops in der Praxis: 2 Live-Praxis-Beispiele (Schritt-für-Schritt)"

**Kanal:** Cristian Gebauhr
**URL:** https://www.youtube.com/watch?v=u2v17HBnhh8
**Länge:** 11:57
**Zusammenfassung erstellt:** 2026-08-22

---

*Siehe auch: [video-summary-NeyVq965bOM.md](video-summary-NeyVq965bOM.md) und [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) — beide erklären `/goal` bereits konzeptionell inkl. Kurzbeispiel ("Baue eine Landingpage", "fertig wenn: läuft auf Mobilgeräten..."), aber ohne durchgehend am Bildschirm gezeigten, vollständigen Ablauf. Dieses Video liefert genau das: zwei komplett am Bildschirm mitverfolgte `/goal`-Durchläufe mit echtem Prompt-Text, echtem generierten Skript und echtem Ergebnis. Auch [video-summary-LwhB_6VBwTQ.md](video-summary-LwhB_6VBwTQ.md) (Kontrollsatz vs. objektives Kriterium) und [video-summary-SFtiPOTLBHA.md](video-summary-SFtiPOTLBHA.md)/[video-summary-4NqKZerJpk8.md](video-summary-4NqKZerJpk8.md) (Loop-Engineering-Einordnung) sind thematisch verwandt.*

## Einleitung: Wann Prompt, wann Loop?

Der Host (Cristian Gebauhr) stellt die Grundunterscheidung an den Anfang: Ein einfacher Prompt reicht, wenn ein Ergebnis nicht verifiziert werden muss (Beispiele: "Schreib mir einen Social-Media-Post", "Gib mir fünf Ideen, wie ich Geld anlegen kann"). Ein Loop lohnt sich, sobald ein Ergebnis geprüft werden kann und soll — etwa "Wir haben eine Webseite erstellt, prüfe die Webseite auf Fehler" oder "Wir haben Dateien, prüfe die Dateien auf Fehler". Als Voraussetzung nennt er die kostenpflichtige Claude-Pro-Variante ("15 Euro") sowie die lokal installierte Claude-Code-App (nicht die Web-/Sandbox-Variante), weil Loops Zugriff auf den lokalen Dateikontext brauchen.

## `/loop` vs. `/goal`: zwei verschiedene Slash-Befehle

Im Slash-Menü von Claude Code zeigt der Host zwei Befehle:
- **`/loop`** — zeitbasiert: Man gibt eine Laufzeit vor (10 Minuten, eine Stunde, ein Tag), es gibt aber kein inhaltliches Ende.
- **`/goal`** — ergebnisbasiert: Der Agent arbeitet so lange, bis eine explizit definierte Bedingung erfüllt ist (z. B. "bis alle 12 Punkte stimmen").

Diese Unterscheidung deckt sich mit der bereits im Repo dokumentierten "zielbasiert vs. zeitbasiert"-Einordnung (siehe [video-summary-NeyVq965bOM.md](video-summary-NeyVq965bOM.md), "Vertrauensleiter").

## Praxisbeispiel 1: Fehlerhafte Demo-Webseite prüfen und fixen

Der Host hat vorab mit Claude eine Demo-Landingpage für einen fiktiven SEO-Freelancer ("Mark Böhnke – SEO", Hamburg) bauen lassen und bewusst Fehler einbauen lassen (Datei `demo-kaputt.html`). Ziel: zeigen, wie ein `/goal`-Loop diese Fehler eigenständig findet und korrigiert.

**Die 12 Prüfpunkte** (laut Frame wörtlich im Prompt an Claude formuliert, verteilt auf vier Kategorien):
- *SEO:* genau eine H1 vorhanden; Title-Tag zwischen 30–60 Zeichen; Meta-Description vorhanden (120–160 Zeichen, gültig); `lang="de"` gesetzt; LocalBusiness-Datenmarkierung vorhanden und gültig
- *Technik:* alle Menü-Links (Leistungen, Ablauf, Preise, Kontakt) führen irgendwohin; keine Fehler in der Browser-Console; HTML ist gültig
- *Barrierefreiheit:* jedes Bild hat einen Alt-Text; Überschriften-Reihenfolge stimmt (keine H4 nach H2); Kontrast der Buttons ausreichend
- *Mobil:* kein waagerechtes Scrollen bei 375 px Breite

Bemerkenswert (nur im Frame sichtbar, im gesprochenen Text nicht erwähnt): Nicht der Host selbst hat das Prüfskript geschrieben, sondern er hat **Claude gebeten, ein Bash-Skript `check.sh` zu schreiben**, das genau diese 12 Punkte automatisiert testet ("Jeder Check soll eine Zeile mit ✅ oder ❌ ausgeben. Am Ende exit 0, wenn alles grün ist, sonst exit 1."). Im Chat-Verlauf ist zu sehen, dass Claude dabei selbständig zwei Bugs im eigenen Prüfskript fand und behob (eine fehlende `.js`-Endung bei `node --check`, ein Umlaut-Encoding-Problem in der Konsole), einen Gegentest gegen eine bereinigte Vergleichsdatei fuhr (12/12 grün, exit 0) und den Ist-Zustand von `demo-kaputt.html` mit "4 ❌, 8 ✅, exit 1" bestätigte — also exakt die vier bewusst eingebauten Fehler, kein Fehlalarm. Das Skript kombiniert laut Chat-Notiz ein Bash-Grundgerüst mit eingebettetem Python für Umlaut-sichere Zeichenzählung, JSON-LD-Parsing, HTML-Tag-Stack-Prüfung und eine WCAG-Kontrastrechnung.

Danach startet der Host den eigentlichen `/goal`-Lauf mit dem Prompt: *"Die Datei demo-kaputt.html besteht alle Checks in check.sh."* Er verlässt den Rechner ("einen Kaffee trinken gehen"), und Claude arbeitet die Fehler eigenständig ab, bis `check.sh` alle 12 Punkte grün meldet — ohne weiteres Zutun des Hosts.

## Praxisbeispiel 2: Excel-Tabelle mit Rechtschreibfehlern korrigieren

Zweites Beispiel: eine Excel-Datei mit 20 fiktiven Blogpost-Themen (Ernährung/Fitness), die Claude zuvor auf Anweisung mit absichtlichen Rechtschreib- und Grammatikfehlern gefüllt hat. Spaltenaufbau laut Prompt: Titel, Text, Anmerkungen, Status ("geprüft"/"nicht geprüft"). Empfehlung des Hosts: Datei nicht per Drag&Drop in den Chat legen, sondern einen ganzen Ordner für Claude Code freigeben — das liefere bessere Ergebnisse, weil die KI dann direkt im Dateisystem arbeiten kann statt mit einem Chat-Anhang.

Der `/goal`-Prompt für diesen Lauf (im Frame vollständig lesbar):
> "ZIEL: In der Datei Demo_Blogposts_Ernährung_mit_Fehlern.xlsx sind alle Rechtschreib- und Grammatikfehler korrigiert – in Titel, Text UND Anmerkungen.
> PRO DURCHLAUF: 1. Öffne die Datei und nimm dir die ersten 5 Zeilen mit Status 'nicht geprüft'. 2. Korrigiere darin jeden Fehler in Spalte B, C und D. Du korrigierst nur Inhalt, Länge und Aussage bleiben identisch. Du schreibst die Texte NICHT um. 3. Schreibe die korrigierten Texte zurück in dieselben Zeilen. 4. Setze den Status dieser Zeilen auf 'geprüft'. 5. Hänge an korrektur_log.md an: Zeilennummer, jeden Fehler als 'falsch → richtig' mit Anzahl für diese Zeile. Speichere die Datei."

Der Loop arbeitet die 20 Zeilen batchweise in 5er-Gruppen ab und protokolliert pro Durchlauf gefundene und korrigierte Fehler (im Frame als Tabelle "Durchlauf/Zeilen/Fehler/Korrekturen" sichtbar, inkl. eines zusätzlichen Prüfdurchlaufs am Ende, der 0 neue Fehler mehr fand). Laut Host dauerte der komplette Lauf rund fünf Minuten, in denen er nicht eingreifen musste ("Ich war einfach Kaffee trinken"). Am Ende sind laut Host alle Fehler behoben (er nennt "268 Fehler" als Gesamtzahl — diese Zahl war anhand der Frames nicht eindeutig gegenzulesen, siehe Zu prüfen), der Status aller Zeilen auf "geprüft" gesetzt und eine Log-Datei mit den einzelnen Korrekturen angelegt.

## Fazit im Video

Prompts bleiben laut Host sinnvoll für einfache, nicht verifizierbare Aufgaben (Social-Media-Post, Ideenlisten). Loops (konkret: `/goal`) lohnen sich, sobald die KI eigenständig Bedingungen erfüllen, verifizieren, prüfen und korrigieren soll — der Vorteil gegenüber wiederholtem manuellem Nachprompten sei der Zeitgewinn, weil der Mensch nicht mehr jede Runde einzeln gegenlesen und zurückschreiben muss.

## Für den technischen Team-/Gruppenleiter

Dieses Video liefert zwei direkt nachbaubare Vorlagen für Team-Workflows, nicht nur Theorie: (1) **Ein QS-Skript von der KI selbst schreiben und gegentesten lassen** — Claude hat hier nicht nur die Prüfkriterien angewendet, sondern das Prüfwerkzeug (`check.sh`) selbst gebaut, gegen einen bekannten guten Zustand verifiziert und eigene Bugs im Skript behoben, bevor es produktiv lief. Das ist ein brauchbares Muster für Abnahme-Skripte in Hardware-/Software-Reviews: die KI nicht nur Kriterien prüfen lassen, sondern das Prüfskript selbst inklusive Selbsttest erstellen lassen. (2) **Batchweise Datenbereinigung mit Fortschritts-Log** — das Excel-Beispiel (5-Zeilen-Batches, Status-Spalte, Korrektur-Log mit "falsch → richtig") ist ein direkt übertragbares Muster für große, sich wiederholende Datenprüfaufgaben (Stücklisten, Messprotokolle, Dokumentationen), bei denen Nachvollziehbarkeit (wer/was wurde geändert) wichtig ist. Beide Beispiele zeigen zudem konkret die Ordner-statt-Chat-Anhang-Empfehlung, die für die Zusammenarbeit mit lokalen Projektdateien im Team relevant ist.

---

## Kernbotschaft
Das Video zeigt anhand von zwei vollständig am Bildschirm mitverfolgten Beispielen (fehlerhafte Webseite mit 12 SEO/Technik/Barrierefreiheit/Mobil-Kriterien; Excel-Tabelle mit Rechtschreibfehlern), wie der `/goal`-Befehl in Claude Code funktioniert: Man definiert eine klare, prüfbare Zielbedingung (bei Bedarf inklusive eines von der KI selbst geschriebenen und gegengetesteten Prüfskripts), startet den Loop und bekommt erst am Ende ein fertig geprüftes und korrigiertes Ergebnis zurück — ohne zwischenzeitliches manuelles Nachprompten. Der Mehrwert gegenüber bereits im Repo dokumentierten `/goal`-Erklärungen liegt nicht im Konzept selbst (das ist bekannt), sondern in den konkret gezeigten, nachvollziehbaren Prompt-Texten und Ergebnissen beider Durchläufe.

## Themen-Tags
Loop Engineering, Claude Code, /goal, /loop, Verifikationsskript, check.sh, QS-Automatisierung, Excel-Datenbereinigung, Batch-Korrektur, Opus 5, Cristian Gebauhr

## Zu prüfen
- **`/goal` und `/loop` als reale Claude-Code-Befehle bestätigt:** Per WebSearch verifiziert — `/goal` ist ein offiziell dokumentierter Claude-Code-Befehl (offizielle Doku unter code.claude.com/docs/en/goal), der laut mehreren unabhängigen Quellen (MindStudio, Medium, Towards AI) nach jedem Claude-Turn ein separates, kleineres Modell (Standard: Haiku) prüfen lässt, ob die Zielbedingung "erfüllt", "noch nicht erfüllt" oder "unmöglich" ist. Die im Video gezeigte Mechanik (Bedingung definieren, laufen lassen, am Ende Ergebnis abholen) ist damit funktional korrekt beschrieben, auch wenn der zweistufige Verifikations-Mechanismus (separates Prüfmodell) im Video selbst nicht erklärt wird.
- **"15 Euro für Claude Pro" — nur bei Jahresabo zutreffend:** Per WebSearch geprüft: Claude Pro kostet bei monatlicher Abrechnung eher ca. 20–21 € (inkl. MwSt.), der genannte Betrag von "15 Euro" entspricht eher dem Netto-Preis bei jährlicher Abrechnung (ca. 15–18 € netto/Monat). Die Aussage ist also nicht falsch, aber ohne den Hinweis auf Jahresabo leicht irreführend als "der" Pro-Preis dargestellt.
- **Ob Loops zwingend Pro erfordern, nicht unabhängig verifiziert:** Der Host behauptet, ohne Pro-Abo könne man "nicht mit Loops arbeiten". Plausibel, da Claude Code für sinnvolle Nutzung ohnehin ein bezahltes Kontingent (Pro/Max oder API-Guthaben) braucht, aber nicht gezielt recherchiert, ob es dafür eine harte, Loop-spezifische Sperre auf Free-Tier gibt.
- **"268 Fehler" im Excel-Beispiel — Zahl im Frame nicht eindeutig verifizierbar:** Die vom Host genannte Gesamtzahl korrigierter Fehler ("die Gesamtbedingungen hat alle 268 Fehler gefunden") ließ sich anhand der extrahierten Frames (kleine, teils unscharfe Ergebnistabelle) nicht zuverlässig gegenlesen. Die grundsätzliche Aussage (Loop lief mehrere Durchläufe über alle 20 Zeilen, am Ende 0 neue Fehler bei einem zusätzlichen Prüfdurchlauf) ist aber anhand der Frames plausibel bestätigt.
- **Cross-Check gegen bestehende Notizen:** Kein inhaltlicher Widerspruch zu [video-summary-NeyVq965bOM.md](video-summary-NeyVq965bOM.md) oder [video-summary-HASGvvp1M3E.md](video-summary-HASGvvp1M3E.md) — beide beschreiben `/goal` bereits korrekt (zielbasiert, Beispielsyntax vorhanden), aber nur mit einem kurzen Beispielsatz, nicht mit einem vollständig durchgespielten Fall. Der eigenständige Mehrwert dieses Videos liegt also tatsächlich in den zwei konkreten, screenshotbelegten Arbeitsabläufen (inkl. selbst geschriebenem, gegengetestetem Prüfskript), nicht in neuen Konzepten. Cristian Gebauhr als Kanal ist im Repo-Bestand neu (keine anderen Videos dieses Erstellers bisher zusammengefasst).
- **Reihenfolge von Frames und gesprochenem Text nicht immer deckungsgleich:** Einzelne Frame-Inhalte (z. B. der Excel-Erstellungsprompt) tauchten in den extrahierten Standbildern zeitlich früher auf als im Transkript an der Stelle erwähnt, an der sie inhaltlich passen — vermutlich, weil der Bildschirm über längere, ähnlich aussehende Passagen kaum wechselt bzw. das Video geschnitten ist. Für die inhaltliche Zusammenfassung wurde die thematische Reihenfolge (Beispiel 1, dann Beispiel 2) genutzt, nicht die exakte Sekunden-Reihenfolge einzelner Frames.

**Hinweis zum Ablauf:** Native YouTube-Untertitel scheiterten mit HTTP 429; der Whisper-Fallback (Replicate) lief erfolgreich durch und lieferte 175 Segmente für die vollen 11:57 Minuten. Die Zusammenfassung basiert auf dem vollständigen Transkript sowie 28 gezielt ausgewählten der 80 extrahierten Frames (insbesondere die Bildschirmaufnahmen mit Prompt-Texten, Checklisten und Ergebnistabellen, die im gesprochenen Text nur zusammengefasst, aber nicht wörtlich genannt wurden).
