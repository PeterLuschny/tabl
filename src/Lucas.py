from functools import cache
from _tabltypes import MakeTriangle

"""Lucas triangle.
  [0] [2]
  [1] [1, 2]
  [2] [1, 3, 2]
  [3] [1, 4, 5, 2]
  [4] [1, 5, 9, 7, 2]
  [5] [1, 6, 14, 16, 9, 2]
  [6] [1, 7, 20, 30, 25, 11, 2]
  [7] [1, 8, 27, 50, 55, 36, 13, 2]
  [8] [1, 9, 35, 77, 105, 91, 49, 15, 2]
  [9] [1, 10, 44, 112, 182, 196, 140, 64, 17, 2]
"""


@cache
def lucas(n: int) -> list[int]:
    if n == 0: return [2]
    if n == 1: return [1, 2]

    row = lucas(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k - 1]
    return row


@MakeTriangle(lucas, "Lucas", ["A029635", "A029653"])
def Lucas(n: int, k: int) -> int:
    return lucas(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Lucas)


''' OEIS

The traits of the Lucas triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence                |
| 2   | A000027 | Std-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 3   | A000032 | Std-DiagSum      | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 4   | A000038 | Std-NegHalf      | Twice A000007                                                                  |
| 5   | A000045 | Rev-DiagSum      | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 6   | A000096 | Std-DiagCol2     | a(n) = n*(n+3)/2                                                               |
| 7   | A000290 | Std-DiagRow2     | The squares: a(n) = n^2                                                        |
| 8   | A000330 | Std-DiagRow3     | Square pyramidal numbers: a(n) = 0^2 + 1^2 + 2^2 + ... + n^2 = n*(n+1)*(2*n+1) |
| 9   | A000384 | Std-PolyRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                            |
| 10  | A002042 | Std-PolyCol3     | a(n) = 7*4^n                                                                   |
| 11  | A002378 | Rev-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A003946 | Std-PosHalf      | Expansion of (1+x)/(1-3*x)                                                     |
| 13  | A003947 | Rev-PolyCol3     | Expansion of (1+x)/(1-4*x)                                                     |
| 14  | A005030 | Std-PolyCol2     | a(n) = 5*3^n                                                                   |
| 15  | A005408 | Std-DiagRow1     | The odd numbers: a(n) = 2*n + 1                                                |
| 16  | A005581 | Std-DiagCol3     | a(n) = (n-1)*n*(n+4)/6                                                         |
| 17  | A006996 | Alt-TransNat0    | a(n) = C(2n,n) mod 3                                                           |
| 18  | A007283 | Std-RowSum       | a(n) = 3*2^n                                                                   |
| 19  | A010701 | Alt-PolyCol2     | Constant sequence: the all 3's sequence                                        |
| 20  | A011379 | Rev-PolyRow3     | a(n) = n^2*(n+1)                                                               |
| 21  | A014105 | Alt-PolyRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                   |
| 22  | A015237 | Std-PolyRow3     | a(n) = (2*n - 1)*n^2                                                           |
| 23  | A020714 | Alt-PolyCol3     | a(n) = 5 * 2^n                                                                 |
| 24  | A029635 | Std-Triangle     | The (1,2)-Pascal triangle (or Lucas triangle) read by rows                     |
| 25  | A029651 | Std-CentralE     | Central elements of the (1,2)-Pascal triangle A029635                          |
| 26  | A029653 | Std-Rev          | Numbers in (2,1)-Pascal triangle (by row)                                      |
| 27  | A034807 | Std-AntiDiag     | Triangle T(n,k) of coefficients of Lucas (or Cardan) polynomials               |
| 28  | A039964 | Std-AltSum       | Motzkin numbers A001006 read mod 3                                             |
| 29  | A050168 | Std-RowMax       | a(0) = 1; for n > 0, a(n) = binomial(n, floor(n/2)) + binomial(n-1, floor(n/2) |
| 30  | A051924 | Std-CentralO     | a(n) = binomial(2*n,n) - binomial(2*n-2,n-1); or (3n-2)*C(n-1), where C = Cata |
| 31  | A051960 | Rev-CentralO     | a(n) = C(n)*(3n+2) where C(n) = Catalan numbers = A000108                      |
| 32  | A053220 | Rev-TransNat0    | a(n) = (3*n-1) * 2^(n-2)                                                       |
| 33  | A055642 | Std-ColRight     | Number of digits in the decimal expansion of n                                 |
| 34  | A066373 | Std-TransNat0    | a(n) = (3*n-2)*2^(n-3)                                                         |
| 35  | A089658 | Std-TransSqrs    | a(n) = S1(n,1), where S1(n, t) = Sum_{k=0..n} (k^t * Sum_{j=0..k} binomial(n,j |
| 36  | A089945 | Std-PolyDiag     | Main diagonal of array A089944, in which the n-th row is the n-th binomial tra |
| 37  | A098156 | Std-AccRevSum    | Interleave n+1 and 2n+1 and take binomial transform                            |
| 38  | A099721 | Alt-PolyRow3     | a(n) = n^2*(2*n+1)                                                             |
| 39  | A129710 | Rev-AntiDiag     | Triangle read by rows: T(n,k) is the number of Fibonacci binary words of lengt |
| 40  | A176043 | Alt-PolyDiag     | a(n) = (2*n-1)*(n-1)^(n-1)                                                     |
| 41  | A276289 | Rev-TransSqrs    | Expansion of x*(1 + x)/(1 - 2*x)^3                                             |
| 42  | A339252 | Std-AccSum       | a(0) = 1, a(1) = 4, a(2) = 11, and a(n) = 4*a(n-1) - 4*a(n-2) for n >= 3       |
| 43  | A355627 | Alt-AccSum       | a(n) is the number of tuples (t_1, ..., t_k) with a positive integer k and int |
| 44  | A373395 | Rev-PolyDiag     | Number of minimum connected dominating sets in the n-triangular graph          |


* Statistic about Lucas:

	Triangles considered: ['Std', 'Alt', 'Rev'].
	distinct A-numbers  : 44.
	all      A-numbers  : 100.
	missing  sequences  : 19.

[('missing', 19), ('A007283', 12), ('A029651', 6), ('A000012', 6), ('A005408', 5), ('A050168', 4), ('A000027', 4), ('A339252', 3), ('A098156', 3), ('A039964', 3), ('A005581', 3), ('A003946', 3), ('A000330', 3), ('A000290', 3), ('A000096', 3), ('A000038', 3), ('A055642', 2), ('A051924', 2), ('A034807', 2), ('A029653', 2), ('A029635', 2), ('A010701', 2), ('A005030', 2), ('A373395', 1), ('A355627', 1), ('A276289', 1), ('A176043', 1), ('A129710', 1), ('A099721', 1), ('A089945', 1), ('A089658', 1), ('A066373', 1), ('A053220', 1), ('A051960', 1), ('A020714', 1), ('A015237', 1), ('A014105', 1), ('A011379', 1), ('A006996', 1), ('A003947', 1), ('A002378', 1), ('A002042', 1), ('A000384', 1), ('A000045', 1), ('A000032', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Lucas.html .
2025/01/11

'''
