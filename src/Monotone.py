from functools import cache
from _tabltypes import MakeTriangle

"""Monotone words (binomial(-n, k)).

[0] [1]
[1] [1, 1]
[2] [1, 2,  3]
[3] [1, 3,  6,  10]
[4] [1, 4, 10,  20,  35]
[5] [1, 5, 15,  35,  70,  126]
[6] [1, 6, 21,  56, 126,  252,  462]
[7] [1, 7, 28,  84, 210,  462,  924, 1716]
[8] [1, 8, 36, 120, 330,  792, 1716, 3432,  6435]
[9] [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310]
"""


@cache
def monotone(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = (row[k] * (n + k)) // (k + 1)
    return row


@MakeTriangle(monotone, "Monotone", ["A059481", "A027555"], True)
def Monotone(n: int, k: int) -> int:
    return monotone(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Monotone)
