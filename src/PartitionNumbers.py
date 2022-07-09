from functools import cache
from itertools import accumulate
from tabltypes import TablGenerator, tgen

"""The partition numbers (Euler's table) A008284, A026820, A000041.

[0] 1
[1] 0, 1
[2] 0, 1, 1
[3] 0, 1, 1, 1
[4] 0, 1, 2, 1, 1
[5] 0, 1, 2, 2, 1, 1
[6] 0, 1, 3, 3, 2, 1, 1
[7] 0, 1, 3, 4, 3, 2, 1, 1
[8] 0, 1, 4, 5, 5, 3, 2, 1, 1
[9] 0, 1, 4, 7, 6, 5, 3, 2, 1, 1

[0] 1
[1] 0, 1
[2] 0, 1, 2
[3] 0, 1, 2,  3
[4] 0, 1, 3,  4,  5
[5] 0, 1, 3,  5,  6,  7
[6] 0, 1, 4,  7,  9, 10, 11
[7] 0, 1, 4,  8, 11, 13, 14, 15
[8] 0, 1, 5, 10, 15, 18, 20, 21, 22
[9] 0, 1, 5, 12, 18, 23, 26, 28, 29, 30
"""


@cache
def _p(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0

    return _p(n - 1, k - 1) + _p(n - k, k)


@cache
def _partnum_exact(n: int) -> list[int]:
    return [_p(n, k) for k in range(n + 1)]


@cache
def _partnum_atmost(n: int) -> list[int]:
    return list(accumulate(_partnum_exact(n)))


partnum_exact: tgen = TablGenerator(_partnum_exact, "Partition numbers (exact)", "PARTEX")

partnum_atmost: tgen = TablGenerator(_partnum_atmost, "Partition numbers (at most)", "PARMOS")


####################################################################

if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(partnum_exact)
    TablTest(partnum_atmost)
