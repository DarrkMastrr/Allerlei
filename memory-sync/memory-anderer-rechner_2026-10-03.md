# Memory-Abgleich für den anderen Rechner (Stand 2026-10-03)

Zweck: Auf diesem Rechner (Stand-PC / Sandbox-Laptop, je nachdem wo diese Datei gelesen wird) sollen dieselben Memory-Einträge gelten wie auf dem Rechner, auf dem sie überarbeitet wurden: zwei Einträge zu den PDF-Regeln (Änderung vom 2026-10-02), ein neuer Eintrag zu Zusammenfassungen für Nicht-Experten und eine Korrektur im Video-Workflow-Eintrag (beides 2026-10-03). Memory-Dateien werden nicht über Git synchronisiert, deshalb dieser Umweg.

**Anweisung an Claude auf dem anderen Rechner:** Diese Datei lesen, bei jedem Eintrag prüfen, ob schon ein gleichnamiger existiert (dann aktualisieren statt duplizieren), und den genauen Wortlaut dem Nutzer zeigen. Nach der Regel des Nutzers (globale CLAUDE.md) erst nach ausdrücklicher Bestätigung schreiben. Memory-Ordner des jeweiligen Projekts: `~/.claude/projects/<projektordner>/memory/`.

## Vorher auf dem anderen Rechner (Skill-Teil, kommt über Git)

1. `git pull` im Repo `Allerlei`.
2. Die gespiegelten Skills aus `claude-skills/` nach `~/.claude/skills/` übernehmen, mindestens `notes-audit` (neues `scripts/md_to_pdf.py` mit Änderungsmarkierung, neuer Absatz in `SKILL.md`) und `watch-playlist` (neuer Hinweis zur generischen "no API key"-Meldung; neue Vorgaben für ausführlichere, erklärende Zusammenfassungen mit Einleitung und Glossar; neuer Schritt 5b mit unabhängiger Prüf-Schleife, max. 3 Durchläufe, Fehler werden als KERN oder DETAIL eingestuft; Warnzeile "Prüfstatus: ACHTUNG" nur bei KERN-Fehlern nach Durchlauf 3, bei nur Detailfehlern eine neutrale Zeile); Korrekturen werden komplett nachgelesen; einheitliche Beleg-Stufen (Volltext / Tool-Zusammenfassung / Suchtreffer / nicht abrufbar); Prüfer nennt Revidierungen früherer Korrekturen als REVIDIERT; Arbeitsverzeichnis erst nach Ende der Schleife löschen; erster Lauf bei Token-Provider-Timeout einmal wiederholen. Die alte Projektkopie `.claude/skills/watch-playlist/` wurde aus dem Repo entfernt, es gilt nur die globale Version. Keine festen Home-Pfade eintragen, sondern `~` bzw. `$USERPROFILE` verwenden.
3. Einmalig prüfen: `pip install --user markdown xhtml2pdf` (für `md_to_pdf.py`).
4. Die Schnappschüsse in `PDFs/.stand/` kommen mit dem Pull mit und dürfen nicht von Hand verändert werden.

## Memory-Eintrag 1: `feedback_pdf_new_text_color.md`

```markdown
---
name: feedback-pdf-new-text-color
description: "When rewriting a PDF, color newly added text blue (not black); text that was blue from a previous update turns back to black on the next update"
metadata:
  type: feedback
---

Whenever a PDF is rewritten, newly added text is shown in a color other than black — blue preferred. Text that was colored blue in a previous update is reset to black on the next update, since it's no longer new at that point.

**Why:** The user doesn't want to re-read the entire document to find out what changed when opening an updated PDF — the color makes it visible at a glance.

**How to apply:** Applies to every PDF rewrite, alongside the strikethrough rule ([[feedback_pdf_deletion_workflow]]): new text = blue, removed text = struck through, unchanged = black; blue from the previous version reverts to black. For the topic-article PDFs this is automatic since 2026-10-02: `md_to_pdf.py` (skill `notes-audit`) diffs against snapshots in `PDFs/.stand/` — no manual work, don't hand-edit `.stand/`. For PDFs made any other way, apply the rule manually and diff against the previous version. Don't generate topic PDFs with a different script, or the marking is lost.
```

## Memory-Eintrag 2: `feedback_pdf_deletion_workflow.md`

```markdown
---
name: feedback-pdf-deletion-workflow
description: "When rewriting a PDF, don't delete text outright in the new version — strike it through first, delete only in the version after that"
metadata:
  type: feedback
---

When producing a new version of a PDF, text that would normally be deleted should instead be **struck through** (visible, not removed) in that new version. Only in the version *after that* (i.e. one revision later) should the struck-through text actually be deleted.

**Why:** The user wants to see exactly what is being removed at the point of removal, so they can consciously "delete" that same information from their own memory at the same time — not have it silently disappear between versions.

**How to apply:** Applies to PDF rewrites specifically (not necessarily other file types, unless the user says otherwise) — likely relevant across projects, not just this one. Sequence: version N has old text; version N+1 shows the to-be-removed text struck through (plus whatever new content); version N+2 is the first version where the struck-through text is actually gone. Don't collapse straight to deletion in one step.

**Status:** Confirmed as valid and implemented 2026-10-02 (user approved the `md_to_pdf.py` change). Struck-through text stays for exactly one version, then is dropped. Applies to PDFs of the topic articles; for other file types only if the user says so.
```

