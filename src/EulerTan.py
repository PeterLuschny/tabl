from functools import cache
from Binomial import binomial
from _tabltypes import MakeTriangle

"""Euler tangent polynomials.

[0]    0;
[1]    1,     0;
[2]    0,     2,     0;
[3]   -2,     0,     3,   0;
[4]    0,    -8,     0,   4,    0;
[5]   16,     0,   -20,   0,    5,    0;
[6]    0,    96,     0, -40,    0,    6,    0;
[7] -272,     0,   336,   0,  -70,    0,    7,  0;
[8]    0, -2176,     0, 896,    0, -112,    0,  8,  0;
[9] 7936,     0, -9792,   0, 2016,    0, -168,  0,  9,  0;
"""


@cache
def eulertan(n: int) -> list[int]:
    b = binomial(n)
    row = [b[k] * eulertan(n - k)[0] if k > 0 else 0 for k in range(n + 1)]
    if n % 2 == 1:
        row[0] = -sum(row[2::2]) + 1

    return row


@MakeTriangle(
    eulertan, "EulerTan", ["A162660", "A350972", "A155585", "A009006", "A000182"], False
)
def EulerTan(n: int, k: int) -> int:
    return eulertan(n)[k]


def eulerT(n: int) -> int:
    return 0 if n % 2 == 0 else eulertan(n)[0]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerTan, short=True)

    print("Bonus:")
    print([eulerT(n) for n in range(30)])


# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials

''' OEIS

The traits of the EulerTan triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000035 | Std-EvenSum      | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 4   | A005843 | Std-PolyRow2     | The nonnegative even numbers: a(n) = 2n                                        |
| 5   | A006519 | Std-RowGcd       | Highest power of 2 dividing n                                                  |
| 6   | A007290 | Std-DiagRow3     | a(n) = 2*binomial(n,3)                                                         |
| 7   | A009006 | Std-ColLeft      | Expansion of e.g.f.: 1 + tan(x)                                                |
| 8   | A009739 | Std-AbsSum       | E.g.f. tan(x)*exp(x)                                                           |
| 9   | A009744 | Std-OddSum       | Expansion of e.g.f. tan(x)*sin(x) (even powers only)                           |
| 10  | A009832 | Std-RowSum       | Expansion of e.g.f. tanh(x)*exp(x)                                             |
| 11  | A100536 | Std-PolyRow3     | a(n) = 3*n^2 - 2                                                               |
| 12  | A109573 | Std-DiagCol1     | E.g.f.: 2*x/(1+exp(-2*x))                                                      |
| 13  | A162660 | Std-Triangle     | Triangle read by rows: coefficients of the complementary Swiss-Knife polynomia |
| 14  | A214447 | Std-CentralE     | (-2)^n * Euler_polynomial(n,1) * binomial(2*n,n)                               |
| 15  | A302587 | Std-PolyDiag     | a(n) = n! * [x^n] exp(n*x)*tanh(x)                                             |
| 16  | A326325 | Std-PosHalf      | a(n) = 2^n*n!*([z^n] exp(x*z)*tanh(z))(1/2)                                    |

* Statistic about EulerTan:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 16.
	all      A-numbers  : 49.
	missing  sequences  : 69.

[('missing', 69), ('A009832', 7), ('A326325', 5), ('A000027', 4), ('A214447', 3), ('A109573', 3), ('A009739', 3), ('A009006', 3), ('A007290', 3), ('A006519', 3), ('A005843', 3), ('A302587', 2), ('A162660', 2), ('A100536', 2), ('A009744', 2), ('A000035', 2), ('A000012', 2)]

A related webpage is: https://peterluschny.github.io/tabl/EulerTan.html .
2025/01/10

'''
