from functools import cache
from _tabltypes import set_attributes

"""Eulerian triangle, 
['A008292 ', 'A123125 ', 'A173018 '].

[0]  1,
[1]  1,    0,
[2]  1,    1,     0,
[3]  1,    4,     1,      0,
[4]  1,   11,    11,      1,      0,
[5]  1,   26,    66,     26,      1,    0,
[6]  1,   57,   302,    302,     57,    1,   0,
[7]  1,  120,  1191,   2416,   1191,  120,   1,  0,
[8]  1,  247,  4293,  15619,  15619, 4293, 247,  1,  0
"""


@cache
def _eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = _eulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@set_attributes(_eulerian, "EULERIANTRIA", False)
def eulerian(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _eulerian(n).copy()
    return _eulerian(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(eulerian)
