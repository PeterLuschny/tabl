from functools import cache
from _tabltypes import MakeTriangle
from Divisibility import divisibility

"""Moebius Matrix.

[0] 1
[1] 0,  1
[2] 0, -1,  1
[3] 0, -1,  0,  1
[4] 0,  0, -1,  0,  1
[5] 0, -1,  0,  0,  0, 1
[6] 0,  1, -1, -1,  0, 0, 1
[7] 0, -1,  0,  0,  0, 0, 0, 1
[8] 0,  0,  0,  0, -1, 0, 0, 0, 1
[9] 0,  0,  0, -1,  0, 0, 0, 0, 0, 1
"""


@cache
def _moebius(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return -1
    return -sum(_moebius(k) for k, i in enumerate(divisibility(n)[: n - 1]) if i != 0)


@cache
def moebius(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = [0 for _ in range(n + 1)]
    r[n] = 1
    for k in range(1, n):
        if n % k == 0:
            r[k] = _moebius(n // k)
    return r


@MakeTriangle(moebius, "Moebius", ["A363914", "A054525"], True)
def Moebius(n: int, k: int) -> int:
    return moebius(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Moebius)
