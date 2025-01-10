from functools import cache
from _tabltypes import MakeTriangle

"""Delannoy triangle.

[0] [1]
[1] [1,  1]
[2] [1,  3,   1]
[3] [1,  5,   5,   1]
[4] [1,  7,  13,   7,   1]
[5] [1,  9,  25,  25,   9,   1]
[6] [1, 11,  41,  63,  41,  11,   1]
[7] [1, 13,  61, 129, 129,  61,  13,   1]
[8] [1, 15,  85, 231, 321, 231,  85,  15,  1]
[9] [1, 17, 113, 377, 681, 681, 377, 113, 17, 1]
"""


@cache
def delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    rov = delannoy(n - 2)
    row = delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rov[k - 1]
    return row


@MakeTriangle(delannoy, "Delannoy", ["A008288"], True)
def Delannoy(n: int, k: int) -> int:
    return delannoy(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Delannoy)

''' OEIS

The traits of the Delannoy triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-RowSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000073 | Std-DiagSum      | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with a(0) = a(1 |
| 5   | A000129 | Std-RowSum       | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 6   | A000247 | Inv-BinConv      | a(n) = 2^n - n - 2                                                             |
| 7   | A001003 | Inv-EvenSum      | Schroeder's second problem (generalized parentheses); also called super-Catala |
| 8   | A001844 | Std-DiagRow2     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 9   | A001845 | Std-DiagRow3     | Centered octahedral numbers (crystal ball sequence for cubic lattice)          |
| 10  | A001850 | Std-CentralE     | Central Delannoy numbers: a(n) = Sum_{k=0..n} C(n,k)*C(n+k,k)                  |
| 11  | A002002 | Std-CentralO     | a(n) = Sum_{k=0..n-1} binomial(n,k+1) * binomial(n+k,k)                        |
| 12  | A002378 | Inv-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 13  | A004526 | Alt-AccSum       | Nonnegative integers repeated, floor(n/2)                                      |
| 14  | A005408 | Std-DiagRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 15  | A006139 | Std-BinConv      | n*a(n) = 2*(2*n-1)*a(n-1) + 4*(n-1)*a(n-2) with a(0) = 1                       |
| 16  | A006318 | Inv-AltSum       | Large Schroeder numbers (or large Schroeder numbers, or big Schroeder numbers) |
| 17  | A007482 | Std-PosHalf      | a(n) is the number of subsequences of [ 1, ..., 2n ] in which each odd number  |
| 18  | A008288 | Std-Triangle     | Square array of Delannoy numbers D(i,j) (i >= 0, j >= 0) read by antidiagonals |
| 19  | A014105 | Inv:Rev-PolyRow2 | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 20  | A015530 | Std-PolyCol3     | Expansion of x/(1 - 4*x - 3*x^2)                                               |
| 21  | A026003 | Std-RowMax       | a(n) = T([n/2],[(n+1)/2]), where T = Delannoy triangle (A008288)               |
| 22  | A026937 | Std-AccSum       | a(n) = Sum_{k=0..n} (k+1)*T(n, n-k), where T is given by A008288               |
| 23  | A028387 | Std-PolyRow2     | a(n) = n + (n+1)^2                                                             |
| 24  | A033878 | Std-RevInv       | Triangular array associated with Schroeder numbers                             |
| 25  | A057597 | Alt-DiagSum      | a(n) = -a(n-1) - a(n-2) + a(n-3), a(0)=0, a(1)=0, a(2)=1                       |
| 26  | A059304 | Std-InvBinConv   | a(n) = 2^n * (2*n)! / (n!)^2                                                   |
| 27  | A077020 | Std-NegHalf      | a(n) is the unique odd positive solution x of 2^n = 7x^2+y^2                   |
| 28  | A088137 | Alt-PolyCol3     | Generalized Gaussian Fibonacci integers                                        |
| 29  | A090288 | Inv-DiagRow2     | a(n) = 2*n^2 + 6*n + 2                                                         |
| 30  | A103138 | Inv-RowMax       | Second column of inverse of Delannoy triangle                                  |
| 31  | A106579 | Inv-AccRev       | Triangular array associated with Schroeder numbers: T(0,0) = 1, T(n,0) = 0 for |
| 32  | A114710 | Inv-PolyCol2     | Number of hill-free Schroeder paths of length 2n that have no horizontal steps |
| 33  | A116404 | Std-EvenSum      | Expansion of (1-x)/((1-x)^2 - x^2*(1+x)^2)                                     |
| 34  | A122538 | Inv-Acc          | Riordan array (1, x*f(x)) where f(x)is the g.f. of A006318                     |
| 35  | A126307 | Std-RowGcd       | a(n) is the length of the leftmost ascent (i.e., height of the first peak) in  |
| 36  | A132372 | Std-Inv          | T(n, k) counts Schroeder n-paths whose ascent starting at the initial vertex h |
| 37  | A330803 | Inv-PosHalf      | Evaluation of the Big-Schroeder polynomials at -1/2 and normalized with (-2)^n |
| 38  | A364553 | Std-TransNat0    | Number of edges in the n-Pell graph                                            |
| 39  | A367393 | Inv-CentralE     | a(n) = A103136(2*n, n), the central terms of the inverse of the Delannoy trian |
| 40  | A376871 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k * hypergeom([-k, k - n], [1], 2)                       |

* Statistic about Delannoy:

	Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 40.
	all      A-numbers  : 116.
	missing  sequences  : 49.

[('missing', 49), ('A001003', 13), ('A000012', 7), ('A006318', 6), ('A005408', 6), ('A132372', 5), ('A103138', 4), ('A026003', 4), ('A008288', 4), ('A001845', 4), ('A001844', 4), ('A000129', 4), ('A000027', 4), ('A077020', 3), ('A033878', 3), ('A026937', 3), ('A007482', 3), ('A367393', 2), ('A330803', 2), ('A126307', 2), ('A122538', 2), ('A116404', 2), ('A114710', 2), ('A106579', 2), ('A090288', 2), ('A059304', 2), ('A028387', 2), ('A006139', 2), ('A002002', 2), ('A001850', 2), ('A000247', 2), ('A000007', 2), ('A376871', 1), ('A364553', 1), ('A088137', 1), ('A057597', 1), ('A015530', 1), ('A014105', 1), ('A004526', 1), ('A002378', 1), ('A000073', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Delannoy.html .
2025/01/10

'''
