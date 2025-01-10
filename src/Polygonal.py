from functools import cache
from _tabltypes import MakeTriangle

"""Polygonal numbers.

[0 ] Nonnegatives . A001477: 0,  1,  2,  3,  4,   5,   6,   7, ...
[1 ] Triangulars .. A000217: 0,  1,  3,  6, 10,  15,  21,  28, ...
[2 ] Squares ...... A000290: 0,  1,  4,  9, 16,  25,  36,  49, ...
[3 ] Pentagonals .. A000326: 0,  1,  5, 12, 22,  35,  51,  70, ...
[4 ] Hexagonals ... A000384: 0,  1,  6, 15, 28,  45,  66,  91, ...
[5 ] Heptagonals .. A000566: 0,  1,  7, 18, 34,  55,  81, 112, ...
[6 ] Octagonals ... A000567: 0,  1,  8, 21, 40,  65,  96, 133, ...
[7 ] 9-gonals ..... A001106: 0,  1,  9, 24, 46,  75, 111, 154, ...
[8 ] 10-gonals .... A001107: 0,  1, 10, 27, 52,  85, 126, 175, ...
[9 ] 11-gonals .... A051682: 0,  1, 11, 30, 58,  95, 141, 196, ...
[10] 12-gonals .... A051624: 0,  1, 12, 33, 64, 105, 156, 217, ...

Triangle view:
[0] [0]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  3]
[4] [0, 1, 4,  6,  4]
[5] [0, 1, 5,  9, 10,  5]
[6] [0, 1, 6, 12, 16, 15,  6]
[7] [0, 1, 7, 15, 22, 25, 21, 7]
"""


@cache
def polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    rov = polygonal(n - 2)
    row = polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - rov[k]
    return row


@MakeTriangle(
    polygonal, "Polygonal", ["A139600", "A057145", "A134394", "A139601"], False
)
def Polygonal(n: int, k: int) -> int:
    return polygonal(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Polygonal)

''' OEIS

The traits of the Polygonal triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-ColRight     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 4   | A000290 | Std-DiagRow2     | The squares: a(n) = n^2                                                        |
| 5   | A000326 | Std-DiagRow3     | Pentagonal numbers: a(n) = n*(3*n-1)/2                                         |
| 6   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 7   | A002061 | Rev-PolyRow3     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 8   | A005563 | Alt-AccSum       | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 9   | A005915 | Alt-PolyRow3     | Hexagonal prism numbers: a(n) = (n + 1)*(3*n^2 + 3*n + 1)                      |
| 10  | A006000 | Std-CentralE     | a(n) = (n+1)*(n^2+n+2)/2; g.f.: (1 + 2*x^2) / (1 - x)^4                        |
| 11  | A006003 | Std-CentralO     | a(n) = n*(n^2 + 1)/2                                                           |
| 12  | A008585 | Std-DiagCol3     | a(n) = 3*n                                                                     |
| 13  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 14  | A055795 | Std-RowSum       | a(n) = binomial(n,4) + binomial(n,2)                                           |
| 15  | A064808 | Rev-CentralO     | a(n) is the (n+1)st (n+2)-gonal number                                         |
| 16  | A083927 | Std-InvBinConv   | Inverse function of N -> N injection A057123                                   |
| 17  | A114890 | Std-RowGcd       | First differences of A114889                                                   |
| 18  | A139600 | Std-Triangle     | Square array T(n,k) = n*(k-1)*k/2+k, of nonnegative numbers together with poly |
| 19  | A249354 | Std-PolyRow3     | a(n) = n*(3*n^2 + 3*n + 1)                                                     |
| 20  | A360605 | Std-NegHalf      | The polygonal polynomials evaluated at x = -1/2 and normalized with (-2)^n     |
| 21  | A360606 | Std-PosHalf      | The polygonal polynomials evaluated at x = 1/2 and normalized with 2^n         |

* Statistic about Polygonal:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 21.
	all      A-numbers  : 56.
	missing  sequences  : 66.

[('missing', 66), ('A000027', 9), ('A055795', 6), ('A000012', 4), ('A360606', 3), ('A114890', 3), ('A083927', 3), ('A008585', 3), ('A006000', 3), ('A000326', 3), ('A000290', 3), ('A000217', 3), ('A360605', 2), ('A139600', 2), ('A006003', 2), ('A249354', 1), ('A064808', 1), ('A014105', 1), ('A005915', 1), ('A005563', 1), ('A002061', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Polygonal.html .
2025/01/10

'''
