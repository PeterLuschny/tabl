from functools import cache
from _tabltypes import MakeTriangle

"""Rencontres triangle.

[0]       1;
[1]       0,      1;
[2]       1,      0,     1;
[3]       2,      3,     0,     1;
[4]       9,      8,     6,     0,    1;
[5]      44,     45,    20,    10,    0,    1;
[6]     265,    264,   135,    40,   15,    0,   1;
[7]    1854,   1855,   924,   315,   70,   21,   0,  1;
[8]   14833,  14832,  7420,  2464,  630,  112,  28,  0, 1;
[9]  133496, 133497, 66744, 22260, 5544, 1134, 168, 36, 0, 1;
"""


@cache
def rencontres(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = [
        (n - 1) * (rencontres(n - 1)[0] + rencontres(n - 2)[0])
    ] + rencontres(n - 1)
    for k in range(1, n - 1):
        row[k] = (n * row[k]) // k
    return row


@MakeTriangle(rencontres, "Rencontres", ["A008290", "A098825"], True)
def Rencontres(n: int, k: int) -> int:
    return rencontres(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Rencontres)

''' OEIS

The traits of the Rencontres triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000023 | Std-AltSum       | Expansion of e.g.f. exp(-2*x)/(1-x)                                            |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Alt-AccRevSum    | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000142 | Std-RowSum       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000166 | Std-ColLeft      | Subfactorial or rencontres numbers, or derangements: number of permutations of |
| 7   | A000217 | Std-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 8   | A000240 | Std-DiagCol1     | Rencontres numbers: number of permutations of [n] with exactly one fixed point |
| 9   | A000272 | Inv-PolyDiag     | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 10  | A000354 | Std-PosHalf      | Expansion of e.g.f. exp(-x)/(1-2*x)                                            |
| 11  | A000387 | Std-DiagCol2     | Rencontres numbers: number of permutations of [n] with exactly two fixed point |
| 12  | A000449 | Std-DiagCol3     | Rencontres numbers: number of permutations of [n] with exactly 3 fixed points  |
| 13  | A000522 | Std-PolyCol2     | Total number of ordered k-tuples (k=0..n) of distinct elements from an n-eleme |
| 14  | A000917 | Inv-CentralO     | a(n) = (2n+3)!/(n!*(n+2)!)                                                     |
| 15  | A001563 | Std-AccSum       | a(n) = n*n! = (n+1)! - n!                                                      |
| 16  | A001787 | Alt-TransSqrs    | a(n) = n*2^(n-1)                                                               |
| 17  | A001815 | Inv:Rev-TransNat | a(n) = binomial(n,2) * 2^(n-1)                                                 |
| 18  | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 19  | A005408 | Inv-NegHalf      | The odd numbers: a(n) = 2*n + 1                                                |
| 20  | A005563 | Inv-DiagCol1     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 21  | A005564 | Inv-DiagCol2     | Number of n-step walks on square lattice in the first quadrant which finish at |
| 22  | A007290 | Std-DiagRow3     | a(n) = 2*binomial(n,3)                                                         |
| 23  | A008290 | Std-Triangle     | Triangle T(n,k) of rencontres numbers (number of permutations of n elements wi |
| 24  | A010842 | Std-PolyCol3     | Expansion of e.g.f.: exp(2*x)/(1-x)                                            |
| 25  | A010843 | Alt-PolyCol2     | Incomplete Gamma Function at -3                                                |
| 26  | A015238 | Inv:Rev-PolyRow3 | a(n) = (2*n - 3)n^2                                                            |
| 27  | A019590 | Inv:Rev-AltSum   | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 28  | A036289 | Inv-EvenSum      | a(n) = n*2^n                                                                   |
| 29  | A048495 | Inv-AbsSum       | a(n) = (n-1)*2^n + 2                                                           |
| 30  | A052849 | Std-AccRevSum    | a(0) = 0; a(n) = 2*n! (n >= 1)                                                 |
| 31  | A055137 | Std-Inv          | Regard triangle of rencontres numbers (see A008290) as infinite matrix, comput |
| 32  | A058922 | Inv-RowSum       | a(n) = n*2^n - 2^n                                                             |
| 33  | A062119 | Rev-TransNat0    | a(n) = n! * (n-1)                                                              |
| 34  | A062282 | Std-EvenSum      | Number of permutations of n elements with an even number of fixed points       |
| 35  | A063083 | Std-OddSum       | Number of permutations of n elements with an odd number of fixed points        |
| 36  | A067331 | Inv-DiagSum      | Convolution of Fibonacci F(n+1), n >= 0, with F(n+3), n >= 0                   |
| 37  | A076616 | Inv-AccSum       | Number of permutations of {1,2,...,n} that result in a binary search tree (whe |
| 38  | A098825 | Std-Rev          | Triangle read by rows: T(n,k) = number of partial derangements, that is, the n |
| 39  | A133297 | Alt-PolyDiag     | a(n) = n!*Sum_{k=1..n} (-1)^(k+1)*n^(n-k-1)/(n-k)!                             |
| 40  | A174318 | Std-RowMax       | a(n) = ceiling(n!/e) with e = A001113 = exp(1)                                 |
| 41  | A177258 | Alt-DiagSum      | Number of derangements of {1,2,...,n} having no adjacent transpositions        |
| 42  | A178987 | Inv-TransNat0    | a(n) = n*(n-3)*2^(n-2)                                                         |
| 43  | A191522 | Inv-RowMax       | Number of valleys in all left factors of Dyck paths of length n. A valley is a |
| 44  | A217701 | Std-PolyDiag     | Permanent of the n X n matrix with all diagonal entries n and all off diagonal |
| 45  | A281262 | Std-CentralE     | Number of permutations of [2n] with exactly n fixed points                     |
| 46  | A335111 | Alt-TransNat0    | a(n) = n! * Sum_{k=0..n-1} (-2)^k / k!                                         |
| 47  | A343582 | Std-NegHalf      | a(n) = (-1)^n*n!*[x^n] exp(-3*x)/(1 - 2*x)                                     |
| 48  | A371995 | Rev-AntiDiag     | Triangle read by rows: T(n, k) = binomial(n - k, k) * subfactorial(k), for n > |
| 49  | A372102 | Rev-DiagSum      | Number of permutations of [n] whose non-fixed points are not neighbors         |

* Statistic about Rencontres:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 49.
	all      A-numbers  : 127.
	missing  sequences  : 82.

[('missing', 82), ('A000012', 11), ('A000142', 7), ('A000027', 6), ('A007290', 5), ('A000217', 5), ('A098825', 4), ('A055137', 4), ('A052849', 4), ('A036289', 4), ('A005563', 4), ('A281262', 3), ('A174318', 3), ('A076616', 3), ('A008290', 3), ('A002522', 3), ('A001563', 3), ('A000449', 3), ('A000387', 3), ('A000354', 3), ('A000240', 3), ('A000166', 3), ('A000023', 3), ('A343582', 2), ('A191522', 2), ('A063083', 2), ('A062282', 2), ('A058922', 2), ('A048495', 2), ('A010843', 2), ('A005564', 2), ('A000522', 2), ('A000079', 2), ('A372102', 1), ('A371995', 1), ('A335111', 1), ('A217701', 1), ('A178987', 1), ('A177258', 1), ('A133297', 1), ('A067331', 1), ('A062119', 1), ('A019590', 1), ('A015238', 1), ('A010842', 1), ('A005408', 1), ('A001815', 1), ('A001787', 1), ('A000917', 1), ('A000272', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Rencontres.html .
2025/01/10

'''
