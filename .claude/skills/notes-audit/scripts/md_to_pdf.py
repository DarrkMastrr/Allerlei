"""Convert this repo's root-level topic-article Markdown files to readable PDFs under PDFs/.

Scope: only the root-level "Themen-Artikel" (e.g. ai-agent-workflow.md), NOT
video-summaries/*.md and NOT anything under .claude/ or claude-skills/.

Usage:
    python md_to_pdf.py                  # regenerate PDFs for all root-level *.md files
    python md_to_pdf.py foo.md bar.md    # regenerate PDFs for specific files only

Requires (install once per machine): pip install --user markdown xhtml2pdf
"""
import sys
from pathlib import Path

import markdown
from xhtml2pdf import pisa

ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
OUT = ROOT / "PDFs"

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


def convert(md_path: Path, out_path: Path):
    text = md_path.read_text(encoding="utf-8")
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


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    targets = sys.argv[1:] if len(sys.argv) > 1 else default_files()
    ok, failed = [], []
    for fname in targets:
        src = ROOT / fname
        if not src.exists():
            failed.append((fname, "Quelldatei fehlt"))
            continue
        out = OUT / (src.stem + ".pdf")
        try:
            err = convert(src, out)
            if err:
                failed.append((fname, "pisa meldete Fehler"))
            else:
                ok.append(fname)
        except Exception as e:
            failed.append((fname, str(e)))

    print(f"\n{len(ok)} OK, {len(failed)} fehlgeschlagen")
    for fname in ok:
        print(f"  OK   {fname}")
    for fname, reason in failed:
        print(f"  FAIL {fname}: {reason}")
