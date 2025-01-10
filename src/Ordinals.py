from functools import cache
from _tabltypes import MakeTriangle

"""von Neumann ordinals (kind of).

[0] [0]
[1] [0,  1]
[2] [0,  1,  2]
[3] [0,  1,  2,  3]
[4] [0,  1,  2,  3,  4]
[5] [0,  1,  2,  3,  4,  5]
[6] [0,  1,  2,  3,  4,  5,  6]
[7] [0,  1,  2,  3,  4,  5,  6,  7]
"""


@cache
def ordinals(n: int) -> list[int]:
    if n == 0:
        return [0]
    return ordinals(n - 1) + [n]


@MakeTriangle(
    ordinals, "Ordinals", ["A002262", "A002260", "A004736", "A025581"], False
)
def Ordinals(n: int, k: int) -> int:
    return ordinals(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Ordinals)

''' OEIS

The traits of the Ordinals triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-RowMax       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000217 | Std-RowSum       | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 4   | A000292 | Std-AccSum       | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 5   | A000295 | Std-PosHalf      | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1 of A1730 |
| 6   | A000330 | Std-TransNat0    | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1) |
| 7   | A000340 | Rev-PolyCol3     | a(0)=1, a(n) = 3*a(n-1) + n + 1                                                |
| 8   | A000384 | Alt-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 9   | A000537 | Std-TransSqrs    | Sum of first n cubes; or n-th triangular number squared                        |
| 10  | A001787 | Std-BinConv      | a(n) = n*2^(n-1)                                                               |
| 11  | A002262 | Std-Triangle     | Triangle read by rows: T(n,k) = k, 0 <= k <= n, in which row n lists the first |
| 12  | A002265 | Alt-DiagSum      | Nonnegative integers repeated 4 times                                          |
| 13  | A002415 | Rev-TransSqrs    | 4-dimensional pyramidal numbers: a(n) = n^2*(n^2-1)/12                         |
| 14  | A002620 | Rev-EvenSum      | Quarter-squares: a(n) = floor(n/2)*ceiling(n/2). Equivalently, a(n) = floor(n^ |
| 15  | A003418 | Std-RowLcm       | Least common multiple (or LCM) of {1, 2, ..., n} for n >= 1, a(0) = 1          |
| 16  | A004526 | Std-AltSum       | Nonnegative integers repeated, floor(n/2)                                      |
| 17  | A007290 | Std-AccRevSum    | a(n) = 2*binomial(n,3)                                                         |
| 18  | A007590 | Alt-AccRevSum    | a(n) = floor(n^2/2)                                                            |
| 19  | A008794 | Std-OddSum       | Squares repeated; a(n) = floor(n/2)^2                                          |
| 20  | A008805 | Std-DiagSum      | Triangular numbers repeated                                                    |
| 21  | A010701 | Std-DiagCol3     | Constant sequence: the all 3's sequence                                        |
| 22  | A011934 | Alt-TransSqrs    | a(n) = |1^3 - 2^3 + 3^3 - 4^3 + ... + (-1)^(n+1)*n^3|                          |
| 23  | A014105 | Std-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 24  | A025581 | Std-Rev          | Triangle read by rows: T(n, k) = n-k, for 0 <= k <= n                          |
| 25  | A036799 | Std-PolyCol2     | a(n) = 2 + 2^(n+1)*(n-1)                                                       |
| 26  | A053088 | Std-NegHalf      | a(n) = 3*a(n-2) + 2*a(n-3) for n > 2, a(0)=1, a(1)=0, a(2)=3                   |
| 27  | A055087 | Std-AntiDiag     | Integers 0..n then 0..n then 0..n+1 then 0..n+1 etc                            |
| 28  | A055642 | Std-DiagCol2     | Number of digits in the decimal expansion of n                                 |
| 29  | A059100 | Rev-PolyRow3     | a(n) = n^2 + 2                                                                 |
| 30  | A062805 | Rev-PolyDiag     | a(n) = Sum_{i=1..n} i*n^(n-i)                                                  |
| 31  | A062806 | Std-PolyDiag     | a(n) = Sum_{i=1..n} i*n^i                                                      |
| 32  | A063524 | Std-InvBinConv   | Characteristic function of 1                                                   |
| 33  | A067389 | Std-PolyRow3     | a(n) = 3*n^3 + 2*n^2 + n                                                       |
| 34  | A082375 | Rev-AntiDiag     | Irregular triangle read by rows: row n begins with n and decreases by 2 until  |
| 35  | A089000 | Rev-Poly         | Square table, read by antidiagonals, of coefficients T(k,n) (row k; column n)  |
| 36  | A094053 | Rev-Diffx1       | Triangle read by rows: T(n,k) = k*(n-k), 1 <= k <= n                           |
| 37  | A110660 | Std-EvenSum      | Oblong (promic) numbers repeated                                               |
| 38  | A112367 | Std-Acc          | a(n) = A000217(n-k), where k is the largest triangular number less than n      |
| 39  | A140960 | Alt-PolyCol2     | a(n) = (2*(-1)^n - 2^(n+1) + 3*n*2^n)/9                                        |
| 40  | A141418 | Std-AccRev       | Triangle read by rows: T(n,k) = k * (2*n - k - 1) / 2, 1 <= k <= n             |
| 41  | A142150 | Alt-AccSum       | The nonnegative integers interleaved with 0's                                  |
| 42  | A289399 | Std-PolyCol3     | Total path length of the complete ternary tree of height n                     |

* Statistic about Ordinals:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 42.
	all      A-numbers  : 113.
	missing  sequences  : 9.

[('A000027', 24), ('missing', 9), ('A000217', 7), ('A000012', 7), ('A004526', 6), ('A000292', 4), ('A063524', 3), ('A055642', 3), ('A025581', 3), ('A010701', 3), ('A007290', 3), ('A003418', 3), ('A002620', 3), ('A001787', 3), ('A000295', 3), ('A141418', 2), ('A140960', 2), ('A112367', 2), ('A110660', 2), ('A055087', 2), ('A053088', 2), ('A036799', 2), ('A008794', 2), ('A007590', 2), ('A002262', 2), ('A289399', 1), ('A142150', 1), ('A094053', 1), ('A089000', 1), ('A082375', 1), ('A067389', 1), ('A062806', 1), ('A062805', 1), ('A059100', 1), ('A014105', 1), ('A011934', 1), ('A008805', 1), ('A002415', 1), ('A002265', 1), ('A000537', 1), ('A000384', 1), ('A000340', 1), ('A000330', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Ordinals.html .
2025/01/10

'''
