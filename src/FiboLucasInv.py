from functools import cache
from FiboLucas import FiboLucas
from _tabltypes import MakeTriangle

"""FiboLucasInv polynomials.

  [0] [  1]
  [1] [ -2,   1]
  [2] [  3,  -2,   1]
  [3] [ -4,   2,  -2,   1]
  [4] [  6,  -2,   1,  -2,   1]
  [5] [-10,   5,   0,   0,  -2,  1]
  [6] [ 15, -10,   5,   2,  -1, -2,  1]
  [7] [-20,  10, -12,   6,   4, -2, -2,  1]
  [8] [ 30,  -8,   4, -16,   8,  6, -3, -2,  1]
  [9] [-52,  26,   8,  -4, -22, 11,  8, -4, -2, 1]

"""

# TODO needs optimation!
@cache
def fibolucasinv(n: int) -> list[int]:
    return FiboLucas.invrev(n+1)[-1]


@MakeTriangle(fibolucasinv, "FiboLucasInv", ["A375025"], True)
def FiboLucasInv(n: int, k: int) -> int:
    return fibolucasinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest
    TablTest(FiboLucasInv, short=True)


"""

* Statistic about FiboLucasInv:
The number of ...
        all      hashes    is 211.
        distinct hashes    is 122.
        core     triangles is 1.
        distinct types     is 5.
        missing  sequences is 135.
        all      A-numbers is 76.
        distinct A-numbers is 38.

The traits of the FiboLucasInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000027 | Inv-DiagRow2     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 5   | A005408 | Inv:Rev-PolyRow1 | The odd numbers: a(n) = 2*n + 1                                                |
| 6   | A007395 | Std-DiagRow1     | Constant sequence: the all 2's sequence                                        |
| 7   | A020725 | Alt-PolyRow1     | Integers >= 2. a(n) = n+1                                                      |
| 8   | A022958 | Std-PolyRow1     | a(n) = 2 - n                                                                   |
| 9   | A022959 | Std-DiagRow2     | 3-n                                                                            |
| 10  | A023607 | Inv-TransNat0    | a(n) = n * Fibonacci(n+1)                                                      |
| 11  | A039834 | Inv-AltSum       | a(n+2) = -a(n+1) + a(n) (signed Fibonacci numbers) with a(-2) = a(-1) = 1; or  |
| 12  | A048654 | Inv-PolyCol2     | a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4                                       |
| 13  | A056105 | Rev-PolyRow2     | First spoke of a hexagonal spiral                                              |
| 14  | A060546 | Inv-DiagSum      | a(n) = 2^ceiling(n/2)                                                          |
| 15  | A060747 | Rev-PolyRow1     | a(n) = 2*n - 1                                                                 |
| 16  | A086990 | Std-OddSum       | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 17  | A087113 | Inv-DiagRow3     | Essentially a duplicate of A005843                                             |
| 18  | A090412 | Std-ColLeft      | A Chebyshev transform of 2^n                                                   |
| 19  | A108300 | Inv-PolyCol3     | a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5                              |
| 20  | A124038 | Std-Inv          | Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If |
| 21  | A162395 | Inv-PolyRow2     | a(n) = -(-1)^n * n^2                                                           |
| 22  | A176981 | Inv:Rev-NegHalf  | Expansion of 1+(1-2*x)/(-1+2*x+x^2)                                            |
| 23  | A183199 | Alt-PolyRow2     | Least integer k such that Floor(k*f(n+1))>k*f(n), where f(n)=(n^2)/(1+n^2)     |
| 24  | B000045 | Inv:Rev-EvenSum  | Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1           |
| 25  | B005843 | Std-DiagRow3     | The nonnegative even numbers: a(n) = 2n                                        |
| 26  | B006131 | Inv-PosHalf      | a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1                                      |
| 27  | B006355 | Inv:Rev-OddSum   | Number of binary vectors of length n containing no singletons                  |
| 28  | B029578 | Inv-DiagCol1     | The natural numbers interleaved with the even numbers                          |
| 29  | B059100 | Std-PolyRow2     | a(n) = n^2 + 2                                                                 |
| 30  | B086990 | Std-RowSum       | Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x                         |
| 31  | B131259 | Inv-DiagCol2     | a(2n)=A000217(n), a(2n+1)=-2*A000217(n)                                        |
| 32  | B133585 | Inv-EvenSum      | Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )                 |
| 33  | B133586 | Inv-OddSum       | Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )                                 |
| 34  | B188377 | Inv-PolyRow3     | a(n) = n^3 - 4n^2 + 6n - 2                                                     |
| 35  | B318829 | Inv-RowGcd       | a(n) = A063994(n) / A049559(n) = (1/gcd(n-1, phi(n))) * Product_{primes p divi |
| 36  | B374439 | Std-RevInv       |                                                                                |
| 37  | B375025 | Std-Triangle     |                                                                                |
| 38  | B375026 | Std-AltSum       |                                                                                |

5 A007395 ['Std-DiagRow1', 'Alt-DiagRow1', 'Rev-DiagCol1', 'Inv-DiagRow1', 'Inv:Rev-DiagCol1']
          Constant sequence: the all 2's sequence
          -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 -2 
4 A000204 ['Inv-RowSum', 'Inv-AbsSum', 'Inv:Rev-RowSum', 'Inv:Rev-AbsSum']
          Lucas numbers (beginning with 1): L(n) = L(n-1) + L(n-2) with L(1) = 1, L(2) = 3
          1 3 4 7 11 18 29 47 76 123 199 322 521 843 1364 2207 3571 5778 9349 15127 24476 39603 64079 103682
4 A124038 ['Std-Inv', 'Rev-InvRev', 'Inv-Triangle', 'Inv:Rev-Rev']
          Determinants of tridiagonal matrices in y with upper diagonal y-2: m(n,n,d)=If[ n == m && 
          1 2 1 1 2 1 2 2 2 1 1 4 3 2 1 2 3 6 4 2 1 1 6 6 8 5 2 1 2 4 12 10 10 6 2 1 1 8 10 20 15 12 7 2 1 2
3 A000244 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          Powers of 3: a(n) = 3^n
          1 -3 9 -27 81 -243 729 -2187 6561 -19683 59049 -177147 531441 -1594323 4782969 -14348907 43046721
3 A022959 ['Std-DiagRow2', 'Alt-DiagRow2', 'Rev-DiagCol2']
          3-n
          3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25
3 A090412 ['Std-ColLeft', 'Alt-ColLeft', 'Rev-ColRight']
          A Chebyshev transform of 2^n
          1 -2 3 -4 6 -10 15 -20 30 -52 78 -96 144 -282 423 -420 630 -1660 2490 -1304 1956 -11332 16998 3896
3 B005843 ['Std-DiagRow3', 'Alt-DiagRow3', 'Rev-DiagCol3']
          The nonnegative even numbers: a(n) = 2n
          -4 -2 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64
3 B086990 ['Std-RowSum', 'Alt-AltSum', 'Rev-RowSum']
          Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x
          1 -1 2 -3 4 -6 10 -15 20 -30 52 -78 96 -144 282 -423 420 -630 1660 -2490 1304 -1956 11332 -16998
3 B374439 ['Std-RevInv', 'Inv-Rev', 'Inv:Rev-Triangle']
          1 1 2 1 2 1 1 2 2 2 1 2 3 4 1 1 2 4 6 3 2 1 2 5 8 6 6 1 1 2 6 10 10 12 4 2 1 2 7 12 15 20 10 8 1 1
3 B375025 ['Std-Triangle', 'Alt-Triangle', 'Inv:Rev-InvRev']
          1 -2 1 3 -2 1 -4 2 -2 1 6 -2 1 -2 1 -10 5 0 0 -2 1 15 -10 5 2 -1 -2 1 -20 10 -12 6 4 -2 -2 1 30 -8
3 B375026 ['Std-AltSum', 'Alt-RowSum', 'Rev-AltSum']
          1 -3 6 -9 12 -18 30 -45 60 -90 156 -234 288 -432 846 -1269 1260 -1890 4980 -7470 3912 -5868 33996
2 A000027 ['Inv-DiagRow2', 'Inv:Rev-DiagCol2']
          The positive integers. Also called the natural numbers, the whole numbers or the counting 
          1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
2 A000034 ['Inv-ColLeft', 'Inv:Rev-ColRight']
          Period 2: repeat [1, 2]; a(n) = 1 + (n mod 2)
          1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
2 A020725 ['Alt-PolyRow1', 'Inv-PolyRow1']
          Integers >= 2. a(n) = n+1
          -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 -21 -22 -23 -24 -25 -26 -27 -28
2 A039834 ['Inv-AltSum', 'Inv:Rev-AltSum']
          a(n+2) = -a(n+1) + a(n) (signed Fibonacci numbers) with a(-2) = a(-1) = 1; or Fibonacci nu
          1 1 0 1 -1 2 -3 5 -8 13 -21 34 -55 89 -144 233 -377 610 -987 1597 -2584 4181 -6765 10946 -17711
2 A048654 ['Inv-PolyCol2', 'Inv:Rev-PosHalf']
          a(n) = 2*a(n-1) + a(n-2); a(0)=1, a(1)=4
          1 4 9 22 53 128 309 746 1801 4348 10497 25342 61181 147704 356589 860882 2078353 5017588 12113529
2 A086990 ['Std-OddSum', 'Alt-OddSum']
          Expansion of (1+4x-sqrt(1+4x^2))/(4+6x) in powers of x
          0 1 -2 3 -4 6 -10 15 -20 30 -52 78 -96 144 -282 423 -420 630 -1660 2490 -1304 1956 -11332 16998
2 A087113 ['Inv-DiagRow3', 'Inv:Rev-DiagCol3']
          Essentially a duplicate of A005843
          2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68
2 A162395 ['Inv-PolyRow2', 'Inv:Rev-PolyRow2']
          a(n) = -(-1)^n * n^2
          1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484 529 576 625 676 729 784
2 B006131 ['Inv-PosHalf', 'Inv:Rev-PolyCol2']
          a(n) = a(n-1) + 4*a(n-2), a(0) = a(1) = 1
          1 5 9 29 65 181 441 1165 2929 7589 19305 49661 126881 325525 833049 2135149 5467345 14007941
2 B029578 ['Inv-DiagCol1', 'Inv:Rev-DiagRow1']
          The natural numbers interleaved with the even numbers
          1 2 2 4 3 6 4 8 5 10 6 12 7 14 8 16 9 18 10 20 11 22 12 24 13 26 14 28 15 30 16 32 17 34 18 36 19
2 B131259 ['Inv-DiagCol2', 'Inv:Rev-DiagRow2']
          a(2n)=A000217(n), a(2n+1)=-2*A000217(n)
          1 2 3 6 6 12 10 20 15 30 21 42 28 56 36 72 45 90 55 110 66 132 78 156 91 182 105 210 120 240 136
2 B318829 ['Inv-RowGcd', 'Inv:Rev-RowGcd']
          a(n) = A063994(n) / A049559(n) = (1/gcd(n-1, phi(n))) * Product_{primes p dividing n} gcd(
          1 2 2 2 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 A005408 ['Inv:Rev-PolyRow1']
          The odd numbers: a(n) = 2*n + 1
          1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69
1 A022958 ['Std-PolyRow1']
          a(n) = 2 - n
          -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
1 A023607 ['Inv-TransNat0']
          a(n) = n * Fibonacci(n+1)
          0 1 4 9 20 40 78 147 272 495 890 1584 2796 4901 8540 14805 25552 43928 75258 128535 218920 371931
1 A056105 ['Rev-PolyRow2']
          First spoke of a hexagonal spiral
          1 2 9 22 41 66 97 134 177 226 281 342 409 482 561 646 737 834 937 1046 1161 1282 1409 1542 1681
1 A060546 ['Inv-DiagSum']
          a(n) = 2^ceiling(n/2)
          1 2 2 4 4 8 8 16 16 32 32 64 64 128 128 256 256 512 512 1024 1024 2048 2048 4096 4096 8192 8192
1 A060747 ['Rev-PolyRow1']
          a(n) = 2*n - 1
          1 -1 -3 -5 -7 -9 -11 -13 -15 -17 -19 -21 -23 -25 -27 -29 -31 -33 -35 -37 -39 -41 -43 -45 -47 -49
1 A108300 ['Inv-PolyCol3']
          a(n+2) = 3*a(n+1) + a(n), with a(0) = 1, a(1) = 5
          1 5 16 53 175 578 1909 6305 20824 68777 227155 750242 2477881 8183885 27029536 89272493 294847015
1 A176981 ['Inv:Rev-NegHalf']
          Expansion of 1+(1-2*x)/(-1+2*x+x^2)
          1 0 1 -2 5 -12 29 -70 169 -408 985 -2378 5741 -13860 33461 -80782 195025 -470832 1136689 -2744210
1 A183199 ['Alt-PolyRow2']
          Least integer k such that Floor(k*f(n+1))>k*f(n), where f(n)=(n^2)/(1+n^2)
          3 6 11 18 27 38 51 66 83 102 123 146 171 198 227 258 291 326 363 402 443 486 531 578 627 678 731
1 B000045 ['Inv:Rev-EvenSum']
          Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1
          1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
1 B006355 ['Inv:Rev-OddSum']
          Number of binary vectors of length n containing no singletons
          0 2 2 4 6 10 16 26 42 68 110 178 288 466 754 1220 1974 3194 5168 8362 13530 21892 35422 57314 92736
1 B059100 ['Std-PolyRow2']
          a(n) = n^2 + 2
          3 2 3 6 11 18 27 38 51 66 83 102 123 146 171 198 227 258 291 326 363 402 443 486 531 578 627 678
1 B133585 ['Inv-EvenSum']
          Expansion of x - x^2*(2*x+1)*(x^2-2) / ( (x^2-x-1)*(x^2+x-1) )
          1 2 2 4 5 10 13 26 34 68 89 178 233 466 610 1220 1597 3194 4181 8362 10946 21892 28657 57314 75025
1 B133586 ['Inv-OddSum']
          Expansion of x*(1+2*x)/( (x^2-x-1)*(x^2+x-1) )
          0 1 2 3 6 8 16 21 42 55 110 144 288 377 754 987 1974 2584 5168 6765 13530 17711 35422 46368 92736
"""