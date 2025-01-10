from functools import cache
from _tabltypes import MakeTriangle

"""Lehmer-Comtet of 2nd kind, unsigned.


[0] 1;
[1] 0,      1;
[2] 0,      1,      1;
[3] 0,      4,      3,      1;
[4] 0,     27,     19,      6,     1;
[5] 0,    256,    175,     55,    10,    1;
[6] 0,   3125,   2101,    660,   125,   15,   1;
[7] 0,  46656,  31031,   9751,  1890,  245,  21,  1;
[8] 0, 823543, 543607, 170898, 33621, 4550, 434, 28, 1;
"""


@cache
def t(n: int, k: int, m: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return n**k
    return m * t(n, k - 1, m) + t(n - 1, k, m + 1)


@cache
def lehmer(n: int) -> list[int]:
    return [t(k - 1, n - k, n - k) if n != k else 1 for k in range(n + 1)]


@MakeTriangle(lehmer, "Lehmer", ["A354794", "A039621"], True)
def Lehmer(n: int, k: int) -> int:
    return lehmer(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    # TODO Needs a more efficient implementation.
    TablTest(Lehmer, short=True)

''' OEIS

The traits of the Lehmer triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Inv-DiagCol1     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000312 | Std-RowMax       | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 7   | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 8   | A005727 | Inv-AltSum       | n-th derivative of x^x at x=1. Also called Lehmer-Comtet numbers               |
| 9   | A014209 | Inv:Rev-PolyRow3 | a(n) = n^2 + 3*n - 1                                                           |
| 10  | A033951 | Rev-PolyRow3     | Write 1,2,... in a clockwise spiral; sequence gives numbers on positive x axis |
| 11  | A045406 | Inv-DiagCol2     | A diagonal of A008296                                                          |
| 12  | A045531 | Std-DiagCol2     | Number of sticky functions: endofunctions of [n] having a fixed point          |
| 13  | A059302 | Inv-DiagRow2     | A diagonal of A008296                                                          |
| 14  | A114890 | Inv-RowGcd       | First differences of A114889                                                   |
| 15  | A176118 | Inv-RowSum       | The n-th derivative of 1/x^x, evaluated at x=1                                 |
| 16  | A195979 | Std-RowSum       | a(n) = Sum_{k=0..n} T(n,k), where T(n,k) is the number of rooted labeled trees |
| 17  | A215862 | Std-DiagRow2     | Number of simple labeled graphs on n+2 nodes with exactly n connected componen |
| 18  | A242659 | Alt-PolyRow3     | a(n) = n*(n^2 - 3*n + 4)                                                       |
| 19  | A265945 | Inv:Rev-NegHalf  | n-th derivative of x^(2*x) at x=1                                              |
| 20  | A281596 | Std-DiagCol3     | a(n) = ((n-2)^n - 2*(n-1)^n + n^n)/2                                           |
| 21  | A290219 | Std-AltSum       | a(n) = n! * [x^n] exp(exp(x) - n*x - 1)                                        |
| 22  | A298511 | Inv-CentralE     | Central Lehmer-Comtet numbers of the first kind: a(n) = A008296(2n,n)          |
| 23  | A347276 | Inv-DiagCol3     | Third column of A008296                                                        |
| 24  | A354794 | Std-Triangle     | Triangle read by rows. The Bell transform of the sequence {m^m | m >= 0}       |
| 25  | A354795 | Std-Inv          | Triangle read by rows. The matrix inverse of A354794. Equivalently, the Bell t |

* Statistic about Lehmer:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 25.
	all      A-numbers  : 78.
	missing  sequences  : 137.

[('missing', 137), ('A000012', 9), ('A195979', 6), ('A000312', 6), ('A000217', 5), ('A000027', 5), ('A000007', 5), ('A354795', 4), ('A354794', 3), ('A290219', 3), ('A281596', 3), ('A215862', 3), ('A045531', 3), ('A002378', 3), ('A347276', 2), ('A298511', 2), ('A176118', 2), ('A114890', 2), ('A059302', 2), ('A045406', 2), ('A005727', 2), ('A000142', 2), ('A265945', 1), ('A242659', 1), ('A033951', 1), ('A014209', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Lehmer.html .
2025/01/10

'''
