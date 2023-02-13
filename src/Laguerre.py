from functools import cache
from _tabltypes import set_attributes


"""Laguerre polynomials n! * L(n, x) (unsigned coefficients).

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
def laguerre(n: int) -> list[int]:

    if n == 0: return [1]

    row: list[int] = [0] + laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@set_attributes(
    laguerre, 
    "Laguerre", 
    ['A021009', 'A021010', 'A144084'], 
    True)
def Laguerre(n: int, k: int) -> int:
    return laguerre(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Laguerre)
