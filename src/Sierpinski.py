from functools import cache
from _tabltypes import MakeTriangle

"""Sierpiński's triangle, binomial(n, k) mod 2.

[0]                               1
[1]                              1, 1
[2]                            1, 0, 1
[3]                           1, 1, 1, 1
[4]                         1, 0, 0, 0, 1
[5]                        1, 1, 0, 0, 1, 1
[6]                      1, 0, 1, 0, 1, 0, 1
[7]                     1, 1, 1, 1, 1, 1, 1, 1
[8]                   1, 0, 0, 0, 0, 0, 0, 0, 1
[9]                  1, 1, 0, 0, 0, 0, 0, 0, 1, 1
"""


@cache
def sierpinski(n: int) -> list[int]:
    return [int(not ~n & k) for k in range(n + 1)]


@MakeTriangle(
    sierpinski,
    "Sierpinski",
    ["A047999", "A090971", "A114700", "A143200", "A166282"],
    True,
)
def Sierpinski(n: int, k: int) -> int:
    return sierpinski(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Sierpinski)


''' OEIS

The traits of the Sierpinski triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-CentralE     | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-RowLcm       | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000035 | Std-DiagRow1     | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 5   | A001316 | Std-RowSum       | Gould's sequence: a(n) = Sum_{k=0..n} (binomial(n,k) mod 2); number of odd ent |
| 6   | A001317 | Std-PosHalf      | Sierpinski's triangle (Pascal's triangle mod 2) converted to decimal           |
| 7   | A002487 | Std-DiagSum      | Stern's diatomic series (or Stern-Brocot sequence): a(0) = 0, a(1) = 1; for n  |
| 8   | A002522 | Std-PolyRow2     | a(n) = n^2 + 1                                                                 |
| 9   | A005563 | Inv-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 10  | A005590 | Inv:Rev-DiagSum  | a(0) = 0, a(1) = 1, a(2n) = a(n), a(2n+1) = a(n+1) - a(n)                      |
| 11  | A019590 | Inv:Rev-EvenSum  | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 12  | A047999 | Std-Triangle     | Sierpinski's [Sierpinski's] triangle (or gasket): triangle, read by rows, form |
| 13  | A048298 | Inv-AccSum       | a(n) = n if n=2^i for i >= 0, otherwise a(n) = 0                               |
| 14  | A053698 | Std-PolyRow3     | a(n) = n^3 + n^2 + n + 1                                                       |
| 15  | A060632 | Std-EvenSum      | a(n) = 2^wt(floor(n/2)) (i.e., 2^A000120(floor(n/2)), or A001316(floor(n/2)))  |
| 16  | A062158 | Alt-PolyRow3     | a(n) = n^3 - n^2 + n - 1 = (n-1) * (n^2 + 1)                                   |
| 17  | A063524 | Inv-OddSum       | Characteristic function of 1                                                   |
| 18  | A088560 | Std-BinConv      | Sum of odd entries in row n of Pascal's triangle                               |
| 19  | A100307 | Std-PolyCol3     | Modulo 2 binomial transform of 3^n                                             |
| 20  | A100735 | Inv-PolyCol2     | Inverse modulo 2 binomial transform of 2^n                                     |
| 21  | A100736 | Inv-PolyCol3     | Inverse modulo 2 binomial transform of 3^n                                     |
| 22  | A100744 | Inv-NegHalf      | Inverse modulo 2 binomial transform of (-2)^n                                  |
| 23  | A121262 | Std-DiagRow3     | The characteristic function of the multiples of four                           |
| 24  | A130706 | Inv-AltSum       | a(0) = 1, a(1) = 2, a(n) = 0 for n > 1                                         |
| 25  | A133872 | Std-DiagRow2     | Period 4: repeat [1, 1, 0, 0]                                                  |
| 26  | A152618 | Inv-PolyRow3     | a(n) = (n-1)^2*(n+1)                                                           |
| 27  | A209229 | Std-ColMiddle    | Characteristic function of powers of 2, cf. A000079                            |
| 28  | A261363 | Std-Acc          | Triangle read by rows: partial row sums of Sierpinski's triangle               |
| 29  | A290452 | Inv-Acc          | Triangle formed by reading the triangle of Eulerian numbers (A173018) mod 2    |
| 30  | A335063 | Std-TransNat0    | a(n) = Sum_{k=0..n} (binomial(n,k) mod 2) * k                                  |

* Statistic about Sierpinski:

        Triangles considered: ['Std', 'Alt', 'Inv', 'Inv:Rev'].
        distinct A-numbers  : 30.
        all      A-numbers  : 122.
        missing  sequences  : 42.

[('missing', 42), ('A000012', 17), ('A047999', 14), ('A001316', 10), ('A209229', 8), ('A121262', 8), ('A048298', 8), ('A000035', 6), ('A000007', 6), ('A133872', 5), ('A290452', 4), ('A000027', 4), ('A001317', 3), ('A261363', 2), ('A152618', 2), ('A130706', 2), ('A100744', 2), ('A100736', 2), ('A100735', 2), ('A088560', 2), ('A063524', 2), ('A060632', 2), ('A005563', 2), ('A002522', 2), ('A335063', 1), ('A100307', 1), ('A062158', 1), ('A053698', 1), ('A019590', 1), ('A005590', 1), ('A002487', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Sierpinski.html .
2025/01/10

'''