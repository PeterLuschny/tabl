from functools import cache
from _tabltypes import MakeTriangle

"""Euler triangle.

[0]     1
[1]    -1      1
[2]     1     -2      1
[3]    -2      3     -3      1
[4]     5     -8      6     -4      1
[5]   -16     25    -20     10     -5     1
[6]    61    -96     75    -40     15    -6     1
[7]  -272    427   -336    175    -70    21    -7    1
[8]  1385  -2176   1708   -896    350  -112    28   -8   1
[9] -7936  12465  -9792   5124  -2016   630  -168   36  -9   1
"""


@cache
def euler(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = euler(n - 1) + [1]
    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * n) // (k)
    row[0] = -sum((-1) ** (j // 2) * row[j] for j in range(n, 0, -2))

    return row


@MakeTriangle(euler, "Euler", ["A247453", "A109449"], True)
def Euler(n: int, k: int) -> int:
    return euler(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Euler)

# See also: https://oeis.org/wiki/User:Peter_Luschny/SwissKnifePolynomials

''' OEIS

The traits of the Euler triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000111 | Std-ColLeft      | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the nu |
| 4   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 5   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 6   | A000667 | Std-AltSum       | Boustrophedon transform of all-1's sequence                                    |
| 7   | A000737 | Alt-AccRevSum    | Boustrophedon transform of natural numbers, cf. A000027                        |
| 8   | A000752 | Alt-PolyCol2     | Boustrophedon transform of powers of 2                                         |
| 9   | A000834 | Std-NegHalf      | Expansion of exp(x)*(1 + tan(x))/(1 - tan(x))                                  |
| 10  | A001093 | Alt-PolyRow3     | a(n) = n^3 + 1                                                                 |
| 11  | A003701 | Rev-EvenSum      | Expansion of e.g.f. exp(x)/cos(x)                                              |
| 12  | A005898 | Rev-PolyRow3     | Centered cube numbers: n^3 + (n+1)^3                                           |
| 13  | A007290 | Std-DiagRow3     | a(n) = 2*binomial(n,3)                                                         |
| 14  | A009739 | Rev-OddSum       | E.g.f. tan(x)*exp(x)                                                           |
| 15  | A062161 | Std-OddSum       | Boustrophedon transform of n mod 2                                             |
| 16  | A062162 | Std-RowSum       | Boustrophedon transform of (-1)^n                                              |
| 17  | A062272 | Std-EvenSum      | Boustrophedon transform of (n+1) mod 2                                         |
| 18  | A065619 | Std-RowMax       | Expansion of e.g.f. x * (tan(x) + sec(x))                                      |
| 19  | A068601 | Std-PolyRow3     | a(n) = n^3 - 1                                                                 |
| 20  | A102590 | Std-PolyCol2     | Inverse Boustrophedon transform of 2^n                                         |
| 21  | A109449 | Std-Triangle     | Triangle read by rows, T(n,k) = binomial(n,k)*A000111(n-k), 0 <= k <= n        |
| 22  | A162171 | Std-DiagCol2     | Third column of A162170                                                        |
| 23  | A231179 | Alt-TransNat0    | Boustrophedon transform of nonnegative integers, cf. A001477                   |
| 24  | A292976 | Alt-PolyDiag     | a(n) = n! * [x^n] exp(n*x)*(sec(x) + tan(x))                                   |
| 25  | A307878 | Alt-PolyCol3     | Expansion of e.g.f. exp(3*x)*(sec(x) + tan(x))                                 |
| 26  | A337443 | Std-AccRevSum    | E.g.f.: (1 + x) * exp(x) / (sec(x) + tan(x))                                   |
| 27  | A343843 | Std-PosHalf      | a(n) = Sum_{k=0..n} (-1)^k*binomial(n, k)*A000831(k)                           |
| 28  | A343845 | Std-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} A109449(n-k, k)                                   |
| 29  | A343846 | Std-CentralE     | a(n) = binomial(2*n, n)*2^n*|Euler(n, 1/2) - Euler(n, 0)|                      |
| 30  | A363394 | Std-Rev          | Triangle read by rows. T(n, k) = A081658(n, k) + A363393(n, k) for k > 0 and T |

* Statistic about Euler:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 30.
	all      A-numbers  : 134.
	missing  sequences  : 81.

[('missing', 81), ('A065619', 10), ('A000667', 10), ('A000027', 10), ('A000012', 9), ('A363394', 7), ('A109449', 7), ('A343846', 5), ('A162171', 5), ('A062162', 5), ('A007290', 5), ('A000737', 5), ('A000290', 5), ('A000217', 5), ('A000111', 5), ('A343843', 4), ('A000834', 4), ('A000752', 4), ('A337443', 3), ('A102590', 3), ('A062272', 3), ('A062161', 3), ('A343845', 2), ('A307878', 2), ('A292976', 2), ('A231179', 2), ('A009739', 2), ('A005898', 2), ('A003701', 2), ('A001093', 2), ('A068601', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Euler.html .
2025/01/10

'''
