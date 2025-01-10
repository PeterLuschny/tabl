from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Chebyshev S(n, x) = U(n, x/2) polynomials.

[0]  1;
[1]  0,  1;
[2] -1,  0,   1;
[3]  0, -2,   0,   1;
[4]  1,  0,  -3,   0,  1;
[5]  0,  3,   0,  -4,  0,  1;
[6] -1,  0,   6,   0, -5,  0,  1;
[7]  0, -4,   0,  10,  0, -6,  0,   1;
[8]  1,  0, -10,   0, 15,  0, -7,   0, 1;
[9]  0,  5,   0, -20,  0,  21,  0, -8, 0, 1;
"""


@cache
def chebyshevs(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov = chebyshevs(n - 2)
    row = [0] + chebyshevs(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


@MakeTriangle(
    chebyshevs, "ChebyshevS", ["A049310", "A053119", "A112552", "A168561"], True
)
def ChebyshevS(n: int, k: int) -> int:
    return chebyshevs(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(ChebyshevS)

''' OEIS

The traits of the ChebyshevS triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-DiagSum      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000045 | Std-AbsSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 5   | A000079 | Inv-AccRevSum    | Powers of 2: a(n) = 2^n                                                        |
| 6   | A000217 | Std-DiagCol2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000245 | Inv-DiagCol2     | a(n) = 3*(2*n)!/((n+2)!*(n-1)!)                                                |
| 8   | A000292 | Std-DiagCol3     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 9   | A001405 | Inv-RowSum       | a(n) = binomial(n, floor(n/2))                                                 |
| 10  | A001906 | Std-PolyCol3     | F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)              |
| 11  | A002057 | Inv-DiagCol3     | Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)        |
| 12  | A002522 | Inv-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 13  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 14  | A005809 | Std-CentralE     | a(n) = binomial(3n,n)                                                          |
| 15  | A025560 | Std-RowLcm       | a(n) = LCM{1, C(n-1,1), C(n-2,2), ..., C(n-[ n/2 ],[ n/2 ])}                   |
| 16  | A026005 | Inv:Rev-CentralO | a(n) = T(4*n,n), where T = Catalan triangle (A008315)                          |
| 17  | A045621 | Inv-TransNat0    | a(n) = 2^n - binomial(n, floor(n/2))                                           |
| 18  | A045721 | Rev-CentralO     | a(n) = binomial(3*n+1,n)                                                       |
| 19  | A052173 | Std-RevInv       | Another version of the Catalan triangle A008315                                |
| 20  | A053121 | Std-Inv          | Catalan triangle (with 0's) read by rows                                       |
| 21  | A054341 | Inv-PolyCol2     | Row sums of triangle A054336 (central binomial convolutions)                   |
| 22  | A054602 | Inv-PolyRow3     | a(n) = Sum_{d|3} phi(d)*n^(3/d)                                                |
| 23  | A056220 | Rev-PolyRow3     | a(n) = 2*n^2 - 1                                                               |
| 24  | A058331 | Inv:Rev-PolyRow3 | a(n) = 2*n^2 + 1                                                               |
| 25  | A073028 | Std-RowMax       | a(n) = max{ C(n,0), C(n-1,1), C(n-2,2), ..., C(n-n,n) }                        |
| 26  | A077957 | Alt-DiagSum      | Powers of 2 alternating with zeros                                             |
| 27  | A097690 | Std-PolyDiag     | Numerators of the continued fraction n-1/(n-1/...) [n times]                   |
| 28  | A099530 | Rev-DiagSum      | Expansion of 1/(1 - x + x^4)                                                   |
| 29  | A101461 | Inv-RowMax       | Row maximum of Catalan triangle with zeros (A053121), i.e., maximum value of ( |
| 30  | A106853 | Std-PosHalf      | Expansion of 1/(1 - x + 4*x^2)                                                 |
| 31  | A107430 | Inv-AccRev       | Triangle read by rows: row n is row n of Pascal's triangle (A007318) sorted in |
| 32  | A121724 | Inv-PosHalf      | Generalized central binomial coefficients for k=2                              |
| 33  | A121725 | Inv:Rev-PolyCol3 | Generalized central coefficients for k=3                                       |
| 34  | A126120 | Inv-DiagSum      | Catalan numbers (A000108) interpolated with 0's                                |
| 35  | A126596 | Inv-CentralE     | a(n) = binomial(4*n,n)*(2*n+1)/(3*n+1)                                         |
| 36  | A126869 | Inv-EvenSum      | a(n) = Sum_{k = 0..n} binomial(n,floor(k/2))*(-1)^(n-k)                        |
| 37  | A126931 | Inv-PolyCol3     | a(n) = A127359(n+1)/2 - A127359(n)                                             |
| 38  | A138364 | Inv-OddSum       | The number of Motzkin n-paths with exactly one flat step                       |
| 39  | A142150 | Std-DiagCol1     | The nonnegative integers interleaved with 0's                                  |
| 40  | A146078 | Rev-PolyCol3     | Expansion of 1/(1-x*(1-9*x))                                                   |
| 41  | A162515 | Std-Rev          | Triangle of coefficients of polynomials defined by Binet form: P(n,x) = (U^n - |
| 42  | A165817 | Std-CentralO     | Number of compositions (= ordered integer partitions) of n into 2n parts       |
| 43  | A168561 | Std-Triangle     | Riordan array (1/(1-x^2), x/(1-x^2)). Unsigned version of A049310              |
| 44  | A186731 | Std-TransNat0    | a(3n) = 2n, a(3n+1) = n, a(3n+2) = n+1                                         |
| 45  | A242135 | Std-PolyRow3     | a(n) = n^3 - 2*n                                                               |
| 46  | A274112 | Inv:Rev-DiagSum  | Number of equivalence classes of ballot paths of length n for the string ddu   |
| 47  | A278415 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, 2k)*binomial(n-k, k)*(-1)^k                    |
| 48  | A296663 | Inv-AccSum       | Row sums of A296664                                                            |
| 49  | A297382 | Inv-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 50  | A344500 | Inv-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)*CT(n, k) = Sum_{k=0..n} (-1)^(n-k)*binomial |
| 51  | A359108 | Inv-CentralO     | a(n) = A128899(2*n, n) = 2*binomial(4*n - 1, 3*n) for n >= 1 and a(0) = 1      |

* Statistic about ChebyshevS:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 51.
	all      A-numbers  : 133.
	missing  sequences  : 48.

[('missing', 48), ('A000027', 12), ('A001405', 7), ('A278415', 6), ('A000012', 6), ('A126120', 5), ('A106853', 5), ('A344500', 4), ('A053121', 4), ('A296663', 3), ('A162515', 3), ('A142150', 3), ('A121724', 3), ('A073028', 3), ('A054341', 3), ('A052173', 3), ('A025560', 3), ('A005809', 3), ('A005563', 3), ('A000292', 3), ('A000217', 3), ('A000079', 3), ('A000045', 3), ('A297382', 2), ('A242135', 2), ('A186731', 2), ('A168561', 2), ('A165817', 2), ('A126596', 2), ('A107430', 2), ('A101461', 2), ('A097690', 2), ('A002522', 2), ('A002057', 2), ('A001906', 2), ('A000245', 2), ('A359108', 1), ('A274112', 1), ('A146078', 1), ('A138364', 1), ('A126931', 1), ('A126869', 1), ('A121725', 1), ('A099530', 1), ('A077957', 1), ('A058331', 1), ('A056220', 1), ('A054602', 1), ('A045721', 1), ('A045621', 1), ('A026005', 1), ('A000007', 1)]

A related webpage is: https://peterluschny.github.io/tabl/ChebyshevS.html .
2025/01/10

'''
