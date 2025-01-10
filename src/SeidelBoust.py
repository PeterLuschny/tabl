from _tabltypes import MakeTriangle
from Seidel import seidel


"""Seidel boustrophedon:

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,   0]
[3] [ 0,  1,   2,   2]
[4] [ 5,  5,   4,   2,   0]
[5] [ 0,  5,  10,  14,  16,  16]
[6] [61, 61,  56,  46,  32,  16,   0]
[7] [ 0, 61, 122, 178, 224, 256, 272, 272]
"""

# #@


def seidelboust(n: int) -> list[int]:
    return seidel(n) if n % 2 else seidel(n)[::-1]


@MakeTriangle(
    seidelboust, "SeidelBoust", ["A008280", "A108040", "A236935", "A239005"], False
)
def SeidelBoust(n: int, k: int) -> int:
    return seidelboust(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SeidelBoust)

''' OEIS

The traits of the SeidelBoust triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Rev-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000111 | Std-RowSum       | Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the nu |
| 4   | A000657 | Std-CentralE     | Median Euler numbers (the middle numbers of Arnold's shuttle triangle)         |
| 5   | A001586 | Std-BinConv      | Generalized Euler numbers, or Springer numbers                                 |
| 6   | A002378 | Rev-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 7   | A002522 | Rev-PolyRow3     | a(n) = n^2 + 1                                                                 |
| 8   | A005437 | Rev-ColMiddle    | Column of Kempner tableau                                                      |
| 9   | A008280 | Std-Triangle     | Boustrophedon version of triangle of Euler-Bernoulli or Entringer numbers read |
| 10  | A009006 | Std-ColRight     | Expansion of e.g.f.: 1 + tan(x)                                                |
| 11  | A048395 | Std-PolyRow3     | Sum of consecutive nonsquares                                                  |
| 12  | A059722 | Alt-PolyRow3     | a(n) = n*(2*n^2 - 2*n + 1)                                                     |
| 13  | A108040 | Std-Rev          | Reflection of triangle in A008280 in vertical axis                             |
| 14  | A122045 | Std-ColLeft      | Euler (or secant) numbers E(n)                                                 |
| 15  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 16  | A240561 | Std-CentralO     | The main diagonal in the difference table of A240559                           |
| 17  | A241209 | Std-DiagCol1     | a(n) = E(n) - E(n+1), where E(n) are the Euler numbers A122045(n)              |

* Statistic about SeidelBoust:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 17.
	all      A-numbers  : 44.
	missing  sequences  : 78.

[('missing', 78), ('A000111', 9), ('A000027', 4), ('A241209', 3), ('A174965', 3), ('A122045', 3), ('A108040', 3), ('A009006', 3), ('A001586', 3), ('A000657', 3), ('A240561', 2), ('A008280', 2), ('A059722', 1), ('A048395', 1), ('A005437', 1), ('A002522', 1), ('A002378', 1), ('A000012', 1)]

A related webpage is: https://peterluschny.github.io/tabl/SeidelBoust.html .
2025/01/10

'''
