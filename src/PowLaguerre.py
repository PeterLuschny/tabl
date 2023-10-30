from functools import cache
from _tabltypes import MakeTriangle


"""Expansion of x^n in terms of Laguerre (unsigned).


[0] [   1]
[1] [   1,     1]
[2] [   2,     4,      2]
[3] [   6,    18,     18,      6]
[4] [  24,    96,    144,     96,     24]
[5] [ 120,   600,   1200,   1200,    600,    120]
[6] [ 720,  4320,  10800,  14400,  10800,   4320,   720]
[7] [5040, 35280, 105840, 176400, 176400, 105840, 35280, 5040]
"""


@cache
def powlaguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = powlaguerre(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@MakeTriangle(powlaguerre, "PowLaguerre", ["A196347", "A021012"], False)
def PowLaguerre(n: int, k: int) -> int:
    return powlaguerre(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(PowLaguerre)
