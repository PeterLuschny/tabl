from functools import cache
from _tabltypes import MakeTriangle

"""Uno, the all 1's triangle.

[0]  1
[1]  1,  1
[2]  1,  1,  1
[3]  1,  1,  1,  1
[4]  1,  1,  1,  1,  1
[5]  1,  1,  1,  1,  1,  1
[6]  1,  1,  1,  1,  1,  1,  1
[7]  1,  1,  1,  1,  1,  1,  1,  1
[8]  1,  1,  1,  1,  1,  1,  1,  1,  1
"""


@cache
def one(n: int) -> list[int]:
    if n == 0:
        return [1]
    return one(n - 1) + [1]


@MakeTriangle(one, "One", ["A000012", "A008836", "A014077"], True)
def One(n: int, k: int) -> int:
    return one(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(One)

''' OEIS

The traits of the One triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-InvBinConv   | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-Triangle     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-RowSum       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Std-AltSum       | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A000079 | Std-BinConv      | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000217 | Std-AccSum       | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000225 | Std-PosHalf      | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 8   | A000330 | Std-TransSqrs    | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1) |
| 9   | A001045 | Std-NegHalf      | Jacobsthal sequence (or Jacobsthal numbers): a(n) = a(n-1) + 2*a(n-2), with a( |
| 10  | A002061 | Std-PolyRow2     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 11  | A002260 | Std-Acc          | Triangle read by rows: T(n,k) = k for n >= 1, k = 1..n                         |
| 12  | A002378 | Inv-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 13  | A003462 | Std-PolyCol3     | a(n) = (3^n - 1)/2                                                             |
| 14  | A004526 | Std-EvenSum      | Nonnegative integers repeated, floor(n/2)                                      |
| 15  | A005408 | Inv-TransSqrs    | The odd numbers: a(n) = 2*n + 1                                                |
| 16  | A007283 | Inv:Rev-NegHalf  | a(n) = 3*2^n                                                                   |
| 17  | A008776 | Inv-PolyCol3     | Pisot sequences E(2,6), L(2,6), P(2,6), T(2,6)                                 |
| 18  | A010054 | Inv-Acc          | a(n) = 1 if n is a triangular number, otherwise 0                              |
| 19  | A010701 | Inv-NegHalf      | Constant sequence: the all 3's sequence                                        |
| 20  | A015518 | Alt-PolyCol3     | a(n) = 2*a(n-1) + 3*a(n-2), with a(0)=0, a(1)=1                                |
| 21  | A019590 | Inv:Rev-DiagSum  | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 22  | A031973 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k                                                        |
| 23  | A045991 | Inv-PolyRow3     | a(n) = n^3 - n^2                                                               |
| 24  | A053698 | Std-PolyRow3     | a(n) = n^3 + n^2 + n + 1                                                       |
| 25  | A055642 | Inv-AltSum       | Number of digits in the decimal expansion of n                                 |
| 26  | A062158 | Alt-PolyRow3     | a(n) = n^3 - n^2 + n - 1 = (n-1) * (n^2 + 1)                                   |
| 27  | A066274 | Inv-PolyDiag     | Number of endofunctions of [n] such that 1 is not a fixed point                |
| 28  | A081209 | Alt-PolyDiag     | a(n) = Sum_{k=0..n} (-1)^(n-k)*n^k                                             |
| 29  | A097806 | Std-Inv          | Riordan array (1+x, 1) read by rows                                            |
| 30  | A104878 | Std-Poly         | A sum-of-powers number triangle                                                |
| 31  | A115944 | Inv-ColMiddle    | Number of partitions of n into distinct factorials                             |
| 32  | A133872 | Alt-DiagSum      | Period 4: repeat [1, 1, 0, 0]                                                  |
| 33  | A135387 | Inv:Rev-Diffx1   | Triangle read by rows, with (2, 1, 0, 0, 0, ...) in every column               |
| 34  | A144217 | Inv-Diffx1       | Weight array of A144216: a rectangular array by antidiagonals                  |
| 35  | A167686 | Inv:Rev-AntiDiag | Hankel transform of A003823                                                    |
| 36  | A177990 | Alt-Acc          | Triangle read by rows, variant of A070909, a cellular automato                 |
| 37  | A240025 | Inv-AntiDiag     | Characteristic function of quarter squares, cf. A002620                        |

* Statistic about One:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 37.
	all      A-numbers  : 142.
	missing  sequences  : 5.

[('A000012', 56), ('A000027', 15), ('A004526', 7), ('missing', 5), ('A097806', 5), ('A055642', 5), ('A000217', 5), ('A000007', 5), ('A010054', 4), ('A000079', 4), ('A002260', 3), ('A001045', 3), ('A000225', 3), ('A002061', 2), ('A000035', 2), ('A240025', 1), ('A177990', 1), ('A167686', 1), ('A144217', 1), ('A135387', 1), ('A133872', 1), ('A115944', 1), ('A104878', 1), ('A081209', 1), ('A066274', 1), ('A062158', 1), ('A053698', 1), ('A045991', 1), ('A031973', 1), ('A019590', 1), ('A015518', 1), ('A010701', 1), ('A008776', 1), ('A007283', 1), ('A005408', 1), ('A003462', 1), ('A002378', 1), ('A000330', 1)]

A related webpage is: https://peterluschny.github.io/tabl/One.html .
2025/01/10

'''