## Memory-Eintrag 3 (neu): `feedback_summaries_for_non_experts.md`

```markdown
---
name: feedback-summaries-for-non-experts
description: "Video summaries must be explanatory for a non-expert who is interested in what's new: intro, terms explained, glossary, ~50-80% longer than before"
metadata:
  type: feedback
---

The user is interested in the latest AI developments but is not an expert. Overly condensed video summaries are of no value to them — they couldn't reconstruct the point of the video from them.

**Why:** After the 2026-09/10 batch (8 videos) the user said they couldn't understand the meaning of some summaries; they want explanations, not bare fact lists. Chosen scope: only new videos from now on (existing files stay as they are). Chosen style: explanatory text plus a separate glossary ("Begriffe"), about 50-80 % longer than before — not 2-3x.

**How to apply:** Implemented in the `watch-playlist` skill (Step 2 subagent prompt, plus a question about expert vs. lay readers in Step 0): `## Worum geht es?` at the start, terms explained at first use, reasoning not just claims, `## Begriffe` glossary before `## Kernbotschaft`, target length ~2,000-4,000 words depending on video length. When writing or reviewing summaries or topic articles by hand, apply the same level of explanation. Understandability beats completeness; don't pad. See [[feedback_video_watching_workflow]].
```

## Memory-Eintrag 4 (Änderung): `feedback_video_watching_workflow.md`, Punkt 6

Falls der Eintrag auf dem anderen Rechner existiert: in der Liste unter "the user wants" den Punkt 6 ersetzen.

Alt:

> 6. **The `watch` skill's Whisper/Replicate backend commonly hits HTTP 429** on this machine specifically because of Replicate's own account-credit gate (not a Whisper API limitation) — see [[project_skill_sync_via_allerlei]]. Sub-agents should be told upfront not to wait long on a stuck Whisper transcription; fall back to frames-only and note it in the summary.

Neu:

> 6. **Whisper/Replicate: not every failure means "no key".** HTTP 429 comes from Replicate's account-credit gate (see [[project_skill_sync_via_allerlei]]); the "no API key" message of `watch.py` is generic and appears on any Whisper failure, e.g. the 6-minute timeout on long audio (fix: own 5-minute chunking, worked 2026-09/10). Before giving up: check the key, retry once, chunk videos over ~15 min. Only then fall back to frames-only — and tell the user (frames-only summaries are error-prone, e.g. a wrong number was found that way).

## Memory-Eintrag 5 (neu): `feedback_pdf_single_videos_always.md`

```markdown
---
name: feedback-pdf-single-videos-always
description: "Each new video summary gets its own single-video PDF even if no topic article fits; made via md_to_pdf.convert(), named video-summary-<ID>.pdf"
metadata:
  type: feedback
---

Für jede neu erzeugte Zusammenfassung unter video-summaries/ auch eine Einzelvideo-PDF unter PDFs/ erzeugen, selbst wenn sie (noch) in keinen Themen-Artikel passt. Dateiname `video-summary-<ID>.pdf`, wie die bestehenden. Gilt immer, nicht nur einmalig.

**Why:** Der Nutzer sagte am 2026-10-03 "Mach die PDFs auch wenn sie nirgends aktuell dazu passen" und bestätigte auf Nachfrage "ja immer". Die frühere Praxis (Einzel-PDFs nur auf Wunsch bei Videos ohne Themen-Cluster) gilt damit nicht mehr als Bremse. md_to_pdf.py schließt video-summaries/ selbst aus.

**How to apply:** Nach Abschluss der Prüf-Schleife von watch-playlist `convert()` aus .claude/skills/notes-audit/scripts/md_to_pdf.py importieren und pro neuer Datei aufrufen. Die Namensregel in [[feedback-pdf-single-video-naming]] gilt nur für Themenartikel mit einer Quelle, nicht für diese Rohzusammenfassungs-PDFs.
```

## Zeilen für den Index `MEMORY.md`

Bestehende Zeilen zu diesen Einträgen ersetzen bzw. neu anlegen:

```markdown
- [PDF rewrite deletion workflow](feedback_pdf_deletion_workflow.md) — strike through removed text one version, delete it the version after; automated in md_to_pdf.py since 2026-10-02
- [PDF new-text color](feedback_pdf_new_text_color.md) — new text blue, previous blue back to black; automated in md_to_pdf.py (snapshots in PDFs/.stand/)
- [Summaries for non-experts](feedback_summaries_for_non_experts.md) — explanatory style, intro + glossary, ~50-80% longer; new videos only
- [Single-video PDFs for every new summary](feedback_pdf_single_videos_always.md) — make video-summary-<ID>.pdf per new summary via md_to_pdf.convert()
```

## Hinweis

Alle anderen Memory-Einträge bleiben unverändert. Die übrigen Erkenntnisse (Whisper-Chunking, generische "no API key"-Meldung) stehen zusätzlich im Skill `watch-playlist` und kommen über den Skill-Abgleich mit.
