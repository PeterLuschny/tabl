from functools import cache
from _tabltypes import MakeTriangle


"""Expansion of x^n in terms of Laguerre (unsigned).


[0] [   1]
[1] [   1,     1]
[2] [   2,     4,      2]
[3] [   6,    18,     18,      6]
[4] [  24,    96,    144,     96,     24]
[5] [ 120,   600,   1200,   1200,    600,    120]
[6] [ 720,  4320,  10800,  14400,  10800,   4320,   720]
[7] [5040, 35280, 105840, 176400, 176400, 105840, 35280, 5040]
"""


@cache
def powlaguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = powlaguerre(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


@MakeTriangle(powlaguerre, "PowLaguerre", ["A196347", "A021012"], False)
def PowLaguerre(n: int, k: int) -> int:
    return powlaguerre(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(PowLaguerre)

''' OEIS

The traits of the PowLaguerre triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000142 | Std-RowGcd       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 4   | A000165 | Std-RowSum       | Double factorial of even numbers: (2n)!! = 2^n*n!                              |
| 5   | A001105 | Std-PolyRow2     | a(n) = 2*n^2                                                                   |
| 6   | A001563 | Std-DiagRow1     | a(n) = n*n! = (n+1)! - n!                                                      |
| 7   | A001804 | Std-DiagRow2     | a(n) = n! * C(n,2)                                                             |
| 8   | A001805 | Std-DiagRow3     | a(n) = n! * binomial(n,3)                                                      |
| 9   | A001813 | Std-BinConv      | Quadruple factorial numbers: a(n) = (2n)!/n!                                   |
| 10  | A002866 | Std-EvenSum      | a(0) = 1; for n > 0, a(n) = 2^(n-1)*n!                                         |
| 11  | A013999 | Alt-DiagSum      | From applying the "rational mean" to the number e                              |
| 12  | A014479 | Std-TransNat0    | Exponential generating function = (1+2*x)/(1-2*x)^3                            |
| 13  | A019590 | Alt-AccSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 14  | A032031 | Std-PosHalf      | Triple factorial numbers: (3n)!!! = 3^n*n!                                     |
| 15  | A047053 | Std-PolyCol3     | a(n) = 4^n * n!                                                                |
| 16  | A059837 | Std-RowMax       | Diagonal T(s,s) of triangle A059836                                            |
| 17  | A063524 | Alt-TransNat0    | Characteristic function of 1                                                   |
| 18  | A122747 | Std-CentralE     | Bishops on an n X n board (see Robinson paper for details)                     |
| 19  | A152684 | Std-PolyDiag     | a(n) is the number of top-down sequences (F_1, F_2, ..., F_n) whereas each F_i |
| 20  | A187735 | Std-AccSum       | G.f.: Sum_{n>=0} (2*n+1)^n * x^n / (1 + (2*n+1)*x)^n                           |
| 21  | A196347 | Std-Triangle     | Triangle T(n, k) read by rows, T(n, k) = n!*binomial(n, k)                     |
| 22  | A240172 | Std-DiagSum      | O.g.f.: Sum_{n>=0} n! * x^n * (1+x)^n                                          |
| 23  | A244726 | Std-PolyRow3     | 6*n^3                                                                          |
| 24  | A360283 | Std-RowLcm       | a(n) = lcm({n! * binomial(n, k) for k = 0..n})                                 |
| 25  | A360602 | Std-CentralO     | a(n) = ((2*n + 1)! / n!)^2 / (n + 1)                                           |

* Statistic about PowLaguerre:

	Triangles considered: ['Std', 'Alt'].
	distinct A-numbers  : 25.
	all      A-numbers  : 69.
	missing  sequences  : 11.

[('missing', 11), ('A000142', 9), ('A000165', 5), ('A196347', 4), ('A122747', 4), ('A059837', 4), ('A002866', 4), ('A001805', 4), ('A001804', 4), ('A001563', 4), ('A187735', 3), ('A032031', 3), ('A360602', 2), ('A360283', 2), ('A244726', 2), ('A001813', 2), ('A001105', 2), ('A000027', 2), ('A000007', 2), ('A240172', 1), ('A152684', 1), ('A063524', 1), ('A047053', 1), ('A019590', 1), ('A014479', 1), ('A013999', 1)]

A related webpage is: https://peterluschny.github.io/tabl/PowLaguerre.html .
2025/01/10

'''
