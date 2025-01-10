from functools import cache
from _tabltypes import MakeTriangle

"""The hyperharmonic numbers.

[0]    1;
[1]    1,     1;
[2]    2,     3,    1;
[3]    6,    11,    5,    1;
[4]   24,    50,   26,    7,   1;
[5]  120,   274,  154,   47,   9,   1;
[6]  720,  1764, 1044,  342,  74,  11,  1;
[7] 5040, 13068, 8028, 2754, 638, 107, 13, 1;
"""


@cache
def hyperharmonic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = hyperharmonic(n - 1) + [1]

    for m in range(n - 1, 0, -1):
        row[m] = (n - m + 1) * row[m] + row[m - 1]
    row[0] *= n

    return row


@MakeTriangle(hyperharmonic, "HyperHarmonic", ["A165675", "A093905", "A105954", "A165674"], True)
def HyperHarmonic(n: int, k: int) -> int:
    return hyperharmonic(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(HyperHarmonic)

''' OEIS

The traits of the HyperHarmonic triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000142 | Std-ColLeft      | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 4   | A000254 | Std-RowMax       | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) = (n+1)*a(n) + n!    |
| 5   | A000290 | Inv-DiagRow2     | The squares: a(n) = n^2                                                        |
| 6   | A000384 | Rev-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 7   | A001705 | Std-DiagCol2     | Generalized Stirling numbers: a(n) = n! * Sum_{k=0..n-1} (k+1)/(n-k)           |
| 8   | A001711 | Std-DiagCol3     | Generalized Stirling numbers                                                   |
| 9   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A002467 | Alt-TransNat0    | The game of Mousetrap with n cards (given n letters and n envelopes, how many  |
| 11  | A002522 | Inv-AltSum       | a(n) = n^2 + 1                                                                 |
| 12  | A005408 | Std-DiagRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 13  | A005563 | Inv-RowSum       | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 14  | A028387 | Inv-PolyRow2     | a(n) = n + (n+1)^2                                                             |
| 15  | A033954 | Inv:Rev-PolyRow3 | Second 10-gonal (or decagonal) numbers: n*(4*n+3)                              |
| 16  | A053506 | Inv-PolyDiag     | a(n) = (n-1)*n^(n-2)                                                           |
| 17  | A058806 | Rev-CentralO     | a(n) = n! * H_n(n) where H_0(n) = 1/n, H_m(n) = Sum_{k=1..n} H_{m-1}(k)        |
| 18  | A073577 | Inv-PosHalf      | a(n) = 4*n^2 + 4*n - 1                                                         |
| 19  | A080663 | Std-DiagRow2     | a(n) = 3*n^2 - 1                                                               |
| 20  | A082108 | Inv:Rev-TransSqr | a(n) = 4*n^2 + 6*n + 1                                                         |
| 21  | A093345 | Std-RowSum       | a(n) = n! * {1 + Sum[i=1..n, 1/i*Sum(j=0..i-1, 1/j!)]}                         |
| 22  | A099721 | Inv-RowLcm       | a(n) = n^2*(2*n+1)                                                             |
| 23  | A105954 | Std-Rev          | Array read by descending antidiagonals: A(n, k) = (n + 1)! * H(k, n + 1), wher |
| 24  | A115944 | Inv-ColLeft      | Number of partitions of n into distinct factorials                             |
| 25  | A142463 | Inv:Rev-TransNat | a(n) = 2*n^2 + 2*n - 1                                                         |
| 26  | A164897 | Inv-NegHalf      | a(n) = 4*n*(n+1) + 3                                                           |
| 27  | A165675 | Std-Triangle     | Triangle read by rows. T(n, k) = (n - k + 1)! * H(k, n - k), where H are the h |
| 28  | A165676 | Std-DiagRow3     | Fourth right hand column of triangle A16567                                    |
| 29  | A261595 | Inv-CentralO     | Triangular array T(n, k) read by rows (n >= 1, 1 <= k <= n): row n gives the l |

* Statistic about HyperHarmonic:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 29.
	all      A-numbers  : 82.
	missing  sequences  : 131.

[('missing', 131), ('A000012', 9), ('A093345', 6), ('A005408', 6), ('A000254', 6), ('A002522', 5), ('A000027', 5), ('A105954', 4), ('A165676', 3), ('A165675', 3), ('A080663', 3), ('A001711', 3), ('A001705', 3), ('A000142', 3), ('A115944', 2), ('A099721', 2), ('A073577', 2), ('A028387', 2), ('A005563', 2), ('A002378', 2), ('A000290', 2), ('A261595', 1), ('A164897', 1), ('A142463', 1), ('A082108', 1), ('A058806', 1), ('A053506', 1), ('A033954', 1), ('A002467', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/HyperHarmonic.html .
2025/01/10

'''
