from functools import cache
from _tabltypes import MakeTriangle

"""FiboLucas polynomials, m = 2.
  [ 0] [1]
  [ 1] [1, 2]
  [ 2] [1, 2, 1]
  [ 3] [1, 2, 2, 2]
  [ 4] [1, 2, 3, 4, 1]
  [ 5] [1, 2, 4, 6, 3, 2]
  [ 6] [1, 2, 5, 8, 6, 6, 1]
  [ 7] [1, 2, 6, 10, 10, 12, 4, 2]
  [ 8] [1, 2, 7, 12, 15, 20, 10, 8, 1]
  [ 9] [1, 2, 8, 14, 21, 30, 20, 20, 5, 2]
  [10] [1, 2, 9, 16, 28, 42, 35, 40, 15, 10, 1]

# @cache
def T(n: int, k: int) -> int:
    if k > n: return 0
    if k < 2: return k + 1
    return T(n - 1, k) + T(n - 2, k - 2)
"""

@cache
def fibolucas(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 2]
    if n == 2: return [1, 2, 1]

    rowA = fibolucas(n - 2)
    row  = fibolucas(n - 1) + [1 + n % 2]
    row[2] += 1

    for k in range(3, n):
        row[k] += rowA[k - 2]

    return row


@MakeTriangle(fibolucas, "FiboLucas", ["A374439"], True)
def FiboLucas(n: int, k: int) -> int:
    return fibolucas(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucas)

    for n in range(11): print(fibolucas(n))

    """
    * Statistic about FiboLucas:
    The number of ...
        all      hashes    is 169.
        distinct hashes    is 106.
        core     triangles is 1.
        distinct types     is 4.
        missing  sequences is 99.
        all      A-numbers is 70.
        distinct A-numbers is 36.

The traits of the FiboLucas triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                   |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000027 | Std-DiagCol2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 2   | A000034 | Std-ColRight     | Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)                                  |
| 3   | A000204 | Std-RowSum       | Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) = 1, L(2) = |
| 4   | A000244 | Rev:Inv-PosHalf  | Powers of 3: a(n) = 3^n                                   |
| 5   | A005408 | Std-PolyRow1     | The odd numbers: a(n) = 2*n + 1                                   |
| 6   | A007395 | Std-DiagCol1     | Constant sequence: the all 2's sequence                                        |
| 7   | A020725 | Rev-PolyRow1     | Integers >= 2. a(n) = n+1                                   |
| 8   | A022958 | Rev:Inv-PolyRow1 | a(n) = 2 - n                                   |
| 9   | A022959 | Rev:Inv-DiagRow2 | 3-n                                   |
| 10  | A023607 | Rev-TransNat0    | a(n) = n * Fibonacci(n+1)                                   |
| 11  | A039834 | Std-AltSum       | a(n+2) = -a(n+1) + a(n) (signed Fibonacci numbers) with a(-2) = a(-1) = 1; or  |
| 12  | A048654 | Std-PosHalf      | a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4                                       |
| 13  | A060546 | Rev-DiagSum      | a(n) = 2^ceiling(n/2)                                   |
| 14  | A060747 | Alt-PolyRow1     | a(n) = 2*n - 1                                   |
| 15  | A086990 | Rev:Inv-OddSum   | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 16  | A087113 | Std-DiagCol3     | Essentially a duplicate of A005843                                   |
| 17  | A090412 | Rev:Inv-ColLeft  | A Chebyshev transform of 2^n                                   |
| 18  | A108300 | Rev-PolyCol3     | a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5                              |
| 19  | A124038 | Std-Rev          | Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If |
| 20  | A162395 | Std-PolyRow2     | a(n) = -(-1)^n * n^2                                   |
| 21  | A174902 | Alt-PolyRow2     | Denominator of 1 - 1/n^2, using 0 at the pole where n=0                        |
| 22  | A176981 | Std-NegHalf      | Expansion of 1+(1-2*x)/(-1+2*x+x^2)                                   |
| 23  | B000045 | Std-EvenSum      | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 24  | B001629 | Alt-AccSum       | Self-convolution of Fibonacci numbers                                          |
| 25  | B005843 | Rev:Inv-DiagRow3 | The nonnegative even numbers: a(n) = 2n                                        |
| 26  | B006131 | Std-PolyCol2     | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 27  | B006355 | Std-OddSum       | Number of binary vectors of length n containing no singletons                  |
| 28  | B029578 | Std-DiagRow1     | The natural numbers interleaved with the even numbers                          |
| 29  | B059100 | Rev:Inv-PolyRow2 | a(n) = n^2 + 2                                   |
| 30  | B086990 | Rev:Inv-RowSum   | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 31  | B131259 | Std-DiagRow2     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 32  | B133585 | Rev-EvenSum      | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 33  | B133586 | Rev-OddSum       | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 34  | B188377 | Rev-PolyRow3     | a(n) = n^3 - 4n^2 + 6n - 2                                   |
| 35  | B318829 | Std-RowGcd       | a(n) = A063994(n) / A049559(n) = (1/gcd(n-1, phi(n))) * Product_{primes p divi |
| 36  | B374439 | Std-Triangle     |                                   |

6 A000204 ['Std-RowSum', 'Std-AbsSum', 'Alt-AltSum', 'Alt-AbsSum', 'Rev-RowSum', 'Rev-AbsSum']
          Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) = 1, L(2) = 3
          1 3 4 7 11 18 29 47 76 123 199 322 521 843 1364 2207 3571 5778 9349 15127 24476 39603 64079 103682
4 A007395 ['Std-DiagCol1', 'Alt-DiagCol1', 'Rev-DiagRow1', 'Rev:Inv-DiagRow1']
          Constant sequence: the all 2's sequence
          2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
4 A124038 ['Std-Rev', 'Alt-Rev', 'Rev-Triangle', 'Rev:Inv-Inv']
          Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If[ n == m &&
          1 2 1 1 2 1 2 2 2 1 1 4 3 2 1 2 3 6 4 2 1 1 6 6 8 5 2 1 2 4 12 10 10 6 2 1 1 8 10 20 15 12 7 2 1 2
3 A000027 ['Std-DiagCol2', 'Alt-DiagCol2', 'Rev-DiagRow2']
          The positive integers. Also called the natural numbers, the whole numbers or the counting
          1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
3 A000034 ['Std-ColRight', 'Alt-ColRight', 'Rev-ColLeft']
          Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)
          1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
3 A039834 ['Std-AltSum', 'Alt-RowSum', 'Rev-AltSum']
          a(n+2) = -a(n+1) + a(n) (signed Fibonacci numbers) with a(-2) = a(-1) = 1; or Fibonacci nu
          1 -1 0 -1 -1 -2 -3 -5 -8 -13 -21 -34 -55 -89 -144 -233 -377 -610 -987 -1597 -2584 -4181 -6765
3 A048654 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4
          1 4 9 22 53 128 309 746 1801 4348 10497 25342 61181 147704 356589 860882 2078353 5017588 12113529
3 A087113 ['Std-DiagCol3', 'Alt-DiagCol3', 'Rev-DiagRow3']
          Essentially a duplicate of A005843
          2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68
3 B029578 ['Std-DiagRow1', 'Alt-DiagRow1', 'Rev-DiagCol1']
          The natural numbers interleaved with the even numbers
          1 2 2 4 3 6 4 8 5 10 6 12 7 14 8 16 9 18 10 20 11 22 12 24 13 26 14 28 15 30 16 32 17 34 18 36 19
3 B131259 ['Std-DiagRow2', 'Alt-DiagRow2', 'Rev-DiagCol2']
          a(2n)=A000217(n), a(2n+1)=-2*A000217(n)
          1 2 3 6 6 12 10 20 15 30 21 42 28 56 36 72 45 90 55 110 66 132 78 156 91 182 105 210 120 240 136
3 B318829 ['Std-RowGcd', 'Alt-RowGcd', 'Rev-RowGcd']
          a(n) = A063994(n) / A049559(n) = (1/gcd(n-1, phi(n))) * Product_{primes p dividing n} gcd(
          1 2 2 2 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
3 B374439 ['Std-Triangle', 'Alt-Triangle', 'Rev:Inv-RevInv']
          1 1 2 1 2 1 1 2 2 2 1 2 3 4 1 1 2 4 6 3 2 1 2 5 8 6 6 1 1 2 6 10 10 12 4 2 1 2 7 12 15 20 10 8 1 1
2 A162395 ['Std-PolyRow2', 'Rev-PolyRow2']
          a(n) = -(-1)^n * n^2
          1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784
2 A176981 ['Std-NegHalf', 'Alt-PosHalf']
          Expansion of 1+(1-2*x)/(-1+2*x+x^2)
          1 0 1 -2 5 -12 29 -70 169 -408 985 -2378 5741 -13860 33461 -80782 195025 -470832 1136689 -2744210
2 B000045 ['Std-EvenSum', 'Alt-EvenSum']
          Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1
          1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
2 B006131 ['Std-PolyCol2', 'Rev-PosHalf']
          a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1
          1 5 9 29 65 181 441 1165 2929 7589 19305 49661 126881 325525 833049 2135149 5467345 14007941
2 B006355 ['Std-OddSum', 'Alt-OddSum']
          Number of binary vectors of length n containing no singletons
          0 2 2 4 6 10 16 26 42 68 110 178 288 466 754 1220 1974 3194 5168 8362 13530 21892 35422 57314 92736
1 A000244 ['Rev:Inv-PosHalf']
          Powers of 3: a(n) = 3^n
          1 -3 9 -27 81 -243 729 -2187 6561 -19683 59049 -177147 531441 -1594323 4782969 -14348907 43046721
1 A005408 ['Std-PolyRow1']
          The odd numbers: a(n) = 2*n + 1
          1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69
1 A020725 ['Rev-PolyRow1']
          Integers >= 2. a(n) = n+1
          2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
1 A022958 ['Rev:Inv-PolyRow1']
          a(n) = 2 - n
          -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
1 A022959 ['Rev:Inv-DiagRow2']
          3-n
          3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25
1 A023607 ['Rev-TransNat0']
          a(n) = n * Fibonacci(n+1)
          0 1 4 9 20 40 78 147 272 495 890 1584 2796 4901 8540 14805 25552 43928 75258 128535 218920 371931
1 A060546 ['Rev-DiagSum']
          a(n) = 2^ceiling(n/2)
          1 2 2 4 4 8 8 16 16 32 32 64 64 128 128 256 256 512 512 1024 1024 2048 2048 4096 4096 8192 8192
1 A060747 ['Alt-PolyRow1']
          a(n) = 2*n - 1
          1 -1 -3 -5 -7 -9 -11 -13 -15 -17 -19 -21 -23 -25 -27 -29 -31 -33 -35 -37 -39 -41 -43 -45 -47 -49
1 A086990 ['Rev:Inv-OddSum']
          Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x
          0 1 -2 3 -4 6 -10 15 -20 30 -52 78 -96 144 -282 423 -420 630 -1660 2490 -1304 1956 -11332 16998
1 A090412 ['Rev:Inv-ColLeft']
          A Chebyshev transform of 2^n
          1 -2 3 -4 6 -10 15 -20 30 -52 78 -96 144 -282 423 -420 630 -1660 2490 -1304 1956 -11332 16998 3896
1 A108300 ['Rev-PolyCol3']
          a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5
          1 5 16 53 175 578 1909 6305 20824 68777 227155 750242 2477881 8183885 27029536 89272493 294847015
1 A174902 ['Alt-PolyRow2']
          Denominator of 1 - 1/n^2, using 0 at the pole where n=0
          1 0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729
1 B001629 ['Alt-AccSum']
          Self-convolution of Fibonacci numbers
          1 0 0 0 -1 -2 -5 -10 -20 -38 -71 -130 -235 -420 -744 -1308 -2285 -3970 -6865 -11822 -20284 -34690
1 B005843 ['Rev:Inv-DiagRow3']
          The nonnegative even numbers: a(n) = 2n
          -4 -2 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64
1 B059100 ['Rev:Inv-PolyRow2']
          a(n) = n^2 + 2
          3 2 3 6 11 18 27 38 51 66 83 102 123 146 171 198 227 258 291 326 363 402 443 486 531 578 627 678
1 B086990 ['Rev:Inv-RowSum']
          Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x
          1 -1 2 -3 4 -6 10 -15 20 -30 52 -78 96 -144 282 -423 420 -630 1660 -2490 1304 -1956 11332 -16998
1 B133585 ['Rev-EvenSum']
          Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )
          1 2 2 4 5 10 13 26 34 68 89 178 233 466 610 1220 1597 3194 4181 8362 10946 21892 28657 57314 75025
1 B133586 ['Rev-OddSum']
          Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )
          0 1 2 3 6 8 16 21 42 55 110 144 288 377 754 987 1974 2584 5168 6765 13530 17711 35422 46368 92736
"""