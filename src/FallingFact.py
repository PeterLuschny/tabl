from functools import cache
from _tabltypes import MakeTriangle

"""Falling factorial, number of permutations of n things k at a time.

[0]  1
[1]  1,  1
[2]  1,  2,  2
[3]  1,  3,  6,   6
[4]  1,  4, 12,  24,   24
[5]  1,  5, 20,  60,  120,  120
[6]  1,  6, 30, 120,  360,  720,  720
"""


@cache
def fallingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = fallingfactorial(n - 1)
    row = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row


@MakeTriangle(fallingfactorial, "FallingFact",
             ["A008279", "A068424", "A094587", "A173333", "A181511"],
             False)
def FallingFactorial(n: int, k: int) -> int:
    return fallingfactorial(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(FallingFactorial)

''' OEIS

The traits of the FallingFact triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Rev:Inv-CentralO | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000023 | Std-NegHalf      | Expansion of e.g.f. exp(-2*x)/(1-x)                                            |
| 4   | A000027 | Std-RowGcd       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 5   | A000142 | Std-RowLcm       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000166 | Std-AltSum       | Subfactorial or rencontres numbers, or derangements: number of permutations of |
| 7   | A000180 | Alt-PolyCol3     | Expansion of E.g.f. exp(-x)/(1-3x)                                             |
| 8   | A000255 | Alt-AccRevSum    | a(n) = n*a(n-1) + (n-1)*a(n-2), a(0) = 1, a(1) = 1                             |
| 9   | A000354 | Alt-PolyCol2     | Expansion of e.g.f. exp(-x)/(1-2*x)                                            |
| 10  | A000407 | Rev-CentralO     | a(n) = (2*n+1)! / n!                                                           |
| 11  | A000522 | Std-RowSum       | Total number of ordered k-tuples (k=0..n) of distinct elements from an n-eleme |
| 12  | A001339 | Std-AccRevSum    | a(n) = Sum_{k=0..n} (k+1)! binomial(n,k)                                       |
| 13  | A001710 | Std-DiagRow2     | Order of alternating group A_n, or number of even permutations of n letters    |
| 14  | A001715 | Std-DiagRow3     | a(n) = n!/6                                                                    |
| 15  | A001813 | Std-CentralE     | Quadruple factorial numbers: a(n) = (2n)!/n!                                   |
| 16  | A001844 | Std-PolyRow2     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 17  | A002378 | Std-DiagCol2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 18  | A002522 | Rev-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 19  | A002720 | Std-BinConv      | Number of partial permutations of an n-set; number of n X n binary matrices wi |
| 20  | A002747 | Std-OddSum       | Logarithmic numbers                                                            |
| 21  | A003470 | Rev-DiagSum      | a(n) = n*a(n-1) - a(n-2) + 1 + (-1)^n                                          |
| 22  | A005408 | Rev:Inv-AccSum   | The odd numbers: a(n) = 2*n + 1                                                |
| 23  | A005563 | Rev:Inv-BinConv  | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 24  | A006963 | Std-CentralO     | Number of planar embedded labeled trees with n nodes: (2*n-3)!/(n-1)! for n >= |
| 25  | A007526 | Rev-TransNat0    | a(n) = n(a(n-1) + 1), a(0) = 0                                                 |
| 26  | A007531 | Std-DiagCol3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 27  | A008279 | Std-Triangle     | Triangle T(n,k) = n!/(n-k)! (0 <= k <= n) read by rows, giving number of permu |
| 28  | A009179 | Rev-EvenSum      | E.g.f. cosh(x)/(1+x)                                                           |
| 29  | A009940 | Std-InvBinConv   | a(n) = n!*L_{n}(1), where L_{n}(x) is the n-th Laguerre polynomial             |
| 30  | A010842 | Std-PosHalf      | Expansion of e.g.f.: exp(2*x)/(1-x)                                            |
| 31  | A010844 | Std-PolyCol2     | a(n) = 2*n*a(n-1) + 1 with a(0) = 1                                            |
| 32  | A010845 | Std-PolyCol3     | a(n) = 3*n*a(n-1) + 1, a(0) = 1                                                |
| 33  | A028387 | Rev:Inv-AccRevSu | a(n) = n + (n+1)^2                                                             |
| 34  | A030297 | Rev-TransSqrs    | a(n) = n*(n + a(n-1)) with a(0)=0                                              |
| 35  | A053486 | Rev-PolyCol3     | E.g.f.: exp(3x)/(1-x)                                                          |
| 36  | A057979 | Rev:Inv-DiagSum  | a(n) = 1 for even n and (n-1)/2 for odd n                                      |
| 37  | A058922 | Rev:Inv-PolyCol2 | a(n) = n*2^n - 2^n                                                             |
| 38  | A063170 | Rev-PolyDiag     | Schenker sums with n-th term                                                   |
| 39  | A072374 | Std-DiagSum      | a(1) = 1; a(n) = 1 + Sum_{i=1..n} Product_{j=i..2*i-1} (n-j)                   |
| 40  | A081125 | Rev-ColMiddle    | a(n) = n! / floor(n/2)!                                                        |
| 41  | A087208 | Std-EvenSum      | Expansion of e.g.f.: exp(x)/(1-x^2)                                            |
| 42  | A093178 | Rev:Inv-EvenSum  | If n is even then 1, otherwise n                                               |
| 43  | A093964 | Std-TransNat0    | a(n) = Sum_{k=1..n} k*k!*C(n,k)                                                |
| 44  | A094587 | Std-Rev          | Triangle of permutation coefficients arranged with 1's on the diagonal. Also,  |
| 45  | A111063 | Std-AccSum       | a(0) = 1; a(n) = (n-1)*a(n-1) + n                                              |
| 46  | A121757 | Std-Diffx1       | Triangle read by rows: multiply Pascal's triangle by 1,2,6,24,120,720,... = A0 |
| 47  | A124625 | Rev:Inv-OddSum   | Even numbers sandwiched between 1's                                            |
| 48  | A127701 | Rev-RevInv       | Infinite lower triangular matrix with (1, 2, 3, ...) in the main diagonal, (1, |
| 49  | A128229 | Std-InvRev       | A natural number transform, inverse of signed A094587                          |
| 50  | A130706 | Rev:Inv-CentralE | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 51  | A130779 | Rev:Inv-ColMiddl | a(0)=a(1)=1, a(2)=2, a(n)=0 for n >= 3                                         |
| 52  | A134558 | Rev-Poly         | Array read by antidiagonals, a(n,k) = gamma(n+1,k)*e^k, where gamma(n,k) is th |
| 53  | A169585 | Rev:Inv-DiagCol2 | A000004 preceded by 1, 3                                                       |
| 54  | A186763 | Rev-OddSum       | Number of increasing odd cycles in all permutations of {1,2,...,n}             |
| 55  | A205825 | Std-ColMiddle    | a(n) = n!/ceiling(n/2)!                                                        |
| 56  | A261595 | Rev:Inv-DiagCol3 | Triangular array T(n, k) read by rows (n >= 1, 1 <= k <= n): row n gives the l |
| 57  | A277452 | Std-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,k) * n^k * k!                                   |
| 58  | A318765 | Rev:Inv-TransSqr | a(n) = (n + 2)*(n^2 + n - 1)                                                   |
| 59  | A319392 | Alt-PolyDiag     | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n,k)*k!*n^k                            |
| 60  | A343276 | Std-TransSqrs    | a(n) = n! * [x^n] -x*(x + 1)*exp(x)/(x - 1)^3                                  |
| 61  | A344391 | Std-AntiDiag     | T(n, k) = binomial(n - k, k) * factorial(k), for n >= 0 and 0 <= k <= floor(n/ |
| 62  | A347667 | Std-Acc          | Triangle read by rows: T(n,k) = Sum_{j=0..k} binomial(n,j) * j! (0 <= k <= n)  |
| 63  | A358603 | Alt-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} (-1)^k * (n-k)!/(n-2*k)!                          |
| 64  | A367962 | Std-AccRev       | Triangle read by rows. T(n, k) = Sum_{j=0..k} (n!/j!)                          |

* Statistic about FallingFact:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 64.
	all      A-numbers  : 153.
	missing  sequences  : 17.

[('missing', 17), ('A000027', 17), ('A000142', 12), ('A000522', 6), ('A000012', 5), ('A128229', 4), ('A094587', 4), ('A000166', 4), ('A111063', 3), ('A010842', 3), ('A009940', 3), ('A008279', 3), ('A007531', 3), ('A005563', 3), ('A005408', 3), ('A002720', 3), ('A002378', 3), ('A001813', 3), ('A001715', 3), ('A001710', 3), ('A001339', 3), ('A367962', 2), ('A347667', 2), ('A344391', 2), ('A205825', 2), ('A130706', 2), ('A127701', 2), ('A121757', 2), ('A087208', 2), ('A028387', 2), ('A010844', 2), ('A006963', 2), ('A002747', 2), ('A002522', 2), ('A001844', 2), ('A000354', 2), ('A000255', 2), ('A000023', 2), ('A000007', 2), ('A358603', 1), ('A343276', 1), ('A319392', 1), ('A318765', 1), ('A277452', 1), ('A261595', 1), ('A186763', 1), ('A169585', 1), ('A134558', 1), ('A130779', 1), ('A124625', 1), ('A093964', 1), ('A093178', 1), ('A081125', 1), ('A072374', 1), ('A063170', 1), ('A058922', 1), ('A057979', 1), ('A053486', 1), ('A030297', 1), ('A010845', 1), ('A009179', 1), ('A007526', 1), ('A003470', 1), ('A000407', 1), ('A000180', 1)]

A related webpage is: https://peterluschny.github.io/tabl/FallingFact.html .
2025/01/10

'''
