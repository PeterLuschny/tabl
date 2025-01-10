from functools import cache
from _tabltypes import MakeTriangle

"""Lah numbers (unsigned).


[0]  1
[1]  0       1
[2]  0       2        1
[3]  0       6        6        1
[4]  0      24       36       12        1
[5]  0     120      240      120       20       1
[6]  0     720     1800     1200      300      30      1
[7]  0    5040    15120    12600     4200     630     42     1
[8]  0   40320   141120   141120    58800   11760   1176    56    1
[9]  0  362880  1451520  1693440   846720  211680  28224  2016   72   1
"""


@cache
def lah(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row


@MakeTriangle(
    lah, "Lah", ["A271703", "A008297", "A066667", "A089231", "A105278", "A111596"], True
)
def Lah(n: int, k: int) -> int:
    return lah(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Lah)

''' OEIS

The traits of the Lah triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-DiagCol1     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000262 | Std-RowSum       | Number of "sets of lists": number of partitions of {1,...,n} into any number o |
| 6   | A001053 | Std-DiagSum      | a(n+1) = n*a(n) + a(n-1) with a(0)=1, a(1)=0                                   |
| 7   | A001286 | Std-DiagCol2     | Lah numbers: a(n) = (n-1)*n!/2                                                 |
| 8   | A001754 | Std-DiagCol3     | Lah numbers: a(n) = n!*binomial(n-1,2)/6                                       |
| 9   | A002378 | Std-RowGcd       | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A002720 | Std-AccRevSum    | Number of partial permutations of an n-set; number of n X n binary matrices wi |
| 11  | A002868 | Std-RowMax       | Largest number in n-th row of triangle of Lah numbers (A008297 and A271703)    |
| 12  | A003154 | Rev-PolyRow3     | Centered 12-gonal numbers, or centered dodecagonal numbers: numbers of the for |
| 13  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 14  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 15  | A025168 | Std-PosHalf      | Expansion of e.g.f.: exp(x/(1-2*x))                                            |
| 16  | A052852 | Std-TransNat0    | Expansion of e.g.f.: (x/(1-x))*exp(x/(1-x))                                    |
| 17  | A052897 | Std-PolyCol2     | Expansion of e.g.f.: exp(2*x/(1-x))                                            |
| 18  | A058798 | Alt-DiagSum      | a(n) = n*a(n-1) - a(n-2) with a(0) = 0, a(1) = 1                               |
| 19  | A062147 | Std-AccSum       | Row sums of unsigned triangle A062137 (generalized a=3 Laguerre)               |
| 20  | A083374 | Std-DiagRow2     | a(n) = n^2 * (n^2 - 1)/2                                                       |
| 21  | A088312 | Std-EvenSum      | Number of sets of lists (cf. A000262) with even number of lists                |
| 22  | A088313 | Std-OddSum       | Number of "sets of lists" (cf. A000262) with an odd number of lists            |
| 23  | A096939 | Rev-OddSum       | Number of sets of odd number of even lists, cf. A000262                        |
| 24  | A096965 | Rev-EvenSum      | Number of sets of even number of even lists, cf. A000262                       |
| 25  | A103194 | Std-TransSqrs    | LAH transform of squares                                                       |
| 26  | A111884 | Std-AltSum       | E.g.f.: exp(x/(1+x))                                                           |
| 27  | A180047 | Std-AntiDiag     | Coefficient triangle of the numerators of the (n-th convergents to) the contin |
| 28  | A187535 | Std-CentralE     | Central Lah numbers: a(n) = A105278(2*n,n) = A008297(2*n,n)                    |
| 29  | A202410 | Alt-AccRevSum    | Inverse Lah transform of 1,2,3,...; e.g.f. exp(x/(x-1))*(2*x-1)/(x-1)          |
| 30  | A226514 | Std-PolyRow3     | Column 3 of array in A226513                                                   |
| 31  | A248045 | Rev-CentralO     | (2*(n-1))! * (2*n-1)! / (n * (n-1)!^3)                                         |
| 32  | A253285 | Std-DiagRow3     | a(n) = RF(n+1,3)*C(n+2,n-1), where RF(a,n) is the rising factorial             |
| 33  | A253286 | Std-Poly         | Square array read by upward antidiagonals, A(n,k) = Sum_{j=0..n} (n-j)!*C(n,n- |
| 34  | A255806 | Std-PolyCol3     | Expansion of e.g.f.: exp(Sum_{k>=1} 3*x^k)                                     |
| 35  | A256467 | Alt-TransSqrs    | Inverse Lah transform of the squares                                           |
| 36  | A271703 | Std-Triangle     | Triangle read by rows: the unsigned Lah numbers T(n, k) = binomial(n-1, k-1)*n |
| 37  | A293145 | Std-PolyDiag     | a(n) = n! * [x^n] exp(n*x/(1 - x))                                             |
| 38  | A293146 | Rev-PolyDiag     | a(n) = n! * [x^n] exp(x/(1 - n*x))                                             |
| 39  | A317279 | Alt-PolyDiag     | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n-1,k-1)*n^k*n!/k!                     |
| 40  | A317364 | Alt-PolyCol2     | Expansion of e.g.f. exp(2*x/(1 + x))                                           |
| 41  | A317365 | Alt-TransNat0    | Expansion of e.g.f. x*exp(x/(1 + x))/(1 + x)                                   |
| 42  | A318223 | Std-NegHalf      | Expansion of e.g.f. exp(x/(1 + 2*x))                                           |
| 43  | A318224 | Inv:Rev-PolyDiag | a(n) = n! * [x^n] exp(x/(1 + n*x))                                             |
| 44  | A321837 | Rev-PolyCol3     | Expansion of e.g.f.: exp(x/(1-3*x))                                            |
| 45  | A343581 | Std-ColMiddle    | a(n) = binomial(n, floor(n/2))*FallingFactorial(n - 1, n - floor(n/2))         |
| 46  | A344050 | Std-InvBinConv   | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n, k)*|Lah(n, k)|. Inverse binomial co |
| 47  | A344051 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*|Lah(n, k)|. Binomial convolution of the un |
| 48  | A349776 | Std-Acc          | Triangle read by rows: T(n,k) is the number of partitions of set [n] into a se |
| 49  | A359365 | Std-RowLcm       | a(n) = lcm([ n!*binomial(n-1, m-1) / m! for m = 1..n ]) with a(0) = 1          |
| 50  | A360205 | Std-Diffx1       | Triangle read by rows. T(n, k) = (-1)^(n-k)*(k+1)*binomial(n, k)*pochhammer(1- |
| 51  | A367776 | Std-CentralO     | a(n) = binomial(2*n, n - 1)*(2*n + 1)! / n!                                    |

* Statistic about Lah:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 51.
	all      A-numbers  : 173.
	missing  sequences  : 42.

[('missing', 42), ('A002378', 10), ('A000262', 10), ('A271703', 7), ('A000012', 6), ('A359365', 5), ('A344051', 5), ('A344050', 5), ('A253285', 5), ('A202410', 5), ('A187535', 5), ('A111884', 5), ('A083374', 5), ('A002868', 5), ('A001754', 5), ('A001286', 5), ('A000142', 5), ('A000007', 5), ('A318223', 4), ('A317364', 4), ('A025168', 4), ('A367776', 3), ('A360205', 3), ('A343581', 3), ('A180047', 3), ('A088313', 3), ('A088312', 3), ('A062147', 3), ('A052897', 3), ('A005563', 3), ('A002720', 3), ('A000027', 3), ('A349776', 2), ('A317365', 2), ('A317279', 2), ('A256467', 2), ('A248045', 2), ('A096965', 2), ('A096939', 2), ('A005408', 2), ('A003154', 2), ('A001053', 2), ('A321837', 1), ('A318224', 1), ('A293146', 1), ('A293145', 1), ('A255806', 1), ('A253286', 1), ('A226514', 1), ('A103194', 1), ('A058798', 1), ('A052852', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Lah.html .
2025/01/10

'''
