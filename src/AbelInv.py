"""
This module provides functions to generate the inverse of the Abel Table. They are
considered here in the unsigned (absolute) form in which they are also called idempotent numbers.
InvAbel is a `Table` object that provides a multitude of methods to investigate 
the inverse of the Abel table. 

Functions:
    invabel(n: int) -> list[int]:
        Computes the coefficients of the n-th polynomial that are given by the n-th row of the inverse Abel Table.

    The InvAbel object can be used to access the coefficients of the InvAbel polynomials directly:
 
    InvAbel(n: int, k: int) -> int:
        Returns the k-th coefficient of the n-th InvAbel polynomial.

Example:
    >>> invabel(3)
    [0, 3, 6, 1]
    >>> InvAbel(3, 2)
    6

References:
    Variants of the triangle are https://oeis.org/A059297 and A059298.
    The triangle is invertible and the inverse is A137452, the triangle of the coefficients of the Abel polynomials.
    An overview is given in https://peterluschny.github.io/tabl/Abel.html
"""

from functools import cache
from Binomial import binomial
from Powers import powers
from _tabltypes import MakeTriangle

'''
Inverse of Abel, unsigned version. Triangle of idempotent numbers. 

[0]  1;
[1]  0,  1;
[2]  0,  2,    1;
[3]  0,  3,    6,     1;
[4]  0,  4,   24,    12,     1;
[5]  0,  5,   80,    90,    20,     1;
[6]  0,  6,  240,   540,   240,    30,     1;
[7]  0,  7,  672,  2835,  2240,   525,    42,    1;
[8]  0,  8, 1792, 11340, 15680,  5880,   980,   56,  1;
[9]  0,  9, 4608, 41580, 94080, 52920, 11760, 1260, 72, 1;
'''

@cache
def abelinv(n: int) -> list[int]:

    b = binomial(n)
    p = powers(n)
    return [b[k] * p[k] for k in range(n + 1)]


@MakeTriangle(abelinv, "AbelInv", ["A059297", "A059298"], True)
def AbelInv(n: int, k: int) -> int:
    return abelinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(AbelInv, short=True)


