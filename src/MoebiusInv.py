from functools import cache
from _tabltypes import set_attributes
from NumMoebius import moebius


'''Inverse Moebius matrix.

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
'''


@cache
def moebiusinv(n: int) -> list[int]:
    if n == 0: return [1]
    r = [0 for _ in range(n + 1)]
    r[n] = 1
    for k in range(1, n):
        if n % k == 0: 
            r[k] = moebius(n // k)
    return r


@set_attributes(
    moebiusinv,
    "MoebiusInv",
    ['A363914'],
    True)
def MoebiusInv(n: int, k: int) -> int:
    return moebiusinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(MoebiusInv)
