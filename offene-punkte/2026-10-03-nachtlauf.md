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

1. **Alle 4 Videos enden mit Prüfstatus-Warnung.** Der Prüfer findet in jedem Durchlauf neue Kleinigkeiten, daher ist die Warnung nicht mehr aussagekräftig. Frage: Fehlerschwere unterscheiden (Kernfehler vs. Kleinigkeit) und die Warnung nur bei Kernfehlern im 3. Durchlauf setzen? Beobachtet: Die Funde werden meist, aber nicht immer, kleiner (die Zahlen sind keine exakte Fehlerzählung, einzelne Punkte sind Sammelpunkte); beim Video `gmZlkrHvkkk` waren es 7 / 9 / 5 Korrekturpunkte.
2. **Prüfer können sich irren.** Zwei Fälle: PyPI-"15 Systeme" wurde von Prüfer 1 als unbelegt bemängelt, von Prüfer 2 mit Quelle bestätigt. Sahara "4 %" meinte Prüfer 2 sei eine Ergänzung, Prüfer 3 fand es im Transkript. Der Wechsel des Prüfers fängt das auf, aber nur, wenn noch ein Durchlauf folgt. Nach Durchlauf 3 bleibt ein Prüfer-Irrtum stehen.
3. **ERLEDIGT (03.10.):** Das ⚠ in der Prüfstatus-Zeile ist im Skill und in den 4 Dateien durch "ACHTUNG:" ersetzt (PDF-Schrift hat das Zeichen nicht).
3b. **ERLEDIGT (03.10.):** Für die 4 neuen Videos wurden Einzelvideo-PDFs erzeugt (`PDFs/video-summary-<ID>.pdf`), obwohl sie in keinen Themen-Artikel eingearbeitet sind. Weg: `convert()` aus `md_to_pdf.py` direkt aufgerufen, weil das Skript `video-summaries/` ausschließt. Noch offen: Soll das künftig für jede neue Zusammenfassung automatisch passieren?
4. **Videos in Themen-Artikel einarbeiten?** Vorschläge, noch nicht gemacht:
   - `nX5RFiNAj_s` und `gmZlkrHvkkk` → `openai-krise-ki-blase.md` bzw. `ki-risiko-warnungen.md` / `ki-sicherheitsvorfaelle-sandbox-escapes.md`
   - `b8SU4cqAWTk` → `ki-zukunftsprognosen.md` (keine UBI-Übersicht im Repo; verwandt: `video-summary-RWDsx8KxtX8.md`, `video-summary-XhvLvqSd8VE.md`)
5. **Skill-Schwächen, die ich beobachtet habe (Wortlaut jeweils zur Bestätigung):**
   - Der Schreib-Agent las nach einer Korrektur oft nicht die ganze Datei nach, dadurch blieben veraltete Reste stehen. Vorschlag: im Korrekturauftrag immer "komplett nachlesen" verlangen (hatte ich ab Durchlauf 2 mündlich so gemacht).
   - Seitenabrufe liefern Tool-Zusammenfassungen, keinen Rohtext. Viele Belege sind daher nur "mittel". Mehrere Quellen (OpenAI-Original, CNBC, Axios, The Decoder, CNN) waren per 403/451 nicht lesbar.
   - Die Meldung "no API key" vom `watch`-Skript war beim 70-Minuten-Video wieder irreführend (Key war vorhanden), ebenso brach der erste Lauf bei zwei Videos mit einem Token-Provider-Timeout ab, der Retry klappte.
   - Im Test von `a_jihWpd8cc` habe ich das Arbeitsverzeichnis zu früh gelöscht (vor Ende der Schleife). Der Skill sagt es richtig, ich habe es nicht eingehalten. Der Prüfer musste die Untertitel neu holen, Frames fehlten.
   - Ein Edit-Skript des Schreib-Agents hat ein Steuerzeichen in einen Dateinamen geschrieben (`download\x0bideo.info.json`). Behoben, andere Dateien sauber.

## Inhaltlich offen (aus den Zusammenfassungen, "Zu prüfen")

- **Namensfrage Sol:** Das Dots-Video nennt "GPT-6.1 Sol", die Notizen führen "GPT-5.6 Sol" bzw. "GPT-6 Sol/Luna". Ob es dasselbe Modell ist, ist ungeklärt. Preise für Dots in den Quellen widersprüchlich (100/200/500 $-Stufen).
- **Repo-Widerspruch OpenAI-Umsatz:** `video-summary-8ufDKUYFnvQ.md` nennt ca. 25 Mrd. ARR (Mai 2026), die neue Zusammenfassung 40 Mrd. Run-Rate (Bloomberg, 13.08.2026). Zeitversatz erklärt es plausibel, nicht aufgelöst.
- **Hutter-Video:** Ob es das dritte oder vierte Everlast-Interview ist, steht nur auf einer Whisper-Halluzinationsstelle. Die 99-%-Berufsliste und das 100-Dollar-Haus kommen vom Host, nicht belegt.
- **Alle vier Dateien:** Frames wurden nur stichprobenartig oder gar nicht gesichtet. Viele Einzelbelege sind nur über Suchtreffer oder Tool-Zusammenfassungen gestützt. Details jeweils im Abschnitt "Zu prüfen".

## Aufräumen / Technik

- **Playlist:** 2 Einträge nicht abrufbar (`1m4ArmuRv_w`, `UoasgyH3ZYU`, vermutlich privat oder gelöscht). Noch nicht angesehen.
- **`~/.config/watch/.env`:** Rechte 644 statt 600 (Hook-Warnung). `chmod 600` nicht ausgeführt.
- **Anderer Rechner:** Nach `git pull` die globale Kopie `~/.claude/skills/watch-playlist/SKILL.md` aus `claude-skills/watch-playlist/SKILL.md` übernehmen.
- **`notes-audit` und `research-verify`:** Projektkopien in `.claude/skills/` gegen die globalen Versionen nicht verglichen.
- **Memory:** Es wurde nichts in die Memory geschrieben (Regel: nur nach Bestätigung). Kandidaten: (a) Prüf-Schleife mit max. 3 Durchläufen und Warnzeile; (b) Einzelvideo-PDFs nicht über `md_to_pdf.py`; (c) ⚠ wird im PDF nicht dargestellt.
- **Kontingent:** Pro Video liefen 1 Schreib-Agent, 3 Prüf-Agents und 3 Korrekturrunden. Das 70-Minuten-Video brauchte allein rund 16 Minuten für Whisper. Bei größerem Rückstand besser in kleinen Batches.
