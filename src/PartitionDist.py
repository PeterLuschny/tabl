from functools import cache
from _tabltypes import MakeTriangle

"""Partitions of n having exactly k distinct parts, A365676.

[0] 1;
[1] 0, 1;
[2] 0, 2,  0;
[3] 0, 2,  1,  0;
[4] 0, 3,  2,  0, 0;
[5] 0, 2,  5,  0, 0, 0;
[6] 0, 4,  6,  1, 0, 0, 0;
[7] 0, 2, 11,  2, 0, 0, 0, 0;
[8] 0, 4, 13,  5, 0, 0, 0, 0, 0;
[9] 0, 3, 17, 10, 0, 0, 0, 0, 0, 0;
"""


@cache
def _pdist(n: int, k: int, r: int) -> int:
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0 or r == 0:
        return 0
    return (sum(_pdist(n - r * j, k - 1, r - 1) for j in range(1, n // r + 1))
           + _pdist(n, k, r - 1))


@cache
def partnumdist(n: int) -> list[int]:
    return [_pdist(n, k, n) for k in range(n + 1)]


@MakeTriangle(partnumdist, "PartitionDist", ["A365676", "A116608", "A060177"], False)
def PartnumDist(n: int, k: int) -> int:
    return partnumdist(n)[k]


if __name__ == "__main__":
    # TablTest has to big test cases
    from _tablviews import PrintViews

    PrintViews(PartnumDist, 10)

''' OEIS

The traits of the PartitionDist triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000005 | Std-DiagCol1     | d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n           |
| 2   | A000007 | Std-CentralE     | The characteristic function of {0}: a(n) = 0^n                                 |
| 3   | A000012 | Rev-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 4   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 5   | A000038 | Std-CentralO     | Twice A000007                                                                  |
| 6   | A000041 | Std-RowSum       | a(n) is the number of partitions of n (the partition numbers)                  |
| 7   | A000070 | Std-AccRevSum    | a(n) = Sum_{k=0..n} p(k) where p(k) = number of partitions of k (A000041)      |
| 8   | A002133 | Std-DiagCol2     | Number of partitions of n with exactly two part sizes                          |
| 9   | A002134 | Std-DiagCol3     | Generalized divisor function. Number of partitions of n with exactly three par |
| 10  | A005563 | Std-PolyRow3     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 11  | A005843 | Std-PolyRow2     | The nonnegative even numbers: a(n) = 2n                                        |
| 12  | A006996 | Std-DiagRow1     | a(n) = C(2n,n) mod 3                                                           |
| 13  | A014105 | Rev-PolyRow3     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 14  | A015128 | Std-PolyCol2     | Number of overpartitions of n: an overpartition of n is an ordered sequence of |
| 15  | A019590 | Std-ColRight     | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 16  | A048793 | Alt-ColMiddle    | List giving all subsets of natural numbers arranged in standard statistical (o |
| 17  | A090794 | Std-OddSum       | Number of partitions of n such that the number of different parts is odd       |
| 18  | A092037 | Std-DiagRow2     | A092255 mod 3                                                                  |
| 19  | A092306 | Std-EvenSum      | Number of partitions of n such that the set of parts has an even number of ele |
| 20  | A104575 | Std-AltSum       | Alternating sum of diagonals in A060177                                        |
| 21  | A135348 | Std-TransSqrs    | Total sum of squares of number of distinct parts in all partitions of n        |
| 22  | A194552 | Rev-TransNat0    | Sum of all parts > 1 of all partitions of n                                    |
| 23  | A264686 | Std-PolyCol3     | Expansion of Product_{k>=1} (1 + 2*x^k)/(1 - x^k)                              |
| 24  | A321880 | Std-PolyDiag     | Number of partitions of n into colored blocks of equal parts with colors from  |
| 25  | A365675 | Std-AccSum       | a(n) = Sum_{k=0..n} p(k) where the p(k) are the partial sums of row n of A3656 |
| 26  | A365676 | Std-Triangle     | Triangle read by rows: T(n, k) is the number of partitions of n having exactly |

* Statistic about PartitionDist:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 26.
	all      A-numbers  : 65.
	missing  sequences  : 57.

[('missing', 57), ('A000007', 8), ('A000041', 6), ('A000070', 4), ('A365675', 3), ('A104575', 3), ('A019590', 3), ('A006996', 3), ('A005843', 3), ('A002134', 3), ('A002133', 3), ('A000005', 3), ('A365676', 2), ('A092306', 2), ('A092037', 2), ('A090794', 2), ('A015128', 2), ('A005563', 2), ('A000038', 2), ('A000027', 2), ('A321880', 1), ('A264686', 1), ('A194552', 1), ('A135348', 1), ('A048793', 1), ('A014105', 1), ('A000012', 1)]

A related webpage is: https://peterluschny.github.io/tabl/PartitionDist.html .
2025/01/10

'''
