from functools import cache
from _tabltypes import MakeTriangle

"""Bell (Peirce/Aitken) triangle, (see also A182930).

[0]     1;
[1]     1,     2;
[2]     2,     3,     5;
[3]     5,     7,    10,    15;
[4]    15,    20,    27,    37,    52;
[5]    52,    67,    87,   114,   151,   203;
[6]   203,   255,   322,   409,   523,   674,   877;
[7]   877,  1080,  1335,  1657,  2066,  2589,  3263,  4140;
[8]  4140,  5017,  6097,  7432,  9089, 11155, 13744, 17007, 21147;
[9] 21147, 25287, 30304, 36401, 43833, 52922, 64077, 77821, 94828, 115975;
"""


@cache
def bell(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [bell(n - 1)[n - 1]] + bell(n - 1)
    for k in range(1, n + 1):
        row[k] += row[k - 1]
    return row


@MakeTriangle(bell, "Bell", ["A011971", "A011972", "A123346"], False)
def Bell(n: int, k: int) -> int:
    return bell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Bell)


''' OEIS

The traits of the Bell triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Rev-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000110 | Std-RowMax       | Bell or exponential numbers: number of ways to partition a set of n labeled el |
| 4   | A005408 | Std-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 5   | A005493 | Std-RowSum       | 2-Bell numbers: a(n) = number of partitions of [n+1] with a distinguished bloc |
| 6   | A011965 | Std-DiagRow2     | Second differences of Bell numbers                                             |
| 7   | A011966 | Std-DiagRow3     | Third differences of Bell numbers                                              |
| 8   | A011968 | Std-DiagCol1     | Apply (1+Shift) to Bell numbers                                                |
| 9   | A011969 | Std-DiagCol2     | Apply (1+Shift)^2 to Bell numbers                                              |
| 10  | A011970 | Std-DiagCol3     | Apply (1+Shift)^3 to Bell numbers                                              |
| 11  | A011971 | Std-Triangle     | Aitken's array: triangle of numbers {a(n,k), n >= 0, 0 <= k <= n} read by rows |
| 12  | A020556 | Std-CentralO     | Number of oriented multigraphs on n labeled arcs (without loops)               |
| 13  | A092923 | Rev-TransNat0    | Number of permutations containing exactly one occurrence of the pattern #, wit |
| 14  | A094577 | Std-CentralE     | Central Peirce numbers. Number of set partitions of {1,2,..,2n+1} in which n+1 |
| 15  | A095676 | Std-PolyCol2     | Row sums of A095675                                                            |
| 16  | A123346 | Std-Rev          | Mirror image of the Bell triangle A011971, which is also called the Pierce tri |
| 17  | A124325 | Std-AccSum       | Number of blocks of size >1 in all partitions of an n-set                      |
| 18  | A126390 | Std-BinConv      | a(n) = Sum_{i=0..n} 2^i*B(i)*binomial(n,i) where B(n) = Bell numbers A000110(n |
| 19  | A208782 | Rev-CentralO     | Number of nX2 nonnegative integer arrays with new values 0 upwards introduced  |
| 20  | A216078 | Std-ColMiddle    | Number of horizontal and antidiagonal neighbor colorings of the odd squares of |
| 21  | A216332 | Rev-ColMiddle    | Number of horizontal and antidiagonal neighbor colorings of the even squares o |
| 22  | A278677 | Std-AccRevSum    | Popularity of left children in treeshelves avoiding pattern T231               |
| 23  | A367775 | Std-AltSum       | a(n) = Sum_{k=0..n} (-1)^(n - k) * A011971(n, k)                               |
| 24  | A367808 | Std-PosHalf      | a(n) = Sum_{k=0..n} A011971(n, k) * 2^(n - k)                                  |
| 25  | A367809 | Std-NegHalf      | a(n) = Sum_{k=0..n} A011971(n, k) * (-2)^(n - k)                               |

* Statistic about Bell:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 25.
	all      A-numbers  : 74.
	missing  sequences  : 49.

[('missing', 49), ('A005493', 9), ('A000110', 9), ('A000012', 4), ('A367808', 3), ('A367775', 3), ('A278677', 3), ('A126390', 3), ('A124325', 3), ('A123346', 3), ('A094577', 3), ('A011970', 3), ('A011969', 3), ('A011968', 3), ('A011966', 3), ('A011965', 3), ('A367809', 2), ('A216078', 2), ('A095676', 2), ('A020556', 2), ('A011971', 2), ('A005408', 2), ('A216332', 1), ('A208782', 1), ('A092923', 1), ('A000027', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Bell.html .
2025/01/10

'''
