from functools import cache
from _tabltypes import MakeTriangle

"""
T(n,k) = binomial(n, k) * Catalan(n - k).
       = CatalanNumber(k) * Pochhammer(-n, k) / k!

[0] 1;
[1] 1, 1;
[2] 1, 2,  2;
[3] 1, 3,  6,   5;
[4] 1, 4, 12,  20,  14;
[5] 1, 5, 20,  50,  70,  42;
[6] 1, 6, 30, 100, 210, 252, 132;
[7] 1, 7, 42, 175, 490, 882, 924, 429;
"""


@cache
def binomialcatalan(n: int) -> list[int]:
    if n == 0:
        return [1]

    a = binomialcatalan(n - 1) + [0]
    row = [0] * (n + 1)
    row[0] = 1
    row[1] = n
    for k in range(2, n + 1):
        row[k] = (a[k] * (n + k + 1) + a[k - 1] * (4 * k - 2)) // (n + 1)

    return row


@MakeTriangle(binomialcatalan, "BinomialCatalan", ["A124644", "A098474"], True)
def BinomialCatalan(n: int, k: int) -> int:
    return binomialcatalan(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BinomialCatalan)

''' OEIS

The traits of the BinomialCatalan triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000034 | Std-RowGcd       | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 4   | A000108 | Std-ColRight     | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 5   | A000292 | Rev:Inv-DiagRow3 | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 6   | A000888 | Std-CentralE     | a(n) = (2*n)!^2 / ((n+1)!*n!^3)                                                |
| 7   | A000891 | Std-CentralO     | a(n) = (2*n)!*(2*n+1)! / (n! * (n+1)!)^2                                       |
| 8   | A000984 | Std-DiagRow1     | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 9   | A001405 | Std-NegHalf      | a(n) = binomial(n, floor(n/2))                                                 |
| 10  | A001844 | Std-PolyRow2     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 11  | A002378 | Std-DiagCol2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A002426 | Alt-AccRevSum    | Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n         |
| 13  | A002522 | Rev-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 14  | A005043 | Std-AltSum       | Riordan numbers: a(n) = (n-1)*(2*a(n-1) + 3*a(n-2))/(n+1)                      |
| 15  | A005491 | Rev-PolyRow3     | a(n) = n^3 + 3*n + 1                                                           |
| 16  | A005563 | Rev:Inv-PolyRow2 | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 17  | A005717 | Alt-TransNat0    | Construct triangle in which n-th row is obtained by expanding (1 + x + x^2)^n  |
| 18  | A007317 | Std-RowSum       | Binomial transform of Catalan numbers                                          |
| 19  | A026375 | Std-AccRevSum    | a(n) = Sum_{k=0..n} binomial(n,k)*binomial(2*k,k)                              |
| 20  | A026376 | Std-TransNat0    | a(n) is the number of integer strings s(0),...,s(n) counted by array T in A026 |
| 21  | A064613 | Std-PosHalf      | Second binomial transform of the Catalan numbers                               |
| 22  | A086618 | Std-BinConv      | a(n) = Sum{k=0..n} binomial(n,k)^2*C(k), where C() = A000108() are the Catalan |
| 23  | A090344 | Std-DiagSum      | Number of Motzkin paths of length n with no level steps at odd level           |
| 24  | A092443 | Std-DiagRow2     | Sequence arising from enumeration of domino tilings of Aztec Pillow-like regio |
| 25  | A098465 | Std-EvenSum      | Expansion of (sqrt(1+3*x)-sqrt(1-5*x))/(4*x*sqrt(1-x))                         |
| 26  | A098473 | Std-Diffx1       | Triangle T(n,k) read by rows, T(n, k) = binomial(2*k, k)*binomial(n, k), 0<=k< |
| 27  | A098474 | Std-Triangle     | Triangle read by rows, T(n,k) = C(n,k)*C(2*k,k)/(k+1), n >= 0, 0 <= k <= n     |
| 28  | A102318 | Rev-EvenSum      | A mean binomial transform of the Catalan numbers                               |
| 29  | A104455 | Rev-PolyCol3     | Expansion of e.g.f. exp(5*x)*(BesselI(0,2*x) - BesselI(1,2*x))                 |
| 30  | A105864 | Rev-DiagSum      | Expansion of (1/(1-x^2))*c(x/(1-x^2)), where c(x) is the g.f. of A000108       |
| 31  | A124644 | Std-Rev          | Triangle read by rows. T(n, k) = binomial(n, k) * CatalanNumber(n - k)         |
| 32  | A125558 | Rev-CentralO     | Central column of triangle A090181                                             |
| 33  | A134481 | Std-DiagCol3     | Row sums of triangle A134480                                                   |
| 34  | A162326 | Std-PolyCol2     | Let a(0) = a(1) = 1, and n*a(n) = 2*(-7+5*n)*a(n-1) + 9*(2-n)*a(n-2) for n >=  |
| 35  | A178955 | Rev:Inv-ColLeft  | E.g.f. is inverse of e.g.f. for Catalan numbers                                |
| 36  | A271025 | Rev-Poly         | A(n, k) is the n-th binomial transform of the Catalan sequence (A000108) evalu |
| 37  | A292632 | Rev-PolyDiag     | a(n) = n! * [x^n] exp((n+2)*x)*(BesselI(0,2*x) - BesselI(1,2*x))               |
| 38  | A308849 | Rev:Inv-PolyCol2 | Expansion of e.g.f. 1 / (BesselI(0,2*x) + BesselI(1,2*x))                      |
| 39  | A337167 | Std-PolyCol3     | a(n) = 1 + 3 * Sum_{k=0..n-1} a(k) * a(n-k-1)                                  |
| 40  | A337168 | Alt-PolyCol2     | a(n) = (-1)^n + 2 * Sum_{k=0..n-1} a(k) * a(n-k-1)                             |
| 41  | A337169 | Alt-PolyCol3     | a(n) = (-1)^n + 3 * Sum_{k=0..n-1} a(k) * a(n-k-1)                             |
| 42  | A338979 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k * binomial(n,k) * Catalan(k)                           |
| 43  | A339001 | Alt-PolyDiag     | a(n) = (-1)^n * Sum_{k=0..n} (-n)^k * binomial(n,k) * Catalan(k)               |
| 44  | A360024 | Alt-DiagSum      | a(n) = Sum_{k=0..floor(n/2)} (-1)^k * binomial(n-k,k) * Catalan(k)             |

* Statistic about BinomialCatalan:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 44.
	all      A-numbers  : 94.
	missing  sequences  : 78.

[('missing', 78), ('A000027', 8), ('A007317', 6), ('A124644', 4), ('A000012', 4), ('A134481', 3), ('A098474', 3), ('A092443', 3), ('A086618', 3), ('A064613', 3), ('A026375', 3), ('A005043', 3), ('A002378', 3), ('A000984', 3), ('A000888', 3), ('A000108', 3), ('A000034', 3), ('A337168', 2), ('A162326', 2), ('A098473', 2), ('A098465', 2), ('A002426', 2), ('A001844', 2), ('A001405', 2), ('A000891', 2), ('A360024', 1), ('A339001', 1), ('A338979', 1), ('A337169', 1), ('A337167', 1), ('A308849', 1), ('A292632', 1), ('A271025', 1), ('A178955', 1), ('A125558', 1), ('A105864', 1), ('A104455', 1), ('A102318', 1), ('A090344', 1), ('A026376', 1), ('A005717', 1), ('A005563', 1), ('A005491', 1), ('A002522', 1), ('A000292', 1)]

A related webpage is: https://peterluschny.github.io/tabl/BinomialCatalan.html .
2025/01/10

'''
