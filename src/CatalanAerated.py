from functools import cache
from tabltypes import tabl, tvals

"""The aerated Catalan triangle, A053121.

[0]   1,
[1]   0,   1,
[2]   1,   0,   1,
[3]   0,   2,   0,   1,
[4]   2,   0,   3,   0,   1,
[5]   0,   5,   0,   4,   0,   1,
[6]   5,   0,   9,   0,   5,   0,   1,
[7]   0,  14,   0,  14,   0,   6,   0,  1,
[8]  14,   0,  28,   0,  20,   0,   7,  0,  1,
[9]   0,  42,   0,  48,   0,  27,   0,  8,  0,  1.
"""


@cache
def _catalan_aerated(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return _catalan_aerated(n - 1)[k] if k >= 0 and k < n else 0

    row: list[int] = _catalan_aerated(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


@tvals(_catalan_aerated, "ABELPO")
def catalan_aerated(size: int) -> tabl: 
    return [_catalan_aerated(j) for j in range(size)]


if __name__ == "__main__":
    from tabltest import TablTest

    TablTest(catalan_aerated)
