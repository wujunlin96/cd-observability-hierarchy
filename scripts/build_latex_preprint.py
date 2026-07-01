"""Build an arXiv-style LaTeX source package from the Markdown draft."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft" / "main_observability_hierarchy.md"
USED_BIB = ROOT / "references" / "observability_used_references.bib"
FIGURE_PNG = ROOT / "figures" / "interface_wall_filter.png"
OUT = (
    ROOT / "paper"
    if (ROOT / "paper").exists() and not (ROOT / "submission").exists()
    else ROOT / "submission" / "arxiv_cd_observability"
)
SUBMISSION_METADATA = ROOT / "config" / "submission_metadata.json"


SPECIAL = {
    "&": r"\&",
    "%": r"\%",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def latex_escape_text(text: str) -> str:
    return "".join(SPECIAL.get(ch, ch) for ch in text)


def latex_escape_code(text: str) -> str:
    text = text.replace("\\", "/")
    return latex_escape_text(text)


def latex_path_code(text: str) -> str:
    text = text.replace("\\", "/")
    text = text.replace("{", "%7B").replace("}", "%7D")
    return r"\path{" + text + "}"


def load_submission_metadata() -> dict[str, str | bool]:
    defaults: dict[str, str | bool] = {
        "ready_for_build": False,
        "author_name": "",
        "affiliation": "",
        "email": "",
        "funding_statement": "",
        "conflict_of_interest_statement": "",
        "author_contributions": "",
        "ai_assistance_disclosure": "",
    }
    if not SUBMISSION_METADATA.exists():
        return defaults

    metadata = defaults | json.loads(SUBMISSION_METADATA.read_text(encoding="utf-8"))
    if not metadata.get("ready_for_build"):
        return metadata

    required = [
        "author_name",
        "affiliation",
        "email",
        "funding_statement",
        "conflict_of_interest_statement",
        "author_contributions",
        "ai_assistance_disclosure",
    ]
    missing = [
        key
        for key in required
        if not str(metadata.get(key, "")).strip()
        or "TODO" in str(metadata.get(key, "")).upper()
    ]
    if missing:
        raise ValueError(
            "config/submission_metadata.json has ready_for_build=true but incomplete fields: "
            + ", ".join(missing)
        )
    return metadata


def author_latex(metadata: dict[str, str | bool]) -> str:
    if not metadata.get("ready_for_build"):
        return "Author information to be finalized"
    name = latex_escape_text(str(metadata["author_name"]).strip())
    affiliation = latex_escape_text(str(metadata["affiliation"]).strip())
    email = latex_escape_text(str(metadata["email"]).strip())
    return name + r"\\" + "\n" + affiliation + r"\\" + "\n" + r"\texttt{" + email + "}"


def apply_submission_metadata(markdown: str, metadata: dict[str, str | bool]) -> str:
    if not metadata.get("ready_for_build"):
        return markdown
    replacements = {
        "No external funding has been specified for the present draft.": str(
            metadata["funding_statement"]
        ).strip(),
        "No conflicts of interest have been specified for the present draft.": str(
            metadata["conflict_of_interest_statement"]
        ).strip(),
        (
            "To be finalized before submission. The current working record is: "
            "the human researcher supplied the motivating C-D question and research direction; "
            "the AI assistant helped formalize assumptions, derive no-go and interface calculations, "
            "run reproducibility checks, and draft manuscript text."
        ): str(metadata["author_contributions"]).strip(),
        (
            "This draft was prepared with assistance from an AI coding and writing assistant. "
            "The assistant contributed to mathematical organization, literature-boundary auditing, "
            "code execution, figure generation, and prose drafting. All claims, citations, "
            "and calculations require final human verification before submission."
        ): str(metadata["ai_assistance_disclosure"]).strip(),
    }
    for old, new in replacements.items():
        if old in markdown:
            markdown = markdown.replace(old, new)
    return markdown


def stash(pattern: str, text: str, store: list[str]) -> str:
    def repl(match: re.Match[str]) -> str:
        token = f"@@TOKEN{len(store)}@@"
        store.append(match.group(0))
        return token

    return re.sub(pattern, repl, text)


def replace_citations(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        keys = re.findall(r"@([A-Za-z0-9:_-]+)", match.group(0))
        return r"\citep{" + ",".join(keys) + "}"

    return re.sub(r"\[(?:@[A-Za-z0-9:_-]+(?:;\s*)?)+\]", repl, text)


def convert_inline(text: str) -> str:
    text = replace_citations(text)
    store: list[str] = []

    def code_repl(match: re.Match[str]) -> str:
        token = f"@@TOKEN{len(store)}@@"
        store.append(latex_path_code(match.group(1)))
        return token

    text = re.sub(r"`([^`]+)`", code_repl, text)
    text = stash(r"\\\(.+?\\\)", text, store)
    text = stash(r"\\citep\{[^}]+\}", text, store)

    def bold_repl(match: re.Match[str]) -> str:
        token = f"@@TOKEN{len(store)}@@"
        store.append(r"\textbf{" + latex_escape_text(match.group(1)) + "}")
        return token

    text = re.sub(r"\*\*(.+?)\*\*", bold_repl, text)
    text = latex_escape_text(text)
    for i, value in enumerate(store):
        text = text.replace(latex_escape_text(f"@@TOKEN{i}@@"), value)
    return text


def heading_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^\d+(?:\.\d+)*\.\s*", "", text)
    text = re.sub(r"^\d+(?:\.\d+)*\s+", "", text)
    return text


def split_table_row(row: str) -> list[str]:
    text = row.strip()
    if text.startswith("|"):
        text = text[1:]
    if text.endswith("|"):
        text = text[:-1]
    cells: list[str] = []
    current: list[str] = []
    in_inline_math = False
    i = 0
    while i < len(text):
        if text.startswith(r"\(", i):
            in_inline_math = True
            current.append(r"\(")
            i += 2
            continue
        if text.startswith(r"\)", i):
            in_inline_math = False
            current.append(r"\)")
            i += 2
            continue
        ch = text[i]
        if ch == "|" and not in_inline_math:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
        i += 1
    cells.append("".join(current).strip())
    return cells


def column_spec(ncols: int) -> str:
    if ncols == 2:
        return r"@{}>{\raggedright\arraybackslash}X >{\raggedright\arraybackslash}X@{}"
    if ncols == 3:
        return (
            r"@{}>{\raggedright\arraybackslash}p{0.28\textwidth}"
            r" >{\raggedright\arraybackslash}p{0.31\textwidth}"
            r" >{\raggedright\arraybackslash}p{0.31\textwidth}@{}"
        )
    if ncols == 4:
        return (
            r"@{}>{\raggedright\arraybackslash}p{0.18\textwidth}"
            r" >{\raggedright\arraybackslash}p{0.27\textwidth}"
            r" >{\raggedright\arraybackslash}p{0.25\textwidth}"
            r" >{\raggedright\arraybackslash}p{0.22\textwidth}@{}"
        )
    return "@{}" + " ".join([r">{\raggedright\arraybackslash}X"] * ncols) + "@{}"


def convert_table(lines: list[str]) -> list[str]:
    rows = [split_table_row(line) for line in lines if not re.match(r"^\s*\|?\s*:?-{3,}", line)]
    if not rows:
        return []
    ncols = len(rows[0])
    out = [
        r"\begin{center}",
        r"\small",
        rf"\begin{{tabularx}}{{\textwidth}}{{{column_spec(ncols)}}}",
        r"\toprule",
        " & ".join(convert_inline(cell) for cell in rows[0]) + r" \\",
        r"\midrule",
    ]
    for row in rows[1:]:
        padded = row + [""] * (ncols - len(row))
        out.append(" & ".join(convert_inline(cell) for cell in padded[:ncols]) + r" \\")
    out.extend([r"\bottomrule", r"\end{tabularx}", r"\end{center}", ""])
    return out


def extract_front_matter(markdown: str) -> tuple[str, str, str, list[str]]:
    lines = markdown.splitlines()
    title = lines[0].lstrip("# ").strip()
    draft_date = ""
    for line in lines[:8]:
        if line.startswith("Draft date:"):
            draft_date = line.split(":", 1)[1].strip()

    abstract_start = lines.index("## Abstract") + 1
    intro_start = next(i for i, line in enumerate(lines) if line.startswith("## 1."))
    abstract = " ".join(line.strip() for line in lines[abstract_start:intro_start] if line.strip())
    body = lines[intro_start:]
    return title, draft_date, abstract, body


def convert_body(lines: list[str]) -> str:
    out: list[str] = []
    in_math = False
    in_code = False
    in_enum = False
    in_appendix = False
    in_declarations = False
    i = 0

    def close_enum() -> None:
        nonlocal in_enum
        if in_enum:
            out.append(r"\end{enumerate}")
            out.append("")
            in_enum = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            close_enum()
            out.append(r"\end{verbatim}" if in_code else r"\begin{verbatim}")
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue

        if stripped == r"\[":
            close_enum()
            in_math = True
            out.append(r"\[")
            i += 1
            continue
        if stripped == r"\]":
            out.append(r"\]")
            out.append("")
            in_math = False
            i += 1
            continue
        if in_math:
            out.append(line)
            i += 1
            continue

        if stripped.startswith("|"):
            close_enum()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.extend(convert_table(table_lines))
            continue

        image = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if image:
            close_enum()
            caption = convert_inline(image.group(1) or "Finite C-D interface wall filter")
            out.extend(
                [
                    r"\begin{figure}[htbp]",
                    r"\centering",
                    r"\includegraphics[width=0.88\textwidth]{figures/interface_wall_filter.png}",
                    rf"\caption{{{caption}.}}",
                    r"\label{fig:interface-wall-filter}",
                    r"\end{figure}",
                    "",
                ]
            )
            i += 1
            continue

        if stripped.startswith("## "):
            close_enum()
            raw = stripped[3:]
            app = re.match(r"Appendix\s+([A-Z])\.\s*(.+)", raw)
            if app:
                if not in_appendix:
                    out.append(r"\appendix")
                    in_appendix = True
                out.append(rf"\section{{{convert_inline(app.group(2))}}}")
                out.append("")
            elif raw == "Declarations":
                in_declarations = True
                out.append(r"\section*{Declarations}")
                out.append("")
            else:
                out.append(rf"\section{{{convert_inline(heading_text(raw))}}}")
                out.append("")
            i += 1
            continue

        if stripped.startswith("### "):
            close_enum()
            raw = stripped[4:]
            command = r"\subsection*" if in_declarations else r"\subsection"
            out.append(rf"{command}{{{convert_inline(heading_text(raw))}}}")
            out.append("")
            i += 1
            continue

        numbered = re.match(r"^\d+\.\s+(.+)", stripped)
        if numbered:
            if not in_enum:
                out.append(r"\begin{enumerate}")
                in_enum = True
            out.append(r"\item " + convert_inline(numbered.group(1)))
            i += 1
            continue

        if not stripped:
            close_enum()
            out.append("")
            i += 1
            continue

        close_enum()
        out.append(convert_inline(stripped))
        out.append("")
        i += 1

    close_enum()
    return "\n".join(out).strip() + "\n"


def latex_document(
    title: str,
    draft_date: str,
    abstract: str,
    body: str,
    metadata: dict[str, str | bool],
) -> str:
    return rf"""\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{amsmath,amssymb,bm}}
