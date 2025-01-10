from functools import cache
from itertools import accumulate
from _tabltypes import MakeTriangle

"""Ternary trees, Fuss-Catalan 2.


[0] [1]
[1] [0, 1]
[2] [0, 1,  3]
[3] [0, 1,  5, 12]
[4] [0, 1,  7, 25,  55]
[5] [0, 1,  9, 42, 130,  273]
[6] [0, 1, 11, 63, 245,  700, 1428]
[7] [0, 1, 13, 88, 408, 1428, 3876, 7752]
"""


@cache
def ternarytrees(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = ternarytrees(n - 1) + [ternarytrees(n - 1)[n - 1]]

    return list(accumulate(accumulate(row)))


@MakeTriangle(ternarytrees, "TernaryTrees", ["A355172"], False)
def TernaryTrees(n: int, k: int) -> int:
    return ternarytrees(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(TernaryTrees)


''' OEIS

The traits of the TernaryTrees triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A001764 | Std-RowMax       | a(n) = binomial(3*n,n)/(2*n+1) (enumerates ternary trees and also noncrossing  |
| 5   | A004319 | Rev-PolyCol3     | a(n) = binomial(3*n, n - 1)                                                    |
| 6   | A005408 | Std-DiagCol2     | The odd numbers: a(n) = 2*n + 1                                                |
| 7   | A006629 | Std-RowSum       | Self-convolution 4th power of A001764, which enumerates ternary trees          |
| 8   | A027691 | Rev-PolyRow3     | a(n) = n^2 + n + 6                                                             |
| 9   | A049450 | Alt-PolyRow2     | Pentagonal numbers multiplied by 2: a(n) = n*(3*n-1)                           |
| 10  | A049451 | Std-PolyRow2     | Twice second pentagonal numbers                                                |
| 11  | A071355 | Std-DiagCol3     | a(n) = 2*n^2 + 11*n + 12                                                       |
| 12  | A102594 | Std-DiagRow2     | Number of noncrossing trees with n edges in which no border edges emanate from |
| 13  | A102893 | Std-AccSum       | Number of noncrossing trees with n edges and having degree of the root at leas |
| 14  | A230547 | Std-DiagRow3     | a(n) = 3*binomial(3*n+9, n)/(n+3)                                              |
| 15  | A246434 | Std-InvBinConv   | Expansion of (3*x/2 - 1 - (7*x - 2)/(2*sqrt(1 - 4*x)))/x                       |
| 16  | A349509 | Std-RowGcd       | a(n) is the denominator of binomial(n^3 + 6*n^2 - 6*n + 2, n^3 - 1)/n^3        |
| 17  | A355172 | Std-Triangle     | The Fuss-Catalan triangle of order 2, read by rows. Related to ternary trees   |

* Statistic about TernaryTrees:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 17.
	all      A-numbers  : 53.
	missing  sequences  : 72.

[('missing', 72), ('A102893', 6), ('A006629', 6), ('A001764', 6), ('A102594', 4), ('A000012', 4), ('A349509', 3), ('A246434', 3), ('A230547', 3), ('A071355', 3), ('A005408', 3), ('A000027', 3), ('A000007', 3), ('A355172', 2), ('A049451', 1), ('A049450', 1), ('A027691', 1), ('A004319', 1)]

A related webpage is: https://peterluschny.github.io/tabl/TernaryTrees.html .
2025/01/10

'''
