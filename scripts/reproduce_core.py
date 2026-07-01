"""Run the core reproducibility pipeline for the C-D observability paper.

The default pipeline avoids network-dependent checks. Use --with-network to
also verify citation sentences and arXiv identifiers.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CORE_SCRIPTS = [
    "cd_no_go_symbolic_checks.py",
    "cd_common_cone_symbolic_check.py",
    "cd_interface_delta_scattering.py",
    "cd_finite_wall_transfer_scan.py",
    "plot_interface_wall_filter.py",
    "plot_interface_wall_filter_png.py",
    "cd_macro_scale_estimates.py",
    "cd_interface_frequency_scaling.py",
    "cd_interface_holonomy_forecast.py",
    "build_used_references.py",
    "build_latex_preprint.py",
    "audit_observability_manuscript.py",
    "audit_latex_preprint.py",
]

NETWORK_SCRIPTS = [
    "audit_citation_sentences.py",
    "verify_used_arxiv_refs.py",
]


def run_script(script_name: str) -> None:
    script = ROOT / "scripts" / script_name
    print(f"==> {script_name}", flush=True)
    subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--with-network",
        action="store_true",
        help="also run checks that may need internet access or live arXiv metadata",
    )
    args = parser.parse_args()

    for script_name in CORE_SCRIPTS:
        run_script(script_name)
    if args.with_network:
        for script_name in NETWORK_SCRIPTS:
            run_script(script_name)

    print("reproduce_core_status=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
