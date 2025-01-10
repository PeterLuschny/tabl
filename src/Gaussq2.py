from functools import cache
from _tabltypes import MakeTriangle

"""Gaussian coefficient for q = 2.

[0]  1;
[1]  1,   1;
[2]  1,   3,    1;
[3]  1,   7,    7,     1;
[4]  1,  15,   35,    15,     1;
[5]  1,  31,  155,   155,    31,    1;
[6]  1,  63,  651,  1395,   651,   63,   1;
[7]  1, 127, 2667, 11811, 11811, 2667, 127, 1;
"""


@cache
def gaussq2(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = gaussq2(n - 1)
    pow = [1] + gaussq2(n - 1)
    p = 2
    for k in range(1, n):
        pow[k] = row[k - 1] + p * row[k]
        p *= 2
    return pow


@MakeTriangle(gaussq2, "Gaussq2", ["A022166"], True)
def Gaussq2(n: int, k: int) -> int:
    return gaussq2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Gaussq2, 8, True)

''' OEIS

The traits of the Gaussq2 triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-RowSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000225 | Std-DiagRow1     | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 5   | A002378 | Inv-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 6   | A005329 | Inv-AccSum       | a(n) = Product_{i=1..n} (2^i - 1). Also called 2-factorial numbers             |
| 7   | A006095 | Std-DiagRow2     | Gaussian binomial coefficient [n,2] for q=2                                    |
| 8   | A006096 | Std-DiagRow3     | Gaussian binomial coefficient [ n,3 ] for q=2                                  |
| 9   | A006098 | Std-CentralE     | Gaussian binomial coefficient [ 2n,n ] for q=2                                 |
| 10  | A006099 | Std-RowMax       | Gaussian binomial coefficient [ n, n/2 ] for q=2                               |
| 11  | A006116 | Std-RowSum       | Sum of Gaussian binomial coefficients [n,k] for q=2 and k=0..n                 |
| 12  | A006125 | Inv-ColLeft      | a(n) = 2^(n*(n-1)/2)                                                           |
| 13  | A014105 | Inv:Rev-PolyRow2 | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 14  | A019320 | Std-RowGcd       | Cyclotomic polynomials at x=2                                                  |
| 15  | A019590 | Inv-PolyCol2     | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 16  | A022166 | Std-Triangle     | Triangle of Gaussian binomial coefficients (or q-binomial coefficients) [n,k]  |
| 17  | A028361 | Inv-AltSum       | Number of totally isotropic spaces of index n in orthogonal geometry of dimens |
| 18  | A028362 | Inv-EvenSum      | Total number of self-dual binary codes of length 2n. Totally isotropic spaces  |
| 19  | A028387 | Std-PolyRow2     | a(n) = n + (n+1)^2                                                             |
| 20  | A127850 | Inv-RowMax       | a(n)=(2^n-1)*2^(n(n-1)/2)/(2^(n-1))                                            |
| 21  | A135950 | Std-Inv          | Matrix inverse of triangle A022166                                             |
| 22  | A135951 | Inv-CentralE     | Central terms of triangle A135950, the matrix inverse of triangle A022166      |
| 23  | A139486 | Inv:Rev-NegHalf  | a(n) = Product_{j=0..n-1} (2^j + 2)                                            |
| 24  | A158474 | Std-RevInv       | Triangle read by rows generated from (x-1)*(x-2)*(x-4)*..                      |
| 25  | A182176 | Std-PosHalf      | Number of affine subspaces of GF(2)^n                                          |
| 26  | A203241 | Inv-DiagRow2     | Second elementary symmetric function of the first n terms of (1,2,4,8,...)     |
| 27  | A218449 | Std-CentralO     | Gaussian binomial coefficient [2*n-1,n] for q=2, n>=0                          |
| 28  | A289541 | Std-EvenSum      | Number of subspaces of GF(2)^n with even dimension                             |
| 29  | A290974 | Std-AltSum       | Alternating sum of row 2n of A022166                                           |

* Statistic about Gaussq2:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 29.
	all      A-numbers  : 98.
	missing  sequences  : 77.

[('missing', 77), ('A005329', 10), ('A000012', 7), ('A022166', 6), ('A000225', 6), ('A135950', 5), ('A028362', 5), ('A127850', 4), ('A028361', 4), ('A006116', 4), ('A006099', 4), ('A006096', 4), ('A006095', 4), ('A000027', 4), ('A182176', 3), ('A158474', 3), ('A290974', 2), ('A289541', 2), ('A218449', 2), ('A203241', 2), ('A135951', 2), ('A028387', 2), ('A019590', 2), ('A019320', 2), ('A006125', 2), ('A006098', 2), ('A000007', 2), ('A139486', 1), ('A014105', 1), ('A002378', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Gaussq2.html .
2025/01/10

'''
