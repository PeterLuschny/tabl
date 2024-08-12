from functools import cache
from FiboLucas import fibolucas
from _tabltypes import MakeTriangle

"""FiboLucasRev polynomials, m = 2.

| [1] |
| [2, 1] |
| [1, 2, 1] |
| [2, 2, 2, 1] |
| [1, 4, 3, 2, 1] |
| [2, 3, 6, 4, 2, 1] |
| [1, 6, 6, 8, 5, 2, 1] |
| [2, 4, 12, 10, 10, 6, 2, 1] |

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""

@cache
def fibolucasrev(n: int) -> list[int]:
    if n == 0: return [1]
    return list(reversed(fibolucas(n)))


@MakeTriangle(fibolucasrev, "FiboLucasRev", ["A124038"], True)
def FiboLucasRev(n: int, k: int) -> int:
    return fibolucasrev(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucasRev)

    """
    * Statistic about FiboLucasRev:
The number of ...
        all      hashes    is 204.
        distinct hashes    is 117.
        core     triangles is 1.
        distinct types     is 5.
        missing  sequences is 136.
        all      A-numbers is 68.
        distinct A-numbers is 34.

The traits of the FiboLucasRev triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000034 | Std-DiagCol1     | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 2   | A001477 | Std-DiagRow2     | The nonnegative integers                                |
| 3   | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                |
| 4   | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                |
| 5   | A005843 | Std-DiagRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 6   | A006131 | Std-PosHalf      | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 7   | A056105 | Inv:Rev-PolyRow3 | First spoke of a hexagonal spiral                                |
| 8   | A060747 | Inv:Rev-PolyRow2 | a(n) = 2*n - 1                                |
| 9   | A067998 | Alt-PolyRow2     | a(n) = n^2 - 2*n                                |
| 10  | A090412 | Inv-DiagCol1     | A Chebyshev transform of 2^n                                |
| 11  | A133494 | Inv-PosHalf      | Diagonal of the array of iterated differences of A047848                       |
| 12  | A162395 | Rev-PolyRow3     | a(n) = -(-1)^n * n^2                                |
| 13  | A198834 | Rev-OddSum       | Number of sequences of n coin flips that win on the last flip, if the sequence |
| 14  | A324969 | Rev-EvenSum      | Number of unlabeled rooted identity trees with n vertices whose non-leaf termi |
| 15  | B000032 | Std-RowSum       | Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1       |
| 16  | B000045 | Std-AltSum       | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 17  | B001629 | Alt-TransNat0    | Self-convolution of Fibonacci numbers                                |
| 18  | B005843 | Inv-DiagRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 19  | B011379 | Alt-PolyRow3     | a(n) = n^2*(n+1)                                |
| 20  | B016116 | Std-DiagSum      | a(n) = 2^floor(n/2)                                |
| 21  | B022958 | Inv-DiagRow2     | a(n) = 2 - n                                |
| 22  | B029578 | Std-DiagCol2     | The natural numbers interleaved with the even numbers                          |
| 23  | B029907 | Alt-AccRevSum    | a(n+1) = a(n) + a(n-1) + Fibonacci(n), with a(0) = 0 and a(1) = 1              |
| 24  | B045991 | Std-PolyRow3     | a(n) = n^3 - n^2                                |
| 25  | B052542 | Alt-PolyCol2     | a(n) = 2*a(n-1) + a(n-2), with a(0) = 1, a(1) = 2, a(2) = 4                    |
| 26  | B055642 | Std-DiagRow1     | Number of digits in the decimal expansion of n                                 |
| 27  | B086990 | Inv-RowSum       | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 28  | B112053 | Alt-DiagSum      | a(n) = A112046(2n) - A112046(2n-1) = A112048(n) - A112047(n)                   |
| 29  | B131259 | Std-DiagCol3     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 30  | B133585 | Std-OddSum       | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 31  | B133586 | Std-EvenSum      | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 32  | B152163 | Rev-AltSum       | a(n) = a(n-1)+a(n-2), n>1 ; a(0)=1, a(1)=-1                                    |
| 33  | B280560 | Alt-DiagRow1     | a(n) = (-1)^n * 2 if n!=0, with a(0) = 1                                       |
| 34  | B343643 | Inv-DiagRow1     | Z-coordinate of points following the 3D square spiral defined in A343640       |

