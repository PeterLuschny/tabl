from functools import cache
from _tabltypes import MakeTriangle

"""Inverse of the DyckPaths triangle. Unsigned version.

 [1] 
 [1, 1] 
 [1, 3, 1] 
 [1, 6, 5, 1] 
 [1, 10, 15, 7, 1] 
 [1, 15, 35, 28, 9, 1] 
 [1, 21, 70, 84, 45, 11, 1]
 [1, 28, 126, 210, 165, 66, 13, 1]
"""


@cache
def dyckpathsinv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    q = dyckpathsinv(n - 2) + [0]
    p = dyckpathsinv(n - 1) + [0]
    row = p.copy()
    row[n] = 1

    for k in range(n - 1, 0, -1):
        row[k] = p[k - 1] + 2 * p[k] - q[k]

    return row


@MakeTriangle(dyckpathsinv, "DyckPathsInv", ["A039599", "A050155"], True)
def DyckPathsInv(n: int, k: int) -> int:
    return dyckpathsinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(DyckPathsInv)


''' OEIS

The traits of the DyckPathsInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                       
  |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Rev:Inv-RowSum   | The characteristic function of {0}: a(n) = 0^n                               
  |
| 2   | A000012 | Std-RowGcd       | The simplest sequence of positive numbers: the all 1's sequence              
  |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Std-DiagSum      | Powers of 2: a(n) = 2^n                                                      
  |
| 5   | A000108 | Inv-AccSum       | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)              
  |
| 6   | A000217 | Std-DiagCol1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 7   | A000245 | Inv-DiagCol1     | a(n) = 3*(2*n)!/((n+2)!*(n-1)!)                                              
  |
| 8   | A000332 | Std-DiagCol2     | Binomial coefficient binomial(n,4) = n*(n-1)*(n-2)*(n-3)/24                  
  |
| 9   | A000344 | Inv-DiagCol2     | a(n) = 5*binomial(2n, n-2)/(n+3)                                             
  |
| 10  | A000384 | Std-DiagRow2     | Hexagonal numbers: a(n) = n*(2*n-1)                                          
  |
| 11  | A000447 | Std-DiagRow3     | a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3             
  |
| 12  | A000579 | Std-DiagCol3     | Figurate numbers or binomial coefficients C(n,6)                             
  |
| 13  | A000588 | Inv-DiagCol3     | a(n) = 7*binomial(2n,n-3)/(n+4)                                              
  |
| 14  | A000957 | Inv-PolyCol2     | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 15  | A000958 | Inv-DiagSum      | Number of ordered rooted trees with n edges having root of odd degree          |
| 16  | A000984 | Inv-AltSum       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2               
  |
| 17  | A001519 | Std-RowSum       | a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1                    
  |
| 18  | A001700 | Inv-EvenSum      | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 19  | A001835 | Std-PolyCol2     | a(n) = 4*a(n-1) - a(n-2), with a(0) = 1, a(1) = 1                            
  |
| 20  | A001870 | Std-TransNat0    | Expansion of (1-x)/(1 - 3*x + x^2)^2                                         
  |
| 21  | A002378 | Rev:Inv-PolyRow2 | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)           
  |
| 22  | A004253 | Std-PolyCol3     | a(n) = 5*a(n-1) - a(n-2), with a(1)=1, a(2)=4                                
  |
| 23  | A005408 | Std-DiagRow1     | The odd numbers: a(n) = 2*n + 1                                              
  |
| 24  | A005439 | Rev:Inv-ColLeft  | Genocchi medians (or Genocchi numbers of second kind)                        
  |
| 25  | A005809 | Std-CentralE     | a(n) = binomial(3n,n)                                                        
  |
| 26  | A007583 | Std-PosHalf      | a(n) = (2^(2*n + 1) + 1)/3                                                   
  |
| 27  | A007854 | Inv:Rev-NegHalf  | Expansion of 1/(1 - 3*x*C(x)), where C(x) = (1 - sqrt(1 - 4*x))/(2*x) = g.f. f |
| 28  | A014105 | Inv:Rev-PolyRow2 | Second hexagonal numbers: a(n) = n*(2*n + 1)                                 
  |
| 29  | A014107 | Inv-DiagRow2     | a(n) = n*(2*n-3)                                                             
  |
| 30  | A025174 | Rev-CentralO     | a(n) = binomial(3n-1, n-1)                                                   
  |
| 31  | A027989 | Std-AccSum       | a(n) = self-convolution of row n of array T given by A027926                 
  |
| 32  | A028387 | Std-PolyRow2     | a(n) = n + (n+1)^2                                                           
  |
| 33  | A034839 | Std-AntiDiag     | Triangular array formed by taking every other term of each row of Pascal's tri |
| 34  | A038730 | Std-AccRev       | Path-counting triangular array T(i,j), read by rows, obtained from array t in  |
| 35  | A038731 | Std-AccRevSum    | Number of columns in all directed column-convex polyominoes of area n+1        |
| 36  | A039599 | Std-Inv          | Triangle formed from even-numbered columns of triangle of expansions of powers |
| 37  | A050165 | Std-RevInv       | Triangle read by rows: T(n,k) = M(2n+1,k,-1), 0 <= k <= n, n >= 0, array M as  |
| 38  | A052535 | Rev-DiagSum      | Expansion of (1-x)*(1+x)/(1-x-2*x^2+x^4)                                     
  |
| 39  | A053698 | Inv-PolyRow3     | a(n) = n^3 + n^2 + n + 1                                                     
  |
| 40  | A054142 | Std-Rev          | Triangular array binomial(2*n-k, k), k=0..n, n >= 0                          
  |
| 41  | A054444 | Rev-TransNat0    | Even-indexed terms of A001629(n), n >= 2, (Fibonacci convolution)            
  |
| 42  | A064062 | Inv-PosHalf      | Generalized Catalan numbers C(2; n)                                          
  |
| 43  | A078718 | Inv:Rev-TransSqr | a(n) = (-1)^n*(2*n - 1)*CatalanNumber(n - 2) for n >= 2, a(n) = n for n = 0, 1 |
| 44  | A082759 | Std-BinConv      | a(n) = Sum_{k = 0..n} binomial(n,k)*trinomial(n,k), where trinomial(n,k) = tri |
| 45  | A085478 | Std-Triangle     | Triangle read by rows: T(n, k) = binomial(n + k, 2*k)                        
  |
| 46  | A087168 | Std-NegHalf      | Expansion of (1 + 2*x)/(1 + 3*x + 4*x^2)                                     
  |
| 47  | A089022 | Inv-NegHalf      | Number of walks of length 2n on the 3-regular tree beginning and ending at som |
| 48  | A094955 | Std-PolyDiag     | Main diagonal of array A094954                                               
  |
| 49  | A098435 | Std-InvRev       | Triangle of Salie numbers T(n,k) for negative n,k, n < k                     
  |
| 50  | A099511 | Rev-OddSum       | Row sums of triangle A099510, so that a(n) = Sum_{k=0..n} coefficient of z^k i |
| 51  | A106734 | Rev-PolyRow3     | a(n) = n^3 - 7*n + 7                                                         
  |
| 52  | A108479 | Rev-EvenSum      | Antidiagonal sums of number triangle A086645                                 
  |
| 53  | A109961 | Std-EvenSum      | Expansion of (1-x)^3/(1-4x+5x^2-4x^3+x^4)                                    
  |
| 54  | A110520 | Inv:Rev-PolyCol3 | Expansion of 1/(1-2*x*c(3*x)), c(x) the g.f. of A000108                      
  |
| 55  | A117671 | Std-CentralO     | a(n) = binomial(3*n+1, n+1)                                                  
  |
| 56  | A123972 | Std-PolyRow3     | a(n) = n^3 - n^2 - 2*n + 1                                                   
  |
| 57  | A126596 | Inv-CentralE     | a(n) = binomial(4*n,n)*(2*n+1)/(3*n+1)                                       
  |
| 58  | A126984 | Inv-PolyCol3     | Expansion of 1/(1+2*x*c(x)), c(x) the g.f. of Catalan numbers A000108          |
| 59  | A128899 | Inv-Acc          | Riordan array (1,(1-2x-sqrt(1-4x))/(2x))                                     
  |
| 60  | A151842 | Alt-TransNat0    | a(3n)=n, a(3n+1)=2n+1, a(3n+2)=n+1                                           
  |
| 61  | A174687 | Inv-InvBinConv   | Central coefficients T(2n,n) of the Catalan triangle A033184                 
  |
| 62  | A212501 | Rev:Inv-DiagRow2 | Number of (w,x,y,z) with all terms in {1,...,n} and w > x < y >= z           
  |
| 63  | A242659 | Rev:Inv-PolyRow3 | a(n) = n*(n^2 - 3*n + 4)                                                     
  |

* Statistic about DyckPathsInv:

        Triangles considered: ['Std', 'Alt', 'Rev', 'Rev:Inv', 'Inv', 'Inv:Rev'].
        distinct A-numbers  : 63.
        all      A-numbers  : 162.
        missing  sequences  : 92.

[('missing', 92), ('A000012', 14), ('A000108', 11), ('A001519', 6), ('A000027', 6), ('A054142', 5), ('A005408', 5), ('A098435', 4), ('A085478', 4), ('A039599', 4), ('A001700', 4), ('A000984', 4), ('A000217', 4), ('A082759', 3), ('A050165', 3), ('A038731', 3), ('A028387', 3), ('A027989', 3), ('A007583', 3), ('A005809', 3), ('A000579', 3), ('A000447', 3), ('A000384', 3), ('A000332', 3), ('A000007', 3), ('A174687', 2), ('A128899', 2), ('A126596', 2), ('A117671', 2), ('A109961', 2), ('A087168', 2), ('A064062', 2), ('A038730', 2), ('A034839', 2), ('A014107', 2), ('A002378', 2), ('A001835', 2), ('A000957', 2), ('A000588', 2), ('A000344', 2), ('A000245', 2), ('A242659', 1), ('A212501', 1), ('A151842', 1), ('A126984', 1), ('A123972', 1), ('A110520', 1), ('A108479', 1), ('A106734', 1), ('A099511', 1), ('A094955', 1), ('A089022', 1), ('A078718', 1), ('A054444', 1), ('A053698', 1), ('A052535', 1), ('A025174', 1), ('A014105', 1), ('A007854', 1), ('A005439', 1), ('A004253', 1), ('A001870', 1), ('A000958', 1), ('A000079', 1)]

A related webpage is: https://peterluschny.github.io/tabl/DyckPathsInv.html .
2025/02/24

14 A000012 ['Std-RowGcd', 'Std-ColLeft', 'Std-ColRight', 'Alt-RowGcd', 'Alt-ColLeft', 'Rev-RowGcd', 'Rev-ColLeft', 'Rev-ColRight', 'Rev:Inv-RowGcd', 'Rev:Inv-ColRight', 'Inv-RowGcd', 'Inv-ColRight', 'Inv:Rev-RowGcd', 'Inv:Rev-ColLeft']
          The simplest sequence of positive numbers: the all 1's sequence
          1 1 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

11 A000108 ['Inv-AccSum', 'Inv-AccRevSum', 'Inv-ColLeft', 'Inv-TransNat0', 'Inv-TransNat1', 'Inv-TransSqrs', 'Inv:Rev-AccSum', 'Inv:Rev-AccRevSum', 'Inv:Rev-ColRight', 'Inv:Rev-TransNat0', 'Inv:Rev-TransNat1']
          Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)
          1 -1 1 -2 5 -14 42 -132 429 -1430 4862 -16796 58786 -208012 742900 -2674440 9694845 -35357670

6 A000027 ['Std-PolyRow1', 'Alt-PolyRow1', 'Rev-PolyRow1', 'Rev:Inv-PolyRow1', 'Inv-PolyRow1', 'Inv:Rev-PolyRow1']
          The positive integers. Also called the natural numbers, the whole numbers or the counting 
          1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36      

6 A001519 ['Std-RowSum', 'Std-AbsSum', 'Alt-AltSum', 'Alt-AbsSum', 'Rev-RowSum', 'Rev-AbsSum']
          a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1
          1 2 5 13 34 89 233 610 1597 4181 10946 28657 75025 196418 514229 1346269 3524578 9227465 24157817       

5 A005408 ['Std-DiagRow1', 'Alt-DiagRow1', 'Rev-DiagCol1', 'Inv-DiagRow1', 'Inv:Rev-DiagCol1']
          The odd numbers: a(n) = 2*n + 1
          1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69     

5 A054142 ['Std-Rev', 'Alt-Rev', 'Rev-Triangle', 'Rev:Inv-Inv', 'Inv-RevInv']
          Triangular array binomial(2*n-k, k), k=0..n, n >= 0
          1 1 1 1 3 1 1 5 6 1 1 7 15 10 1 1 9 28 35 15 1 1 11 45 84 70 21 1 1 13 66 165 210 126 28 1 1 15 91      

4 A000217 ['Std-DiagCol1', 'Alt-DiagCol1', 'Rev-DiagRow1', 'Rev:Inv-DiagRow1']
          Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n
          1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171 190 210 231 253 276 300 325 351 378 406 435     

4 A000984 ['Inv-AltSum', 'Inv-AbsSum', 'Inv:Rev-AltSum', 'Inv:Rev-AbsSum']
          Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2
          1 -2 6 -20 70 -252 924 -3432 12870 -48620 184756 -705432 2704156 -10400600 40116600 -155117520

4 A001700 ['Inv-EvenSum', 'Inv-OddSum', 'Inv:Rev-EvenSum', 'Inv:Rev-OddSum']
          a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls into n+1 di
          1 -1 3 -10 35 -126 462 -1716 6435 -24310 92378 -352716 1352078 -5200300 20058300 -77558760

4 A039599 ['Std-Inv', 'Rev-InvRev', 'Inv-Triangle', 'Inv:Rev-Rev']
          Triangle formed from even-numbered columns of triangle of expansions of powers of x in ter
          1 -1 1 2 -3 1 -5 9 -5 1 14 -28 20 -7 1 -42 90 -75 35 -9 1 132 -297 275 -154 54 -11 1 -429 1001

4 A085478 ['Std-Triangle', 'Alt-Triangle', 'Rev:Inv-RevInv', 'Inv:Rev-InvRev']
          Triangle read by rows: T(n, k) = binomial(n + k, 2*k)
          1 1 1 1 3 1 1 6 5 1 1 10 15 7 1 1 15 35 28 9 1 1 21 70 84 45 11 1 1 28 126 210 165 66 13 1 1 36 210     

4 A098435 ['Std-InvRev', 'Alt-InvRev', 'Rev-Inv', 'Rev:Inv-Triangle']
          Triangle of Salie numbers T(n,k) for negative n,k, n < k
          1 -1 1 2 -3 1 -8 13 -6 1 56 -92 45 -10 1 -608 1000 -493 115 -15 1 9440 -15528 7662 -1799 245 -21 1      

3 A000007 ['Rev:Inv-RowSum', 'Inv-RowSum', 'Inv:Rev-RowSum']
          The characteristic function of {0}: a(n) = 0^n
          1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

3 A000332 ['Std-DiagCol2', 'Alt-DiagCol2', 'Rev-DiagRow2']
          Binomial coefficient binomial(n,4) = n*(n-1)*(n-2)*(n-3)/24
          1 5 15 35 70 126 210 330 495 715 1001 1365 1820 2380 3060 3876 4845 5985 7315 8855 10626 12650

3 A000384 ['Std-DiagRow2', 'Alt-DiagRow2', 'Rev-DiagCol2']
          Hexagonal numbers: a(n) = n*(2*n-1)
          1 6 15 28 45 66 91 120 153 190 231 276 325 378 435 496 561 630 703 780 861 946 1035 1128 1225 1326      

3 A000447 ['Std-DiagRow3', 'Alt-DiagRow3', 'Rev-DiagCol3']
          a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3
          1 10 35 84 165 286 455 680 969 1330 1771 2300 2925 3654 4495 5456 6545 7770 9139 10660 12341 14190      

3 A000579 ['Std-DiagCol3', 'Alt-DiagCol3', 'Rev-DiagRow3']
          Figurate numbers or binomial coefficients C(n,6)
          1 7 28 84 210 462 924 1716 3003 5005 8008 12376 18564 27132 38760 54264 74613 100947 134596 177100      

3 A005809 ['Std-CentralE', 'Alt-CentralE', 'Rev-CentralE']
          a(n) = binomial(3n,n)
          1 3 15 84 495 3003 18564 116280 735471 4686825 30045015 193536720 1251677700 8122425444 52860229080     

3 A007583 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          a(n) = (2^(2*n + 1) + 1)/3
          1 3 11 43 171 683 2731 10923 43691 174763 699051 2796203 11184811 44739243 178956971 715827883

3 A027989 ['Std-AccSum', 'Rev-AccRevSum', 'Rev-TransNat1']
          a(n) = self-convolution of row n of array T given by A027926
          1 3 10 33 105 324 977 2895 8462 24465 70101 199368 563425 1583643 4430290 12342849 34262337

3 A028387 ['Std-PolyRow2', 'Alt-PolyRow2', 'Rev-PolyRow2']
          a(n) = n + (n+1)^2
          1 5 11 19 29 41 55 71 89 109 131 155 181 209 239 271 305 341 379 419 461 505 551 599 649 701 755        

3 A038731 ['Std-AccRevSum', 'Std-TransNat1', 'Rev-AccSum']
          Number of columns in all directed column-convex polyominoes of area n+1
          1 3 10 32 99 299 887 2595 7508 21526 61251 173173 486925 1362627 3797374 10543724 29180067 80521055     

3 A050165 ['Std-RevInv', 'Inv-Rev', 'Inv:Rev-Triangle']
          Triangle read by rows: T(n,k) = M(2n+1,k,-1), 0 <= k <= n, n >= 0, array M as in A050144  
          1 1 -1 1 -3 2 1 -5 9 -5 1 -7 20 -28 14 1 -9 35 -75 90 -42 1 -11 54 -154 275 -297 132 1 -13 77 -273      

3 A082759 ['Std-BinConv', 'Alt-InvBinConv', 'Rev-BinConv']
          a(n) = Sum_{k = 0..n} binomial(n,k)*trinomial(n,k), where trinomial(n,k) = trinomial coeff
          1 2 8 35 160 752 3599 17446 85376 420884 2087008 10398016 52010479 261021854 1313707256 6628095035      

2 A000245 ['Inv-DiagCol1', 'Inv:Rev-DiagRow1']
          a(n) = 3*(2*n)!/((n+2)!*(n-1)!)
          1 -3 9 -28 90 -297 1001 -3432 11934 -41990 149226 -534888 1931540 -7020405 25662825 -94287120

2 A000344 ['Inv-DiagCol2', 'Inv:Rev-DiagRow2']
          a(n) = 5*binomial(2n, n-2)/(n+3)
          1 -5 20 -75 275 -1001 3640 -13260 48450 -177650 653752 -2414425 8947575 -33266625 124062000

2 A000588 ['Inv-DiagCol3', 'Inv:Rev-DiagRow3']
          a(n) = 7*binomial(2n,n-3)/(n+4)
          1 -7 35 -154 637 -2548 9996 -38760 149226 -572033 2187185 -8351070 31865925 -121580760 463991880        

2 A000957 ['Inv-PolyCol2', 'Inv:Rev-PosHalf']
          Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n-set; also n
          1 1 0 1 -2 6 -18 57 -186 622 -2120 7338 -25724 91144 -325878 1174281 -4260282 15548694 -57048048        

2 A001835 ['Std-PolyCol2', 'Rev-PosHalf']
          a(n) = 4*a(n-1) - a(n-2), with a(0) = 1, a(1) = 1
          1 3 11 41 153 571 2131 7953 29681 110771 413403 1542841 5757961 21489003 80198051 299303201

2 A002378 ['Rev:Inv-PolyRow2', 'Inv-PolyRow2']
          Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)
          2 0 0 2 6 12 20 30 42 56 72 90 110 132 156 182 210 240 272 306 342 380 420 462 506 552 600 650 702      

2 A014107 ['Inv-DiagRow2', 'Inv:Rev-DiagCol2']
          a(n) = n*(2*n-3)
          2 9 20 35 54 77 104 135 170 209 252 299 350 405 464 527 594 665 740 819 902 989 1080 1175 1274 1377     

2 A034839 ['Std-AntiDiag', 'Alt-AntiDiag']
          Triangular array formed by taking every other term of each row of Pascal's triangle       
          1 1 1 1 1 3 1 6 1 1 10 5 1 15 15 1 1 21 35 7 1 28 70 28 1 1 36 126 84 9 1 45 210 210 45 1 1 55 330      

2 A038730 ['Std-AccRev', 'Rev-Acc']
          Path-counting triangular array T(i,j), read by rows, obtained from array t in A038792 by T
          1 1 2 1 4 5 1 6 12 13 1 8 23 33 34 1 10 38 73 88 89 1 12 57 141 211 232 233 1 14 80 245 455 581 609     

2 A064062 ['Inv-PosHalf', 'Inv:Rev-PolyCol2']
          Generalized Catalan numbers C(2; n)
          1 -1 3 -13 67 -381 2307 -14589 95235 -636925 4341763 -30056445 210731011 -1493303293 10678370307        

2 A087168 ['Std-NegHalf', 'Alt-PosHalf']
          Expansion of (1 + 2*x)/(1 + 3*x + 4*x^2)
          1 -1 -1 7 -17 23 -1 -89 271 -457 287 967 -4049 8279 -8641 -7193 56143 -139657 194399 -24569 -703889     

2 A109961 ['Std-EvenSum', 'Alt-EvenSum']
          Expansion of (1-x)^3/(1-4x+5x^2-4x^3+x^4)
          1 1 2 6 17 45 117 305 798 2090 5473 14329 37513 98209 257114 673134 1762289 4613733 12078909

2 A117671 ['Std-CentralO', 'Alt-CentralO']
          a(n) = binomial(3*n+1, n+1)
          1 6 35 210 1287 8008 50388 319770 2042975 13123110 84672315 548354040 3562467300 23206929840

2 A126596 ['Inv-CentralE', 'Inv:Rev-CentralE']
          a(n) = binomial(4*n,n)*(2*n+1)/(3*n+1)
          1 -3 20 -154 1260 -10659 92092 -807300 7152444 -63882940 574221648 -5188082354 47073334100

2 A128899 ['Inv-Acc', 'Inv:Rev-AccRev']
          Riordan array (1,(1-2x-sqrt(1-4x))/(2x))
          1 -1 0 2 -1 0 -5 4 -1 0 14 -14 6 -1 0 -42 48 -27 8 -1 0 132 -165 110 -44 10 -1 0 -429 572 -429 208      

2 A174687 ['Inv-InvBinConv', 'Inv:Rev-InvBinConv']
          Central coefficients T(2n,n) of the Catalan triangle A033184
          1 2 9 48 275 1638 9996 62016 389367 2466750 15737865 100975680 650872404 4211628008 27341497800

1 A000079 ['Std-DiagSum']
          Powers of 2: a(n) = 2^n
          1 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576       

1 A000958 ['Inv-DiagSum']
          Number of ordered rooted trees with n edges having root of odd degree
          1 -1 3 -8 24 -75 243 -808 2742 -9458 33062 -116868 417022 -1500159 5434563 -19808976 72596742

1 A001870 ['Std-TransNat0']
          Expansion of (1-x)/(1 - 3*x + x^2)^2
          0 1 5 19 65 210 654 1985 5911 17345 50305 144516 411900 1166209 3283145 9197455 25655489 71293590       

1 A004253 ['Std-PolyCol3']
          a(n) = 5*a(n-1) - a(n-2), with a(1)=1, a(2)=4
          1 4 19 91 436 2089 10009 47956 229771 1100899 5274724 25272721 121088881 580171684 2779769539

1 A005439 ['Rev:Inv-ColLeft']
          Genocchi medians (or Genocchi numbers of second kind)
          1 -1 2 -8 56 -608 9440 -198272 5410688 -186043904 7867739648 -401293838336 24290513745920

1 A007854 ['Inv:Rev-NegHalf']
          Expansion of 1/(1 - 3*x*C(x)), where C(x) = (1 - sqrt(1 - 4*x))/(2*x) = g.f. for the Catal
          1 -3 12 -51 222 -978 4338 -19323 86310 -386250 1730832 -7763550 34847796 -156503064 703149438

1 A014105 ['Inv:Rev-PolyRow2']
          Second hexagonal numbers: a(n) = n*(2*n + 1)
          1 0 3 10 21 36 55 78 105 136 171 210 253 300 351 406 465 528 595 666 741 820 903 990 1081 1176 1275     

1 A025174 ['Rev-CentralO']
          a(n) = binomial(3n-1, n-1)
          1 5 28 165 1001 6188 38760 245157 1562275 10015005 64512240 417225900 2707475148 17620076360

1 A052535 ['Rev-DiagSum']
          Expansion of (1-x)*(1+x)/(1-x-2*x^2+x^4)
          1 1 2 4 7 14 26 50 95 181 345 657 1252 2385 4544 8657 16493 31422 59864 114051 217286 413966 788674     

1 A053698 ['Inv-PolyRow3']
          a(n) = n^3 + n^2 + n + 1
          -5 0 1 4 15 40 85 156 259 400 585 820 1111 1464 1885 2380 2955 3616 4369 5220 6175 7240 8421 9724       

1 A054444 ['Rev-TransNat0']
          Even-indexed terms of A001629(n), n >= 2, (Fibonacci convolution)
          0 1 5 20 71 235 744 2285 6865 20284 59155 170711 488400 1387225 3916061 10996580 30737759 85573315      

1 A078718 ['Inv:Rev-TransSqrs']
          a(n) = (-1)^n*(2*n - 1)*CatalanNumber(n - 2) for n >= 2, a(n) = n for n = 0, 1
          0 -1 5 -14 45 -154 546 -1980 7293 -27170 102102 -386308 1469650 -5616324 21544100 -82907640

1 A089022 ['Inv-NegHalf']
          Number of walks of length 2n on the 3-regular tree beginning and ending at some fixed vert
          1 3 15 87 543 3543 23823 163719 1143999 8099511 57959535 418441191 3043608351 22280372247

1 A094955 ['Std-PolyDiag']
          Main diagonal of array A094954
          1 2 11 91 985 13201 211303 3936808 83739041 2003229469 53252096051 1557702562417 49731172316281

1 A099511 ['Rev-OddSum']
          Row sums of triangle A099510, so that a(n) = Sum_{k=0..n} coefficient of z^k in (1 + 2*z +
          0 1 3 6 17 45 116 305 799 2090 5473 14329 37512 98209 257115 673134 1762289 4613733 12078908

1 A106734 ['Rev-PolyRow3']
          a(n) = n^3 - 7*n + 7
          1 13 43 97 181 301 463 673 937 1261 1651 2113 2653 3277 3991 4801 5713 6733 7867 9121 10501 12013       

1 A108479 ['Rev-EvenSum']
          Antidiagonal sums of number triangle A086645
          1 1 2 7 17 44 117 305 798 2091 5473 14328 37513 98209 257114 673135 1762289 4613732 12078909

1 A110520 ['Inv:Rev-PolyCol3']
          Expansion of 1/(1-2*x*c(3*x)), c(x) the g.f. of A000108
          1 -2 10 -68 538 -4652 42628 -406856 4001914 -40285724 413049580 -4298523704 45288486436

1 A123972 ['Std-PolyRow3']
          a(n) = n^3 - n^2 - 2*n + 1
          1 13 41 91 169 281 433 631 881 1189 1561 2003 2521 3121 3809 4591 5473 6461 7561 8779 10121 11593       

1 A126984 ['Inv-PolyCol3']
          Expansion of 1/(1+2*x*c(x)), c(x) the g.f. of Catalan numbers A000108
          1 2 2 4 2 12 -12 72 -190 700 -2308 8120 -28364 100856 -360792 1301904 -4727358 17268636 -63405012       

1 A151842 ['Alt-TransNat0']
          a(3n)=n, a(3n+1)=2n+1, a(3n+2)=n+1
          0 -1 -1 1 3 2 -2 -5 -3 3 7 4 -4 -9 -5 5 11 6 -6 -13 -7 7 15 8 -8 -17 -9 9 19 10 -10 -21 -11 11 23       

1 A212501 ['Rev:Inv-DiagRow2']
          Number of (w,x,y,z) with all terms in {1,...,n} and w > x < y >= z
          2 13 45 115 245 462 798 1290 1980 2915 4147 5733 7735 10220 13260 16932 21318 26505 32585 39655
'''
