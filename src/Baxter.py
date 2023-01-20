from functools import cache
from math import factorial
from _tabltypes import set_attributes


"""Baxter polynomials.

[0] 1
[1] 0, 1
[2] 0, 1,   1
[3] 0, 1,   4,    1
[4] 0, 1,  10,   10,     1
[5] 0, 1,  20,   50,    20,     1
[6] 0, 1,  35,  175,   175,    35,     1
[7] 0, 1,  56,  490,   980,   490,    56,    1
[8] 0, 1,  84, 1176,  4116,  4116,  1176,   84,   1
[9] 0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1
"""

@cache
def F(n: int) -> int:
    return factorial(n) ** 3 * ((n + 1) * (n + 1) * (n + 2))


@cache
def _baxter(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [0] + [(2 * F(n - 1)) // (F(k - 1) * F(n - k)) for k in range(1, n + 1)]
    return row


@set_attributes(
    _baxter, 
    "Baxter", 
    ['A359363', 'A056939'],
    False)
def baxter(n: int, k: int = -1) -> list[int] | int: 
    if k == -1: return _baxter(n).copy()
    return _baxter(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(baxter)
