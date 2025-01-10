from functools import cache
from _tabltypes import MakeTriangle

"""Partition numbers (Euler's table), see also A026820, A000041.

[0] 1
[1] 0, 1
[2] 0, 1, 1
[3] 0, 1, 1, 1
[4] 0, 1, 2, 1, 1
[5] 0, 1, 2, 2, 1, 1
[6] 0, 1, 3, 3, 2, 1, 1
[7] 0, 1, 3, 4, 3, 2, 1, 1
[8] 0, 1, 4, 5, 5, 3, 2, 1, 1
[9] 0, 1, 4, 7, 6, 5, 3, 2, 1, 1
"""


@cache
def part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0

    return part(n - 1, k - 1) + part(n - k, k)


@cache
def partnumexact(n: int) -> list[int]:
    return [part(n, k) for k in range(n + 1)]


@MakeTriangle(partnumexact, "Partition", ["A072233", "A008284", "A058398"], True)
def PartnumExact(n: int, k: int) -> int:
    return partnumexact(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(PartnumExact)

''' OEIS

The traits of the Partition triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000009 | Rev-DiagSum      | Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into distin |
| 3   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 4   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 5   | A000041 | Std-RowSum       | a(n) is the number of partitions of n (the partition numbers)                  |
| 6   | A000065 | Std-CentralO     | -1 + number of partitions of n                                                 |
| 7   | A000700 | Std-AltSum       | Expansion of Product_{k>=0} (1 + x^(2k+1)); number of partitions of n into dis |
| 8   | A000701 | Rev-OddSum       | One half of number of non-self-conjugate partitions; also half of number of as |
| 9   | A001399 | Std-DiagCol3     | a(n) is the number of partitions of n into at most 3 parts; also partitions of |
| 10  | A002061 | Rev-PolyRow3     | Central polygonal numbers: a(n) = n^2 - n + 1                                  |
| 11  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 12  | A002569 | Std-RowMax       | Max_{k=0..n} { Number of partitions of n into exactly k parts }                |
| 13  | A002865 | Std-DiagSum      | Number of partitions of n that do not contain 1 as a part                      |
| 14  | A004526 | Std-DiagCol2     | Nonnegative integers repeated, floor(n/2)                                      |
| 15  | A006128 | Std-TransNat0    | Total number of parts in all partitions of n. Also, sum of largest parts of al |
| 16  | A007706 | Inv-CentralO     | a(n) = 1 + coefficient of x^n in Product_{k>=1} (1-x^k) (essentially the expan |
| 17  | A010701 | Std-DiagRow3     | Constant sequence: the all 3's sequence                                        |
| 18  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 19  | A027187 | Std-EvenSum      | Number of partitions of n into an even number of parts                         |
| 20  | A027193 | Std-OddSum       | Number of partitions of n into an odd number of parts                          |
| 21  | A027444 | Std-PolyRow3     | a(n) = n^3 + n^2 + n                                                           |
| 22  | A039800 | Inv-DiagCol1     | Column 1 of Inverse partition triangle A038498                                 |
| 23  | A039801 | Inv-DiagCol2     | Column 2 of Inverse partition triangle A038498                                 |
| 24  | A039802 | Inv-DiagCol3     | Column 3 of Inverse partition triangle A038498                                 |
| 25  | A039966 | Inv-DiagRow3     | a(0) = 1; thereafter a(3n+2) = 0, a(3n) = a(3n+1) = a(n)                       |
| 26  | A045991 | Inv-PolyRow3     | a(n) = n^3 - n^2                                                               |
| 27  | A046682 | Rev-EvenSum      | Number of cycle types of conjugacy classes of all even permutations of n eleme |
| 28  | A055642 | Std-DiagRow2     | Number of digits in the decimal expansion of n                                 |
| 29  | A058397 | Std-AccSum       | Row sums of partition triangle A026820                                         |
| 30  | A064284 | Std-RowGcd       | Number of times n appears in Recaman's sequence A005132                        |
| 31  | A066639 | Std-ColMiddle    | Number of partitions of n with floor(n/2) parts                                |
| 32  | A069778 | Alt-PolyRow3     | q-factorial numbers 3!_q                                                       |
| 33  | A070933 | Std-PolyCol2     | Expansion of Product_{k>=1} 1/(1 - 2*t^k)                                      |
| 34  | A071109 | Alt-PolyCol2     | Expansion of Product_{k>=1} 1/(1+2*x^k)                                        |
| 35  | A072233 | Std-Triangle     | Square array T(n,k) read by antidiagonals giving number of ways to distribute  |
| 36  | A075900 | Std-PosHalf      | Expansion of g.f.: Product_{n>0} 1/(1 - 2^(n-1)*x^n)                           |
| 37  | A093694 | Std-AccRevSum    | Number of one-element transitions from the partitions of n to the partitions o |
| 38  | A098545 | Std-BinConv      | Row sums of A098546                                                            |
| 39  | A119620 | Rev-ColMiddle    | Number of partitions of floor(3n/2) into n parts each from {1,2,...,n}         |
| 40  | A124577 | Std-PolyDiag     | Define p(alpha) to be the number of H-conjugacy classes where H is a Young sub |
| 41  | A196087 | Rev-TransNat0    | Sum of all parts minus the total numbers of parts of all partitions of n       |
| 42  | A242587 | Std-PolyCol3     | The number of conjugacy classes of n X n matrices over F_3                     |
| 43  | A261582 | Alt-PolyCol3     | Expansion of Product_{k>=1} 1/(1 + 3*x^k)                                      |
| 44  | A272901 | Inv-ColMiddle    | Smallest k>=1 such that A067128(n+k) - A067128(n) is in A067128 or a(n)=0 if t |
| 45  | A292134 | Alt-PolyDiag     | Main diagonal of A292133                                                       |
| 46  | A296010 | Std-TransSqrs    | Sum of the squares of the number of parts in all partitions of n               |
| 47  | A298596 | Alt-DiagSum      | Expansion of Product_{k>=2} 1/(1 + x^k)                                        |
| 48  | A300579 | Rev-PolyCol3     | Expansion of Product_{k>=1} 1/(1 - 3^(k-1)*x^k)                                |
| 49  | A338697 | Rev-PolyDiag     | a(n) = [x^n] Product_{k>=1} 1 / (1 - n^(k-1)*x^k)                              |
| 50  | A352402 | Std-NegHalf      | Expansion of Product_{k>=1} 1 / (1 + 2^(k-1)*x^k)                              |

* Statistic about Partition:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 50.
	all      A-numbers  : 122.
	missing  sequences  : 89.

[('missing', 89), ('A000012', 17), ('A000041', 10), ('A000027', 6), ('A000007', 5), ('A098545', 3), ('A093694', 3), ('A075900', 3), ('A072233', 3), ('A064284', 3), ('A058397', 3), ('A055642', 3), ('A010701', 3), ('A004526', 3), ('A002569', 3), ('A002378', 3), ('A001399', 3), ('A000700', 3), ('A352402', 2), ('A071109', 2), ('A070933', 2), ('A066639', 2), ('A039966', 2), ('A039802', 2), ('A039801', 2), ('A039800', 2), ('A027193', 2), ('A027187', 2), ('A019590', 2), ('A000065', 2), ('A338697', 1), ('A300579', 1), ('A298596', 1), ('A296010', 1), ('A292134', 1), ('A272901', 1), ('A261582', 1), ('A242587', 1), ('A196087', 1), ('A124577', 1), ('A119620', 1), ('A069778', 1), ('A046682', 1), ('A045991', 1), ('A027444', 1), ('A007706', 1), ('A006128', 1), ('A002865', 1), ('A002061', 1), ('A000701', 1), ('A000009', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Partition.html .
2025/01/10

'''
