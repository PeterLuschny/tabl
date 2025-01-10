from functools import cache
from _tabltypes import MakeTriangle

"""Bessel2 triangle.

[0] 1
[1] 1, 0
[2] 1, 0,  1
[3] 1, 0,  3, 0
[4] 1, 0,  6, 0,   3
[5] 1, 0, 10, 0,  15, 0
[6] 1, 0, 15, 0,  45, 0,   15
[7] 1, 0, 21, 0, 105, 0,  105, 0
[8] 1, 0, 28, 0, 210, 0,  420, 0, 105
[9] 1, 0, 36, 0, 378, 0, 1260, 0, 945, 0
"""

@cache
def bessel2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]

    row = bessel2(n - 1) + [0]
    row[n] = 0 if n % 2 else row[n - 2]
    for k in range(2, n, 2):
        row[k] = (n * row[k]) // (n - k)
    return row


@MakeTriangle(
    bessel2,
    "Bessel2",
    ["A359760", "A073278", "A066325", "A099174", "A111924", "A144299", "A104556"],
    False,
)
def Bessel2(n: int, k: int) -> int:
    return bessel2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Bessel2)


''' OEIS

The traits of the Bessel2 triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Rev-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000085 | Std-RowSum       | Number of self-inverse permutations on n letters, also known as involutions; n |
| 4   | A000217 | Std-DiagCol2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 5   | A000457 | Std-DiagRow3     | Exponential generating function: (1+3*x)/(1-2*x)^(7/2)                         |
| 6   | A001464 | Rev:Inv-RowSum   | Expansion of e.g.f. exp(-x - (1/2)*x^2)                                        |
| 7   | A001515 | Rev-DiagSum      | Bessel polynomial y_n(x) evaluated at x=1                                      |
| 8   | A001879 | Std-DiagRow2     | a(n) = (2n+2)!/(n!*2^(n+1))                                                    |
| 9   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 10  | A005425 | Std-PosHalf      | a(n) = 2*a(n-1) + (n-1)*a(n-2)                                                 |
| 11  | A005563 | Rev:Inv-PolyRow2 | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 12  | A013989 | Rev-TransNat0    | a(n) = (n+1)*(a(n-1)/n + a(n-2)), with a(0)=1, a(1)=2                          |
| 13  | A056107 | Std-PolyRow3     | Third spoke of a hexagonal spiral                                              |
| 14  | A058794 | Rev:Inv-PolyRow3 | Row 3 of A007754                                                               |
| 15  | A066223 | Rev-EvenSum      | Bisection of A000085                                                           |
| 16  | A066224 | Rev-OddSum       | Bisection of A000085                                                           |
| 17  | A069834 | Std-RowGcd       | a(n) = n-th reduced triangular number: n*(n+1)/{2^k} where 2^k is the largest  |
| 18  | A079908 | Rev-PolyRow3     | Solution to the Dancing School Problem with 3 girls and n+3 boys: f(3,n)       |
| 19  | A089466 | Rev:Inv-PolyDiag | Inverse hyperbinomial transform of A089467                                     |
| 20  | A099174 | Std-Rev          | Triangle read by rows: coefficients of modified Hermite polynomials            |
| 21  | A115329 | Std-PolyCol2     | Expansion of e.g.f.: exp(x + 2*x^2)                                            |
| 22  | A123023 | Std-ColRight     | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 23  | A131441 | Rev:Inv-OddSum   | Row sums of triangle A130757 (coefficients of scaled Laguerre-Sonin polynomial |
| 24  | A202834 | Rev-PolyCol3     | E.g.f.: exp(3*x + x^2/2)                                                       |
| 25  | A278990 | Rev:Inv-DiagSum  | Number of loopless linear chord diagrams with n chords                         |
| 26  | A344501 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*HT(n, k) = Sum_{k=0..n} (-1)^(n-k)*binomial |
| 27  | A359739 | Std-PolyDiag     | a(n) = Sum_{j=0..n, j even} binomial(n, j) * oddfactorial(j/2) * n^j, where od |
| 28  | A359760 | Std-Triangle     | Triangle read by rows. The Kummer triangle, the coefficients of the Kummer pol |
| 29  | A359761 | Std-CentralE     | a(n) = binomial(4*n, 2*n)*(2*n)!/(2^n*n!)                                      |
| 30  | A362176 | Rev:Inv-PosHalf  | Expansion of e.g.f. exp(x * (1-2*x))                                           |
| 31  | A362718 | Rev:Inv-EvenSum  | Expansion of e.g.f. cos(x)*exp(x^2/2) = Sum_{n>=0} a(n)*x^(2*n)/(2*n)!         |

* Statistic about Bessel2:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 31.
	all      A-numbers  : 97.
	missing  sequences  : 60.

[('missing', 60), ('A000085', 16), ('A123023', 8), ('A344501', 6), ('A000012', 6), ('A005425', 5), ('A359761', 4), ('A115329', 4), ('A099174', 4), ('A069834', 4), ('A001879', 4), ('A000457', 4), ('A000217', 4), ('A359760', 3), ('A002522', 3), ('A362176', 2), ('A359739', 2), ('A056107', 2), ('A001464', 2), ('A000027', 2), ('A362718', 1), ('A278990', 1), ('A202834', 1), ('A131441', 1), ('A089466', 1), ('A079908', 1), ('A066224', 1), ('A066223', 1), ('A058794', 1), ('A013989', 1), ('A005563', 1), ('A001515', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Bessel2.html .
2025/01/10

'''
