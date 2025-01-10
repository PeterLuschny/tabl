from functools import cache
from _tabltypes import MakeTriangle
from Binomial import binomial

"""Lozanic numbers.


[0]  1;
[1]  1,  1;
[2]  1,  1,  1;
[3]  1,  2,  2,  1;
[4]  1,  2,  4,  2,  1;
[5]  1,  3,  6,  6,  3,  1;
[6]  1,  3,  9, 10,  9,  3,  1;
[7]  1,  4, 12, 19, 19, 12,  4,  1;
[8]  1,  4, 16, 28, 38, 28, 16,  4,  1;
[9]  1,  5, 20, 44, 66, 66, 44, 20,  5,  1;
"""


@cache
def lozanic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1] + lozanic(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]

    if n % 2 != 0:
        return row

    b = binomial(n // 2 - 1)
    for k in range(1, n, 2):
        row[k] -= b[(k - 1) // 2]

    return row


@MakeTriangle(lozanic, "Lozanic", ["A034851"], True)
def Lozanic(n: int, k: int) -> int:
    return lozanic(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Lozanic)

''' OEIS

The traits of the Lozanic triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-RowSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A001224 | Std-DiagSum      | If F(n) is the n-th Fibonacci number, then a(2n) = (F(2n+1) + F(n+2))/2 and a( |
| 5   | A002061 | Std-PolyRow2     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 6   | A002378 | Inv-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 7   | A002620 | Std-DiagRow2     | Quarter-squares: a(n) = floor(n/2)*ceiling(n/2). Equivalently, a(n) = floor(n^ |
| 8   | A004526 | Std-DiagRow1     | Nonnegative integers repeated, floor(n/2)                                      |
| 9   | A005418 | Std-RowSum       | Number of (n-1)-bead black-white reversible strings; also binary grids; also r |
| 10  | A005654 | Std-CentralO     | Number of bracelets (turn over necklaces) with n red, 1 pink and n-1 blue bead |
| 11  | A005993 | Std-DiagRow3     | Expansion of (1+x^2)/((1-x)^2*(1-x^2)^2)                                       |
| 12  | A027444 | Alt-PolyRow3     | a(n) = n^3 + n^2 + n                                                           |
| 13  | A032123 | Std-CentralE     | Number of 2n-bead black-white reversible strings with n black beads            |
| 14  | A033445 | Inv:Rev-PolyRow3 | a(n) = (n - 1)*(n^2 + n - 1)                                                   |
| 15  | A034851 | Std-Triangle     | Rows of Losanitsch's triangle T(n, k), n >= 0, 0 <= k <= n                     |
| 16  | A034872 | Std-RowMax       | Central column of Losanitsch's triangle A034851                                |
| 17  | A051437 | Std-OddSum       | Number of undirected walks of length n+1 on an oriented triangle, visiting n+2 |
| 18  | A055138 | Std-Inv          | Matrix inverse of Losanitsch's triangle A034851                                |
| 19  | A055139 | Inv-ColLeft      | Column 0 of triangle A055138                                                   |
| 20  | A069778 | Std-PolyRow3     | q-factorial numbers 3!_q                                                       |
| 21  | A077957 | Std-AltSum       | Powers of 2 alternating with zeros                                             |
| 22  | A081437 | Inv-PolyRow3     | Diagonal in array of n-gonal numbers A081422                                   |
| 23  | A087102 | Inv-RowGcd       | Number of numbers occurring most frequently as difference between consecutive  |
| 24  | A102541 | Std-AntiDiag     | Triangle read by rows, formed from antidiagonals of Losanitsch's triangle. T(n |

* Statistic about Lozanic:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 24.
	all      A-numbers  : 68.
	missing  sequences  : 102.

[('missing', 102), ('A034851', 6), ('A005418', 6), ('A055138', 5), ('A004526', 5), ('A000027', 5), ('A000012', 5), ('A034872', 4), ('A005993', 4), ('A002620', 4), ('A102541', 2), ('A087102', 2), ('A077957', 2), ('A055139', 2), ('A051437', 2), ('A032123', 2), ('A005654', 2), ('A002061', 2), ('A000007', 2), ('A081437', 1), ('A069778', 1), ('A033445', 1), ('A027444', 1), ('A002378', 1), ('A001224', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Lozanic.html .
2025/01/10

'''
