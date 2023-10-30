from functools import cache
from _tabltypes import MakeTriangle

"""EulerianB triangle.


[0] [1]
[1] [1,    1]
[2] [1,    6,     1]
[3] [1,   23,    23,      1]
[4] [1,   76,   230,     76,      1]
[5] [1,  237,  1682,   1682,    237,     1]
[6] [1,  722, 10543,  23548,  10543,   722,    1]
[7] [1, 2179, 60657, 259723, 259723, 60657, 2179,  1]
"""


@cache
def eulerianb(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = eulerianb(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


@MakeTriangle(eulerianb, "EulerianB", ["A060187", "A138076"], True)
def EulerianB(n: int, k: int) -> int:
    return eulerianb(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerianB)
