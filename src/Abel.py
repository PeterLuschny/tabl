from functools import cache
from Binomial import binomial
from _tabltypes import MakeTriangle


"""Abel polynomials (unsigned coefficients).
[0] [1]
[1] [0,        1]
[2] [0,        2,       1]
[3] [0,        9,       6,       1]
[4] [0,       64,      48,      12,      1]
[5] [0,      625,     500,     150,     20,      1]
[6] [0,     7776,    6480,    2160,    360,     30,    1]
[7] [0,   117649,  100842,   36015,   6860,    735,   42,   1]
[8] [0,  2097152, 1835008,  688128, 143360,  17920, 1344,  56, 1]
"""


@cache
def abel(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = binomial(n - 1)
    return [b[k - 1] * n ** (n - k) if k > 0 else 0 for k in range(n + 1)]


@MakeTriangle(abel, "Abel", ["A137452", "A061356", "A139526"], True)
def Abel(n: int, k: int) -> int:
    return abel(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Abel, short=True)


''' OEIS

The traits of the Abel triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000169 | Std-RowMax       | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 5   | A000248 | Inv-AltSum       | Expansion of e.g.f. exp(x*exp(x))                                              |
| 6   | A000272 | Std-RowSum       | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 7   | A000312 | Std-AltSum       | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 8   | A001788 | Inv-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 9   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A003725 | Inv-RowSum       | E.g.f.: exp( x * exp(-x) )                                                     |
| 11  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A007334 | Std-PolyCol2     | Number of spanning trees in the graph K_{n}/e, which results from contracting  |
| 14  | A009121 | Inv-EvenSum      | Expansion of e.g.f. cosh(exp(x)*x)                                             |
| 15  | A009565 | Inv-OddSum       | Expansion of e.g.f. sinh(exp(x)*x)                                             |
| 16  | A016778 | Rev-PolyRow3     | a(n) = (3*n+1)^2                                                               |
| 17  | A036216 | Inv-DiagCol3     | Expansion of 1/(1 - 3*x)^4; 4-fold convolution of A000244 (powers of 3)        |
| 18  | A052750 | Std-PosHalf      | a(n) = (2*n + 1)^(n - 1)                                                       |
| 19  | A052752 | Rev-PolyCol3     | a(n) = (3*n+1)^(n-1)                                                           |
| 20  | A053506 | Std-DiagCol2     | a(n) = (n-1)*n^(n-2)                                                           |
| 21  | A053507 | Std-DiagCol3     | a(n) = binomial(n-1,2)*n^(n-3)                                                 |
| 22  | A055541 | Alt-TransSqrs    | Total number of leaves (nodes of vertex degree 1) in all labeled trees with n  |
| 23  | A059297 | Std-Inv          | Triangle of idempotent numbers binomial(n,k)*k^(n-k), version 1                |
| 24  | A059299 | Std-RevInv       | Triangle of idempotent numbers (version 3), T(n, k) = binomial(n, k) * (n - k) |
| 25  | A063524 | Alt-TransNat0    | Characteristic function of 1                                                   |
| 26  | A065513 | Rev-TransNat0    | Number of endofunctions of [n] with a cycle a->b->c->a and for all x in [n], s |
| 27  | A085527 | Std-NegHalf      | a(n) = (2n+1)^n                                                                |
| 28  | A089946 | Std-TransNat0    | Secondary diagonal of array A089944, in which the n-th row is the n-th binomia |
| 29  | A100536 | Inv:Rev-PolyRow3 | a(n) = 3*n^2 - 2                                                               |
| 30  | A137452 | Std-Triangle     | Triangular array of the coefficients of the sequence of Abel polynomials A(n,x |
| 31  | A193678 | Std-PolyDiag     | Discriminant of Chebyshev C-polynomials                                        |
| 32  | A195136 | Std-OddSum       | a(n) = ((n+1)^(n-1) + (n-1)^(n-1))/2 for n>=1                                  |
| 33  | A195509 | Inv:Rev-EvenSum  | Expansion of e.g.f. (exp(x*exp(x)) + exp(x/exp(x)))/2                          |
| 34  | A216689 | Inv-NegHalf      | Expansion of e.g.f. exp( x * exp(x)^2 )                                        |
| 35  | A225497 | Std-TransSqrs    | Total number of rooted labeled trees over all forests on {1,2,...,n} in which  |
| 36  | A232006 | Std-Poly         | Triangular array read by rows: T(n,k) is the number of simple labeled graphs o |
| 37  | A274278 | Std-EvenSum      | a(n) = ((n+1)^(n-1) - (n-1)^(n-1))/2 for n>=1                                  |
| 38  | A275707 | Inv:Rev-NegHalf  | Number of partial functions f:{1,2,...,n}->{1,2,...,n} such that every element |
| 39  | A320258 | Inv:Rev-PolyDiag | a(n) = n! * [x^n] exp(x*exp(-n*x))                                             |
| 40  | A356819 | Inv-PosHalf      | Expansion of e.g.f. exp(-x * exp(2*x))                                         |
| 41  | A356820 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp(-x * exp(3*x))                                         |
| 42  | A360814 | Inv-DiagSum      | Expansion of Sum_{k>=0} x^(2*k) / (1 - k*x)^(k+1)                              |
| 43  | A362354 | Std-PolyCol3     | a(n) = 3*(n+3)^(n-1)                                                           |
| 44  | A366151 | Alt-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1/2)^(n-k |
| 45  | A367254 | Std-CentralE     | a(n) = binomial(2*n - 1, n - 1)*(2*n)^n                                        |
| 46  | A367255 | Std-AccRevSum    | a(n) = (n + 1)^(n - 2)*(3*n + 1)                                               |
| 47  | A367256 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, k - 1) * n^(n - k)        |
| 48  | A367257 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, n - k - 1) * (-n)^k       |
| 49  | A367271 | Inv-CentralE     | a(n) = binomial(2*n, n) * n^n                                                  |
| 50  | A367272 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)^2 * k^(n - k)                               |
| 51  | A367273 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * (k - n)^k                               |
| 52  | A367274 | Inv:Rev-ColMiddl | a(n) = binomial(n, k) * (n - k)^k where k = floor(n/2)                         |

* Statistic about Abel:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 52.
	all      A-numbers  : 126.
	missing  sequences  : 88.

[('missing', 88), ('A000027', 10), ('A000272', 6), ('A000169', 6), ('A000012', 6), ('A002378', 5), ('A000312', 5), ('A000007', 5), ('A059297', 4), ('A000248', 4), ('A367257', 3), ('A367256', 3), ('A367255', 3), ('A367254', 3), ('A137452', 3), ('A059299', 3), ('A053507', 3), ('A053506', 3), ('A052750', 3), ('A005563', 3), ('A367273', 2), ('A367272', 2), ('A367271', 2), ('A356819', 2), ('A274278', 2), ('A195136', 2), ('A085527', 2), ('A036216', 2), ('A007334', 2), ('A005408', 2), ('A003725', 2), ('A001788', 2), ('A367274', 1), ('A366151', 1), ('A362354', 1), ('A360814', 1), ('A356820', 1), ('A320258', 1), ('A275707', 1), ('A232006', 1), ('A225497', 1), ('A216689', 1), ('A195509', 1), ('A193678', 1), ('A100536', 1), ('A089946', 1), ('A065513', 1), ('A063524', 1), ('A055541', 1), ('A052752', 1), ('A016778', 1), ('A009565', 1), ('A009121', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Abel.html .
2025/01/10

'''
