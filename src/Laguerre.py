from functools import cache
from _tabltypes import MakeTriangle


"""Laguerre polynomials n! * L(n, x) (unsigned coefficients).

[0]      1
[1]      1,       1
[2]      2,       4,       1
[3]      6,      18,       9,       1
[4]     24,      96,      72,      16,       1
[5]    120,     600,     600,     200,      25,      1
[6]    720,    4320,    5400,    2400,     450,     36,     1
[7]   5040,   35280,   52920,   29400,    7350,    882,    49,    1
[8]  40320,  322560,  564480,  376320,  117600,  18816,  1568,   64,  1
"""


@cache
def laguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + laguerre(n - 1)
    for k in range(0, n):
        row[k] += (n + k) * row[k + 1]
    return row


@MakeTriangle(laguerre, "Laguerre", ["A021009", "A021010", "A144084"], True)
def Laguerre(n: int, k: int) -> int:
    return laguerre(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Laguerre)

''' OEIS

The traits of the Laguerre triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000142 | Std-ColLeft      | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 4   | A000262 | Std-AccRevSum    | Number of "sets of lists": number of partitions of {1,...,n} into any number o |
| 5   | A000290 | Std-DiagRow1     | The squares: a(n) = n^2                                                        |
| 6   | A001040 | Std-DiagSum      | a(n+1) = n*a(n) + a(n-1) with a(0)=0, a(1)=1                                   |
| 7   | A001563 | Std-DiagCol1     | a(n) = n*n! = (n+1)! - n!                                                      |
| 8   | A001809 | Std-DiagCol2     | a(n) = n! * n(n-1)/4                                                           |
| 9   | A001810 | Std-DiagCol3     | a(n) = n!*n*(n-1)*(n-2)/36                                                     |
| 10  | A002720 | Std-RowSum       | Number of partial permutations of an n-set; number of n X n binary matrices wi |
| 11  | A008865 | Std-PolyRow2     | a(n) = n^2 - 2                                                                 |
| 12  | A009940 | Std-AltSum       | a(n) = n!*L_{n}(1), where L_{n}(x) is the n-th Laguerre polynomial             |
| 13  | A021009 | Std-Triangle     | Triangle of coefficients of Laguerre polynomials n!*L_n(x) (rising powers of x |
| 14  | A025166 | Std-NegHalf      | E.g.f.: -exp(-x/(1-2*x))/(1-2*x)                                               |
| 15  | A025167 | Std-PosHalf      | E.g.f: exp(x/(1-2*x))/(1-2*x)                                                  |
| 16  | A056220 | Rev-PolyRow2     | a(n) = 2*n^2 - 1                                                               |
| 17  | A058797 | Alt-DiagSum      | a(n) = n*a(n-1) - a(n-2), with a(-1) = 0, a(0) = 1                             |
| 18  | A084950 | Std-AntiDiag     | Array of coefficients of denominator polynomials of the n-th approximation of  |
| 19  | A087912 | Std-PolyCol2     | Exponential generating function is exp(2*x/(1-x))/(1-x)                        |
| 20  | A102631 | Std-RowGcd       | a(n) = n^2 / (squarefree kernel of n)                                          |
| 21  | A102757 | Rev-PolyCol3     | a(n) = Sum_{i=0..n} C(n,i)^2 * i! * 3^i                                        |
| 22  | A103194 | Std-TransNat0    | LAH transform of squares                                                       |
| 23  | A105219 | Std-TransSqrs    | a(n) = Sum_{k=0..n} C(n,k)^2*(n-k)!*k^2                                        |
| 24  | A144084 | Std-Rev          | T(n,k) is the number of partial bijections of height k (height(alpha) = |Im(al |
| 25  | A163102 | Std-DiagRow2     | a(n) = n^2*(n+1)^2/2                                                           |
| 26  | A179058 | Std-DiagRow3     | Number of non-attacking placements of 3 rooks on an n X n board                |
| 27  | A216831 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n,k)^3 * k!                                       |
| 28  | A277373 | Std-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,n-k)*n^(n-k)*n!/(n-k)!                          |
| 29  | A277382 | Std-PolyCol3     | a(n) = n!*LaguerreL(n, -3)                                                     |
| 30  | A277423 | Alt-PolyDiag     | a(n) = n!*LaguerreL(n, n)                                                      |
| 31  | A295382 | Alt-PolyCol2     | Expansion of e.g.f. exp(-2*x/(1 - x))/(1 - x)                                  |
| 32  | A295383 | Std-CentralE     | a(n) = (2*n)! * [x^(2*n)] (-x/(1 - x))^n/((1 - x)*n!)                          |
| 33  | A330260 | Rev-PolyDiag     | a(n) = n! * Sum_{k=0..n} binomial(n,k) * n^(n - k) / k!                        |
| 34  | A330497 | Inv:Rev-PolyDiag | a(n) = n! * Sum_{k=0..n} (-1)^k * binomial(n,k) * n^(n - k) / k!               |
| 35  | A331325 | Std-EvenSum      | a(n) = n!*[x^n] cosh(x/(1-x))/(1-x)                                            |
| 36  | A331326 | Std-OddSum       | a(n) = n!*[x^n] sinh(x/(1 - x))/(1 - x)                                        |
| 37  | A343580 | Std-ColMiddle    | a(n) = abs(A021009(n, floor(n/2)))                                             |
| 38  | A343840 | Std-InvBinConv   | a(n) = Sum_{k=0..n}(-1)^(n-k)*binomial(n, k)*|A021009(n, k)|                   |
| 39  | A343847 | Std-Poly         | T(n, k) = (n - k)! * [x^(n-k)] exp(k*x/(1 - x))/(1 - x). Triangle read by rows |

* Statistic about Laguerre:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 39.
	all      A-numbers  : 142.
	missing  sequences  : 73.

[('missing', 73), ('A002720', 10), ('A144084', 7), ('A021009', 7), ('A343840', 5), ('A295383', 5), ('A216831', 5), ('A179058', 5), ('A163102', 5), ('A102631', 5), ('A009940', 5), ('A001810', 5), ('A001809', 5), ('A001563', 5), ('A000290', 5), ('A000142', 5), ('A000027', 5), ('A295382', 4), ('A025167', 4), ('A025166', 4), ('A000012', 4), ('A343580', 3), ('A331326', 3), ('A331325', 3), ('A087912', 3), ('A084950', 3), ('A008865', 3), ('A000262', 3), ('A277423', 2), ('A105219', 2), ('A056220', 2), ('A001040', 2), ('A343847', 1), ('A330497', 1), ('A330260', 1), ('A277382', 1), ('A277373', 1), ('A103194', 1), ('A102757', 1), ('A058797', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Laguerre.html .
2025/01/10

'''
