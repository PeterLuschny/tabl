from functools import cache
from _tabltypes import MakeTriangle

"""Little Schroeder triangle.
[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     11,     17,      7,     1;
[4]     45,     76,     40,    10,     1;
[5]    197,    353,    216,    72,    13,     1;
[6]    903,   1688,   1345,   458,   113,    16,    1;
[7]   4279,   8257,   6039,  2745,   829,   163,   19,   1;
[8]  20793,  41128,  31864, 15932,  5558,  1356,  222,  22,  1;
[9] 103049, 207905, 168584, 90776, 35318, 10070, 2066, 290, 25, 1;
"""


@cache
def schroederl(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arow = schroederl(n - 1) + [0]
    row = schroederl(n - 1) + [1]

    row[0] = row[0] + 2 * row[1]
    for k in range(1, n):
        row[k] = arow[k - 1] + 3 * arow[k] + 2 * arow[k + 1]

    return row


@MakeTriangle(schroederl, "SchroederL", ["A172094"], True)
def SchroederL(n: int, k: int) -> int:
    return schroederl(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(SchroederL)

''' OEIS

The traits of the SchroederL triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-AltSum       | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000295 | Inv-DiagCol1     | Eulerian numbers (Euler's triangle: column k=2 of A008292, column k=1 of A1730 |
| 5   | A000567 | Rev-PolyRow2     | Octagonal numbers: n*(3*n-2). Also called star numbers                         |
| 6   | A001003 | Std-ColLeft      | Schroeder's second problem (generalized parentheses); also called super-Catala |
| 7   | A001519 | Inv-DiagSum      | a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1                      |
| 8   | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 9   | A006012 | Inv-AltSum       | a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - 2*a(n-2), n >= 2                         |
| 10  | A006318 | Alt-AccSum       | Large Schroeder numbers (or large Schroeder numbers, or big Schroeder numbers) |
| 11  | A016116 | Inv-PolyCol3     | a(n) = 2^floor(n/2)                                                            |
| 12  | A016777 | Std-DiagRow1     | a(n) = 3*n + 1                                                                 |
| 13  | A045889 | Inv-DiagCol2     | Partial sums of A045618                                                        |
| 14  | A051682 | Inv-DiagRow2     | 11-gonal (or hendecagonal) numbers: a(n) = n*(9*n-7)/2                         |
| 15  | A052984 | Inv:Rev-NegHalf  | a(n) = 5*a(n-1) - 2*a(n-2) for n>1, with a(0) = 1, a(1) = 3                    |
| 16  | A055583 | Inv-DiagCol3     | Seventh column of triangle A055252                                             |
| 17  | A077020 | Inv-PolyCol2     | a(n) is the unique odd positive solution x of 2^n = 7x^2+y^2                   |
| 18  | A091527 | Inv-CentralE     | a(n) = ((3*n)!/n!^2)*(Gamma(1+n/2)/Gamma(1+3n/2))                              |
| 19  | A109980 | Std-RowSum       | Number of Delannoy paths of length n with no (1,1)-steps on the line y=x       |
| 20  | A121463 | Inv-AntiDiag     | Triangle read by rows: T(n,k) is the number of nondecreasing Dyck paths of sem |
| 21  | A123968 | Inv-PolyRow2     | a(n) = n^2 - 3                                                                 |
| 22  | A146559 | Inv-RowSum       | Expansion of (1-x)/(1 - 2*x + 2*x^2)                                           |
| 23  | A172094 | Std-Triangle     | The Riordan square of the little Schroeder numbers A001003                     |
| 24  | A225887 | Std-EvenSum      | a(n) = A212205(2*n + 1)                                                        |
| 25  | A239204 | Std-DiagCol1     | Expansion of ((x-1)*sqrt(x^2-6*x+1)-x^2-4*x+1)/(8*x^3)                         |
| 26  | A244469 | Inv:Rev-CentralO | a(0) = 0, thereafter, a(n) = 2^(2*n-1)*( binomial((3*n-1)/2,n) - binomial(3*n/ |
| 27  | A297382 | Inv-RowGcd       | Denominator of -A023900(n)/2                                                   |
| 28  | A330802 | Std-NegHalf      | Evaluation of the Big-Schroeder polynomials at 1/2 and normalized with 2^n     |
| 29  | A331328 | Std-PosHalf      | Evaluation of the Little-Schroeder polynomials at 1/2 and normalized with 2^n  |
| 30  | A331969 | Std-Inv          | T(n, k) = [x^(n-k)] 1/(((1 - 2*x)^k)*(1 - x)^(k + 1)). Triangle read by rows,  |

* Statistic about SchroederL:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 30.
	all      A-numbers  : 86.
	missing  sequences  : 130.

[('missing', 130), ('A000012', 7), ('A225887', 6), ('A109980', 6), ('A016777', 5), ('A001003', 5), ('A000027', 5), ('A331969', 4), ('A006318', 4), ('A006012', 4), ('A331328', 3), ('A239204', 3), ('A172094', 3), ('A000007', 3), ('A330802', 2), ('A297382', 2), ('A146559', 2), ('A123968', 2), ('A091527', 2), ('A077020', 2), ('A055583', 2), ('A051682', 2), ('A045889', 2), ('A005563', 2), ('A000295', 2), ('A244469', 1), ('A121463', 1), ('A052984', 1), ('A016116', 1), ('A001519', 1), ('A000567', 1)]

A related webpage is: https://peterluschny.github.io/tabl/SchroederL.html .
2025/01/10

'''
