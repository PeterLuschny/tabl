from functools import cache
from _tabltypes import MakeTriangle

"""FiboLucas polynomials, m = 2.
  [ 0] [1]
  [ 1] [1, 2]
  [ 2] [1, 2, 1]
  [ 3] [1, 2, 2, 2]
  [ 4] [1, 2, 3, 4, 1]
  [ 5] [1, 2, 4, 6, 3, 2]
  [ 6] [1, 2, 5, 8, 6, 6, 1]
  [ 7] [1, 2, 6, 10, 10, 12, 4, 2]
  [ 8] [1, 2, 7, 12, 15, 20, 10, 8, 1]
  [ 9] [1, 2, 8, 14, 21, 30, 20, 20, 5, 2]
  [10] [1, 2, 9, 16, 28, 42, 35, 40, 15, 10, 1]

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""

@cache
def fibolucas(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 2]
    if n == 2: return [1, 2, 1]

    rowA = fibolucas(n - 2)
    row  = fibolucas(n - 1) + [1 + n % 2]
    row[2] += 1

    for k in range(3, n):
        row[k] += rowA[k - 2]

    return row


@MakeTriangle(fibolucas, "FiboLucas", ["A374439"], True)
def FiboLucas(n: int, k: int) -> int:
    return fibolucas(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucas)

    for n in range(11): print(fibolucas(n))


''' OEIS

The traits of the FiboLucas triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagCol2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000032 | Std-RowSum       | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 4   | A000034 | Std-ColRight     | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 5   | A000045 | Std-EvenSum      | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 6   | A000129 | Std-NegHalf      | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 7   | A000244 | Rev:Inv-PosHalf  | Powers of 3: a(n) = 3^n                                                        |
| 8   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 9   | A001477 | Rev:Inv-DiagRow2 | The nonnegative integers                                                       |
| 10  | A001629 | Alt-AccSum       | Self-convolution of Fibonacci numbers                                          |
| 11  | A005408 | Std-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A005843 | Std-DiagCol3     | The nonnegative even numbers: a(n) = 2n                                        |
| 13  | A006131 | Std-PolyCol2     | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 14  | A006355 | Std-OddSum       | Number of binary vectors of length n containing no singletons                  |
| 15  | A016116 | Rev-DiagSum      | a(n) = 2^floor(n/2)                                                            |
| 16  | A023607 | Rev-TransNat0    | a(n) = n * Fibonacci(n+1)                                                      |
| 17  | A029578 | Std-DiagRow1     | The natural numbers interleaved with the even numbers                          |
| 18  | A048654 | Std-PosHalf      | a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4                                       |
| 19  | A055642 | Std-DiagCol1     | Number of digits in the decimal expansion of n                                 |
| 20  | A059100 | Rev:Inv-PolyRow2 | a(n) = n^2 + 2                                                                 |
| 21  | A086990 | Rev:Inv-RowSum   | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 22  | A108300 | Rev-PolyCol3     | a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5                              |
| 23  | A124038 | Std-Rev          | Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If |
| 24  | A126982 | Rev:Inv-PolyCol2 | Expansion of 1/(1+3*x*c(x)), c(x) the g.f. of Catalan numbers A000108          |
| 25  | A131259 | Std-DiagRow2     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 26  | A133585 | Rev-EvenSum      | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 27  | A133586 | Rev-OddSum       | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 28  | A188377 | Rev-PolyRow3     | a(n) = n^3 - 4n^2 + 6n - 2                                                     |
| 29  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 30  | A374439 | Std-Triangle     | Triangle read by rows: the coefficients of the Lucas-Fibonacci polynomials. T( |
| 31  | A375025 | Std-InvRev       | Triangle read by rows: Matrix inverse of row-reversed A374439                  |
| 32  | A375026 | Rev:Inv-AltSum   | a(n) = [x^n] 2/(3*sqrt(4*x^2 + 1) + 6*x - 1). Alternating row sums of A375025  |

* Statistic about FiboLucas:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 32.
	all      A-numbers  : 80.
	missing  sequences  : 92.

[('missing', 92), ('A000032', 6), ('A000045', 5), ('A000027', 5), ('A375025', 4), ('A124038', 4), ('A055642', 4), ('A005843', 4), ('A000012', 4), ('A374439', 3), ('A297382', 3), ('A131259', 3), ('A086990', 3), ('A048654', 3), ('A029578', 3), ('A000290', 3), ('A000034', 3), ('A006355', 2), ('A006131', 2), ('A005408', 2), ('A000129', 2), ('A375026', 1), ('A188377', 1), ('A133586', 1), ('A133585', 1), ('A126982', 1), ('A108300', 1), ('A059100', 1), ('A023607', 1), ('A016116', 1), ('A001629', 1), ('A001477', 1), ('A000244', 1)]

A related webpage is: https://peterluschny.github.io/tabl/FiboLucas.html .
2025/01/10

'''
