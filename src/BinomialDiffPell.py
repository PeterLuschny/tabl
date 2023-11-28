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

'''* Statistic about BinomialDiffPell:

The number of ...
        all      hashes    is 203.
        distinct hashes    is 111.
        core     triangles is 1.
        distinct types     is 5.
        missing  sequences is 149.
        all      A-numbers is 54.
        distinct A-numbers is 22.

The traits of the BinomialDiffPell triangle as represented in the OEIS.

|     | A-number | trait            | A-name                                                                    |
| --- | -------- | ---------------- | --------------------------------------------------------------------------|
| 1   | A000027  | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers |
| 2   | A001333  | Std-ColLeft      | Numerators of continued fraction convergents to sqrt(2)                   |
| 3   | A001541  | Std-PosHalf      | a(0) = 1, a(1) = 3; for n > 1, a(n) = 6*a(n-1) - a(n-2)                   |
| 4   | A006012  | Std-RowSum       | a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - 2*a(n-2), n >= 2                    |
| 5   | A008865  | Inv:Rev-PolyRow2 | a(n) = n^2 - 2                                                            |
| 6   | A011973  | Inv:Rev-AntiDiag | Irregular triangle of numbers read by rows: {binomial(n-k, k), n >= 0, 0  |
| 7   | A023443  | Alt-PolyRow1     | a(n) = n - 1                                                              |
| 8   | A025731  | Inv-DiagRow2     | Index of 8^n within sequence of numbers of form 7^i*8^j                   |
| 9   | A056109  | Rev-PolyRow2     | Fifth spoke of a hexagonal spiral                                         |
| 10  | A059100  | Alt-PolyRow2     | a(n) = n^2 + 2                                                            |
| 11  | A077957  | Std-AltSum       | Powers of 2 alternating with zeros                                        |
| 12  | A083878  | Std-PolyCol2     | a(0)=1, a(1)=3, a(n) = 6*a(n-1) - 7*a(n-2), n >= 2                        |
| 13  | A083879  | Std-PolyCol3     | a(0)=1, a(1)=4, a(n) = 8*a(n-1) - 14*a(n-2), n >= 2                       |
| 14  | A084058  | Std-NegHalf      | a(n) = 2*a(n-1) + 7*a(n-2) for n>1, a(0)=1, a(1)=1                        |
| 15  | A084154  | Std-OddSum       | Binomial transform of sinh(x)*cosh(sqrt(2)*x)                             |
| 16  | A088013  | Std-EvenSum      | Binomial transform of A001541 (with interpolated zeros)                   |
| 17  | A183199  | Std-PolyRow2     | Least integer k such that Floor(k*f(n+1)>k*f(n), where f(n)=(n^2)/(1+n^2) |
| 18  | A329684  | Inv-RowGcd       | Number of excursions of length n with Motzkin-steps forbidding all consec |
| 19  | B008865  | Inv-PolyRow2     | a(n) = n^2 - 2                                                            |
| 20  | B045943  | Std-DiagRow2     | Triangular matchstick numbers: a(n) = 3*n*(n+1)/2                         |
| 21  | B134481  | Inv-DiagRow3     | Row sums of triangle A134480                                              |
| 22  | B367564  | Std-Triangle     | Triangular array read by rows: T(n, k) = binomial(n, k) * A001333(n - k)  |
'''
