from functools import cache
from _tabltypes import MakeTriangle

"""Worpitzky triangle.

[0]  1;
[1]  1,   1;
[2]  1,   3,    2;
[3]  1,   7,   12,     6;
[4]  1,  15,   50,    60,     24;
[5]  1,  31,  180,   390,    360,    120;
[6]  1,  63,  602,  2100,   3360,   2520,    720;
[7]  1, 127, 1932, 10206,  25200,  31920,  20160,   5040;
[8]  1, 255, 6050, 46620, 166824, 317520, 332640, 181440, 40320;
"""


@cache
def worpitzky(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = worpitzky(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k - 1] + (k + 1) * row[k]
    return row


@MakeTriangle(
    worpitzky,
    "Worpitzky",
    ["A028246", "A053440", "A075263", "A130850", "A163626"],
    False,
)
def Worpitzky(n: int, k: int) -> int:
    return worpitzky(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Worpitzky)

''' OEIS

The traits of the Worpitzky triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000142 | Std-ColRight     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 5   | A000169 | Std-BinConv      | Number of labeled rooted trees with n nodes: n^(n-1)                           |
| 6   | A000225 | Std-DiagCol1     | a(n) = 2^n - 1. (Sometimes called Mersenne numbers, although that name is usua |
| 7   | A000384 | Std-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 8   | A000629 | Std-RowSum       | Number of necklaces of partitions of n+1 labeled beads                         |
| 9   | A000670 | Std-EvenSum      | Fubini numbers: number of preferential arrangements of n labeled elements; or  |
| 10  | A001710 | Std-DiagRow1     | Order of alternating group A_n, or number of even permutations of n letters    |
| 11  | A002378 | Rev-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A004123 | Alt-PolyCol3     | Number of generalized weak orders on n points                                  |
| 13  | A005460 | Std-DiagRow2     | a(n) = (3*n+4)*(n+3)!/24                                                       |
| 14  | A005461 | Std-DiagRow3     | Number of simplices in barycentric subdivision of n-simplex                    |
| 15  | A009006 | Std-NegHalf      | Expansion of e.g.f.: 1 + tan(x)                                                |
| 16  | A014105 | Alt-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 17  | A016269 | Rev:Inv-DiagRow2 | Number of monotone Boolean functions of n variables with 2 mincuts. Also numbe |
| 18  | A019538 | Std-Diffx1       | Triangle of numbers T(n,k) = k!*Stirling2(n,k) read by rows (n >= 1, 1 <= k <= |
| 19  | A028243 | Std-DiagCol2     | a(n) = 3^(n-1) - 2^n + 1 (essentially Stirling numbers of second kind)         |
| 20  | A028244 | Std-DiagCol3     | a(n) = 4^(n-1) - 3*3^(n-1) + 3*2^(n-1) - 1 (essentially Stirling numbers of se |
| 21  | A028246 | Std-Triangle     | Triangular array a(n,k) = (1/k)*Sum_{i=0..k} (-1)^(k-i)*binomial(k,i)*i^n; n > |
| 22  | A028387 | Rev:Inv-PolyRow2 | a(n) = n + (n+1)^2                                                             |
| 23  | A036563 | Alt-TransSqrs    | a(n) = 2^n - 3                                                                 |
| 24  | A054255 | Std-AccRev       | Triangle T(n,k) (n >= 1, 0<=k<=n) giving number of preferential arrangements o |
| 25  | A089026 | Rev:Inv-RowGcd   | a(n) = n if n is a prime, otherwise a(n) = 1                                   |
| 26  | A094421 | Alt-PolyRow3     | a(n) = n * (6*n^2 + 6*n + 1)                                                   |
| 27  | A106340 | Std-InvRev       | Triangle T, read by rows, equal to the matrix inverse of the triangle defined  |
| 28  | A106341 | Rev:Inv-DiagCol1 | Column 1 of triangle A106340                                                   |
| 29  | A123227 | Std-PosHalf      | Expansion of e.g.f.: 2*exp(2*x) / (3 - exp(2*x))                               |
| 30  | A130850 | Std-Rev          | Triangle read by rows, 0 <= k <= n, T(n,k) = Sum_{j=0..n} A(n,j)*binomial(n-j, |
| 31  | A185157 | Std-CentralE     | G.f. A(x) = sum(n>0, a(n)*x^n/(2*n-1)!) is the inverse function to x*Bernoulli |
| 32  | A201339 | Std-PolyCol2     | Expansion of e.g.f. exp(x) / (3 - 2*exp(x))                                    |
| 33  | A201354 | Std-PolyCol3     | Expansion of e.g.f. exp(x) / (4 - 3*exp(x))                                    |
| 34  | A201355 | Rev-PolyCol3     | Expansion of e.g.f.: 3*exp(3*x) / (4 - exp(3*x))                               |
| 35  | A229046 | Std-DiagSum      | G.f.: Sum_{n>=0} n! * x^n * (1+x)^n / Product_{k=1..n} (1 + k*x)               |
| 36  | A343583 | Std-TransNat0    | a(n) = (1/2)*Li_{-n-1}(1/2) - Li_{-n}(1/2), where Li_{n}(x) is the polylogarit |
| 37  | A343584 | Std-InvBinConv   | a(n) = Sum_{j=0..n}(-1)^(n-j)*binomial(n, j)*A028246(n+1, j+1)                 |
| 38  | A369435 | Std-Poly         | Square array A(n, k) = n! * [t^n] (exp(t)/(1+k-k*exp(t))) for n >= 0 and k >=  |
| 39  | A372312 | Std-PolyDiag     | Row sums of A372311                                                            |

* Statistic about Worpitzky:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 39.
	all      A-numbers  : 102.
	missing  sequences  : 67.

[('missing', 67), ('A000670', 11), ('A000012', 9), ('A000629', 6), ('A000027', 5), ('A130850', 4), ('A106340', 4), ('A000225', 4), ('A343584', 3), ('A185157', 3), ('A123227', 3), ('A028246', 3), ('A028244', 3), ('A028243', 3), ('A005461', 3), ('A005460', 3), ('A001710', 3), ('A000169', 3), ('A000142', 3), ('A000007', 3), ('A201339', 2), ('A054255', 2), ('A009006', 2), ('A372312', 1), ('A369435', 1), ('A343583', 1), ('A229046', 1), ('A201355', 1), ('A201354', 1), ('A106341', 1), ('A094421', 1), ('A089026', 1), ('A036563', 1), ('A028387', 1), ('A019538', 1), ('A016269', 1), ('A014105', 1), ('A004123', 1), ('A002378', 1), ('A000384', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Worpitzky.html .
2025/01/10

'''
