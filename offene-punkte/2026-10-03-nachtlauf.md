# Offene Punkte nach dem Nachtlauf vom 03.10.2026

Entstanden beim Test der neuen Prüf-Schleife (Schritt 5b im Skill `watch-playlist`) und beim Abarbeiten der Watchlist.

## Was erledigt ist

- **Skill erweitert:** `watch-playlist` hat jetzt Schritt 5b mit Prüf-Schleife (max. 3 Durchläufe, neuer Prüfer pro Durchlauf, Prüfer korrigiert nie, Warnzeile "Prüfstatus" nach Durchlauf 3). Global (`~/.claude/skills/`) und in `claude-skills/` identisch. Die abweichende Projektkopie `.claude/skills/watch-playlist/` wurde entfernt.
- **4 neue Video-Zusammenfassungen** (alle noch nicht in Themen-Artikel eingearbeitet):

| Video | Länge | Korrekturpunkte je Durchlauf (1 / 2 / 3), wie von mir an den Schreib-Agent weitergegeben | Ergebnis |
|---|---|---|---|
| `a_jihWpd8cc` OpenAI Dots Failed Live on Stage (Satirekanal) | 5 min | 6 / 6 / 7 | Prüfstatus-Warnung |
| `nX5RFiNAj_s` Warum es ChatGPT nächstes Jahr nicht mehr gibt | 16 min | 5 / 4 / 4 | Prüfstatus-Warnung |
| `gmZlkrHvkkk` The AI Bubble Just Showed Its First Real Crack | 29 min | 7 / 9 / 5 | Prüfstatus-Warnung |
| `b8SU4cqAWTk` "In 5 Jahren sind ALLE Bürojobs weg!" (Prof. Hutter) | 70 min | 4 / 6 / 6 | Prüfstatus-Warnung |

- **Notizen nachgetragen:** `gpt-6-astra-ueberblick.md` und `ki-modellvergleich-kosten.md` (Nachtrag DevDay: Dots, Sol, Ultrafast), jeweils mit Vorbehalten.
- **PDFs:** Alle 27 Themen-PDFs mit `md_to_pdf.py` neu erzeugt (1 neu: `physik-ki-industrie.pdf`). Nachtrag in den zwei geänderten Artikeln ist blau markiert, geprüft per Seitenbild.

## Zu klären (Entscheidung nötig)

1. **ERLEDIGT (03.10.):** Der Skill stuft Prüffunde jetzt als KERN oder DETAIL ein; die Warnzeile "ACHTUNG" gibt es nur noch bei KERN-Fehlern nach Durchlauf 3, bei nur Detailfehlern eine neutrale Zeile. Einstufung der vier Videos im Nachhinein: `a_jihWpd8cc` und `gmZlkrHvkkk` nur Detailfehler (neutrale Zeile); `nX5RFiNAj_s` (falsch zugeordnetes Albanese-Zitat) und `b8SU4cqAWTk` (Verallgemeinerung in der Kernbotschaft) sind Grenzfälle und bleiben bei ACHTUNG. Offen: Prüfer können die Einstufung zu mild vornehmen; der Skill verlangt eine Begründung und stichprobenartige Kontrolle, ob das reicht, zeigt sich erst im nächsten Lauf.
2. **Prüfer können sich irren.** Zwei Fälle: PyPI-"15 Systeme" wurde von Prüfer 1 als unbelegt bemängelt, von Prüfer 2 mit Quelle bestätigt. Sahara "4 %" meinte Prüfer 2 sei eine Ergänzung, Prüfer 3 fand es im Transkript. Der Wechsel des Prüfers fängt das auf, aber nur, wenn noch ein Durchlauf folgt. Nach Durchlauf 3 bleibt ein Prüfer-Irrtum stehen.
3. **ERLEDIGT (03.10.):** Das ⚠ in der Prüfstatus-Zeile ist im Skill und in den 4 Dateien durch "ACHTUNG:" ersetzt (PDF-Schrift hat das Zeichen nicht).
3b. **ERLEDIGT (03.10.):** Für die 4 neuen Videos wurden Einzelvideo-PDFs erzeugt (`PDFs/video-summary-<ID>.pdf`), obwohl sie in keinen Themen-Artikel eingearbeitet sind. Weg: `convert()` aus `md_to_pdf.py` direkt aufgerufen, weil das Skript `video-summaries/` ausschließt. Noch offen: Soll das künftig für jede neue Zusammenfassung automatisch passieren?
4. **ERLEDIGT (03.10.):** Die drei Videos sind als Nachtrag mit Warnvermerk eingearbeitet: `b8SU4cqAWTk` → `ki-zukunftsprognosen.md`; `gmZlkrHvkkk` und `nX5RFiNAj_s` → `openai-krise-ki-blase.md` und `ki-sicherheitsvorfaelle-sandbox-escapes.md`. PDFs dieser drei Artikel neu erzeugt. Offen: Eine eigene Übersicht zu UBI/Arbeitsmarkt gibt es weiter nicht.
5. **ERLEDIGT (03.10.), vom Nutzer bestätigt:** Fünf Ergänzungen im Skill `watch-playlist`: (1) Schreib-Agent liest nach einer Korrektur die ganze Datei nach und prüft auf Steuerzeichen; (2) einheitliche Beleg-Stufen Volltext / Tool-Zusammenfassung / Suchtreffer / nicht abrufbar, Prüfer nennt Revidierungen als REVIDIERT; (3) erster Lauf bei Token-Provider-Timeout einmal wiederholen; (4) Arbeitsverzeichnis-Pfad im Todo notieren und erst nach Ende der Schleife löschen; (5) Richtwert Kontingent (Batches von höchstens 3 Videos, bei über 50 Minuten rund 15 Minuten Whisper). Ob die Beleg-Stufen den Aufwand lohnen, zeigt der nächste Lauf.

