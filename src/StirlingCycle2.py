from functools import cache
from _tabltypes import set_attributes

"""Stirling cycle numbers of second order, A008306, A106828.


[0]  1
[1]  0,     0
[2]  0,     1,     0
[3]  0,     2,     0,     0
[4]  0,     6,     3,     0,    0
[5]  0,    24,    20,     0,    0, 0
[6]  0,   120,   130,    15,    0, 0, 0
[7]  0,   720,   924,   210,    0, 0, 0, 0
[8]  0,  5040,  7308,  2380,  105, 0, 0, 0, 0
[9]  0, 40320, 64224, 26432, 2520, 0, 0, 0, 0, 0
"""


@cache
def _stirling_cycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov: list[int] = _stirling_cycle2(n - 2)
    row: list[int] = _stirling_cycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


@set_attributes(_stirling_cycle2, "STIRLCYCORD2", False)
def stirling_cycle2(n: int, k: int = -1) -> list[int] | int:
    if k == -1: return _stirling_cycle2(n).copy()
    return _stirling_cycle2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    
    TablTest(stirling_cycle2)
