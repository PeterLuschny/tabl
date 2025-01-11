from functools import cache
from _tabltypes import MakeTriangle

"""Powers.

[0]  [1]
[1]  [0, 1]
[2]  [0, 1,   1]
[3]  [0, 1,   2,   1]
[4]  [0, 1,   4,   3,    1]
[5]  [0, 1,   8,   9,    4,   1]
[6]  [0, 1,  16,  27,   16,   5,   1]
[7]  [0, 1,  32,  81,   64,  25,   6,  1]
[8]  [0, 1,  64, 243,  256, 125,  36,  7, 1]
[9]  [0, 1, 128, 729, 1024, 625, 216, 49, 8, 1]

"""

@cache
def powers(n: int) -> list[int]:
    if n == 0:
        return [1]

    lrow = powers(n - 1)
    return [k * lrow[k] for k in range(n)] + [1]


@MakeTriangle(powers, "Powers", ["A004248", "A009998", "A051129"])
def Powers(n: int, k: int) -> int:
    return powers(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Powers)


''' OEIS

The traits of the Powers triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Std-DiagCol2     | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000169 | Rev-CentralO     | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 6   | A000244 | Std-DiagCol3     | Powers of 3: a(n) = 3^n                                                        |
| 7   | A000248 | Std-BinConv      | Expansion of e.g.f. exp(x*exp(x))                                              |
| 8   | A000290 | Std-DiagRow2     | The squares: a(n) = n^2                                                        |
| 9   | A000312 | Std-CentralE     | a(n) = n^n; number of labeled mappings from n points to themselves (endofuncti |
| 10  | A000578 | Std-DiagRow3     | The cubes: a(n) = n^3                                                          |
| 11  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A003101 | Std-TransNat0    | a(n) = Sum_{k = 1..n} (n - k + 1)^k                                            |
| 13  | A003320 | Std-RowMax       | a(n) = max_{k=0..n} k^(n-k)                                                    |
| 14  | A003725 | Std-InvBinConv   | E.g.f.: exp( x * exp(-x) )                                                     |
| 15  | A003992 | Std-Rev          | Square array read by upwards antidiagonals: T(n,k) = n^k for n >= 0, k >= 0    |
| 16  | A004248 | Std-Triangle     | Array read by ascending antidiagonals: A(n, k) = k^n                           |
| 17  | A007778 | Std-CentralO     | a(n) = n^(n+1)                                                                 |
| 18  | A011379 | Alt-PolyRow3     | a(n) = n^2*(n+1)                                                               |
| 19  | A026898 | Std-RowSum       | a(n) = Sum_{k=0..n} (n-k+1)^k                                                  |
| 20  | A038125 | Std-AltSum       | a(n) = Sum_{k=0..n} (k-n)^k                                                    |
| 21  | A045991 | Std-PolyRow3     | a(n) = n^3 - n^2                                                               |
| 22  | A062807 | Rev-TransNat0    | a(n) = Sum_{i=1..n} i*(n-i)^i                                                  |
| 23  | A062809 | Std-TransSqrs    | a(n) = Sum_{i = 1..n} (n - i)^(1 + i)                                          |
| 24  | A101495 | Std-AccSum       | Column 1 of triangle A101494                                                   |
| 25  | A104872 | Std-DiagSum      | Diagonal sums of A004248                                                       |
| 26  | A110132 | Std-ColMiddle    | a(n) = floor(n/2)^ceiling(n/2)                                                 |
| 27  | A110138 | Rev-ColMiddle    | a(n) = ceiling(n/2)^floor(n/2)                                                 |
| 28  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 29  | A265583 | Std-Diffx1       | Array T(n,k) = k*(k-1)^(n-1) read by ascending antidiagonals; k,n >= 1         |
| 30  | A349852 | Alt-TransNat0    | Expansion of Sum_{k>=0} k * x^k/(1 + k * x)                                    |
| 31  | A349853 | Alt-TransSqrs    | Expansion of Sum_{k>=0} k^2 * x^k/(1 + k * x)                                  |
| 32  | A349969 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} (k*n)^(n-k)                                                |
| 33  | A349970 | Std-PosHalf      | a(n) = Sum_{k=0..n} (2*k)^(n-k)                                                |
| 34  | A351279 | Std-PolyCol2     | a(n) = Sum_{k=0..n} 2^k * k^(n-k)                                              |
| 35  | A351282 | Std-PolyCol3     | a(n) = Sum_{k=0..n} 3^k * k^(n-k)                                              |
| 36  | A351340 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k * k^(n-k)                                              |
| 37  | A352944 | Rev-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} (n-2*k)^k                                         |
| 38  | A353016 | Rev-EvenSum      | a(n) = Sum_{k=0..floor(n/2)} (n-2*k)^(2*k)                                     |


* Statistic about Powers:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 38.
	all      A-numbers  : 88.
	missing  sequences  : 41.

[('missing', 41), ('A026898', 6), ('A000027', 6), ('A000012', 6), ('A000290', 4), ('A349970', 3), ('A174965', 3), ('A101495', 3), ('A038125', 3), ('A003992', 3), ('A003725', 3), ('A003320', 3), ('A000578', 3), ('A000312', 3), ('A000248', 3), ('A000244', 3), ('A000079', 3), ('A000007', 3), ('A351279', 2), ('A265583', 2), ('A110132', 2), ('A007778', 2), ('A004248', 2), ('A002378', 2), ('A353016', 1), ('A352944', 1), ('A351340', 1), ('A351282', 1), ('A349969', 1), ('A349853', 1), ('A349852', 1), ('A110138', 1), ('A104872', 1), ('A062809', 1), ('A062807', 1), ('A045991', 1), ('A011379', 1), ('A003101', 1), ('A000169', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Powers.html .
2025/01/11

'''
