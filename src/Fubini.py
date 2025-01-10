from functools import cache
from _tabltypes import MakeTriangle

"""Fubini triangle.

[0]  1;
[1]  0,  1;
[2]  0,  1,    2;
[3]  0,  1,    6,     6;
[4]  0,  1,   14,    36,    24;
[5]  0,  1,   30,   150,   240,    120;
[6]  0,  1,   62,   540,  1560,   1800,    720;
[7]  0,  1,  126,  1806,  8400,  16800,  15120,  5040;
[8]  0,  1,  254,  5796, 40824, 126000, 191520, 141120, 40320;
"""


@cache
def fubini(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return fubini(n - 1)[k] if k <= n - 1 else 0

    row = [0] + fubini(n - 1)
    for k in range(1, n + 1):
        row[k] = k * (r(k - 1) + r(k))
    return row


@MakeTriangle(fubini, "Fubini", ["A131689", "A019538", "A090582", "A278075"], False)
def Fubini(n: int, k: int) -> int:
    return fubini(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Fubini)

''' OEIS

The traits of the Fubini triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Alt-AccRevSum    | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000142 | Std-ColRight     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000225 | Alt-TransNat0    | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 7   | A000247 | Alt-AccSum       | a(n) = 2^n - n - 2                                                             |
| 8   | A000312 | Std-BinConv      | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 9   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 10  | A000629 | Alt-PolyCol2     | Number of necklaces of partitions of n+1 labeled beads                         |
| 11  | A000670 | Std-RowSum       | Fubini numbers: number of preferential arrangements of n labeled elements; or  |
| 12  | A000918 | Std-DiagCol2     | a(n) = 2^n - 2                                                                 |
| 13  | A001117 | Std-DiagCol3     | a(n) = 3^n - 3*2^n + 3                                                         |
| 14  | A001286 | Std-DiagRow1     | Lah numbers: a(n) = (n-1)*n!/2                                                 |
| 15  | A002869 | Std-RowMax       | Largest number in n-th row of triangle A019538                                 |
| 16  | A004123 | Std-PolyCol2     | Number of generalized weak orders on n points                                  |
| 17  | A005649 | Std-AccRevSum    | Expansion of e.g.f. (2 - e^x)^(-2)                                             |
| 18  | A009006 | Std-NegHalf      | Expansion of e.g.f.: 1 + tan(x)                                                |
| 19  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 20  | A027760 | Std-RowGcd       | Denominator of Sum_{p prime, p-1 divides n} 1/p                                |
| 21  | A028872 | Rev-PolyRow3     | a(n) = n^2 - 3                                                                 |
| 22  | A032033 | Std-PolyCol3     | Stirling transform of A032031                                                  |
| 23  | A032109 | Rev-EvenSum      | "BIJ" (reversible, indistinct, labeled) transform of 1,1,1,1,..                |
| 24  | A037960 | Std-DiagRow2     | a(n) = n*(3*n+1)*(n+2)!/24                                                     |
| 25  | A037961 | Std-DiagRow3     | a(n) = n^2*(n+1)*(n+3)!/48                                                     |
| 26  | A052841 | Std-EvenSum      | Expansion of e.g.f.: 1/(exp(x)*(2-exp(x)))                                     |
| 27  | A069321 | Std-TransNat0    | Stirling transform of A001563: a(0) = 1 and a(n) = Sum_{k=1..n} Stirling2(n,k) |
| 28  | A083411 | Std-TransSqrs    | a(n) = Sum(((k-1)/2)*k!*Stirling_2(n,k),k=1..n)                                |
| 29  | A089677 | Std-OddSum       | Exponential convolution of A000670(n), with A000670(0)=0, with the sequence of |
| 30  | A091344 | Alt-TransSqrs    | a(n) = 2*3^n - 3*2^n + 1                                                       |
| 31  | A094420 | Std-PolyDiag     | Generalized ordered Bell numbers Bo(n,n)                                       |
| 32  | A094421 | Std-PolyRow3     | a(n) = n * (6*n^2 + 6*n + 1)                                                   |
| 33  | A105795 | Std-DiagSum      | Shallow diagonal sums of the triangle k!*Stirling2(n,k): a(n) = Sum_{k=0..floo |
| 34  | A120368 | Std-AccSum       | a(n) = number of sequences (a_1, a_2, ..., a_n) in {1,2,...,n} such that the r |
| 35  | A122704 | Std-PosHalf      | a(n) = Sum_{k=0..n} 3^(n-k)*A123125(n, k)                                      |
| 36  | A131689 | Std-Triangle     | Triangle of numbers T(n,k) = k!*Stirling2(n,k) = A000142(k)*A048993(n,k) read  |
| 37  | A201339 | Alt-PolyCol3     | Expansion of e.g.f. exp(x) / (3 - 2*exp(x))                                    |
| 38  | A210029 | Std-CentralE     | Number of sequences over the alphabet of n symbols of length 2n which have n d |
| 39  | A233734 | Rev-CentralO     | Central terms of triangles A019538 and A090582                                 |
| 40  | A255927 | Rev-PolyCol3     | a(n) = (3/4) * Sum_{k>=0} (3*k)^n/4^k                                          |
| 41  | A331690 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} Stirling2(n,k) * k! * n^(n - k)                            |
| 42  | A344053 | Std-InvBinConv   | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n, k)*Stirling2(n, k)*k!               |
| 43  | A344392 | Std-AntiDiag     | T(n, k) = k!*Stirling2(n - k, k), for n >= 0 and 0 <= k <= floor(n/2). Triangl |
| 44  | A344397 | Std-ColMiddle    | a(n) = Stirling2(n, floor(n/2)) * floor(n/2)!                                  |
| 45  | A344499 | Std-Poly         | T(n, k) = F(n - k, k), where F(n, x) is the Fubini polynomial. Triangle read b |
| 46  | A367392 | Std-CentralO     | a(n) = Sum_{k=0..n} (-1)^k * binomial(n, k) * (n - k)^(2*n + 1)                |

* Statistic about Fubini:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 46.
	all      A-numbers  : 96.
	missing  sequences  : 25.

[('missing', 25), ('A000670', 6), ('A000012', 5), ('A344053', 3), ('A210029', 3), ('A122704', 3), ('A120368', 3), ('A037961', 3), ('A037960', 3), ('A027760', 3), ('A005649', 3), ('A002869', 3), ('A001286', 3), ('A001117', 3), ('A000918', 3), ('A000312', 3), ('A000142', 3), ('A000027', 3), ('A000007', 3), ('A367392', 2), ('A344397', 2), ('A344392', 2), ('A089677', 2), ('A052841', 2), ('A009006', 2), ('A004123', 2), ('A000629', 2), ('A000079', 2), ('A344499', 1), ('A331690', 1), ('A255927', 1), ('A233734', 1), ('A201339', 1), ('A131689', 1), ('A105795', 1), ('A094421', 1), ('A094420', 1), ('A091344', 1), ('A083411', 1), ('A069321', 1), ('A032109', 1), ('A032033', 1), ('A028872', 1), ('A014105', 1), ('A000384', 1), ('A000247', 1), ('A000225', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Fubini.html .
2025/01/10

'''
