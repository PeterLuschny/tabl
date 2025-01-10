from functools import cache
from _tabltypes import MakeTriangle

"""Harmonic polynomials (coefficients).

[0] 1
[1] 0,     1
[2] 0,     2,     1
[3] 0,     6,     4,     1
[4] 0,    24,    18,     7,    1
[5] 0,   120,    96,    46,   11,    1
[6] 0,   720,   600,   326,  101,   16,   1
[7] 0,  5040,  4320,  2556,  932,  197,  22,  1
"""


@cache
def harmonic(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = harmonic(n - 1) + [1]
    sav = row[1]

    for k in range(n - 1, 0, -1):
        row[k] = (n - 1) * row[k] + row[k - 1]
    row[1] += sav

    return row


@MakeTriangle(harmonic, "Harmonic", ["A358694", "A109822"], True)
def Harmonic(n: int, k: int) -> int:
    return harmonic(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Harmonic)

''' OEIS

The traits of the Harmonic triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000124 | Std-DiagRow1     | Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 + 1; or, max |
| 5   | A000142 | Std-RowMax       | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000254 | Std-RowSum       | Unsigned Stirling numbers of first kind, s(n+1,2): a(n+1) = (n+1)*a(n) + n!    |
| 7   | A001563 | Std-DiagCol2     | a(n) = n*n! = (n+1)! - n!                                                      |
| 8   | A001710 | Std-AltSum       | Order of alternating group A_n, or number of even permutations of n letters    |
| 9   | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 10  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 11  | A011968 | Inv-AltSum       | Apply (1+Shift) to Bell numbers                                                |
| 12  | A033484 | Inv-DiagCol2     | a(n) = 3*2^n - 2                                                               |
| 13  | A052582 | Std-PolyCol2     | a(n) = 2*n*n!                                                                  |
| 14  | A055642 | Inv-DiagCol1     | Number of digits in the decimal expansion of n                                 |
| 15  | A056220 | Inv:Rev-PolyRow3 | a(n) = 2*n^2 - 1                                                               |
| 16  | A067318 | Std-DiagCol3     | Total number of transpositions in all permutations of n letters                |
| 17  | A080859 | Rev-PolyRow3     | a(n) = 6*n^2 + 4*n + 1                                                         |
| 18  | A081052 | Std-TransNat0    | Difference of Stirling numbers of the first kind                               |
| 19  | A090809 | Inv-DiagRow2     | Coefficient of the irreducible character of S_m indexed by (m-2n+2,2n-2) in th |
| 20  | A091344 | Inv-DiagCol3     | a(n) = 2*3^n - 3*2^n + 1                                                       |
| 21  | A101851 | Inv-RowSum       | a(n) = Sum_{k=0..n} (-1)^(n-k)*k*Stirling2(n,k)                                |
| 22  | A129890 | Std-PosHalf      | a(n) = (2*n+2)!! - (2*n+1)!!                                                   |
| 23  | A138772 | Alt-TransNat0    | Number of entries in the second cycles of all permutations of {1,2,...,n}; eac |
| 24  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 25  | A182541 | Std-EvenSum      | Coefficients in g.f. for certain marked mesh patterns                          |
| 26  | A192459 | Std-NegHalf      | Coefficient of x in the reduction by x^2->x+2 of the polynomial p(n,x) defined |
| 27  | A227341 | Std-Inv          | Triangular array: Number of partitions of the vertex set of a forest of two tr |
| 28  | A308305 | Std-DiagRow2     | a(n) = s(n,n) + s(n,n-1) + s(n,n-2), where s(n,k) are the unsigned Stirling nu |
| 29  | A323618 | Alt-TransSqrs    | Expansion of e.g.f. (1 + x)*log(1 + x)*(2 + log(1 + x))/2                      |
| 30  | A358694 | Std-Triangle     | Triangle read by rows. Coefficients of the polynomials H(n, x) = Sum_{k=0..n-1 |
| 31  | A363071 | Inv-DiagSum      | Number of partitions of [n] into m blocks that are ordered with increasing lea |

* Statistic about Harmonic:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 31.
	all      A-numbers  : 89.
	missing  sequences  : 126.

[('missing', 126), ('A000254', 6), ('A000142', 6), ('A000012', 6), ('A174965', 5), ('A000124', 5), ('A000007', 5), ('A227341', 4), ('A011968', 4), ('A358694', 3), ('A308305', 3), ('A129890', 3), ('A067318', 3), ('A005563', 3), ('A001710', 3), ('A001563', 3), ('A000027', 3), ('A192459', 2), ('A182541', 2), ('A101851', 2), ('A091344', 2), ('A090809', 2), ('A055642', 2), ('A052582', 2), ('A033484', 2), ('A005408', 2), ('A363071', 1), ('A323618', 1), ('A138772', 1), ('A081052', 1), ('A080859', 1), ('A056220', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Harmonic.html .
2025/01/10

'''