6 A001477 ['Std-DiagRow2', 'Std-PolyRow1', 'Alt-DiagRow2', 'Alt-PolyRow1', 'Rev-DiagCol2', 'Inv-PolyRow1']
          The nonnegative integers
          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
6 B000032 ['Std-RowSum', 'Std-AbsSum', 'Alt-AltSum', 'Alt-AbsSum', 'Rev-RowSum', 'Rev-AbsSum']
          Lucas numbers beginning at 2: L(n) = L(n-1) + L(n-2), L(0) = 2, L(1) = 1
          1 1 3 4 7 11 18 29 47 76 123 199 322 521 843 1364 2207 3571 5778 9349 15127 24476 39603 64079
3 A000034 ['Std-DiagCol1', 'Alt-DiagCol1', 'Rev-DiagRow1']
          Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)
          1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
3 A005843 ['Std-DiagRow3', 'Alt-DiagRow3', 'Rev-DiagCol3']
          The nonnegative even numbers: a(n) = 2n
          0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68
3 A006131 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1
          1 1 5 9 29 65 181 441 1165 2929 7589 19305 49661 126881 325525 833049 2135149 5467345 14007941
3 B029578 ['Std-DiagCol2', 'Alt-DiagCol2', 'Rev-DiagRow2']
          The natural numbers interleaved with the even numbers
          1 2 2 4 3 6 4 8 5 10 6 12 7 14 8 16 9 18 10 20 11 22 12 24 13 26 14 28 15 30 16 32 17 34 18 36 19
3 B086990 ['Inv-RowSum', 'Inv-EvenSum', 'Inv:Rev-RowSum']
          Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x
          1 1 -1 2 -3 4 -6 10 -15 20 -30 52 -78 96 -144 282 -423 420 -630 1660 -2490 1304 -1956 11332 -16998
3 B131259 ['Std-DiagCol3', 'Alt-DiagCol3', 'Rev-DiagRow3']
          a(2n)=A000217(n), a(2n+1)=-2*A000217(n)
          1 2 3 6 6 12 10 20 15 30 21 42 28 56 36 72 45 90 55 110 66 132 78 156 91 182 105 210 120 240 136
2 A067998 ['Alt-PolyRow2', 'Inv-PolyRow2']
          a(n) = n^2 - 2*n
          0 -1 0 3 8 15 24 35 48 63 80 99 120 143 168 195 224 255 288 323 360 399 440 483 528 575 624 675 728
2 A090412 ['Inv-DiagCol1', 'Inv:Rev-DiagRow1']
          A Chebyshev transform of 2^n
          1 -2 3 -4 6 -10 15 -20 30 -52 78 -96 144 -282 423 -420 630 -1660 2490 -1304 1956 -11332 16998 3896
2 A133494 ['Inv-PosHalf', 'Inv:Rev-PolyCol2']
          Diagonal of the array of iterated differences of A047848
          1 1 -3 9 -27 81 -243 729 -2187 6561 -19683 59049 -177147 531441 -1594323 4782969 -14348907 43046721
2 B000045 ['Std-AltSum', 'Alt-RowSum']
          Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1
          1 -1 -1 0 -1 1 -2 3 -5 8 -13 21 -34 55 -89 144 -233 377 -610 987 -1597 2584 -4181 6765 -10946 17711
2 B005843 ['Inv-DiagRow3', 'Inv:Rev-DiagCol3']
          The nonnegative even numbers: a(n) = 2n
          0 -4 -2 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62
2 B022958 ['Inv-DiagRow2', 'Inv:Rev-DiagCol2']
          a(n) = 2 - n
          0 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24
