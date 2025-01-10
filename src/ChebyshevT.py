from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Chebyshev T(n, x) polynomials.

[0]   1;
[1]   0,  1;
[2]  -1,  0,   2;
[3]   0, -3,   0,    4;
[4]   1,  0,  -8,    0,    8;
[5]   0,  5,   0,  -20,    0,    16;
[6]  -1,  0,  18,    0,  -48,     0    32;
[7]   0, -7,   0,   56,    0,  -112     0,   64;
[8]   1,  0, -32,    0,  160,     0  -256,    0,  128;
[9]   0,  9,   0, -120,    0,   432     0, -576,    0,  256;
"""


@cache
def chebyshevt(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov = chebyshevt(n - 2)
    row = [0] + chebyshevt(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


@MakeTriangle(chebyshevt, "ChebyshevT", ["A053120", "A039991", "A081265"], True)
def ChebyshevT(n: int, k: int) -> int:
    return chebyshevt(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(ChebyshevT)

''' OEIS

The traits of the ChebyshevT triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-DiagSum      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowSum       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Std-EvenSum      | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A000073 | Rev-DiagSum      | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with a(0) = a(1 |
| 6   | A000079 | Std-ColRight     | Powers of 2: a(n) = 2^n                                                        |
| 7   | A000290 | Std-TransNat0    | The squares: a(n) = n^2                                                        |
| 8   | A001075 | Std-PolyCol2     | a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - a(n-2)                                   |
| 9   | A001105 | Std-DiagCol2     | a(n) = 2*n^2                                                                   |
| 10  | A001333 | Std-AbsSum       | Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)    |
| 11  | A001541 | Std-PolyCol3     | a(0) = 1, a(1) = 3; for n > 1, a(n) = 6*a(n-1) - a(n-2)                        |
| 12  | A001792 | Std-DiagRow2     | a(n) = (n+2)*2^(n-1)                                                           |
| 13  | A002378 | Rev-TransNat0    | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 14  | A002492 | Std-DiagCol3     | Sum of the first n even squares: 2*n*(n+1)*(2*n+1)/3                           |
| 15  | A002522 | Std-AccRevSum    | a(n) = n^2 + 1                                                                 |
| 16  | A008776 | Alt-DiagSum      | Pisot sequences E(2,6), L(2,6), P(2,6), T(2,6)                                 |
| 17  | A008865 | Rev-PolyRow2     | a(n) = n^2 - 2                                                                 |
| 18  | A014820 | Std-TransSqrs    | a(n) = (1/3)*(n^2 + 2*n + 3)*(n+1)^2                                           |
| 19  | A025172 | Rev-PolyCol3     | Let phi = arccos(1/3), the dihedral angle of the regular tetrahedron. Then cos |
| 20  | A028387 | Std-AccSum       | a(n) = n + (n+1)^2                                                             |
| 21  | A036909 | Std-CentralE     | a(n) = (2/3) * 4^n * binomial(3*n, n)                                          |
| 22  | A053120 | Std-Triangle     | Triangle of coefficients of Chebyshev's T(n,x) polynomials (powers of x in inc |
| 23  | A056220 | Std-PolyRow2     | a(n) = 2*n^2 - 1                                                               |
| 24  | A081265 | Std-Rev          | Triangle of coefficients of the polynomials a(n, x) = 2*a(n-1, x)+ x^2*a(n-2,x |
| 25  | A101124 | Std-Poly         | Number triangle associated to Chebyshev polynomials of first kind              |
| 26  | A115066 | Std-PolyDiag     | Chebyshev polynomial of the first kind T(n,x), evaluated at x=n                |
| 27  | A138230 | Alt-PosHalf      | Expansion of (1-x)/(1 - 2*x + 4*x^2)                                           |
| 28  | A144129 | Std-PolyRow3     | a(n) = ChebyshevT(3, n)                                                        |
| 29  | A193356 | Std-DiagCol1     | If n is even then 0, otherwise n                                               |

* Statistic about ChebyshevT:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 29.
	all      A-numbers  : 71.
	missing  sequences  : 37.

[('missing', 37), ('A000012', 6), ('A002522', 5), ('A028387', 4), ('A001075', 4), ('A000035', 4), ('A193356', 3), ('A036909', 3), ('A002492', 3), ('A001792', 3), ('A001333', 3), ('A001105', 3), ('A000079', 3), ('A144129', 2), ('A138230', 2), ('A115066', 2), ('A101124', 2), ('A081265', 2), ('A056220', 2), ('A014820', 2), ('A001541', 2), ('A000290', 2), ('A000027', 2), ('A053120', 1), ('A025172', 1), ('A008865', 1), ('A008776', 1), ('A002378', 1), ('A000073', 1), ('A000007', 1)]

A related webpage is: https://peterluschny.github.io/tabl/ChebyshevT.html .
2025/01/10

'''
