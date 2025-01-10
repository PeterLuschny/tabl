from functools import cache
from _tabltypes import MakeTriangle

"""Genocchi triangle.

[0] [     1]
[1] [     1,      1]
[2] [     2,      3,      3]
[3] [     8,     14,     17,     17]
[4] [    56,    104,    138,    155,    155]
[5] [   608,   1160,   1608,   1918,   2073,   2073]
[6] [  9440,  18272,  25944,  32008,  36154,  38227,  38227]
[7] [198272, 387104, 557664, 702280, 814888, 891342, 929569, 929569]
"""


@cache
def genocchi(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [0] + genocchi(n - 1) + [0]

    for k in range(n, 0, -1):
        row[k] += row[k + 1]

    for k in range(2, n + 2):
        row[k] += row[k - 1]

    return row[1:]


@MakeTriangle(genocchi, "Genocchi", ["A297703"], False)
def Genocchi(n: int, k: int) -> int:
    return genocchi(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Genocchi)

''' OEIS

The traits of the Genocchi triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A005439 | Std-RowSum       | Genocchi medians (or Genocchi numbers of second kind)                          |
| 4   | A033816 | Rev-PolyRow2     | a(n) = 2*n^2 + 3*n + 3                                                         |
| 5   | A036968 | Std-InvBinConv   | Genocchi numbers (of first kind): expansion of 2*x/(exp(x)+1)                  |
| 6   | A077588 | Std-PolyRow2     | Maximum number of regions into which the plane is divided by n triangles       |
| 7   | A110501 | Std-AccRevSum    | Unsigned Genocchi numbers (of first kind) of even index                        |
| 8   | A297703 | Std-Triangle     | The Genocchi triangle read by rows, T(n,k) for n>=0 and 0<=k<=n                |

* Statistic about Genocchi:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 8.
	all      A-numbers  : 35.
	missing  sequences  : 90.

[('missing', 90), ('A110501', 12), ('A005439', 9), ('A036968', 3), ('A000027', 3), ('A000012', 3), ('A297703', 2), ('A077588', 2), ('A033816', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Genocchi.html .
2025/01/10

'''
