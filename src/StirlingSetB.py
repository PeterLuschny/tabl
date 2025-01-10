from functools import cache
from _tabltypes import MakeTriangle

"""Stirling set B-type.


[0]     1;
[1]     1,     1;
[2]     3,     4,     1;
[3]    11,    19,     9,     1;
[4]    49,   104,    70,    16,    1;
[5]   257,   641,   550,   190,   25,   1;
[6]  1539,  4380,  4531,  2080,  425,  36,  1;
[7] 10299, 32803, 39515, 22491, 6265, 833, 49, 1;
"""


@cache
def stirlingsetb(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    pow = stirlingsetb(n - 1)
    row = stirlingsetb(n - 1) + [1]

    row[0] += 2 * row[1]

    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]

    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


@MakeTriangle(stirlingsetb, "StirlingSetB", ["A154602"], True)
def StirlingSetB(n: int, k: int) -> int:
    return stirlingsetb(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingSetB)


''' OEIS

The traits of the StirlingSetB triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Alt-AccSum       | Powers of 2: a(n) = 2^n                                                        |
| 5   | A000290 | Std-DiagRow1     | The squares: a(n) = n^2                                                        |
| 6   | A000567 | Rev-PolyRow2     | Octagonal numbers: n*(3*n-2). Also called star numbers                         |
| 7   | A004211 | Std-ColLeft      | Shifts one place left under 2nd-order binomial transform                       |
| 8   | A004213 | Std-NegHalf      | Shifts one place left under 4th-order binomial transform                       |
| 9   | A005408 | Inv-PolyCol2     | The odd numbers: a(n) = 2*n + 1                                                |
| 10  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 11  | A009235 | Alt-PolyCol2     | E.g.f. exp( sinh(x) / exp(x) ) = exp( (1-exp(-2*x))/2 )                        |
| 12  | A010844 | Inv:Rev-NegHalf  | a(n) = 2*n*a(n-1) + 1 with a(0) = 1                                            |
| 13  | A055142 | Inv-RowSum       | Expansion of e.g.f.: exp(x)*sqrt(1-2x)                                         |
| 14  | A055882 | Std-RowSum       | a(n) = 2^n*Bell(n). E.g.f.: exp(exp(2x)-1)                                     |
| 15  | A084262 | Inv-AltSum       | Binomial transform of double factorials                                        |
| 16  | A123968 | Inv-PolyRow2     | a(n) = n^2 - 3                                                                 |
| 17  | A154602 | Std-Triangle     | Exponential Riordan array [exp(sinh(x)*exp(x)), sinh(x)*exp(x)]                |
| 18  | A211012 | Alt-TransSqrs    | Total area of all squares and rectangles after 2^n stages in the toothpick str |
| 19  | A297382 | Inv-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 20  | A308536 | Alt-PolyCol3     | Expansion of e.g.f. exp(1 - exp(2*x))                                          |
| 21  | A308543 | Std-PolyCol3     | Expansion of e.g.f. exp(2*(exp(2*x) - 1))                                      |
| 22  | A353546 | Inv-DiagCol1     | Expansion of e.g.f. -log(1-2*x) * exp(x)/2                                     |

* Statistic about StirlingSetB:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 22.
	all      A-numbers  : 61.
	missing  sequences  : 155.

[('missing', 155), ('A000012', 7), ('A055882', 6), ('A000290', 5), ('A000027', 5), ('A084262', 4), ('A000079', 4), ('A154602', 3), ('A004211', 3), ('A000007', 3), ('A353546', 2), ('A297382', 2), ('A123968', 2), ('A055142', 2), ('A009235', 2), ('A005563', 2), ('A005408', 2), ('A004213', 2), ('A308543', 1), ('A308536', 1), ('A211012', 1), ('A010844', 1), ('A000567', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingSetB.html .
2025/01/10

'''
