from functools import cache
from _tabltypes import MakeTriangle

"""Stirling cycle numbers of second order.

[0]  1
[1]  0,     0
[2]  0,     1,     0
[3]  0,     2,     0,     0
[4]  0,     6,     3,     0,    0
[5]  0,    24,    20,     0,    0, 0
[6]  0,   120,   130,    15,    0, 0, 0
[7]  0,   720,   924,   210,    0, 0, 0, 0
[8]  0,  5040,  7308,  2380,  105, 0, 0, 0, 0
[9]  0, 40320, 64224, 26432, 2520, 0, 0, 0, 0, 0
"""


@cache
def stirlingcycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov = stirlingcycle2(n - 2)
    row = stirlingcycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


@MakeTriangle(
    stirlingcycle2, "StirlingCycle2", ["A358622", "A008306", "A106828"], False
)
def StirlingCycle2(n: int, k: int) -> int:
    return stirlingcycle2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingCycle2)


''' OEIS

The traits of the StirlingCyc2 triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000027 | Std-AltSum       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000142 | Std-DiagCol1     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 4   | A000166 | Std-RowSum       | Subfactorial or rencontres numbers, or derangements: number of permutations of |
| 5   | A000276 | Std-DiagCol2     | Associated Stirling numbers                                                    |
| 6   | A000387 | Rev-OddSum       | Rencontres numbers: number of permutations of [n] with exactly two fixed point |
| 7   | A000483 | Std-DiagCol3     | Associated Stirling numbers: second-order reciprocal Stirling numbers (Fekete) |
| 8   | A000906 | Std-CentralO     | Exponential generating function: 2*(1+3*x)/(1-2*x)^(7/2)                       |
| 9   | A001105 | Rev-PolyRow3     | a(n) = 2*n^2                                                                   |
| 10  | A001147 | Std-CentralE     | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 11  | A003221 | Rev-EvenSum      | Number of even permutations of length n with no fixed points                   |
| 12  | A005843 | Std-PolyRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 13  | A033030 | Rev-PolyCol3     | Derangement numbers d(n,3) where d(n,k) = k(n-1)(d(n-1,k) + d(n-2,k)), with d( |
| 14  | A053871 | Std-PosHalf      | a(0)=1; a(1)=0; a(n) = 2*(n-1)*(a(n-1) + a(n-2))                               |
| 15  | A055142 | Std-NegHalf      | Expansion of e.g.f.: exp(x)*sqrt(1-2x)                                         |
| 16  | A063524 | Std-DiagRow1     | Characteristic function of 1                                                   |
| 17  | A087981 | Std-PolyCol2     | E.g.f.: exp(-2*x) / (1-x)^2                                                    |
| 18  | A123023 | Rev-ColMiddle    | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 19  | A137775 | Std-PolyCol3     | Number of triples of permutations on n letters such that for each j, exactly o |
| 20  | A162973 | Std-TransNat0    | Number of cycles in all derangement permutations of {1,2,...,n}                |
| 21  | A216778 | Std-EvenSum      | Number of derangements on n elements with an even number of cycles             |
| 22  | A216779 | Std-OddSum       | Number of derangements on n elements with an odd number of cycles              |
| 23  | A277423 | Alt-PolyDiag     | a(n) = n!*LaguerreL(n, n)                                                      |
| 24  | A295182 | Std-PolyDiag     | a(n) = n! * [x^n] exp(-n*x)/(1 - x)^n                                          |
| 25  | A358622 | Std-Triangle     | Regular triangle read by rows. T(n, k) = [[n, k]], where [[n, k]] are the seco |

* Statistic about StirlingCyc2:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 25.
	all      A-numbers  : 62.
	missing  sequences  : 59.

[('missing', 59), ('A000027', 9), ('A000166', 6), ('A000007', 6), ('A063524', 3), ('A053871', 3), ('A001147', 3), ('A000483', 3), ('A000276', 3), ('A000142', 3), ('A358622', 2), ('A216779', 2), ('A216778', 2), ('A087981', 2), ('A055142', 2), ('A005843', 2), ('A000906', 2), ('A295182', 1), ('A277423', 1), ('A162973', 1), ('A137775', 1), ('A123023', 1), ('A033030', 1), ('A003221', 1), ('A001105', 1), ('A000387', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingCyc2.html .
2025/01/10

'''
