"""Frequency-scaling families for C-D interface conversion.

The solved delta-wall model depends on alpha(lambda, omega).  This script
compares phenomenological scalings alpha = alpha_ref * (omega/omega_ref)^p.
"""

from __future__ import annotations

import csv
from pathlib import Path


def probabilities(alpha: float) -> tuple[float, float, float, float]:
    denom = (1.0 + alpha**2) ** 2
    p_refl = alpha**4 / denom
    p_c = 1.0 / denom
    p_d_total = 2.0 * alpha**2 / denom
    p_echo = (alpha**2 / denom) ** 2
    return p_refl, p_c, p_d_total, p_echo


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    # Frequency anchors in Hz; omega-ratios are identical to frequency ratios.
    bands = [
        ("radio_1GHz", 1e9),
        ("mm_100GHz", 1e11),
        ("infrared_30THz", 3e13),
        ("optical_500THz", 5e14),
        ("xray_1keV", 2.417989e17),
        ("gamma_1GeV", 2.417989e23),
    ]
    ref_hz = 1e9
    alpha_ref = 1e-2
    scalings = [
        ("constant_delta_lambda", -1.0),
        ("omega_delta_lambda", 0.0),
        ("time_derivative_delta", 1.0),
    ]

    rows = []
    for scaling_name, power in scalings:
        for band, freq_hz in bands:
            alpha = alpha_ref * (freq_hz / ref_hz) ** power
            p_refl, p_c, p_d_total, p_echo = probabilities(alpha)
            rows.append(
                {
                    "scaling": scaling_name,
                    "power_p": f"{power:.1f}",
                    "band": band,
                    "frequency_hz": f"{freq_hz:.9e}",
                    "alpha": f"{alpha:.9e}",
                    "P_convert_total_D": f"{p_d_total:.9e}",
                    "P_two_wall_forward_echo": f"{p_echo:.9e}",
                    "P_reflect_C": f"{p_refl:.9e}",
                    "P_transmit_C": f"{p_c:.9e}",
                }
            )

    path = out_dir / "cd_interface_frequency_scaling.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
