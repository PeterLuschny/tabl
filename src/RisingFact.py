from functools import cache
from _tabltypes import MakeTriangle

"""Rising factorial.

[0]  1;
[1]  1, 1;
[2]  1, 2,   6;
[3]  1, 3,  12,  60;
[4]  1, 4,  20, 120,  840;
[5]  1, 5,  30, 210, 1680, 15120;
[6]  1, 6,  42, 336, 3024, 30240, 332640;
[7]  1, 7,  56, 504, 5040, 55440, 665280, 8648640;
"""


@cache
def risingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = row[k] * (n + k)
    return row


@MakeTriangle(risingfactorial, "RisingFact", ["A124320"], False)
def RisingFactorial(n: int, k: int) -> int:
    return risingfactorial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(RisingFactorial)

''' OEIS

The traits of the RisingFact triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000407 | Std-RowLcm       | a(n) = (2*n+1)! / n!                                                           |
| 4   | A001761 | Std-DiagRow3     | a(n) = (2*n)!/(n+1)!                                                           |
| 5   | A001813 | Std-DiagRow1     | Quadruple factorial numbers: a(n) = (2n)!/n!                                   |
| 6   | A002378 | Std-DiagCol2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 7   | A005843 | Rev:Inv-DiagRow2 | The nonnegative even numbers: a(n) = 2n                                        |
| 8   | A006963 | Std-DiagRow2     | Number of planar embedded labeled trees with n nodes: (2*n-3)!/(n-1)! for n >= |
| 9   | A007531 | Std-DiagCol3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 10  | A028875 | Rev:Inv-PolyRow2 | a(n) = n^2 - 5                                                                 |
| 11  | A064352 | Std-CentralO     | a(n) = (3*n)!/(2*n)!                                                           |
| 12  | A117951 | Rev-PolyRow2     | a(n) = n^2 + 5                                                                 |
| 13  | A123680 | Std-RowSum       | a(n) = Sum_{k=0..n} C(n+k-1,k)*k!                                              |
| 14  | A124320 | Std-Triangle     | Triangle read by rows: T(n,k) = k!*binomial(n+k-1,k) (n >= 0, 0 <= k <= n), ri |
| 15  | A136392 | Std-PolyRow2     | a(n) = 6*n^2 - 10*n + 5                                                        |
| 16  | A139570 | Rev:Inv-DiagRow3 | a(n) = 2*n*(n+3)                                                               |
| 17  | A201279 | Alt-PolyRow2     | a(n) = 6n^2 + 10n + 5                                                          |
| 18  | A278069 | Std-InvBinConv   | a(n) = hypergeometric([n, -n], [], 1)                                          |
| 19  | A278070 | Std-BinConv      | a(n) = hypergeometric([n, -n], [], -1)                                         |
| 20  | A352601 | Std-CentralE     | a(n) = RisingFactorial(2*n, n) = A124320(2*n, n)                               |

* Statistic about RisingFact:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 20.
	all      A-numbers  : 66.
	missing  sequences  : 107.

[('missing', 107), ('A000027', 12), ('A000407', 9), ('A123680', 6), ('A000012', 4), ('A352601', 3), ('A278070', 3), ('A278069', 3), ('A124320', 3), ('A007531', 3), ('A006963', 3), ('A002378', 3), ('A001813', 3), ('A001761', 3), ('A064352', 2), ('A201279', 1), ('A139570', 1), ('A136392', 1), ('A117951', 1), ('A028875', 1), ('A005843', 1)]

A related webpage is: https://peterluschny.github.io/tabl/RisingFact.html .
2025/01/10

'''
