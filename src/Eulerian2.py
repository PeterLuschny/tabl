from functools import cache
from _tabltypes import MakeTriangle

"""Eulerian2 triangle.

[0] 1;
[1] 0, 1;
[2] 0, 1,   2;
[3] 0, 1,   8,     6;
[4] 0, 1,  22,    58,     24;
[5] 0, 1,  52,   328,    444,    120;
[6] 0, 1, 114,  1452,   4400,   3708,    720;
[7] 0, 1, 240,  5610,  32120,  58140,  33984,  5040;
[8] 0, 1, 494, 19950, 195800, 644020, 785304, 341136, 40320;
"""


@cache
def eulerian2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = eulerian2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row


@MakeTriangle(
    eulerian2, "Eulerian2", ["A340556", "A008517", "A112007", "A163936"], False
)
def Eulerian2(n: int, k: int) -> int:
    return eulerian2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Eulerian2)

# See also http://luschny.de/math/oeis/A340556.html

''' OEIS

The traits of the Eulerian2 triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-ColRight     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000311 | Std-PosHalf      | Schroeder's fourth problem; also series-reduced rooted trees with n labeled le |
| 6   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 7   | A000457 | Rev-TransNat0    | Exponential generating function: (1+3*x)/(1-2*x)^(7/2)                         |
| 8   | A001147 | Std-RowSum       | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 9   | A001662 | Std-AltSum       | Coefficients of Airey's converging factor                                      |
| 10  | A002538 | Std-DiagRow1     | Second-order Eulerian numbers <<n+1,n-1>>                                      |
| 11  | A002539 | Std-DiagRow2     | Eulerian numbers of the second kind: <<n+3, n>>                                |
| 12  | A004301 | Std-DiagCol3     | Second-order Eulerian numbers <<n,2>>                                          |
| 13  | A005803 | Std-DiagCol2     | Second-order Eulerian numbers: a(n) = 2^n - 2*n                                |
| 14  | A007347 | Std-RowMax       | Maximal Eulerian numbers of second kind                                        |
| 15  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 16  | A051577 | Std-TransNat0    | a(n) = (2*n + 3)!!/3 = A001147(n+2)/3                                          |
| 17  | A112008 | Std-DiagRow3     | Fourth diagonal of second-order Eulerian triangle A008517. Fourth column (m=3) |
| 18  | A112487 | Std-PolyCol2     | a(n) = Sum_{k=0..n} E2(n, k)*2^k, where E2(n, k) are the second-order Eulerian |
| 19  | A163936 | Std-Rev          | Triangle related to the o.g.f.s. of the right-hand columns of A130534 (E(x,m=1 |
| 20  | A201637 | Std-Triangle     | Triangle of second-order Eulerian numbers T(n,k) (n>=0, 0 <= k <= n) read by r |
| 21  | A261898 | Std-AccSum       | Values of |G-hat_1(n)|, a sum involving Stirling numbers of the second kind    |
| 22  | A341106 | Std-NegHalf      | a(n) = 2^n*E2poly(n, -1/2), where E2poly(n, x) = Sum_{k=0..n} A340556(n, k)*x^ |
| 23  | A367369 | Std-CentralE     | a(n) = A340556(2*n, n), the central terms of the second order Eulerian numbers |

* Statistic about Eulerian2:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 23.
	all      A-numbers  : 62.
	missing  sequences  : 63.

[('missing', 63), ('A001147', 6), ('A000012', 4), ('A367369', 3), ('A261898', 3), ('A163936', 3), ('A112008', 3), ('A007347', 3), ('A005803', 3), ('A004301', 3), ('A002539', 3), ('A002538', 3), ('A001662', 3), ('A000311', 3), ('A000142', 3), ('A000027', 3), ('A000007', 3), ('A341106', 2), ('A201637', 2), ('A112487', 2), ('A051577', 1), ('A014105', 1), ('A000457', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Eulerian2.html .
2025/01/10

'''
