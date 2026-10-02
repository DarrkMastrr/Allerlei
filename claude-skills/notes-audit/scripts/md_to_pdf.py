"""Convert the current project's root-level topic-article Markdown files to readable PDFs under PDFs/.

Scope: only the root-level "Themen-Artikel" (e.g. ai-agent-workflow.md), NOT
video-summaries/*.md and NOT anything under .claude/ or claude-skills/.

ROOT is always the current working directory, NOT this script's own location
- this skill is installed globally (~/.claude/skills/) and shared across
projects, so it must operate on whichever project it's invoked from. Always
run it from the target project's root directory.

Usage:
    python md_to_pdf.py                  # regenerate PDFs for all root-level *.md files
    python md_to_pdf.py foo.md bar.md    # regenerate PDFs for specific files only

Änderungsmarkierung (gilt für jede Neuerzeugung einer PDF):
    - neuer/geänderter Text seit der vorigen Fassung: blau
    - entfernter Text: in dieser Fassung durchgestrichen, erst in der nächsten Fassung weg
    - Text, der in der vorigen Fassung blau war: wieder schwarz
Als Vergleichsbasis dienen Schnappschüsse der Markdown-Quellen in PDFs/.stand/ (<name>.cur.md =
Stand der letzten Fassung, <name>.prev.md = Stand davor). Beim allerersten Lauf für eine Datei
wird nur der Ausgangsstand gemerkt und nichts markiert. Ein erneuter Lauf ohne inhaltliche
Änderung erzeugt dieselbe Markierung wie zuvor.

Requires (install once per machine): pip install --user markdown xhtml2pdf
"""
import difflib
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown
from xhtml2pdf import pisa

ROOT = Path.cwd()
OUT = ROOT / "PDFs"
CHANGELOG = OUT / "_zuletzt-aktualisiert.txt"

CSS = """
<style>
@page {
    size: A4;
    margin: 2.4cm 2.2cm 2.4cm 2.2cm;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.5;
    color: #1a1a1a;
}
h1 {
    font-size: 19pt;
    color: #0f172a;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 4px;
}
.meta {
    font-size: 8.5pt;
    color: #94a3b8;
    margin-bottom: 18px;
}
h2 {
    font-size: 13.5pt;
    color: #1e3a8a;
    margin-top: 18px;
    margin-bottom: 8px;
    border-bottom: 0.75px solid #cbd5e1;
    padding-bottom: 3px;
}
h3 {
    font-size: 11.5pt;
    color: #1e3a8a;
    margin-top: 14px;
    margin-bottom: 6px;
}
h4 {
    font-size: 10.5pt;
    color: #334155;
    margin-top: 12px;
    margin-bottom: 5px;
}
p { margin: 0 0 9px 0; text-align: left; }
a { color: #2563eb; text-decoration: underline; }
strong { color: #0f172a; }
em { color: #334155; }
ul, ol { margin: 0 0 10px 0; padding-left: 16px; }
li { margin-bottom: 4px; }
code {
    font-family: Courier, monospace;
    background-color: #f1f5f9;
    padding: 1px 3px;
    font-size: 9pt;
}
pre {
    background-color: #f1f5f9;
    padding: 8px;
    font-family: Courier, monospace;
    font-size: 8.5pt;
    border-left: 3px solid #94a3b8;
}
pre code { background-color: transparent; padding: 0; }
blockquote {
    border-left: 3px solid #94a3b8;
    margin: 0 0 10px 0;
    padding-left: 12px;
    color: #475569;
}
hr {
    border: none;
    border-top: 0.75px solid #cbd5e1;
    margin: 14px 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 12px;
    font-size: 9pt;
}
th, td {
    border: 0.5px solid #cbd5e1;
    padding: 5px 7px;
    text-align: left;
}
th {
    background-color: #eff6ff;
    color: #0f172a;
}
</style>
"""


STAND = OUT / ".stand"
BLUE = '<span style="color:#1d4ed8">'


