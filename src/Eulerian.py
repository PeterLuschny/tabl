from functools import cache
from _tabltypes import MakeTriangle

"""Eulerian triangle.

[0]  1,
[1]  1,    0,
[2]  1,    1,     0,
[3]  1,    4,     1,      0,
[4]  1,   11,    11,      1,      0,
[5]  1,   26,    66,     26,      1,    0,
[6]  1,   57,   302,    302,     57,    1,   0,
[7]  1,  120,  1191,   2416,   1191,  120,   1,  0,
[8]  1,  247,  4293,  15619,  15619, 4293, 247,  1,  0
=======================================================
0:  1
1:  0 1
2:  0 1    1
3:  0 1    4     1
4:  0 1   11    11      1
5:  0 1   26    66     26       1
6:  0 1   57   302    302      57       1
7:  0 1  120  1191   2416    1191     120      1
8:  0 1  247  4293  15619   15619    4293    247     1
"""


@cache
def KnuthEulerian(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = KnuthEulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@cache
def eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = eulerian(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - k + 1) * row[k - 1] + k * row[k]
    return row


@MakeTriangle(eulerian, "Eulerian", ["A123125", "A173018", "A008292"], True)
def Eulerian(n: int, k: int) -> int:
    return eulerian(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Eulerian)
