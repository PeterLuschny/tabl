from functools import cache
from _tabltypes import MakeTriangle

"""
T(n, k) = if k == 0 then 0^n else binomial(n-1, k-1) * Bell(n - k)

[0]     1
[1]     1,    1
[2]     2,    2,    1
[3]     5,    6,    3,    1
[4]    15,   20,   12,    4,    1
[5]    52,   75,   50,   20,    5,   1
[6]   203,  312,  225,  100,   30,   6,  1
[7]   877, 1421, 1092,  525,  175,  42,  7, 1
[8]  4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1
"""


@cache
def binomialbell(n: int) -> list[int]:

    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    a = binomialbell(n - 1) + [1]
    s = sum(a) - 1

    for j in range(n - 1, 0, -1):
        a[j] = (a[j - 1] * n) // j
    a[0] = s

    return a


@MakeTriangle(binomialbell, "BinomialBell", ["A056857", "A056860"], True)
def BinomialBell(n: int, k: int) -> int:
    return binomialbell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialBell)
