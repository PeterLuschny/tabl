from functools import cache
from itertools import accumulate
from _tabltypes import MakeTriangle

"""Fuss-Catalan triangle.

[0] [1]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  5]
[4] [0, 1, 4,  9, 14]
[5] [0, 1, 5, 14, 28,  42]
[6] [0, 1, 6, 20, 48,  90, 132]
[7] [0, 1, 7, 27, 75, 165, 297, 429]
"""


@cache
def fusscatalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = fusscatalan(n - 1) + [fusscatalan(n - 1)[n - 1]]
    return list(accumulate(row))


@MakeTriangle(fusscatalan, "FussCatalan", ["A355173", "A030237", "A054445"], False)
def FussCatalan(n: int, k: int) -> int:
    return fusscatalan(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(FussCatalan)

''' OEIS

The traits of the FussCatalan triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-InvBinConv   | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000096 | Std-DiagCol3     | a(n) = n*(n+3)/2                                                               |
| 5   | A000108 | Std-RowMax       | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 6   | A000245 | Std-RowSum       | a(n) = 3*(2*n)!/((n+2)!*(n-1)!)                                                |
| 7   | A000344 | Std-DiagRow3     | a(n) = 5*binomial(2n, n-2)/(n+3)                                               |
| 8   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 9   | A000957 | Rev-EvenSum      | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 10  | A000958 | Std-AltSum       | Number of ordered rooted trees with n edges having root of odd degree          |
| 11  | A001558 | Rev-OddSum       | Number of hill-free Dyck paths of semilength n+3 and having length of first de |
| 12  | A001791 | Std-PosHalf      | a(n) = binomial coefficient C(2n, n-1)                                         |
| 13  | A002057 | Std-AccSum       | Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)        |
| 14  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 15  | A026004 | Rev-CentralO     | a(n) = T(3n+1,n), where T = Catalan triangle (A008315)                         |
| 16  | A027688 | Rev-PolyRow3     | a(n) = n^2 + n + 3                                                             |
| 17  | A037952 | Std-DiagSum      | a(n) = binomial(n, floor((n-1)/2))                                             |
| 18  | A065601 | Alt-AccSum       | Number of Dyck paths of length 2n with exactly 1 hill                          |
| 19  | A208355 | Alt-DiagSum      | Right edge of the triangle in A208101                                          |
| 20  | A262394 | Std-CentralE     | a(n) = (1/n)*Sum_{k=1..n} k*binomial(n,k-1)*binomial(2*n,n-k)                  |
| 21  | A289871 | Std-AntiDiag     | Irregular triangle read by rows T(n, k) is the number of admissible pinnacle s |
| 22  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 23  | A355173 | Std-Triangle     | The Fuss-Catalan triangle of order 1, read by rows. Related to binary trees    |

* Statistic about FussCatalan:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 23.
	all      A-numbers  : 68.
	missing  sequences  : 56.

[('missing', 56), ('A000245', 9), ('A000027', 9), ('A002057', 6), ('A000108', 6), ('A000344', 4), ('A000012', 4), ('A297382', 3), ('A262394', 3), ('A001791', 3), ('A000958', 3), ('A000096', 3), ('A000007', 3), ('A355173', 2), ('A289871', 1), ('A208355', 1), ('A065601', 1), ('A037952', 1), ('A027688', 1), ('A026004', 1), ('A014105', 1), ('A001558', 1), ('A000957', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/FussCatalan.html .
2025/01/10

'''
