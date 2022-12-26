from functools import cache
from _tabltypes import set_attributes

"""Stirling cycle B-type. 

[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     15,     23,      9,     1;
[4]    105,    176,     86,    16,     1;
[5]    945,   1689,    950,   230,    25,   1;
[6]  10395,  19524,  12139,  3480,   505,  36,  1;
[7] 135135, 264207, 177331, 57379, 10045, 973, 49, 1;
"""


@cache
def _stirling_cycleB(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _stirling_cycleB(n - 1) + [1]

    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m
    return row


@set_attributes(
    _stirling_cycleB, 
    "StirlingCycB", 
    ['A028338', 'A039757', 'A039758', 'A109692'], 
    True)
def stirling_cycleB(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _stirling_cycleB(n).copy()
    return _stirling_cycleB(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(stirling_cycleB)
