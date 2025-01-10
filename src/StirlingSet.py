from functools import cache
from _tabltypes import MakeTriangle

"""Stirling set numbers.

[0]  1
[1]  0, 1
[2]  0, 1,   1
[3]  0, 1,   3,    1
[4]  0, 1,   7,    6,    1
[5]  0, 1,  15,   25,   10,    1
[6]  0, 1,  31,   90,   65,   15,    1
[7]  0, 1,  63,  301,  350,  140,   21,   1
[8]  0, 1, 127,  966, 1701, 1050,  266,  28,  1
[9]  0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1
"""


@cache
def stirlingset(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + stirlingset(n - 1)
    for k in range(1, n):
        row[k] = row[k] + k * row[k + 1]
    return row


@MakeTriangle(
    stirlingset,
    "StirlingSet",
    [
        "A048993",
        "A008277",
        "A008278",
        "A080417",
        "A106800",
        "A151511",
        "A151512",
        "A154959",
        "A213735",
    ],
    True,
)
def StirlingSet(n: int, k: int) -> int:
    return stirlingset(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingSet)


''' OEIS

The traits of the StirlingSet triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000110 | Std-RowSum       | Bell or exponential numbers: number of ways to partition a set of n labeled el |
| 5   | A000142 | Inv-AltSum       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000225 | Std-DiagCol2     | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 8   | A000254 | Inv-DiagCol2     | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) = (n+1)*a(n) + n!    |
| 9   | A000392 | Std-DiagCol3     | Stirling numbers of second kind S(n,3)                                         |
| 10  | A000399 | Inv-DiagCol3     | Unsigned Stirling numbers of first kind s(n,3)                                 |
| 11  | A000587 | Std-AltSum       | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 |
| 12  | A000914 | Inv-DiagRow2     | Stirling numbers of the first kind: s(n+2, n)                                  |
| 13  | A001147 | Inv-PosHalf      | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 14  | A001296 | Std-DiagRow2     | 4-dimensional pyramidal numbers: a(n) = (3*n+1)*binomial(n+2, 3)/4. Also Stirl |
| 15  | A001297 | Std-DiagRow3     | Stirling numbers of the second kind S(n+3, n)                                  |
| 16  | A001303 | Inv-DiagRow3     | Stirling numbers of first kind, s(n+3, n), negated                             |
| 17  | A001710 | Inv-EvenSum      | Order of alternating group A_n, or number of even permutations of n letters    |
| 18  | A001861 | Std-PolyCol2     | Expansion of e.g.f. exp(2*(exp(x) - 1))                                        |
| 19  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 20  | A002870 | Std-RowMax       | Largest Stirling numbers of second kind: a(n) = max_{k=1..n} S2(n,k)           |
| 21  | A004211 | Std-PosHalf      | Shifts one place left under 2nd-order binomial transform                       |
| 22  | A004212 | Rev-PolyCol3     | Shifts one place left under 3rd-order binomial transform                       |
| 23  | A005493 | Std-TransNat0    | 2-Bell numbers: a(n) = number of partitions of [n+1] with a distinguished bloc |
| 24  | A007531 | Inv-PolyRow3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 25  | A007820 | Std-CentralE     | Stirling numbers of second kind S(2n,n)                                        |
| 26  | A008544 | Inv:Rev-PolyCol3 | Triple factorial numbers: Product_{k=0..n-1} (3*k+2)                           |
| 27  | A009235 | Std-NegHalf      | E.g.f. exp( sinh(x) / exp(x) ) = exp( (1-exp(-2*x))/2 )                        |
| 28  | A014105 | Inv:Rev-PolyRow3 | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 29  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 30  | A024428 | Rev-DiagSum      | S(n,n) + S(n-1,n-2) + S(n-2,n-4) + ... + S(n-k+1,n-2k+2), where k = [ (n+1)/2  |
| 31  | A024429 | Std-OddSum       | Expansion of e.g.f. sinh(exp(x)-1)                                             |
| 32  | A024430 | Std-EvenSum      | Expansion of e.g.f. cosh(exp(x)-1)                                             |
| 33  | A027710 | Std-PolyCol3     | Number of ways of placing n labeled balls into n unlabeled (but 3-colored) box |
| 34  | A028387 | Rev-PolyRow3     | a(n) = n + (n+1)^2                                                             |
| 35  | A033445 | Std-PolyRow3     | a(n) = (n - 1)*(n^2 + n - 1)                                                   |
| 36  | A033452 | Std-TransSqrs    | "STIRLING" transform of squares A000290                                        |
| 37  | A045406 | Inv-TransSqrs    | A diagonal of A008296                                                          |
| 38  | A048993 | Std-Triangle     | Triangle of Stirling numbers of 2nd kind, S(n,k), n >= 0, 0 <= k <= n          |
| 39  | A054654 | Std-RevInv       | Triangle of Stirling numbers of 1st kind, S(n, n-k), n >= 0, 0 <= k <= n       |
| 40  | A063039 | Inv-RowLcm       | LCM of unsigned Stirling numbers of the first kind, s(n,k) for 1 <= k <= n; s( |
| 41  | A063040 | Std-RowLcm       | LCM of Stirling numbers of the second kind, S(n,k) for 1 <= k <= n; S(n,k) = n |
| 42  | A065048 | Inv-RowMax       | Largest unsigned Stirling number of the first kind: max_k(s(n+1,k)); i.e., lar |
| 43  | A089026 | Std-RowGcd       | a(n) = n if n is a prime, otherwise a(n) = 1                                   |
| 44  | A096647 | Rev-EvenSum      | Number of partitions of an n-set with even number of even blocks               |
| 45  | A096648 | Rev-OddSum       | Number of partitions of an n-set with odd number of even blocks                |
| 46  | A101851 | Alt-TransNat0    | a(n) = Sum_{k=0..n} (-1)^(n-k)*k*Stirling2(n,k)                                |
| 47  | A106800 | Std-Rev          | Triangle of Stirling numbers of 2nd kind, S(n, n-k), n >= 0, 0 <= k <= n       |
| 48  | A111673 | Rev-Poly         | Triangle, generated from A111579                                               |
| 49  | A122455 | Std-BinConv      | a(n) = Sum_{k=0..n} C(n,k)*S2(n,k). Binomial convolution of the Stirling numbe |
| 50  | A122851 | Inv-Poly         | Number triangle T(n,k) = C(k,n-k)*(n-k)!                                       |
| 51  | A129505 | Inv:Rev-CentralO | Number of permutations of 2n-1 objects with exactly n cycles                   |
| 52  | A129506 | Rev-CentralO     | Number of partitions of a {2n-1}-set into n nonempty subsets                   |
| 53  | A132393 | Std-Inv          | Triangle of unsigned Stirling numbers of the first kind (see A048994), read by |
| 54  | A154415 | Inv-ColMiddle    | The middle Stirling numbers of first kind: a(n) = Stirling1(n, floor(n/2))     |
| 55  | A171367 | Std-DiagSum      | Antidiagonal sums of triangle of Stirling numbers of 2nd kind A048993          |
| 56  | A186685 | Inv-PolyCol3     | Total number of n-digit numbers requiring 19 positive biquadrates in their rep |
| 57  | A187646 | Inv-CentralE     | (Signless) Central Stirling numbers of the first kind s(2n,n)                  |
| 58  | A189233 | Std-Poly         | Square array A(n,k), n >= 0, k >= 0, read by antidiagonals upwards, where the  |
| 59  | A211210 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n, k)*|S1(n, k)|                                  |
| 60  | A213170 | Alt-PolyCol2     | E.g.f.: exp(2*(1-exp(x)))                                                      |
| 61  | A242817 | Std-PolyDiag     | a(n) = B(n,n), where B(n,x) = Sum_{k=0..n} Stirling2(n,k)*x^k are the Bell pol |
| 62  | A247238 | Std-CentralO     | a(n) = Stirling2(2*n+1, n)                                                     |
| 63  | A278677 | Rev-TransNat0    | Popularity of left children in treeshelves avoiding pattern T231               |
| 64  | A292866 | Alt-PolyDiag     | a(n) = n! * [x^n] exp(n*(1 - exp(x)))                                          |
| 65  | A301419 | Rev-PolyDiag     | a(n) = [x^n] Sum_{k>=0} x^k/Product_{j=1..k} (1 - n*j*x)                       |
| 66  | A309084 | Alt-PolyCol3     | a(n) = exp(3) * Sum_{k>=0} (-3)^k*k^n/k!                                       |
| 67  | A317274 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n,k)*Stirling1(n,k)                               |
| 68  | A318765 | Alt-PolyRow3     | a(n) = (n + 2)*(n^2 + n - 1)                                                   |
| 69  | A331327 | Inv-AntiDiag     | T(n, k) = [x^k] Pochhammer(x, n-k) for n >= 0, 0 <= k <= floor(n/2). Irregular |
| 70  | A343278 | Rev-ColMiddle    | a(n) = Stirling2(n, ceiling(n/2))                                              |
| 71  | A343279 | Std-ColMiddle    | a(n) = Stirling2(n, floor(n/2))                                                |
| 72  | A343579 | Inv-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} |Stirling1(n - k, k)|                             |
| 73  | A343841 | Std-InvBinConv   | a(n) = Sum{k=0..n} (-1)^(n-k)*binomial(n, k)*Stirling2(n, k)                   |
| 74  | A349731 | Inv:Rev-PolyDiag | a(n) = -(-n)^n * FallingFactorial(1/n, n) for n >= 1 and a(0) = -1             |
| 75  | A353260 | Alt-DiagSum      | Expansion of Sum_{k>=0} (-1)^k * x^(2*k)/Product_{j=1..k} (1 - j * x)          |
| 76  | A359107 | Std-Acc          | Triangle read by rows, T(n, k) = Sum_{j=0..k} Stirling2(n, j) = Sum_{j=0..k} A |
| 77  | A359109 | Std-AccSum       | Row sums of the accumulated Stirling2 triangle A359107                         |
| 78  | A360174 | Inv-Diffx1       | Triangle read by rows. T(n, k) = (k + 1) * abs(Stirling1(n, k))                |
| 79  | A367777 | Inv-CentralO     | a(n) = |Stirling1(2*n + 1, n)|                                                 |
| 80  | A372803 | Alt-TransSqrs    | Expansion of e.g.f. exp(1 - exp(-x)) * (exp(-x) - 1) * (exp(-x) - 2)           |

* Statistic about StirlingSet:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 80.
	all      A-numbers  : 186.
	missing  sequences  : 29.

[('missing', 29), ('A000142', 16), ('A000012', 11), ('A000110', 9), ('A000217', 5), ('A000027', 5), ('A000007', 5), ('A132393', 4), ('A106800', 4), ('A001710', 4), ('A359109', 3), ('A343841', 3), ('A122455', 3), ('A089026', 3), ('A063040', 3), ('A054654', 3), ('A048993', 3), ('A007820', 3), ('A004211', 3), ('A002870', 3), ('A002378', 3), ('A001297', 3), ('A001296', 3), ('A001147', 3), ('A000587', 3), ('A000392', 3), ('A000225', 3), ('A359107', 2), ('A343279', 2), ('A317274', 2), ('A247238', 2), ('A213170', 2), ('A211210', 2), ('A187646', 2), ('A065048', 2), ('A063039', 2), ('A024430', 2), ('A024429', 2), ('A019590', 2), ('A009235', 2), ('A001861', 2), ('A001303', 2), ('A000914', 2), ('A000399', 2), ('A000254', 2), ('A372803', 1), ('A367777', 1), ('A360174', 1), ('A353260', 1), ('A349731', 1), ('A343579', 1), ('A343278', 1), ('A331327', 1), ('A318765', 1), ('A309084', 1), ('A301419', 1), ('A292866', 1), ('A278677', 1), ('A242817', 1), ('A189233', 1), ('A186685', 1), ('A171367', 1), ('A154415', 1), ('A129506', 1), ('A129505', 1), ('A122851', 1), ('A111673', 1), ('A101851', 1), ('A096648', 1), ('A096647', 1), ('A045406', 1), ('A033452', 1), ('A033445', 1), ('A028387', 1), ('A027710', 1), ('A024428', 1), ('A014105', 1), ('A008544', 1), ('A007531', 1), ('A005493', 1), ('A004212', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingSet.html .
2025/01/10

'''
