from functools import cache
from _tabltypes import MakeTriangle

"""Rising factorial.

[0]  1;
[1]  1, 1;
[2]  1, 2,   6;
[3]  1, 3,  12,  60;
[4]  1, 4,  20, 120,  840;
[5]  1, 5,  30, 210, 1680, 15120;
[6]  1, 6,  42, 336, 3024, 30240, 332640;
[7]  1, 7,  56, 504, 5040, 55440, 665280, 8648640;
"""


@cache
def risingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = row[k] * (n + k)
    return row


@MakeTriangle(risingfactorial, "RisingFact", ["A124320"], False)
def RisingFactorial(n: int, k: int) -> int:
    return risingfactorial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(RisingFactorial)
