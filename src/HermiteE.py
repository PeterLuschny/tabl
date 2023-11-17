from functools import cache
from _tabltypes import MakeTriangle

"""(Probabilist's) Hermite polynomials He, unsigned coefficients. 

[0] [ 1]
[1] [ 0,   1]
[2] [ 1,   0,  1]
[3] [ 0,   3,  0,   1]
[4] [ 3,   0,  6,   0,  1]
[5] [ 0,  15,  0,  10,  0,  1]
[6] [15,   0, 45,   0, 15,  0, 1]
[7] [ 0, 105,  0, 105,  0, 21, 0, 1]
"""


@cache
def hermitee(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


@MakeTriangle(hermitee, "HermiteE", ["A099174", "A066325", "A073278"], True)
def HermiteE(n: int, k: int) -> int:
    return hermitee(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HermiteE)