''' OEIS

The traits of the AbelInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000169 | Inv-RowMax       | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 5   | A000248 | Std-RowSum       | Expansion of e.g.f. exp(x*exp(x))                                              |
| 6   | A000272 | Inv-AltSum       | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 7   | A000312 | Inv-RowSum       | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 8   | A001788 | Std-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 9   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A003725 | Std-AltSum       | E.g.f.: exp( x * exp(-x) )                                                     |
| 11  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A007334 | Inv:Rev-NegHalf  | Number of spanning trees in the graph K_{n}/e, which results from contracting  |
| 14  | A009121 | Std-EvenSum      | Expansion of e.g.f. cosh(exp(x)*x)                                             |
| 15  | A009565 | Std-OddSum       | Expansion of e.g.f. sinh(exp(x)*x)                                             |
| 16  | A016790 | Inv:Rev-PolyRow3 | a(n) = (3n+2)^2                                                                |
| 17  | A019590 | Inv-PolyDiag     | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 18  | A036216 | Std-DiagCol3     | Expansion of 1/(1 - 3*x)^4; 4-fold convolution of A000244 (powers of 3)        |
| 19  | A052750 | Inv-NegHalf      | a(n) = (2*n + 1)^(n - 1)                                                       |
| 20  | A053506 | Inv-DiagCol2     | a(n) = (n-1)*n^(n-2)                                                           |
| 21  | A053507 | Inv-DiagCol3     | a(n) = binomial(n-1,2)*n^(n-3)                                                 |
| 22  | A055541 | Inv-TransSqrs    | Total number of leaves (nodes of vertex degree 1) in all labeled trees with n  |
| 23  | A055897 | Inv:Rev-TransNat | a(n) = n*(n-1)^(n-1)                                                           |
| 24  | A059297 | Std-Triangle     | Triangle of idempotent numbers binomial(n,k)*k^(n-k), version 1                |
| 25  | A059299 | Std-Rev          | Triangle of idempotent numbers (version 3), T(n, k) = binomial(n, k) * (n - k) |
| 26  | A063524 | Inv-TransNat0    | Characteristic function of 1                                                   |
| 27  | A085527 | Inv-PosHalf      | a(n) = (2n+1)^n                                                                |
| 28  | A100536 | Rev-PolyRow3     | a(n) = 3*n^2 - 2                                                               |
| 29  | A137452 | Std-Inv          | Triangular array of the coefficients of the sequence of Abel polynomials A(n,x |
| 30  | A174841 | Inv:Rev-PolyDiag | Determinant of the symmetric n X n matrix M_n where M_n(j,k) = n^abs(j-k)      |
| 31  | A185298 | Std-TransNat0    | Expansion of e.g.f. x*exp(x)*exp(x*exp(x))                                     |
| 32  | A195136 | Inv-OddSum       | a(n) = ((n+1)^(n-1) + (n-1)^(n-1))/2 for n>=1                                  |
| 33  | A195509 | Rev-EvenSum      | Expansion of e.g.f. (exp(x*exp(x)) + exp(x/exp(x)))/2                          |
| 34  | A216689 | Std-PosHalf      | Expansion of e.g.f. exp( x * exp(x)^2 )                                        |
| 35  | A274265 | Inv:Rev-PolyCol3 | a(n) = (3*n - 1)^(n-1)                                                         |
| 36  | A274278 | Inv-EvenSum      | a(n) = ((n+1)^(n-1) - (n-1)^(n-1))/2 for n>=1                                  |
| 37  | A275707 | Std-PolyCol2     | Number of partial functions f:{1,2,...,n}->{1,2,...,n} such that every element |
| 38  | A295552 | Rev-PolyDiag     | a(n) = n! * [x^n] exp(x*exp(n*x))                                              |
| 39  | A295623 | Std-PolyDiag     | a(n) = n! * [x^n] exp(n*x*exp(x))                                              |
| 40  | A355501 | Std-PolyCol3     | Expansion of e.g.f. exp(3 * x * exp(x))                                        |
| 41  | A356819 | Std-NegHalf      | Expansion of e.g.f. exp(-x * exp(2*x))                                         |
| 42  | A356827 | Rev-PolyCol3     | Expansion of e.g.f. exp(x * exp(3*x))                                          |
| 43  | A360782 | Rev-DiagSum      | Expansion of Sum_{k>=0} x^k / (1 - k*x^2)^(k+1)                                |
| 44  | A360814 | Std-DiagSum      | Expansion of Sum_{k>=0} x^(2*k) / (1 - k*x)^(k+1)                              |
| 45  | A366151 | Inv-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1/2)^(n-k |
| 46  | A367254 | Inv-CentralE     | a(n) = binomial(2*n - 1, n - 1)*(2*n)^n                                        |
| 47  | A367256 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, k - 1) * n^(n - k)        |
| 48  | A367257 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, n - k - 1) * (-n)^k       |
| 49  | A367271 | Std-CentralE     | a(n) = binomial(2*n, n) * n^n                                                  |
| 50  | A367272 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * k^(n - k)                               |
| 51  | A367273 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)^2 * (k - n)^k                               |
| 52  | A367274 | Rev-ColMiddle    | a(n) = binomial(n, k) * (n - k)^k where k = floor(n/2)                         |


* Statistic about AbelInv:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 52.
	all      A-numbers  : 125.
	missing  sequences  : 90.

[('missing', 90), ('A000027', 11), ('A000248', 6), ('A000012', 6), ('A002378', 5), ('A000312', 5), ('A000007', 5), ('A137452', 4), ('A059299', 4), ('A000272', 4), ('A000169', 4), ('A367273', 3), ('A367272', 3), ('A367271', 3), ('A216689', 3), ('A059297', 3), ('A036216', 3), ('A005563', 3), ('A003725', 3), ('A001788', 3), ('A367257', 2), ('A367256', 2), ('A367254', 2), ('A356819', 2), ('A275707', 2), ('A085527', 2), ('A053507', 2), ('A053506', 2), ('A009565', 2), ('A009121', 2), ('A005408', 2), ('A367274', 1), ('A366151', 1), ('A360814', 1), ('A360782', 1), ('A356827', 1), ('A355501', 1), ('A295623', 1), ('A295552', 1), ('A274278', 1), ('A274265', 1), ('A195509', 1), ('A195136', 1), ('A185298', 1), ('A174841', 1), ('A100536', 1), ('A063524', 1), ('A055897', 1), ('A055541', 1), ('A052750', 1), ('A019590', 1), ('A016790', 1), ('A007334', 1)]

A related webpage is: https://peterluschny.github.io/tabl/AbelInv.html .
2025/02/06

'''