def _wrap(line, start, end):
    """Zeileninhalt in start/end einfassen, ohne die Markdown-Struktur (Liste, Überschrift, Tabelle) zu zerstören."""
    if not line.strip():
        return line
    if line.lstrip().startswith("|"):  # Tabellenzeile: jede Zelle einzeln
        cells = line.strip().strip("|").split("|")
        if all(re.fullmatch(r"\s*:?-+:?\s*", c) for c in cells):
            return line
        return "|" + "|".join(f"{start}{c.strip()}{end}" if c.strip() else c for c in cells) + "|"
    m = re.match(r"^(\s*(?:#{1,6} |[-*+] |\d+\. |> ))(.*)$", line)
    if m:
        return f"{m.group(1)}{start}{m.group(2)}{end}"
    return f"{start}{line}{end}"


def _blue(line):
    return _wrap(line, BLUE, "</span>")


def _mark(prev, cur):
    out = []
    old, new = prev.splitlines(), cur.splitlines()
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == "equal":
            out.extend(new[j1:j2])
            continue
        if tag in ("insert", "replace"):
            out.extend(_blue(line) for line in new[j1:j2])
        if tag in ("delete", "replace"):
            out.extend(_wrap(line, "<del>", "</del>") for line in old[i1:i2] if line.strip())
    return "\n".join(out) + "\n"


def with_markup(md_path: Path, text: str):
    """Markdown-Text mit Änderungsmarkierung gegenüber der vorigen Fassung zurückgeben."""
    STAND.mkdir(parents=True, exist_ok=True)
    cur_f = STAND / f"{md_path.stem}.cur.md"
    prev_f = STAND / f"{md_path.stem}.prev.md"
    if not cur_f.exists():
        cur_f.write_text(text, encoding="utf-8", newline="")
        return text
    cur = cur_f.read_text(encoding="utf-8")
    if cur != text:
        prev_f.write_text(cur, encoding="utf-8", newline="")
        cur_f.write_text(text, encoding="utf-8", newline="")
        prev = cur
    elif prev_f.exists():
        prev = prev_f.read_text(encoding="utf-8")
    else:
        return text
    return _mark(prev, text)


def convert(md_path: Path, out_path: Path):
    text = with_markup(md_path, md_path.read_text(encoding="utf-8"))
    html_body = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "nl2br"],
    )
    html = f"""<html><head><meta charset="utf-8">{CSS}</head><body>
{html_body}
<div class="meta">Quelle: {md_path.name}</div>
</body></html>"""
    with open(out_path, "wb") as f:
        result = pisa.CreatePDF(src=html, dest=f, encoding="utf-8")
    return result.err


def default_files():
    return sorted(p.name for p in ROOT.glob("*.md"))


def write_changelog(created, updated, failed):
    """Overwrite PDFs/_zuletzt-aktualisiert.txt with this run's result, so the
    user can see at a glance which PDFs are new/changed without opening each
    one or checking git dates."""
    lines = [f"PDF-Generierung: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    lines.append(f"Neu erzeugt ({len(created)}):")
    lines += [f"  - {name}" for name in created] if created else ["  (keine)"]
    lines.append("")
    lines.append(f"Aktualisiert ({len(updated)}):")
    lines += [f"  - {name}" for name in updated] if updated else ["  (keine)"]
    if failed:
        lines.append("")
        lines.append(f"Fehlgeschlagen ({len(failed)}):")
        lines += [f"  - {name}: {reason}" for name, reason in failed]
    CHANGELOG.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    targets = sys.argv[1:] if len(sys.argv) > 1 else default_files()
    created, updated, failed = [], [], []
    for fname in targets:
        src = ROOT / fname
        if not src.exists():
            failed.append((fname, "Quelldatei fehlt"))
            continue
        out = OUT / (src.stem + ".pdf")
        was_existing = out.exists()
        try:
            err = convert(src, out)
            if err:
                failed.append((fname, "pisa meldete Fehler"))
            elif was_existing:
                updated.append(fname)
            else:
                created.append(fname)
        except Exception as e:
            failed.append((fname, str(e)))

    write_changelog(created, updated, failed)

    ok = created + updated
    print(f"\n{len(ok)} OK, {len(failed)} fehlgeschlagen")
    for fname in created:
        print(f"  NEU  {fname}")
    for fname in updated:
        print(f"  OK   {fname}")
    for fname, reason in failed:
        print(f"  FAIL {fname}: {reason}")
    print(f"\nDetails: {CHANGELOG.relative_to(ROOT)}")
