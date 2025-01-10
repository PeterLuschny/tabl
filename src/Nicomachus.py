from functools import cache
from _tabltypes import MakeTriangle

"""Nicomachus triangle.

[0] [  1]
[1] [  2,   3]
[2] [  4,   6,   9]
[3] [  8,  12,  18,  27]
[4] [ 16,  24,  36,  54,  81]
[5] [ 32,  48,  72, 108, 162, 243]
[6] [ 64,  96, 144, 216, 324, 486,  729]
[7] [128, 192, 288, 432, 648, 972, 1458, 2187]
"""


@cache
def nicomachus(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = nicomachus(n - 1) + [3 * nicomachus(n - 1)[n - 1]]
    for k in range(0, n):
        row[k] *= 2
    return row


@MakeTriangle(nicomachus, "Nicomachus", ["A036561", "A081954", "A175840"], False)
def Nicomachus(n: int, k: int) -> int:
    return nicomachus(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Nicomachus)

''' OEIS

The traits of the Nicomachus triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000079 | Std-ColLeft      | Powers of 2: a(n) = 2^n                                                        |
| 3   | A000244 | Std-RowMax       | Powers of 3: a(n) = 3^n                                                        |
| 4   | A000351 | Std-BinConv      | Powers of 5: a(n) = 5^n                                                        |
| 5   | A000400 | Std-RowLcm       | Powers of 6: a(n) = 6^n                                                        |
| 6   | A001047 | Std-RowSum       | a(n) = 3^n - 2^n                                                               |
| 7   | A003946 | Std-DiagRow2     | Expansion of (1+x)/(1-3*x)                                                     |
| 8   | A005010 | Std-DiagCol2     | a(n) = 9*2^n                                                                   |
| 9   | A005051 | Std-DiagRow3     | a(n) = 8*3^n                                                                   |
| 10  | A005061 | Std-PosHalf      | a(n) = 4^n - 3^n                                                               |
| 11  | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A007283 | Std-DiagCol1     | a(n) = 3*2^n                                                                   |
| 13  | A008776 | Std-DiagRow1     | Pisot sequences E(2,6), L(2,6), P(2,6), T(2,6)                                 |
| 14  | A015441 | Std-AltSum       | Generalized Fibonacci numbers                                                  |
| 15  | A016129 | Std-PolyCol2     | Expansion of 1/((1-2*x)*(1-6*x))                                               |
| 16  | A016133 | Std-PolyCol3     | Expansion of 1/((1-2*x)*(1-9*x))                                               |
| 17  | A016137 | Rev-PolyCol3     | Expansion of 1/((1-3*x)*(1-6*x))                                               |
| 18  | A016777 | Alt-PolyRow1     | a(n) = 3*n + 1                                                                 |
| 19  | A016789 | Std-PolyRow1     | a(n) = 3*n + 2                                                                 |
| 20  | A026532 | Rev-ColMiddle    | Ratios of successive terms are 3, 2, 3, 2, 3, 2, 3, 2, ..                      |
| 21  | A026549 | Std-ColMiddle    | Ratios of successive terms are 2, 3, 2, 3, 2, 3, 2, 3, ..                      |
| 22  | A036561 | Std-Triangle     | Nicomachus triangle read by rows, T(n, k) = 2^(n - k)*3^k, for 0 <= k <= n     |
| 23  | A053404 | Std-NegHalf      | Expansion of 1/((1+3*x)*(1-4*x))                                               |
| 24  | A053524 | Alt-PolyCol2     | a(n) = (6^n - (-2)^n)/8                                                        |
| 25  | A066810 | Std-AccSum       | Expansion of x^2/((1-3*x)*(1-2*x)^2)                                           |
| 26  | A081341 | Rev-CentralO     | Expansion of exp(3*x)*cosh(3*x)                                                |
| 27  | A135247 | Rev-DiagSum      | a(n) = 3*a(n-1) + 2*a(n-2) - 6*a(n-3)                                          |
| 28  | A167747 | Std-CentralO     | a(n) = phi(6^n)                                                                |
| 29  | A167762 | Std-DiagSum      | a(n) = 2*a(n-1)+3*a(n-2)-6*a(n-3) starting a(0)=a(1)=0, a(2)=1                 |
| 30  | A167910 | Rev-EvenSum      | a(n) = (4*3^n - 5*2^n + (-2)^n)/20                                             |
| 31  | A175806 | Std-DiagCol3     | a(n) = 27*2^n                                                                  |
| 32  | A175840 | Std-Rev          | Mirror image of Nicomachus' table: T(n,k) = 3^(n-k)*2^k for n>=0 and 0<=k<=n   |
| 33  | A230435 | Std-Acc          | Triangle by rows, A001047 convolved with A000079                               |

* Statistic about Nicomachus:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 33.
	all      A-numbers  : 82.
	missing  sequences  : 41.

[('missing', 41), ('A001047', 6), ('A000400', 6), ('A000244', 6), ('A000012', 4), ('A175840', 3), ('A175806', 3), ('A066810', 3), ('A015441', 3), ('A008776', 3), ('A007283', 3), ('A005061', 3), ('A005051', 3), ('A005010', 3), ('A003946', 3), ('A000351', 3), ('A000079', 3), ('A230435', 2), ('A167747', 2), ('A053524', 2), ('A053404', 2), ('A036561', 2), ('A026549', 2), ('A016129', 2), ('A167910', 1), ('A167762', 1), ('A135247', 1), ('A081341', 1), ('A026532', 1), ('A016789', 1), ('A016777', 1), ('A016137', 1), ('A016133', 1), ('A005408', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Nicomachus.html .
2025/01/10

'''
