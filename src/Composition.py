from functools import cache
from _tabltypes import MakeTriangle
from CompositionMax import compomax

"""Compositions of n with exact k parts.
[0]  1;
[1]  0,  1;
[2]  0,  1,  1;
[3]  0,  1,  2,   1;
[4]  0,  1,  4,   2,   1;
[5]  0,  1,  7,   5,   2,  1;
[6]  0,  1, 12,  11,   5,  2,  1;
[7]  0,  1, 20,  23,  12,  5,  2,  1;
[8]  0,  1, 33,  47,  27, 12,  5,  2, 1;
[9]  0,  1, 54,  94,  59, 28, 12,  5, 2, 1;
"""


@cache
def composition(n: int) -> list[int]:
    if n == 0:
        return [1]

    cm = compomax(n)
    return [cm[k] - cm[k - 1] if k > 0 else 0 for k in range(n + 1)]


@MakeTriangle(composition, "Composition", ["A048004"], True)
def Composition(n: int, k: int) -> int:
    return composition(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Composition, 8, True)

''' OEIS

The traits of the Composition triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000071 | Std-DiagCol2     | a(n) = Fibonacci(n) - 1                                                        |
| 5   | A000079 | Std-RowSum       | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000100 | Std-DiagCol3     | a(n) is the number of compositions of n in which the maximal part is 3         |
| 7   | A000290 | Rev-PolyRow3     | The squares: a(n) = n^2                                                        |
| 8   | A001477 | Inv:Rev-CentralO | The nonnegative integers                                                       |
| 9   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 10  | A011379 | Alt-PolyRow3     | a(n) = n^2*(n+1)                                                               |
| 11  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 12  | A033420 | Std-RowGcd       | a(n) = floor(100/n)                                                            |
| 13  | A039671 | Std-AccSum       | Row sums up to the main diagonal of the "postage stamp" array (n,m >= 0) defin |
| 14  | A045623 | Rev-CentralO     | Number of 1's in all compositions of n+1                                       |
| 15  | A045991 | Std-PolyRow3     | a(n) = n^3 - n^2                                                               |
| 16  | A047859 | Std-CentralE     | a(n) = T(2, n), where T is the array given by A047858                          |
| 17  | A055642 | Std-DiagRow1     | Number of digits in the decimal expansion of n                                 |
| 18  | A072643 | Std-DiagRow2     | Half of the binary width of the terms of A014486, the number of digits in A063 |
| 19  | A102712 | Std-TransNat0    | Sum of largest parts of all compositions of n                                  |
| 20  | A103421 | Std-OddSum       | Number of compositions of n in which the greatest part is odd                  |
| 21  | A103422 | Std-EvenSum      | Number of compositions of n in which the greatest part is even                 |
| 22  | A368279 | Std-DiagSum      | a(n) is the number of compositions of n where the first part is the largest pa |

* Statistic about Composition:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 22.
	all      A-numbers  : 77.
	missing  sequences  : 135.

[('missing', 135), ('A000012', 11), ('A000027', 8), ('A055642', 7), ('A000007', 7), ('A000079', 6), ('A033420', 5), ('A072643', 3), ('A047859', 3), ('A039671', 3), ('A002378', 3), ('A000100', 3), ('A000071', 3), ('A103422', 2), ('A103421', 2), ('A019590', 2), ('A011379', 2), ('A000290', 2), ('A368279', 1), ('A102712', 1), ('A045991', 1), ('A045623', 1), ('A001477', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Composition.html .
2025/01/10

'''
