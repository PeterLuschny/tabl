from functools import cache
from FiboLucas import fibolucas
from _tabltypes import MakeTriangle

"""FiboLucasRev polynomials, m = 2.

| [1] |
| [2, 1] |
| [1, 2, 1] |
| [2, 2, 2, 1] |
| [1, 4, 3, 2, 1] |
| [2, 3, 6, 4, 2, 1] |
| [1, 6, 6, 8, 5, 2, 1] |
| [2, 4, 12, 10, 10, 6, 2, 1] |

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""

@cache
def fibolucasrev(n: int) -> list[int]:
    if n == 0: return [1]
    return list(reversed(fibolucas(n)))


@MakeTriangle(fibolucasrev, "FiboLucasRev", ["A124038"], True)
def FiboLucasRev(n: int, k: int) -> int:
    return fibolucasrev(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucasRev)


''' OEIS

The traits of the FiboLucasRev triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000032 | Std-RowSum       | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 4   | A000034 | Std-ColLeft      | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 5   | A000045 | Std-AltSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 6   | A000129 | Alt-PolyCol2     | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 7   | A000244 | Inv-PosHalf      | Powers of 3: a(n) = 3^n                                                        |
| 8   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 9   | A001477 | Inv-DiagRow2     | The nonnegative integers                                                       |
| 10  | A001629 | Alt-AccRevSum    | Self-convolution of Fibonacci numbers                                          |
| 11  | A003688 | Alt-PolyCol3     | a(n) = 3*a(n-1) + a(n-2), with a(1)=1 and a(2)=4                               |
| 12  | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 13  | A005843 | Std-DiagRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 14  | A006131 | Std-PosHalf      | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 15  | A006355 | Rev-OddSum       | Number of binary vectors of length n containing no singletons                  |
| 16  | A016116 | Std-DiagSum      | a(n) = 2^floor(n/2)                                                            |
| 17  | A023607 | Std-TransNat0    | a(n) = n * Fibonacci(n+1)                                                      |
| 18  | A029578 | Std-DiagCol1     | The natural numbers interleaved with the even numbers                          |
| 19  | A048654 | Std-PolyCol2     | a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4                                       |
| 20  | A055642 | Std-DiagRow1     | Number of digits in the decimal expansion of n                                 |
| 21  | A056105 | Inv:Rev-PolyRow2 | First spoke of a hexagonal spiral                                              |
| 22  | A059100 | Inv-PolyRow2     | a(n) = n^2 + 2                                                                 |
| 23  | A086990 | Inv-RowSum       | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 24  | A108300 | Std-PolyCol3     | a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5                              |
| 25  | A124038 | Std-Triangle     | Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If |
| 26  | A126982 | Inv-PolyCol2     | Expansion of 1/(1+3*x*c(x)), c(x) the g.f. of Catalan numbers A000108          |
| 27  | A130706 | Alt-DiagSum      | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 28  | A131259 | Std-DiagCol2     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 29  | A133585 | Std-EvenSum      | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 30  | A133586 | Std-OddSum       | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 31  | A188377 | Std-PolyRow3     | a(n) = n^3 - 4n^2 + 6n - 2                                                     |
| 32  | A240847 | Alt-TransNat0    | a(n) = 2*a(n-1) + a(n-2) - 2*a(n-3) - a(n-4) for n>3, a(0)=a(1)=a(3)=0, a(2)=1 |
| 33  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 34  | A374439 | Std-Rev          | Triangle read by rows: the coefficients of the Lucas-Fibonacci polynomials. T( |
| 35  | A375025 | Std-Inv          | Triangle read by rows: Matrix inverse of row-reversed A374439                  |
| 36  | A375026 | Inv-AltSum       | a(n) = [x^n] 2/(3*sqrt(4*x^2 + 1) + 6*x - 1). Alternating row sums of A375025  |

* Statistic about FiboLucasRev:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 36.
	all      A-numbers  : 93.
	missing  sequences  : 121.

[('missing', 121), ('A000032', 6), ('A000027', 6), ('A086990', 5), ('A005843', 5), ('A375025', 4), ('A374439', 4), ('A055642', 4), ('A000045', 4), ('A000012', 4), ('A297382', 3), ('A131259', 3), ('A124038', 3), ('A029578', 3), ('A006131', 3), ('A000290', 3), ('A000034', 3), ('A375026', 2), ('A133586', 2), ('A133585', 2), ('A126982', 2), ('A048654', 2), ('A005408', 2), ('A001629', 2), ('A001477', 2), ('A000244', 2), ('A000129', 2), ('A240847', 1), ('A188377', 1), ('A130706', 1), ('A108300', 1), ('A059100', 1), ('A056105', 1), ('A023607', 1), ('A016116', 1), ('A006355', 1), ('A003688', 1)]

A related webpage is: https://peterluschny.github.io/tabl/FiboLucasRev.html .
2025/01/10

'''
