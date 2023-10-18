from functools import cache
from _tabltypes import set_attributes

"""Coefficients of Chebyshev U(n, x) polynomials.


[0]  1;
[1]  0,  2;
[2] -1,  0,   4;
[3]  0, -4,   0,    8;
[4]  1,  0, -12,    0,  16;
[5]  0,  6,   0,  -32,   0,   32;
[6] -1,  0,  24,    0, -80,    0,   64;
[7]  0, -8,   0,   80,   0, -192,    0,   128;
[8]  1,  0, -40,    0, 240,    0, -448,     0, 256;
[9]  0, 10,   0, -160,   0,  672,    0, -1024,   0,  512;
"""


@cache
def chebyshevu(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]

    rov: list[int] = chebyshevu(n - 2)
    row: list[int] = [0] + chebyshevu(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@set_attributes(chebyshevu, "ChebyshevU", ["A053117", "A053118", "A115322"], True)
def ChebyshevU(n: int, k: int) -> int:
    return chebyshevu(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(ChebyshevU)
