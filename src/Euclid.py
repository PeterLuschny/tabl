from functools import cache
from _tabltypes import set_attributes

"""Euclid's triangle.

[ 0] [0]
[ 1] [1, 1]
[ 2] [0, 1, 0]
[ 3] [0, 1, 1, 0]
[ 4] [0, 1, 0, 1, 0]
[ 5] [0, 1, 1, 1, 1, 0]
[ 6] [0, 1, 0, 0, 0, 1, 0]
[ 7] [0, 1, 1, 1, 1, 1, 1, 0]
[ 8] [0, 1, 0, 1, 0, 1, 0, 1, 0]
[ 9] [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
[10] [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
[11] [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
"""

# We give two imlementations. This is the first one:

@cache
def _euclidX(n: int, k: int) -> int:
    while k != 0:
        t = k
        k = n % k
        n = t
    return 1 if n == 1 else 0

@cache
def euclidX(n: int) -> list[int]:
    return [_euclidX(i, n) for i in range(n + 1)]

# This is the second (faster) one:

@cache
def euclid(n: int) -> list[int]:
    if n == 0: return [0]
    if n == 1: return [1, 1]

    row = [0 for _ in range(n + 1)]
    row[1] = row[n - 1] = 1

    for k in range(2, n // 2 + 2):
        j = n % k
        if j > 0:
            row[k] = row[n - k] = euclid(n - j)[j] 

    return row


@set_attributes(
    euclid,
    "Euclid",
    ['A217831'],
    False)
def Euclid(n: int, k: int) -> int:
    return euclid(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Euclid, 12)
    #for n in range(12): print([n], euclid(n))
    #for n in range(12): print([n], euclidX(n))
