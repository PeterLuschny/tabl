from functools import cache
from _tabltypes import MakeTriangle

"""Motzkin generating function triangle.

[0]    1;
[1]    1,    1;
[2]    2,    2,    1;
[3]    4,    5,    3,    1;
[4]    9,   12,    9,    4,   1;
[5]   21,   30,   25,   14,   5,   1;
[6]   51,   76,   69,   44,  20,   6,   1;
[7]  127,  196,  189,  133,  70,  27,   7,  1;
[8]  323,  512,  518,  392, 230, 104,  35,  8, 1;
[9]  835, 1353, 1422, 1140, 726, 369, 147, 44, 9, 1.
"""


@cache
def motzkin(n: int) -> list[int]:
    if n == 0:
        return [1]

    def r(k: int) -> int:
        return motzkin(n - 1)[k] if k >= 0 and k < n else 0

    row = motzkin(n - 1) + [1]
    for k in range(0, n):
        row[k] += r(k - 1) + r(k + 1)
    return row


@MakeTriangle(motzkin, "Motzkin", ["A064189", "A026300", "A009766"], True)
def Motzkin(n: int, k: int) -> int:
    return motzkin(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Motzkin)

''' OEIS

The traits of the Motzkin triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000096 | Std-DiagRow2     | a(n) = n*(n+3)/2                                                               |
| 4   | A000217 | Inv-DiagRow2     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 5   | A000244 | Std-AccRevSum    | Powers of 3: a(n) = 3^n                                                        |
| 6   | A000297 | Std-DiagRow3     | a(n) = (n+1)*(n+3)*(n+8)/6                                                     |
| 7   | A001006 | Std-ColLeft      | Motzkin numbers: number of ways of drawing any number of nonintersecting chord |
| 8   | A001844 | Rev-PolyRow2     | Centered square numbers: a(n) = 2*n*(n+1)+1. Sums of two consecutive squares.  |
| 9   | A001906 | Inv:Rev-NegHalf  | F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)              |
| 10  | A002026 | Std-DiagCol1     | Generalized ballot numbers (first differences of Motzkin numbers)              |
| 11  | A002426 | Std-EvenSum      | Central trinomial coefficients: largest coefficient of (1 + x + x^2)^n         |
| 12  | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 13  | A004524 | Inv-OddSum       | Three even followed by one odd                                                 |
| 14  | A004525 | Inv-EvenSum      | One even followed by three odd                                                 |
| 15  | A005043 | Std-AltSum       | Riordan numbers: a(n) = (n-1)*(2*a(n-1) + 3*a(n-2))/(n+1)                      |
| 16  | A005322 | Std-DiagCol2     | Column of Motzkin triangle                                                     |
| 17  | A005323 | Std-DiagCol3     | Column of Motzkin triangle                                                     |
| 18  | A005408 | Inv:Rev-PolyRow2 | The odd numbers: a(n) = 2*n + 1                                                |
| 19  | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 20  | A005586 | Inv-DiagRow3     | a(n) = n*(n+4)*(n+5)/6                                                         |
| 21  | A005717 | Std-OddSum       | Construct triangle in which n-th row is obtained by expanding (1 + x + x^2)^n  |
| 22  | A005773 | Std-RowSum       | Number of directed animals of size n (or directed n-ominoes in standard positi |
| 23  | A025170 | Inv:Rev-PolyCol3 | Expansion of g.f.: 1/(1 + 2*x + 9*x^2)                                         |
| 24  | A026300 | Std-Rev          | Motzkin triangle, T, read by rows; T(0,0) = T(1,0) = T(1,1) = 1; for n >= 2, T |
| 25  | A026302 | Std-CentralE     | a(n) = number of (s(0), s(1), ..., s(n)) such that s(i) is a nonnegative integ |
| 26  | A026307 | Rev-ColMiddle    | a(n) = T(n,[ n/2 ]), where T is the array in A026300                           |
| 27  | A026741 | Inv-AccSum       | a(n) = n if n odd, n/2 if n even                                               |
| 28  | A026938 | Std-RowMax       | Greatest number in row of n array T given by A026300                           |
| 29  | A026943 | Std-AccSum       | a(n) = Sum_{k=0..n} (k+1) * T(n, k), with T given by A026300                   |
| 30  | A029578 | Inv:Rev-TransNat | The natural numbers interleaved with the even numbers                          |
| 31  | A049072 | Inv-NegHalf      | Expansion of 1/(1 - 3*x + 4*x^2)                                               |
| 32  | A057979 | Inv-AccRevSum    | a(n) = 1 for even n and (n-1)/2 for odd n                                      |
| 33  | A059738 | Std-PolyCol2     | Binomial transform of A054341 and inverse binomial transform of A049027        |
| 34  | A064189 | Std-Triangle     | Triangle T(n,k), 0 <= k <= n, read by rows, defined by: T(0,0)=1, T(n,k)=0 if  |
| 35  | A089372 | Alt-DiagSum      | Number of Motzkin paths of length n with no peaks at level 1                   |
| 36  | A094792 | Alt-PolyRow3     | a(n) = (1/n!)*A001565(n)                                                       |
| 37  | A106489 | Std-AntiDiag     | Triangle read by rows: T(n,k) is the number of short bushes with n edges and h |
| 38  | A106853 | Inv-PosHalf      | Expansion of 1/(1 - x + 4*x^2)                                                 |
| 39  | A128504 | Inv-DiagCol2     | Row sums of array A128503 (second convolution of Chebyshev's S(n,x) = U(n,x/2) |
| 40  | A129889 | Inv-TransSqrs    | Write down n, then n*(n+1)                                                     |
| 41  | A132199 | Inv-RowGcd       | Rowland's prime-generating sequence: first differences of A106108              |
| 42  | A135859 | Std-PolyRow3     | Row sums of triangle A135858                                                   |
| 43  | A142150 | Inv-TransNat0    | The nonnegative integers interleaved with 0's                                  |
| 44  | A187306 | Alt-TransNat0    | Alternating sum of Motzkin numbers A001006                                     |
| 45  | A191519 | Rev-DiagSum      | Number of dispersed Dyck paths of semilength n (i.e., Motzkin paths of length  |
| 46  | A242135 | Inv-PolyRow3     | a(n) = n^3 - 2*n                                                               |
| 47  | A249303 | Inv-AntiDiag     | Triangular array:  row n gives the coefficients of the polynomial p(n,x) defin |
| 48  | A327871 | Rev-CentralO     | Number of self-avoiding planar walks starting at (0,0), ending at (n,n), remai |
| 49  | A330792 | Std-Poly         | T(n, k) = P(n-k, k) where P(n, x) = Sum_{k=0..n} A064189(n, k)*x^k. Triangle r |
| 50  | A330796 | Std-TransNat0    | a(n) = Sum_{k=0..n} binomial(n, k)*(2^k - binomial(k, floor(k/2)))             |
| 51  | A330799 | Std-PosHalf      | Evaluation of the Motzkin polynomials at 1/2 and normalized with 2^n           |
| 52  | A330800 | Std-NegHalf      | Evaluation of the Motzkin polynomials at -1/2 and normalized with (-2)^n       |
| 53  | A344394 | Std-ColMiddle    | a(n) = binomial(n, n/2 - 1/4 + (-1)^n/4)*hypergeom([-n/4 - 1/8 + (-1)^n/8, -n/ |
| 54  | A344396 | Std-CentralO     | a(n) = binomial(2*n + 1, n)*hypergeom([-(n + 1)/2, -n/2], [n + 2], 4)          |
| 55  | A344502 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n, k)^2 * hypergeom([(k-n)/2, (k-n+1)/2], [k+2],  |
| 56  | A344503 | Std-InvBinConv   | a(n) = Sum_{k=0..n} (-1)^(n-k)*binomial(n, k)^2*hypergeom([(k-n)/2, (k-n+1)/2] |
| 57  | A344504 | Std-TransSqrs    | a(n) = [x^n] ((x - 1)/sqrt(4/(x + 1) - 3) + x + 1)/(2*x*(3*x - 1))             |
| 58  | A344506 | Std-PolyCol3     | a(n) = [x^n] 2 / (1 - 7*x + sqrt(1 - 2*x - 3*x^2))                             |
| 59  | A344507 | Alt-PolyCol2     | a(n) = [x^n] 2/(3*x + sqrt((1 - 3*x)*(x + 1)) + 1)                             |
| 60  | A350383 | Inv-CentralO     | a(n) = [x^n] 1/(1 + x + x^2)^n                                                 |

* Statistic about Motzkin:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 60.
	all      A-numbers  : 137.
	missing  sequences  : 56.

[('missing', 56), ('A000027', 13), ('A000012', 7), ('A005773', 6), ('A026300', 4), ('A005043', 4), ('A344503', 3), ('A344502', 3), ('A330799', 3), ('A064189', 3), ('A057979', 3), ('A026943', 3), ('A026938', 3), ('A026741', 3), ('A026302', 3), ('A005323', 3), ('A005322', 3), ('A002026', 3), ('A001006', 3), ('A000297', 3), ('A000244', 3), ('A000096', 3), ('A344507', 2), ('A344396', 2), ('A344394', 2), ('A330800', 2), ('A132199', 2), ('A128504', 2), ('A106853', 2), ('A106489', 2), ('A059738', 2), ('A005717', 2), ('A005586', 2), ('A004525', 2), ('A004524', 2), ('A002522', 2), ('A002426', 2), ('A000217', 2), ('A350383', 1), ('A344506', 1), ('A344504', 1), ('A330796', 1), ('A330792', 1), ('A327871', 1), ('A249303', 1), ('A242135', 1), ('A191519', 1), ('A187306', 1), ('A142150', 1), ('A135859', 1), ('A129889', 1), ('A094792', 1), ('A089372', 1), ('A049072', 1), ('A029578', 1), ('A026307', 1), ('A025170', 1), ('A005563', 1), ('A005408', 1), ('A001906', 1), ('A001844', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Motzkin.html .
2025/01/10

'''
