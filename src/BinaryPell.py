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
def binarypell(n):

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

'''
* Statistic about BinomialPell:
The number of ...
        all      hashes    is 122.
        distinct hashes    is 64.
        core     triangles is 1.
        distinct types     is 3.
        missing  sequences is 68.
        all      A-numbers is 54.
        distinct A-numbers is 25.

The traits of the BinomialPell triangle as represented in the OEIS.

|    | A-number| trait        | A-name                                                                 |
|----|---------|--------------|------------------------------------------------------------------------|
| 1  | A000027 | Std-ColRight | The positive integers. Also called the natural numbers, the whole numb |
| 2  | A003484 | Std-RowGcd   | Radon function, also called Hurwitz-Radon numbers                      |
| 3  | A007070 | Std-RowSum   | a(n) = 4*a(n-1) - 2*a(n-2) with a(0) = 1, a(1) = 4                     |
| 4  | A053228 | Std-PolyRow1 | n for which second differences of sigma(n) are positive                |
| 5  | A077957 | Std-AltSum   | Powers of 2 alternating with zeros                                     |
| 6  | A077985 | Std-ColLeft  | Expansion of 1/(1 + 2*x - x^2)                                         |
| 7  | A112415 | Std-DiagRow3 | a(n) = C(1+n,1) * C(2+n,1) * C(4+n,2)                                  |
| 8  | A120328 | Alt-PolyRow2 | Sum of three consecutive squares: a(n) = n^2 + (n + 1)^2 + (n + 2)^2   |
| 9  | A239229 | Alt-PolyRow1 | Euler characteristic of n-holed torus: 2 - 2*n                         |
| 10 | A292022 | Std-PolyRow3 | a(n) = 4n(n^2+2)                                                       |
| 11 | A367211 | Std-Triangle | Triangular array T(n,k), read by rows: coefficients of strong divisibi |
| 12 | B001109 | Std-PosHalf  | a(n)^2 is a triangular number: a(n) = 6*a(n-1) - a(n-2) with a(0)=0, a |
| 13 | B002378 | Std-DiagRow1 | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)     |
| 14 | B005918 | Std-PolyRow2 | Number of points on surface of square pyramid: 3*n^2 + 2 (n>0)         |
| 15 | B015519 | Std-NegHalf  | a(n) = 2*a(n-1) + 7*a(n-2)                                             |
| 16 | B081179 | Std-PolyCol2 | 3rd binomial transform of (0,1,0,2,0,4,0,8,0,16,...)                   |
| 17 | B081180 | Std-PolyCol3 | 4th binomial transform of (0,1,0,2,0,4,0,8,0,16,...)                   |
| 18 | B093968 | Alt-AccSum   | Inverse binomial transform of n*Pell(n)                                |
| 19 | B094038 | Std-EvenSum  | Binomial transform of (Pell(-n)+Pell(n))/2                             |
| 20 | B099626 | Std-DiagSum  | A transform of the Pell numbers                                        |
| 21 | B112575 | Alt-DiagSum  | Chebyshev transform of the second kind of the Pell numbers             |
| 22 | B134481 | Std-DiagRow2 | Row sums of triangle A134480                                           |
| 23 | B190331 | Rev-PolyCol3 | a(n) = 8*a(n-1) + 2*a(n-2), with a(0)=0, a(1)=1                        |
| 24 | B292022 | Alt-PolyRow3 | a(n) = 4n(n^2+2)                                                       |
| 25 | B361732 | Std-DiagCol1 | a(n) = [x^n] (x^5 + 5*x^4 + 4*x^3 - 3*x + 1)/(x^2 + 2*x - 1)^2         |
'''
