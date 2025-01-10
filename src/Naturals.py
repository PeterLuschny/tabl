from functools import cache
from tabl import MakeTriangle, PrintProfile

"""
This is a demo of the most primitive use of the 'tabl' module.

The function 'natural' computes the n-th row of a regular integer
triangle. It has to be defined for n >= 0.
"""


@cache
def naturals(n: int) -> list[int]:
    R = range((n * (n + 1)) // 2, ((n + 1) * (n + 2)) // 2)
    return [i + 1 for i in R]


@MakeTriangle(naturals, "Naturals", ['A000027', 'A001477'], True)
def Naturals(n: int, k: int) -> int:
    return naturals(n)[k]


if __name__ == "__main__":
    PrintProfile(Naturals)

''' OEIS

The traits of the Naturals triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-Triangle     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000096 | Std-DiagRow1     | a(n) = n*(n+3)/2                                                               |
| 4   | A000124 | Std-ColLeft      | Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 + 1; or, max |
| 5   | A000217 | Std-RowMax       | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000982 | Std-ColMiddle    | a(n) = ceiling(n^2/2)                                                          |
| 7   | A001105 | Std-CentralO     | a(n) = 2*n^2                                                                   |
| 8   | A001844 | Std-CentralE     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 9   | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 10  | A006003 | Std-RowSum       | a(n) = n*(n^2 + 1)/2                                                           |
| 11  | A016777 | Alt-PolyRow1     | a(n) = 3*n + 1                                                                 |
| 12  | A016789 | Std-PolyRow1     | a(n) = 3*n + 2                                                                 |
| 13  | A019590 | Std-InvBinConv   | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 14  | A034856 | Std-DiagRow2     | a(n) = binomial(n+1, 2) + n - 1 = n*(n+3)/2 - 1                                |
| 15  | A038722 | Std-Rev          | Take the sequence of natural numbers (A000027) and reverse successive subseque |
| 16  | A055998 | Std-DiagRow3     | a(n) = n*(n+5)/2                                                               |
| 17  | A056536 | Std-AntiDiag     | Mapping from half-antidiagonal reading of the triangle (as used in A028297) to |
| 18  | A058331 | Rev-CentralO     | a(n) = 2*n^2 + 1                                                               |
| 19  | A061431 | Std-RowLcm       | a(n) = LCM of the n consecutive numbers n(n-1)/2 + 1, ..., n(n+1)/2            |
| 20  | A079824 | Std-DiagSum      | Sum of numbers in n-th upward diagonal of triangle in A079823                  |
| 21  | A084850 | Std-BinConv      | 2^(n-1)*(n^2+2n+2)                                                             |
| 22  | A099392 | Rev-ColMiddle    | a(n) = floor((n^2 - 2*n + 3)/2)                                                |
| 23  | A131474 | Std-EvenSum      | a(n) = ceiling(n/2)*ceiling(n^2/2)                                             |
| 24  | A132117 | Std-AccRevSum    | Binomial transform of [1, 7, 17, 17, 6, 0, 0, 0, ...]                          |
| 25  | A145018 | Std-DiagCol3     | a(n) = (n^2 - n + 8)/2                                                         |
| 26  | A152457 | Std-TransNat0    | Partial sums of A027444                                                        |
| 27  | A152948 | Std-DiagCol1     | a(n) = (n^2 - 3*n + 6)/2                                                       |
| 28  | A152950 | Std-DiagCol2     | a(n) = 3 + n*(n-1)/2                                                           |
| 29  | A176060 | Rev-TransNat0    | a(n) = n*(n+1)*(3*n^2+5*n+4)/12                                                |

* Statistic about Naturals:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 29.
	all      A-numbers  : 70.
	missing  sequences  : 53.

[('missing', 53), ('A006003', 6), ('A000217', 6), ('A152950', 3), ('A152948', 3), ('A145018', 3), ('A132117', 3), ('A084850', 3), ('A061431', 3), ('A055998', 3), ('A038722', 3), ('A034856', 3), ('A001844', 3), ('A000124', 3), ('A000096', 3), ('A000012', 3), ('A131474', 2), ('A056536', 2), ('A001105', 2), ('A000982', 2), ('A000027', 2), ('A176060', 1), ('A152457', 1), ('A099392', 1), ('A079824', 1), ('A058331', 1), ('A019590', 1), ('A016789', 1), ('A016777', 1), ('A005408', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Naturals.html .
2025/01/10

'''
