from functools import cache
from _tabltypes import MakeTriangle

"""Pascal triangle, binomial coefficients.


[0]   1;
[1]   1,   1;
[2]   1,   2,   1;
[3]   1,   3,   3,   1;
[4]   1,   4,   6,   4,   1;
[5]   1,   5,  10,  10,   5,   1;
[6]   1,   6,  15,  20,  15,   6,   1;
[7]   1,   7,  21,  35,  35,  21,   7,   1;
[8]   1,   8,  28,  56,  70,  56,  28,   8,   1;
[9]   1,   9,  36,  84, 126, 126,  84,  36,   9,   1;
"""


@cache
def pascal(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1] + pascal(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


@MakeTriangle(
    pascal,
    "Pascal",
    [
        "A007318",
        "A074909",
        "A108086",
        "A117440",
        "A118433",
        "A130595",
        "A135278",
        "A154926",
    ],
    True,
)
def Pascal(n: int, k: int) -> int:
    return pascal(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Pascal)

''' OEIS

The traits of the Pascal triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000045 | Std-DiagSum      | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 5   | A000079 | Std-RowSum       | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000169 | Std-PolyDiag     | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 7   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 8   | A000244 | Std-PosHalf      | Powers of 3: a(n) = 3^n                                                        |
| 9   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 10  | A000292 | Std-DiagRow3     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 11  | A000302 | Std-PolyCol3     | Powers of 4: a(n) = 4^n                                                        |
| 12  | A000578 | Std-PolyRow3     | The cubes: a(n) = n^3                                                          |
| 13  | A000984 | Std-CentralE     | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 14  | A001405 | Std-RowMax       | a(n) = binomial(n, floor(n/2))                                                 |
| 15  | A001700 | Std-CentralO     | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 16  | A001787 | Std-TransNat0    | a(n) = n*2^(n-1)                                                               |
| 17  | A001788 | Std-TransSqrs    | a(n) = n*(n+1)*2^(n-2)                                                         |
| 18  | A001792 | Std-AccSum       | a(n) = (n+2)*2^(n-1)                                                           |
| 19  | A002944 | Std-RowLcm       | a(n) = LCM(1,2,...,n) / n                                                      |
| 20  | A007318 | Std-Triangle     | Pascal's triangle read by rows: C(n,k) = binomial(n,k) = n!/(k!*(n-k)!), 0 <=  |
| 21  | A007778 | Alt-PolyDiag     | a(n) = n^(n+1)                                                                 |
| 22  | A008949 | Std-Acc          | Triangle read by rows of partial sums of binomial coefficients: T(n,k) = Sum_{ |
| 23  | A009998 | Std-Poly         | Triangle in which j-th entry in i-th row is (j+1)^(i-j)                        |
| 24  | A011973 | Std-AntiDiag     | Irregular triangle read by rows: T(n,k) = binomial(n-k, k), n >= 0, 0 <= k <=  |
| 25  | A014963 | Std-RowGcd       | Exponential of Mangoldt function M(n): a(n) = 1 unless n is a prime or prime p |
| 26  | A019590 | Alt-AccSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 27  | A039968 | Alt-TransSqrs    | An example of a d-perfect sequence                                             |
| 28  | A063524 | Alt-TransNat0    | Characteristic function of 1                                                   |
| 29  | A071919 | Alt-Acc          | Number of monotone nondecreasing functions [n]->[m] for n >= 0, m >= 0, read b |
| 30  | A103406 | Std-Diffx1       | Triangle read by rows: n-th row = unsigned coefficients of the characteristic  |
| 31  | A126869 | Std-InvBinConv   | a(n) = Sum_{k = 0..n} binomial(n,floor(k/2))*(-1)^(n-k)                        |

* Statistic about Pascal:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 31.
	all      A-numbers  : 150.
	missing  sequences  : 8.

[('A000079', 19), ('A007318', 14), ('A000027', 12), ('missing', 8), ('A001405', 8), ('A000984', 8), ('A000292', 8), ('A000217', 8), ('A000012', 8), ('A000244', 5), ('A126869', 4), ('A019590', 4), ('A014963', 4), ('A002944', 4), ('A001700', 4), ('A000578', 4), ('A000290', 4), ('A000007', 4), ('A071919', 3), ('A063524', 3), ('A039968', 3), ('A007778', 3), ('A001792', 3), ('A103406', 2), ('A011973', 2), ('A008949', 2), ('A000045', 2), ('A009998', 1), ('A001788', 1), ('A001787', 1), ('A000302', 1), ('A000169', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Pascal.html .
2025/01/10

'''
