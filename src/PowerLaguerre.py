from functools import cache
from _tabltypes import set_attributes


"""Expansion of x^n in terms of Laguerre (unsigned), A196347, A021012.

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
def _powlag(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _powlag(n - 1) + [1] 
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(_powlag, "POWERSLAGUER", False)
def powlag(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _powlag(n).copy()
    return _powlag(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(powlag)
