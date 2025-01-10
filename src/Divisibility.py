from functools import cache
from _tabltypes import MakeTriangle

"""
The divisibility matrix, the indicator function for divisibility.

[ 0]  1
[ 1]  0  1
[ 2]  0  1  1
[ 3]  0  1  0  1
[ 4]  0  1  1  0  1
[ 5]  0  1  0  0  0  1
[ 6]  0  1  1  1  0  0  1
[ 7]  0  1  0  0  0  0  0  1
[ 8]  0  1  1  0  1  0  0  0  1
[ 9]  0  1  0  1  0  0  0  0  0  1
[10]  0  1  1  0  0  1  0  0  0  0  1
"""


@cache
def divisibility(n: int) -> list[int]:
    if n == 0:
        return [1]
    L = [0 for _ in range(n + 1)]
    L[1] = L[n] = 1
    i = 1
    div = n

    while i < div:
        div, mod = divmod(n, i)
        if mod == 0:
            L[i] = L[div] = 1
        i += 1
    return L


@MakeTriangle(divisibility, "Divisibility", ["A113704", "A051731"], True)
def Divisibility(n: int, k: int) -> int:
    return divisibility(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(Divisibility)

''' OEIS

The traits of the Divisibility triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000005 | Std-RowSum       | d(n) (also called tau(n) or sigma_0(n)), the number of divisors of n           |
| 2   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 3   | A000010 | Inv-AccSum       | Euler totient function phi(n): count numbers <= n and prime to n               |
| 4   | A000012 | Std-RevInv       | The simplest sequence of positive numbers: the all 1's sequence                |
| 5   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 6   | A000035 | Std-DiagCol2     | Period 2: repeat [0, 1]; a(n) = n mod 2; parity of n                           |
| 7   | A000203 | Std-TransNat0    | a(n) = sigma(n), the sum of the divisors of n. Also called sigma_1(n)          |
| 8   | A001157 | Std-TransSqrs    | a(n) = sigma_2(n): sum of squares of divisors of n                             |
| 9   | A001227 | Std-OddSum       | Number of odd divisors of n                                                    |
| 10  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 11  | A002522 | Rev-PolyRow3     | a(n) = n^2 + 1                                                                 |
| 12  | A005563 | Inv:Rev-PolyRow3 | a(n) = n*(n+2) = (n+1)^2 - 1                                                   |
| 13  | A007434 | Inv-TransSqrs    | Jordan function J_2(n) (a generalization of phi(n))                            |
| 14  | A007503 | Std-AccRevSum    | Number of subgroups of dihedral group: sigma(n) + d(n)                         |
| 15  | A007531 | Inv-PolyRow3     | a(n) = n*(n-1)*(n-2) (or n!/(n-3)!)                                            |
| 16  | A008966 | Inv-DiagCol1     | a(n) = 1 if n is squarefree, otherwise 0                                       |
| 17  | A019590 | Inv-RowSum       | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 18  | A027375 | Inv-PolyCol2     | Number of aperiodic binary strings of length n; also number of binary sequence |
| 19  | A032741 | Std-DiagSum      | a(0) = 0; for n > 0, a(n) = number of proper divisors of n (divisors of n whic |
| 20  | A034262 | Std-PolyRow3     | a(n) = n^3 + n                                                                 |
| 21  | A034444 | Inv-AbsSum       | a(n) is the number of unitary divisors of n (d such that d divides n, gcd(d, n |
| 22  | A036987 | Inv:Rev-OddSum   | Fredholm-Rueppel sequence                                                      |
| 23  | A039966 | Std-DiagRow2     | a(0) = 1; thereafter a(3n+2) = 0, a(3n) = a(3n+1) = a(n)                       |
| 24  | A054718 | Inv-PolyCol3     | Number of ternary sequences with primitive period n                            |
| 25  | A055895 | Std-PolyCol2     | Inverse Moebius transform of powers of 2                                       |
| 26  | A056045 | Std-BinConv      | a(n) = Sum_{d|n} binomial(n,d)                                                 |
| 27  | A063524 | Std-DiagRow1     | Characteristic function of 1                                                   |
| 28  | A064027 | Alt-TransSqrs    | a(n) = (-1)^n*Sum_{d|n} (-1)^d*d^2                                             |
| 29  | A066108 | Std-PolyDiag     | Sum n^d over all divisors of n                                                 |
| 30  | A074854 | Std-PosHalf      | a(n) = Sum_{d|n} (2^(n-d))                                                     |
| 31  | A079978 | Std-DiagCol3     | Characteristic function of multiples of three                                  |
| 32  | A081307 | Std-AccSum       | a(n) = (n+1)*tau(n) - sigma(n)                                                 |
| 33  | A094471 | Rev-TransNat0    | a(n) = Sum_{(n - k)|n, 0 <= k <= n} k                                          |
| 34  | A098018 | Inv-DiagSum      | a(n) = Sum_{k|n, k>=2} mu(k-1), where mu() is the Moebius function             |
| 35  | A112329 | Std-AltSum       | Number of divisors of n if n odd, number of divisors of n/4 if n divisible by  |
| 36  | A113184 | Alt-TransNat0    | Absolute difference between sum of odd divisors of n and sum of even divisors  |
| 37  | A113704 | Std-Triangle     | Triangle read by rows. The indicator function for divisibility                 |
| 38  | A115944 | Inv:Rev-EvenSum  | Number of partitions of n into distinct factorials                             |
| 39  | A130779 | Inv-AltSum       | a(0)=a(1)=1, a(2)=2, a(n)=0 for n >= 3                                         |
| 40  | A135528 | Std-ColMiddle    | 1, then repeat 1,0                                                             |
| 41  | A154272 | Inv-EvenSum      | 1,0,1 followed by 0,0,0,..                                                     |
| 42  | A183063 | Std-EvenSum      | Number of even divisors of n                                                   |
| 43  | A209229 | Std-CentralO     | Characteristic function of powers of 2, cf. A000079                            |
| 44  | A252764 | Inv-PolyDiag     | Number of length n primitive (=aperiodic or period n) n-ary words              |
| 45  | A320111 | Rev-EvenSum      | Number of divisors d of n that are not of the form 4k+2                        |
| 46  | A325937 | Alt-DiagSum      | Expansion of Sum_{k>=1} (-1)^(k + 1) * x^(2*k) / (1 - x^k)                     |
| 47  | A357051 | Rev-PolyCol3     | a(n) = Sum_{d|n} 3^(n-d)                                                       |
| 48  | A363629 | Alt-AccRevSum    | Expansion of Sum_{k>0} (1/(1+x^k)^2 - 1)                                       |
| 49  | A363733 | Std-Poly         | Array read by upwards antidiagonals. The family of polynomials generated by th |
| 50  | A363913 | Std-PolyCol3     | a(n) = Sum_{k=0..n} divides(k, n) * 3^k, where divides(k, n) = 1 if k divides  |
| 51  | A363914 | Std-Inv          | The Moebius triangle read by rows. Inverse matrix of the divisibility triangle |
| 52  | A363916 | Inv-Poly         | Array read by descending antidiagonals. A(n, k) = Sum_{d=0..k} A363914(k, d) * |
| 53  | A365807 | Inv-DiagCol3     | a(n) = 1 if A163511(n) is a square, 0 otherwise                                |
| 54  | A367326 | Rev-TransSqrs    | a(n) = Sum_{(n - k)|n} k^2                                                     |
| 55  | A367773 | Inv-NegHalf      | a(n) = Sum_{k=0..n} A363914(n, k)*(-2)^(n - k)                                 |
| 56  | A367774 | Inv-PosHalf      | a(n) = Sum_{k=0..n} A363914(n, k)*2^(n - k)                                    |

* Statistic about Divisibility:

	Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
	distinct A-numbers  : 56.
	all      A-numbers  : 164.
	missing  sequences  : 47.

[('missing', 47), ('A000012', 33), ('A000007', 12), ('A000010', 8), ('A000005', 6), ('A363914', 5), ('A063524', 5), ('A000035', 5), ('A000027', 5), ('A039966', 4), ('A001227', 4), ('A209229', 3), ('A135528', 3), ('A113704', 3), ('A112329', 3), ('A081307', 3), ('A079978', 3), ('A074854', 3), ('A056045', 3), ('A007503', 3), ('A002378', 3), ('A367774', 2), ('A365807', 2), ('A363629', 2), ('A183063', 2), ('A130779', 2), ('A055895', 2), ('A034444', 2), ('A034262', 2), ('A027375', 2), ('A019590', 2), ('A008966', 2), ('A367773', 1), ('A367326', 1), ('A363916', 1), ('A363913', 1), ('A363733', 1), ('A357051', 1), ('A325937', 1), ('A320111', 1), ('A252764', 1), ('A154272', 1), ('A115944', 1), ('A113184', 1), ('A098018', 1), ('A094471', 1), ('A066108', 1), ('A064027', 1), ('A054718', 1), ('A036987', 1), ('A032741', 1), ('A007531', 1), ('A007434', 1), ('A005563', 1), ('A002522', 1), ('A001157', 1), ('A000203', 1)]

A related webpage is: https://peterluschny.github.io/tabl/Divisibility.html .
2025/01/10

'''
