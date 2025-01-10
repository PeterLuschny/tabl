from functools import cache
from _tabltypes import MakeTriangle

"""Schroeder triangle.

[0] [1]
[1] [0,     1]
[2] [0,     2,     1]
[3] [0,     6,     4,     1]
[4] [0,    22,    16,     6,    1]
[5] [0,    90,    68,    30,    8,    1]
[6] [0,   394,   304,   146,   48,   10,   1]
[7] [0,  1806,  1412,   714,  264,   70,  12,   1]
[8] [0,  8558,  6752,  3534, 1408,  430,  96,  14,  1]
[9] [0, 41586, 33028, 17718, 7432, 2490, 652, 126, 16, 1]
"""


@cache
def schroeder(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = schroeder(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]

    return row


@MakeTriangle(
    schroeder,
    "Schroeder",
    ["A122538", "A033877", "A080245", "A080247", "A106579"],
    True,
)
def Schroeder(n: int, k: int) -> int:
    return schroeder(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Schroeder)

''' OEIS

The traits of the Schroeder triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000225 | Std-InvBinConv   | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 5   | A000982 | Inv-TransSqrs    | a(n) = ceiling(n^2/2)                                                          |
| 6   | A001003 | Std-RowSum       | Schroeder's second problem (generalized parentheses); also called super-Catala |
| 7   | A001105 | Inv-DiagRow2     | a(n) = 2*n^2                                                                   |
| 8   | A001333 | Inv-AltSum       | Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2)    |
| 9   | A001590 | Inv-DiagSum      | Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) with a(0)=0, a(1)=1, a(2)= |
| 10  | A002003 | Inv-CentralE     | a(n) = 2 * Sum_{k=0..n-1} binomial(n-1, k)*binomial(n+k, k)                    |
| 11  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 12  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A005843 | Std-DiagRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 14  | A005899 | Inv-DiagCol3     | Number of points on surface of octahedron; also coordination sequence for cubi |
| 15  | A006318 | Std-RowMax       | Large Schroeder numbers (or large Schroeder numbers, or big Schroeder numbers) |
| 16  | A006319 | Std-DiagCol2     | Royal paths in a lattice (convolution of A006318)                              |
| 17  | A006320 | Std-DiagCol3     | Royal paths in a lattice                                                       |
| 18  | A006603 | Std-DiagSum      | Generalized Fibonacci numbers                                                  |
| 19  | A007483 | Inv-NegHalf      | a(n) = 3*a(n-1) + 2*a(n-2), with a(0)=1, a(1)=5                                |
| 20  | A007590 | Inv:Rev-TransSqr | a(n) = floor(n^2/2)                                                            |
| 21  | A008586 | Inv-DiagCol2     | Multiples of 4                                                                 |
| 22  | A010683 | Std-OddSum       | Let S(x,y) = number of lattice paths from (0,0) to (x,y) that use the step set |
| 23  | A026003 | Rev-DiagSum      | a(n) = T([n/2],[(n+1)/2]), where T = Delannoy triangle (A008288)               |
| 24  | A035597 | Inv-DiagRow3     | Number of points of L1 norm 3 in cubic lattice Z^n                             |
| 25  | A050146 | Inv:Rev-CentralO | a(n) = T(n,n), array T as in A050143                                           |
| 26  | A054000 | Std-DiagRow2     | a(n) = 2*n^2 - 2                                                               |
| 27  | A055642 | Std-RowGcd       | Number of digits in the decimal expansion of n                                 |
| 28  | A056220 | Inv:Rev-PolyRow3 | a(n) = 2*n^2 - 1                                                               |
| 29  | A065096 | Std-TransSqrs    | Sums of lists produced by a variant of the iteration that produces the Catalan |
| 30  | A077020 | Inv-PosHalf      | a(n) is the unique odd positive solution x of 2^n = 7x^2+y^2                   |
| 31  | A078050 | Inv-PolyCol2     | Expansion of (1-x)/(1+x+2*x^2)                                                 |
| 32  | A080859 | Rev-PolyRow3     | a(n) = 6*n^2 + 4*n + 1                                                         |
| 33  | A087455 | Inv:Rev-PolyCol3 | Expansion of (1 - x)/(1 - 2*x + 3*x^2) in powers of x                          |
| 34  | A093178 | Inv-AccSum       | If n is even then 1, otherwise n                                               |
| 35  | A103885 | Std-CentralE     | a(n) = [x^(2*n)] ((1 + x)/(1 - x))^n                                           |
| 36  | A104934 | Inv:Rev-NegHalf  | Expansion of (1-x)/(1 - 3*x - 2*x^2)                                           |
| 37  | A106579 | Std-Rev          | Triangular array associated with Schroeder numbers: T(0,0) = 1, T(n,0) = 0 for |
| 38  | A109980 | Std-PolyCol2     | Number of Delannoy paths of length n with no (1,1)-steps on the line y=x       |
| 39  | A110110 | Inv-RowMax       | Number of symmetric Schroeder paths of length 2n (A Schroeder path of length 2 |
| 40  | A111587 | Inv-EvenSum      | a(n) = 2*a(n-1) + 2*a(n-3) + a(n-4), a(0) = 1, a(1) = 4, a(2) = 9, a(3) = 20   |
| 41  | A122538 | Std-Triangle     | Riordan array (1, x*f(x)) where f(x)is the g.f. of A006318                     |
| 42  | A124625 | Inv-AccRevSum    | Even numbers sandwiched between 1's                                            |
| 43  | A144944 | Std-AccRev       | Super-Catalan triangle (read by rows) = triangular array associated with littl |
| 44  | A178792 | Std-BinConv      | Dot product of the rows of triangle A046899 with vector (1,2,4,8,...) (= A0000 |
| 45  | A180735 | Inv:Rev-DiagSum  | Expansion of (1+x)*(1-x)/(1 - x + x^2 + x^3)                                   |
| 46  | A193356 | Inv-TransNat0    | If n is even then 0, otherwise n                                               |
| 47  | A227506 | Rev-EvenSum      | Schroeder triangle sums: a(2*n-1) = A010683(2*n-2) and a(2*n) = A010683(2*n-1) |
| 48  | A237420 | Inv:Rev-TransNat | If n is odd, then a(n) = 0; otherwise, a(n) = n                                |
| 49  | A239204 | Std-EvenSum      | Expansion of ((x-1)*sqrt(x^2-6*x+1)-x^2-4*x+1)/(8*x^3)                         |
| 50  | A240688 | Inv-InvBinConv   | Expansion of -(x*sqrt(-4*x^2-4*x+1)-2*x^2-3*x) / ((x+1)*sqrt(-4*x^2-4*x+1)+ 4* |
| 51  | A330801 | Rev-CentralO     | a(n) = A080247(2*n, n), the central values of the Big-Schroeder triangle       |
| 52  | A330802 | Std-PosHalf      | Evaluation of the Big-Schroeder polynomials at 1/2 and normalized with 2^n     |
| 53  | A330803 | Std-NegHalf      | Evaluation of the Big-Schroeder polynomials at -1/2 and normalized with (-2)^n |

* Statistic about Schroeder:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 53.
	all      A-numbers  : 136.
	missing  sequences  : 70.

[('missing', 70), ('A001003', 9), ('A055642', 7), ('A006318', 6), ('A000012', 6), ('A010683', 5), ('A005843', 5), ('A000007', 5), ('A239204', 4), ('A106579', 4), ('A001333', 4), ('A330802', 3), ('A178792', 3), ('A124625', 3), ('A122538', 3), ('A110110', 3), ('A103885', 3), ('A093178', 3), ('A054000', 3), ('A006320', 3), ('A006319', 3), ('A005563', 3), ('A000225', 3), ('A000027', 3), ('A330803', 2), ('A240688', 2), ('A144944', 2), ('A109980', 2), ('A078050', 2), ('A077020', 2), ('A035597', 2), ('A008586', 2), ('A005899', 2), ('A005408', 2), ('A002003', 2), ('A001105', 2), ('A330801', 1), ('A237420', 1), ('A227506', 1), ('A193356', 1), ('A180735', 1), ('A111587', 1), ('A104934', 1), ('A087455', 1), ('A080859', 1), ('A065096', 1), ('A056220', 1), ('A050146', 1), ('A026003', 1), ('A007590', 1), ('A007483', 1), ('A006603', 1), ('A001590', 1), ('A000982', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Schroeder.html .
2025/01/10

'''
