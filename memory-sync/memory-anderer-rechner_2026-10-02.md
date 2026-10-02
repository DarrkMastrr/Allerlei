# Memory-Abgleich für den anderen Rechner (Stand 2026-10-02)

Zweck: Auf diesem Rechner (Stand-PC / Sandbox-Laptop, je nachdem wo diese Datei gelesen wird) sollen dieselben zwei Memory-Einträge zu den PDF-Regeln gelten wie auf dem Rechner, auf dem sie überarbeitet wurden. Memory-Dateien werden nicht über Git synchronisiert, deshalb dieser Umweg.

**Anweisung an Claude auf dem anderen Rechner:** Diese Datei lesen, bei beiden Einträgen prüfen, ob schon ein gleichnamiger existiert (dann aktualisieren statt duplizieren), und den genauen Wortlaut dem Nutzer zeigen. Nach der Regel des Nutzers (globale CLAUDE.md) erst nach ausdrücklicher Bestätigung schreiben. Memory-Ordner des jeweiligen Projekts: `~/.claude/projects/<projektordner>/memory/`.

## Vorher auf dem anderen Rechner (Skill-Teil, kommt über Git)

1. `git pull` im Repo `Allerlei`.
2. Die gespiegelten Skills aus `claude-skills/` nach `~/.claude/skills/` übernehmen, mindestens `notes-audit` (neues `scripts/md_to_pdf.py` mit Änderungsmarkierung, neuer Absatz in `SKILL.md`) und `watch-playlist` (neuer Hinweis zur generischen "no API key"-Meldung). Keine festen Home-Pfade eintragen, sondern `~` bzw. `$USERPROFILE` verwenden.
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

## Zeilen für den Index `MEMORY.md`

Bestehende Zeilen zu diesen beiden Einträgen ersetzen bzw. neu anlegen:

```markdown
- [PDF rewrite deletion workflow](feedback_pdf_deletion_workflow.md) — strike through removed text one version, delete it the version after; automated in md_to_pdf.py since 2026-10-02
- [PDF new-text color](feedback_pdf_new_text_color.md) — new text blue, previous blue back to black; automated in md_to_pdf.py (snapshots in PDFs/.stand/)
```

## Hinweis

Alle anderen Memory-Einträge bleiben unverändert. In dieser Runde ist kein neuer Eintrag dazugekommen. Die übrigen Erkenntnisse (Whisper-Chunking, generische "no API key"-Meldung) stehen bereits im Skill `watch-playlist` und kommen über den Skill-Abgleich mit.
