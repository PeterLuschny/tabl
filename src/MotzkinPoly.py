from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Motzkin polynomials.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   2
[5] 1, 0, 10, 0,  10, 0
[6] 1, 0, 15, 0,  30, 0,   5
[7] 1, 0, 21, 0,  70, 0,  35, 0
[8] 1, 0, 28, 0, 140, 0, 140, 0,  14
[9] 1, 0, 36, 0, 252, 0, 420, 0, 126, 0
"""


@cache
def motzkinpoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    h = 0 if n % 2 else (motzkinpoly(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkinpoly(n - 1) + [h]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@MakeTriangle(motzkinpoly, "MotzkinPoly", ["A359364"], False)
def MotzkinPoly(n: int, k: int) -> int:
    return motzkinpoly(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(MotzkinPoly)
