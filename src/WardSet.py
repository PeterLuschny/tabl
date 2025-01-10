from functools import cache
from _tabltypes import MakeTriangle

"""Ward set numbers.


[0] [1]
[1] [0, 1]
[2] [0, 1,   3]
[3] [0, 1,  10,    15]
[4] [0, 1,  25,   105,    105]
[5] [0, 1,  56,   490,   1260,     945]
[6] [0, 1, 119,  1918,   9450,   17325,   10395]
[7] [0, 1, 246,  6825,  56980,  190575,  270270,  135135]
[8] [0, 1, 501, 22935, 302995, 1636635, 4099095, 4729725, 2027025]
"""


@cache
def wardset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = wardset(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]

    return row


@MakeTriangle(wardset, "WardSet", ["A269939", "A134991"], False)
def WardSet(n: int, k: int) -> int:
    return wardset(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(WardSet)

''' OEIS

The traits of the WardSet triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-AltSum       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000247 | Std-DiagCol2     | a(n) = 2^n - n - 2                                                             |
| 6   | A000296 | Std-DiagSum      | Set partitions without singletons: number of partitions of an n-set into block |
| 7   | A000311 | Std-RowSum       | Schroeder's fourth problem; also series-reduced rooted trees with n labeled le |
| 8   | A000457 | Std-DiagRow1     | Exponential generating function: (1+3*x)/(1-2*x)^(7/2)                         |
| 9   | A000478 | Std-DiagCol3     | Number of ways of placing n labeled balls into 3 indistinguishable boxes with  |
| 10  | A000497 | Std-DiagRow2     | S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the second kind  |
| 11  | A000504 | Std-DiagRow3     | S2(j,2j+3) where S2(n,k) is a 2-associated Stirling number of the second kind  |
| 12  | A000587 | Alt-DiagSum      | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 |
| 13  | A001147 | Std-ColRight     | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 14  | A001662 | Std-NegHalf      | Coefficients of Airey's converging factor                                      |
| 15  | A001705 | Alt-TransNat0    | Generalized Stirling numbers: a(n) = n! * Sum_{k=0..n-1} (k+1)/(n-k)           |
| 16  | A049450 | Alt-PolyRow2     | Pentagonal numbers multiplied by 2: a(n) = n*(3*n-1)                           |
| 17  | A049451 | Std-PolyRow2     | Twice second pentagonal numbers                                                |
| 18  | A110560 | Std-RowGcd       | Numerators of T(n+1)/n! reduced to lowest terms, where T(n) are the triangular |
| 19  | A112487 | Alt-PolyCol2     | a(n) = Sum_{k=0..n} E2(n, k)*2^k, where E2(n, k) are the second-order Eulerian |
| 20  | A121555 | Alt-AccRevSum    | Number of 1-cell columns in all deco polyominoes of height n                   |
| 21  | A137375 | Std-AntiDiag     | Triangle read by rows, T(n,k) = (-1)^k*{{n,k}} where {{n,k}} are the second-or |
| 22  | A201465 | Std-PolyCol2     | E.g.f. satisfies: A(x) = (x + 2*exp(A(x)) - 2)/3                               |
| 23  | A201466 | Std-PolyCol3     | E.g.f. satisfies: A(x) = (x + 3*exp(A(x)) - 3)/4                               |
| 24  | A269939 | Std-Triangle     | Triangle read by rows, Ward numbers T(n, k) = Sum_{m=0..k} (-1)^(m + k) * bino |
| 25  | A323618 | Alt-AccSum       | Expansion of e.g.f. (1 + x)*log(1 + x)*(2 + log(1 + x))/2                      |

* Statistic about WardSet:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 25.
	all      A-numbers  : 59.
	missing  sequences  : 66.

[('missing', 66), ('A000311', 6), ('A000012', 4), ('A110560', 3), ('A001147', 3), ('A000504', 3), ('A000497', 3), ('A000478', 3), ('A000457', 3), ('A000247', 3), ('A000142', 3), ('A000027', 3), ('A000007', 3), ('A269939', 2), ('A201465', 2), ('A137375', 2), ('A121555', 2), ('A112487', 2), ('A001662', 2), ('A323618', 1), ('A201466', 1), ('A049451', 1), ('A049450', 1), ('A001705', 1), ('A000587', 1), ('A000296', 1)]

A related webpage is: https://peterluschny.github.io/tabl/WardSet.html .
2025/01/10

'''
