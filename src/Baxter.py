from functools import cache
from math import factorial
from _tabltypes import MakeTriangle


"""Baxter polynomials.

[0] 1
[1] 0, 1
[2] 0, 1,   1
[3] 0, 1,   4,    1
[4] 0, 1,  10,   10,     1
[5] 0, 1,  20,   50,    20,     1
[6] 0, 1,  35,  175,   175,    35,     1
[7] 0, 1,  56,  490,   980,   490,    56,    1
[8] 0, 1,  84, 1176,  4116,  4116,  1176,   84,   1
[9] 0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1
"""


@cache
def F(n: int) -> int:
    return factorial(n) ** 3 * ((n + 1) * (n + 1) * (n + 2))


@cache
def baxter(n: int) -> list[int]:
    if n == 0:
        return [1]

    return [0] + [(2 * F(n - 1)) // (F(k - 1) * F(n - k)) for k in range(1, n + 1)]


@MakeTriangle(baxter, "Baxter", ["A359363", "A056939"], False)
def Baxter(n: int, k: int) -> int:
    return baxter(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Baxter)


''' OEIS

The traits of the Baxter triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000292 | Std-DiagRow1     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 5   | A001181 | Std-RowSum       | Number of Baxter permutations of length n (also called Baxter numbers)         |
| 6   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 7   | A006542 | Std-DiagRow2     | a(n) = binomial(n,3)*binomial(n-1,3)/4                                         |
| 8   | A028872 | Rev-PolyRow3     | a(n) = n^2 - 3                                                                 |
| 9   | A047819 | Std-DiagRow3     | a(n) = Product_{i=1..n} ((i+3)*(i+4)*(i+5))/(i*(i+1)*(i+2))                    |
| 10  | A350265 | Std-AccSum       | a(n) = hypergeometric([-n - 1, 1 - n, -n], [1, 3], -1)                         |
| 11  | A359363 | Std-Triangle     | Triangle read by rows. The coefficients of the Baxter polynomials p(0, x) = 1  |
| 12  | A368708 | Std-PosHalf      | a(n) = hypergeom([-1 - n, -n, 1 - n], [2, 3], -2)                              |
| 13  | A368709 | Std-NegHalf      | a(n) = hypergeom([-1 - n, -n, 1 - n], [2, 3], +2)                              |
| 14  | A368733 | Rev-PolyCol3     | a(n) = hypergeom([-1 - n, -n, 1 - n], [2, 3], -3)                              |

* Statistic about Baxter:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 14.
	all      A-numbers  : 51.
	missing  sequences  : 78.

[('missing', 78), ('A006542', 6), ('A001181', 6), ('A000292', 6), ('A000012', 6), ('A359363', 5), ('A350265', 4), ('A368708', 3), ('A047819', 3), ('A000027', 3), ('A000007', 3), ('A368709', 2), ('A002378', 2), ('A368733', 1), ('A028872', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Baxter.html .
2025/01/10

'''
