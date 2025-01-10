from functools import cache
from _tabltypes import MakeTriangle

"""Ordered cycle numbers.

[0] [1]
[1] [0,    1]
[2] [0,    1,     2]
[3] [0,    2,     6,     6]
[4] [0,    6,    22,    36,     24]
[5] [0,   24,   100,   210,    240,    120]
[6] [0,  120,   548,  1350,   2040,   1800,    720]
[7] [0,  720,  3528,  9744,  17640,  21000,  15120,   5040]
[8] [0, 5040, 26136, 78792, 162456, 235200, 231840, 141120, 40320]
"""


@cache
def orderedcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = orderedcycle(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row


@MakeTriangle(orderedcycle, "OrderedCycle", ["A225479", "A048594", "A075181"], False)
def OrderedCycle(n: int, k: int) -> int:
    return orderedcycle(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(OrderedCycle)


''' OEIS

The traits of the OrderedCycle triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Rev-PolyRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-ColRight     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 6   | A001286 | Std-DiagRow1     | Lah numbers: a(n) = (n-1)*n!/2                                                 |
| 7   | A006252 | Std-AltSum       | Expansion of e.g.f. 1/(1 - log(1+x))                                           |
| 8   | A007840 | Std-RowSum       | Number of factorizations of permutations of n letters into ordered cycles      |
| 9   | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 10  | A051890 | Rev-PolyRow3     | a(n) = 2*(n^2 - n + 1)                                                         |
| 11  | A052517 | Std-DiagCol2     | Number of ordered pairs of cycles over all n-permutations having two cycles    |
| 12  | A052748 | Std-DiagCol3     | Expansion of e.g.f.: -(log(1-x))^3                                             |
| 13  | A052801 | Std-AccRevSum    | A simple grammar: labeled pairs of sequences of cycles                         |
| 14  | A052811 | Std-EvenSum      | A simple grammar: sequences of pairs of cycles                                 |
| 15  | A058583 | Std-RowMax       | Max_{k=0..n} k!*|Stirling1(n,k)|                                               |
| 16  | A075182 | Std-RowGcd       | Greatest common divisors of rows of triangle A075181 and of (unsigned) triangl |
| 17  | A088500 | Std-PolyCol2     | Expansion of e.g.f. 1/(1+2*log(1-x))                                           |
| 18  | A088501 | Alt-PolyCol2     | Expansion of e.g.f. 1/(1-2*log(1+x))                                           |
| 19  | A129841 | Std-DiagSum      | Antidiagonal sums of triangle T defined in A048594: T(j,k) = k! * Stirling1(j, |
| 20  | A213829 | Alt-PolyRow3     | Principal diagonal of the convolution array A213828                            |
| 21  | A215916 | Std-TransNat0    | The total number of components (cycles) in all alignments                      |
| 22  | A225479 | Std-Triangle     | Triangle read by rows, the ordered Stirling cycle numbers, T(n, k) = k!* s(n,  |
| 23  | A227917 | Std-PosHalf      | Number of semi-increasing binary plane trees with n vertices                   |
| 24  | A238685 | Rev-CentralO     | a(n) = n! * A129505(n) * (-1)^(n+1)                                            |
| 25  | A277759 | Std-BinConv      | a(n) equals the coefficient of x^n in n!*(1 - log(1-x))^n                      |
| 26  | A308565 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n,k) * Stirling1(n,k) * k!                        |
| 27  | A317171 | Std-PolyDiag     | a(n) = n! * [x^n] 1/(1 + n*log(1 - x))                                         |
| 28  | A317172 | Alt-PolyDiag     | a(n) = n! * [x^n] 1/(1 - n*log(1 + x))                                         |
| 29  | A317280 | Alt-AccRevSum    | Expansion of e.g.f. 1/(1 - log(1 + x))^2                                       |
| 30  | A320344 | Alt-TransNat0    | Expansion of e.g.f. log(1 + x)/(1 - log(1 + x))^2                              |
| 31  | A335531 | Alt-PolyCol3     | Expansion of e.g.f. 1/(1-3*log(1+x))                                           |
| 32  | A344498 | Std-ColMiddle    | a(n) = |Stirling1(n, floor(n/2))| * floor(n/2)!                                |
| 33  | A352069 | Rev-PolyCol3     | Expansion of e.g.f. 1 / (1 + log(1 - 3*x) / 3)                                 |
| 34  | A352074 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} Stirling1(n,k) * k! * (-n)^(n-k)                           |
| 35  | A354237 | Std-NegHalf      | Expansion of e.g.f. 1 / (1 - log(1 + 2*x) / 2)                                 |
| 36  | A354263 | Std-PolyCol3     | Expansion of e.g.f. 1/(1 + 3 * log(1-x))                                       |
| 37  | A376873 | Std-CentralE     | a(n) = n! * |Stirling1(2*n, n)|                                                |

* Statistic about OrderedCycle:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 37.
	all      A-numbers  : 80.
	missing  sequences  : 45.

[('missing', 45), ('A007840', 6), ('A000142', 6), ('A376873', 3), ('A308565', 3), ('A277759', 3), ('A227917', 3), ('A075182', 3), ('A058583', 3), ('A052801', 3), ('A052748', 3), ('A052517', 3), ('A006252', 3), ('A001286', 3), ('A000027', 3), ('A000007', 3), ('A354237', 2), ('A344498', 2), ('A317280', 2), ('A225479', 2), ('A088501', 2), ('A088500', 2), ('A052811', 2), ('A354263', 1), ('A352074', 1), ('A352069', 1), ('A335531', 1), ('A320344', 1), ('A317172', 1), ('A317171', 1), ('A238685', 1), ('A215916', 1), ('A213829', 1), ('A129841', 1), ('A051890', 1), ('A014105', 1), ('A000384', 1), ('A000012', 1)]

A related webpage is: https://peterluschny.github.io/tabl/OrderedCycle.html .
2025/01/10

'''
