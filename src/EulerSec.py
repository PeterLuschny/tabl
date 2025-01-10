from functools import cache
from Binomial import binomial
from _tabltypes import MakeTriangle

"""Euler secant polynomials.

[0] [   1]
[1] [   0,     1]
[2] [  -1,     0,     1]
[3] [   0,    -3,     0,   1]
[4] [   5,     0,    -6,   0,   1]
[5] [   0,    25,     0, -10,   0,   1]
[6] [ -61,     0,    75,   0, -15,   0,   1]
[7] [   0,  -427,     0, 175,   0, -21,   0,  1]
[8] [1385,     0, -1708,   0, 350,   0, -28,  0,  1]
"""


@cache
def eulersec(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = binomial(n)
    row = [b[k] * eulersec(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 0:
        row[0] = -sum(row[2::2])
    return row


@MakeTriangle(eulersec, "EulerSec", ["A119879", "A081658", "A153641"], True)
def EulerSec(n: int, k: int) -> int:
    return eulersec(n)[k]


def eulerS(n: int) -> int:
    return 0 if n % 2 == 1 else eulersec(n)[0]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerSec, short=True)

    print("Bonus:")
    print([eulerS(n) for n in range(30)])

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials

''' OEIS

The traits of the EulerSec triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-EvenSum      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Inv-ColLeft      | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A000079 | Inv-RowSum       | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000384 | Inv-DiagCol2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 8   | A000447 | Inv-DiagCol3     | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3               |
| 9   | A000810 | Rev-PolyCol3     | Expansion of e.g.f. (sin x + cos x)/cos 3x                                     |
| 10  | A001448 | Inv-CentralE     | a(n) = binomial(4n,2n) or (4*n)!/((2*n)!*(2*n)!)                               |
| 11  | A001519 | Inv-DiagSum      | a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1                      |
| 12  | A001586 | Std-PosHalf      | Generalized Euler numbers, or Springer numbers                                 |
| 13  | A002458 | Inv:Rev-CentralO | a(n) = binomial(4*n+1, 2*n)                                                    |
| 14  | A002522 | Inv-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 15  | A003665 | Inv:Rev-PolyCol3 | a(n) = 2^(n-1)*( 2^n + (-1)^n )                                                |
| 16  | A003701 | Std-AbsSum       | Expansion of e.g.f. exp(x)/cos(x)                                              |
| 17  | A005252 | Inv:Rev-DiagSum  | a(n) = Sum_{k=0..floor(n/4)} binomial(n-2k,2k)                                 |
| 18  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 19  | A007051 | Inv-PolyCol2     | a(n) = (3^n + 1)/2                                                             |
| 20  | A007582 | Inv-PolyCol3     | a(n) = 2^(n-1)*(1+2^n)                                                         |
| 21  | A009006 | Std-RowSum       | Expansion of e.g.f.: 1 + tan(x)                                                |
| 22  | A009725 | Std-AccRevSum    | Expansion of e.g.f.: tan(x)*(1+x)                                              |
| 23  | A009843 | Std-DiagCol1     | E.g.f. x/cos(x) (odd powers only)                                              |
| 24  | A046717 | Inv-PosHalf      | a(n) = 2*a(n-1) + 3*a(n-2), a(0) = a(1) = 1                                    |
| 25  | A056107 | Inv:Rev-PolyRow3 | Third spoke of a hexagonal spiral                                              |
| 26  | A057711 | Inv-TransNat0    | a(0)=0, a(1)=1, a(n) = n*2^(n-2) for n >= 2                                    |
| 27  | A058794 | Std-PolyRow3     | Row 3 of A007754                                                               |
| 28  | A062024 | Inv-PolyDiag     | a(n) = ((n+1)^n + (n-1)^n)/2                                                   |
| 29  | A079908 | Inv-PolyRow3     | Solution to the Dancing School Problem with 3 girls and n+3 boys: f(3,n)       |
| 30  | A080663 | Rev-PolyRow3     | a(n) = 3*n^2 - 1                                                               |
| 31  | A080929 | Inv-TransSqrs    | Sequence associated with a(n) = 2*a(n-1) + k*(k+2)*a(n-2)                      |
| 32  | A081658 | Std-Rev          | Triangle read by rows: T(n, k) = (-2)^k*binomial(n, k)*Euler(k, 1/2)           |
| 33  | A087447 | Inv-AccSum       | a(0) = a(1) = 1; for n > 1, a(n) = (n+2)*2^(n-2)                               |
| 34  | A100033 | Inv-CentralO     | Bisection of A001700                                                           |
| 35  | A103424 | Inv-EvenSum      | Expansion of e.g.f.: 1 + sinh(2*x)                                             |
| 36  | A109573 | Std-TransNat0    | E.g.f.: 2*x/(1+exp(-2*x))                                                      |
| 37  | A119358 | Inv-BinConv      | Number of n-element subsets of [2n] having an even sum                         |
| 38  | A119467 | Std-Inv          | A masked Pascal triangle                                                       |
| 39  | A119879 | Std-Triangle     | Exponential Riordan array (sech(x),x)                                          |
| 40  | A119880 | Std-PolyCol2     | Expansion of e.g.f. exp(2x)*sech(x)                                            |
| 41  | A119881 | Std-PolyCol3     | Expansion of e.g.f. exp(3*x)*sech(x)                                           |
| 42  | A122045 | Std-ColLeft      | Euler (or secant) numbers E(n)                                                 |
| 43  | A141665 | Std-RevInv       | A signed half of Pascal's triangle A007318: p(x,n) = (1+I*x)^n; t(n,m) = real  |
| 44  | A155457 | Std-RowGcd       | a(n) = exp(Lambda(n)), where Lambda(n) is the von Mangoldt function for odd (! |
| 45  | A193356 | Inv-DiagCol1     | If n is even then 0, otherwise n                                               |
| 46  | A199572 | Inv-OddSum       | Number of round trips of length n on the cycle graph C_2 from any of the two v |
| 47  | A214282 | Inv-RowMax       | Largest Euler characteristic of a downset on an n-dimensional cube             |
| 48  | A214445 | Std-CentralE     | a(n) = Euler(2*n)*binomial(4*n,2*n)                                            |
| 49  | A247498 | Std-Poly         | Generalized Euler numbers: Square array read by descending antidiagonals, T(n, |
| 50  | A302585 | Std-PolyDiag     | a(n) = n! * [x^n] exp(n*x)/cosh(x)                                             |
| 51  | A345632 | Inv:Rev-PolyDiag | Sum of terms of even index in the binomial decomposition of n^(n-1)            |
| 52  | A378063 | Rev-PolyDiag     | a(n) = (-2*n)^n * Euler(n, (n - 1)/(2*n)) for n >= 1, and a(0) = 1. Main diago |

* Statistic about EulerSec:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 52.
	all      A-numbers  : 137.
	missing  sequences  : 66.

[('missing', 66), ('A009006', 9), ('A000079', 7), ('A087447', 6), ('A000012', 6), ('A009725', 5), ('A001586', 5), ('A000217', 5), ('A119880', 4), ('A119467', 4), ('A119358', 4), ('A081658', 4), ('A214445', 3), ('A155457', 3), ('A141665', 3), ('A122045', 3), ('A119879', 3), ('A046717', 3), ('A009843', 3), ('A007051', 3), ('A005563', 3), ('A003701', 3), ('A000027', 3), ('A302585', 2), ('A247498', 2), ('A214282', 2), ('A193356', 2), ('A119881', 2), ('A109573', 2), ('A080929', 2), ('A058794', 2), ('A057711', 2), ('A002522', 2), ('A001448', 2), ('A000447', 2), ('A000384', 2), ('A000035', 2), ('A000007', 2), ('A378063', 1), ('A345632', 1), ('A199572', 1), ('A103424', 1), ('A100033', 1), ('A080663', 1), ('A079908', 1), ('A062024', 1), ('A056107', 1), ('A007582', 1), ('A005252', 1), ('A003665', 1), ('A002458', 1), ('A001519', 1), ('A000810', 1)]

A related webpage is: https://peterluschny.github.io/tabl/EulerSec.html .
2025/01/10

'''
