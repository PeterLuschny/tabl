from functools import cache
from _tabltypes import MakeTriangle

"""Leibniz's Triangle, FallingFactorial(n + 1, n) / (k! * (n - k)!).

[0]  1
[1]  2   2
[2]  3   6    3
[3]  4  12   12    4
[4]  5  20   30   20    5
[5]  6  30   60   60   30    6
[6]  7  42  105  140  105   42    7
[7]  8  56  168  280  280  168   56    8
[8]  9  72  252  504  630  504  252   72   9
[9] 10  90  360  840 1260 1260  840  360  90  10
"""


@cache
def leibniz(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = leibniz(n - 1) + [n + 1]
    row[0] = row[n] = n + 1
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@MakeTriangle(leibniz, "Leibniz", ["A003506"], False)
def Leibniz(n: int, k: int) -> int:
    return leibniz(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Leibniz)

''' OEIS

The traits of the Leibniz triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000312 | Std-PolyDiag     | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 4   | A001629 | Std-DiagSum      | Self-convolution of Fibonacci numbers                                          |
| 5   | A001787 | Std-RowSum       | a(n) = n*2^(n-1)                                                               |
| 6   | A001788 | Std-AccSum       | a(n) = n*(n+1)*2^(n-2)                                                         |
| 7   | A001815 | Std-TransNat0    | a(n) = binomial(n,2) * 2^(n-1)                                                 |
| 8   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 9   | A002457 | Std-CentralE     | a(n) = (2n+1)!/n!^2                                                            |
| 10  | A002697 | Std-PolyCol3     | a(n) = n*4^(n-1)                                                               |
| 11  | A003418 | Std-RowLcm       | Least common multiple (or LCM) of {1, 2, ..., n} for n >= 1, a(0) = 1          |
| 12  | A003506 | Std-Triangle     | Triangle of denominators in Leibniz's Harmonic Triangle a(n,k), n >= 1, 1 <= k |
| 13  | A005430 | Std-CentralO     | Apery numbers: n*C(2*n,n)                                                      |
| 14  | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 15  | A027471 | Std-PosHalf      | a(n) = (n-1)*3^(n-2), n > 0                                                    |
| 16  | A027480 | Std-DiagRow2     | a(n) = n*(n+1)*(n+2)/2                                                         |
| 17  | A033428 | Std-PolyRow2     | a(n) = 3*n^2                                                                   |
| 18  | A033430 | Std-PolyRow3     | a(n) = 4*n^3                                                                   |
| 19  | A033488 | Std-DiagRow3     | a(n) = n*(n+1)*(n+2)*(n+3)/6                                                   |
| 20  | A037965 | Std-BinConv      | a(n) = n*binomial(2*n-2, n-1)                                                  |
| 21  | A057711 | Std-EvenSum      | a(0)=0, a(1)=1, a(n) = n*2^(n-2) for n >= 2                                    |
| 22  | A100071 | Std-RowMax       | a(n) = n * binomial(n-1, floor((n-1)/2)) = n * max_{i=0..n} binomial(n-1, i)   |
| 23  | A104002 | Std-Poly         | Triangle T(n,k) read by rows: number of permutations in S_n avoiding all k-len |
| 24  | A128502 | Std-AntiDiag     | Convolution array for Chebyshev's S(n,x)=U(n,x/2) polynomials                  |
| 25  | A130706 | Alt-AccSum       | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 26  | A186731 | Alt-DiagSum      | a(3n) = 2n, a(3n+1) = n, a(3n+2) = n+1                                         |
| 27  | A335462 | Alt-TransNat0    | Number of (1,2,1) and (2,1,2)-matching permutations of the prime indices of n  |

* Statistic about Leibniz:

	Triangles considered: ['Std', 'Alt'].
	distinct A-numbers  : 27.
	all      A-numbers  : 74.
	missing  sequences  : 10.

[('missing', 10), ('A000027', 9), ('A001787', 5), ('A100071', 4), ('A057711', 4), ('A033488', 4), ('A027480', 4), ('A003506', 4), ('A002457', 4), ('A002378', 4), ('A130706', 3), ('A027471', 3), ('A001788', 3), ('A128502', 2), ('A037965', 2), ('A033430', 2), ('A033428', 2), ('A005843', 2), ('A005430', 2), ('A003418', 2), ('A000007', 2), ('A335462', 1), ('A186731', 1), ('A104002', 1), ('A002697', 1), ('A001815', 1), ('A001629', 1), ('A000312', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Leibniz.html .
2025/01/10

'''
