from functools import cache
from _tabltypes import MakeTriangle


"""
Inverse of Bessel, unsigned version.

[0]  [1]
[1]  [0, 1]
[2]  [0, 1, 1]
[3]  [0, 0, 3,  1]
[4]  [0, 0, 3,  6,   1]
[5]  [0, 0, 0, 15,  10,   1]
[6]  [0, 0, 0, 15,  45,  15,    1]
[7]  [0, 0, 0,  0, 105, 105,   21,   1]
[8]  [0, 0, 0,  0, 105, 420,  210,  28,  1]
[9]  [0, 0, 0,  0,   0, 945, 1260, 378, 36, 1]
"""


@cache
def besselinv(n: int) -> list[int]:
    if n == 0:
        return [1]

    b = besselinv(n - 1)
    return [0] + [(2*k - n + 1)*b[k] + 
            b[k-1] for k in range(1, n)] + [1]


@MakeTriangle(besselinv, "BesselInv", ["A122848", "A104556", "A096713"], True)
def BesselInv(n: int, k: int) -> int:
    return besselinv(n)[k]


if __name__ == "__main__":
    from _tabltest import TablTest

    TablTest(BesselInv)


''' OEIS

The traits of the BesselInv triangle as represented in the OEIS.

|     | A-number| trait            | A-name                                
                                         |
|-----|---------|------------------|--------------------------------------------------------------------------------|
| 1   | A000007 | Std-ColLeft      | The characteristic function of {0}: a(n) = 0^n                                 |
| 2   | A000012 | Std-ColRight     | The simplest sequence of positive numbers: the all 1's sequence                |
| 3   | A000027 | Std-PolyRow1     | The positive integers. Also called the natural numbers, the whole numbers or t |
| 4   | A000085 | Std-RowSum       | Number of self-inverse permutations on n letters, also known as involutions; n |
| 5   | A000217 | Std-DiagRow1     | Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n   |
| 6   | A000704 | Rev-EvenSum      | Number of degree-n even permutations of order dividing 2                       |
| 7   | A000898 | Std-PolyCol2     | a(n) = 2*(a(n-1) + (n-1)*a(n-2)) for n >= 2 with a(0) = 1                      |
| 8   | A001093 | Inv-PolyRow3     | a(n) = n^3 + 1                        
                                         |
| 9   | A001147 | Std-CentralE     | Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)          |
| 10  | A001464 | Std-AltSum       | Expansion of e.g.f. exp(-x - (1/2)*x^2)                                        |
| 11  | A001465 | Rev-OddSum       | Number of degree-n odd permutations of order 2                                 |
| 12  | A001475 | Std-AccRevSum    | a(n) = a(n-1) + n * a(n-2), where a(1) = 1, a(2) = 2                           |
| 13  | A001515 | Inv-AltSum       | Bessel polynomial y_n(x) evaluated at x=1                                      |
| 14  | A001517 | Inv-NegHalf      | Bessel polynomials y_n(x) (see A001498) evaluated at 2                         |
| 15  | A001879 | Inv-DiagCol3     | a(n) = (2n+2)!/(n!*2^(n+1))           
                                         |
| 16  | A002119 | Inv-PosHalf      | Bessel polynomial y_n(-2)             
                                         |
| 17  | A002378 | Std-PolyRow2     | Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)             |
| 18  | A003215 | Inv:Rev-PolyRow3 | Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for he |
| 19  | A003436 | Inv-AccRevSum    | Number of inequivalent labeled Hamiltonian circuits on n-octahedron. Interlaci |
| 20  | A006199 | Inv:Rev-TransNat | Bessel polynomial {y_n}'(-1)          
                                         |
| 21  | A016777 | Rev-PolyRow3     | a(n) = 3*n + 1                        
                                         |
| 22  | A019590 | Std-DiagCol1     | Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution i |
| 23  | A025164 | Inv-OddSum       | a(n) = a(n-2) + (2n-1)a(n-1); a(0)=1, a(1)=1                                   |
| 24  | A036244 | Inv-EvenSum      | Denominator of continued fraction given by C(n) = [ 1; 3, 5, 7, ...(2n-1)]     |
| 25  | A047974 | Std-PosHalf      | a(n) = a(n-1) + 2*(n-1)*a(n-2)                                                 |
| 26  | A050534 | Std-DiagRow2     | Tritriangular numbers: a(n) = binomial(binomial(n,2),2) = n*(n+1)*(n-1)*(n-2)/ |
| 27  | A062267 | Alt-PolyCol2     | Row sums of (signed) triangle A060821 (Hermite polynomials)                    |
| 28  | A065923 | Inv:Rev-PolyCol3 | Bessel polynomial y_n(-3)             
                                         |
| 29  | A069834 | Std-RowGcd       | a(n) = n-th reduced triangular number: n*(n+1)/{2^k} where 2^k is the largest  |
| 30  | A085386 | Std-EvenSum      | E.g.f. cosh(x+x^2/2)                  
                                         |
| 31  | A104548 | Std-RevInv       | Triangle read by rows giving coefficients of Bessel polynomial p_n(x)          |
| 32  | A107104 | Inv:Rev-NegHalf  | Absolute row sums of triangle A107102, which is the matrix inverse of A100862  |
| 33  | A115327 | Rev-PolyCol3     | E.g.f.: exp(x + 3/2*x^2)              
                                         |
| 34  | A122848 | Std-Triangle     | Exponential Riordan array (1, x(1+x/2))                                        |
| 35  | A123023 | Std-ColMiddle    | a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                                            |
| 36  | A132062 | Std-Inv          | Sheffer triangle (1,1-sqrt(1-2*x)). Extended Bessel triangle A001497           |
| 37  | A133221 | Rev-ColMiddle    | A001147 with each term repeated                                                |
| 38  | A144299 | Std-Rev          | Triangle of Bessel numbers read by rows. Row n gives T(n,n), T(n,n-1), T(n,n-2 |
| 39  | A162970 | Rev-TransNat0    | Number of 2-cycles in all involutions of {1,2,...,n}                           |
| 40  | A174764 | Rev-TransSqrs    | Sum of the numerators for computing the second moment of the probability mass  |
| 41  | A189940 | Std-TransNat0    | Number of connected components in all simple labeled graphs with n nodes havin |
| 42  | A240440 | Std-DiagRow3     | Number of ways to place 3 points on a triangular grid of side n so that they a |
| 43  | A245066 | Inv:Rev-CentralO | Central terms of triangles A001497 and A001498                                 |
| 44  | A277614 | Rev-PolyDiag     | a(n) is the coefficient of x^n/n! in exp(x + n*x^2/2)                          |
| 45  | A278990 | Inv-RowSum       | Number of loopless linear chord diagrams with n chords                         |
| 46  | A293604 | Std-NegHalf      | Expansion of e.g.f.: exp(x * (1 - x))                                          |
| 47  | A335819 | Std-PolyCol3     | E.g.f.: exp((3/2) * x * (2 + x))                                               |
| 48  | A359762 | Rev-Poly         | Array read by ascending antidiagonals. T(n, k) = n!*[x^n] exp(x + (k/2) * x^2) |
| 49  | A366151 | Std-PolyRow3     | a(n) = T(n, 3), where T(n, k) = Sum_{i=0..n} i^k * binomial(n, i) * (1/2)^(n-k |
| 50  | A376872 | Inv-CentralE     | a(n) = n! * 2^(-n) * binomial(3*n - 1, 2*n) * binomial(2*n, n). Central terms  |


* Statistic about BesselInv:

        Triangles considered: ['Std', 'Alt', 'Rev', 'Inv', 'Inv:Rev'].     
        distinct A-numbers  : 50.
        all      A-numbers  : 129.
        missing  sequences  : 84.

[('missing', 84), ('A001147', 10), ('A000085', 6), ('A000012', 6), ('A240440', 5), ('A069834', 5), ('A050534', 5), ('A000217', 5), ('A000027', 5), ('A000007', 5), ('A144299', 4), ('A132062', 4), ('A001515', 4), ('A001464', 4), ('A278990', 3), ('A122848', 3), ('A104548', 3), ('A047974', 3), ('A019590', 3), ('A003436', 3), ('A002378', 3), ('A001475', 3), ('A376872', 2), ('A293604', 2), ('A123023', 2), ('A085386', 2), ('A062267', 2), ('A002119', 2), ('A001879', 2), ('A000898', 2), ('A366151', 1), ('A359762', 1), ('A335819', 1), ('A277614', 1), ('A245066', 1), ('A189940', 1), ('A174764', 1), ('A162970', 1), ('A133221', 1), ('A115327', 1), ('A107104', 1), ('A065923', 1), ('A036244', 1), ('A025164', 1), ('A016777', 1), ('A006199', 1), ('A003215', 1), ('A001517', 1), ('A001465', 1), ('A001093', 1), ('A000704', 1)]       

A related webpage is: https://peterluschny.github.io/tabl/BesselInv.html . 
2025/02/24

10 A001147 ['Std-CentralE', 'Alt-CentralE', 'Rev-CentralE', 'Rev-CentralO', 'Inv-RowMax', 'Inv-DiagCol1', 'Inv-DiagCol2', 'Inv:Rev-RowMax', 'Inv:Rev-DiagRow1', 'Inv:Rev-DiagRow2']
          Double factorial of odd numbers: a(n) = (2*n-1)!! = 1*3*5*...*(2*n-1)
          1 1 3 15 105 945 10395 135135 2027025 34459425 654729075 13749310575 316234143225 7905853580625

6 A000012 ['Std-ColRight', 'Rev-ColLeft', 'Rev-PolyRow1', 'Inv-ColRight', 'Inv:Rev-ColLeft', 'Inv:Rev-PolyRow1']
          The simplest sequence of positive numbers: the all 1's sequence  

          1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

6 A000085 ['Std-RowSum', 'Std-AbsSum', 'Alt-AltSum', 'Alt-AbsSum', 'Rev-RowSum', 'Rev-AbsSum']
          Number of self-inverse permutations on n letters, also known as involutions; number of sta
          1 1 2 4 10 26 76 232 764 2620 9496 35696 140152 568504 2390480 10349536 46206736 211799312

5 A000007 ['Std-ColLeft', 'Alt-ColLeft', 'Rev-ColRight', 'Inv-ColLeft', 'Inv:Rev-ColRight']
          The characteristic function of {0}: a(n) = 0^n                   

          1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

5 A000027 ['Std-PolyRow1', 'Alt-PolyRow1', 'Rev-PolyRow2', 'Inv-PolyRow1', 'Inv:Rev-PolyRow2']
          The positive integers. Also called the natural numbers, the whole numbers or the counting
          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35

5 A000217 ['Std-DiagRow1', 'Alt-DiagRow1', 'Rev-DiagCol1', 'Inv-DiagRow1', 'Inv:Rev-DiagCol1']
          Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n
          0 1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171 190 210 231 253 276 300 325 351 378 406

5 A050534 ['Std-DiagRow2', 'Alt-DiagRow2', 'Rev-DiagCol2', 'Inv-DiagRow2', 'Inv:Rev-DiagCol2']
          Tritriangular numbers: a(n) = binomial(binomial(n,2),2) = n*(n+1)*(n-1)*(n-2)/8
          0 0 3 15 45 105 210 378 630 990 1485 2145 3003 4095 5460 7140 9180 11628 14535 17955 21945 26565

5 A069834 ['Std-RowGcd', 'Alt-RowGcd', 'Rev-RowGcd', 'Inv-RowGcd', 'Inv:Rev-RowGcd']
          a(n) = n-th reduced triangular number: n*(n+1)/{2^k} where 2^k is the largest power of 2 t
          1 1 1 3 3 5 15 21 7 9 45 55 33 39 91 105 15 17 153 171 95 105 231 253 69 75 325 351 189 203 435 465

5 A240440 ['Std-DiagRow3', 'Alt-DiagRow3', 'Rev-DiagCol3', 'Inv-DiagRow3', 'Inv:Rev-DiagCol3']
          Number of ways to place 3 points on a triangular grid of side n so that they are not verti
          0 0 0 15 105 420 1260 3150 6930 13860 25740 45045 75075 120120 185640 278460 406980 581400 813960

4 A001464 ['Std-AltSum', 'Alt-RowSum', 'Rev-AltSum', 'Inv:Rev-DiagSum']    
          Expansion of e.g.f. exp(-x - (1/2)*x^2)                          

          1 -1 0 2 -2 -6 16 20 -132 -28 1216 -936 -12440 23672 138048 -469456 -1601264 9112560 18108928

4 A001515 ['Inv-AltSum', 'Inv-AbsSum', 'Inv:Rev-AltSum', 'Inv:Rev-AbsSum'] 
          Bessel polynomial y_n(x) evaluated at x=1                        

          1 -1 2 -7 37 -266 2431 -27007 353522 -5329837 90960751 -1733584106 36496226977 -841146804577

4 A132062 ['Std-Inv', 'Rev-InvRev', 'Inv-Triangle', 'Inv:Rev-Rev']
          Sheffer triangle (1,1-sqrt(1-2*x)). Extended Bessel triangle A001497
          1 0 1 0 -1 1 0 3 -3 1 0 -15 15 -6 1 0 105 -105 45 -10 1 0 -945 945 -420 105 -15 1 0 10395 -10395

4 A144299 ['Std-Rev', 'Alt-Rev', 'Rev-Triangle', 'Inv-RevInv']
          Triangle of Bessel numbers read by rows. Row n gives T(n,n), T(n,n-1), T(n,n-2), ..., T(n,
          1 1 0 1 1 0 1 3 0 0 1 6 3 0 0 1 10 15 0 0 0 1 15 45 15 0 0 0 1 21 105 105 0 0 0 0 1 28 210 420 105

3 A001475 ['Std-AccRevSum', 'Std-TransNat1', 'Rev-AccSum']
          a(n) = a(n-1) + n * a(n-2), where a(1) = 1, a(2) = 2             

          1 2 5 13 38 116 382 1310 4748 17848 70076 284252 1195240 5174768 23103368 105899656 498656912

3 A002378 ['Std-PolyRow2', 'Alt-PolyRow2', 'Inv-PolyRow2']
          Oblong (or promic, pronic, or heteromecic) numbers: a(n) = n*(n+1)
          0 2 6 12 20 30 42 56 72 90 110 132 156 182 210 240 272 306 342 380 420 462 506 552 600 650 702 756

3 A003436 ['Inv-AccRevSum', 'Inv-TransNat1', 'Inv:Rev-AccSum']
          Number of inequivalent labeled Hamiltonian circuits on n-octahedron. Interlacing chords jo
          1 2 1 1 -4 31 -293 3326 -44189 673471 -11588884 222304897 -4704612119 108897613826 -2737023412199

3 A019590 ['Std-DiagCol1', 'Alt-DiagCol1', 'Rev-DiagRow1']
          Fermat's Last Theorem: a(n) = 1 if x^n + y^n = z^n has a nontrivial solution in integers,
          1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

3 A047974 ['Std-PosHalf', 'Alt-NegHalf', 'Rev-PolyCol2']
          a(n) = a(n-1) + 2*(n-1)*a(n-2)                                   

          1 1 3 7 25 81 331 1303 5937 26785 133651 669351 3609673 19674097 113525595 664400311 4070168161

3 A104548 ['Std-RevInv', 'Inv-Rev', 'Inv:Rev-Triangle']
          Triangle read by rows giving coefficients of Bessel polynomial p_n(x)
          1 1 0 1 -1 0 1 -3 3 0 1 -6 15 -15 0 1 -10 45 -105 105 0 1 -15 105 -420 945 -945 0 1 -21 210 -1260

3 A122848 ['Std-Triangle', 'Alt-Triangle', 'Inv:Rev-InvRev']
          Exponential Riordan array (1, x(1+x/2))                          

          1 0 1 0 1 1 0 0 3 1 0 0 3 6 1 0 0 0 15 10 1 0 0 0 15 45 15 1 0 0 0 0 105 105 21 1 0 0 0 0 105 420

3 A278990 ['Inv-RowSum', 'Inv-TransNat0', 'Inv:Rev-RowSum']
          Number of loopless linear chord diagrams with n chords           

          1 1 0 1 -5 36 -329 3655 -47844 721315 -12310199 234615096 -4939227215 113836841041 -2850860253240

2 A000898 ['Std-PolyCol2', 'Rev-PosHalf']
          a(n) = 2*(a(n-1) + (n-1)*a(n-2)) for n >= 2 with a(0) = 1        

          1 2 6 20 76 312 1384 6512 32400 168992 921184 5222208 30710464 186753920 1171979904 7573069568

2 A001879 ['Inv-DiagCol3', 'Inv:Rev-DiagRow3']
          a(n) = (2n+2)!/(n!*2^(n+1))                                      

          1 -6 45 -420 4725 -62370 945945 -16216200 310134825 -6547290750 151242416325 -3794809718700

2 A002119 ['Inv-PosHalf', 'Inv:Rev-PolyCol2']
          Bessel polynomial y_n(-2)                                        

          1 1 -1 7 -71 1001 -18089 398959 -10391023 312129649 -10622799089 403978495031 -16977719590391

2 A062267 ['Alt-PolyCol2', 'Rev-NegHalf']
          Row sums of (signed) triangle A060821 (Hermite polynomials)      

          1 -2 2 4 -20 8 184 -464 -1648 10720 8224 -230848 280768 4978816 -17257600 -104891648 727511296

2 A085386 ['Std-EvenSum', 'Alt-EvenSum']
          E.g.f. cosh(x+x^2/2)                                             

          1 0 1 3 4 10 46 126 316 1296 5356 17380 63856 296088 1264264 4940040 22302736 110455936 507711376

2 A123023 ['Std-ColMiddle', 'Alt-ColMiddle']
          a(n) = (n-1)*a(n-2), a(0)=1, a(1)=0                              

          1 0 1 0 3 0 15 0 105 0 945 0 10395 0 135135 0 2027025 0 34459425 0 654729075 0 13749310575 0

2 A293604 ['Std-NegHalf', 'Alt-PosHalf']
          Expansion of e.g.f.: exp(x * (1 - x))                            

          1 1 -1 -5 1 41 31 -461 -895 6481 22591 -107029 -604031 1964665 17669471 -37341149 -567425279

2 A376872 ['Inv-CentralE', 'Inv:Rev-CentralE']
          a(n) = n! * 2^(-n) * binomial(3*n - 1, 2*n) * binomial(2*n, n). Central terms of the Besse
          1 -1 15 -420 17325 -945945 64324260 -5237832600 496939367925 -53835098191875 6557114959770375

1 A000704 ['Rev-EvenSum']
          Number of degree-n even permutations of order dividing 2         

          1 1 1 1 4 16 46 106 316 1324 5356 18316 63856 272416 1264264 5409496 22302736 101343376 507711376

1 A001093 ['Inv-PolyRow3']
          a(n) = n^3 + 1                                                   

          0 1 2 9 28 65 126 217 344 513 730 1001 1332 1729 2198 2745 3376 4097 4914 5833 6860 8001 9262 10649

1 A001465 ['Rev-OddSum']
          Number of degree-n odd permutations of order 2                   

          0 0 1 3 6 10 30 126 448 1296 4140 17380 76296 296088 1126216 4940040 23904000 110455936 489602448

1 A001517 ['Inv-NegHalf']
          Bessel polynomials y_n(x) (see A001498) evaluated at 2           

          1 1 3 19 193 2721 49171 1084483 28245729 848456353 28875761731 1098127402131 46150226651233

1 A003215 ['Inv:Rev-PolyRow3']
          Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for hexagonal latt
          1 1 7 19 37 61 91 127 169 217 271 331 397 469 547 631 721 817 919 1027 1141 1261 1387 1519 1657

1 A006199 ['Inv:Rev-TransNat0']
          Bessel polynomial {y_n}'(-1)                                     

          0 0 -1 3 -21 185 -2010 25914 -386407 6539679 -123823305 2593076255 -59505341676 1484818160748

1 A016777 ['Rev-PolyRow3']
          a(n) = 3*n + 1                                                   

          1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61 64 67 70 73 76 79 82 85 88 91 94 97 100

1 A025164 ['Inv-OddSum']
          a(n) = a(n-2) + (2n-1)a(n-1); a(0)=1, a(1)=1                     

          0 1 -1 4 -21 151 -1380 15331 -200683 3025576 -51635475 984099601 -20717727096 477491822809

1 A036244 ['Inv-EvenSum']
          Denominator of continued fraction given by C(n) = [ 1; 3, 5, 7, ...(2n-1)]
          1 0 1 -3 16 -115 1051 -11676 152839 -2304261 39325276 -749484505 15778499881 -363654981768

1 A065923 ['Inv:Rev-PolyCol3']
          Bessel polynomial y_n(-3)                                        

          1 1 -2 19 -287 6046 -163529 5402503 -210861146 9494154073 -484412718869 27621019129606

1 A107104 ['Inv:Rev-NegHalf']
          Absolute row sums of triangle A107102, which is the matrix inverse of A100862
          1 -2 6 -26 154 -1182 11254 -128522 1715802 -26251118 453132214 -8714516538 184817376154

1 A115327 ['Rev-PolyCol3']
          E.g.f.: exp(x + 3/2*x^2)                                         

          1 1 4 10 46 166 856 3844 21820 114076 703216 4125496 27331624 175849480 1241782816 8627460976

1 A133221 ['Rev-ColMiddle']
          A001147 with each term repeated                                  

          1 1 1 3 3 15 15 105 105 945 945 10395 10395 135135 135135 2027025 2027025 34459425 34459425

1 A162970 ['Rev-TransNat0']
          Number of 2-cycles in all involutions of {1,2,...,n}             

          0 0 1 3 12 40 150 546 2128 8352 34380 144100 626736 2784288 12753832 59692920 286857600 1407536896

1 A174764 ['Rev-TransSqrs']
          Sum of the numerators for computing the second moment of the probability mass function (PM
          0 0 1 3 18 70 330 1386 6328 28008 130140 603460 2895816 14024088 69786808 352043160 1817317440

1 A189940 ['Std-TransNat0']
          Number of connected components in all simple labeled graphs with n nodes having degrees at
          0 1 3 9 28 90 306 1078 3984 15228 60580 248556 1055088 4606264 20712888 95550120 452450176

1 A245066 ['Inv:Rev-CentralO']
          Central terms of triangles A001497 and A001498                   

          1 -3 45 -1260 51975 -2837835 192972780 -15713497800 1490818103775 -161505294575625

1 A277614 ['Rev-PolyDiag']
          a(n) is the coefficient of x^n/n! in exp(x + n*x^2/2)            

          1 1 3 10 73 426 4951 41308 658785 7149628 144963451 1937124696 47660873833 756536698360

1 A335819 ['Std-PolyCol3']
          E.g.f.: exp((3/2) * x * (2 + x))                                 

          1 3 12 54 270 1458 8424 51516 331452 2230740 15641424 113846472 857706408 6671592216 53465326560

1 A359762 ['Rev-Poly']
          Array read by ascending antidiagonals. T(n, k) = n!*[x^n] exp(x + (k/2) * x^2). A generali
          1 1 1 1 1 1 1 2 1 1 1 4 3 1 1 1 10 7 4 1 1 1 26 25 10 5 1 1 1 76 81 46 13 6 1 1 1 232 331 166 73 16
'''
