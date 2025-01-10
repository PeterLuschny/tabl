from functools import cache
from _tabltypes import MakeTriangle

"""Balott Catalan triangle.

[0] 1;
[1] 0,    1;
[2] 0,    2,    1;
[3] 0,    5,    4,    1;
[4] 0,   14,   14,    6,    1;
[5] 0,   42,   48,   27,    8,    1;
[6] 0,  132,  165,  110,   44,   10,   1;
[7] 0,  429,  572,  429,  208,   65,  12,   1;
[8] 0, 1430, 2002, 1638,  910,  350,  90,  14,  1;
[9] 0, 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1;
"""


@cache
def catalan(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    pow = catalan(n - 1) + [0]
    row = pow.copy()
    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]
    row[n] = 1

    return row


@MakeTriangle(catalan, "Catalan", ["A128899", "A039598"], True)
def Catalan(n: int, k: int) -> int:
    return catalan(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Catalan)

''' OEIS

The traits of the Catalan triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Inv-DiagSum      | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000108 | Std-AltSum       | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 6   | A000292 | Inv-DiagCol2     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 7   | A000302 | Std-TransNat0    | Powers of 4: a(n) = 4^n                                                        |
| 8   | A000389 | Inv-DiagCol3     | Binomial coefficients C(n,5)                                                   |
| 9   | A000957 | Std-DiagSum      | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 10  | A000984 | Std-OddSum       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 11  | A001700 | Std-RowSum       | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 12  | A001791 | Std-EvenSum      | a(n) = binomial coefficient C(2n, n-1)                                         |
| 13  | A001906 | Inv-AltSum       | F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)              |
| 14  | A002057 | Std-DiagCol2     | Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)        |
| 15  | A002450 | Inv-NegHalf      | a(n) = (4^n - 1)/3                                                             |
| 16  | A002457 | Std-TransSqrs    | a(n) = (2n+1)!/n!^2                                                            |
| 17  | A002492 | Inv-DiagRow3     | Sum of the first n even squares: 2*n*(n+1)*(2*n+1)/3                           |
| 18  | A003517 | Std-DiagCol3     | Number of permutations of [n+1] with exactly 1 increasing subsequence of lengt |
| 19  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                                |
| 20  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 21  | A005843 | Std-DiagRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 22  | A010673 | Inv-PolyCol2     | Period 2: repeat [0, 2]                                                        |
| 23  | A014105 | Inv-DiagRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 24  | A014106 | Std-DiagRow2     | a(n) = n*(2*n + 3)                                                             |
| 25  | A025174 | Std-BinConv      | a(n) = binomial(3n-1, n-1)                                                     |
| 26  | A026005 | Rev-CentralO     | a(n) = T(4*n,n), where T = Catalan triangle (A008315)                          |
| 27  | A038665 | Alt-AccSum       | Convolution of A007054 (super ballot numbers) with A000984 (central binomial c |
| 28  | A045721 | Inv:Rev-CentralO | a(n) = binomial(3*n+1,n)                                                       |
| 29  | A045944 | Inv:Rev-PolyRow3 | Rhombic matchstick numbers: a(n) = n*(3*n+2)                                   |
| 30  | A049072 | Inv-PosHalf      | Expansion of 1/(1 - 3*x + 4*x^2)                                               |
| 31  | A052530 | Inv:Rev-NegHalf  | a(n) = 4*a(n-1) - a(n-2), with a(0) = 0, a(1) = 2                              |
| 32  | A063524 | Alt-TransNat0    | Characteristic function of 1                                                   |
| 33  | A064062 | Std-NegHalf      | Generalized Catalan numbers C(2; n)                                            |
| 34  | A067336 | Std-PolyCol2     | a(0)=1, a(1)=2, a(n) = a(n-1)*9/2 - Catalan(n-1) where Catalan(n) = binomial(2 |
| 35  | A068875 | Alt-TransSqrs    | Expansion of (1 + x*C)*C, where C = (1 - (1 - 4*x)^(1/2))/(2*x) is the g.f. fo |
| 36  | A079273 | Rev-PolyRow3     | Octo numbers (a polygonal sequence): a(n) = 5*n^2 - 6*n + 2 = (n-1)^2 + (2*n-1 |
| 37  | A099838 | Inv-PolyCol3     | Expansion of (1-x)^2*(1+x)/(1+x+x^2)                                           |
| 38  | A099996 | Inv-RowLcm       | a(n) = lcm{1, 2, ..., 2*n}                                                     |
| 39  | A104530 | Std-PolyCol3     | Expansion of (1+sqrt(1-4x))/(4sqrt(1-4x)-2)                                    |
| 40  | A113066 | Inv-OddSum       | Expansion of (1 + x)^2/((1 + x + x^2)*(1 + 3*x + x^2))                         |
| 41  | A114121 | Std-AccRevSum    | Expansion of (sqrt(1 - 4*x) + (1 - 2*x))/(2*(1 - 4*x))                         |
| 42  | A122918 | Inv-TransNat0    | Expansion of (1+x)^2/(1+x+x^2)^2                                               |
| 43  | A128899 | Std-Triangle     | Riordan array (1,(1-2x-sqrt(1-4x))/(2x))                                       |
| 44  | A128908 | Std-Inv          | Riordan array (1, x/(1-x)^2)                                                   |
| 45  | A135334 | Alt-DiagSum      | Number of Dyck paths of semilength n having no UDDU's starting at level 1      |
| 46  | A137241 | Inv-AccRevSum    | Number triples (k,3-k,2-2k), concatenated for k=0, 1, 2, 3,..                  |
| 47  | A165817 | Inv-CentralE     | Number of compositions (= ordered integer partitions) of n into 2n parts       |
| 48  | A172060 | Rev-TransNat0    | The number of returns to the origin in all possible one-dimensional walks of l |
| 49  | A190970 | Inv:Rev-PolyCol3 | a(n) = 5*a(n-1) - 9*a(n-2), with a(0)=0, a(1)=1                                |
| 50  | A194723 | Std-PosHalf      | Number of ternary words either empty or beginning with the first character of  |
| 51  | A194724 | Rev-PolyCol3     | Number of quaternary words either empty or beginning with the first character  |
| 52  | A224747 | Rev-DiagSum      | Number of lattice paths from (0,0) to (n,0) that do not go below the x-axis an |
| 53  | A262440 | Inv-InvBinConv   | a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k-1,n-k)                        |
| 54  | A290890 | Inv-EvenSum      | p-INVERT of the positive integers, where p(S) = 1 - S^2                        |
| 55  | A296770 | Std-AccSum       | Row sums of A050158                                                            |
| 56  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 57  | A329682 | Inv-RowSum       | Number of excursions of length n with Motzkin-steps forbidding all consecutive |
| 58  | A332057 | Inv-AccSum       | Partial sums (and absolute value of first differences) of A332056: if odd (res |
| 59  | A350290 | Inv-BinConv      | a(n) = Sum_{k=0..n} (-1)^(n - k) * binomial(n, k) * binomial(n + k - 1, n - k) |
| 60  | A359108 | Std-CentralE     | a(n) = A128899(2*n, n) = 2*binomial(4*n - 1, 3*n) for n >= 1 and a(0) = 1      |
| 61  | A376716 | Inv:Rev-EvenSum  | Expansion of (1 - x + x^2)/((1 - x + x^2)^2 - 4*x^2)                           |

* Statistic about Catalan:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 61.
	all      A-numbers  : 140.
	missing  sequences  : 74.

[('missing', 74), ('A000108', 8), ('A001700', 6), ('A000012', 6), ('A297382', 5), ('A005843', 5), ('A000027', 5), ('A000007', 5), ('A128908', 4), ('A001906', 4), ('A359108', 3), ('A332057', 3), ('A296770', 3), ('A194723', 3), ('A137241', 3), ('A128899', 3), ('A114121', 3), ('A025174', 3), ('A014106', 3), ('A005563', 3), ('A003517', 3), ('A002057', 3), ('A350290', 2), ('A329682', 2), ('A262440', 2), ('A165817', 2), ('A099996', 2), ('A067336', 2), ('A064062', 2), ('A049072', 2), ('A014105', 2), ('A010673', 2), ('A005408', 2), ('A002492', 2), ('A001791', 2), ('A000984', 2), ('A000389', 2), ('A000292', 2), ('A376716', 1), ('A290890', 1), ('A224747', 1), ('A194724', 1), ('A190970', 1), ('A172060', 1), ('A135334', 1), ('A122918', 1), ('A113066', 1), ('A104530', 1), ('A099838', 1), ('A079273', 1), ('A068875', 1), ('A063524', 1), ('A052530', 1), ('A045944', 1), ('A045721', 1), ('A038665', 1), ('A026005', 1), ('A002457', 1), ('A002450', 1), ('A000957', 1), ('A000302', 1), ('A000079', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Catalan.html .
2025/01/10

'''
