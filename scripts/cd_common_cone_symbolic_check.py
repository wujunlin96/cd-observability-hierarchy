"""Symbolic check for the common-cone Lorentz constraint.

The check asks which symmetric bilinear forms F are invariant under the
visible Lorentz algebra. With signature (-,+,+,+), the answer should be the
one-dimensional span of eta. Rotation invariance alone leaves two parameters,
diag(a,b,b,b); adding boosts forces a = -b.
"""

from __future__ import annotations

from sympy import Matrix, diag, linear_eq_to_matrix, linsolve, symbols


def symmetric_bilinear() -> tuple[Matrix, tuple]:
    names = []
    rows = []
    for i in range(4):
        row = []
        for j in range(4):
            if i <= j:
                name = f"f{i}{j}"
                names.append(name)
                row.append(symbols(name))
            else:
                row.append(rows[j][i])
        rows.append(row)
    variables = tuple(symbols(" ".join(names)))
    lookup = dict(zip(names, variables))
    matrix = Matrix([[lookup[str(entry)] if str(entry) in lookup else entry for entry in row] for row in rows])
    return matrix, variables


def generator(i: int, j: int, boost: bool) -> Matrix:
    g = Matrix.zeros(4, 4)
    if boost:
        g[0, i] = 1
        g[i, 0] = 1
    else:
        g[i, j] = 1
        g[j, i] = -1
    return g


def invariant_solution(generators: list[Matrix], variables: tuple) -> tuple[int, list[Matrix]]:
    f, _ = symmetric_bilinear()
    equations = []
    for gen in generators:
        condition = gen.T * f + f * gen
        equations.extend(condition)
    coeffs, rhs = linear_eq_to_matrix(equations, variables)
    solution = linsolve((coeffs, rhs), variables)
    basis = coeffs.nullspace()
    return len(basis), basis


def vector_to_matrix(vector: Matrix, variables: tuple) -> Matrix:
    f, _ = symmetric_bilinear()
    replacements = dict(zip(variables, list(vector)))
    return f.subs(replacements)


def main() -> None:
    _, variables = symmetric_bilinear()

    rotations = [
        generator(1, 2, boost=False),
        generator(1, 3, boost=False),
        generator(2, 3, boost=False),
    ]
    boosts = [
        generator(1, 0, boost=True),
        generator(2, 0, boost=True),
        generator(3, 0, boost=True),
    ]

    rotation_dim, rotation_basis = invariant_solution(rotations, variables)
    lorentz_dim, lorentz_basis = invariant_solution(rotations + boosts, variables)

    eta = diag(-1, 1, 1, 1)
    lorentz_matrix_basis = [vector_to_matrix(vec, variables) for vec in lorentz_basis]
    proportional_to_eta = (
        lorentz_dim == 1
        and lorentz_matrix_basis[0] == eta
    )

    print(f"rotation_invariant_symmetric_dim = {rotation_dim}")
    print("rotation_basis_matrices =")
    for item in rotation_basis:
        print(vector_to_matrix(item, variables))
    print(f"lorentz_invariant_symmetric_dim = {lorentz_dim}")
    print("lorentz_basis_matrices =")
    for item in lorentz_matrix_basis:
        print(item)
    print(f"lorentz_basis_proportional_to_eta = {proportional_to_eta}")


if __name__ == "__main__":
    main()
