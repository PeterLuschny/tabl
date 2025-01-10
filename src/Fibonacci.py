from functools import cache
from _tabltypes import MakeTriangle

"""Fibonacci-Pascal triangle.

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,  1]
[3] [ 1,  2,  2,  1]
[4] [ 2,  3,  4,  3,  1]
[5] [ 3,  5,  7,  7,  4,  1]
[6] [ 5,  8, 12, 14, 11,  5,  1]
[7] [ 8, 13, 20, 26, 25, 16,  6,  1]
[8] [13, 21, 33, 46, 51, 41, 22,  7, 1]
[9] [21, 34, 54, 79, 97, 92, 63, 29, 8, 1]
"""


@cache
def fibonacci(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = fibonacci(n - 1) + [1]
    s = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row


@MakeTriangle(fibonacci, "Fibonacci", ["A354267", "A105809", "A228074"], False)
def Fibonacci(n: int, k: int) -> int:
    return fibonacci(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Fibonacci)

''' OEIS

The traits of the Fibonacci triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000045 | Std-AltSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 4   | A000071 | Std-DiagCol2     | a(n) = Fibonacci(n) - 1                                                        |
| 5   | A000124 | Std-DiagRow2     | Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 + 1; or, max |
| 6   | A001924 | Std-DiagCol3     | Apply partial sum operator twice to Fibonacci numbers                          |
| 7   | A002061 | Std-PolyRow2     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 8   | A004006 | Std-DiagRow3     | a(n) = C(n,1) + C(n,2) + C(n,3), or n*(n^2 + 5)/6                              |
| 9   | A006367 | Std-DiagSum      | Number of binary vectors of length n+1 beginning with 0 and containing just 1  |
| 10  | A027444 | Alt-PolyRow3     | a(n) = n^3 + n^2 + n                                                           |
| 11  | A027988 | Std-RowMax       | Greatest number in row n of array T given by A027926                           |
| 12  | A039834 | Alt-AccRevSum    | a(n+2) = -a(n+1) + a(n) (signed Fibonacci numbers) with a(-2) = a(-1) = 1; or  |
| 13  | A069778 | Std-PolyRow3     | q-factorial numbers 3!_q                                                       |
| 14  | A079282 | Std-TransNat0    | Diagonal sums of triangle A055249                                              |
| 15  | A099036 | Std-RowSum       | a(n) = 2^n - Fibonacci(n)                                                      |
| 16  | A106511 | Alt-DiagSum      | Expansion of g.f. (1+x)^2/((1 + x + x^2)*(1 + x - x^2))                        |
| 17  | A108081 | Rev-CentralO     | a(n) = Sum_{i=0..n} binomial(2*n-i, n+i)                                       |
| 18  | A113312 | Alt-PolyCol2     | Expansion of (1+x)^2/(1-2x^2+x^3)                                              |
| 19  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 20  | A212804 | Alt-TransNat0    | Expansion of (1 - x)/(1 - x - x^2)                                             |
| 21  | A354267 | Std-Triangle     | A Fibonacci-Pascal triangle read by rows: T(n, n) = 1, T(n, n-1) = n - 1, T(n, |
| 22  | A371870 | Std-CentralE     | a(n) = Sum_{k=0..floor(n/2)} binomial(2*n-k-1,n-2*k)                           |

* Statistic about Fibonacci:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 22.
	all      A-numbers  : 66.
	missing  sequences  : 61.

[('missing', 61), ('A000045', 9), ('A099036', 8), ('A371870', 6), ('A000027', 5), ('A174965', 3), ('A027988', 3), ('A004006', 3), ('A002061', 3), ('A001924', 3), ('A000124', 3), ('A000071', 3), ('A000012', 3), ('A354267', 2), ('A113312', 2), ('A069778', 2), ('A039834', 2), ('A212804', 1), ('A108081', 1), ('A106511', 1), ('A079282', 1), ('A027444', 1), ('A006367', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Fibonacci.html .
2025/01/10

'''
