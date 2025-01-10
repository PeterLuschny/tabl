from functools import cache
from _tabltypes import MakeTriangle

"""Catalan paths.

[0]   1,
[1]   0,   1,
[2]   1,   0,   1,
[3]   0,   2,   0,   1,
[4]   2,   0,   3,   0,   1,
[5]   0,   5,   0,   4,   0,   1,
[6]   5,   0,   9,   0,   5,   0,   1,
[7]   0,  14,   0,  14,   0,   6,   0,  1,
[8]  14,   0,  28,   0,  20,   0,   7,  0,  1,
[9]   0,  42,   0,  48,   0,  27,   0,  8,  0,  1.
"""


@cache
def catalanpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return catalanpaths(n - 1)[k] if k >= 0 and k < n else 0

    row = catalanpaths(n - 1) + [1]
    for k in range(0, n):
        row[k] = r(k - 1) + r(k + 1)
    return row


@MakeTriangle(
    catalanpaths, "CatalanPaths", ["A053121", "A052173", "A112554", "A322378"], True
)
def CatalanPaths(n: int, k: int) -> int:
    return catalanpaths(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CatalanPaths)

''' OEIS

The traits of the CatalanPaths triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Inv-DiagSum      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000045 | Inv-AbsSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 5   | A000079 | Std-AccRevSum    | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000217 | Inv-DiagCol2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000245 | Std-DiagCol2     | a(n) = 3*(2*n)!/((n+2)!*(n-1)!)                                                |
| 8   | A000292 | Inv-DiagCol3     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 9   | A000957 | Alt-DiagSum      | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 10  | A001405 | Std-RowSum       | a(n) = binomial(n, floor(n/2))                                                 |
| 11  | A001906 | Inv-PolyCol3     | F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)              |
| 12  | A002057 | Std-DiagCol3     | Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)        |
| 13  | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 14  | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 15  | A005809 | Inv-CentralE     | a(n) = binomial(3n,n)                                                          |
| 16  | A025560 | Inv-RowLcm       | a(n) = LCM{1, C(n-1,1), C(n-2,2), ..., C(n-[ n/2 ],[ n/2 ])}                   |
| 17  | A026005 | Rev-CentralO     | a(n) = T(4*n,n), where T = Catalan triangle (A008315)                          |
| 18  | A045621 | Std-TransNat0    | a(n) = 2^n - binomial(n, floor(n/2))                                           |
| 19  | A045721 | Inv:Rev-CentralO | a(n) = binomial(3*n+1,n)                                                       |
| 20  | A052173 | Std-Rev          | Another version of the Catalan triangle A008315                                |
| 21  | A053121 | Std-Triangle     | Catalan triangle (with 0's) read by rows                                       |
| 22  | A054341 | Std-PolyCol2     | Row sums of triangle A054336 (central binomial convolutions)                   |
| 23  | A054602 | Std-PolyRow3     | a(n) = Sum_{d|3} phi(d)*n^(3/d)                                                |
| 24  | A056220 | Inv:Rev-PolyRow3 | a(n) = 2*n^2 - 1                                                               |
| 25  | A058331 | Rev-PolyRow3     | a(n) = 2*n^2 + 1                                                               |
| 26  | A073028 | Inv-RowMax       | a(n) = max{ C(n,0), C(n-1,1), C(n-2,2), ..., C(n-n,n) }                        |
| 27  | A097690 | Inv-PolyDiag     | Numerators of the continued fraction n-1/(n-1/...) [n times]                   |
| 28  | A099530 | Inv:Rev-DiagSum  | Expansion of 1/(1 - x + x^4)                                                   |
| 29  | A101461 | Std-RowMax       | Row maximum of Catalan triangle with zeros (A053121), i.e., maximum value of ( |
| 30  | A106853 | Inv-PosHalf      | Expansion of 1/(1 - x + 4*x^2)                                                 |
| 31  | A107430 | Std-AccRev       | Triangle read by rows: row n is row n of Pascal's triangle (A007318) sorted in |
| 32  | A121724 | Std-PosHalf      | Generalized central binomial coefficients for k=2                              |
| 33  | A121725 | Rev-PolyCol3     | Generalized central coefficients for k=3                                       |
| 34  | A126120 | Std-DiagSum      | Catalan numbers (A000108) interpolated with 0's                                |
| 35  | A126596 | Std-CentralE     | a(n) = binomial(4*n,n)*(2*n+1)/(3*n+1)                                         |
| 36  | A126869 | Std-EvenSum      | a(n) = Sum_{k = 0..n} binomial(n,floor(k/2))*(-1)^(n-k)                        |
| 37  | A126931 | Std-PolyCol3     | a(n) = A127359(n+1)/2 - A127359(n)                                             |
| 38  | A138364 | Std-OddSum       | The number of Motzkin n-paths with exactly one flat step                       |
| 39  | A142150 | Inv-DiagCol1     | The nonnegative integers interleaved with 0's                                  |
| 40  | A146078 | Inv:Rev-PolyCol3 | Expansion of 1/(1-x*(1-9*x))                                                   |
| 41  | A162515 | Std-RevInv       | Triangle of coefficients of polynomials defined by Binet form: P(n,x) = (U^n - |
| 42  | A165817 | Inv-CentralO     | Number of compositions (= ordered integer partitions) of n into 2n parts       |
| 43  | A168561 | Std-Inv          | Riordan array (1/(1-x^2), x/(1-x^2)). Unsigned version of A049310              |
| 44  | A186731 | Inv-TransNat0    | a(3n) = 2n, a(3n+1) = n, a(3n+2) = n+1                                         |
| 45  | A242135 | Inv-PolyRow3     | a(n) = n^3 - 2*n                                                               |
| 46  | A274112 | Rev-DiagSum      | Number of equivalence classes of ballot paths of length n for the string ddu   |
| 47  | A278415 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, 2k)*binomial(n-k, k)*(-1)^k                    |
| 48  | A296663 | Std-AccSum       | Row sums of A296664                                                            |
| 49  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 50  | A344500 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*CT(n, k) = Sum_{k=0..n} (-1)^(n-k)*binomial |
| 51  | A359108 | Std-CentralO     | a(n) = A128899(2*n, n) = 2*binomial(4*n - 1, 3*n) for n >= 1 and a(0) = 1      |

* Statistic about CatalanPaths:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 51.
	all      A-numbers  : 143.
	missing  sequences  : 47.

[('missing', 47), ('A000027', 11), ('A001405', 10), ('A126120', 7), ('A344500', 6), ('A000012', 6), ('A121724', 5), ('A000079', 5), ('A296663', 4), ('A278415', 4), ('A168561', 4), ('A054341', 4), ('A052173', 4), ('A297382', 3), ('A162515', 3), ('A126596', 3), ('A107430', 3), ('A106853', 3), ('A101461', 3), ('A053121', 3), ('A002522', 3), ('A002057', 3), ('A000245', 3), ('A359108', 2), ('A142150', 2), ('A138364', 2), ('A126931', 2), ('A126869', 2), ('A073028', 2), ('A054602', 2), ('A045621', 2), ('A025560', 2), ('A005809', 2), ('A005563', 2), ('A000292', 2), ('A000217', 2), ('A000045', 2), ('A274112', 1), ('A242135', 1), ('A186731', 1), ('A165817', 1), ('A146078', 1), ('A121725', 1), ('A099530', 1), ('A097690', 1), ('A058331', 1), ('A056220', 1), ('A045721', 1), ('A026005', 1), ('A001906', 1), ('A000957', 1), ('A000007', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CatalanPaths.html .
2025/01/10

'''
