from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Charlier polynomials.

[0] [1]
[1] [1, -1]
[2] [1, -3, 1]
[3] [1, -6, 8, -1]
[4] [1, -10, 29, -24, 1]
[5] [1, -15, 75, -145, 89, -1]
[6] [1, -21, 160, -545, 814, -415, 1]
[7] [1, -28, 301, -1575, 4179, -5243, 2372, -1]
[8] [1, -36, 518, -3836, 15659, -34860, 38618, -16072, 1]
"""


@cache
def charlier(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, -1]

    a = charlier(n - 1)
    b = [0] + charlier(n - 2)
    c = charlier(n - 1) + [(-1) ** n]

    for k in range(1, n):
        c[k] = a[k] - n * a[k - 1] - (n - 1) * b[k - 1]

    return c


@MakeTriangle(charlier, "Charlier", ["A046716", "A094816"], True)
def Charlier(n: int, k: int) -> int:
    return charlier(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Charlier)
