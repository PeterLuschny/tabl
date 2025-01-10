from functools import cache
from _tabltypes import MakeTriangle

"""Stirling cycle numbers, unsigned Stirling numbers of the 1. kind.


[0]  1
[1]  0,     1
[2]  0,     1,      1
[3]  0,     2,      3,      1
[4]  0,     6,     11,      6,     1
[5]  0,    24,     50,     35,    10,     1
[6]  0,   120,    274,    225,    85,    15,    1
[7]  0,   720,   1764,   1624,   735,   175,   21,   1
[8]  0,  5040,  13068,  13132,  6769,  1960,  322,  28,  1
[9]  0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1
"""


@cache
def stirlingcycle(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + stirlingcycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]

    return row


@MakeTriangle(
    stirlingcycle,
    "StirlingCycle",
    ["A132393", "A008275", "A008276", "A048994", "A054654", "A094638", "A130534"],
    True,
)
def StirlingCycle(n: int, k: int) -> int:
    return stirlingcycle(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingCycle)

''' OEIS

The traits of the StirlingCycle triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000110 | Inv-AltSum       | Bell or exponential numbers: number of ways to partition a set of n labeled el |
| 5   | A000142 | Std-RowSum       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000225 | Inv-DiagCol2     | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 8   | A000254 | Std-TransNat0    | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) = (n+1)*a(n) + n!    |
| 9   | A000384 | Rev-PolyRow3     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 10  | A000392 | Inv-DiagCol3     | Stirling numbers of second kind S(n,3)                                         |
| 11  | A000399 | Std-DiagCol3     | Unsigned Stirling numbers of first kind s(n,3)                                 |
| 12  | A000407 | Std-PolyDiag     | a(n) = (2*n+1)! / n!                                                           |
| 13  | A000587 | Inv-RowSum       | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 |
| 14  | A000774 | Std-AccRevSum    | a(n) = n!*(1 + Sum_{i=1..n} 1/i)                                               |
| 15  | A000914 | Std-DiagRow2     | Stirling numbers of the first kind: s(n+2, n)                                  |
| 16  | A001147 | Std-PosHalf      | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 17  | A001296 | Inv-DiagRow2     | 4-dimensional pyramidal numbers: a(n) = (3*n+1)*binomial(n+2, 3)/4. Also Stirl |
| 18  | A001297 | Inv-DiagRow3     | Stirling numbers of the second kind S(n+3, n)                                  |
| 19  | A001303 | Std-DiagRow3     | Stirling numbers of first kind, s(n+3, n), negated                             |
| 20  | A001710 | Std-EvenSum      | Order of alternating group A_n, or number of even permutations of n letters    |
| 21  | A001861 | Inv:Rev-NegHalf  | Expansion of e.g.f. exp(2*(exp(x) - 1))                                        |
| 22  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 23  | A002870 | Inv-RowMax       | Largest Stirling numbers of second kind: a(n) = max_{k=1..n} S2(n,k)           |
| 24  | A004211 | Inv-NegHalf      | Shifts one place left under 2nd-order binomial transform                       |
| 25  | A007531 | Std-PolyRow3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 26  | A007559 | Rev-PolyCol3     | Triple factorial numbers (3*n-2)!!! with leading 1 added                       |
| 27  | A007820 | Inv-CentralE     | Stirling numbers of second kind S(2n,n)                                        |
| 28  | A009235 | Inv-PosHalf      | E.g.f. exp( sinh(x) / exp(x) ) = exp( (1-exp(-2*x))/2 )                        |
| 29  | A019590 | Rev-AltSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 30  | A024429 | Inv-OddSum       | Expansion of e.g.f. sinh(exp(x)-1)                                             |
| 31  | A024430 | Inv-EvenSum      | Expansion of e.g.f. cosh(exp(x)-1)                                             |
| 32  | A028387 | Inv:Rev-PolyRow3 | a(n) = n + (n+1)^2                                                             |
| 33  | A045406 | Alt-TransSqrs    | A diagonal of A008296                                                          |
| 34  | A048993 | Std-Inv          | Triangle of Stirling numbers of 2nd kind, S(n,k), n >= 0, 0 <= k <= n          |
| 35  | A054654 | Std-Rev          | Triangle of Stirling numbers of 1st kind, S(n, n-k), n >= 0, 0 <= k <= n       |
| 36  | A063039 | Std-RowLcm       | LCM of unsigned Stirling numbers of the first kind, s(n,k) for 1 <= k <= n; s( |
| 37  | A063040 | Inv-RowLcm       | LCM of Stirling numbers of the second kind, S(n,k) for 1 <= k <= n; S(n,k) = n |
| 38  | A065048 | Std-RowMax       | Largest unsigned Stirling number of the first kind: max_k(s(n+1,k)); i.e., lar |
| 39  | A067318 | Rev-TransNat0    | Total number of transpositions in all permutations of n letters                |
| 40  | A089026 | Inv-RowGcd       | a(n) = n if n is a prime, otherwise a(n) = 1                                   |
| 41  | A092985 | Rev-PolyDiag     | a(n) is the product of first n terms of an arithmetic progression with the fir |
| 42  | A096647 | Inv:Rev-EvenSum  | Number of partitions of an n-set with even number of even blocks               |
| 43  | A096648 | Inv:Rev-OddSum   | Number of partitions of an n-set with odd number of even blocks                |
| 44  | A096747 | Std-AccRev       | Triangle read by rows: T(n,1) = 1, T(n,k) = T(n-1,k)+(n-1)*T(n-1,k-1) for 1<=k |
| 45  | A101851 | Inv-TransNat0    | a(n) = Sum_{k=0..n} (-1)^(n-k)*k*Stirling2(n,k)                                |
| 46  | A106800 | Std-RevInv       | Triangle of Stirling numbers of 2nd kind, S(n, n-k), n >= 0, 0 <= k <= n       |
| 47  | A121586 | Std-AccSum       | Number of columns in all deco polyominoes of height n. A deco polyomino is a d |
| 48  | A122455 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} C(n,k)*S2(n,k). Binomial convolution of the Stirling numbe |
| 49  | A122851 | Alt-Poly         | Number triangle T(n,k) = C(k,n-k)*(n-k)!                                       |
| 50  | A124380 | Rev-DiagSum      | O.g.f.: A(x) = Sum_{n>=0} x^n*Product_{k=0..n} (1 + k*x)                       |
| 51  | A129505 | Rev-CentralO     | Number of permutations of 2n-1 objects with exactly n cycles                   |
| 52  | A129506 | Inv:Rev-CentralO | Number of partitions of a {2n-1}-set into n nonempty subsets                   |
| 53  | A132393 | Std-Triangle     | Triangle of unsigned Stirling numbers of the first kind (see A048994), read by |
| 54  | A151881 | Std-TransSqrs    | Sum (number of cycles)^2 over all n! permutations of [1..n]                    |
| 55  | A154415 | Std-ColMiddle    | The middle Stirling numbers of first kind: a(n) = Stirling1(n, floor(n/2))     |
| 56  | A171367 | Inv-DiagSum      | Antidiagonal sums of triangle of Stirling numbers of 2nd kind A048993          |
| 57  | A186685 | Alt-PolyCol3     | Total number of n-digit numbers requiring 19 positive biquadrates in their rep |
| 58  | A187646 | Std-CentralE     | (Signless) Central Stirling numbers of the first kind s(2n,n)                  |
| 59  | A211210 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*|S1(n, k)|                                  |
| 60  | A213170 | Inv-PolyCol2     | E.g.f.: exp(2*(1-exp(x)))                                                      |
| 61  | A247238 | Inv-CentralO     | a(n) = Stirling2(2*n+1, n)                                                     |
| 62  | A256268 | Rev-Poly         | Table of k-fold factorials, read by antidiagonals                              |
| 63  | A292866 | Inv-PolyDiag     | a(n) = n! * [x^n] exp(n*(1 - exp(x)))                                          |
| 64  | A309084 | Inv-PolyCol3     | a(n) = exp(3) * Sum_{k>=0} (-3)^k*k^n/k!                                       |
| 65  | A317274 | Std-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n,k)*Stirling1(n,k)                               |
| 66  | A317996 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp((1 - exp(-3*x))/3)                                     |
| 67  | A318183 | Inv:Rev-PolyDiag | a(n) = [x^n] Sum_{k>=0} x^k/Product_{j=1..k} (1 + n*j*x)                       |
| 68  | A318765 | Inv-PolyRow3     | a(n) = (n + 2)*(n^2 + n - 1)                                                   |
| 69  | A331327 | Std-AntiDiag     | T(n, k) = [x^k] Pochhammer(x, n-k) for n >= 0, 0 <= k <= floor(n/2). Irregular |
| 70  | A343278 | Inv:Rev-ColMiddl | a(n) = Stirling2(n, ceiling(n/2))                                              |
| 71  | A343279 | Inv-ColMiddle    | a(n) = Stirling2(n, floor(n/2))                                                |
| 72  | A343579 | Std-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} |Stirling1(n - k, k)|                             |
| 73  | A343841 | Inv-BinConv      | a(n) = Sum{k=0..n} (-1)^(n-k)*binomial(n, k)*Stirling2(n, k)                   |
| 74  | A349782 | Std-Acc          | Triangle read by rows, T(n, k) = Sum_{j=0..k} |Stirling1(n, j)|                |
| 75  | A353253 | Alt-DiagSum      | Expansion of Sum_{k>=0} x^k * Product_{j=0..k-1} (j - x)                       |
| 76  | A360174 | Std-Diffx1       | Triangle read by rows. T(n, k) = (k + 1) * abs(Stirling1(n, k))                |
| 77  | A367777 | Std-CentralO     | a(n) = |Stirling1(2*n + 1, n)|                                                 |
| 78  | A372803 | Inv-TransSqrs    | Expansion of e.g.f. exp(1 - exp(-x)) * (exp(-x) - 1) * (exp(-x) - 2)           |

* Statistic about StirlingCycle:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 78.
	all      A-numbers  : 179.
	missing  sequences  : 30.

[('missing', 30), ('A000142', 16), ('A000012', 9), ('A001710', 7), ('A001147', 5), ('A000217', 5), ('A000027', 5), ('A000007', 5), ('A048993', 4), ('A000254', 4), ('A000110', 4), ('A317274', 3), ('A211210', 3), ('A187646', 3), ('A121586', 3), ('A106800', 3), ('A065048', 3), ('A063039', 3), ('A054654', 3), ('A002378', 3), ('A001303', 3), ('A000914', 3), ('A000774', 3), ('A000399', 3), ('A367777', 2), ('A360174', 2), ('A349782', 2), ('A343841', 2), ('A331327', 2), ('A213170', 2), ('A154415', 2), ('A132393', 2), ('A122455', 2), ('A096747', 2), ('A089026', 2), ('A063040', 2), ('A009235', 2), ('A007820', 2), ('A007531', 2), ('A002870', 2), ('A001297', 2), ('A001296', 2), ('A000587', 2), ('A000392', 2), ('A000225', 2), ('A372803', 1), ('A353253', 1), ('A343579', 1), ('A343279', 1), ('A343278', 1), ('A318765', 1), ('A318183', 1), ('A317996', 1), ('A309084', 1), ('A292866', 1), ('A256268', 1), ('A247238', 1), ('A186685', 1), ('A171367', 1), ('A151881', 1), ('A129506', 1), ('A129505', 1), ('A124380', 1), ('A122851', 1), ('A101851', 1), ('A096648', 1), ('A096647', 1), ('A092985', 1), ('A067318', 1), ('A045406', 1), ('A028387', 1), ('A024430', 1), ('A024429', 1), ('A019590', 1), ('A007559', 1), ('A004211', 1), ('A001861', 1), ('A000407', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingCycle.html .
2025/01/10

'''
