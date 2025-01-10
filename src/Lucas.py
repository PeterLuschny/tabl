from functools import cache
from _tabltypes import MakeTriangle

"""Lucas polynomials (unsigned coefficients).
  [ 0]  1;
  [ 1]  1,  0;
  [ 2]  1,  1,  1;
  [ 3]  1,  2,  1,  0;
  [ 4]  1,  3,  1,  1,  1;
  [ 5]  1,  4,  1,  3,  2,  0;
  [ 6]  1,  5,  1,  6,  3,  1,  1;
  [ 7]  1,  6,  1, 10,  4,  4,  3,  0;
  [ 8]  1,  7,  1, 15,  5, 10,  6,  1,  1;
  [ 9]  1,  8,  1, 21,  6, 20, 10,  5,  4,  0;
  [10]  1,  9,  1, 28,  7, 35, 15, 15, 10,  1, 1;
"""


@cache
def lucas(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 0]
    if n == 2: return [1, 1, 1]

    rowA = lucas(n - 2)
    row  = lucas(n - 1) + [(n + 1) % 2]
    row[1] += 1

    for k in range(3, n):
        row[k] += rowA[k - 2]

    return row


@MakeTriangle(lucas, "Lucas", ["A374440"], True)
def Lucas(n: int, k: int) -> int:
    return lucas(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Lucas)

''' OEIS

The traits of the Lucas triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Rev:Inv-EvenSum  | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000032 | Std-RowSum       | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 5   | A000035 | Std-ColRight     | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 6   | A000071 | Std-OddSum       | a(n) = Fibonacci(n) - 1                                                        |
| 7   | A000217 | Std-DiagCol3     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 8   | A000290 | Std-PolyRow3     | The squares: a(n) = n^2                                                        |
| 9   | A001611 | Std-EvenSum      | a(n) = Fibonacci(n) + 1                                                        |
| 10  | A001911 | Std-AltSum       | a(n) = Fibonacci(n+3) - 2                                                      |
| 11  | A002061 | Std-PolyRow2     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 12  | A025560 | Std-RowLcm       | a(n) = LCM{1, C(n-1,1), C(n-2,2), ..., C(n-[ n/2 ],[ n/2 ])}                   |
| 13  | A028387 | Rev:Inv-DiagRow2 | a(n) = n + (n+1)^2                                                             |
| 14  | A045991 | Rev-PolyRow3     | a(n) = n^3 - n^2                                                               |
| 15  | A057979 | Std-DiagRow1     | a(n) = 1 for even n and (n-1)/2 for odd n                                      |
| 16  | A073028 | Std-RowMax       | a(n) = max{ C(n,0), C(n-1,1), C(n-2,2), ..., C(n-n,n) }                        |
| 17  | A086341 | Rev-DiagSum      | a(n) = 2*2^floor(n/2) - (-1)^n                                                 |
| 18  | A167155 | Std-RowGcd       | Exponential primorial constant Sum_{k>=0} 1/A140319(k)                         |
| 19  | A174965 | Rev:Inv-RowGcd   | Length of the n-th run of consecutive terms in A000961                         |
| 20  | A374440 | Std-Triangle     | Triangle read by rows: T(n, k) = T(n - 1, k) + T(n - 2, k - 2), with boundary  |

* Statistic about Lucas:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 20.
	all      A-numbers  : 60.
	missing  sequences  : 113.

[('missing', 113), ('A000012', 9), ('A000032', 6), ('A000027', 6), ('A374440', 3), ('A167155', 3), ('A073028', 3), ('A057979', 3), ('A025560', 3), ('A002061', 3), ('A001911', 3), ('A000217', 3), ('A000035', 3), ('A028387', 2), ('A001611', 2), ('A000290', 2), ('A000071', 2), ('A174965', 1), ('A086341', 1), ('A045991', 1), ('A000007', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Lucas.html .
2025/01/10

'''
