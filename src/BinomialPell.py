from functools import cache
from _tabltypes import MakeTriangle

"""Binomial Pell triangle


[0]   1
[1]   2     2
[2]   5     6    3
[3]  12    20    12     4
[4]  29    60    50    20     5
[5]  70   174   180   100    30     6
[6] 169   490   609   420   175    42   7
[7] 408  1352  1960  1624   840   280   56   8
[8] 985  3672  6084  5880  3654  1512  420  72  9
"""


@cache
def binomialpell(n: int) -> list[int]:

    if n == 0:
        return [1]
    if n == 1:
        return [2, 2]

    arow = binomialpell(n - 1)
    row = arow + [n + 1]
    for k in range(1, n):
        row[k] = (arow[k - 1] * (n + 1)) // k
    row[0] = 2 * arow[0] + binomialpell(n - 2)[0]

    return row


@MakeTriangle(binomialpell, "BinomialPell", ["A367211"], True)
def BinomialPell(n: int, k: int) -> int:
    return binomialpell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialPell)

''' OEIS

The traits of the BinomialPell triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000027 | Std-ColRight     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 2   | A000129 | Std-ColLeft      | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 3   | A001109 | Std-PosHalf      | a(n)^2 is a triangular number: a(n) = 6*a(n-1) - a(n-2) with a(0)=0, a(1)=1    |
| 4   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 5   | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 6   | A005918 | Std-PolyRow2     | Number of points on surface of square pyramid: 3*n^2 + 2 (n>0)                 |
| 7   | A006519 | Std-RowGcd       | Highest power of 2 dividing n                                                  |
| 8   | A007070 | Std-RowSum       | a(n) = 4*a(n-1) - 2*a(n-2) with a(0) = 1, a(1) = 4                             |
| 9   | A015519 | Std-NegHalf      | a(n) = 2*a(n-1) + 7*a(n-2), with a(0) = 0, a(1) = 1                            |
| 10  | A033486 | Std-DiagRow3     | a(n) = n*(n + 1)*(n + 2)*(n + 3)/2                                             |
| 11  | A036289 | Alt-TransNat0    | a(n) = n*2^n                                                                   |
| 12  | A077957 | Std-AltSum       | Powers of 2 alternating with zeros                                             |
| 13  | A081179 | Std-PolyCol2     | 3rd binomial transform of (0,1,0,2,0,4,0,8,0,16,...)                           |
| 14  | A081180 | Std-PolyCol3     | 4th binomial transform of (0,1,0,2,0,4,0,8,0,16,...)                           |
| 15  | A093968 | Alt-AccSum       | Inverse binomial transform of n*Pell(n)                                        |
| 16  | A094038 | Std-EvenSum      | Binomial transform of (Pell(-n)+Pell(n))/2                                     |
| 17  | A099626 | Std-DiagSum      | A transform of the Pell numbers                                                |
| 18  | A112575 | Alt-DiagSum      | Chebyshev transform of the second kind of the Pell numbers                     |
| 19  | A134481 | Std-DiagRow2     | Row sums of triangle A134480                                                   |
| 20  | A190331 | Rev-PolyCol3     | a(n) = 8*a(n-1) + 2*a(n-2), with a(0)=0, a(1)=1                                |
| 21  | A292022 | Std-PolyRow3     | a(n) = 4n(n^2+2)                                                               |
| 22  | A361732 | Std-DiagCol1     | a(n) = [x^n] (x^5 + 5*x^4 + 4*x^3 - 3*x + 1)/(x^2 + 2*x - 1)^2                 |
| 23  | A367211 | Std-Triangle     | Triangular array T(n,k), read by rows: coefficients of strong divisibility seq |

* Statistic about BinomialPell:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 23.
	all      A-numbers  : 58.
	missing  sequences  : 67.

[('missing', 67), ('A007070', 7), ('A000129', 5), ('A361732', 3), ('A134481', 3), ('A094038', 3), ('A077957', 3), ('A033486', 3), ('A006519', 3), ('A005843', 3), ('A002378', 3), ('A001109', 3), ('A000027', 3), ('A367211', 2), ('A292022', 2), ('A081179', 2), ('A015519', 2), ('A005918', 2), ('A190331', 1), ('A112575', 1), ('A099626', 1), ('A093968', 1), ('A081180', 1), ('A036289', 1)]

A related webpage is: https://peterluschny.github.io/tabl/BinomialPell.html .
2025/01/10

'''
