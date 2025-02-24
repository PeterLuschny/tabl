from functools import cache
from _tabltypes import MakeTriangle


"""Inverse Catalan triangle. Unsigned version.

  [0] [1]
  [1] [0, 1]
  [2] [0, 2, 1]
  [3] [0, 3, 4, 1]
  [4] [0, 4, 10, 6, 1]
  [5] [0, 5, 20, 21, 8, 1]
  [6] [0, 6, 35, 56, 36, 10, 1]
  [7] [0, 7, 56, 126, 120, 55, 12, 1]
  [8] [0, 8, 84, 252, 330, 220, 78, 14, 1]
  [9] [0, 9, 120, 462, 792, 715, 364, 105, 16, 1]
"""

@cache
def catalaninv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = [0]*(n+1)
    c0 = catalaninv(n-2) + [0, 0]
    c1 = catalaninv(n-1) + [0]
    for k in range(1, n+1):
        row[k] = c1[k-1] + 2*c1[k] - c0[k]
    return row


@MakeTriangle(catalaninv, "CatalanInv", ["A128908", "A053122", "A078812", "A285072"], True)
def CatalanInv(n: int, k: int) -> int:
    return catalaninv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest


''' OEIS

The traits of the CatalanInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                                                       
  |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                               
  |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence              
  |
| 3   | A000027 | Std-DiagCol1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000079 | Std-DiagSum      | Powers of 2: a(n) = 2^n                                                      
  |
| 5   | A000108 | Inv-RowSum       | Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)              
  |
| 6   | A000292 | Std-DiagCol2     | Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2) |
| 7   | A000389 | Std-DiagCol3     | Binomial coefficients C(n,5)                                                 
  |
| 8   | A000567 | Rev-PolyRow3     | Octagonal numbers: n*(3*n-2). Also called star numbers                       
  |
| 9   | A000957 | Inv-DiagSum      | Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n |
| 10  | A000984 | Inv-OddSum       | Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2               
  |
| 11  | A001700 | Inv-AltSum       | a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls |
| 12  | A001791 | Inv-EvenSum      | a(n) = binomial coefficient C(2n, n-1)                                       
  |
| 13  | A001906 | Std-RowSum       | F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)            
  |
| 14  | A002057 | Inv-DiagCol2     | Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)        |
| 15  | A002450 | Std-PosHalf      | a(n) = (4^n - 1)/3                                                           
  |
| 16  | A002492 | Std-DiagRow3     | Sum of the first n even squares: 2*n*(n+1)*(2*n+1)/3                         
  |
| 17  | A003517 | Inv-DiagCol3     | Number of permutations of [n+1] with exactly 1 increasing subsequence of lengt |
| 18  | A005408 | Rev-PolyRow2     | The odd numbers: a(n) = 2*n + 1                                              
  |
| 19  | A005563 | Std-PolyRow2     | a(n) = n*(n+2) = (n+1)^2 - 1                                                 
  |
| 20  | A005843 | Std-DiagRow1     | The nonnegative even numbers: a(n) = 2n                                      
  |
| 21  | A009545 | Alt-DiagSum      | Expansion of e.g.f. sin(x)*exp(x)                                            
  |
| 22  | A010673 | Alt-PolyCol2     | Period 2: repeat [0, 2]                                                      
  |
| 23  | A011655 | Std-AltSum       | Period 3: repeat [0, 1, 1]                                                   
  |
| 24  | A014105 | Std-DiagRow2     | Second hexagonal numbers: a(n) = n*(2*n + 1)                                 
  |
| 25  | A014106 | Inv-DiagRow2     | a(n) = n*(2*n + 3)                                                           
  |
| 26  | A025174 | Inv-InvBinConv   | a(n) = binomial(3n-1, n-1)                                                   
  |
| 27  | A026005 | Inv:Rev-CentralO | a(n) = T(4*n,n), where T = Catalan triangle (A008315)                        
  |
| 28  | A030267 | Std-TransNat0    | Compose the natural numbers with themselves, A(x) = B(B(x)) where B(x) = x/(1- |
| 29  | A038665 | Inv-AccSum       | Convolution of A007054 (super ballot numbers) with A000984 (central binomial c |
| 30  | A045721 | Rev-CentralO     | a(n) = binomial(3*n+1,n)                                                     
  |
| 31  | A049072 | Std-NegHalf      | Expansion of 1/(1 - 3*x + 4*x^2)                                             
  |
| 32  | A052530 | Std-PolyCol2     | a(n) = 4*a(n-1) - a(n-2), with a(0) = 0, a(1) = 2                            
  |
| 33  | A063524 | Inv-TransNat0    | Characteristic function of 1                                                 
  |
| 34  | A064062 | Inv-PosHalf      | Generalized Catalan numbers C(2; n)                                          
  |
| 35  | A067336 | Inv:Rev-NegHalf  | a(0)=1, a(1)=2, a(n) = a(n-1)*9/2 - Catalan(n-1) where Catalan(n) = binomial(2 |
| 36  | A068875 | Inv-TransSqrs    | Expansion of (1 + x*C)*C, where C = (1 - (1 - 4*x)^(1/2))/(2*x) is the g.f. fo |
| 37  | A084103 | Alt-PolyCol3     | Expansion of (1+x)^3/(1+x^3)                                                 
  |
| 38  | A099459 | Rev-PolyCol3     | Expansion of 1/(1 - 7*x + 9*x^2)                                             
  |
| 39  | A099996 | Std-RowLcm       | a(n) = lcm{1, 2, ..., 2*n}                                                   
  |
| 40  | A113066 | Std-OddSum       | Expansion of (1 + x)^2/((1 + x + x^2)*(1 + 3*x + x^2))                       
  |
| 41  | A122918 | Alt-TransNat0    | Expansion of (1+x)^2/(1+x+x^2)^2                                             
  |
| 42  | A128899 | Std-Inv          | Riordan array (1,(1-2x-sqrt(1-4x))/(2x))                                     
  |
| 43  | A128908 | Std-Triangle     | Riordan array (1, x/(1-x)^2)                                                 
  |
| 44  | A137241 | Alt-AccRevSum    | Number triples (k,3-k,2-2k), concatenated for k=0, 1, 2, 3,..                
  |
| 45  | A158943 | Rev-DiagSum      | INVERT transform of A027656: (1, 0, 2, 0, 3, 0, 4, 0, 5, ...)                
  |
| 46  | A165817 | Std-CentralE     | Number of compositions (= ordered integer partitions) of n into 2n parts       |
| 47  | A190816 | Inv:Rev-PolyRow3 | a(n) = 5*n^2 - 4*n + 1                                                       
  |
| 48  | A194723 | Inv-NegHalf      | Number of ternary words either empty or beginning with the first character of  |
| 49  | A262440 | Std-BinConv      | a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k-1,n-k)                      
  |
| 50  | A281199 | Rev-TransNat0    | Number of n X 2 0..1 arrays with no element equal to more than one of its hori |
| 51  | A290890 | Std-EvenSum      | p-INVERT of the positive integers, where p(S) = 1 - S^2                      
  |
| 52  | A290902 | Std-PolyCol3     | p-INVERT of the positive integers, where p(S) = 1 - 3*S                      
  |
| 53  | A290917 | Std-AccRevSum    | p-INVERT of the positive integers, where p(S) = (1 - S)^2                    
  |
| 54  | A297382 | Std-RowGcd       | Denominator of -A023900(n)/2                                                 
  |
| 55  | A317637 | Std-PolyRow3     | a(n) = n*(n+1)*(n+3)                                                         
  |
| 56  | A329682 | Rev-AltSum       | Number of excursions of length n with Motzkin-steps forbidding all consecutive |
| 57  | A332057 | Alt-AccSum       | Partial sums (and absolute value of first differences) of A332056: if odd (res |
| 58  | A350290 | Std-InvBinConv   | a(n) = Sum_{k=0..n} (-1)^(n - k) * binomial(n, k) * binomial(n + k - 1, n - k) |
| 59  | A359108 | Inv-CentralE     | a(n) = A128899(2*n, n) = 2*binomial(4*n - 1, 3*n) for n >= 1 and a(0) = 1      |
| 60  | A371391 | Inv:Rev-PolyCol3 | Expansion of (1/x) * Series_Reversion( x * (1-x) / (1+2*x)^2 )               
  |
| 61  | A376716 | Rev-EvenSum      | Expansion of (1 - x + x^2)/((1 - x + x^2)^2 - 4*x^2)                         
  |
| 62  | A377866 | Std-AccSum       | Number of subwords of the form DUUD or DDUUD in nondecreasing Dyck paths of le |


* Statistic about CatalanInv:

        Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].
        distinct A-numbers  : 62.
        all      A-numbers  : 143.
        missing  sequences  : 69.

[('missing', 69), ('A000108', 7), ('A001906', 6), ('A000027', 6), ('A000012', 6), ('A297382', 5), ('A005843', 5), ('A000007', 5), ('A128899', 4), ('A001700', 4), ('A377866', 3), ('A350290', 3), ('A290917', 3), ('A262440', 3), ('A165817', 3), ('A099996', 3), ('A038665', 3), ('A014105', 3), ('A005563', 3), ('A002492', 3), ('A002450', 3), ('A000389', 3), ('A000292', 3), ('A359108', 2), ('A290890', 2), ('A137241', 2), ('A128908', 2), ('A113066', 2), ('A064062', 2), ('A052530', 2), ('A049072', 2), ('A025174', 2), ('A014106', 2), ('A011655', 2), ('A010673', 2), ('A005408', 2), ('A003517', 2), ('A002057', 2), ('A000984', 2), ('A376716', 1), ('A371391', 1), ('A332057', 1), ('A329682', 1), ('A317637', 1), ('A290902', 1), ('A281199', 1), ('A194723', 1), ('A190816', 1), ('A158943', 1), ('A122918', 1), ('A099459', 1), ('A084103', 1), ('A068875', 1), ('A067336', 1), ('A063524', 1), ('A045721', 1), ('A030267', 1), ('A026005', 1), ('A009545', 1), ('A001791', 1), ('A000957', 1), ('A000567', 1), ('A000079', 1)]

A related webpage is: https://peterluschny.github.io/tabl/CatalanInv.html .
2025/02/24

7 A000108 ['Inv-RowSum', 'Inv-AccRevSum', 'Inv-TransNat1', 'Inv-DiagCol1', 'Inv:Rev-RowSum', 'Inv:Rev-AccSum', 'Inv:Rev-DiagRow1']
          Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!)
          1 1 -1 2 -5 14 -42 132 -429 1430 -4862 16796 -58786 208012 -742900 2674440 -9694845 35357670

6 A000012 ['Std-ColRight', 'Rev-ColLeft', 'Rev-PolyRow1', 'Inv-ColRight', 'Inv:Rev-ColLeft', 'Inv:Rev-PolyRow1']  
          The simplest sequence of positive numbers: the all 1's sequence
          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

6 A000027 ['Std-DiagCol1', 'Std-PolyRow1', 'Alt-DiagCol1', 'Alt-PolyRow1', 'Rev-DiagRow1', 'Inv-PolyRow1']        
          The positive integers. Also called the natural numbers, the whole numbers or the counting 
          1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36      

6 A001906 ['Std-RowSum', 'Std-AbsSum', 'Alt-AltSum', 'Alt-AbsSum', 'Rev-RowSum', 'Rev-AbsSum']
          F(2n) = bisection of Fibonacci sequence: a(n) = 3*a(n-1) - a(n-2)
          1 1 3 8 21 55 144 377 987 2584 6765 17711 46368 121393 317811 832040 2178309 5702887 14930352

5 A000007 ['Std-ColLeft', 'Alt-ColLeft', 'Rev-ColRight', 'Inv-ColLeft', 'Inv:Rev-ColRight']
          The characteristic function of {0}: a(n) = 0^n
          1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

5 A005843 ['Std-DiagRow1', 'Alt-DiagRow1', 'Rev-DiagCol1', 'Inv-DiagRow1', 'Inv:Rev-DiagCol1']
          The nonnegative even numbers: a(n) = 2n
          0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68     

5 A297382 ['Std-RowGcd', 'Alt-RowGcd', 'Rev-RowGcd', 'Inv-RowGcd', 'Inv:Rev-RowGcd']
          Denominator of -A023900(n)/2
          1 1 2 1 2 1 1 1 2 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

4 A001700 ['Inv-AltSum', 'Inv-AbsSum', 'Inv:Rev-AltSum', 'Inv:Rev-AbsSum']
          a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls into n+1 di
          1 -1 3 -10 35 -126 462 -1716 6435 -24310 92378 -352716 1352078 -5200300 20058300 -77558760

4 A128899 ['Std-Inv', 'Rev-InvRev', 'Inv-Triangle', 'Inv:Rev-Rev']
          Riordan array (1,(1-2x-sqrt(1-4x))/(2x))
          1 0 1 0 -2 1 0 5 -4 1 0 -14 14 -6 1 0 42 -48 27 -8 1 0 -132 165 -110 44 -10 1 0 429 -572 429 -208       

3 A000292 ['Std-DiagCol2', 'Alt-DiagCol2', 'Rev-DiagRow2']
          Tetrahedral (or triangular pyramidal) numbers: a(n) = C(n+2,3) = n*(n+1)*(n+2)/6
          1 4 10 20 35 56 84 120 165 220 286 364 455 560 680 816 969 1140 1330 1540 1771 2024 2300 2600 2925      

3 A000389 ['Std-DiagCol3', 'Alt-DiagCol3', 'Rev-DiagRow3']
          Binomial coefficients C(n,5)
          1 6 21 56 126 252 462 792 1287 2002 3003 4368 6188 8568 11628 15504 20349 26334 33649 42504 53130       

3 A002450 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          a(n) = (4^n - 1)/3
          1 1 5 21 85 341 1365 5461 21845 87381 349525 1398101 5592405 22369621 89478485 357913941 1431655765     

3 A002492 ['Std-DiagRow3', 'Alt-DiagRow3', 'Rev-DiagCol3']
          Sum of the first n even squares: 2*n*(n+1)*(2*n+1)/3
          0 4 20 56 120 220 364 560 816 1140 1540 2024 2600 3276 4060 4960 5984 7140 8436 9880 11480 13244        

3 A005563 ['Std-PolyRow2', 'Alt-PolyRow2', 'Inv-PolyRow2']
          a(n) = n*(n+2) = (n+1)^2 - 1
          0 3 8 15 24 35 48 63 80 99 120 143 168 195 224 255 288 323 360 399 440 483 528 575 624 675 728 783      

3 A014105 ['Std-DiagRow2', 'Alt-DiagRow2', 'Rev-DiagCol2']
          Second hexagonal numbers: a(n) = n*(2*n + 1)
          0 3 10 21 36 55 78 105 136 171 210 253 300 351 406 465 528 595 666 741 820 903 990 1081 1176 1275       

3 A038665 ['Inv-AccSum', 'Inv:Rev-AccRevSum', 'Inv:Rev-TransNat1']
          Convolution of A007054 (super ballot numbers) with A000984 (central binomial coefficients)
          1 1 -3 8 -25 84 -294 1056 -3861 14300 -53482 201552 -764218 2912168 -11143500 42791040 -164812365       

3 A099996 ['Std-RowLcm', 'Alt-RowLcm', 'Rev-RowLcm']
          a(n) = lcm{1, 2, ..., 2*n}
          1 1 2 12 60 840 2520 27720 360360 720720 12252240 232792560 232792560 5354228880 26771144400

3 A165817 ['Std-CentralE', 'Alt-CentralE', 'Rev-CentralE']
          Number of compositions (= ordered integer partitions) of n into 2n parts
          1 2 10 56 330 2002 12376 77520 490314 3124550 20030010 129024480 834451800 5414950296 35240152720       

3 A262440 ['Std-BinConv', 'Alt-InvBinConv', 'Rev-BinConv']
          a(n) = Sum_{k=0..n} binomial(n,k) * binomial(n+k-1,n-k)
          1 1 5 22 101 476 2282 11075 54245 267592 1327580 6617128 33110090 166215895 836761343 4222640822        

3 A290917 ['Std-AccRevSum', 'Std-TransNat1', 'Rev-AccSum']
          p-INVERT of the positive integers, where p(S) = (1 - S)^2
          1 2 7 22 67 200 588 1708 4913 14018 39725 111922 313752 875702 2434747 6746350 18636343 51340988        

3 A350290 ['Std-InvBinConv', 'Alt-BinConv', 'Rev-InvBinConv']
          a(n) = Sum_{k=0..n} (-1)^(n - k) * binomial(n, k) * binomial(n + k - 1, n - k)
          1 1 -3 -2 21 -4 -150 155 1029 -2072 -6468 22056 34122 -208857 -106249 1816958 -639067 -14629264

3 A377866 ['Std-AccSum', 'Rev-AccRevSum', 'Rev-TransNat1']
          Number of subwords of the form DUUD or DDUUD in nondecreasing Dyck paths of length 2n     
          1 1 5 18 59 185 564 1685 4957 14406 41455 118321 335400 945193 2650229 7398330 20573219 57013865        

2 A000984 ['Inv-OddSum', 'Inv:Rev-TransNat0']
          Central binomial coefficients: binomial(2*n,n) = (2*n)!/(n!)^2
          0 1 -2 6 -20 70 -252 924 -3432 12870 -48620 184756 -705432 2704156 -10400600 40116600 -155117520        

2 A002057 ['Inv-DiagCol2', 'Inv:Rev-DiagRow2']
          Fourth convolution of Catalan numbers: a(n) = 4*binomial(2*n+3,n)/(n+4)
          1 -4 14 -48 165 -572 2002 -7072 25194 -90440 326876 -1188640 4345965 -15967980 58929450 -218349120      

2 A003517 ['Inv-DiagCol3', 'Inv:Rev-DiagRow3']
          Number of permutations of [n+1] with exactly 1 increasing subsequence of length 3
          1 -6 27 -110 429 -1638 6188 -23256 87210 -326876 1225785 -4601610 17298645 -65132550 245642760

2 A005408 ['Rev-PolyRow2', 'Inv:Rev-PolyRow2']
          The odd numbers: a(n) = 2*n + 1
          1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69     

2 A010673 ['Alt-PolyCol2', 'Rev-NegHalf']
          Period 2: repeat [0, 2]
          1 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2 0 -2 0 2      

2 A011655 ['Std-AltSum', 'Alt-RowSum']
          Period 3: repeat [0, 1, 1]
          1 -1 -1 0 1 1 0 -1 -1 0 1 1 0 -1 -1 0 1 1 0 -1 -1 0 1 1 0 -1 -1 0 1 1 0 -1 -1 0 1 1 0 -1 -1 0 1 1 0     

2 A014106 ['Inv-DiagRow2', 'Inv:Rev-DiagCol2']
          a(n) = n*(2*n + 3)
          0 5 14 27 44 65 90 119 152 189 230 275 324 377 434 495 560 629 702 779 860 945 1034 1127 1224 1325      

2 A025174 ['Inv-InvBinConv', 'Inv:Rev-InvBinConv']
          a(n) = binomial(3n-1, n-1)
          1 1 5 28 165 1001 6188 38760 245157 1562275 10015005 64512240 417225900 2707475148 17620076360

2 A049072 ['Std-NegHalf', 'Alt-PosHalf']
          Expansion of 1/(1 - 3*x + 4*x^2)
          1 1 -3 5 -3 -11 45 -91 93 85 -627 1541 -2115 181 7917 -24475 41757 -27371 -84915 364229 -753027

2 A052530 ['Std-PolyCol2', 'Rev-PosHalf']
          a(n) = 4*a(n-1) - a(n-2), with a(0) = 0, a(1) = 2
          1 2 8 30 112 418 1560 5822 21728 81090 302632 1129438 4215120 15731042 58709048 219105150 817711552     

2 A064062 ['Inv-PosHalf', 'Inv:Rev-PolyCol2']
          Generalized Catalan numbers C(2; n)
          1 1 -3 13 -67 381 -2307 14589 -95235 636925 -4341763 30056445 -210731011 1493303293 -10678370307        

2 A113066 ['Std-OddSum', 'Alt-OddSum']
          Expansion of (1 + x)^2/((1 + x + x^2)*(1 + 3*x + x^2))
          0 1 2 4 10 27 72 189 494 1292 3382 8855 23184 60697 158906 416020 1089154 2851443 7465176 19544085      

2 A128908 ['Std-Triangle', 'Inv:Rev-InvRev']
          Riordan array (1, x/(1-x)^2)
          1 0 1 0 2 1 0 3 4 1 0 4 10 6 1 0 5 20 21 8 1 0 6 35 56 36 10 1 0 7 56 126 120 55 12 1 0 8 84 252        

2 A137241 ['Alt-AccRevSum', 'Alt-TransNat1']
          Number triples (k,3-k,2-2k), concatenated for k=0, 1, 2, 3,..
          1 -2 -1 2 3 0 -4 -4 1 6 5 -2 -8 -6 3 10 7 -4 -12 -8 5 14 9 -6 -16 -10 7 18 11 -8 -20 -12 9 22 13        

2 A290890 ['Std-EvenSum', 'Alt-EvenSum']
          p-INVERT of the positive integers, where p(S) = 1 - S^2
          1 0 1 4 11 28 72 188 493 1292 3383 8856 23184 60696 158905 416020 1089155 2851444 7465176 19544084      

2 A359108 ['Inv-CentralE', 'Inv:Rev-CentralE']
          a(n) = A128899(2*n, n) = 2*binomial(4*n - 1, 3*n) for n >= 1 and a(0) = 1
          1 -2 14 -110 910 -7752 67298 -592020 5259150 -47071640 423830264 -3834669566 34834267234

1 A000079 ['Std-DiagSum']
          Powers of 2: a(n) = 2^n
          1 0 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576     

1 A000567 ['Rev-PolyRow3']
          Octagonal numbers: n*(3*n-2). Also called star numbers
          1 8 21 40 65 96 133 176 225 280 341 408 481 560 645 736 833 936 1045 1160 1281 1408 1541 1680 1825      

1 A000957 ['Inv-DiagSum']
          Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n-set; also n
          1 0 1 -2 6 -18 57 -186 622 -2120 7338 -25724 91144 -325878 1174281 -4260282 15548694 -57048048

1 A001791 ['Inv-EvenSum']
          a(n) = binomial coefficient C(2n, n-1)
          1 0 1 -4 15 -56 210 -792 3003 -11440 43758 -167960 646646 -2496144 9657700 -37442160 145422675

1 A009545 ['Alt-DiagSum']
          Expansion of e.g.f. sin(x)*exp(x)
          1 0 -1 -2 -2 0 4 8 8 0 -16 -32 -32 0 64 128 128 0 -256 -512 -512 0 1024 2048 2048 0 -4096 -8192

1 A026005 ['Inv:Rev-CentralO']
          a(n) = T(4*n,n), where T = Catalan triangle (A008315)
          1 -4 27 -208 1700 -14364 123970 -1085760 9612108 -85795600 770755843 -6960408624 63127818572

1 A030267 ['Std-TransNat0']
          Compose the natural numbers with themselves, A(x) = B(B(x)) where B(x) = x/(1-x)^2 is the 
          0 1 4 14 46 145 444 1331 3926 11434 32960 94211 267384 754309 2116936 5914310 16458034 45638101

1 A045721 ['Rev-CentralO']
          a(n) = binomial(3*n+1,n)
          1 4 21 120 715 4368 27132 170544 1081575 6906900 44352165 286097760 1852482996 12033222880

1 A063524 ['Inv-TransNat0']
          Characteristic function of 1
          0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

1 A067336 ['Inv:Rev-NegHalf']
          a(0)=1, a(1)=2, a(n) = a(n-1)*9/2 - Catalan(n-1) where Catalan(n) = binomial(2n,n)/(n+1) =
          1 -2 8 -34 148 -652 2892 -12882 57540 -257500 1153888 -5175700 23231864 -104335376 468766292

1 A068875 ['Inv-TransSqrs']
          Expansion of (1 + x*C)*C, where C = (1 - (1 - 4*x)^(1/2))/(2*x) is the g.f. for Catalan nu
          0 1 2 -2 4 -10 28 -84 264 -858 2860 -9724 33592 -117572 416024 -1485800 5348880 -19389690 70715340      

1 A084103 ['Alt-PolyCol3']
          Expansion of (1+x)^3/(1+x^3)
          1 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0 -3 3 0     

1 A099459 ['Rev-PolyCol3']
          Expansion of 1/(1 - 7*x + 9*x^2)
          1 1 7 40 217 1159 6160 32689 173383 919480 4875913 25856071 137109280 727060321 3855438727

1 A122918 ['Alt-TransNat0']
          Expansion of (1+x)^2/(1+x+x^2)^2
          0 -1 0 2 2 -1 -4 -3 2 6 4 -3 -8 -5 4 10 6 -5 -12 -7 6 14 8 -7 -16 -9 8 18 10 -9 -20 -11 10 22 12        

1 A158943 ['Rev-DiagSum']
          INVERT transform of A027656: (1, 0, 2, 0, 3, 0, 4, 0, 5, ...)
          1 1 1 3 5 10 19 36 69 131 250 476 907 1728 3292 6272 11949 22765 43371 82629 157422 299915 571388       

1 A190816 ['Inv:Rev-PolyRow3']
          a(n) = 5*n^2 - 4*n + 1
          1 2 13 34 65 106 157 218 289 370 461 562 673 794 925 1066 1217 1378 1549 1730 1921 2122 2333 2554       

1 A194723 ['Inv-NegHalf']
          Number of ternary words either empty or beginning with the first character of the alphabet
          1 1 5 29 181 1181 7941 54573 381333 2699837 19319845 139480397 1014536117 7426790749 54669443141        

1 A281199 ['Rev-TransNat0']
          Number of n X 2 0..1 arrays with no element equal to more than one of its horizontal and a
          0 0 2 10 38 130 420 1308 3970 11822 34690 100610 289032 823800 2332418 6566290 18394910 51310978        

1 A290902 ['Std-PolyCol3']
          p-INVERT of the positive integers, where p(S) = 1 - 3*S
          1 3 15 72 345 1653 7920 37947 181815 871128 4173825 19997997 95816160 459082803 2199597855

1 A317637 ['Std-PolyRow3']
          a(n) = n*(n+1)*(n+3)
          0 8 30 72 140 240 378 560 792 1080 1430 1848 2340 2912 3570 4320 5168 6120 7182 8360 9660 11088

1 A329682 ['Rev-AltSum']
          Number of excursions of length n with Motzkin-steps forbidding all consecutive steps of le
          1 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0 1 -1 0     

1 A332057 ['Alt-AccSum']
          Partial sums (and absolute value of first differences) of A332056: if odd (resp. even) add
          1 -1 -3 -2 3 7 4 -5 -11 -6 7 15 8 -9 -19 -10 11 23 12 -13 -27 -14 15 31 16 -17 -35 -18 19 39 20 -21     

1 A371391 ['Inv:Rev-PolyCol3']
          Expansion of (1/x) * Series_Reversion( x * (1-x) / (1+2*x)^2 )
          1 1 -5 34 -269 2326 -21314 203428 -2000957 20142862 -206524790 2149261852 -22644243218 241061343004     

A related webpage is: https://peterluschny.github.io/tabl/CatalanInv.html .
2025/02/24
'''