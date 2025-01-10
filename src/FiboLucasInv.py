from functools import cache
from FiboLucas import FiboLucas
from _tabltypes import MakeTriangle

"""FiboLucasInv polynomials.

  [0] [  1]
  [1] [ -2,   1]
  [2] [  3,  -2,   1]
  [3] [ -4,   2,  -2,   1]
  [4] [  6,  -2,   1,  -2,   1]
  [5] [-10,   5,   0,   0,  -2,  1]
  [6] [ 15, -10,   5,   2,  -1, -2,  1]
  [7] [-20,  10, -12,   6,   4, -2, -2,  1]
  [8] [ 30,  -8,   4, -16,   8,  6, -3, -2,  1]
  [9] [-52,  26,   8,  -4, -22, 11,  8, -4, -2, 1]

"""

# TODO needs optimation!
@cache
def fibolucasinv(n: int) -> list[int]:
    return FiboLucas.invrev(n+1)[-1]


@MakeTriangle(fibolucasinv, "FiboLucasInv", ["A375025"], True)
def FiboLucasInv(n: int, k: int) -> int:
    return fibolucasinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucasInv, short=True)


''' OEIS

The traits of the FiboLucasInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000032 | Inv-RowSum       | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 4   | A000034 | Inv-ColLeft      | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 5   | A000045 | Inv-AltSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 6   | A000129 | Inv:Rev-NegHalf  | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 7   | A000244 | Std-PosHalf      | Powers of 3: a(n) = 3^n                                                        |
| 8   | A000290 | Inv-PolyRow2     | The squares: a(n) = n^2                                                        |
| 9   | A001477 | Std-DiagRow2     | The nonnegative integers                                                       |
| 10  | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 11  | A005843 | Std-DiagRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 12  | A006131 | Inv-PosHalf      | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 13  | A006355 | Inv:Rev-OddSum   | Number of binary vectors of length n containing no singletons                  |
| 14  | A016116 | Inv-DiagSum      | a(n) = 2^floor(n/2)                                                            |
| 15  | A023607 | Inv-TransNat0    | a(n) = n * Fibonacci(n+1)                                                      |
| 16  | A029578 | Inv-DiagCol1     | The natural numbers interleaved with the even numbers                          |
| 17  | A048654 | Inv-PolyCol2     | a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4                                       |
| 18  | A055642 | Std-DiagRow1     | Number of digits in the decimal expansion of n                                 |
| 19  | A056105 | Rev-PolyRow2     | First spoke of a hexagonal spiral                                              |
| 20  | A059100 | Std-PolyRow2     | a(n) = n^2 + 2                                                                 |
| 21  | A086990 | Std-RowSum       | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 22  | A108300 | Inv-PolyCol3     | a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5                              |
| 23  | A124038 | Std-Inv          | Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If |
| 24  | A126982 | Std-PolyCol2     | Expansion of 1/(1+3*x*c(x)), c(x) the g.f. of Catalan numbers A000108          |
| 25  | A131259 | Inv-DiagCol2     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 26  | A133585 | Inv-EvenSum      | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 27  | A133586 | Inv-OddSum       | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 28  | A188377 | Inv-PolyRow3     | a(n) = n^3 - 4n^2 + 6n - 2                                                     |
| 29  | A297382 | Inv-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 30  | A374439 | Std-RevInv       | Triangle read by rows: the coefficients of the Lucas-Fibonacci polynomials. T( |
| 31  | A375025 | Std-Triangle     | Triangle read by rows: Matrix inverse of row-reversed A374439                  |
| 32  | A375026 | Std-AltSum       | a(n) = [x^n] 2/(3*sqrt(4*x^2 + 1) + 6*x - 1). Alternating row sums of A375025  |

* Statistic about FiboLucasInv:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 32.
	all      A-numbers  : 81.
	missing  sequences  : 133.

[('missing', 133), ('A086990', 8), ('A005843', 5), ('A000027', 5), ('A124038', 4), ('A055642', 4), ('A000032', 4), ('A000012', 4), ('A375026', 3), ('A375025', 3), ('A374439', 3), ('A001477', 3), ('A000244', 3), ('A000045', 3), ('A297382', 2), ('A131259', 2), ('A126982', 2), ('A059100', 2), ('A048654', 2), ('A029578', 2), ('A006131', 2), ('A005408', 2), ('A000290', 2), ('A000034', 2), ('A188377', 1), ('A133586', 1), ('A133585', 1), ('A108300', 1), ('A056105', 1), ('A023607', 1), ('A016116', 1), ('A006355', 1), ('A000129', 1)]

A related webpage is: https://peterluschny.github.io/tabl/FiboLucasInv.html .
2025/01/10

'''
