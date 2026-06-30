"""Structural checks for the generated LaTeX preprint package."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PKG = next(
    (
        path
        for path in [
            ROOT / "submission" / "arxiv_cd_observability",
            ROOT / "paper",
        ]
        if path.exists()
    ),
    ROOT / "submission" / "arxiv_cd_observability",
)
MAIN = PKG / "main.tex"
BIB = PKG / "references.bib"
PORTABLE_TECTONIC = ROOT / "tools" / "tectonic-0.16.9" / "tectonic.exe"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\{([^,]+),", text))


def cite_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\citep\{([^}]+)\}", text):
        keys.update(k.strip() for k in match.group(1).split(",") if k.strip())
    return keys


def begin_end_balance(text: str, env: str) -> tuple[int, int]:
    return len(re.findall(rf"\\begin\{{{re.escape(env)}\}}", text)), len(
        re.findall(rf"\\end\{{{re.escape(env)}\}}", text)
    )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        PKG / "main.tex",
        PKG / "references.bib",
        PKG / "figures" / "interface_wall_filter.png",
        PKG / "README.md",
        PKG / "MANIFEST.txt",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing package file: {path}")

    if MAIN.exists() and BIB.exists():
        tex = read(MAIN)
        bib = read(BIB)
        missing_cites = sorted(cite_keys(tex) - bib_keys(bib))
        if missing_cites:
            errors.append(f"missing bibliography keys: {missing_cites}")
        if (
            "[@" in tex
            or "**" in tex
            or re.search(r"^##\s", tex, re.M)
            or re.search(r"^\|[-:\s|]+\|?$", tex, re.M)
        ):
            errors.append("markdown residue found in LaTeX")
        for fig in re.findall(r"\\includegraphics(?:\[[^\]]+\])?\{([^}]+)\}", tex):
            fig_path = PKG / fig
            if not fig_path.exists():
                errors.append(f"missing included figure: {fig_path}")
        for env in ["abstract", "center", "tabularx", "enumerate", "figure", "verbatim"]:
            begins, ends = begin_end_balance(tex, env)
            if begins != ends:
                errors.append(f"environment balance mismatch for {env}: {begins} begin, {ends} end")
        if "Author information to be finalized" in tex:
            warnings.append("author placeholder remains")
        if "No external funding has been specified" in tex:
            warnings.append("funding placeholder remains")

    pdflatex = shutil.which("pdflatex")
    tectonic = str(PORTABLE_TECTONIC) if PORTABLE_TECTONIC.exists() else shutil.which("tectonic")
    compile_status = "SKIPPED_NO_TEX_ENGINE"
    if pdflatex and not errors:
        try:
            subprocess.run([pdflatex, "-interaction=nonstopmode", "main.tex"], cwd=PKG, check=True, timeout=120)
            compile_status = "PDFLATEX_PASS"
        except Exception as exc:
            errors.append(f"pdflatex failed: {exc}")
            compile_status = "PDFLATEX_FAIL"
    elif tectonic and not errors:
        try:
            subprocess.run(
                [tectonic, "main.tex", "--keep-logs", "--keep-intermediates"],
                cwd=PKG,
                check=True,
                timeout=180,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            compile_status = "TECTONIC_PASS"
        except subprocess.CalledProcessError as exc:
            errors.append(f"tectonic failed: {exc.stdout[-2000:] if exc.stdout else exc}")
            compile_status = "TECTONIC_FAIL"
        except Exception as exc:
            errors.append(f"tectonic failed: {exc}")
            compile_status = "TECTONIC_FAIL"

    if compile_status in {"PDFLATEX_PASS", "TECTONIC_PASS"}:
        pdf = PKG / "main.pdf"
        log = PKG / "main.log"
        if not pdf.exists() or pdf.stat().st_size == 0:
            errors.append("compiled PDF missing or empty")
        if log.exists():
            log_text = read(log)
            if "undefined citations" in log_text or re.search(r"Citation `[^']+' .* undefined", log_text):
                errors.append("compiled log contains unresolved citations")

    print(f"package={PKG}")
    print(f"tex_citations={len(cite_keys(read(MAIN))) if MAIN.exists() else 0}")
    print(f"bib_entries={len(bib_keys(read(BIB))) if BIB.exists() else 0}")
    print(f"compile_status={compile_status}")
    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("latex_preprint_audit_status=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
