from functools import cache
from _tabltypes import MakeTriangle

"""Eulerian triangle.

[0]  1,
[1]  1,    0,
[2]  1,    1,     0,
[3]  1,    4,     1,      0,
[4]  1,   11,    11,      1,      0,
[5]  1,   26,    66,     26,      1,    0,
[6]  1,   57,   302,    302,     57,    1,   0,
[7]  1,  120,  1191,   2416,   1191,  120,   1,  0,
[8]  1,  247,  4293,  15619,  15619, 4293, 247,  1,  0
=======================================================
0:  1
1:  0 1
2:  0 1    1
3:  0 1    4     1
4:  0 1   11    11      1
5:  0 1   26    66     26       1
6:  0 1   57   302    302      57       1
7:  0 1  120  1191   2416    1191     120      1
8:  0 1  247  4293  15619   15619    4293    247     1
"""


@cache
def KnuthEulerian(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = KnuthEulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@cache
def eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = eulerian(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - k + 1) * row[k - 1] + k * row[k]
    return row


@MakeTriangle(eulerian, "Eulerian", ["A123125", "A173018", "A008292"], True)
def Eulerian(n: int, k: int) -> int:
    return eulerian(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Eulerian)

''' OEIS

The traits of the Eulerian triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-RowSum       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000295 | Std-DiagRow1     | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1 of A1730 |
| 6   | A000460 | Std-DiagRow2     | Eulerian numbers (Euler's triangle: column k=3 of A008292, column k=2 of A1730 |
| 7   | A000498 | Std-DiagRow3     | Eulerian numbers (Euler's triangle: column k=4 of A008292, column k=3 of A1730 |
| 8   | A000629 | Std-PolyCol2     | Number of necklaces of partitions of n+1 labeled beads                         |
| 9   | A000670 | Std-PosHalf      | Fubini numbers: number of preferential arrangements of n labeled elements; or  |
| 10  | A000800 | Std-DiagSum      | Sum of upward diagonals of Eulerian triangle                                   |
| 11  | A001286 | Rev-TransNat0    | Lah numbers: a(n) = (n-1)*n!/2                                                 |
| 12  | A001710 | Std-AccSum       | Order of alternating group A_n, or number of even permutations of n letters    |
| 13  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 14  | A006551 | Std-RowMax       | Maximal Eulerian numbers                                                       |
| 15  | A009006 | Std-AltSum       | Expansion of e.g.f.: 1 + tan(x)                                                |
| 16  | A011818 | Std-BinConv      | Normalized volume of center slice of n-dimensional cube: 2^n* n!*Vol({ (x_1,.. |
| 17  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 18  | A025585 | Rev-CentralO     | Central Eulerian numbers A(2n-1,n)                                             |
| 19  | A028872 | Rev-PolyRow3     | a(n) = n^2 - 3                                                                 |
| 20  | A038720 | Std-AccRevSum    | a(n) = (n+3)*n!/2                                                              |
| 21  | A045944 | Inv:Rev-PolyRow3 | Rhombic matchstick numbers: a(n) = n*(3*n+2)                                   |
| 22  | A055326 | Inv-DiagCol1     | Column 1 of triangle A055325                                                   |
| 23  | A122020 | Std-PolyDiag     | Sum[k=0..n] Eulerian[n,k]*n^k                                                  |
| 24  | A122704 | Rev-PolyCol3     | a(n) = Sum_{k=0..n} 3^(n-k)*A123125(n, k)                                      |
| 25  | A122778 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} A(n,k)*n^k where A(n,k) are Eulerian numbers               |
| 26  | A123227 | Std-PolyCol3     | Expansion of e.g.f.: 2*exp(2*x) / (3 - exp(2*x))                               |
| 27  | A128103 | Std-OddSum       | Number of permutations of [n] with an even number of rises                     |
| 28  | A173018 | Std-Triangle     | Euler's triangle: triangle of Eulerian numbers T(n,k) (n>=0, 0 <= k <= n) read |
| 29  | A179929 | Alt-PolyCol2     | a(n) = 2^n*A(n, -1/2), A(n, x) the Eulerian polynomials                        |
| 30  | A180056 | Std-CentralE     | The number of permutations of {1,2,...,2n} with n ascents                      |
| 31  | A180057 | Std-RowLcm       | The LCM of the n-th row of the triangle of Eulerian numbers, A008292           |
| 32  | A212846 | Std-NegHalf      | Polylogarithm li(-n,-1/2) multiplied by (3^(n+1))/2                            |
| 33  | A262745 | Std-EvenSum      | Number of permutations of [n] with an odd number of rises                      |
| 34  | A332700 | Rev-Poly         | A(n, k) = Sum_{j=0..n} j!*Stirling2(n, j)*(k-1)^(n-j), for n >= 0 and k >= 0,  |
| 35  | A344052 | Std-InvBinConv   | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n, k)*E1(n, k)                         |
| 36  | A344054 | Rev-TransSqrs    | a(n) = Sum_{k = 0..n} E1(n, k)*k^2, where E1 are the Eulerian numbers A173018  |
| 37  | A344393 | Rev-AntiDiag     | T(n, k) = Eulerian1(n - k, k), for n >= 0 and 0 <= k <= floor(n/2). Triangle r |

* Statistic about Eulerian:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 37.
	all      A-numbers  : 112.
	missing  sequences  : 103.

[('missing', 103), ('A000012', 11), ('A000295', 8), ('A173018', 7), ('A000460', 6), ('A000142', 6), ('A000027', 5), ('A000007', 5), ('A006551', 4), ('A001710', 4), ('A344052', 3), ('A262745', 3), ('A180057', 3), ('A180056', 3), ('A128103', 3), ('A038720', 3), ('A011818', 3), ('A009006', 3), ('A002378', 3), ('A000670', 3), ('A000498', 3), ('A212846', 2), ('A179929', 2), ('A055326', 2), ('A019590', 2), ('A000800', 2), ('A000629', 2), ('A344393', 1), ('A344054', 1), ('A332700', 1), ('A123227', 1), ('A122778', 1), ('A122704', 1), ('A122020', 1), ('A045944', 1), ('A028872', 1), ('A025585', 1), ('A001286', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Eulerian.html .
2025/01/10

'''
