from functools import cache
from _tabltypes import MakeTriangle

"""Binomial Diff Pell triangle


[0]    1;
[1]    1,    1;
[2]    3,    2,    1;
[3]    7,    9,    3,    1;
[4]   17,   28,   18,    4,    1;
[5]   41,   85,   70,   30,    5,    1;
[6]   99,  246,  255,  140,   45,    6,   1;
[7]  239,  693,  861,  595,  245,   63,   7,   1;
[8]  577, 1912, 2772, 2296, 1190,  392,  84,   8, 1;
[9] 1393, 5193, 8604, 8316, 5166, 2142, 588, 108, 9, 1;
"""


@cache
def binomialdiffpell(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arow = binomialdiffpell(n - 1)
    row = arow + [1]
    for k in range(1, n):
        row[k] = (arow[k - 1] * n) // k
    row[0] = 2 * arow[0] + binomialdiffpell(n - 2)[0]

    return row


@MakeTriangle(binomialdiffpell, "BinomialDiffPell", ["A367564"], True)
def BinomialDiffPell(n: int, k: int) -> int:
    return binomialdiffpell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialDiffPell)


''' OEIS

The traits of the BinomialDiffPell triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000217 | Inv-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 4   | A001333 | Std-ColLeft      | Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)    |
| 5   | A001541 | Std-PosHalf      | a(0) = 1, a(1) = 3; for n > 1, a(n) = 6*a(n-1) - a(n-2)                        |
| 6   | A006012 | Std-RowSum       | a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - 2*a(n-2), n >= 2                         |
| 7   | A008865 | Inv-PolyRow2     | a(n) = n^2 - 2                                                                 |
| 8   | A012816 | Inv-RowSum       | E.g.f. arctan(sec(x)*sinh(x)) (odd powers only)                                |
| 9   | A014480 | Alt-TransNat0    | Expansion of (1+2*x)/(1-2*x)^2                                                 |
| 10  | A045943 | Std-DiagRow2     | Triangular matchstick numbers: a(n) = 3*n*(n+1)/2                              |
| 11  | A056109 | Rev-PolyRow2     | Fifth spoke of a hexagonal spiral                                              |
| 12  | A059100 | Std-PolyRow2     | a(n) = n^2 + 2                                                                 |
| 13  | A077957 | Std-AltSum       | Powers of 2 alternating with zeros                                             |
| 14  | A083100 | Std-NegHalf      | a(n) = 2*a(n-1) + 7*a(n-2)                                                     |
| 15  | A083878 | Std-PolyCol2     | a(0)=1, a(1)=3, a(n) = 6*a(n-1) - 7*a(n-2), n >= 2                             |
| 16  | A083879 | Std-PolyCol3     | a(0)=1, a(1)=4, a(n) = 8*a(n-1) - 14*a(n-2), n >= 2                            |
| 17  | A084154 | Std-OddSum       | Binomial transform of sinh(x)*cosh(sqrt(2)*x)                                  |
| 18  | A088013 | Std-EvenSum      | Binomial transform of A001541 (with interpolated zeros)                        |
| 19  | A134481 | Inv-DiagRow3     | Row sums of triangle A134480                                                   |
| 20  | A367564 | Std-Triangle     | Triangular array read by rows: T(n, k) = binomial(n, k) * A001333(n - k)       |

* Statistic about BinomialDiffPell:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 20.
	all      A-numbers  : 66.
	missing  sequences  : 143.

[('missing', 143), ('A000027', 10), ('A000012', 9), ('A006012', 7), ('A001333', 5), ('A367564', 3), ('A088013', 3), ('A084154', 3), ('A077957', 3), ('A045943', 3), ('A001541', 3), ('A134481', 2), ('A083878', 2), ('A083100', 2), ('A059100', 2), ('A012816', 2), ('A008865', 2), ('A000217', 2), ('A083879', 1), ('A056109', 1), ('A014480', 1)]

A related webpage is: https://peterluschny.github.io/tabl/BinomialDiffPell.html .
2025/01/10

'''
