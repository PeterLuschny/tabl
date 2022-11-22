from functools import cache
from tabltypes import tabl, tstruct

"""Laguerre polynomials n! * L(n, x) (unsigned coefficients), unsigned A021009.

[0]      1
[1]      1,       1
[2]      2,       4,       1
[3]      6,      18,       9,       1
[4]     24,      96,      72,      16,       1
[5]    120,     600,     600,     200,      25,      1
[6]    720,    4320,    5400,    2400,     450,     36,     1
[7]   5040,   35280,   52920,   29400,    7350,    882,    49,    1
[8]  40320,  322560,  564480,  376320,  117600,  18816,  1568,   64,  1
"""


@cache
def _laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [0] + _laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@tstruct(_laguerre, "LAGUERREPOLY")
def laguerre(size: int) -> tabl: 
    return [_laguerre(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(laguerre)
