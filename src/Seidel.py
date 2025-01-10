from functools import cache
from _tabltypes import MakeTriangle

"""Seidel triangle.

[0] [1]
[1] [0,   1]
[2] [0,   1,   1]
[3] [0,   1,   2,   2]
[4] [0,   2,   4,   5,    5]
[5] [0,   5,  10,  14,   16,   16]
[6] [0,  16,  32,  46,   56,   61,   61]
[7] [0,  61, 122, 178,  224,  256,  272,  272]
"""


@cache
def seidel(n: int) -> list[int]:
    if n == 0:
        return [1]

    rowA = seidel(n - 1)
    row = [0] + seidel(n - 1)
    row[1] = row[n]
    for k in range(2, n + 1):
        row[k] = row[k - 1] + rowA[n - k]
    return row


@MakeTriangle(seidel, "Seidel", ["A008281", "A008282", "A010094"], False)
def Seidel(n: int, k: int) -> int:
    return seidel(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Seidel)

''' OEIS

The traits of the Seidel triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Rev-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000111 | Std-RowSum       | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the nu |
| 5   | A000657 | Std-CentralE     | Median Euler numbers (the middle numbers of Arnold's shuttle triangle)         |
| 6   | A001250 | Std-DiagCol2     | Number of alternating permutations of order n                                  |
| 7   | A001586 | Std-BinConv      | Generalized Euler numbers, or Springer numbers                                 |
| 8   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 9   | A002522 | Rev-PolyRow3     | a(n) = n^2 + 1                                                                 |
| 10  | A005437 | Rev-ColMiddle    | Column of Kempner tableau                                                      |
| 11  | A006212 | Std-DiagRow2     | Number of down-up permutations of n+3 starting with n+1                        |
| 12  | A006213 | Std-DiagRow3     | Number of down-up permutations of n+4 starting with n+1                        |
| 13  | A006216 | Std-DiagCol3     | Number of down-up permutations of n+4 starting with 4                          |
| 14  | A008281 | Std-Triangle     | Triangle of Euler-Bernoulli or Entringer numbers read by rows                  |
| 15  | A008282 | Std-AccRev       | Triangle of Euler-Bernoulli or Entringer numbers read by rows: T(n,k) is the n |
| 16  | A034428 | Std-AccSum       | E.g.f.: 1 - (1-x)*(tan(x) + sec(x))                                            |
| 17  | A048395 | Std-PolyRow3     | Sum of consecutive nonsquares                                                  |
| 18  | A059722 | Alt-PolyRow3     | a(n) = n*(2*n^2 - 2*n + 1)                                                     |
| 19  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 20  | A240561 | Std-CentralO     | The main diagonal in the difference table of A240559                           |
| 21  | A278678 | Rev-TransNat0    | Popularity of left children in treeshelves avoiding pattern T321               |

* Statistic about Seidel:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 21.
	all      A-numbers  : 65.
	missing  sequences  : 57.

[('missing', 57), ('A000111', 21), ('A174965', 3), ('A034428', 3), ('A006216', 3), ('A006213', 3), ('A006212', 3), ('A001586', 3), ('A001250', 3), ('A000657', 3), ('A000027', 3), ('A000007', 3), ('A240561', 2), ('A008282', 2), ('A008281', 2), ('A002378', 2), ('A278678', 1), ('A059722', 1), ('A048395', 1), ('A005437', 1), ('A002522', 1), ('A000012', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Seidel.html .
2025/01/10

'''
