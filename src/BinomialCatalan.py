from functools import cache
from _tabltypes import set_attributes

"""
T(n,k) = T(n,k) = binomial(n, k) * Catalan(n - k).
       = CatalanNumber[k] Pochhammer[-n, k] / k!

| 0 | [1] 
| 1 | [1, 1] 
| 2 | [1, 2,  2] 
| 3 | [1, 3,  6,   5] 
| 4 | [1, 4, 12,  20,  14] 
| 5 | [1, 5, 20,  50,  70,  42] 
| 6 | [1, 6, 30, 100, 210, 252, 132] 
| 7 | [1, 7, 42, 175, 490, 882, 924, 429]
"""


@cache
def binomialcatalan(n: int) -> list[int]:

    if n == 0: return [1]

    a = binomialcatalan(n - 1) + [0]
    row = [0] * (n + 1)
    row[0] = 1
    row[1] = n
    for k in range(2, n + 1):
        row[k] = (a[k] * (n + k + 1) + a[k - 1] * (4 * k - 2)) // (n + 1)

    return row


@set_attributes(
    binomialcatalan, 
    "BinomialCatalan", 
    ['A124644', 'A098474'], 
    True)
def BinomialCatalan(n: int, k: int) -> int: 
    return binomialcatalan(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialCatalan)
