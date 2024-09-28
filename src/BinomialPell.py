from functools import cache
from _tabltypes import MakeTriangle

"""Binomial Pell triangle


[0]   1
[1]   2     2
[2]   5     6    3
[3]  12    20    12     4
[4]  29    60    50    20     5
[5]  70   174   180   100    30     6
[6] 169   490   609   420   175    42   7
[7] 408  1352  1960  1624   840   280   56   8
[8] 985  3672  6084  5880  3654  1512  420  72  9
"""


@cache
def binomialpell(n: int) -> list[int]:

    if n == 0:
        return [1]
    if n == 1:
        return [2, 2]

    arow = binomialpell(n - 1)
    row = arow + [n + 1]
    for k in range(1, n):
        row[k] = (arow[k - 1] * (n + 1)) // k
    row[0] = 2 * arow[0] + binomialpell(n - 2)[0]

    return row


@MakeTriangle(binomialpell, "BinomialPell", ["A367211"], True)
def BinomialPell(n: int, k: int) -> int:
    return binomialpell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialPell)
