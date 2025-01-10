from functools import cache
from _tabltypes import MakeTriangle

"""Monotone words (binomial(-n, k)).

[0] [1]
[1] [1, 1]
[2] [1, 2,  3]
[3] [1, 3,  6,  10]
[4] [1, 4, 10,  20,  35]
[5] [1, 5, 15,  35,  70,  126]
[6] [1, 6, 21,  56, 126,  252,  462]
[7] [1, 7, 28,  84, 210,  462,  924, 1716]
[8] [1, 8, 36, 120, 330,  792, 1716, 3432,  6435]
[9] [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310]
"""


@cache
def monotone(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = (row[k] * (n + k)) // (k + 1)
    return row


@MakeTriangle(monotone, "Monotone", ["A059481", "A027555"], True)
def Monotone(n: int, k: int) -> int:
    return monotone(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Monotone)

''' OEIS

The traits of the Monotone triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-InvBinConv   | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000096 | Rev:Inv-DiagRow2 | a(n) = n*(n+3)/2                                                               |
| 5   | A000217 | Std-DiagCol2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000292 | Std-DiagCol3     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 7   | A000984 | Std-RowSum       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2                 |
| 8   | A001612 | Rev:Inv-AbsSum   | a(n) = a(n-1) + a(n-2) - 1 for n > 1, a(0)=3, a(1)=2                           |
| 9   | A001700 | Std-AccSum       | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 10  | A001791 | Std-DiagRow3     | a(n) = binomial coefficient C(2n, n-1)                                         |
| 11  | A002003 | Std-BinConv      | a(n) = 2 * Sum_{k=0..n-1} binomial(n-1, k)*binomial(n+k, k)                    |
| 12  | A005581 | Rev:Inv-DiagRow3 | a(n) = (n-1)*n*(n+4)/6                                                         |
| 13  | A005809 | Std-CentralO     | a(n) = binomial(3n,n)                                                          |
| 14  | A008865 | Rev:Inv-PolyRow2 | a(n) = n^2 - 2                                                                 |
| 15  | A014300 | Rev-OddSum       | Number of nodes of odd outdegree in all ordered rooted (planar) trees with n e |
| 16  | A014963 | Rev:Inv-RowGcd   | Exponential of Mangoldt function M(n): a(n) = 1 unless n is a prime or prime p |
| 17  | A026641 | Rev-EvenSum      | Number of nodes of even outdegree (including leaves) in all ordered trees with |
| 18  | A032443 | Std-PosHalf      | a(n) = Sum_{i=0..n} binomial(2*n, i)                                           |
| 19  | A034275 | Std-AccRevSum    | a(n)=f(n,n-2) where f is given in A034261                                      |
| 20  | A037952 | Alt-DiagSum      | a(n) = binomial(n, floor((n-1)/2))                                             |
| 21  | A046899 | Std-Acc          | Triangle in which n-th row is {binomial(n+k,k), k=0..n}, n >= 0                |
| 22  | A055642 | Rev:Inv-CentralE | Number of digits in the decimal expansion of n                                 |
| 23  | A056105 | Alt-PolyRow2     | First spoke of a hexagonal spiral                                              |
| 24  | A056109 | Std-PolyRow2     | Fifth spoke of a hexagonal spiral                                              |
| 25  | A059100 | Rev-PolyRow2     | a(n) = n^2 + 2                                                                 |
| 26  | A059481 | Std-Triangle     | Triangle read by rows. T(n, k) = binomial(n+k-1, k) for 0 <= k <= n            |
| 27  | A072547 | Std-AltSum       | Main diagonal of the array in which first column and row are filled alternativ |
| 28  | A080924 | Rev:Inv-NegHalf  | Jacobsthal gap sequence                                                        |
| 29  | A081204 | Std-ColMiddle    | Staircase on Pascal's triangle                                                 |
| 30  | A098600 | Rev:Inv-AltSum   | a(n) = Fibonacci(n-1) + Fibonacci(n+1) - (-1)^n                                |
| 31  | A098601 | Rev:Inv-DiagSum  | Expansion of (1+2*x)/((1+x)*(1-x^2-x^3))                                       |
| 32  | A100100 | Std-Rev          | Triangle T(n,k) = binomial(2*n-k-1, n-k) read by rows                          |
| 33  | A100192 | Rev-PolyCol3     | a(n) = Sum_{k=0..n} binomial(2n,n+k)*2^k                                       |
| 34  | A100217 | Rev-DiagSum      | Diagonal sums of a binomial number triangle                                    |
| 35  | A100218 | Std-InvRev       | Riordan array ((1-2*x)/(1-x), (1-x))                                           |
| 36  | A100219 | Rev:Inv-RowSum   | Expansion of (1-2*x)/((1-x)*(1-x+x^2))                                         |
| 37  | A110609 | Std-TransNat0    | a(n) = n * C(2*n,n-1)                                                          |
| 38  | A110665 | Rev:Inv-TransNat | Sequence is {a(0,n)}, where a(m,0)=0, a(m,n) = a(m-1,n)+a(m,n-1) and a(0,n) is |
| 39  | A110666 | Rev:Inv-AccRevSu | Sequence is {a(1,n)}, where a(m,n) is defined at sequence A110665              |
| 40  | A116406 | Std-DiagSum      | Expansion of ((1 + x - 2x^2) + (1+x)*sqrt(1-4x^2))/(2(1-4x^2))                 |
| 41  | A117671 | Rev-CentralO     | a(n) = binomial(3*n+1, n+1)                                                    |
| 42  | A119259 | Std-PolyCol2     | Central terms of the triangle in A119258                                       |
| 43  | A130706 | Rev:Inv-DiagCol1 | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 44  | A165817 | Std-CentralE     | Number of compositions (= ordered integer partitions) of n into 2n parts       |
| 45  | A201635 | Alt-Acc          | Triangle formed by T(n,n) = (-1)^n*Sum_{j=0..n} C(-n,j), T(n,k) = Sum_{j=0..k} |
| 46  | A220101 | Rev-TransSqrs    | Number of ordered set partitions of {1,...,n} into n-1 blocks avoiding the pat |
| 47  | A267602 | Rev:Inv-ColMiddl | Number of unlabeled, connected graphs on n vertices that are prime and have no |
| 48  | A277282 | Rev:Inv-RowMax   | Max coefficient in n-th Lucas polynomial                                       |
| 49  | A293574 | Rev-PolyDiag     | a(n) = Sum_{k=0..n} n^(n-k)*binomial(n+k-1,k)                                  |
| 50  | A321632 | Rev:Inv-PolyCol2 | Expansion of e.g.f. (1 + sin(x))/exp(x)                                        |
| 51  | A366043 | Rev:Inv-OddSum   | Number of circular binary sequences of length n with an odd number of 0's and  |
| 52  | A367548 | Std-NegHalf      | a(n) = Sum_{k = 0..n} binomial(-n, k) * 2^(n - k)                              |
| 53  | A368488 | Std-PolyDiag     | a(n) = Sum_{k=0..n} n^k * binomial(k+n-1,k)                                    |

* Statistic about Monotone:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv'].
	distinct A-numbers  : 53.
	all      A-numbers  : 120.
	missing  sequences  : 52.

[('missing', 52), ('A001700', 12), ('A000984', 9), ('A000027', 8), ('A000012', 8), ('A100218', 4), ('A100100', 4), ('A001791', 4), ('A000007', 4), ('A165817', 3), ('A072547', 3), ('A059481', 3), ('A034275', 3), ('A032443', 3), ('A002003', 3), ('A000292', 3), ('A000217', 3), ('A367548', 2), ('A119259', 2), ('A110666', 2), ('A081204', 2), ('A046899', 2), ('A005809', 2), ('A368488', 1), ('A366043', 1), ('A321632', 1), ('A293574', 1), ('A277282', 1), ('A267602', 1), ('A220101', 1), ('A201635', 1), ('A130706', 1), ('A117671', 1), ('A116406', 1), ('A110665', 1), ('A110609', 1), ('A100219', 1), ('A100217', 1), ('A100192', 1), ('A098601', 1), ('A098600', 1), ('A080924', 1), ('A059100', 1), ('A056109', 1), ('A056105', 1), ('A055642', 1), ('A037952', 1), ('A026641', 1), ('A014963', 1), ('A014300', 1), ('A008865', 1), ('A005581', 1), ('A001612', 1), ('A000096', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Monotone.html .
2025/01/10

'''
