from functools import cache
from tabltypes import tabl, tvals

"""The EulerianB triangle, A060187.

[0] [1]
[1] [0, 1]
[2] [0, 1,    1]
[3] [0, 1,    6,     1]
[4] [0, 1,   23,    23,      1]
[5] [0, 1,   76,   230,     76,      1]
[6] [0, 1,  237,  1682,   1682,    237,     1]
[7] [0, 1,  722, 10543,  23548,  10543,   722,    1]
[8] [0, 1, 2179, 60657, 259723, 259723, 60657, 2179,  1]
"""


@cache
def _eulerianB(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row: list[int] = _eulerianB(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k - 1) * row[k]
    return row


@tvals(_eulerianB, "EULIRB")
def eulerianB(size: int) -> tabl: 
    return [_eulerianB(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(eulerianB)
