# C-D Observability Hierarchy arXiv source package

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

Before submission, replace the placeholder author block and finalize funding,
conflict-of-interest, contribution, and AI-assistance disclosures.
