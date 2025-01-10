from functools import cache
from _tabltypes import MakeTriangle

"""DyckPaths

[0]    1;
[1]    1,     1;
[2]    2,     3,     1;
[3]    5,     9,     5,    1;
[4]   14,    28,    20,    7,    1;
[5]   42,    90,    75,   35,    9,    1;
[6]  132,   297,   275,  154,   54,   11,   1;
[7]  429,  1001,  1001,  637,  273,   77,  13,   1;
[8] 1430,  3432,  3640, 2548, 1260,  440, 104,  15,  1;
[9] 4862, 11934, 13260, 9996, 5508, 2244, 663, 135, 17, 1;
"""


@cache
def dyckpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    pow = dyckpaths(n - 1) + [0]
    row = pow.copy()
    row[0] += row[1]
    row[n] = 1

    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]

    return row


@MakeTriangle(dyckpaths, "DyckPaths", ["A039599", "A050155"], True)
def DyckPaths(n: int, k: int) -> int:
    return dyckpaths(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(DyckPaths)

''' OEIS

The traits of the DyckPaths triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Inv-DiagSum      | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000108 | Std-ColLeft      | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)                |
| 6   | A000217 | Inv-DiagCol1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000245 | Std-DiagCol1     | a(n) = 3*(2*n)!/((n+2)!*(n-1)!)                                                |
| 8   | A000332 | Inv-DiagCol2     | Binomial coefficient binomial(n,4) = n*(n-1)*(n-2)*(n-3)/24                    |
| 9   | A000344 | Std-DiagCol2     | a(n) = 5*binomial(2n, n-2)/(n+3)                                               |
| 10  | A000346 | Std-TransNat0    | a(n) = 2^(2*n+1) - binomial(2*n+1, n+1)                                        |
| 11  | A000384 | Rev-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 12  | A000447 | Inv-DiagRow3     | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3               |
| 13  | A000531 | Std-TransSqrs    | From area of cyclic polygon of 2n + 1 sides                                    |
| 14  | A000579 | Inv-DiagCol3     | Figurate numbers or binomial coefficients C(n,6)                               |
| 15  | A000588 | Std-DiagCol3     | a(n) = 7*binomial(2n,n-3)/(n+4)                                                |
| 16  | A000957 | Alt-PolyCol2     | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 17  | A000958 | Std-DiagSum      | Number of ordered rooted trees with n edges having root of odd degree          |
| 18  | A000984 | Std-RowSum       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 19  | A001519 | Inv-AltSum       | a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1                      |
| 20  | A001700 | Std-EvenSum      | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 21  | A001835 | Inv:Rev-NegHalf  | a(n) = 4*a(n-1) - a(n-2), with a(0) = 1, a(1) = 1                              |
| 22  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 23  | A005408 | Std-DiagRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 24  | A005809 | Inv-CentralE     | a(n) = binomial(3n,n)                                                          |
| 25  | A007583 | Inv-NegHalf      | a(n) = (2^(2*n + 1) + 1)/3                                                     |
| 26  | A007854 | Std-PolyCol2     | Expansion of 1/(1 - 3*x*C(x)), where C(x) = (1 - sqrt(1 - 4*x))/(2*x) = g.f. f |
| 27  | A014107 | Std-DiagRow2     | a(n) = n*(2*n-3)                                                               |
| 28  | A025174 | Inv:Rev-CentralO | a(n) = binomial(3n-1, n-1)                                                     |
| 29  | A027849 | Rev-PolyRow3     | a(n) = (n+1)*(5*n^2+4*n+1)                                                     |
| 30  | A028387 | Inv-PolyRow2     | a(n) = n + (n+1)^2                                                             |
| 31  | A032443 | Std-AccRevSum    | a(n) = Sum_{i=0..n} binomial(2*n, i)                                           |
| 32  | A034839 | Inv-AntiDiag     | Triangular array formed by taking every other term of each row of Pascal's tri |
| 33  | A035610 | Rev-PolyCol3     | G.f.: 3/(1 + 2*sqrt(1-12*x))                                                   |
| 34  | A035929 | Alt-DiagSum      | Number of Dyck n-paths starting U^mD^m (an m-pyramid), followed by a pyramid-f |
| 35  | A039599 | Std-Triangle     | Triangle formed from even-numbered columns of triangle of expansions of powers |
| 36  | A050157 | Std-Acc          | T(n, k) = S(2n, n, k) for 0<=k<=n and n>=0, where S(p, q, r) is the number of  |
| 37  | A050165 | Std-Rev          | Triangle read by rows: T(n,k) = M(2n+1,k,-1), 0 <= k <= n, n >= 0, array M as  |
| 38  | A053698 | Alt-PolyRow3     | a(n) = n^3 + n^2 + n + 1                                                       |
| 39  | A054142 | Std-RevInv       | Triangular array binomial(2*n-k, k), k=0..n, n >= 0                            |
| 40  | A062158 | Std-PolyRow3     | a(n) = n^3 - n^2 + n - 1 = (n-1) * (n^2 + 1)                                   |
| 41  | A062344 | Std-AccRev       | Triangle of binomial(2*n, k) with n >= k                                       |
| 42  | A064062 | Std-NegHalf      | Generalized Catalan numbers C(2; n)                                            |
| 43  | A076035 | Std-PolyCol3     | G.f.: 1/(1-4*x*C) where C = (1/2-1/2*(1-4*x)^(1/2))/x = g.f. for Catalan numbe |
| 44  | A082759 | Inv-InvBinConv   | a(n) = Sum_{k = 0..n} binomial(n,k)*trinomial(n,k), where trinomial(n,k) = tri |
| 45  | A085478 | Std-Inv          | Triangle read by rows: T(n, k) = binomial(n + k, 2*k)                          |
| 46  | A087168 | Inv-PosHalf      | Expansion of (1 + 2*x)/(1 + 3*x + 4*x^2)                                       |
| 47  | A087169 | Inv:Rev-PolyCol3 | Expansion of (1 + 3*x)/(1 + 5*x + 9*x^2)                                       |
| 48  | A089022 | Std-PosHalf      | Number of walks of length 2n on the 3-regular tree beginning and ending at som |
| 49  | A099511 | Inv:Rev-OddSum   | Row sums of triangle A099510, so that a(n) = Sum_{k=0..n} coefficient of z^k i |
| 50  | A108479 | Inv:Rev-EvenSum  | Antidiagonal sums of number triangle A086645                                   |
| 51  | A109961 | Inv-EvenSum      | Expansion of (1-x)^3/(1-4x+5x^2-4x^3+x^4)                                      |
| 52  | A117671 | Inv-CentralO     | a(n) = binomial(3*n+1, n+1)                                                    |
| 53  | A126596 | Std-CentralE     | a(n) = binomial(4*n,n)*(2*n+1)/(3*n+1)                                         |
| 54  | A126984 | Alt-PolyCol3     | Expansion of 1/(1+2*x*c(x)), c(x) the g.f. of Catalan numbers A000108          |
| 55  | A128899 | Alt-Acc          | Riordan array (1,(1-2x-sqrt(1-4x))/(2x))                                       |
| 56  | A138187 | Inv:Rev-TransNat | Hankel transform of binomial(2*n+3, n)                                         |
| 57  | A174687 | Std-BinConv      | Central coefficients T(2n,n) of the Catalan triangle A033184                   |
| 58  | A274115 | Rev-DiagSum      | Number of equivalence classes of Dyck paths of semilength n for the string duu |
| 59  | A296771 | Std-AccSum       | Row sums of A050157                                                            |

* Statistic about DyckPaths:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 59.
	all      A-numbers  : 142.
	missing  sequences  : 59.

[('missing', 59), ('A000012', 9), ('A000108', 8), ('A001700', 6), ('A000984', 6), ('A005408', 5), ('A000027', 5), ('A085478', 4), ('A050165', 4), ('A001519', 4), ('A296771', 3), ('A174687', 3), ('A126596', 3), ('A089022', 3), ('A054142', 3), ('A039599', 3), ('A032443', 3), ('A014107', 3), ('A000588', 3), ('A000384', 3), ('A000344', 3), ('A000245', 3), ('A000007', 3), ('A087168', 2), ('A082759', 2), ('A064062', 2), ('A062344', 2), ('A050157', 2), ('A028387', 2), ('A007854', 2), ('A005809', 2), ('A002378', 2), ('A000957', 2), ('A000579', 2), ('A000531', 2), ('A000447', 2), ('A000332', 2), ('A000217', 2), ('A274115', 1), ('A138187', 1), ('A128899', 1), ('A126984', 1), ('A117671', 1), ('A109961', 1), ('A108479', 1), ('A099511', 1), ('A087169', 1), ('A076035', 1), ('A062158', 1), ('A053698', 1), ('A035929', 1), ('A035610', 1), ('A034839', 1), ('A027849', 1), ('A025174', 1), ('A007583', 1), ('A001835', 1), ('A000958', 1), ('A000346', 1), ('A000079', 1)]

A related webpage is: https://peterluschny.github.io/tabl/DyckPaths.html .
2025/01/10

'''
