from functools import cache
from itertools import accumulate
from _tabltypes import MakeTriangle
from Partition import partnumexact

"""Euler's table, partition numbers at most.

[0] 1
[1] 0, 1
[2] 0, 1, 2
[3] 0, 1, 2,  3
[4] 0, 1, 3,  4,  5
[5] 0, 1, 3,  5,  6,  7
[6] 0, 1, 4,  7,  9, 10, 11
[7] 0, 1, 4,  8, 11, 13, 14, 15
[8] 0, 1, 5, 10, 15, 18, 20, 21, 22
[9] 0, 1, 5, 12, 18, 23, 26, 28, 29, 30
"""


@cache
def partnummax(n: int) -> list[int]:
    return list(accumulate(partnumexact(n)))


@MakeTriangle(partnummax, "PartitionMax", ["A026820"], False)
def PartnumMax(n: int, k: int) -> int:
    return partnummax(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(PartnumMax)

''' OEIS

The traits of the PartitionMax triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000041 | Std-RowMax       | a(n) is the number of partitions of n (the partition numbers)                  |
| 5   | A000065 | Std-DiagRow1     | -1 + number of partitions of n                                                 |
| 6   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 7   | A001399 | Std-DiagCol3     | a(n) is the number of partitions of n into at most 3 parts; also partitions of |
| 8   | A004526 | Std-DiagCol2     | Nonnegative integers repeated, floor(n/2)                                      |
| 9   | A007042 | Std-DiagRow2     | Left diagonal of partition triangle A047812                                    |
| 10  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 11  | A046682 | Std-AltSum       | Number of cycle types of conjugacy classes of all even permutations of n eleme |
| 12  | A058397 | Std-RowSum       | Row sums of partition triangle A026820                                         |
| 13  | A059100 | Rev-PolyRow3     | a(n) = n^2 + 2                                                                 |
| 14  | A067389 | Std-PolyRow3     | a(n) = 3*n^3 + 2*n^2 + n                                                       |
| 15  | A110618 | Std-DiagSum      | Number of partitions of n with no part larger than n/2. Also partitions of n i |
| 16  | A171985 | Rev-CentralO     | Number of partitions of 2*n-1 into parts not greater than n                    |
| 17  | A209816 | Std-CentralE     | Number of partitions of 2n in which every part is <n+1; also, the number of pa |
| 18  | A335323 | Std-DiagRow3     | First lower diagonal of Parker's triangle A047812                              |
| 19  | A336106 | Rev-ColMiddle    | Number of integer partitions of n whose greatest part is at most one more than |

* Statistic about PartitionMax:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 19.
	all      A-numbers  : 55.
	missing  sequences  : 70.

[('missing', 70), ('A000012', 7), ('A058397', 6), ('A000041', 6), ('A335323', 3), ('A209816', 3), ('A110618', 3), ('A046682', 3), ('A007042', 3), ('A004526', 3), ('A001399', 3), ('A000065', 3), ('A000027', 3), ('A000007', 3), ('A336106', 1), ('A171985', 1), ('A067389', 1), ('A059100', 1), ('A014105', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/PartitionMax.html .
2025/01/10

'''
