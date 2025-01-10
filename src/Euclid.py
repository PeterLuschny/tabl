from functools import cache
from _tabltypes import MakeTriangle

"""Euclid's triangle.

[ 0] [0]
[ 1] [1, 1]
[ 2] [0, 1, 0]
[ 3] [0, 1, 1, 0]
[ 4] [0, 1, 0, 1, 0]
[ 5] [0, 1, 1, 1, 1, 0]
[ 6] [0, 1, 0, 0, 0, 1, 0]
[ 7] [0, 1, 1, 1, 1, 1, 1, 0]
[ 8] [0, 1, 0, 1, 0, 1, 0, 1, 0]
[ 9] [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
[10] [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
[11] [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
"""


@cache
def _euclid(n: int, k: int) -> int:
    while k != 0:
        t = k
        k = n % k
        n = t
    return 1 if n == 1 else 0


@cache
def euclid(n: int) -> list[int]:
    return [_euclid(i, n) for i in range(n + 1)]


@MakeTriangle(euclid, "Euclid", ["A217831"], False)
def Euclid(n: int, k: int) -> int:
    return euclid(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Euclid, 12)
    # for n in range(22): print([n], euclid(n))
    # print([sum(euclid(n)) for n in range(53)])

''' OEIS

The traits of the Euclid triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000010 | Std-RowSum       | Euler totient function phi(n): count numbers <= n and prime to n               |
| 2   | A000012 | Std-RowLcm       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Std-ColMiddle    | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A002378 | Std-PolyRow3     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 6   | A011655 | Std-DiagRow3     | Period 3: repeat [0, 1, 1]                                                     |
| 7   | A023022 | Std-DiagSum      | Number of partitions of n into two relatively prime parts. After initial term, |
| 8   | A023896 | Std-TransNat0    | Sum of positive integers in smallest positive reduced residue system modulo n. |
| 9   | A053818 | Std-TransSqrs    | a(n) = Sum_{k=1..n, gcd(n,k) = 1} k^2                                          |
| 10  | A055034 | Std-OddSum       | a(1) = 1, a(n) = phi(2*n)/2 for n > 1                                          |
| 11  | A056188 | Std-BinConv      | a(1) = 1; for n>1, sum of binomial(n,k) as k runs over RRS(n), the reduced res |
| 12  | A062570 | Std-AltSum       | a(n) = phi(2*n)                                                                |
| 13  | A063524 | Std-ColLeft      | Characteristic function of 1                                                   |
| 14  | A092790 | Std-AccSum       | a(n) = (n+1)*phi(n-1)/2                                                        |
| 15  | A209229 | Std-CentralE     | Characteristic function of powers of 2, cf. A000079                            |
| 16  | A217831 | Std-Triangle     | Euclid's triangle read by rows. T(n, k) = 1 if k is prime to n, otherwise 0    |
| 17  | A325887 | Alt-TransNat0    | Excess of sum of odd integers up to n and coprime to n over sum of even intege |
| 18  | A349136 | Std-EvenSum      | Moebius transform of Kimberling's paraphrases, A003602                         |
| 19  | A367544 | Std-PosHalf      | Euclid's triangle A217831 represented as decimal numbers                       |
| 20  | A367545 | Std-NegHalf      | a(n) = Sum_{k=0..n} (-2)^k * |(n - k | k)|, where (a | b) denotes the Kronecke |
| 21  | A367546 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k * |(n - k | k)|, where (a | b) denotes the Kronecker s |
| 22  | A378068 | Std-Acc          | Table read by row: T(n, k) = Sum_{j=0..k} A217831(n, j). Partial row sums of E |

* Statistic about Euclid:

	Triangles considered: ['Std', 'Alt'].
	distinct A-numbers  : 22.
	all      A-numbers  : 63.
	missing  sequences  : 18.

[('missing', 18), ('A000012', 10), ('A000035', 6), ('A217831', 4), ('A063524', 4), ('A000027', 4), ('A000010', 4), ('A367545', 3), ('A367544', 3), ('A092790', 3), ('A011655', 3), ('A378068', 2), ('A349136', 2), ('A209229', 2), ('A062570', 2), ('A056188', 2), ('A055034', 2), ('A002378', 2), ('A367546', 1), ('A325887', 1), ('A053818', 1), ('A023896', 1), ('A023022', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Euclid.html .
2025/01/10

'''
