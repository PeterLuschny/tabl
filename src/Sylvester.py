from functools import cache
from Binomial import Binomial
from StirlingCycle import StirlingCycle
from _tabltypes import MakeTriangle

"""Sylvester polynomials.

[0] 1;
[1] 0,   2;
[2] 0,   1,    4;
[3] 0,   2,    6,    8;
[4] 0,   6,   19,   24,   16;
[5] 0,  24,   80,  110,   80,   32;
[6] 0, 120,  418,  615,  500,  240,  64;
[7] 0, 720, 2604, 4046, 3570, 1960, 672, 128;
"""


@cache
def sylvester(n: int) -> list[int]:
    def s(n: int, k: int) -> int:
        return sum(
            Binomial(n, k - j) * StirlingCycle(n - k + j, j) for j in range(k + 1)
        )

    return [s(n, k) for k in range(n + 1)]


@MakeTriangle(sylvester, "Sylvester", ["A341101"], False)
def Sylvester(n: int, k: int) -> int:
    return sylvester(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Sylvester)


''' OEIS

The traits of the Sylvester triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000027 | Std-AltSum       | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000034 | Std-RowGcd       | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 4   | A000079 | Std-ColRight     | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000142 | Std-DiagCol1     | Factorial numbers: n! = 1*2*3*4*...*n (order of symmetric group S_n, number of |
| 6   | A000522 | Std-RowSum       | Total number of ordered k-tuples (k=0..n) of distinct elements from an n-eleme |
| 7   | A001788 | Std-DiagRow1     | a(n) = n*(n+1)*2^(n-2)                                                         |
| 8   | A005843 | Std-PolyRow1     | The nonnegative even numbers: a(n) = 2n                                        |
| 9   | A007466 | Alt-PolyCol2     | Exponential-convolution of natural numbers with themselves                     |
| 10  | A007742 | Std-PolyRow2     | a(n) = n*(4*n+1)                                                               |
| 11  | A033991 | Alt-PolyRow2     | a(n) = n*(4*n-1)                                                               |
| 12  | A038155 | Rev-OddSum       | a(n) = (n!/2) * Sum_{k=0..n-2} 1/k!                                            |
| 13  | A055642 | Rev-PolyRow1     | Number of digits in the decimal expansion of n                                 |
| 14  | A081923 | Std-PolyCol2     | Expansion of exp(2x)/(1-x)^2                                                   |
| 15  | A084262 | Std-PosHalf      | Binomial transform of double factorials                                        |
| 16  | A137882 | Rev-PolyRow3     | Number of (directed) Hamiltonian paths in the n-ladder graph                   |
| 17  | A277373 | Alt-PolyDiag     | a(n) = Sum_{k=0..n} binomial(n,n-k)*n^(n-k)*n!/(n-k)!                          |
| 18  | A295183 | Std-PolyDiag     | a(n) = n! * [x^n] exp(n*x)/(1 - x)^n                                           |
| 19  | A341101 | Std-Triangle     | T(n, k) = Sum_{j=0..k} binomial(n, k - j)*Stirling1(n - k + j, j)*(-1)^(n-k).  |
| 20  | A346258 | Rev-PolyCol3     | E.g.f.: exp(x) / (1 - 3 * x)^(1/3)                                             |

* Statistic about Sylvester:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 20.
	all      A-numbers  : 44.
	missing  sequences  : 81.

[('missing', 81), ('A000522', 6), ('A000027', 4), ('A084262', 3), ('A001788', 3), ('A000142', 3), ('A000079', 3), ('A000034', 3), ('A000007', 3), ('A341101', 2), ('A081923', 2), ('A007466', 2), ('A005843', 2), ('A346258', 1), ('A295183', 1), ('A277373', 1), ('A137882', 1), ('A055642', 1), ('A038155', 1), ('A033991', 1), ('A007742', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Sylvester.html .
2025/01/10

'''
