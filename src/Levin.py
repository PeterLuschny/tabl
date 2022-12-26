from functools import cache
from _tabltypes import set_attributes


"""Levin's Triangle, RisingFactorial(n + 1, n) / (k! * (n - k)!).


[0]     1;
[1]     2,      2;
[2]     6,     12,      6;
[3]    20,     60,     60,     20;
[4]    70,    280,    420,    280,     70;
[5]   252,   1260,   2520,   2520,   1260,    252;
[6]   924,   5544,  13860,  18480,  13860,   5544,    924;
[7]  3432,  24024,  72072, 120120, 120120,  72072,  24024,   3432;
[8] 12870, 102960, 360360, 720720, 900900, 720720, 360360, 102960, 12870;
"""


@cache
def _levin(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _levin(n - 1) + [1] 
    row[0] = row[n] = (row[n - 1] * (4 * n - 2)) // n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@set_attributes(
    _levin, 
    "Levin", 
    ['A356546'], 
    False)
def levin(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _levin(n).copy()
    return _levin(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(levin)
