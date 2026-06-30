# C-D Observability Hierarchy

This repository contains the public research artifacts for the manuscript:

**A C-D Observability Hierarchy for Multi-Sector Speed Constants**

The project studies a two-sector thought experiment in which a hidden sector is assigned an internal speed scale `D` while the visible sector uses speed scale `C`. The central claim is intentionally modest: a hidden speed ratio `D/C` is not automatically a visible second light cone. Under exact common Lorentz equivariance, smooth local sector maps, and flat relative calibration, the ratio has no local invariant visible content. Observable C-D physics must enter through controlled failure modes such as preferred hidden fields, relative holonomy, interfaces/defects, or portal-projected effective coefficients.

This is not a claim of a detected second light speed.

## Repository Layout

```text
draft/
  main_observability_hierarchy.md      # Markdown manuscript source

config/
  submission_metadata.json             # Final author/declaration metadata used for build
  submission_metadata.template.json

paper/
  main.pdf                             # Current compiled PDF
  main.tex                             # Generated LaTeX source
  main.bbl                             # Bibliography generated for arXiv-style source
  references.bib                       # Bibliography used by main.tex
  README.md
  MANIFEST.txt
  arxiv_cd_observability_source.zip    # Clean arXiv-style source package
  figures/
    interface_wall_filter.png

scripts/
  cd_no_go_symbolic_checks.py
  cd_common_cone_symbolic_check.py
  cd_interface_delta_scattering.py
  cd_finite_wall_transfer_scan.py
  cd_interface_holonomy_forecast.py
  plot_interface_wall_filter.py
  plot_interface_wall_filter_png.py
  audit_*.py

results/
  cd_*                                # Generated reproducibility tables
  citation_*                          # Citation audit outputs

notes/
  current_research_decision_v109.md
  novelty_adversarial_audit_v122.md
  novelty_external_audit_v107.md
  paper_self_review_v108.md

figures/
  interface_wall_filter.png
  interface_wall_filter.svg

references/
  observability_used_references.bib
```

## Quick Checks

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the core symbolic checks:

```bash
python scripts/cd_no_go_symbolic_checks.py
python scripts/cd_common_cone_symbolic_check.py
```

Regenerate the interface and forecast tables:

```bash
python scripts/cd_interface_delta_scattering.py
python scripts/cd_finite_wall_transfer_scan.py
python scripts/cd_interface_frequency_scaling.py
python scripts/cd_interface_holonomy_forecast.py
```

Run manuscript/package audits:

```bash
python scripts/audit_observability_manuscript.py
python scripts/audit_latex_preprint.py
```

`audit_latex_preprint.py` compiles with a local TeX engine if available. The manuscript was locally compiled with Tectonic in the working environment used to prepare this release.

## Current Status

This is a pre-arXiv public artifact bundle. The manuscript now includes formal no-go propositions, an interface/relative-holonomy morphology vector, and conservative forecast-scale tables.

The technical package is ready for author-side arXiv preview. Remaining blockers are human checks: final reading of the PDF by the author, comparison with the arXiv-generated preview, and endorsement if arXiv requests it.

## Caution

The manuscript is a no-go/classification framework plus controlled toy calculations. It does not claim:

- evidence for a hidden D-sector spacetime;
- direct observation of a second light speed;
- novelty for Lorentz violation, varying-speed-of-light models, SME coefficients, disformal metrics, aether theories, hidden photons, sterile-neutrino altered dispersion, or multimetric gravity.

## License

For arXiv submission, the author selected the arXiv.org perpetual, non-exclusive license. No separate repository-wide software license has been added yet.
