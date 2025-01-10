from functools import cache
from _tabltypes import MakeTriangle

"""Christmas tree, binomial(n mod 2, k mod 2).

[0]                           1
[1]                          1, 1
[2]                        1, 0, 1
[3]                       1, 1, 1, 1
[4]                     1, 0, 1, 0, 1
[5]                    1, 1, 1, 1, 1, 1
[6]                  1, 0, 1, 0, 1, 0, 1
[7]                 1, 1, 1, 1, 1, 1, 1, 1
[8]               1, 0, 1, 0, 1, 0, 1, 0, 1
[9]              1, 1, 1, 1, 1, 1, 1, 1, 1, 1
"""


@cache
def ctree(n: int) -> list[int]:
    if n % 2 == 1:
        return [1] * (n + 1)

    return [1, 0] * (n // 2) + [1]


@MakeTriangle(ctree, "CTree", ["A106465", "A106470"], True)
def CTree(n: int, k: int) -> int:
    return ctree(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CTree)

''' OEIS

The traits of the CTree triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-RowSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RevInv       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Std-CentralE     | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 6   | A004526 | Std-EvenSum      | Nonnegative integers repeated, floor(n/2)                                      |
| 7   | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 8   | A010673 | Inv-AccSum       | Period 2: repeat [0, 2]                                                        |
| 9   | A010707 | Inv-NegHalf      | Period 2: repeat (3,9)                                                         |
| 10  | A019590 | Inv:Rev-EvenSum  | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 11  | A029578 | Std-RowSum       | The natural numbers interleaved with the even numbers                          |
| 12  | A039966 | Inv:Rev-DiagSum  | a(0) = 1; thereafter a(3n+2) = 0, a(3n) = a(3n+1) = a(n)                       |
| 13  | A040057 | Inv:Rev-PolyCol3 | Continued fraction for sqrt(66)                                                |
| 14  | A051494 | Alt-AccSum       | Expansion of (1 - x + x^2 + x^3)/(1 - x^2)^3                                   |
| 15  | A052992 | Alt-PosHalf      | Expansion of 1/((1 - x)*(1 - 2*x)*(1 + 2*x))                                   |
| 16  | A053698 | Std-PolyRow3     | a(n) = n^3 + n^2 + n + 1                                                       |
| 17  | A056136 | Std-TransNat0    | Largest positive integer whose harmonic mean with another positive integer is  |
| 18  | A062158 | Alt-PolyRow3     | a(n) = n^3 - n^2 + n - 1 = (n-1) * (n^2 + 1)                                   |
| 19  | A063524 | Inv-OddSum       | Characteristic function of 1                                                   |
| 20  | A079944 | Inv-CentralO     | A run of 2^n 0's followed by a run of 2^n 1's, for n=0, 1, 2, ..               |
| 21  | A084558 | Inv:Rev-TransSqr | a(0) = 0; for n >= 1: a(n) = largest m such that n >= m!                       |
| 22  | A103424 | Std-InvBinConv   | Expansion of e.g.f.: 1 + sinh(2*x)                                             |
| 23  | A105397 | Inv-AbsSum       | Periodic with period 2: repeat [4,2]                                           |
| 24  | A106465 | Std-Triangle     | Triangle read by rows, T(n, k) = 1 if n mod 2 = 1, otherwise (k + 1) mod 2     |
| 25  | A106466 | Std-DiagSum      | Interleave 1,2,3,.. with 1,1,2,2,3,3,..                                        |
| 26  | A106468 | Std-Inv          | Absolute value of inverse of number triangle A106465                           |
| 27  | A115944 | Inv-ColMiddle    | Number of partitions of n into distinct factorials                             |
| 28  | A117856 | Inv-PolyCol2     | Number of palindromes of length n (in base 4)                                  |
| 29  | A129889 | Alt-TransNat0    | Write down n, then n*(n+1)                                                     |
| 30  | A130706 | Inv-AltSum       | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 31  | A137344 | Inv:Rev-NegHalf  | a(n)=4a(n-2). Also 3*A084221                                                   |
| 32  | A142150 | Std-OddSum       | The nonnegative integers interleaved with 0's                                  |
| 33  | A152618 | Inv-PolyRow3     | a(n) = (n-1)^2*(n+1)                                                           |
| 34  | A158302 | Std-BinConv      | "1" followed by repeats of 2^k deleting all 4^k, k>                            |
| 35  | A166486 | Std-ColMiddle    | Periodic sequence [0,1,1,1] of length 4; Characteristic function of numbers th |
| 36  | A354856 | Alt-DiagSum      | a(1) = 1, a(n) = the number of times a(n-1) appears among the first n-2 terms  |
| 37  | A359366 | Std-AccSum       | a(n) = (1/8)*(((3*n + 1) + (n - 1)*(-1)^n)*(n + 1))                            |

* Statistic about CTree:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 37.
	all      A-numbers  : 117.
	missing  sequences  : 38.

[('missing', 38), ('A000012', 26), ('A000035', 15), ('A010673', 8), ('A106465', 6), ('A106468', 5), ('A142150', 4), ('A029578', 4), ('A000027', 4), ('A359366', 3), ('A051494', 3), ('A166486', 2), ('A158302', 2), ('A152618', 2), ('A130706', 2), ('A117856', 2), ('A105397', 2), ('A103424', 2), ('A063524', 2), ('A005563', 2), ('A004526', 2), ('A002522', 2), ('A000007', 2), ('A354856', 1), ('A137344', 1), ('A129889', 1), ('A115944', 1), ('A106466', 1), ('A084558', 1), ('A079944', 1), ('A062158', 1), ('A056136', 1), ('A053698', 1), ('A052992', 1), ('A040057', 1), ('A039966', 1), ('A019590', 1), ('A010707', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CTree.html .
2025/01/10

'''