2 B029907 ['Alt-AccRevSum', 'Alt-TransNat1']
          a(n+1) = a(n) + a(n-1) + Fibonacci(n), with a(0) = 0 and a(1) = 1
          1 -2 -1 0 -1 2 -4 8 -15 28 -51 92 -164 290 -509 888 -1541 2662 -4580 7852 -13419 22868 -38871 65920
2 B052542 ['Alt-PolyCol2', 'Rev-NegHalf']
          a(n) = 2*a(n-1) + a(n-2), with a(0) = 1, a(1) = 2, a(2) = 4
          1 -2 0 -2 4 -10 24 -58 140 -338 816 -1970 4756 -11482 27720 -66922 161564 -390050 941664 -2273378
2 B055642 ['Std-DiagRow1', 'Rev-DiagCol1']
          Number of digits in the decimal expansion of n
          0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 B133585 ['Std-OddSum', 'Alt-OddSum']
          Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )
          0 1 2 2 4 5 10 13 26 34 68 89 178 233 466 610 1220 1597 3194 4181 8362 10946 21892 28657 57314
2 B133586 ['Std-EvenSum', 'Alt-EvenSum']
          Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )
          1 0 1 2 3 6 8 16 21 42 55 110 144 288 377 754 987 1974 2584 5168 6765 13530 17711 35422 46368 92736
2 B343643 ['Inv-DiagRow1', 'Inv:Rev-DiagCol1']
          Z-coordinate of points following the 3D square spiral defined in A343640
          0 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2
1 A005408 ['Rev-PolyRow2']
          The odd numbers: a(n) = 2*n + 1
          1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69
1 A005563 ['Std-PolyRow2']
          a(n) = n*(n+2) = (n+1)^2 - 1
          0 3 8 15 24 35 48 63 80 99 120 143 168 195 224 255 288 323 360 399 440 483 528 575 624 675 728 783
1 A056105 ['Inv:Rev-PolyRow3']
          First spoke of a hexagonal spiral
          1 2 9 22 41 66 97 134 177 226 281 342 409 482 561 646 737 834 937 1046 1161 1282 1409 1542 1681
1 A060747 ['Inv:Rev-PolyRow2']
          a(n) = 2*n - 1
          1 -1 -3 -5 -7 -9 -11 -13 -15 -17 -19 -21 -23 -25 -27 -29 -31 -33 -35 -37 -39 -41 -43 -45 -47 -49
1 A162395 ['Rev-PolyRow3']
1 A324969 ['Rev-EvenSum']
          Number of unlabeled rooted identity trees with n vertices whose non-leaf terminal subtrees
          1 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
1 B001629 ['Alt-TransNat0']
          Self-convolution of Fibonacci numbers
          0 -1 0 0 0 1 -2 5 -10 20 -38 71 -130 235 -420 744 -1308 2285 -3970 6865 -11822 20284 -34690 59155
1 B011379 ['Alt-PolyRow3']
          a(n) = n^2*(n+1)
          0 0 -2 -12 -36 -80 -150 -252 -392 -576 -810 -1100 -1452 -1872 -2366 -2940 -3600 -4352 -5202 -6156
1 B016116 ['Std-DiagSum']
          a(n) = 2^floor(n/2)
          1 0 1 2 2 4 4 8 8 16 16 32 32 64 64 128 128 256 256 512 512 1024 1024 2048 2048 4096 4096 8192 8192
1 B045991 ['Std-PolyRow3']
          a(n) = n^3 - n^2
          0 4 18 48 100 180 294 448 648 900 1210 1584 2028 2548 3150 3840 4624 5508 6498 7600 8820 10164
1 B112053 ['Alt-DiagSum']
          a(n) = A112046(2n) - A112046(2n-1) = A112048(n) - A112047(n)
          1 0 -1 -2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 B152163 ['Rev-AltSum']
          a(n) = a(n-1)+a(n-2), n>1 ; a(0)=1, a(1)=-1
          1 1 -1 0 -1 -1 -2 -3 -5 -8 -13 -21 -34 -55 -89 -144 -233 -377 -610 -987 -1597 -2584 -4181 -6765
    """