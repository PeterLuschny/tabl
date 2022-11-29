from functools import cache
from tabltypes import set_name

"""Stirling set numbers of second order, A008299, A137375.


[0] 1;
[1] 0, 0;
[2] 0, 1,   0;
[3] 0, 1,   0,    0;
[4] 0, 1,   3,    0,    0;
[5] 0, 1,  10,    0,    0,  0;
[6] 0, 1,  25,   15,    0,  0,  0;
[7] 0, 1,  56,  105,    0,  0,  0,  0;
[8] 0, 1, 119,  490,  105,  0,  0,  0,  0;
[9] 0, 1, 246, 1918, 1260,  0,  0,  0,  0,  0;
"""


@cache
def _stirling_set2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov: list[int] = _stirling_set2(n - 2)
    row: list[int] = _stirling_set2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]
    return row


@set_name(_stirling_set2, "STIRLSETORD2")
def stirling_set2(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _stirling_set2(n).copy()
    return _stirling_set2(n)[k]


if __name__ == "__main__":
    from tabltest import TablTest
    
    TablTest(stirling_set2)
