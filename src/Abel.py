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

'''
* Statistic about Abel:
The number of ...
        all      hashes    is 199.
        distinct hashes    is 116.
        core     triangles is 1.
        distinct types     is 5.
        missing  sequences is 86.
        all      A-numbers is 113.
        distinct A-numbers is 58.

The traits of the Abel triangle as represented in the OEIS.

|    | A-number| trait            | A-name                                                                  |
|----|---------|------------------|-------------------------------------------------------------------------|
| 1  | A000027 | Inv-DiagCol1     | The positive integers. Also called the natural numbers, the whole numb  |
| 2  | A000169 | Std-RowMax       | Number of labeled rooted trees with n nodes: n^(n-1)                    |
| 3  | A000248 | Inv-AltSum       | Expansion of e.g.f. exp(x*exp(x))                                       |
| 4  | A001477 | Std-PolyRow1     | The nonnegative integers                                                |
| 5  | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)      |
| 6  | A003725 | Inv-RowSum       | E.g.f.: exp( x * exp(-x) )                                              |
| 7  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                         |
| 8  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                            |
| 9  | A007334 | Std-PolyCol2     | Number of spanning trees in the graph K_{n}/e, which results from cont  |
| 10 | A009121 | Inv-EvenSum      | Expansion of e.g.f. cosh(exp(x)*x)                                      |
| 11 | A009565 | Inv-OddSum       | Expansion of e.g.f. sinh(exp(x)*x)                                      |
| 12 | A014026 | Alt-PolyDiag     | Inverse of 17th cyclotomic polynomial                                   |
| 13 | A016778 | Rev-PolyRow3     | a(n) = (3*n+1)^2                                                        |
| 14 | A028310 | Std-RowGcd       | Expansion of (1 - x + x^2) / (1 - x)^2 in powers of x                   |
| 15 | A033683 | Alt-TransNat0    | a(n) = 1 if n is an odd square not divisible by 3, otherwise 0          |
| 16 | A036216 | Inv-DiagCol3     | Expansion of 1/(1 - 3*x)^4; 4-fold convolution of A000244 (powers of 3  |
| 17 | A052750 | Std-PosHalf      | a(n) = (2*n + 1)^(n - 1)                                                |
| 18 | A052752 | Rev-PolyCol3     | a(n) = (3*n+1)^(n-1)                                                    |
| 19 | A059297 | Std-Inv          | Triangle of idempotent numbers binomial(n,k)*k^(n-k), version 1         |
| 20 | A059299 | Std-RevInv       | Triangle of idempotent numbers (version 3), T(n, k) = binomial(n, k) *  |
| 21 | A060747 | Inv:Rev-PolyRow2 | a(n) = 2*n - 1                                                          |
| 22 | A067998 | Alt-PolyRow2     | a(n) = n^2 - 2*n                                                        |
| 23 | A085527 | Std-NegHalf      | a(n) = (2n+1)^n                                                         |
| 24 | A089946 | Std-TransNat0    | Secondary diagonal of array A089944, in which the n-th row is the n-th  |
| 25 | A137452 | Std-Triangle     | Triangular array of the coefficients of the sequence of Abel polynomia  |
| 26 | A177885 | Std-AltSum       | a(n) = (1-n)^(n-1)                                                      |
| 27 | A193678 | Std-PolyDiag     | Discriminant of Chebyshev C-polynomials                                 |
| 28 | A195136 | Std-OddSum       | a(n) = ((n+1)^(n-1) + (n-1)^(n-1))/2 for n>=1                           |
| 29 | A195509 | Inv:Rev-EvenSum  | Expansion of e.g.f. (exp(x*exp(x)) + exp(x/exp(x)))/2                   |
| 30 | A208879 | Inv:Rev-Poly     | Number of words A(n,k), either empty or beginning with the first lette  |
| 31 | A216689 | Inv-NegHalf      | E.g.f. exp( x * exp(x)^2 )                                              |
| 32 | A225497 | Std-TransSqrs    | Total number of rooted labeled trees over all forests on {1,2,...,n} i  |
| 33 | A232006 | Std-Poly         | Triangular array read by rows: T(n,k) is the number of simple labeled   |
| 34 | A274278 | Std-EvenSum      | a(n) = ((n+1)^(n-1) - (n-1)^(n-1))/2 for n>=1                           |
| 35 | A274741 | Rev-Poly         | Table of coefficients in functions that satisfy W_n(x) = W_{n-1}(x)^W_  |
| 36 | A275707 | Inv:Rev-NegHalf  | Number of partial functions f:{1,2,...,n}->{1,2,...,n} such that ever   |
| 37 | A320258 | Inv:Rev-PolyDiag | a(n) = n! * [x^n] exp(x*exp(-n*x))                                      |
| 38 | A356819 | Inv-PosHalf      | Expansion of e.g.f. exp(-x * exp(2*x))                                  |
| 39 | A356820 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp(-x * exp(3*x))                                  |
| 40 | A360814 | Inv-DiagSum      | Expansion of Sum_{k>=0} x^(2*k) / (1 - k*x)^(k+1)                       |
| 41 | A362354 | Std-PolyCol3     | a(n) = 3*(n+3)^(n-1)                                                    |
| 42 | A367254 | Std-CentralE     | a(n) = binomial(2*n - 1, n - 1)*(2*n)^n                                 |
| 43 | A367255 | Std-AccRevSum    | a(n) = (n + 1)^(n - 2)*(3*n + 1)                                        |
| 44 | A367256 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, k - 1) * n^(n - k  |
| 45 | A367257 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k) * binomial(n - 1, n - k - 1) * (-n)  |
| 46 | A367271 | Inv-CentralE     | a(n) = binomial(2*n, n) * n^n                                           |
| 47 | A367272 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)^2 * k^(n - k)                        |
| 48 | A367273 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * (k - n)^k                        |
| 49 | A367274 | Inv:Rev-ColMiddle| a(n) = binomial(n, k) * (n - k)^k where k = floor(n/2)                  |
| 50 | B000272 | Std-RowSum       | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                 |
| 51 | B000312 | Alt-AccRevSum    | a(n) = n^n; number of labeled mappings from n points to themselves (en  |
| 52 | B001788 | Inv-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                  |
| 53 | B053506 | Std-DiagCol2     | a(n) = (n-1)*n^(n-2)                                                    |
| 54 | B053507 | Std-DiagCol3     | a(n) = binomial(n-1,2)*n^(n-3)                                          |
| 55 | B055541 | Alt-TransSqrs    | Total number of leaves (nodes of vertex degree 1) in all labeled trees  |
| 56 | B065513 | Rev-TransNat0    | Number of endofunctions of [n] with a cycle a->b->c->a and for all x i  |
| 57 | B100536 | Inv:Rev-PolyRow3 | a(n) = 3*n^2 - 2                                                        |
| 58 | B366151 | Alt-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1  |

With much better navigation and the missing sequences:
    https://luschny.de/math/oeis/Abel.html
'''
