"""Conservative scale forecasts for C-D interface and holonomy routes.

The output is not an exclusion curve. It lists morphology-scale relations that
must be specified before fitting any transient or clock-network data.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


C = 299_792_458.0


def cone_factor(xi: float) -> tuple[float, float]:
    """Return D/C and |1-C/D| for D/C=sqrt(1+xi)."""
    if xi <= -1.0:
        raise ValueError("xi must be greater than -1")
    d_over_c = math.sqrt(1.0 + xi)
    mismatch = abs(1.0 - 1.0 / d_over_c)
    return d_over_c, mismatch


def required_segment(delta_t_s: float, xi: float) -> float:
    _, mismatch = cone_factor(xi)
    return math.inf if mismatch == 0 else C * delta_t_s / mismatch


def coherence_frequency_hz(wall_thickness_m: float, xi: float) -> float:
    """Frequency where |k_C-k_D| L_w ~= 1."""
    _, mismatch = cone_factor(xi)
    return math.inf if mismatch == 0 else C / (2.0 * math.pi * wall_thickness_m * mismatch)


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    rows: list[dict[str, str]] = []

    for delta_label, delta_t_s in [
        ("1_ns", 1e-9),
        ("1_us", 1e-6),
        ("1_ms", 1e-3),
    ]:
        for xi in [1.0, 1e-3, 1e-6]:
            d_over_c, mismatch = cone_factor(xi)
            length_m = required_segment(delta_t_s, xi)
            rows.append(
                {
                    "forecast_type": "interface_delay",
                    "observable": delta_label,
                    "xi": f"{xi:.9e}",
                    "D_over_C": f"{d_over_c:.9e}",
                    "mismatch_abs_1_minus_C_over_D": f"{mismatch:.9e}",
                    "input_scale": f"{delta_t_s:.9e} s",
                    "derived_scale": f"{length_m:.9e} m",
                    "interpretation": "hidden segment length needed for a visible time offset",
                }
            )

    for thickness_label, wall_thickness_m in [
        ("1_m", 1.0),
        ("1_km", 1e3),
        ("1000_km", 1e6),
    ]:
        for xi in [1.0, 1e-3, 1e-6]:
            d_over_c, mismatch = cone_factor(xi)
            cutoff_hz = coherence_frequency_hz(wall_thickness_m, xi)
            rows.append(
                {
                    "forecast_type": "interface_coherence",
                    "observable": thickness_label,
                    "xi": f"{xi:.9e}",
                    "D_over_C": f"{d_over_c:.9e}",
                    "mismatch_abs_1_minus_C_over_D": f"{mismatch:.9e}",
                    "input_scale": f"{wall_thickness_m:.9e} m",
                    "derived_scale": f"{cutoff_hz:.9e} Hz",
                    "interpretation": "frequency above which finite-wall phase mismatch suppresses conversion",
                }
            )

    clocks = [
        ("microwave_clock_9GHz", 9.192631770e9),
        ("optical_clock_4e14Hz", 4.0e14),
        ("optical_clock_1e15Hz", 1.0e15),
    ]
    for clock_label, frequency_hz in clocks:
        for phase_label, phase_rad in [("0p01_rad", 0.01), ("1_rad", 1.0)]:
            delta_tau_s = phase_rad / (2.0 * math.pi * frequency_hz)
            for duration_label, duration_s in [("1_s_event", 1.0), ("1_hour_event", 3600.0)]:
                rows.append(
                    {
                        "forecast_type": "relative_holonomy_clock",
                        "observable": f"{clock_label}_{phase_label}_{duration_label}",
                        "xi": "",
                        "D_over_C": "",
                        "mismatch_abs_1_minus_C_over_D": "",
                        "input_scale": f"{frequency_hz:.9e} Hz; {duration_s:.9e} s",
                        "derived_scale": f"{delta_tau_s:.9e} s; y~{delta_tau_s/duration_s:.9e}",
                        "interpretation": "clock proper-time step and event-averaged fractional shift for target holonomy phase",
                    }
                )

    path = out_dir / "cd_interface_holonomy_forecast.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
