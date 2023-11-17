from functools import cache
from _tabltypes import MakeTriangle

"""Fibonacci-Pascal triangle.

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,  1]
[3] [ 1,  2,  2,  1]
[4] [ 2,  3,  4,  3,  1]
[5] [ 3,  5,  7,  7,  4,  1]
[6] [ 5,  8, 12, 14, 11,  5,  1]
[7] [ 8, 13, 20, 26, 25, 16,  6,  1]
[8] [13, 21, 33, 46, 51, 41, 22,  7, 1]
[9] [21, 34, 54, 79, 97, 92, 63, 29, 8, 1]
"""


@cache
def fibonacci(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = fibonacci(n - 1) + [1]
    s = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row


@MakeTriangle(fibonacci, "Fibonacci", ["A354267", "A105809", "A228074"], False)
def Fibonacci(n: int, k: int) -> int:
    return fibonacci(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Fibonacci)
