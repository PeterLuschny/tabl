from functools import cache
from Binomial import binomial
from DistLattices import dist_latt
from _tabltypes import MakeTriangle

"""EulerianZigZag triangle.

[0] [1]
[1] [1,  0]
[2] [1,  0,   0]
[3] [1,  1,   0,   0]
[4] [1,  3,   1,   0,   0]
[5] [1,  7,   7,   1,   0,  0]
[6] [1, 14,  31,  14,   1,  0, 0]
[7] [1, 26, 109, 109,  26,  1, 0, 0]
[8] [1, 46, 334, 623, 334, 46, 1, 0, 0]
"""

@cache
def eulerianzigzag(n: int) -> list[int]:

    b = binomial(n + 1)
    return [sum((-1)**j * b[j] * dist_latt(n, k - j) for j in range(k + 1))
            for k in range(n + 1)]


@cache
def ezz(n: int) -> list[int]:
    n += 2
    b = binomial(n + 1)
    return [sum((-1)**j * b[j] * dist_latt(n, k - j) for j in range(k + 1))
            for k in range(n - 1)]


@MakeTriangle(eulerianzigzag, "EulerianZigZag", ["A205497"], False)
def EulerianZigZag(n: int, k: int) -> int:
    return eulerianzigzag(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerianZigZag)
