from functools import cache
from _tabltypes import MakeTriangle

"""Binary Pell triangle

[0] [  1]
[1] [  2,    1]
[2] [  4,    4,    1]
[3] [  8,   12,    6,    1]
[4] [ 16,   32,   24,    8,    1]
[5] [ 32,   80,   80,   40,   10,   1]
[6] [ 64,  192,  240,  160,   60,  12,   1]
[7] [128,  448,  672,  560,  280,  84,  14,  1]
[8] [256, 1024, 1792, 1792, 1120, 448, 112, 16, 1]
"""


@cache
def binarypell(n: int) -> list[int]:

    if n == 0:
        return [1]

    arow = binarypell(n-1)
    row = arow + [1]
    for k in range(n-1, 0, -1):
        row[k] = arow[k - 1] + 2 * arow[k]
    row[0] = 2 * arow[0]
    return row


@MakeTriangle(binarypell, "BinaryPell", ["A038207"], True)
def BinaryPell(n: int, k: int) -> int:
    return binarypell(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinaryPell)


''' OEIS

The traits of the BinaryPell triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Alt-PolyCol2     | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-AltSum       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Std-ColLeft      | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000129 | Std-DiagSum      | Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2)          |
| 6   | A000244 | Std-RowSum       | Powers of 3: a(n) = 3^n                                                        |
| 7   | A000272 | Std-PolyDiag     | Number of trees on n labeled nodes: n^(n-2) with a(0)=1                        |
| 8   | A000290 | Std-PolyRow2     | The squares: a(n) = n^2                                                        |
| 9   | A000302 | Std-PolyCol2     | Powers of 4: a(n) = 4^n                                                        |
| 10  | A000351 | Std-PosHalf      | Powers of 5: a(n) = 5^n                                                        |
| 11  | A000420 | Rev-PolyCol3     | Powers of 7: a(n) = 7^n                                                        |
| 12  | A000578 | Std-PolyRow3     | The cubes: a(n) = n^3                                                          |
| 13  | A001045 | Rev-DiagSum      | Jacobsthal sequence (or Jacobsthal numbers): a(n) = a(n-1) + 2*a(n-2), with a( |
| 14  | A001787 | Std-DiagCol1     | a(n) = n*2^(n-1)                                                               |
| 15  | A001788 | Std-DiagCol2     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 16  | A001789 | Std-DiagCol3     | a(n) = binomial(n,3)*2^(n-3)                                                   |
| 17  | A001850 | Std-BinConv      | Central Delannoy numbers: a(n) = Sum_{k=0..n} C(n,k)*C(n+k,k)                  |
| 18  | A002939 | Inv:Rev-TransSqr | a(n) = 2*n*(2*n-1)                                                             |
| 19  | A003462 | Std-OddSum       | a(n) = (3^n - 1)/2                                                             |
| 20  | A005408 | Alt-AccSum       | The odd numbers: a(n) = 2*n + 1                                                |
| 21  | A005563 | Alt-TransSqrs    | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 22  | A005843 | Std-DiagRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 23  | A006234 | Std-AccRevSum    | a(n) = n*3^(n-4)                                                               |
| 24  | A007051 | Std-EvenSum      | a(n) = (3^n + 1)/2                                                             |
| 25  | A008788 | Alt-PolyDiag     | a(n) = n^(n+2)                                                                 |
| 26  | A013609 | Std-Rev          | Triangle of coefficients in expansion of (1+2*x)^n                             |
| 27  | A016754 | Rev-PolyRow2     | Odd squares: a(n) = (2n+1)^2. Also centered octagonal numbers                  |
| 28  | A016755 | Rev-PolyRow3     | Odd cubes: a(n) = (2*n + 1)^3                                                  |
| 29  | A027471 | Std-TransNat0    | a(n) = (n-1)*3^(n-2), n > 0                                                    |
| 30  | A038207 | Std-Triangle     | Triangle whose (i,j)-th entry is binomial(i,j)*2^(i-j)                         |
| 31  | A046092 | Std-DiagRow2     | 4 times triangular numbers: a(n) = 2*n*(n+1)                                   |
| 32  | A046717 | Rev-EvenSum      | a(n) = 2*a(n-1) + 3*a(n-2), a(0) = a(1) = 1                                    |
| 33  | A051129 | Std-Poly         | Table T(n,k) = k^n read by upwards antidiagonals (n >= 1, k >= 1)              |
| 34  | A059304 | Std-CentralE     | a(n) = 2^n * (2*n)! / (n!)^2                                                   |
| 35  | A062189 | Rev-TransSqrs    | a(n) = 2 * 3^(n-2)*n*(1+2*n)                                                   |
| 36  | A069720 | Rev-CentralO     | a(n) = 2^(n-1)*binomial(2n-1, n)                                               |
| 37  | A069723 | Std-CentralO     | a(n) = 2^(n-1)*binomial(2*n-3, n-1)                                            |
| 38  | A077020 | Inv:Rev-DiagSum  | a(n) is the unique odd positive solution x of 2^n = 7x^2+y^2                   |
| 39  | A081038 | Std-AccSum       | 3rd binomial transform of (1,2,0,0,0,0,0,0,...)                                |
| 40  | A085527 | Rev-PolyDiag     | a(n) = (2n+1)^n                                                                |
| 41  | A085528 | Inv:Rev-PolyDiag | a(n) = (2*n+1)^(n+1)                                                           |
| 42  | A098332 | Std-InvBinConv   | Expansion of 1/sqrt(1 - 2*x + 9*x^2)                                           |
| 43  | A098660 | Rev-ColMiddle    | E.g.f. BesselI(0,2*sqrt(2)*x) + BesselI(1,2*sqrt(2)*x)/sqrt(2)                 |
| 44  | A109388 | Std-RowMax       | Maximum number of pairwise incomparable subcubes of the discrete n-cube. Large |
| 45  | A119258 | Alt-AccRev       | Triangle read by rows: T(n,0) = T(n,n) = 1 and for 0<k<n: T(n,k) = 2*T(n-1, k- |
| 46  | A128099 | Rev-AntiDiag     | Triangle read by rows: T(n,k) is the number of ways to tile a 3 X n rectangle  |
| 47  | A130809 | Std-DiagRow3     | If X_1, ..., X_n is a partition of a 2n-set X into 2-blocks then a(n) is equal |
| 48  | A145905 | Rev-Poly         | Square array read by antidiagonals: Hilbert transform of triangle A060187      |
| 49  | A152011 | Rev-OddSum       | a(0) = 1 and a(n) = (3^n - (-1)^n)/2 for n >= 1                                |
| 50  | A171977 | Std-RowGcd       | a(n) = 2^(k+1) where 2^k is the highest power of 2 dividing n                  |
| 51  | A207538 | Std-AntiDiag     | Triangle of coefficients of polynomials v(n,x) jointly generated with A207537; |
| 52  | A212697 | Rev-TransNat0    | a(n) = 2*n*3^(n-1)                                                             |

* Statistic about BinaryPell:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 52.
	all      A-numbers  : 178.
	missing  sequences  : 26.

[('missing', 26), ('A000244', 14), ('A000027', 11), ('A000012', 7), ('A005843', 6), ('A005408', 6), ('A000351', 6), ('A171977', 5), ('A130809', 5), ('A109388', 5), ('A098332', 5), ('A059304', 5), ('A046092', 5), ('A001850', 5), ('A001789', 5), ('A001788', 5), ('A001787', 5), ('A000079', 5), ('A013609', 4), ('A000007', 4), ('A207538', 3), ('A119258', 3), ('A081038', 3), ('A069723', 3), ('A038207', 3), ('A007051', 3), ('A006234', 3), ('A003462', 3), ('A000578', 3), ('A000302', 3), ('A000290', 3), ('A152011', 2), ('A128099', 2), ('A098660', 2), ('A069720', 2), ('A046717', 2), ('A016755', 2), ('A016754', 2), ('A008788', 2), ('A005563', 2), ('A000129', 2), ('A212697', 1), ('A145905', 1), ('A085528', 1), ('A085527', 1), ('A077020', 1), ('A062189', 1), ('A051129', 1), ('A027471', 1), ('A002939', 1), ('A001045', 1), ('A000420', 1), ('A000272', 1)]

A related webpage is: https://peterluschny.github.io/tabl/BinaryPell.html .
2025/01/10

'''