## Inhaltlich offen (aus den Zusammenfassungen, "Zu prüfen")

- **Namensfrage Sol:** Das Dots-Video nennt "GPT-6.1 Sol", die Notizen führen "GPT-5.6 Sol" bzw. "GPT-6 Sol/Luna". Ob es dasselbe Modell ist, ist ungeklärt. Preise für Dots in den Quellen widersprüchlich (100/200/500 $-Stufen).
- **Repo-Widerspruch OpenAI-Umsatz:** `video-summary-8ufDKUYFnvQ.md` nennt ca. 25 Mrd. ARR (Mai 2026), die neue Zusammenfassung 40 Mrd. Run-Rate (Bloomberg, 13.08.2026). Zeitversatz erklärt es plausibel, nicht aufgelöst.
- **Hutter-Video:** Ob es das dritte oder vierte Everlast-Interview ist, steht nur auf einer Whisper-Halluzinationsstelle. Die 99-%-Berufsliste und das 100-Dollar-Haus kommen vom Host, nicht belegt.
- **Alle vier Dateien:** Frames wurden nur stichprobenartig oder gar nicht gesichtet. Viele Einzelbelege sind nur über Suchtreffer oder Tool-Zusammenfassungen gestützt. Details jeweils im Abschnitt "Zu prüfen".

## Aufräumen / Technik

- **Playlist:** ERLEDIGT (03.10.), geprüft: Die 2 nicht abrufbaren Einträge (`1m4ArmuRv_w` auf Position 3, `UoasgyH3ZYU` auf Position 10 von 114) sind laut yt-dlp "Private video", auch mit den Firefox-Cookies des angemeldeten Kontos. Titel und Kanal sind nicht zu ermitteln. Sie gehören also nicht dem angemeldeten Konto oder wurden vom Besitzer auf privat gestellt. Entscheidung des Nutzers: Er kann die Videos selbst auch nicht ansehen. Sie bleiben in der Playlist, das Skript überspringt sie; sie können von Hand in YouTube aus der Playlist entfernt werden (kein Schreibzugriff durch Claude). Kein weiterer Handlungsbedarf.
- **`~/.config/watch/.env`:** ERLEDIGT (03.10.), Entscheidung: Warnung wird ignoriert. Ursache ist kein Skill-Abgleich zwischen den Rechnern, sondern Windows: `chmod 600` hält dort nicht (an einer Kopie getestet, blieb 644), der Hook meldet bei jedem Sitzungsstart 644. Die Datei liegt nicht in Git und ist seit dem 08.06. unverändert.
- **Anderer Rechner:** Nach `git pull` die globale Kopie `~/.claude/skills/watch-playlist/SKILL.md` aus `claude-skills/watch-playlist/SKILL.md` übernehmen.
- **`notes-audit` und `research-verify`:** ERLEDIGT (03.10.): Kopien waren byteidentisch. Auf Entscheidung des Nutzers wurden die Projektkopien unter `.claude/skills/` entfernt; es gibt nur noch global (`~/.claude/skills/`) und die Sync-Kopie (`claude-skills/`). Pfad von `md_to_pdf.py` in `notes-audit/SKILL.md` auf den globalen Pfad umgestellt, Pflegehinweis ("beide Kopien byteidentisch halten") in `notes-audit`, `research-verify` und `watch-playlist` eingefügt, Memory und Sync-Notiz angepasst. Offen: `.claude/settings.json` enthält noch Berechtigungen für den alten Projektpfad (u. a. ein Pfad `c:/Claude/Allerlei/...`), nicht angefasst.
- **Memory:** Es wurde nichts in die Memory geschrieben (Regel: nur nach Bestätigung). Kandidaten: (a) Prüf-Schleife mit max. 3 Durchläufen und Warnzeile; (b) Einzelvideo-PDFs nicht über `md_to_pdf.py`; (c) ⚠ wird im PDF nicht dargestellt.
- **Kontingent:** Pro Video liefen 1 Schreib-Agent, 3 Prüf-Agents und 3 Korrekturrunden. Das 70-Minuten-Video brauchte allein rund 16 Minuten für Whisper. Bei größerem Rückstand besser in kleinen Batches.