\usepackage{{graphicx}}
\usepackage{{booktabs,tabularx,array}}
\usepackage{{natbib}}
\usepackage{{xurl}}
\usepackage{{hyperref}}
\hypersetup{{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}}
\Urlmuskip=0mu plus 2mu\relax

\title{{{convert_inline(title)}}}
\author{{{author_latex(metadata)}}}
\date{{Draft date: {convert_inline(draft_date)}}}

\begin{{document}}
\maketitle

\begin{{abstract}}
{convert_inline(abstract)}
\end{{abstract}}

{body}

{{\scriptsize
\setlength{{\bibsep}}{{0pt plus 0.3ex}}
\bibliographystyle{{abbrvnat}}
\bibliography{{references}}
}}

\end{{document}}
"""


def write_readme() -> None:
    readme = """# C-D Observability Hierarchy arXiv source package

This directory is generated from `draft/main_observability_hierarchy.md`.

Build sequence on a TeX-enabled machine:

```bash
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

The local workspace also includes a portable Tectonic binary under
`tools/tectonic-0.16.9/`, and `scripts/audit_latex_preprint.py` uses it to
compile this package when system TeX tools are unavailable.

Before submission, the submitting author should inspect the generated arXiv
preview against the local PDF and confirm that author metadata, declarations,
figures, equations, and references render correctly.
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")


def write_manifest() -> None:
    manifest = """main.tex
references.bib
main.bbl
figures/interface_wall_filter.png
README.md
MANIFEST.txt
"""
    (OUT / "MANIFEST.txt").write_text(manifest, encoding="utf-8")


def main() -> None:
    metadata = load_submission_metadata()
    markdown = apply_submission_metadata(DRAFT.read_text(encoding="utf-8"), metadata)
    title, draft_date, abstract, body_lines = extract_front_matter(markdown)
    body = convert_body(body_lines)

    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    (OUT / "main.tex").write_text(
        latex_document(title, draft_date, abstract, body, metadata), encoding="utf-8"
    )
    shutil.copy2(USED_BIB, OUT / "references.bib")
    shutil.copy2(FIGURE_PNG, OUT / "figures" / "interface_wall_filter.png")
    write_readme()
    write_manifest()
    print(OUT)


if __name__ == "__main__":
    main()
