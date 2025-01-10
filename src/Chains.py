from functools import cache
from _tabltypes import MakeTriangle

"""Chains of length k in partially ordered set formed from subsets of n-set by inclusion.

0  [  1]
1  [  2,    1]
2  [  4,    5,     2]
3  [  8,   19,    18,     6]
4  [ 16,   65,   110,    84,    24]
5  [ 32,  211,   570,   750,   480,   120]
6  [ 64,  665,  2702,  5460,  5880,  3240,   720]
7  [128, 2059, 12138, 35406, 57120, 52080, 25200, 5040]
"""


@cache
def chains(n: int) -> list[int]:
    if n == 0:
        return [1]

    ch = chains(n - 1) + [0]
    row = ch.copy()
    row[0] = 2 * ch[0]
    row[n] = n * ch[n - 1]

    for k in range(n - 1, 0, -1):
        row[k] = k * ch[k - 1] + (k + 2) * ch[k]

    return row


@MakeTriangle(chains, "Chains", ["A038719"], False)
def Chains(n: int, k: int) -> int:
    return chains(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Chains)

''' OEIS

The traits of the Chains triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Alt-AccRevSum    | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-AltSum       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Std-ColLeft      | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000142 | Std-ColRight     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000272 | Std-BinConv      | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 7   | A000629 | Std-EvenSum      | Number of necklaces of partitions of n+1 labeled beads                         |
| 8   | A001047 | Std-DiagCol1     | a(n) = 3^n - 2^n                                                               |
| 9   | A002050 | Std-OddSum       | Number of simplices in barycentric subdivision of n-simplex                    |
| 10  | A005408 | Rev-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 11  | A007047 | Std-RowSum       | Number of chains in power set of n-set                                         |
| 12  | A010684 | Alt-TransSqrs    | Period 2: repeat (1,3); offset 0                                               |
| 13  | A038719 | Std-Triangle     | Triangle T(n,k) (0 <= k <= n) giving number of chains of length k in partially |
| 14  | A038720 | Std-DiagRow1     | a(n) = (n+3)*n!/2                                                              |
| 15  | A038721 | Std-DiagCol2     | k=2 column of A038719                                                          |
| 16  | A052841 | Alt-PolyCol2     | Expansion of e.g.f.: 1/(exp(x)*(2-exp(x)))                                     |
| 17  | A054552 | Rev-PolyRow2     | a(n) = 4*n^2 - 3*n + 1                                                         |
| 18  | A084849 | Std-PolyRow2     | a(n) = 1 + n + 2*n^2                                                           |
| 19  | A119881 | Std-NegHalf      | Expansion of e.g.f. exp(3*x)*sech(x)                                           |
| 20  | A130850 | Alt-AccRev       | Triangle read by rows, 0 <= k <= n, T(n,k) = Sum_{j=0..n} A(n,j)*binomial(n-j, |
| 21  | A130883 | Alt-PolyRow2     | a(n) = 2*n^2 - n + 1                                                           |
| 22  | A162509 | Std-AccRevSum    | Row sums of the absolute values of a triangular array related to the Bernoulli |
| 23  | A199400 | Std-Diffx1       | Triangle T(n,k), read by rows, given by (2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,...) DE |
| 24  | A368319 | Std-PolyCol2     | Expansion of e.g.f. exp(2*x) / (3 - 2*exp(x))                                  |
| 25  | A368322 | Std-PolyCol3     | Expansion of e.g.f. exp(2*x) / (4 - 3*exp(x))                                  |

* Statistic about Chains:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 25.
	all      A-numbers  : 59.
	missing  sequences  : 65.

[('missing', 65), ('A007047', 6), ('A000012', 6), ('A162509', 3), ('A038721', 3), ('A038720', 3), ('A001047', 3), ('A000272', 3), ('A000142', 3), ('A000079', 3), ('A000027', 3), ('A368319', 2), ('A199400', 2), ('A119881', 2), ('A052841', 2), ('A038719', 2), ('A002050', 2), ('A000629', 2), ('A000007', 2), ('A368322', 1), ('A130883', 1), ('A130850', 1), ('A084849', 1), ('A054552', 1), ('A010684', 1), ('A005408', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Chains.html .
2025/01/10

'''
