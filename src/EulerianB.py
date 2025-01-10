from functools import cache
from _tabltypes import MakeTriangle

"""EulerianB triangle.


[0] [1]
[1] [1,    1]
[2] [1,    6,     1]
[3] [1,   23,    23,      1]
[4] [1,   76,   230,     76,      1]
[5] [1,  237,  1682,   1682,    237,     1]
[6] [1,  722, 10543,  23548,  10543,   722,    1]
[7] [1, 2179, 60657, 259723, 259723, 60657, 2179,  1]
"""


@cache
def eulerianb(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = eulerianb(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


@MakeTriangle(eulerianb, "EulerianB", ["A060187", "A138076"], True)
def EulerianB(n: int, k: int) -> int:
    return eulerianb(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(EulerianB)

''' OEIS

The traits of the EulerianB triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-RowSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000165 | Std-RowSum       | Double factorial of even numbers: (2n)!! = 2^n*n!                              |
| 5   | A002436 | Std-AltSum       | E.g.f.: Sum_{n >= 0} a(n)*x^(2*n)/(2*n)! = sec(2*x)                            |
| 6   | A014479 | Std-TransNat0    | Exponential generating function = (1+2*x)/(1-2*x)^3                            |
| 7   | A028884 | Std-PolyRow2     | a(n) = (n + 3)^2 - 8                                                           |
| 8   | A060187 | Std-Triangle     | Triangle read by rows: Eulerian numbers of type B, T(n,k) (1 <= k <= n) given  |
| 9   | A060188 | Std-DiagRow1     | A column and  diagonal of A060187                                              |
| 10  | A060189 | Std-DiagRow2     | A column and diagonal of A060187 (k=3)                                         |
| 11  | A060190 | Std-DiagRow3     | A column and diagonal of A060187 (k=4)                                         |
| 12  | A080253 | Std-PosHalf      | a(n) is the number of elements in the Coxeter complex of type B_n (or C_n)     |
| 13  | A135705 | Inv:Rev-PolyRow2 | a(n) = 10*binomial(n,2) + 9*n                                                  |
| 14  | A154420 | Std-RowMax       | Maximal coefficient of MacMahon polynomial (cf. A060187) p(x,n)=2^n*(1 - x)^(n |
| 15  | A171273 | Std-Inv          | Matrix inverse of the MacMahon numbers A060187 by way of recursive calculation |
| 16  | A177043 | Std-CentralE     | Central MacMahon numbers: a(n)=A060187(2*n+1, n+1)                             |
| 17  | A178118 | Std-DiagSum      | Antidiagonal sums of the triangle A060187                                      |
| 18  | A187735 | Std-AccSum       | G.f.: Sum_{n>=0} (2*n+1)^n * x^n / (1 + (2*n+1)*x)^n                           |

* Statistic about EulerianB:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 18.
	all      A-numbers  : 60.
	missing  sequences  : 115.

[('missing', 115), ('A000012', 7), ('A060188', 6), ('A060187', 6), ('A171273', 5), ('A154420', 4), ('A060190', 4), ('A060189', 4), ('A000165', 4), ('A000027', 4), ('A187735', 3), ('A080253', 3), ('A177043', 2), ('A002436', 2), ('A000007', 2), ('A178118', 1), ('A135705', 1), ('A028884', 1), ('A014479', 1)]

A related webpage is: https://peterluschny.github.io/tabl/EulerianB.html .
2025/01/10

'''
