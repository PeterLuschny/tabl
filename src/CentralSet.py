from functools import cache
from _tabltypes import MakeTriangle

"""Central set factorial numbers.

[0] [1]
[1] [0, 1]
[2] [0, 1,    1]
[3] [0, 1,    5,      1]
[4] [0, 1,   21,     14,      1]
[5] [0, 1,   85,    147,     30,     1]
[6] [0, 1,  341,   1408,    627,    55,    1]
[7] [0, 1, 1365,  13013,  11440,  2002,   91,   1]
[8] [0, 1, 5461, 118482, 196053, 61490, 5278, 140,  1]
"""


@cache
def centralset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = centralset(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@MakeTriangle(centralset, "CentralSet", ["A269945", "A008957", "A036969"], True)
def CentralSet(n: int, k: int) -> int:
    return centralset(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CentralSet)
