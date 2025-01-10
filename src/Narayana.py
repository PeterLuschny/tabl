from functools import cache
from _tabltypes import MakeTriangle


"""Narayana triangle.


[0]  1;
[1]  0,  1;
[2]  0,  1,   1;
[3]  0,  1,   3,    1;
[4]  0,  1,   6,    6,     1;
[5]  0,  1,  10,   20,    10,     1;
[6]  0,  1,  15,   50,    50,    15,     1;
[7]  0,  1,  21,  105,   175,   105,    21,    1;
[8]  0,  1,  28,  196,   490,   490,   196,   28,   1;
[9]  0,  1,  36,  336,  1176,  1764,  1176,  336,  36,  1;
"""


@cache
def narayana(n: int) -> list[int]:
    if n < 3:
        return [[1], [0, 1], [0, 1, 1]][n]

    a = narayana(n - 2) + [0, 0]
    row = narayana(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = (
            (row[k] + row[k - 1]) * (2 * n - 1)
            - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 2)
        ) // (n + 1)

    return row


@MakeTriangle(narayana, "Narayana", ["A090181", "A001263", "A131198"], True)
def Narayana(n: int, k: int) -> int:
    return narayana(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Narayana)

''' OEIS

The traits of the Narayana triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000108 | Std-RowSum       | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 5   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000891 | Rev-CentralO     | a(n) = (2*n)!*(2*n+1)! / (n! * (n+1)!)^2                                       |
| 7   | A001003 | Std-PosHalf      | Schroeder's second problem (generalized parentheses); also called super-Catala |
| 8   | A001405 | Alt-AccSum       | a(n) = binomial(n, floor(n/2))                                                 |
| 9   | A001700 | Std-AccSum       | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 10  | A002054 | Rev-TransNat0    | Binomial coefficient C(2n+1, n-1)                                              |
| 11  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A002415 | Std-DiagRow2     | 4-dimensional pyramidal numbers: a(n) = n^2*(n^2-1)/12                         |
| 13  | A004148 | Std-DiagSum      | Generalized Catalan numbers: a(n+1) = a(n) + Sum_{k=1..n-1} a(k)*a(n-1-k)      |
| 14  | A005558 | Std-RowMax       | a(n) is the number of n-step walks on square lattice such that 0 <= y <= x at  |
| 15  | A006318 | Std-PolyCol2     | Large Schroeder numbers (or large Schroeder numbers, or big Schroeder numbers) |
| 16  | A006542 | Std-DiagRow3     | a(n) = binomial(n,3)*binomial(n-1,3)/4                                         |
| 17  | A007531 | Inv-PolyRow3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 18  | A007564 | Rev-PolyCol3     | Shifts left when INVERT transform applied thrice                               |
| 19  | A008550 | Rev-Poly         | Table T(n,k), n>=0 and k>=0, read by antidiagonals: the k-th column given by t |
| 20  | A008911 | Inv-DiagRow2     | a(n) = n^2*(n^2 - 1)/6                                                         |
| 21  | A014105 | Inv:Rev-PolyRow3 | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 22  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 23  | A028387 | Rev-PolyRow3     | a(n) = n + (n+1)^2                                                             |
| 24  | A033445 | Std-PolyRow3     | a(n) = (n - 1)*(n^2 + n - 1)                                                   |
| 25  | A034267 | Rev-TransSqrs    | a(n)=f(n,n) where f is given in A034261                                        |
| 26  | A046715 | Std-CentralO     | Secondary root edges in doubly rooted tree maps with n edges                   |
| 27  | A047891 | Std-PolyCol3     | Number of planar rooted trees with n nodes and tricolored end nodes            |
| 28  | A071684 | Std-OddSum       | Number of plane trees with n edges and having an odd number of leaves          |
| 29  | A071688 | Std-EvenSum      | Number of plane trees with even number of leaves                               |
| 30  | A090181 | Std-Triangle     | Triangle of Narayana (A001263) with 0 <= k <= n, read by rows                  |
| 31  | A091593 | Std-NegHalf      | Reversion of Jacobsthal numbers A001045                                        |
| 32  | A103365 | Inv-DiagCol1     | First column of triangle A103364, which equals the matrix inverse of the Naray |
| 33  | A103366 | Inv-RowMax       | Second column of triangle A103364, which equals the matrix inverse of the Nara |
| 34  | A103367 | Inv-AltSum       | Absolute row sums of triangle A103364, which equals the matrix inverse of the  |
| 35  | A125558 | Std-CentralE     | Central column of triangle A090181                                             |
| 36  | A126120 | Std-AltSum       | Catalan numbers (A000108) interpolated with 0's                                |
| 37  | A129509 | Alt-DiagSum      | G.f.: (1+x+x^2-sqrt(1+2x+3x^2-2x^3+x^4))/2                                     |
| 38  | A131490 | Inv-AccSum       | Appears in Taylor series of powers of generalized Bessel functions             |
| 39  | A141222 | Std-TransSqrs    | Expansion of -1/(2*x) + (2*x-1)^2/(2*x*(1-4x)^(3/2))                           |
| 40  | A152681 | Alt-PolyCol2     | [x^(n+1)]Reversion[x*(1-x)/(1-3*x)]                                            |
| 41  | A189176 | Std-AccRevSum    | Row sums of the Riordan matrix (1+x/sqrt(1-4*x),(1-sqrt(1-4*x))/2) (A189175)   |
| 42  | A242369 | Rev-PolyDiag     | a(n) = P(n, 1, -2*n-1, 1-2*n)/(n+1), P the Jacobi polynomial                   |
| 43  | A318765 | Alt-PolyRow3     | a(n) = (n + 2)*(n^2 + n - 1)                                                   |
| 44  | A349740 | Std-Acc          | Number of partitions of set [n] in a set of <= k noncrossing subsets. Number o |
| 45  | A367270 | Rev-Diffx1       | Triangle read by rows. T(n, k) = binomial(n, k)*binomial(n - 1, n - k - 1)     |

* Statistic about Narayana:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 45.
	all      A-numbers  : 132.
	missing  sequences  : 83.

[('missing', 83), ('A000012', 11), ('A131490', 9), ('A000217', 8), ('A090181', 7), ('A002415', 6), ('A000108', 6), ('A000027', 5), ('A000007', 5), ('A103367', 4), ('A103366', 4), ('A005558', 4), ('A001700', 4), ('A189176', 3), ('A126120', 3), ('A125558', 3), ('A071688', 3), ('A071684', 3), ('A006542', 3), ('A002378', 3), ('A001003', 3), ('A349740', 2), ('A152681', 2), ('A103365', 2), ('A091593', 2), ('A046715', 2), ('A019590', 2), ('A008911', 2), ('A006318', 2), ('A004148', 2), ('A001405', 2), ('A367270', 1), ('A318765', 1), ('A242369', 1), ('A141222', 1), ('A129509', 1), ('A047891', 1), ('A034267', 1), ('A033445', 1), ('A028387', 1), ('A014105', 1), ('A008550', 1), ('A007564', 1), ('A007531', 1), ('A002054', 1), ('A000891', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Narayana.html .
2025/01/10

'''
