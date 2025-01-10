from functools import cache
from _tabltypes import MakeTriangle

"""Stirling set numbers of second order.


[0] 1;
[1] 0, 0;
[2] 0, 1,   0;
[3] 0, 1,   0,    0;
[4] 0, 1,   3,    0,    0;
[5] 0, 1,  10,    0,    0,  0;
[6] 0, 1,  25,   15,    0,  0,  0;
[7] 0, 1,  56,  105,    0,  0,  0,  0;
[8] 0, 1, 119,  490,  105,  0,  0,  0,  0;
[9] 0, 1, 246, 1918, 1260,  0,  0,  0,  0,  0;
"""


@cache
def stirlingset2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov = stirlingset2(n - 2)
    row = stirlingset2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]

    return row


@MakeTriangle(stirlingset2, "StirlingSet2", ["A358623", "A008299", "A137375"], False)
def StirlingSet2(n: int, k: int) -> int:
    return stirlingset2(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingSet2)


''' OEIS

The traits of the StirlingSet2 triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagCol1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000247 | Std-DiagCol2     | a(n) = 2^n - n - 2                                                             |
| 5   | A000290 | Rev-PolyRow3     | The squares: a(n) = n^2                                                        |
| 6   | A000296 | Std-RowSum       | Set partitions without singletons: number of partitions of an n-set into block |
| 7   | A000457 | Std-CentralO     | Exponential generating function: (1+3*x)/(1-2*x)^(7/2)                         |
| 8   | A000478 | Std-DiagCol3     | Number of ways of placing n labeled balls into 3 indistinguishable boxes with  |
| 9   | A000587 | Std-AltSum       | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 |
| 10  | A001147 | Std-CentralE     | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 11  | A063524 | Std-DiagRow1     | Characteristic function of 1                                                   |
| 12  | A097762 | Std-OddSum       | Number of different partitions of the set {1, 2, ..., n} into an odd number of |
| 13  | A097763 | Std-EvenSum      | Number of different partitions of the set {1, 2, ..., n} into an even number o |
| 14  | A123023 | Rev-ColMiddle    | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 15  | A194689 | Std-PolyCol2     | a(n) = Sum_{k=0..n} binomial(n,k)*w(k)*w(n-k) where w() = A000296()            |
| 16  | A259877 | Std-ColMiddle    | If n is even then a(n) = n!/( 2^(n/2)*(n/2)! ), otherwise a(n) = n!/( 3*2^((n- |
| 17  | A334190 | Std-NegHalf      | a(n) = exp(1/2) * Sum_{k>=0} (2*k + 1)^n / ((-2)^k * k!)                       |
| 18  | A334243 | Alt-PolyDiag     | a(n) = exp(n) * Sum_{k>=0} (k + n)^n * (-n)^k / k!                             |
| 19  | A337038 | Std-PosHalf      | a(n) = exp(-1/2) * Sum_{k>=0} (2*k - 1)^n / (2^k * k!)                         |
| 20  | A337039 | Rev-PolyCol3     | a(n) = exp(-1/3) * Sum_{k>=0} (3*k - 1)^n / (3^k * k!)                         |
| 21  | A337043 | Rev-PolyDiag     | a(0) = 1; thereafter a(n) = exp(-1/n) * Sum_{k>=0} (n*k - 1)^n / (n^k * k!)    |
| 22  | A337057 | Std-PolyDiag     | a(n) = exp(-n) * Sum_{k>=0} (k - n)^n * n^k / k!                               |
| 23  | A358623 | Std-Triangle     | Regular triangle read by rows. T(n, k) = {{n, k}}, where {{n, k}} are the seco |
| 24  | A367890 | Std-PolyCol3     | Expansion of e.g.f. exp(3*(exp(x) - 1 - x))                                    |

* Statistic about StirlingSet2:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 24.
	all      A-numbers  : 59.
	missing  sequences  : 62.

[('missing', 62), ('A000296', 6), ('A000007', 6), ('A000027', 5), ('A337038', 3), ('A063524', 3), ('A001147', 3), ('A000587', 3), ('A000478', 3), ('A000247', 3), ('A000012', 3), ('A358623', 2), ('A334190', 2), ('A259877', 2), ('A194689', 2), ('A097763', 2), ('A097762', 2), ('A000457', 2), ('A367890', 1), ('A337057', 1), ('A337043', 1), ('A337039', 1), ('A334243', 1), ('A123023', 1), ('A000290', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingSet2.html .
2025/01/10

'''
