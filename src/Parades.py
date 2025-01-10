from functools import cache
from Binomial import binomial
from _tabltypes import MakeTriangle


"""Parades triangle.
  [0] 1;
  [1] 0, 0;
  [2] 0, 1,  0;
  [3] 0, 1,  1,   0;
  [4] 0, 1,  5,   1,   0;
  [5] 0, 1, 13,  13,   1,  0;
  [6] 0, 1, 29,  73,  29,  1, 0;
  [7] 0, 1, 61, 301, 301, 61, 1, 0;
"""

@cache
def A(n: int, k: int) -> int:
    if n == 0: return int(k == 0)
    if k > n: n, k = k, n
    b = binomial(k + 1)
    return k * A(n - 1, k) + sum(b[j + 1] * A(n - 1, k - j)
                             for j in range(1, k + 1))

@cache
def parades(n: int) -> list[int]:
    return [A(n - k, k) for k in range(n + 1)]


@MakeTriangle(parades, "Parades", ["A371761", "A272644"], True)
def Parades(n: int, k: int) -> int:
    return parades(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Parades, short=True)

''' OEIS

The traits of the Parades triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-DiagRow1     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A002378 | Std-PolyRow3     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 5   | A006230 | Std-DiagRow3     | Bitriangular permutations                                                      |
| 6   | A036563 | Std-DiagRow2     | a(n) = 2^n - 3                                                                 |
| 7   | A036968 | Std-AltSum       | Genocchi numbers (of first kind): expansion of 2*x/(exp(x)+1)                  |
| 8   | A048144 | Std-CentralE     | a(n) = Sum_{k=0..n} (k!)^2 * Stirling_2(n,k)^2                                 |
| 9   | A052841 | Std-BinConv      | Expansion of e.g.f.: 1/(exp(x)*(2-exp(x)))                                     |
| 10  | A210657 | Std-InvBinConv   | a(0)=1; thereafter a(n) = -2*Sum_{k=1..n} binomial(2n,2k)*a(n-k)               |
| 11  | A272645 | Std-RowMax       | a(n) = largest term in row n of array in A272644                               |
| 12  | A297195 | Std-RowSum       | Number of bitriangular permutations (row sums of A272644 if that triangle is p |
| 13  | A371761 | Std-Triangle     | Array read by antidiagonals: The number of parades with n girls and k boys tha |

* Statistic about Parades:

	Triangles considered: ['Std', 'Alt'].
	distinct A-numbers  : 13.
	all      A-numbers  : 40.
	missing  sequences  : 42.

[('missing', 42), ('A371761', 4), ('A297195', 4), ('A272645', 4), ('A036563', 4), ('A006230', 4), ('A000012', 4), ('A000007', 4), ('A210657', 2), ('A052841', 2), ('A048144', 2), ('A036968', 2), ('A002378', 2), ('A000027', 2)]

A related webpage is: https://peterluschny.github.io/tabl/Parades.html .
2025/01/10

'''
