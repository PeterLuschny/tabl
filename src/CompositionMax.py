from functools import cache
from _tabltypes import MakeTriangle

"""Compositions of n into at most k parts.

[0] 1;
[1] 0, 1;
[2] 0, 1,  2;
[3] 0, 1,  3,   4;
[4] 0, 1,  5,   7,   8;
[5] 0, 1,  8,  13,  15,  16;
[6] 0, 1, 13,  24,  29,  31,  32;
[7] 0, 1, 21,  44,  56,  61,  63,  64;
[8] 0, 1, 34,  81, 108, 120, 125, 127, 128;
[9] 0, 1, 55, 149, 208, 236, 248, 253, 255, 256;
"""


@cache
def compomax(n: int) -> list[int]:
    @cache
    def t(n: int, k: int) -> int:
        if n == 0 or k == 1:
            return 1
        return sum(t(n - j, k) for j in range(1, min(n, k) + 1))

    return [t(n, k) for k in range(n + 1)]


@MakeTriangle(compomax, "CompositionMax", ["A126198"], False)
def CompoMax(n: int, k: int) -> int:
    return compomax(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CompoMax, 8, True)

''' OEIS

The traits of the CompositionMax triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000045 | Std-DiagCol2     | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 5   | A000073 | Std-DiagCol3     | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with a(0) = a(1 |
| 6   | A000079 | Std-RowMax       | Powers of 2: a(n) = 2^n                                                        |
| 7   | A000225 | Std-DiagRow1     | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 8   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 9   | A008464 | Std-CentralE     | a(n) = 2^(2n+3) - 2^n*(n+3)                                                    |
| 10  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 11  | A014206 | Rev-PolyRow3     | a(n) = n^2 + n + 2                                                             |
| 12  | A036563 | Std-DiagRow2     | a(n) = 2^n - 3                                                                 |
| 13  | A039671 | Std-RowSum       | Row sums up to the main diagonal of the "postage stamp" array (n,m >= 0) defin |
| 14  | A100575 | Std-CentralO     | Half the number of permutations of 0..n with exactly two maxima                |
| 15  | A159741 | Std-DiagRow3     | a(n) = 8*(2^n - 1)                                                             |
| 16  | A336103 | Rev-ColMiddle    | Number of separable multisets of size n covering an initial interval of positi |
| 17  | A368484 | Std-ColMiddle    | Number of compositions (ordered partitions) of n into parts not greater than n |

* Statistic about CompositionMax:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 17.
	all      A-numbers  : 51.
	missing  sequences  : 74.

[('missing', 74), ('A000012', 7), ('A039671', 6), ('A000079', 6), ('A159741', 3), ('A036563', 3), ('A008464', 3), ('A000225', 3), ('A000073', 3), ('A000045', 3), ('A000027', 3), ('A000007', 3), ('A368484', 2), ('A100575', 2), ('A336103', 1), ('A014206', 1), ('A014105', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CompositionMax.html .
2025/01/10

'''
