from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Motzkin polynomials.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   2
[5] 1, 0, 10, 0,  10, 0
[6] 1, 0, 15, 0,  30, 0,   5
[7] 1, 0, 21, 0,  70, 0,  35, 0
[8] 1, 0, 28, 0, 140, 0, 140, 0,  14
[9] 1, 0, 36, 0, 252, 0, 420, 0, 126, 0
"""


@cache
def motzkinpoly(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    h = 0 if n % 2 else (motzkinpoly(n - 2)[n - 2] * 2 * (n - 1)) // (n // 2 + 1)
    row = motzkinpoly(n - 1) + [h]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@MakeTriangle(motzkinpoly, "MotzkinPoly", ["A359364"], False)
def MotzkinPoly(n: int, k: int) -> int:
    return motzkinpoly(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(MotzkinPoly)

''' OEIS

The traits of the MotzkinPoly triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Rev-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000108 | Std-PosHalf      | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 4   | A000217 | Std-DiagCol2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 5   | A001006 | Std-RowSum       | Motzkin numbers: number of ways of drawing any number of nonintersecting chord |
| 6   | A002212 | Rev-PolyCol3     | Number of restricted hexagonal polyominoes with n cells                        |
| 7   | A002457 | Std-DiagRow2     | a(n) = (2n+1)!/n!^2                                                            |
| 8   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 9   | A002802 | Std-DiagRow3     | a(n) = (2*n+3)!/(6*n!*(n+1)!)                                                  |
| 10  | A005563 | Rev:Inv-PolyRow2 | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 11  | A005717 | Rev-TransNat0    | Construct triangle in which n-th row is obtained by expanding (1 + x + x^2)^n  |
| 12  | A006318 | Rev-DiagSum      | Large Schroeder numbers (or large Schroeder numbers, or big Schroeder numbers) |
| 13  | A023426 | Std-DiagSum      | a(n) = a(n-1) + Sum_{k=0..n-4} a(k)*a(n-4-k), a(0) = 1. Generalized Catalan Nu |
| 14  | A025179 | Std-AccRevSum    | a(n) = number of (s(0), s(1), ..., s(n)) such that s(i) is an integer, s(0) =  |
| 15  | A026945 | Rev-EvenSum      | A bisection of the Motzkin numbers A001006                                     |
| 16  | A056107 | Std-PolyRow3     | Third spoke of a hexagonal spiral                                              |
| 17  | A058794 | Rev:Inv-PolyRow3 | Row 3 of A007754                                                               |
| 18  | A079908 | Rev-PolyRow3     | Solution to the Dancing School Problem with 3 girls and n+3 boys: f(3,n)       |
| 19  | A091147 | Std-PolyCol2     | Expansion of (1-x-sqrt(1-2x-15x^2))/(8x^2)                                     |
| 20  | A097610 | Std-Rev          | Triangle read by rows: T(n,k) is number of Motzkin paths of length n and havin |
| 21  | A099250 | Rev-OddSum       | Bisection of Motzkin numbers A001006                                           |
| 22  | A126120 | Std-ColRight     | Catalan numbers (A000108) interpolated with 0's                                |
| 23  | A138364 | Std-DiagRow1     | The number of Motzkin n-paths with exactly one flat step                       |
| 24  | A189912 | Std-AccSum       | Extended Motzkin numbers, Sum_{k>=0} C(n,k)C(k), C(k) the extended Catalan num |
| 25  | A238390 | Rev:Inv-ColLeft  | E.g.f.: x / BesselJ(1, 2*x) (even powers only)                                 |
| 26  | A247495 | Rev-Poly         | Generalized Motzkin numbers: Square array read by descending antidiagonals, T( |
| 27  | A247496 | Rev-PolyDiag     | a(n) = n!*[x^n](exp(n*x)*BesselI_{1}(2*x)/x), n>=0, main diagonal of A247495   |
| 28  | A308846 | Rev:Inv-RowSum   | Expansion of e.g.f. x*exp(-x) / BesselI(1,2*x)                                 |
| 29  | A359364 | Std-Triangle     | Triangle read by rows. The Motzkin triangle, the coefficients of the Motzkin p |
| 30  | A359647 | Std-CentralE     | a(n) = [x^n] hypergeom([1/4, 3/4], [2], 64*x). The central terms of the Motzki |
| 31  | A359649 | Std-PolyDiag     | a(n) = hypergeom([(1 - n)/2, -n/2], [2], 4*n^2)                                |

* Statistic about MotzkinPoly:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 31.
	all      A-numbers  : 85.
	missing  sequences  : 78.

[('missing', 78), ('A001006', 11), ('A000012', 6), ('A025179', 5), ('A000108', 5), ('A189912', 4), ('A097610', 4), ('A091147', 4), ('A000217', 4), ('A359647', 3), ('A359364', 3), ('A138364', 3), ('A126120', 3), ('A002802', 3), ('A002522', 3), ('A002457', 3), ('A359649', 2), ('A308846', 2), ('A056107', 2), ('A023426', 2), ('A000027', 2), ('A247496', 1), ('A247495', 1), ('A238390', 1), ('A099250', 1), ('A079908', 1), ('A058794', 1), ('A026945', 1), ('A006318', 1), ('A005717', 1), ('A005563', 1), ('A002212', 1)]

A related webpage is: https://peterluschny.github.io/tabl/MotzkinPoly.html .
2025/01/10

'''
