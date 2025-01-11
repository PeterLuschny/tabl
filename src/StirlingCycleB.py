from functools import cache
from _tabltypes import MakeTriangle

"""Stirling cycle B-type.

[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     15,     23,      9,     1;
[4]    105,    176,     86,    16,     1;
[5]    945,   1689,    950,   230,    25,   1;
[6]  10395,  19524,  12139,  3480,   505,  36,  1;
[7] 135135, 264207, 177331, 57379, 10045, 973, 49, 1;
"""


@cache
def stirlingcycleb(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = stirlingcycleb(n - 1) + [1]

    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m

    return row


@MakeTriangle(
    stirlingcycleb, "StirlingCycleB", ["A028338", "A039757", "A039758", "A109692"], True
)
def StirlingCycleB(n: int, k: int) -> int:
    return stirlingcycleb(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(StirlingCycleB)


''' OEIS

The traits of the StirlingCycleB triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000165 | Std-RowSum       | Double factorial of even numbers: (2n)!! = 2^n*n!                              |
| 5   | A000290 | Std-DiagRow1     | The squares: a(n) = n^2                                                        |
| 6   | A000567 | Rev-PolyRow2     | Octagonal numbers: n*(3*n-2). Also called star numbers                         |
| 7   | A001147 | Std-ColLeft      | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 8   | A002866 | Std-EvenSum      | a(0) = 1; for n > 0, a(n) = 2^(n-1)*n!                                         |
| 9   | A003462 | Inv-DiagCol1     | a(n) = (3^n - 1)/2                                                             |
| 10  | A004041 | Std-RowMax       | Scaled sums of odd reciprocals: a(n) = (2*n + 1)!!*(Sum_{k=0..n} 1/(2*k + 1))  |
| 11  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 12  | A007405 | Inv-AltSum       | Dowling numbers: e.g.f.: exp(x + (exp(b*x) - 1)/b) with b=2                    |
| 13  | A007696 | Std-NegHalf      | Quartic (or 4-fold) factorial numbers: a(n) = Product_{k = 0..n-1} (4*k + 1)   |
| 14  | A008545 | Std-PosHalf      | Quadruple factorial numbers: Product_{k=0..n-1} (4*k + 3)                      |
| 15  | A016209 | Inv-DiagCol2     | Expansion of 1/((1-x)(1-3x)(1-5x))                                             |
| 16  | A021424 | Inv-DiagCol3     | Expansion of 1/((1-x)(1-3x)(1-5x)(1-7x))                                       |
| 17  | A024196 | Std-DiagRow2     | a(n) = 2nd elementary symmetric function of the first n+1 odd positive integer |
| 18  | A024197 | Std-DiagRow3     | a(n) = 3rd elementary symmetric function of the first n+2 odd positive integer |
| 19  | A028338 | Std-Triangle     | Triangle of coefficients in expansion of (x+1)*(x+3)*...*(x + 2n - 1) in risin |
| 20  | A028339 | Std-DiagCol2     | Coefficient of x^2 in expansion of (x+1)*(x+3)*...*(x+2*n-1)                   |
| 21  | A028340 | Std-DiagCol3     | Coefficient of x^3 in expansion of (x+1)*(x+3)*...*(x+2*n-1)                   |
| 22  | A039755 | Std-Inv          | Triangle of B-analogs of Stirling numbers of the second kind                   |
| 23  | A039756 | Std-RevInv       | Triangle of B-analogs of Stirling numbers of 2nd kind                          |
| 24  | A049308 | Rev-PolyCol3     | Sextuple factorial numbers: Product_{k=0..n-1} (6*k+4)                         |
| 25  | A103220 | Inv-DiagRow2     | a(n) = n*(n+1)*(3*n^2+n-1)/6                                                   |
| 26  | A109692 | Std-Rev          | Triangle of coefficients in expansion of (1+x)*(1+3x)*(1+5x)*(1+7x)*...*(1+(2n |
| 27  | A123968 | Inv-PolyRow2     | a(n) = n^2 - 3                                                                 |
| 28  | A126390 | Inv:Rev-NegHalf  | a(n) = Sum_{i=0..n} 2^i*B(i)*binomial(n,i) where B(n) = Bell numbers A000110(n |
| 29  | A130706 | Alt-PolyCol3     | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 30  | A177145 | Alt-PolyDiag     | Expansion of e.g.f. arcsin(x)                                                  |
| 31  | A197130 | Rev-TransNat0    | Sum of reflection (or absolute) lengths of all elements in the Coxeter group o |
| 32  | A202153 | Rev-DiagSum      | G.f.: Sum_{n>=0} x^n * Product_{k=0..n-1} (1 + (2*k+1)*x)                      |
| 33  | A203159 | Std-TransNat0    | (n-1)-st elementary symmetric function of {2,4,6,8,...,2n}                     |
| 34  | A293318 | Std-CentralE     | a(n) = (2*n)! * [x^(2*n)] (-log(sqrt(1 - 2*x)))^n/(sqrt(1 - 2*x)*n!)           |
| 35  | A297382 | Inv-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 36  | A308645 | Inv-PolyCol2     | Expansion of e.g.f. exp(1 + x - exp(2*x))                                      |
| 37  | A334190 | Inv-RowSum       | a(n) = exp(1/2) * Sum_{k>=0} (2*k + 1)^n / ((-2)^k * k!)                       |
| 38  | A348087 | Inv-CentralO     | a(n) = [x^n] Product_{k=1..n} 1/(1 - (2*k-1) * x)                              |
| 39  | A355165 | Inv-NegHalf      | a(n) = exp(-1/4) * Sum_{k>=0} (4*k + 2)^n / (4^k * k!)                         |
| 40  | A370912 | Std-PolyRow3     | a(n) = n*(n + 2)*(n + 4)                                                       |
| 41  | A374866 | Std-PolyDiag     | Obverse convolution (n)**(3n+2); see Comments                                  |


* Statistic about StirlingCycleB:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 41.
	all      A-numbers  : 118.
	missing  sequences  : 98.

[('missing', 98), ('A000165', 10), ('A002866', 7), ('A001147', 7), ('A000012', 7), ('A004041', 6), ('A000290', 5), ('A000027', 5), ('A109692', 4), ('A039755', 4), ('A007405', 4), ('A293318', 3), ('A039756', 3), ('A028340', 3), ('A028339', 3), ('A028338', 3), ('A024197', 3), ('A024196', 3), ('A008545', 3), ('A000007', 3), ('A334190', 2), ('A308645', 2), ('A297382', 2), ('A123968', 2), ('A103220', 2), ('A021424', 2), ('A016209', 2), ('A007696', 2), ('A005563', 2), ('A003462', 2), ('A374866', 1), ('A370912', 1), ('A355165', 1), ('A348087', 1), ('A203159', 1), ('A202153', 1), ('A197130', 1), ('A177145', 1), ('A130706', 1), ('A126390', 1), ('A049308', 1), ('A000567', 1)]

A related webpage is: https://peterluschny.github.io/tabl/StirlingCycleB.html .
2025/01/11

'''
