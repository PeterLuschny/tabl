from functools import cache
from _tabltypes import MakeTriangle

"""(Physicist's) Hermite polynomials, unsigned coefficients.

[0]     1;
[1]     0,     2;
[2]     2,     0,      4;
[3]     0,    12,      0,      8;
[4]    12,     0,     48,      0,     16;
[5]     0,   120,      0,    160,      0,    32;
[6]  120,      0,    720,      0,    480,     0,     64;
[7]     0,  1680,      0,   3360,      0,  1344,      0,   128;
[8]  1680,     0,  13440,      0,  13440,     0,   3584,     0,   256;
[9]     0, 30240,      0,  80640,      0, 48384,      0,  9216,     0,  512;
"""


@cache
def hermiteh(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 2**n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))
    return row


@MakeTriangle(hermiteh, "HermiteH", ["A060821"], False)
def HermiteH(n: int, k: int) -> int:
    return hermiteh(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HermiteH)

''' OEIS

The traits of the HermiteH triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000079 | Std-ColRight     | Powers of 2: a(n) = 2^n                                                        |
| 2   | A000898 | Std-RowSum       | a(n) = 2*(a(n-1) + (n-1)*a(n-2)) for n >= 2 with a(0) = 1                      |
| 3   | A001815 | Std-DiagRow2     | a(n) = binomial(n,2) * 2^(n-1)                                                 |
| 4   | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 5   | A005899 | Std-PolyRow2     | Number of points on surface of octahedron; also coordination sequence for cubi |
| 6   | A016116 | Std-RowGcd       | a(n) = 2^floor(n/2)                                                            |
| 7   | A055642 | Rev-PolyRow1     | Number of digits in the decimal expansion of n                                 |
| 8   | A060821 | Std-Triangle     | Triangle read by rows. T(n, k) are the coefficients of the Hermite polynomial  |
| 9   | A067994 | Std-ColLeft      | Hermite numbers                                                                |
| 10  | A079949 | Std-PolyCol3     | Special values of Hermite polynomials                                          |
| 11  | A127394 | Std-PolyCol2     | Number of irreducible representations of Sp(2n,R) with same infinitesimal char |
| 12  | A255843 | Rev-PolyRow2     | a(n) = 2*n^2 + 4                                                               |
| 13  | A272261 | Alt-DiagSum      | Number of one-to-one functions f from [n] to [2n] where f(x) may not be equal  |
| 14  | A277281 | Std-RowMax       | Maximal coefficient (ignoring signs) in Hermite polynomial of order n          |

* Statistic about HermiteH:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 14.
	all      A-numbers  : 43.
	missing  sequences  : 75.

[('missing', 75), ('A000898', 10), ('A067994', 6), ('A127394', 4), ('A277281', 3), ('A016116', 3), ('A001815', 3), ('A000079', 3), ('A079949', 2), ('A060821', 2), ('A005899', 2), ('A005843', 2), ('A272261', 1), ('A255843', 1), ('A055642', 1)]

A related webpage is: https://peterluschny.github.io/tabl/HermiteH.html .
2025/01/10

'''
