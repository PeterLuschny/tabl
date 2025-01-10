from functools import cache
from DistLattices import dist_latt
from _tabltypes import MakeTriangle

"""Kekule triangle.

  [0] 1;
  [1] 1,  1;
  [2] 1,  2,  1;
  [3] 1,  3,  3,  1;
  [4] 1,  5,  6,  4,  1;
  [5] 1,  8, 14, 10,  5,  1;
  [6] 1, 13, 31, 30, 15,  6, 1;
  [7] 1, 21, 70, 85, 55, 21, 7, 1;
"""

@cache
def kekule(n: int) -> list[int]:
    return [dist_latt(n - k, k) for k in range(n + 1)]


@MakeTriangle(kekule, "Kekule", ["A050446", "A050447"], False)
def Kekule(n: int, k: int) -> int:
    return kekule(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Kekule)
    #for n in range(9): print(kekule(n))

"""
    # A050446
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 3, 6, 10, 15, 21, 28, 36, 45]
    [1, 5, 14, 30, 55, 91, 140, 204, 285]
    [1, 8, 31, 85, 190, 371, 658, 1086, 1695]
    [1, 13, 70, 246, 671, 1547, 3164, 5916, 10317]
    [1, 21, 157, 707, 2353, 6405, 15106, 31998, 62349]
    [1, 34, 353, 2037, 8272, 26585, 72302, 173502, 377739]
    [1, 55, 793, 5864, 29056, 110254, 345775, 940005, 2286648]
    [1, 89, 1782, 16886, 102091, 457379, 1654092, 5094220, 13846117]
"""

''' OEIS

The traits of the Kekule triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Rev:Inv-RowSum   | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000045 | Std-DiagCol1     | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 5   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 7   | A000330 | Std-DiagRow3     | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1) |
| 8   | A000578 | Std-PolyRow3     | The cubes: a(n) = n^3                                                          |
| 9   | A006356 | Std-DiagCol2     | a(n) = 2*a(n-1) + a(n-2) - a(n-3) for n >= 3, starting with a(0) = 1, a(1) = 3 |
| 10  | A006357 | Std-DiagCol3     | Number of distributive lattices; also number of paths with n turns when light  |
| 11  | A019590 | Rev:Inv-AccRevSu | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 12  | A039968 | Rev:Inv-TransSqr | An example of a d-perfect sequence                                             |
| 13  | A050446 | Std-Triangle     | Table read by ascending antidiagonals: T(n, m) giving total degree of n-th-ord |
| 14  | A050447 | Std-Rev          | Table T(n,m) giving total degree of n-th-order elementary symmetric polynomial |
| 15  | A063524 | Rev:Inv-TransNat | Characteristic function of 1                                                   |
| 16  | A132199 | Std-RowGcd       | Rowland's prime-generating sequence: first differences of A106108              |
| 17  | A276313 | Std-CentralO     | Number of weak up-down sequences of length n and values in {1,2,...,n}         |
| 18  | A373353 | Std-RowSum       | Row sums of A373424                                                            |
| 19  | A373659 | Std-CentralE     | a(n) = A050446(n, n) = A050447(n, n)                                           |

* Statistic about Kekule:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 19.
	all      A-numbers  : 64.
	missing  sequences  : 111.

[('missing', 111), ('A000027', 7), ('A373353', 6), ('A000012', 6), ('A132199', 4), ('A050447', 4), ('A000578', 4), ('A000290', 4), ('A000045', 4), ('A373659', 3), ('A050446', 3), ('A006357', 3), ('A006356', 3), ('A000330', 3), ('A000217', 3), ('A276313', 2), ('A019590', 2), ('A063524', 1), ('A039968', 1), ('A000007', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Kekule.html .
2025/01/10

'''
