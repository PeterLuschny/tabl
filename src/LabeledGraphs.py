from functools import cache
from Binomial import Binomial
from _tabltypes import MakeTriangle

"""Labeled graphs.

[0] 1;
[1] 0,       1;
[2] 0,       1,      1;
[3] 0,       2,      2,     4;
[4] 0,       8,      6,    12,    38;
[5] 0,      64,     32,    48,   152,    728;
[6] 0,    1024,    320,   320,   760,   3640,   26704;
[7] 0,   32768,   6144,  3840,  6080,  21840,  160224,  1866256;
"""


@cache
def labeledgraphs(n: int) -> list[int]:
    if n == 0:
        return [1]

    s = [
        2 ** (((k - n + 1) * (k - n)) // 2)
        * Binomial(n - 1, k - 1)
        * labeledgraphs(k)[k]
        for k in range(1, n)
    ]
    b = 2 ** (((n - 1) * n) // 2) - sum(s)

    return [0] + s + [b]


@MakeTriangle(labeledgraphs, "LabeledGraphs", ["A360603"], True)
def LabeledGraphs(n: int, k: int) -> int:
    return labeledgraphs(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(LabeledGraphs, short=True)

''' OEIS

The traits of the LabeledGraphs triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Rev-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A001187 | Std-RowMax       | Number of connected labeled graphs with n nodes                                |
| 5   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 6   | A006125 | Std-RowSum       | a(n) = 2^(n*(n-1)/2)                                                           |
| 7   | A053549 | Std-DiagRow1     | Number of labeled rooted connected graphs                                      |
| 8   | A060818 | Std-RowGcd       | a(n) = 2^(n - HammingWeight(n)) = 2^(n - BitCount(n)) = 2^(n - A000120(n))     |
| 9   | A123903 | Std-DiagCol2     | Total number of "Emperors" in all tournaments on n labeled nodes               |
| 10  | A137882 | Rev-PolyRow3     | Number of (directed) Hamiltonian paths in the n-ladder graph                   |
| 11  | A275462 | Std-DiagRow2     | Number of leaves in all simple labeled connected graphs on n nodes             |
| 12  | A360603 | Std-Triangle     | Triangle read by rows. T(n, k) = A360604(n, k) * A001187(k) for 0 <= k <= n    |
| 13  | A360860 | Std-Acc          | Accumulation triangle of A360603 read by rows                                  |

* Statistic about LabeledGraphs:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 13.
	all      A-numbers  : 41.
	missing  sequences  : 84.

[('missing', 84), ('A006125', 9), ('A001187', 6), ('A275462', 3), ('A123903', 3), ('A060818', 3), ('A053549', 3), ('A000027', 3), ('A000007', 3), ('A360860', 2), ('A360603', 2), ('A002378', 2), ('A137882', 1), ('A000012', 1)]

A related webpage is: https://peterluschny.github.io/tabl/LabeledGraphs.html .
2025/01/10

'''
