from functools import cache
from _tabltypes import MakeTriangle


"""Levin's Triangle, RisingFactorial(n + 1, n) / (k! * (n - k)!).


[0]     1;
[1]     2,      2;
[2]     6,     12,      6;
[3]    20,     60,     60,     20;
[4]    70,    280,    420,    280,     70;
[5]   252,   1260,   2520,   2520,   1260,    252;
[6]   924,   5544,  13860,  18480,  13860,   5544,    924;
[7]  3432,  24024,  72072, 120120, 120120,  72072,  24024,   3432;
[8] 12870, 102960, 360360, 720720, 900900, 720720, 360360, 102960, 12870;
"""


@cache
def levin(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = levin(n - 1) + [1]
    row[0] = row[n] = (row[n - 1] * (4 * n - 2)) // n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@MakeTriangle(levin, "Levin", ["A356546"], False)
def Levin(n: int, k: int) -> int:
    return levin(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Levin)

''' OEIS

The traits of the Levin triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000079 | Alt-DiagSum      | Powers of 2: a(n) = 2^n                                                        |
| 3   | A000897 | Std-CentralE     | a(n) = (4*n)! / ((2*n)!*n!^2)                                                  |
| 4   | A000911 | Std-DiagRow2     | a(n) = (2n+3)! /( n! * (n+1)! )                                                |
| 5   | A000984 | Std-RowGcd       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 6   | A002894 | Std-BinConv      | a(n) = binomial(2n, n)^2                                                       |
| 7   | A005430 | Std-DiagRow1     | Apery numbers: n*C(2*n,n)                                                      |
| 8   | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 9   | A006139 | Std-DiagSum      | n*a(n) = 2*(2*n-1)*a(n-1) + 4*(n-1)*a(n-2) with a(0) = 1                       |
| 10  | A008556 | Std-AntiDiag     | Triangle of coefficients of Legendre polynomials 2^n P_n (x)                   |
| 11  | A033581 | Std-PolyRow2     | a(n) = 6*n^2                                                                   |
| 12  | A059304 | Std-RowSum       | a(n) = 2^n * (2*n)! / (n!)^2                                                   |
| 13  | A069723 | Std-EvenSum      | a(n) = 2^(n-1)*binomial(2*n-3, n-1)                                            |
| 14  | A098430 | Std-PolyCol3     | a(n) = 4^n*(2*n)!/(n!)^2                                                       |
| 15  | A098658 | Std-PosHalf      | a(n) = 3^n*(2*n)!/(n!)^2                                                       |
| 16  | A130706 | Alt-AccSum       | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 17  | A335462 | Alt-TransNat0    | Number of (1,2,1) and (2,1,2)-matching permutations of the prime indices of n  |
| 18  | A356546 | Std-Triangle     | Triangle read by rows. T(n, k) = RisingFactorial(n + 1, n) / (k! * (n - k)!)   |

* Statistic about Levin:

	Triangles considered: ['Std', 'Alt'].
	distinct A-numbers  : 18.
	all      A-numbers  : 54.
	missing  sequences  : 30.

[('missing', 30), ('A000984', 9), ('A059304', 5), ('A356546', 4), ('A069723', 4), ('A005430', 4), ('A000911', 4), ('A000897', 4), ('A130706', 3), ('A098658', 3), ('A033581', 2), ('A008556', 2), ('A005843', 2), ('A002894', 2), ('A000007', 2), ('A335462', 1), ('A098430', 1), ('A006139', 1), ('A000079', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Levin.html .
2025/01/10

'''
