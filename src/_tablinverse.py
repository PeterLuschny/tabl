
# import numpy as np

# def NumpyInvertTabl(L: list[list[int]]) -> list[list[int]]:
#     """ NOT YET TESTED! """
#     n = len(L)
#     inv = np.zeros((n, n))

#     for k in range(n):
#         if L[k][k] == 0:
#             return []  # Inverse does not exist

#         inv[k][k] = 1 / L[k][k]

#         for j in range(k + 1, n):
#             inv[k][j] = -np.dot(inv[k][:k], L[k][:k+1:-1]) / L[k][k]

#     return inv.tolist()

from typing import Any

# #@


def InvertTabl(L: list[list[int]]) -> list[list[int]]:
    """
    Calculates the inverse of a lower triangular matrix.

    Args:
        L (list[list[int]]): The lower triangular matrix.

    Returns:
        list[list[int]]: The integer inverse of the lower triangular matrix if it exists.
        []: If the inverse does not exist.

    """
    n = len(L)
    inv = [[0 for _ in range(n)] for _ in range(n)]  # Identity matrix
    for i in range(n):
        inv[i][i] = 1
    for k in range(n):
        for j in range(n):
            for i in range(k):
                inv[k][j] -= inv[i][j] * L[k][i]
            a = inv[k][j]
            b = L[k][k]
            if b == 0:
                # print("Warning: Inverse does not exist!")
                # raise ValueError("Inverse does not exist!")
                return []
            a, r = divmod(a, b)  # make sure that a is integer
            if r != 0:
                # print("Warning: Integer terms do not exist!")
                # raise ValueError("Integer terms do not exist!")
                return []
    return [row[0:n + 1] for n, row in enumerate(inv)]


def InvertTriangle(r: Any, dim: int) -> list[list[int]]:
    M = [[r(n)[k] if k <= n else 0 for k in range(dim)] for n in range(dim)]
    return InvertTabl(M)


if __name__ == "__main__":

    def test() -> None:
        m = [[1, 0, 0], [1, 2, 0], [1, 2, 3]]
        v = InvertTabl(m)
        print(v)

        m = [[1, 0, 0], [1, 2, 0], [1, 2, 0]]
        v = InvertTabl(m)
        print(v)

        m = [
            [1,      0,      0,     0,    0,   0,  0, 0],
            [0,      1,      0,     0,    0,   0,  0, 0],
            [0,      2,      1,     0,    0,   0,  0, 0],
            [0,      9,      6,     1,    0,   0,  0, 0],
            [0,     64,     48,    12,    1,   0,  0, 0],
            [0,    625,    500,   150,   20,   1,  0, 0],
            [0,   7776,   6480,  2160,  360,  30,  1, 0],
            [0, 117649, 100842, 36015, 6860, 735, 42, 1],
        ]
        v = InvertTabl(m)
        print(v)

    from Abel import Abel
    from Bell import Bell
    from StirlingSet import StirlingSet

    dim = 8
    print(InvertTabl(Abel.tab(dim)))
    print(InvertTriangle(Abel.gen, dim))

    print(InvertTabl(StirlingSet.tab(dim)))
    print(InvertTriangle(StirlingSet.gen, dim))

    print(InvertTabl(Bell.tab(dim)))
    print(InvertTriangle(Bell.gen, dim))
