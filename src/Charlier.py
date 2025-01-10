from functools import cache
from _tabltypes import MakeTriangle

"""Coefficients of Charlier polynomials.

[0] [1]
[1] [1, -1]
[2] [1, -3, 1]
[3] [1, -6, 8, -1]
[4] [1, -10, 29, -24, 1]
[5] [1, -15, 75, -145, 89, -1]
[6] [1, -21, 160, -545, 814, -415, 1]
[7] [1, -28, 301, -1575, 4179, -5243, 2372, -1]
[8] [1, -36, 518, -3836, 15659, -34860, 38618, -16072, 1]
"""


@cache
def charlier(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, -1]

    a = charlier(n - 1)
    b = [0] + charlier(n - 2)
    c = charlier(n - 1) + [(-1) ** n]

    for k in range(1, n):
        c[k] = a[k] - n * a[k - 1] - (n - 1) * b[k - 1]

    return c


@MakeTriangle(charlier, "Charlier", ["A046716", "A094816"], True)
def Charlier(n: int, k: int) -> int:
    return charlier(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Charlier)

''' OEIS

The traits of the Charlier triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Rev:Inv-AltSum   | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColLeft      | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-RowSum       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000110 | Rev:Inv-ColLeft  | Bell or exponential numbers: number of ways to partition a set of n labeled el |
| 5   | A000217 | Std-DiagCol1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000522 | Std-AltSum       | Total number of ordered k-tuples (k=0..n) of distinct elements from an n-eleme |
| 7   | A001339 | Std-NegHalf      | a(n) = Sum_{k=0..n} (k+1)! binomial(n,k)                                       |
| 8   | A001861 | Rev:Inv-RowSum   | Expansion of e.g.f. exp(2*(exp(x) - 1))                                        |
| 9   | A002104 | Std-DiagRow1     | Logarithmic numbers                                                            |
| 10  | A002378 | Rev:Inv-PolyRow2 | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 11  | A003128 | Rev:Inv-DiagCol2 | Number of driving-point impedances of an n-terminal network                    |
| 12  | A004211 | Rev:Inv-NegHalf  | Shifts one place left under 2nd-order binomial transform                       |
| 13  | A005493 | Rev:Inv-DiagCol1 | 2-Bell numbers: a(n) = number of partitions of [n+1] with a distinguished bloc |
| 14  | A009132 | Rev-EvenSum      | Expansion of e.g.f. cosh(log(1+x))/exp(x)                                      |
| 15  | A009578 | Rev-OddSum       | E.g.f. sinh(log(1+x))/exp(x). Unsigned sequence gives degrees of (finite by ni |
| 16  | A009940 | Rev-PolyDiag     | a(n) = n!*L_{n}(1), where L_{n}(x) is the n-th Laguerre polynomial             |
| 17  | A027710 | Rev:Inv-PolyCol2 | Number of ways of placing n labeled balls into n unlabeled (but 3-colored) box |
| 18  | A028387 | Std-PosHalf      | a(n) = n + (n+1)^2                                                             |
| 19  | A028557 | Inv-PolyRow2     | a(n) = n*(n+5)                                                                 |
| 20  | A033445 | Rev:Inv-PolyRow3 | a(n) = (n - 1)*(n^2 + n - 1)                                                   |
| 21  | A035009 | Rev:Inv-EvenSum  | STIRLING transform of [1,1,2,4,8,16,32,...]                                    |
| 22  | A035051 | Rev:Inv-PolyDiag | Number of labeled rooted connected graphs where every block is a complete grap |
| 23  | A046716 | Std-Triangle     | Coefficients of a special case of Poisson-Charlier polynomials                 |
| 24  | A049020 | Std-InvRev       | Triangle of numbers a(n,k), 0 <= k <= n: number of set partitions of {1,2,..., |
| 25  | A078944 | Rev:Inv-PolyCol3 | First column of A078939, the fourth power of lower triangular matrix A056857   |
| 26  | A081367 | Alt-PolyCol2     | E.g.f.: exp(2*x)/sqrt(1-2*x)                                                   |
| 27  | A090809 | Rev:Inv-DiagRow2 | Coefficient of the irreducible character of S_m indexed by (m-2n+2,2n-2) in th |
| 28  | A094816 | Std-Rev          | Triangle read by rows: T(n,k) are the coefficients of Charlier polynomials: A0 |
| 29  | A094822 | Alt-PolyCol3     | E.g.f.: exp(3x)/(1-3x)^(1/3)                                                   |
| 30  | A174965 | Std-RowGcd       | Length of the n-th run of consecutive terms in A000961                         |
| 31  | A245109 | Rev:Inv-CentralE | G.f.: Sum_{n>=0} exp(-(1 + n^2*x)) * (1 + n^2*x)^n / n!                        |
| 32  | A253667 | Rev-Poly         | Square array read by ascending antidiagonals, T(n, k) = k!*[x^k](exp(-x) *sum( |
| 33  | A290312 | Std-DiagCol2     | Third diagonal sequence of the Sheffer triangle A094816 (special Charlier)     |
| 34  | A290313 | Std-DiagCol3     | Fourth diagonal sequence of the Sheffer triangle A094816 (special Charlier)    |
| 35  | A343560 | Inv:Rev-PolyRow2 | a(n) = (n-1)*(4*n+1)                                                           |
| 36  | A346842 | Rev:Inv-DiagCol3 | E.g.f.: exp(exp(x) - 1) * (exp(x) - 1)^3 / 3!                                  |

* Statistic about Charlier:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 36.
	all      A-numbers  : 94.
	missing  sequences  : 168.

[('missing', 168), ('A000012', 10), ('A000027', 9), ('A028387', 6), ('A000522', 6), ('A094816', 5), ('A002104', 5), ('A049020', 4), ('A046716', 4), ('A035009', 4), ('A000217', 4), ('A290313', 3), ('A290312', 3), ('A174965', 3), ('A000007', 3), ('A081367', 2), ('A001861', 2), ('A001339', 2), ('A346842', 1), ('A343560', 1), ('A253667', 1), ('A245109', 1), ('A094822', 1), ('A090809', 1), ('A078944', 1), ('A035051', 1), ('A033445', 1), ('A028557', 1), ('A027710', 1), ('A009940', 1), ('A009578', 1), ('A009132', 1), ('A005493', 1), ('A004211', 1), ('A003128', 1), ('A002378', 1), ('A000110', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Charlier.html .
2025/01/10

'''
