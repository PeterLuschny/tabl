from functools import cache
from _tabltypes import MakeTriangle

"""Schroeder bilateral paths.


[0]     1;
[1]     2,     1;
[2]     6,     6,     1;
[3]    20,    30,    12,     1;
[4]    70,   140,    90,    20,     1;
[5]   252,   630,   560,   210,    30,    1;
[6]   924,  2772,  3150,  1680,   420,   42,    1;
[7]  3432, 12012, 16632, 11550,  4200,  756,   56,  1;
[8] 12870, 51480, 84084, 72072, 34650, 9240, 1260, 72, 1;
"""


@cache
def schroederpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = schroederpaths(n - 1) + [1]

    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n

    return row


@MakeTriangle(schroederpaths, "SchroederPaths", ["A104684", "A063007"], True)
def SchroederPaths(n: int, k: int) -> int:
    return schroederpaths(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SchroederPaths)


''' OEIS

The traits of the SchroederPaths triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-AltSum       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000290 | Alt-TransNat0    | The squares: a(n) = n^2                                                        |
| 4   | A000984 | Std-ColLeft      | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 5   | A001850 | Std-RowSum       | Central Delannoy numbers: a(n) = Sum_{k=0..n} C(n,k)*C(n+k,k)                  |
| 6   | A002061 | Alt-AccSum       | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 7   | A002378 | Std-DiagRow1     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 8   | A002426 | Rev-DiagSum      | Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n         |
| 9   | A002457 | Std-DiagCol1     | a(n) = (2n+1)!/n!^2                                                            |
| 10  | A002544 | Std-DiagCol2     | a(n) = binomial(2*n+1,n)*(n+1)^2                                               |
| 11  | A003154 | Rev-PolyRow2     | Centered 12-gonal numbers, or centered dodecagonal numbers: numbers of the for |
| 12  | A005258 | Std-BinConv      | Apery numbers: a(n) = Sum_{k=0..n} binomial(n,k)^2 * binomial(n+k,k)           |
| 13  | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 14  | A005563 | Alt-AccRevSum    | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 15  | A006442 | Std-PosHalf      | Expansion of 1/sqrt(1 - 10*x + x^2)                                            |
| 16  | A006480 | Std-CentralE     | De Bruijn's S(3,n): (3n)!/(n!)^3                                               |
| 17  | A007744 | Std-DiagCol3     | Expansion of (1+6*x)/(1-4*x)^(7/2)                                             |
| 18  | A028872 | Std-PolyRow2     | a(n) = n^2 - 3                                                                 |
| 19  | A033487 | Std-DiagRow2     | a(n) = n*(n+1)*(n+2)*(n+3)/4                                                   |
| 20  | A047665 | Std-OddSum       | Expansion of (1/sqrt(1-6*x+x^2)-1/(1-x))/2                                     |
| 21  | A063007 | Std-Rev          | T(n,k) = binomial(n,k)*binomial(n+k,k), 0 <= k <= n, triangle read by rows     |
| 22  | A069835 | Std-PolyCol2     | Define an array as follows: b(i,0)=b(0,j)=1, b(i,j) = 2*b(i-1,j-1) + b(i-1,j)  |
| 23  | A084768 | Rev-PolyCol3     | P_n(7), where P_n is n-th Legendre polynomial; also, a(n) = central coefficien |
| 24  | A084771 | Std-PolyCol3     | Coefficients of expansion of 1/sqrt(1 - 10*x + 9*x^2); also, a(n) is the centr |
| 25  | A098332 | Alt-PolyCol3     | Expansion of 1/sqrt(1 - 2*x + 9*x^2)                                           |
| 26  | A104684 | Std-Triangle     | Triangle read by rows: T(n,k) is the number of lattice paths from (0,0) to (n, |
| 27  | A105939 | Std-DiagRow3     | a(n) = binomial(n+3,3)*binomial(n+6,3)                                         |
| 28  | A108626 | Alt-DiagSum      | Antidiagonal sums of square array A108625, in which row n equals the crystal b |
| 29  | A108666 | Std-TransNat0    | Number of (1,1)-steps in all Delannoy paths of length n                        |
| 30  | A126869 | Alt-PolyCol2     | a(n) = Sum_{k = 0..n} binomial(n,floor(k/2))*(-1)^(n-k)                        |
| 31  | A160674 | Rev-PolyRow3     | A bisection of A063522                                                         |
| 32  | A208881 | Std-CentralO     | Number of words either empty or beginning with the first letter of the ternary |
| 33  | A226994 | Std-EvenSum      | Number of lattice paths from (0,0) to (n,n) consisting of steps U=(1,1), H=(1, |
| 34  | A331656 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k,k) * n^k                      |
| 35  | A335309 | Std-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k,k) * n^(n-k)                  |
| 36  | A335310 | Alt-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k,k) * (-n)^(n-k)               |
| 37  | A349713 | Std-DiagSum      | Antidiagonal sums of triangle A104684                                          |

* Statistic about SchroederPaths:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 37.
	all      A-numbers  : 87.
	missing  sequences  : 118.

[('missing', 118), ('A001850', 8), ('A000012', 6), ('A002378', 5), ('A063007', 4), ('A000027', 4), ('A105939', 3), ('A104684', 3), ('A033487', 3), ('A007744', 3), ('A006480', 3), ('A006442', 3), ('A005258', 3), ('A002544', 3), ('A002457', 3), ('A000984', 3), ('A226994', 2), ('A208881', 2), ('A126869', 2), ('A069835', 2), ('A047665', 2), ('A005563', 2), ('A005408', 2), ('A003154', 2), ('A349713', 1), ('A335310', 1), ('A335309', 1), ('A331656', 1), ('A160674', 1), ('A108666', 1), ('A108626', 1), ('A098332', 1), ('A084771', 1), ('A084768', 1), ('A028872', 1), ('A002426', 1), ('A002061', 1), ('A000290', 1)]

A related webpage is: https://peterluschny.github.io/tabl/SchroederPaths.html .
2025/01/10

'''
