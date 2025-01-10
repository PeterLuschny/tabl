from functools import cache
from _tabltypes import MakeTriangle

"""
T(n, k) = if k == 0 then 0^n else binomial(n-1, k-1) * Bell(n - k)

[0]     1
[1]     1,    1
[2]     2,    2,    1
[3]     5,    6,    3,    1
[4]    15,   20,   12,    4,    1
[5]    52,   75,   50,   20,    5,   1
[6]   203,  312,  225,  100,   30,   6,  1
[7]   877, 1421, 1092,  525,  175,  42,  7, 1
[8]  4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1
"""


@cache
def binomialbell(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    a = binomialbell(n - 1) + [1]
    s = sum(a) - 1

    for j in range(n - 1, 0, -1):
        a[j] = (a[j - 1] * n) // j
    a[0] = s

    return a


@MakeTriangle(binomialbell, "BinomialBell", ["A056857", "A056860"], True)
def BinomialBell(n: int, k: int) -> int:
    return binomialbell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialBell)

''' OEIS

The traits of the BinomialBell triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000110 | Std-RowSum       | Bell or exponential numbers: number of ways to partition a set of n labeled el |
| 4   | A000292 | Inv-DiagRow3     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 5   | A000296 | Std-AltSum       | Set partitions without singletons: number of partitions of an n-set into block |
| 6   | A000587 | Inv-RowSum       | Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 |
| 7   | A001844 | Rev-PolyRow2     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 8   | A002378 | Std-DiagRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 9   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 10  | A005408 | Inv:Rev-PolyRow2 | The odd numbers: a(n) = 2*n + 1                                                |
| 11  | A005491 | Std-PolyRow3     | a(n) = n^3 + 3*n + 1                                                           |
| 12  | A005493 | Std-PolyCol2     | 2-Bell numbers: a(n) = number of partitions of [n+1] with a distinguished bloc |
| 13  | A005494 | Std-PolyCol3     | 3-Bell numbers: E.g.f.: exp(3*z + exp(z) - 1)                                  |
| 14  | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 15  | A052889 | Std-DiagCol1     | Number of rooted set partitions                                                |
| 16  | A056857 | Std-Triangle     | Triangle read by rows: T(n,c) = number of successive equalities in set partiti |
| 17  | A056860 | Std-Rev          | Triangle T(n,k) = number of element-subset partitions of {1..n} with n-k+1 equ |
| 18  | A070071 | Std-TransNat0    | a(n) = n*B(n), where B(n) are the Bell numbers, A000110                        |
| 19  | A074051 | Inv-PolyCol2     | For each n there are uniquely determined numbers a(n) and b(n) and a polynomia |
| 20  | A102286 | Std-OddSum       | Total number of odd blocks in all partitions of n-set                          |
| 21  | A105479 | Std-DiagCol2     | a(n) = C(n,2)*Bell(n-2) (cf. A000217, A000110)                                 |
| 22  | A105480 | Std-DiagCol3     | Number of partitions of {1...n} containing 3 pairs of consecutive integers, wh |
| 23  | A108087 | Std-Poly         | Array, read by antidiagonals, where A(n,k) = exp(-1)*Sum_{i>=0} (i+k)^n/i!     |
| 24  | A109747 | Inv-AltSum       | E.g.f.: exp(-exp(-x)+1+x)                                                      |
| 25  | A124102 | Std-CentralE     | a(n) = C(2n,n)*Bell(n)                                                         |
| 26  | A124311 | Std-NegHalf      | a(n) = Sum_{i=0..n} (-2)^i*binomial(n,i)*B(i) where B(n) = Bell numbers A00011 |
| 27  | A124427 | Std-AccRevSum    | Sum of the sizes of the blocks containing the element 1 in all set partitions  |
| 28  | A126390 | Std-PosHalf      | a(n) = Sum_{i=0..n} 2^i*B(i)*binomial(n,i) where B(n) = Bell numbers A000110(n |
| 29  | A126617 | Alt-PolyCol2     | a(n) = Sum_{i=0..n} (-2)^(n-i)*B(i)*binomial(n,i) where B(n) = Bell numbers A0 |
| 30  | A127741 | Rev-TransNat0    | a(n) = (n+1) * A005493(n)                                                      |
| 31  | A129334 | Std-Inv          | Triangle T(n,k) read by rows: inverse of the matrix PE = exp(P)/exp(1) given i |
| 32  | A134481 | Std-DiagRow3     | Row sums of triangle A134480                                                   |
| 33  | A134980 | Std-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,k)*n^(n-k)*A000110(k)                           |
| 34  | A143987 | Std-RevInv       | Eigentriangle of (A007318)^(-1); row sums = A014182, exp(1-x-exp(-x))          |
| 35  | A153732 | Inv:Rev-NegHalf  | Binomial transform of A109747                                                  |
| 36  | A175716 | Std-TransSqrs    | The total number of elements(ordered pairs) in all equivalence relations on {1 |
| 37  | A177058 | Inv:Rev-PolyRow3 | a(n) = n^3 - 3n^2 + 3                                                          |
| 38  | A184175 | Alt-DiagSum      | Number of set partitions of {1,2,...,n} having no blocks of the form {i, i+1}  |
| 39  | A193683 | Inv-PolyCol3     | Alternating row sums of Sheffer triangle A143495 (3-restricted Stirling2 numbe |
| 40  | A224271 | Std-EvenSum      | Number of set partitions of {1,2,...,n} such that the element 1 is in an odd-s |
| 41  | A250105 | Alt-TransNat0    | Column 1 of triangle in A250104 (or A124323)                                   |
| 42  | A284859 | Rev-PolyCol3     | Row sums of the Sheffer triangle (exp(x), exp(3*x)-1) given in A282629         |
| 43  | A284860 | Inv:Rev-PolyCol3 | Alternating row sums of the Sheffer triangle (exp(x), exp(3*x) - 1) given in A |
| 44  | A290219 | Alt-PolyDiag     | a(n) = n! * [x^n] exp(exp(x) - n*x - 1)                                        |
| 45  | A297926 | Std-CentralO     | Number of set partitions of [2n] in which the size of the first block is n     |
| 46  | A298373 | Inv-PolyDiag     | a(n) = n! * [x^n] exp(n*x - exp(x) + 1)                                        |
| 47  | A303586 | Rev-DiagSum      | Number of partitions of [n] that contain no isolated singletons                |
| 48  | A307066 | Rev-PolyDiag     | a(n) = exp(-1) * Sum_{k>=0} (n*k + 1)^n/k!                                     |
| 49  | A307080 | Inv:Rev-PolyDiag | a(n) = exp(1) * Sum_{k>=0} (-1)^k*(n*k + 1)^n/k!                               |
| 50  | A308645 | Inv-PosHalf      | Expansion of e.g.f. exp(1 + x - exp(2*x))                                      |
| 51  | A346738 | Alt-PolyCol3     | Expansion of e.g.f.: exp(exp(x) - 3*x - 1)                                     |
| 52  | A367743 | Inv-NegHalf      | Expansion of e.g.f. exp(1 - x - exp(2*x))                                      |

* Statistic about BinomialBell:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 52.
	all      A-numbers  : 114.
	missing  sequences  : 99.

[('missing', 99), ('A000027', 10), ('A000110', 9), ('A129334', 4), ('A056860', 4), ('A000587', 4), ('A000012', 4), ('A143987', 3), ('A134481', 3), ('A126390', 3), ('A124427', 3), ('A124102', 3), ('A105480', 3), ('A105479', 3), ('A056857', 3), ('A052889', 3), ('A002378', 3), ('A000296', 3), ('A308645', 2), ('A297926', 2), ('A224271', 2), ('A126617', 2), ('A124311', 2), ('A109747', 2), ('A102286', 2), ('A074051', 2), ('A005493', 2), ('A002522', 2), ('A000292', 2), ('A367743', 1), ('A346738', 1), ('A307080', 1), ('A307066', 1), ('A303586', 1), ('A298373', 1), ('A290219', 1), ('A284860', 1), ('A284859', 1), ('A250105', 1), ('A193683', 1), ('A184175', 1), ('A177058', 1), ('A175716', 1), ('A153732', 1), ('A134980', 1), ('A127741', 1), ('A108087', 1), ('A070071', 1), ('A005563', 1), ('A005494', 1), ('A005491', 1), ('A005408', 1), ('A001844', 1)]

A related webpage is: https://peterluschny.github.io/tabl/BinomialBell.html .
2025/01/10

'''
