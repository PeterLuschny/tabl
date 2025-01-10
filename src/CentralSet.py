from functools import cache
from _tabltypes import MakeTriangle

"""Central set factorial numbers.

[0] [1]
[1] [0, 1]
[2] [0, 1,    1]
[3] [0, 1,    5,      1]
[4] [0, 1,   21,     14,      1]
[5] [0, 1,   85,    147,     30,     1]
[6] [0, 1,  341,   1408,    627,    55,    1]
[7] [0, 1, 1365,  13013,  11440,  2002,   91,   1]
[8] [0, 1, 5461, 118482, 196053, 61490, 5278, 140,  1]
"""


@cache
def centralset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = centralset(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


@MakeTriangle(centralset, "CentralSet", ["A269945", "A008957", "A036969"], True)
def CentralSet(n: int, k: int) -> int:
    return centralset(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(CentralSet)

''' OEIS

The traits of the CentralSet triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000330 | Std-DiagRow1     | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1) |
| 5   | A000596 | Inv-DiagRow2     | Central factorial numbers                                                      |
| 6   | A000597 | Inv-DiagRow3     | Central factorial numbers                                                      |
| 7   | A001044 | Inv-DiagCol1     | a(n) = (n!)^2                                                                  |
| 8   | A001819 | Inv-RowMax       | Central factorial numbers: second right-hand column of triangle A008955        |
| 9   | A001820 | Inv-DiagCol3     | Central factorial numbers                                                      |
| 10  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 11  | A002450 | Std-DiagCol2     | a(n) = (4^n - 1)/3                                                             |
| 12  | A002451 | Std-DiagCol3     | Expansion of 1/((1-x)*(1-4*x)*(1-9*x))                                         |
| 13  | A010791 | Inv-AccSum       | a(n) = n!*(n+2)!/2                                                             |
| 14  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 15  | A033954 | Inv:Rev-PolyRow3 | Second 10-gonal (or decagonal) numbers: n*(4*n+3)                              |
| 16  | A051893 | Inv-EvenSum      | a(n) = Sum_{i=1..n-1} i^2*a(i), a(1) = 1                                       |
| 17  | A060493 | Std-DiagRow2     | A diagonal of A036969                                                          |
| 18  | A082111 | Rev-PolyRow3     | a(n) = n^2 + 5*n + 1                                                           |
| 19  | A101686 | Inv-AltSum       | a(n) = Product_{i=1..n} (i^2 + 1)                                              |
| 20  | A128059 | Std-RowGcd       | a(n) = numerator((2*n-1)^2/(2*(2*n)!))                                         |
| 21  | A135920 | Std-RowSum       | O.g.f.: A(x) = Sum_{n>=0} x^n / Product_{k=0..n} (1 - k^2*x)                   |
| 22  | A234324 | Inv:Rev-CentralO | Central terms of the triangle of central factorial numbers (A008955)           |
| 23  | A269944 | Std-Inv          | Triangle read by rows, Stirling cycle numbers of order 2, T(n, n) = 1, T(n, k) |
| 24  | A269945 | Std-Triangle     | Triangle read by rows. Stirling set numbers of order 2, T(n, n) = 1, T(n, k) = |
| 25  | A277352 | Inv-NegHalf      | a(n) = Product_{k=1..n} (2*k^2+1)                                              |
| 26  | A298851 | Std-CentralE     | a(n) = [x^n] Product_{k=1..n} 1/(1-k^2*x)                                      |
| 27  | A351105 | Std-DiagRow3     | a(n) = Sum_{k=1..n} Sum_{j=1..k} Sum_{i=1..j} (i*j*k)^2                        |

* Statistic about CentralSet:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 27.
	all      A-numbers  : 94.
	missing  sequences  : 121.

[('missing', 121), ('A000012', 11), ('A010791', 8), ('A135920', 6), ('A000330', 5), ('A000027', 5), ('A000007', 5), ('A269944', 4), ('A101686', 4), ('A051893', 4), ('A001819', 4), ('A351105', 3), ('A298851', 3), ('A269945', 3), ('A128059', 3), ('A060493', 3), ('A002451', 3), ('A002450', 3), ('A002378', 3), ('A019590', 2), ('A001820', 2), ('A001044', 2), ('A000597', 2), ('A000596', 2), ('A277352', 1), ('A234324', 1), ('A082111', 1), ('A033954', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CentralSet.html .
2025/01/10

'''
