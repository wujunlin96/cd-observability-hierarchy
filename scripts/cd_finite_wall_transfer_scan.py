"""Finite-thickness C-D interface transfer-matrix scan.

The scan keeps the integrated wall coupling fixed:

    integral lambda(z) dz = 2 * alpha_int * omega * sqrt(C * D)

so the thin-wall limit approaches the delta-interface result with alpha_int.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import expm


@dataclass(frozen=True)
class ScatterResult:
    r_c: complex
    r_d: complex
    t_c: complex
    t_d: complex
    p_reflect_c: float
    p_reflect_d: float
    p_transmit_c: float
    p_transmit_d: float
    flux_sum: float


def system_matrix(omega: float, c_speed: float, d_speed: float, lam: float) -> np.ndarray:
    k_c = omega / c_speed
    k_d = omega / d_speed
    return np.array(
        [
            [0.0, 1.0, 0.0, 0.0],
            [-k_c**2, 0.0, lam / c_speed**2, 0.0],
            [0.0, 0.0, 0.0, 1.0],
            [lam / d_speed**2, 0.0, -k_d**2, 0.0],
        ],
        dtype=complex,
    )


def transfer_matrix(
    alpha_int: float,
    zeta: float,
    d_over_c: float,
    profile: str,
    n_steps: int = 800,
    cutoff: float = 8.0,
) -> np.ndarray:
    omega = 1.0
    c_speed = 1.0
    d_speed = d_over_c
    lambda_int = 2.0 * alpha_int * omega * np.sqrt(c_speed * d_speed)

    if zeta <= 0:
        raise ValueError("zeta must be positive")

    if profile == "square":
        length = zeta
        lam = lambda_int / length
        return expm(system_matrix(omega, c_speed, d_speed, lam) * length)

    if profile == "sech2":
        z_min = -cutoff * zeta
        z_max = cutoff * zeta
        dz = (z_max - z_min) / n_steps
        mat = np.eye(4, dtype=complex)
        for i in range(n_steps):
            z_mid = z_min + (i + 0.5) * dz
            sech = 1.0 / np.cosh(z_mid / zeta)
            lam = lambda_int * (sech**2) / (2.0 * zeta)
            mat = expm(system_matrix(omega, c_speed, d_speed, lam) * dz) @ mat
        return mat

    raise ValueError(f"unknown profile: {profile}")


def solve_scattering(
    alpha_int: float,
    zeta: float,
    d_over_c: float,
    profile: str,
    n_steps: int = 800,
) -> ScatterResult:
    omega = 1.0
    c_speed = 1.0
    d_speed = d_over_c
    k_c = omega / c_speed
    k_d = omega / d_speed
    mat = transfer_matrix(alpha_int, zeta, d_over_c, profile, n_steps=n_steps)

    def left_state(r_c: complex, r_d: complex) -> np.ndarray:
        return np.array(
            [
                1.0 + r_c,
                1j * k_c * (1.0 - r_c),
                r_d,
                -1j * k_d * r_d,
            ],
            dtype=complex,
        )

    def right_state(t_c: complex, t_d: complex) -> np.ndarray:
        return np.array(
            [
                t_c,
                1j * k_c * t_c,
                t_d,
                1j * k_d * t_d,
            ],
            dtype=complex,
        )

    # Unknown vector x = [r_C, r_D, t_C, t_D].
    base = mat @ left_state(0.0, 0.0) - right_state(0.0, 0.0)
    cols = []
    for basis in [
        (1.0, 0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0, 0.0),
        (0.0, 0.0, 1.0, 0.0),
        (0.0, 0.0, 0.0, 1.0),
    ]:
        r_c, r_d, t_c, t_d = basis
        cols.append(mat @ left_state(r_c, r_d) - right_state(t_c, t_d) - base)
    linear = np.column_stack(cols)
    x = np.linalg.solve(linear, -base)
    r_c, r_d, t_c, t_d = x

    p_reflect_c = abs(r_c) ** 2
    p_reflect_d = d_speed / c_speed * abs(r_d) ** 2
    p_transmit_c = abs(t_c) ** 2
    p_transmit_d = d_speed / c_speed * abs(t_d) ** 2
    flux_sum = p_reflect_c + p_reflect_d + p_transmit_c + p_transmit_d

    return ScatterResult(
        r_c=r_c,
        r_d=r_d,
        t_c=t_c,
        t_d=t_d,
        p_reflect_c=float(p_reflect_c),
        p_reflect_d=float(p_reflect_d),
        p_transmit_c=float(p_transmit_c),
        p_transmit_d=float(p_transmit_d),
        flux_sum=float(flux_sum),
    )


def delta_forward_probability(alpha: float) -> float:
    return alpha**2 / (1.0 + alpha**2) ** 2


def sinc(x: float) -> float:
    if abs(x) < 1e-12:
        return 1.0
    return float(np.sin(x) / x)


def sech2_fourier_norm(q_lw: float) -> float:
    if abs(q_lw) < 1e-10:
        return 1.0
    return float(np.pi * q_lw / (2.0 * np.sinh(np.pi * q_lw / 2.0)))


def born_ratios(profile: str, zeta: float, d_over_c: float) -> tuple[float, float]:
    """Weak-coupling ratios to the delta forward probability.

    Forward conversion samples q_- = k_C - k_D. Backward conversion samples
    q_+ = k_C + k_D.  The ratio is |Fourier(lambda)(q)/lambda_int|^2.
    """
    q_minus_lw = zeta * (1.0 - 1.0 / d_over_c)
    q_plus_lw = zeta * (1.0 + 1.0 / d_over_c)

    if profile == "square":
        f_minus = sinc(q_minus_lw / 2.0)
        f_plus = sinc(q_plus_lw / 2.0)
    elif profile == "sech2":
        f_minus = sech2_fourier_norm(q_minus_lw)
        f_plus = sech2_fourier_norm(q_plus_lw)
    else:
        raise ValueError(f"unknown profile: {profile}")

    return f_minus**2, f_plus**2


def main() -> None:
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    rows = []
    d_over_c_values = [1.0, np.sqrt(1.0 + 1e-3), 1.2, 2.0]

    for profile in ["square", "sech2"]:
        for d_over_c in d_over_c_values:
            for alpha_int in [1e-2, 0.1, 1.0]:
                for zeta in [1e-3, 1e-2, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]:
                    n_steps = 1200 if profile == "sech2" and zeta >= 10 else 600
                    result = solve_scattering(
                        alpha_int=alpha_int,
                        zeta=zeta,
                        d_over_c=d_over_c,
                        profile=profile,
                        n_steps=n_steps,
                    )
                    delta_p = delta_forward_probability(alpha_int)
                    born_forward, born_backward = born_ratios(profile, zeta, d_over_c)
                    rows.append(
                        {
                            "profile": profile,
                            "D_over_C": f"{d_over_c:.9e}",
                            "alpha_integrated": f"{alpha_int:.9e}",
                            "zeta_omega_Lw_over_C": f"{zeta:.9e}",
                            "P_C_reflect": f"{result.p_reflect_c:.9e}",
                            "P_D_reflect_left": f"{result.p_reflect_d:.9e}",
                            "P_C_transmit": f"{result.p_transmit_c:.9e}",
                            "P_D_transmit_forward": f"{result.p_transmit_d:.9e}",
                            "P_D_total": f"{result.p_reflect_d + result.p_transmit_d:.9e}",
                            "two_wall_forward_echo": f"{result.p_transmit_d**2:.9e}",
                            "delta_wall_forward_P": f"{delta_p:.9e}",
                            "forward_over_delta": f"{result.p_transmit_d / delta_p if delta_p else np.nan:.9e}",
                            "born_forward_over_delta": f"{born_forward:.9e}",
                            "born_backward_over_delta": f"{born_backward:.9e}",
                            "flux_sum": f"{result.flux_sum:.9e}",
                            "flux_error": f"{abs(result.flux_sum - 1.0):.9e}",
                        }
                    )

    path = out_dir / "cd_finite_wall_transfer_scan.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(path)


if __name__ == "__main__":
    main()
