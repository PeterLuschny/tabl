from functools import cache
from _tabltypes import MakeTriangle
from Divisibility import divisibility

"""Moebius Matrix.

[0] 1
[1] 0,  1
[2] 0, -1,  1
[3] 0, -1,  0,  1
[4] 0,  0, -1,  0,  1
[5] 0, -1,  0,  0,  0, 1
[6] 0,  1, -1, -1,  0, 0, 1
[7] 0, -1,  0,  0,  0, 0, 0, 1
[8] 0,  0,  0,  0, -1, 0, 0, 0, 1
[9] 0,  0,  0, -1,  0, 0, 0, 0, 0, 1
"""


@cache
def _moebius(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return -1
    return -sum(_moebius(k) for k, i in enumerate(divisibility(n)[: n - 1]) if i != 0)


@cache
def moebius(n: int) -> list[int]:
    if n == 0:
        return [1]
    r = [0 for _ in range(n + 1)]
    r[n] = 1
    for k in range(1, n):
        if n % k == 0:
            r[k] = _moebius(n // k)
    return r


@MakeTriangle(moebius, "Moebius", ["A363914", "A054525"], True)
def Moebius(n: int, k: int) -> int:
    return moebius(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Moebius)

''' OEIS

The traits of the Moebius triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000005 | Inv-RowSum       | d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n           |
| 2   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 3   | A000010 | Std-AccSum       | Euler totient function phi(n): count numbers <= n and prime to n               |
| 4   | A000012 | Std-Rev          | The simplest sequence of positive numbers: the all 1's sequence                |
| 5   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 6   | A000035 | Rev-ColMiddle    | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 7   | A000203 | Inv-TransNat0    | a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n)          |
| 8   | A001157 | Inv-TransSqrs    | a(n) = sigma_2(n): sum of squares of divisors of n                             |
| 9   | A001227 | Inv-OddSum       | Number of odd divisors of n                                                    |
| 10  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 11  | A002522 | Inv:Rev-PolyRow3 | a(n) = n^2 + 1                                                                 |
| 12  | A005563 | Rev-PolyRow3     | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A007434 | Std-TransSqrs    | Jordan function J_2(n) (a generalization of phi(n))                            |
| 14  | A007503 | Inv-AccRevSum    | Number of subgroups of dihedral group: sigma(n) + d(n)                         |
| 15  | A007531 | Std-PolyRow3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 16  | A008966 | Std-DiagCol1     | a(n) = 1 if n is squarefree, otherwise 0                                       |
| 17  | A019590 | Std-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 18  | A027375 | Std-PolyCol2     | Number of aperiodic binary strings of length n; also number of binary sequence |
| 19  | A032741 | Inv-DiagSum      | a(0) = 0; for n > 0, a(n) = number of proper divisors of n (divisors of n whic |
| 20  | A034262 | Inv-PolyRow3     | a(n) = n^3 + n                                                                 |
| 21  | A034444 | Std-AbsSum       | a(n) is the number of unitary divisors of n (d such that d divides n, gcd(d, n |
| 22  | A036987 | Rev-OddSum       | Fredholm-Rueppel sequence                                                      |
| 23  | A039966 | Std-DiagRow2     | a(0) = 1; thereafter a(3n+2) = 0, a(3n) = a(3n+1) = a(n)                       |
| 24  | A054718 | Std-PolyCol3     | Number of ternary sequences with primitive period n                            |
| 25  | A055895 | Inv-PolyCol2     | Inverse Moebius transform of powers of 2                                       |
| 26  | A056045 | Inv-BinConv      | a(n) = Sum_{d|n} binomial(n,d)                                                 |
| 27  | A063524 | Std-DiagRow1     | Characteristic function of 1                                                   |
| 28  | A066108 | Inv-PolyDiag     | Sum n^d over all divisors of n                                                 |
| 29  | A074854 | Inv-PosHalf      | a(n) = Sum_{d|n} (2^(n-d))                                                     |
| 30  | A079978 | Inv-DiagCol3     | Characteristic function of multiples of three                                  |
| 31  | A081307 | Inv-AccSum       | a(n) = (n+1)*tau(n) - sigma(n)                                                 |
| 32  | A094471 | Inv:Rev-TransNat | a(n) = Sum_{(n - k)|n, 0 <= k <= n} k                                          |
| 33  | A098018 | Std-DiagSum      | a(n) = Sum_{k|n, k>=2} mu(k-1), where mu() is the Moebius function             |
| 34  | A112329 | Inv-AltSum       | Number of divisors of n if n odd, number of divisors of n/4 if n divisible by  |
| 35  | A113704 | Std-Inv          | Triangle read by rows. The indicator function for divisibility                 |
| 36  | A115944 | Rev-EvenSum      | Number of partitions of n into distinct factorials                             |
| 37  | A130779 | Std-AltSum       | a(0)=a(1)=1, a(2)=2, a(n)=0 for n >= 3                                         |
| 38  | A135528 | Std-ColMiddle    | 1, then repeat 1,0                                                             |
| 39  | A154272 | Std-EvenSum      | 1,0,1 followed by 0,0,0,..                                                     |
| 40  | A183063 | Inv-EvenSum      | Number of even divisors of n                                                   |
| 41  | A209229 | Std-CentralO     | Characteristic function of powers of 2, cf. A000079                            |
| 42  | A252764 | Std-PolyDiag     | Number of length n primitive (=aperiodic or period n) n-ary words              |
| 43  | A320111 | Inv:Rev-EvenSum  | Number of divisors d of n that are not of the form 4k+2                        |
| 44  | A325596 | Alt-AccSum       | a(n) = Sum_{d|n} mu(n/d) * (-1)^(d + 1) * d                                    |
| 45  | A338547 | Alt-TransSqrs    | a(n) = n^2 * Sum_{d|n} (-1)^(n/d + 1) * mu(d) / d^2                            |
| 46  | A357051 | Inv:Rev-PolyCol3 | a(n) = Sum_{d|n} 3^(n-d)                                                       |
| 47  | A363733 | Inv-Poly         | Array read by upwards antidiagonals. The family of polynomials generated by th |
| 48  | A363913 | Inv-PolyCol3     | a(n) = Sum_{k=0..n} divides(k, n) * 3^k, where divides(k, n) = 1 if k divides  |
| 49  | A363914 | Std-Triangle     | The Moebius triangle read by rows. Inverse matrix of the divisibility triangle |
| 50  | A363916 | Std-Poly         | Array read by descending antidiagonals. A(n, k) = Sum_{d=0..k} A363914(k, d) * |
| 51  | A365807 | Std-DiagCol3     | a(n) = 1 if A163511(n) is a square, 0 otherwise                                |
| 52  | A367326 | Inv:Rev-TransSqr | a(n) = Sum_{(n - k)|n} k^2                                                     |
| 53  | A367773 | Std-NegHalf      | a(n) = Sum_{k=0..n} A363914(n, k)*(-2)^(n - k)                                 |
| 54  | A367774 | Std-PosHalf      | a(n) = Sum_{k=0..n} A363914(n, k)*2^(n - k)                                    |

* Statistic about Moebius:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 54.
	all      A-numbers  : 164.
	missing  sequences  : 44.

[('missing', 44), ('A000012', 35), ('A000007', 12), ('A000010', 8), ('A113704', 5), ('A063524', 5), ('A000027', 5), ('A039966', 4), ('A000035', 4), ('A000005', 4), ('A367774', 3), ('A365807', 3), ('A363914', 3), ('A325596', 3), ('A209229', 3), ('A135528', 3), ('A130779', 3), ('A081307', 3), ('A034444', 3), ('A019590', 3), ('A008966', 3), ('A007503', 3), ('A002378', 3), ('A001227', 3), ('A367773', 2), ('A154272', 2), ('A112329', 2), ('A079978', 2), ('A074854', 2), ('A056045', 2), ('A055895', 2), ('A027375', 2), ('A007531', 2), ('A367326', 1), ('A363916', 1), ('A363913', 1), ('A363733', 1), ('A357051', 1), ('A338547', 1), ('A320111', 1), ('A252764', 1), ('A183063', 1), ('A115944', 1), ('A098018', 1), ('A094471', 1), ('A066108', 1), ('A054718', 1), ('A036987', 1), ('A034262', 1), ('A032741', 1), ('A007434', 1), ('A005563', 1), ('A002522', 1), ('A001157', 1), ('A000203', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Moebius.html .
2025/01/10

'''
