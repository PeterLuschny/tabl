from functools import cache
from _tabltypes import MakeTriangle

"""Central cycle factorial numbers.

[0] [1]
[1] [0,    1]
[2] [0,    2,     3]
[3] [0,    6,    20,     15]
[4] [0,   24,   130,    210,    105]
[5] [0,  120,   924,   2380,   2520,    945]
[6] [0,  720,  7308,  26432,  44100,  34650,  10395]
[7] [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135]
"""


@cache
def centralcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = centralcycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])

    return row


@MakeTriangle(centralcycle, "CentralCycle", ["A269940", "A111999", "A259456"], False)
def CentralCycle(n: int, k: int) -> int:
    return centralcycle(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CentralCycle)


''' OEIS

The traits of the CentralCycle triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-DiagCol1     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000166 | Std-DiagSum      | Subfactorial or rencontres numbers, or derangements: number of permutations of |
| 6   | A000276 | Std-DiagCol2     | Associated Stirling numbers                                                    |
| 7   | A000295 | Alt-TransNat0    | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1 of A1730 |
| 8   | A000325 | Alt-AccRevSum    | a(n) = 2^n - n                                                                 |
| 9   | A000483 | Std-DiagCol3     | Associated Stirling numbers: second-order reciprocal Stirling numbers (Fekete) |
| 10  | A000567 | Alt-PolyRow2     | Octagonal numbers: n*(3*n-2). Also called star numbers                         |
| 11  | A000906 | Std-DiagRow1     | Exponential generating function: 2*(1+3*x)/(1-2*x)^(7/2)                       |
| 12  | A000907 | Std-DiagRow2     | Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+2, n]]. The numbe |
| 13  | A001147 | Std-ColRight     | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 14  | A001662 | Std-NegHalf      | Coefficients of Airey's converging factor                                      |
| 15  | A001784 | Std-DiagRow3     | Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+3, n]]. The numbe |
| 16  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 17  | A006351 | Alt-PolyCol2     | Number of series-parallel networks with n labeled edges. Also called yoke-chai |
| 18  | A032188 | Std-RowSum       | Number of labeled series-reduced mobiles (circular rooted trees) with n leaves |
| 19  | A045944 | Std-PolyRow2     | Rhombic matchstick numbers: a(n) = n*(3*n+2)                                   |
| 20  | A058562 | Alt-PolyCol3     | Another 3-way generalization of series-parallel networks with n labeled edges  |
| 21  | A070313 | Alt-AccSum       | a(n) = 2^n - (2*n+1)                                                           |
| 22  | A106828 | Std-AntiDiag     | Triangle T(n,k) read by rows: associated Stirling numbers of first kind (n >=  |
| 23  | A239325 | Rev-PolyRow3     | a(n) = 6*n^2 + 8*n + 1                                                         |
| 24  | A269940 | Std-Triangle     | Triangle read by rows, T(n, k) = Sum_{m=0..k} (-1)^(m + k)*binomial(n + k, n + |

* Statistic about CentralCycle:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 24.
	all      A-numbers  : 55.
	missing  sequences  : 66.

[('missing', 66), ('A032188', 6), ('A000012', 5), ('A001784', 3), ('A001147', 3), ('A000907', 3), ('A000906', 3), ('A000483', 3), ('A000276', 3), ('A000142', 3), ('A000027', 3), ('A000007', 3), ('A106828', 2), ('A006351', 2), ('A001662', 2), ('A000325', 2), ('A269940', 1), ('A239325', 1), ('A070313', 1), ('A058562', 1), ('A045944', 1), ('A005408', 1), ('A000567', 1), ('A000295', 1), ('A000166', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CentralCycle.html .
2025/01/10

'''