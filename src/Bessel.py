from functools import cache
from _tabltypes import MakeTriangle

"""Bessel triangle.

[0] [1]
[1] [0,      1]
[2] [0,      1,      1]
[3] [0,      3,      3,     1]
[4] [0,     15,     15,     6,     1]
[5] [0,    105,    105,    45,    10,    1]
[6] [0,    945,    945,   420,   105,   15,   1]
[7] [0,  10395,  10395,  4725,  1260,  210,  21,  1]
[8] [0, 135135, 135135, 62370, 17325, 3150, 378, 28, 1]
"""


@cache
def bessel(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = bessel(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + (2 * (n - 1) - k) * row[k]
    return row


@MakeTriangle(bessel, "Bessel", ["A132062", "A001497", "A001498", "A122850"], True)
def Bessel(n: int, k: int) -> int:
    return bessel(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Bessel)


''' OEIS

The traits of the Bessel triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000085 | Rev-DiagSum      | Number of self-inverse permutations on n letters, also known as involutions; n |
| 5   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000704 | Inv:Rev-EvenSum  | Number of degree-n even permutations of order dividing 2                       |
| 7   | A000898 | Inv:Rev-NegHalf  | a(n) = 2*(a(n-1) + (n-1)*a(n-2)) for n >= 2 with a(0) = 1                      |
| 8   | A001093 | Alt-PolyRow3     | a(n) = n^3 + 1                                                                 |
| 9   | A001147 | Std-RowMax       | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 10  | A001464 | Inv-RowSum       | Expansion of e.g.f. exp(-x - (1/2)*x^2)                                        |
| 11  | A001465 | Inv:Rev-OddSum   | Number of degree-n odd permutations of order 2                                 |
| 12  | A001514 | Rev-TransNat0    | Bessel polynomial {y_n}'(1)                                                    |
| 13  | A001515 | Std-RowSum       | Bessel polynomial y_n(x) evaluated at x=1                                      |
| 14  | A001517 | Std-PosHalf      | Bessel polynomials y_n(x) (see A001498) evaluated at 2                         |
| 15  | A001518 | Rev-PolyCol3     | Bessel polynomial y_n(3)                                                       |
| 16  | A001879 | Std-DiagCol3     | a(n) = (2n+2)!/(n!*2^(n+1))                                                    |
| 17  | A002119 | Std-NegHalf      | Bessel polynomial y_n(-2)                                                      |
| 18  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 19  | A003215 | Rev-PolyRow3     | Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for he |
| 20  | A003436 | Alt-AccRevSum    | Number of inequivalent labeled Hamiltonian circuits on n-octahedron. Interlaci |
| 21  | A016789 | Inv:Rev-PolyRow3 | a(n) = 3*n + 2                                                                 |
| 22  | A025164 | Std-OddSum       | a(n) = a(n-2) + (2n-1)a(n-1); a(0)=1, a(1)=1                                   |
| 23  | A036244 | Std-EvenSum      | Denominator of continued fraction given by C(n) = [ 1; 3, 5, 7, ...(2n-1)]     |
| 24  | A047974 | Inv-NegHalf      | a(n) = a(n-1) + 2*(n-1)*a(n-2)                                                 |
| 25  | A050534 | Std-DiagRow2     | Tritriangular numbers: a(n) = binomial(binomial(n,2),2) = n*(n+1)*(n-1)*(n-2)/ |
| 26  | A062267 | Inv-PolyCol2     | Row sums of (signed) triangle A060821 (Hermite polynomials)                    |
| 27  | A068601 | Std-PolyRow3     | a(n) = n^3 - 1                                                                 |
| 28  | A069834 | Std-RowGcd       | a(n) = n-th reduced triangular number: n*(n+1)/{2^k} where 2^k is the largest  |
| 29  | A085386 | Inv-EvenSum      | E.g.f. cosh(x+x^2/2)                                                           |
| 30  | A104548 | Std-Rev          | Triangle read by rows giving coefficients of Bessel polynomial p_n(x)          |
| 31  | A107103 | Std-TransNat0    | Column 1 of triangle A107102, which is the matrix inverse of A100862           |
| 32  | A107104 | Std-PolyCol2     | Absolute row sums of triangle A107102, which is the matrix inverse of A100862  |
| 33  | A123023 | Inv-ColMiddle    | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 34  | A132062 | Std-Triangle     | Sheffer triangle (1,1-sqrt(1-2*x)). Extended Bessel triangle A001497           |
| 35  | A133221 | Inv:Rev-ColMiddl | A001147 with each term repeated                                                |
| 36  | A240440 | Std-DiagRow3     | Number of ways to place 3 points on a triangular grid of side n so that they a |
| 37  | A245066 | Rev-CentralO     | Central terms of triangles A001497 and A001498                                 |
| 38  | A278990 | Std-AltSum       | Number of loopless linear chord diagrams with n chords                         |
| 39  | A293604 | Inv-PosHalf      | Expansion of e.g.f.: exp(x * (1 - x))                                          |
| 40  | A362276 | Inv:Rev-PolyDiag | a(n) = n! * Sum_{k=0..floor(n/2)} (-n/2)^k * binomial(n-k,k)/(n-k)!            |
| 41  | A362278 | Inv:Rev-PolyCol3 | Expansion of e.g.f. exp(x - 3*x^2/2)                                           |
| 42  | A369746 | Std-PolyCol3     | Expansion of e.g.f. exp( 3 * (1-sqrt(1-2*x)) )                                 |
| 43  | A376872 | Std-CentralE     | a(n) = n! * 2^(-n) * binomial(3*n - 1, 2*n) * binomial(2*n, n). Central terms  |

* Statistic about Bessel:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 43.
	all      A-numbers  : 116.
	missing  sequences  : 89.

[('missing', 89), ('A001147', 12), ('A001515', 6), ('A000012', 6), ('A240440', 5), ('A069834', 5), ('A050534', 5), ('A000217', 5), ('A000085', 5), ('A000027', 5), ('A000007', 5), ('A278990', 4), ('A104548', 4), ('A376872', 3), ('A132062', 3), ('A002378', 3), ('A001879', 3), ('A001517', 3), ('A293604', 2), ('A107104', 2), ('A062267', 2), ('A036244', 2), ('A025164', 2), ('A003436', 2), ('A002119', 2), ('A001464', 2), ('A369746', 1), ('A362278', 1), ('A362276', 1), ('A245066', 1), ('A133221', 1), ('A123023', 1), ('A107103', 1), ('A085386', 1), ('A068601', 1), ('A047974', 1), ('A016789', 1), ('A003215', 1), ('A001518', 1), ('A001514', 1), ('A001465', 1), ('A001093', 1), ('A000898', 1), ('A000704', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Bessel.html .
2025/01/10

'''
