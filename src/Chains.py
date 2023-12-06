from functools import cache
from _tabltypes import MakeTriangle

"""Chains of length k in partially ordered set formed from subsets of n-set by inclusion.

0  [  1]
1  [  2,    1]
2  [  4,    5,     2]
3  [  8,   19,    18,     6]
4  [ 16,   65,   110,    84,    24]
5  [ 32,  211,   570,   750,   480,   120]
6  [ 64,  665,  2702,  5460,  5880,  3240,   720]
7  [128, 2059, 12138, 35406, 57120, 52080, 25200, 5040]
"""


@cache
def chains(n: int) -> list[int]:
    if n == 0:
        return [1]

    ch = chains(n - 1) + [0]
    row = ch.copy()
    row[0] = 2 * ch[0]
    row[n] = n * ch[n - 1]

    for k in range(n - 1, 0, -1):
        row[k] = k * ch[k - 1] + (k + 2) * ch[k]

    return row


@MakeTriangle(chains, "Chains", ["A038719"], False)
def Chains(n: int, k: int) -> int:
    return chains(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Chains)
