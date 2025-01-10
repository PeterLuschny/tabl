from functools import cache
from Binomial import binomial
from DistLattices import dist_latt
from _tabltypes import MakeTriangle

"""EulerianZigZag triangle.

[0] [1]
[1] [1,  0]
[2] [1,  0,   0]
[3] [1,  1,   0,   0]
[4] [1,  3,   1,   0,   0]
[5] [1,  7,   7,   1,   0,  0]
[6] [1, 14,  31,  14,   1,  0, 0]
[7] [1, 26, 109, 109,  26,  1, 0, 0]
[8] [1, 46, 334, 623, 334, 46, 1, 0, 0]
"""

@cache
def eulerianzigzag(n: int) -> list[int]:

    b = binomial(n + 1)
    return [sum((-1)**j * b[j] * dist_latt(n, k - j) for j in range(k + 1))
            for k in range(n + 1)]


@cache
def ezz(n: int) -> list[int]:
    n += 2
    b = binomial(n + 1)
    return [sum((-1)**j * b[j] * dist_latt(n, k - j) for j in range(k + 1))
            for k in range(n - 1)]


@MakeTriangle(eulerianzigzag, "EulerianZigZag", ["A205497"], False)
def EulerianZigZag(n: int, k: int) -> int:
    return eulerianzigzag(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerianZigZag)

''' OEIS

The traits of the EulerianZigZag triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColRight     | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow3     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000111 | Std-RowSum       | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the nu |
| 5   | A000290 | Rev-PolyRow2     | The squares: a(n) = n^2                                                        |
| 6   | A001924 | Std-DiagRow3     | Apply partial sum operator twice to Fibonacci numbers                          |
| 7   | A006326 | Std-TransNat0    | Total preorders                                                                |
| 8   | A011379 | Rev-PolyRow3     | a(n) = n^2*(n+1)                                                               |
| 9   | A045991 | Rev:Inv-PolyRow3 | a(n) = n^3 - n^2                                                               |
| 10  | A115944 | Rev:Inv-RowSum   | Number of partitions of n into distinct factorials                             |
| 11  | A205492 | Std-DiagCol2     | Expansion of (1-x^2-x^3-x^4+x^5)/((1-x)^3*(1-x-x^2)^2*(1-2*x-x^2+x^3))         |
| 12  | A205493 | Std-DiagCol3     | Third row or column of table A205497                                           |
| 13  | A350354 | Std-PolyCol2     | Number of up/down (or down/up) patterns of length n                            |
| 14  | A373388 | Std-AltSum       | Alternating row sums of the Eulerian zig-zag number triangle A205497           |
| 15  | A373389 | Alt-PolyCol2     | The Eulerian zig-zag polynomials A205497 evaluated at x = -1/2 and normalized  |
| 16  | A373752 | Std-EvenSum      | a(n) = Sum_{k=0..n-2} A205497(n, k) * (1 - k mod 2) if n >= 2, a(0) = a(1) = 1 |
| 17  | A373753 | Std-OddSum       | a(n) = Sum_{k=0..n-2} A205497(n, k) * (k mod 2)                                |
| 18  | A373755 | Std-RowMax       | a(n) = A205497(n, floor((n - 1) / 2)). The middle coefficients of the Eulerian |

* Statistic about EulerianZigZag:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 18.
	all      A-numbers  : 64.
	missing  sequences  : 108.

[('missing', 108), ('A000012', 11), ('A000007', 8), ('A001924', 7), ('A000111', 6), ('A000027', 4), ('A373755', 3), ('A373753', 3), ('A373752', 3), ('A373388', 3), ('A205493', 3), ('A205492', 3), ('A373389', 2), ('A350354', 2), ('A000290', 2), ('A115944', 1), ('A045991', 1), ('A011379', 1), ('A006326', 1)]

A related webpage is: https://peterluschny.github.io/tabl/EulerianZigZag.html .
2025/01/10

'''
