from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Chebyshev U(n, x) polynomials.


[0]  1;
[1]  0,  2;
[2] -1,  0,   4;
[3]  0, -4,   0,    8;
[4]  1,  0, -12,    0,  16;
[5]  0,  6,   0,  -32,   0,   32;
[6] -1,  0,  24,    0, -80,    0,   64;
[7]  0, -8,   0,   80,   0, -192,    0,   128;
[8]  1,  0, -40,    0, 240,    0, -448,     0, 256;
[9]  0, 10,   0, -160,   0,  672,    0, -1024,   0,  512;
"""


@cache
def chebyshevu(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]

    rov = chebyshevu(n - 2)
    row = [0] + chebyshevu(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@MakeTriangle(chebyshevu, "ChebyshevU", ["A053117", "A053118", "A115322"], True)
def ChebyshevU(n: int, k: int) -> int:
    return chebyshevu(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(ChebyshevU)

''' OEIS

The traits of the ChebyshevU triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000027 | Std-RowSum       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 2   | A000035 | Std-DiagSum      | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 3   | A000079 | Std-ColRight     | Powers of 2: a(n) = 2^n                                                        |
| 4   | A000129 | Std-AbsSum       | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 5   | A000466 | Std-PolyRow2     | a(n) = 4*n^2 - 1                                                               |
| 6   | A001109 | Std-PolyCol3     | a(n)^2 is a triangular number: a(n) = 6*a(n-1) - a(n-2) with a(0)=0, a(1)=1    |
| 7   | A001353 | Std-PolyCol2     | a(n) = 4*a(n-1) - a(n-2) with a(0) = 0, a(1) = 1                               |
| 8   | A001787 | Std-DiagRow2     | a(n) = n*2^(n-1)                                                               |
| 9   | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 10  | A006527 | Std-AccRevSum    | a(n) = (n^3 + 2*n)/3                                                           |
| 11  | A006588 | Std-CentralE     | a(n) = 4^n*(3*n)!/((2*n)!*n!)                                                  |
| 12  | A007290 | Std-TransNat0    | a(n) = 2*binomial(n,3)                                                         |
| 13  | A008937 | Rev-DiagSum      | a(n) = Sum_{k=0..n} T(k) where T(n) are the tribonacci numbers A000073         |
| 14  | A025170 | Rev-PolyCol3     | Expansion of g.f.: 1/(1 + 2*x + 9*x^2)                                         |
| 15  | A028347 | Rev-PolyRow2     | a(n) = n^2 - 4                                                                 |
| 16  | A046092 | Std-DiagCol2     | 4 times triangular numbers: a(n) = 2*n*(n+1)                                   |
| 17  | A053118 | Std-Rev          | Triangle of coefficients of Chebyshev's U(n,x) polynomials (exponents in decre |
| 18  | A055642 | Rev-PolyRow1     | Number of digits in the decimal expansion of n                                 |
| 19  | A088138 | Std-PosHalf      | Generalized Gaussian Fibonacci integers                                        |
| 20  | A115322 | Std-Triangle     | Triangle of coefficients of Pell polynomials                                   |
| 21  | A130809 | Std-DiagCol3     | If X_1, ..., X_n is a partition of a 2n-set X into 2-blocks then a(n) is equal |
| 22  | A144138 | Std-PolyRow3     | Chebyshev polynomial of the second kind U(3,n)                                 |
| 23  | A193356 | Std-EvenSum      | If n is even then 0, otherwise n                                               |
| 24  | A228161 | Std-Poly         | Number triangle associated to Chebyshev polynomials of the second kind         |
| 25  | A237420 | Std-OddSum       | If n is odd, then a(n) = 0; otherwise, a(n) = n                                |
| 26  | A254006 | Alt-DiagSum      | a(0) = 1, a(n) = 3*a(n-2) if n mod 2 = 0, otherwise a(n) = 0                   |
| 27  | A323118 | Std-PolyDiag     | a(n) = U_{n}(n) where U_{n}(x) is a Chebyshev polynomial of the second kind    |

* Statistic about ChebyshevU:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 27.
	all      A-numbers  : 72.
	missing  sequences  : 43.

[('missing', 43), ('A000027', 7), ('A237420', 5), ('A088138', 5), ('A006527', 5), ('A001353', 4), ('A130809', 3), ('A053118', 3), ('A046092', 3), ('A007290', 3), ('A006588', 3), ('A001787', 3), ('A000129', 3), ('A000079', 3), ('A323118', 2), ('A228161', 2), ('A193356', 2), ('A144138', 2), ('A115322', 2), ('A005843', 2), ('A001109', 2), ('A000466', 2), ('A254006', 1), ('A055642', 1), ('A028347', 1), ('A025170', 1), ('A008937', 1), ('A000035', 1)]

A related webpage is: https://peterluschny.github.io/tabl/ChebyshevU.html .
2025/01/10

'''
