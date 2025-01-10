from functools import cache
from _tabltypes import MakeTriangle

"""(Probabilist's) Hermite polynomials He, unsigned coefficients.

[0] [ 1]
[1] [ 0,   1]
[2] [ 1,   0,  1]
[3] [ 0,   3,  0,   1]
[4] [ 3,   0,  6,   0,  1]
[5] [ 0,  15,  0,  10,  0,  1]
[6] [15,   0, 45,   0, 15,  0, 1]
[7] [ 0, 105,  0, 105,  0, 21, 0, 1]
"""


@cache
def hermitee(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 1
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (n - k)
    return row


@MakeTriangle(hermitee, "HermiteE", ["A099174", "A066325", "A073278"], True)
def HermiteE(n: int, k: int) -> int:
    return hermitee(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HermiteE)

''' OEIS

The traits of the HermiteE triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000085 | Std-RowSum       | Number of self-inverse permutations on n letters, also known as involutions; n |
| 4   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 5   | A000457 | Std-DiagCol3     | Exponential generating function: (1+3*x)/(1-2*x)^(7/2)                         |
| 6   | A001464 | Inv-RowSum       | Expansion of e.g.f. exp(-x - (1/2)*x^2)                                        |
| 7   | A001515 | Std-DiagSum      | Bessel polynomial y_n(x) evaluated at x=1                                      |
| 8   | A001879 | Std-DiagCol2     | a(n) = (2n+2)!/(n!*2^(n+1))                                                    |
| 9   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 10  | A005425 | Std-PolyCol2     | a(n) = 2*a(n-1) + (n-1)*a(n-2)                                                 |
| 11  | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 12  | A013989 | Std-TransNat0    | a(n) = (n+1)*(a(n-1)/n + a(n-2)), with a(0)=1, a(1)=2                          |
| 13  | A056107 | Rev-PolyRow3     | Third spoke of a hexagonal spiral                                              |
| 14  | A058794 | Inv-PolyRow3     | Row 3 of A007754                                                               |
| 15  | A066223 | Std-EvenSum      | Bisection of A000085                                                           |
| 16  | A066224 | Std-OddSum       | Bisection of A000085                                                           |
| 17  | A069834 | Std-RowGcd       | a(n) = n-th reduced triangular number: n*(n+1)/{2^k} where 2^k is the largest  |
| 18  | A079908 | Std-PolyRow3     | Solution to the Dancing School Problem with 3 girls and n+3 boys: f(3,n)       |
| 19  | A080663 | Inv:Rev-PolyRow3 | a(n) = 3*n^2 - 1                                                               |
| 20  | A089466 | Inv-PolyDiag     | Inverse hyperbinomial transform of A089467                                     |
| 21  | A099174 | Std-Triangle     | Triangle read by rows: coefficients of modified Hermite polynomials            |
| 22  | A115329 | Std-PosHalf      | Expansion of e.g.f.: exp(x + 2*x^2)                                            |
| 23  | A123023 | Std-ColLeft      | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 24  | A131441 | Inv-OddSum       | Row sums of triangle A130757 (coefficients of scaled Laguerre-Sonin polynomial |
| 25  | A202834 | Std-PolyCol3     | E.g.f.: exp(3*x + x^2/2)                                                       |
| 26  | A278990 | Alt-DiagSum      | Number of loopless linear chord diagrams with n chords                         |
| 27  | A344501 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*HT(n, k) = Sum_{k=0..n} (-1)^(n-k)*binomial |
| 28  | A359739 | Rev-PolyDiag     | a(n) = Sum_{j=0..n, j even} binomial(n, j) * oddfactorial(j/2) * n^j, where od |
| 29  | A359760 | Std-Rev          | Triangle read by rows. The Kummer triangle, the coefficients of the Kummer pol |
| 30  | A359761 | Std-CentralE     | a(n) = binomial(4*n, 2*n)*(2*n)!/(2^n*n!)                                      |
| 31  | A362176 | Inv-PosHalf      | Expansion of e.g.f. exp(x * (1-2*x))                                           |
| 32  | A362718 | Inv-EvenSum      | Expansion of e.g.f. cos(x)*exp(x^2/2) = Sum_{n>=0} a(n)*x^(2*n)/(2*n)!         |

* Statistic about HermiteE:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 32.
	all      A-numbers  : 116.
	missing  sequences  : 80.

[('missing', 80), ('A000085', 17), ('A123023', 10), ('A344501', 6), ('A000012', 6), ('A359761', 5), ('A115329', 5), ('A069834', 5), ('A001879', 5), ('A001464', 5), ('A000457', 5), ('A000217', 5), ('A359760', 4), ('A005425', 4), ('A362176', 3), ('A099174', 3), ('A002522', 3), ('A000027', 3), ('A278990', 2), ('A202834', 2), ('A079908', 2), ('A066224', 2), ('A066223', 2), ('A013989', 2), ('A005563', 2), ('A362718', 1), ('A359739', 1), ('A131441', 1), ('A089466', 1), ('A080663', 1), ('A058794', 1), ('A056107', 1), ('A001515', 1)]

A related webpage is: https://peterluschny.github.io/tabl/HermiteE.html .
2025/01/10

'''
