"""Landau-Zener-style phase-matching estimates for a resonant C-D wall."""

from __future__ import annotations

import csv
import math
from pathlib import Path


def lz_probability(mu: float, beta: float) -> float:
    """Adiabatic C-to-D conversion probability for a linear detuning crossing."""
    if beta <= 0:
        raise ValueError("beta must be positive")
    return 1.0 - math.exp(-2.0 * math.pi * mu * mu / beta)


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)
    rows = []
    for mu in [1e-4, 1e-3, 1e-2, 0.03, 0.1, 0.3, 1.0]:
        for beta in [1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1.0]:
            gamma = mu * mu / beta
            rows.append(
                {
                    "mu_coupling_per_length": f"{mu:.9e}",
                    "beta_detuning_slope": f"{beta:.9e}",
                    "adiabaticity_mu2_over_beta": f"{gamma:.9e}",
                    "P_LZ_conversion": f"{lz_probability(mu, beta):.9e}",
                }
            )

    path = out_dir / "cd_resonant_wall_lz_scan.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
