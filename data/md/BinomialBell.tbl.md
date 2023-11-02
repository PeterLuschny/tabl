# BinomialBell
['A056857', 'A056860']

BinomialBell Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 1] |
| Row3 | [0, 2, 2, 1] |
| Row4 | [0, 5, 6, 3, 1] |
| Row5 | [0, 15, 20, 12, 4, 1] |
| Row6 | [0, 52, 75, 50, 20, 5, 1] |
| Row7 | [0, 203, 312, 225, 100, 30, 6, 1] |
| Row8 | [0, 877, 1421, 1092, 525, 175, 42, 7, 1] |
| Row9 | [0, 4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1] |

BinomialBell Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 1], [0, 2, 2, 1], [0, 5, 6, 3, 1], [0, 15, 20, 12, 4, 1], [0, 52, 75, 50, 20, 5, 1], [0, 203, 312, 225, 100, 30, 6, 1], [0, 877, 1421, 1092, 525, 175, 42, 7, 1], [0, 4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1]] |
| RevTabl    | [[1], [1, 0], [1, 1, 0], [1, 2, 2, 0], [1, 3, 6, 5, 0], [1, 4, 12, 20, 15, 0], [1, 5, 20, 50, 75, 52, 0], [1, 6, 30, 100, 225, 312, 203, 0], [1, 7, 42, 175, 525, 1092, 1421, 877, 0], [1, 8, 56, 280, 1050, 2912, 5684, 7016, 4140, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 2, 1], [0, 5, 2], [0, 15, 6, 1], [0, 52, 20, 3], [0, 203, 75, 12, 1], [0, 877, 312, 50, 4]] |
| AccTabl    | [[1], [0, 1], [0, 1, 2], [0, 2, 4, 5], [0, 5, 11, 14, 15], [0, 15, 35, 47, 51, 52], [0, 52, 127, 177, 197, 202, 203], [0, 203, 515, 740, 840, 870, 876, 877], [0, 877, 2298, 3390, 3915, 4090, 4132, 4139, 4140], [0, 4140, 11156, 16840, 19752, 20802, 21082, 21138, 21146, 21147]] |
| RevAccTabl | [[1], [1, 0], [2, 1, 0], [5, 4, 2, 0], [15, 14, 11, 5, 0], [52, 51, 47, 35, 15, 0], [203, 202, 197, 177, 127, 52, 0], [877, 876, 870, 840, 740, 515, 203, 0], [4140, 4139, 4132, 4090, 3915, 3390, 2298, 877, 0], [21147, 21146, 21138, 21082, 20802, 19752, 16840, 11156, 4140, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 2, 2], [1, 3, 5, 5], [1, 4, 10, 15, 15], [1, 5, 17, 37, 52, 52], [1, 6, 26, 76, 151, 203, 203], [1, 7, 37, 137, 362, 674, 877, 877], [1, 8, 50, 225, 750, 1842, 3263, 4140, 4140], [1, 9, 65, 345, 1395, 4307, 9991, 17007, 21147, 21147]] |

BinomialBell Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147] |
| EvenSum      | [1, 0, 1, 2, 7, 24, 96, 418, 1989, 10216] |
| OddSum       | [0, 1, 1, 3, 8, 28, 107, 459, 2151, 10931] |
| AltSum       | [1, -1, 0, -1, -1, -4, -11, -41, -162, -715] |
| AccSum       | [1, 1, 3, 11, 45, 200, 958, 4921, 26981, 157203] |
| AccRevSum    | [1, 2, 5, 14, 45, 164, 666, 2972, 14419, 75414] |
| DiagSum      | [1, 0, 1, 1, 3, 7, 22, 75, 291, 1243] |

BinomialBell Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 30, 60, 3900, 4750200, 4860246300, 2682855957600] |
| RowGcd     | [1, 1, 1, 2, 1, 1, 1, 1, 1, 2] |
| RowMax     | [1, 1, 1, 2, 6, 20, 75, 312, 1421, 7016] |
| CentralE   | [1, 1, 6, 50, 525] |
| CentralO   | [0, 2, 20, 225, 2912] |
| ColMiddle  | [1, 0, 1, 2, 6, 20, 50, 225, 525, 2912] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 5, 19, 72, 292, 1283, 6091, 31083, 169619] |
| TransNat0  | [0, 1, 3, 9, 30, 112, 463, 2095, 10279, 54267] |
| TransNat1  | [1, 2, 5, 14, 45, 164, 666, 2972, 14419, 75414] |

BinomialBell Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]|
| DiagRow3 | [0, 5, 20, 50, 100, 175, 280, 420, 600, 825]|
| DiagRow4 | [0, 15, 75, 225, 525, 1050, 1890, 3150, 4950, 7425]|
| DiagRow5 | [0, 52, 312, 1092, 2912, 6552, 13104, 24024, 41184, 66924]|
| DiagRow6 | [0, 203, 1421, 5684, 17052, 42630, 93786, 187572, 348348, 609609]|
| DiagRow7 | [0, 877, 7016, 31572, 105240, 289410, 694584, 1504932, 3009864, 5643495]|
| DiagRow8 | [0, 4140, 37260, 186300, 683100, 2049300, 5328180, 12432420, 26640900, 53281800]|
| DiagRow9 | [0, 21147, 211470, 1163085, 4652340, 15120105, 42336294, 105840735, 241921680, 514083570]|

BinomialBell Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147] |
| DiagCol2 | [1, 2, 6, 20, 75, 312, 1421, 7016, 37260, 211470] |
| DiagCol3 | [1, 3, 12, 50, 225, 1092, 5684, 31572, 186300, 1163085] |
| DiagCol4 | [1, 4, 20, 100, 525, 2912, 17052, 105240, 683100, 4652340] |
| DiagCol5 | [1, 5, 30, 175, 1050, 6552, 42630, 289410, 2049300, 15120105] |
| DiagCol6 | [1, 6, 42, 280, 1890, 13104, 93786, 694584, 5328180, 42336294] |
| DiagCol7 | [1, 7, 56, 420, 3150, 24024, 187572, 1504932, 12432420, 105840735] |
| DiagCol8 | [1, 8, 72, 600, 4950, 41184, 348348, 3009864, 26640900, 241921680] |
| DiagCol9 | [1, 9, 90, 825, 7425, 66924, 609609, 5643495, 53281800, 514083570] |

BinomialBell Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] |
| PolyRow3 | [0, 5, 20, 51, 104, 185, 300, 455, 656, 909] |
| PolyRow4 | [0, 15, 74, 231, 564, 1175, 2190, 3759, 6056, 9279] |
| PolyRow5 | [0, 52, 302, 1116, 3196, 7700, 16362, 31612, 56696, 95796] |
| PolyRow6 | [0, 203, 1348, 5745, 18944, 52135, 125268, 270893, 538720, 1000899] |
| PolyRow7 | [0, 877, 6526, 31443, 117484, 365065, 983802, 2367631, 5199448, 10590309] |
| PolyRow8 | [0, 4140, 34014, 182442, 761988, 2645160, 7932210, 21122934, 51009192, 113545188] |
| PolyRow9 | [0, 21147, 189656, 1118817, 5164080, 19835975, 65698632, 192493581, 509002592, 1234300275] |

BinomialBell Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147] |
| PolyCol2 | [1, 2, 6, 20, 74, 302, 1348, 6526, 34014, 189656] |
| PolyCol3 | [1, 3, 12, 51, 231, 1116, 5745, 31443, 182442, 1118817] |
| PolyCol4 | [1, 4, 20, 104, 564, 3196, 18944, 117484, 761988, 5164080] |
| PolyCol5 | [1, 5, 30, 185, 1175, 7700, 52135, 365065, 2645160, 19835975] |
| PolyCol6 | [1, 6, 42, 300, 2190, 16362, 125268, 983802, 7932210, 65698632] |
| PolyCol7 | [1, 7, 56, 455, 3759, 31612, 270893, 2367631, 21122934, 192493581] |
| PolyCol8 | [1, 8, 72, 656, 6056, 56696, 538720, 5199448, 51009192, 509002592] |
| PolyCol9 | [1, 9, 90, 909, 9279, 95796, 1000899, 10590309, 113545188, 1234300275] |

# BinomialBell:Inv
[]

BinomialBell:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, -1, 1] |
| Row3 | [0, 0, -2, 1] |
| Row4 | [0, 1, 0, -3, 1] |
| Row5 | [0, 1, 4, 0, -4, 1] |
| Row6 | [0, -2, 5, 10, 0, -5, 1] |
| Row7 | [0, -9, -12, 15, 20, 0, -6, 1] |
| Row8 | [0, -9, -63, -42, 35, 35, 0, -7, 1] |
| Row9 | [0, 50, -72, -252, -112, 70, 56, 0, -8, 1] |

BinomialBell:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, -1, 1], [0, 0, -2, 1], [0, 1, 0, -3, 1], [0, 1, 4, 0, -4, 1], [0, -2, 5, 10, 0, -5, 1], [0, -9, -12, 15, 20, 0, -6, 1], [0, -9, -63, -42, 35, 35, 0, -7, 1], [0, 50, -72, -252, -112, 70, 56, 0, -8, 1]] |
| RevTabl    | [[1], [1, 0], [1, -1, 0], [1, -2, 0, 0], [1, -3, 0, 1, 0], [1, -4, 0, 4, 1, 0], [1, -5, 0, 10, 5, -2, 0], [1, -6, 0, 20, 15, -12, -9, 0], [1, -7, 0, 35, 35, -42, -63, -9, 0], [1, -8, 0, 56, 70, -112, -252, -72, 50, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, -1], [0, 0, 1], [0, 1, -2], [0, 1, 0, 1], [0, -2, 4, -3], [0, -9, 5, 0, 1], [0, -9, -12, 10, -4]] |
| AccTabl    | [[1], [0, 1], [0, -1, 0], [0, 0, -2, -1], [0, 1, 1, -2, -1], [0, 1, 5, 5, 1, 2], [0, -2, 3, 13, 13, 8, 9], [0, -9, -21, -6, 14, 14, 8, 9], [0, -9, -72, -114, -79, -44, -44, -51, -50], [0, 50, -22, -274, -386, -316, -260, -260, -268, -267]] |
| RevAccTabl | [[1], [1, 0], [0, -1, 0], [-1, -2, 0, 0], [-1, -2, 1, 1, 0], [2, 1, 5, 5, 1, 0], [9, 8, 13, 13, 3, -2, 0], [9, 8, 14, 14, -6, -21, -9, 0], [-50, -51, -44, -44, -79, -114, -72, -9, 0], [-267, -268, -260, -260, -316, -386, -274, -22, 50, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 0, 0], [1, -1, -1, -1], [1, -2, -2, -1, -1], [1, -3, -3, 1, 2, 2], [1, -4, -4, 6, 11, 9, 9], [1, -5, -5, 15, 30, 18, 9, 9], [1, -6, -6, 29, 64, 22, -41, -50, -50], [1, -7, -7, 49, 119, 7, -245, -317, -267, -267]] |

BinomialBell:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, -1, -1, 2, 9, 9, -50, -267] |
| EvenSum      | [1, 0, 1, -2, 1, 0, 6, 2, -27, -136] |
| OddSum       | [0, 1, -1, 1, -2, 2, 3, 7, -23, -131] |
| AltSum       | [1, -1, 2, -3, 3, -2, 3, -5, -4, -5] |
| AccSum       | [1, 1, -1, -3, -1, 14, 44, 9, -463, -2003] |
| AccRevSum    | [1, 2, 1, -2, -5, 0, 28, 72, -37, -934] |
| DiagSum      | [1, 0, 1, -1, 1, -1, 2, -1, -3, -15] |

BinomialBell:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 3, 4, 10, 180, 630, 25200] |
| RowGcd     | [1, 1, 1, 2, 3, 4, 1, 1, 1, 2] |
| RowMax     | [1, 1, 1, 2, 3, 4, 10, 20, 63, 252] |
| CentralE   | [1, -1, 0, 10, 35] |
| CentralO   | [0, 0, 4, 15, -112] |
| ColMiddle  | [1, 0, -1, 0, 0, 4, 10, 15, 35, -112] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 3, 1, -10, -22, 19, 231, 517, -963] |
| TransNat0  | [0, 1, 1, -1, -4, -2, 19, 63, 13, -667] |
| TransNat1  | [1, 2, 1, -2, -5, 0, 28, 72, -37, -934] |

BinomialBell:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]|
| DiagRow2 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow3 | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165]|
| DiagRow4 | [0, 1, 5, 15, 35, 70, 126, 210, 330, 495]|
| DiagRow5 | [0, -2, -12, -42, -112, -252, -504, -924, -1584, -2574]|
| DiagRow6 | [0, -9, -63, -252, -756, -1890, -4158, -8316, -15444, -27027]|
| DiagRow7 | [0, -9, -72, -324, -1080, -2970, -7128, -15444, -30888, -57915]|
| DiagRow8 | [0, 50, 450, 2250, 8250, 24750, 64350, 150150, 321750, 643500]|
| DiagRow9 | [0, 267, 2670, 14685, 58740, 190905, 534534, 1336335, 3054480, 6490770]|

BinomialBell:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, -1, 0, 1, 1, -2, -9, -9, 50, 267] |
| DiagCol2 | [1, -2, 0, 4, 5, -12, -63, -72, 450, 2670] |
| DiagCol3 | [1, -3, 0, 10, 15, -42, -252, -324, 2250, 14685] |
| DiagCol4 | [1, -4, 0, 20, 35, -112, -756, -1080, 8250, 58740] |
| DiagCol5 | [1, -5, 0, 35, 70, -252, -1890, -2970, 24750, 190905] |
| DiagCol6 | [1, -6, 0, 56, 126, -504, -4158, -7128, 64350, 534534] |
| DiagCol7 | [1, -7, 0, 84, 210, -924, -8316, -15444, 150150, 1336335] |
| DiagCol8 | [1, -8, 0, 120, 330, -1584, -15444, -30888, 321750, 3054480] |
| DiagCol9 | [1, -9, 0, 165, 495, -2574, -27027, -57915, 643500, 6490770] |

BinomialBell:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 0, 2, 6, 12, 20, 30, 42, 56, 72] |
| PolyRow3 | [0, -1, 0, 9, 32, 75, 144, 245, 384, 567] |
| PolyRow4 | [0, -1, -6, 3, 68, 255, 654, 1379, 2568, 4383] |
| PolyRow5 | [0, 2, -14, -42, 68, 730, 2742, 7406, 16648, 33138] |
| PolyRow6 | [0, 9, 0, -177, -312, 1365, 10104, 37275, 103728, 243873] |
| PolyRow7 | [0, 9, 118, -297, -2340, -1595, 28674, 170163, 613048, 1735425] |
| PolyRow8 | [0, -50, 434, 864, -8084, -31870, 26190, 654724, 3361784, 11826486] |
| PolyRow9 | [0, -267, 292, 8655, -6840, -181175, -404052, 1641507, 16381840, 76016925] |

BinomialBell:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 0, -1, -1, 2, 9, 9, -50, -267] |
| PolyCol2 | [1, 2, 2, 0, -6, -14, 0, 118, 434, 292] |
| PolyCol3 | [1, 3, 6, 9, 3, -42, -177, -297, 864, 8655] |
| PolyCol4 | [1, 4, 12, 32, 68, 68, -312, -2340, -8084, -6840] |
| PolyCol5 | [1, 5, 20, 75, 255, 730, 1365, -1595, -31870, -181175] |
| PolyCol6 | [1, 6, 30, 144, 654, 2742, 10104, 28674, 26190, -404052] |
| PolyCol7 | [1, 7, 42, 245, 1379, 7406, 37275, 170163, 654724, 1641507] |
| PolyCol8 | [1, 8, 56, 384, 2568, 16648, 103728, 613048, 3361784, 16381840] |
| PolyCol9 | [1, 9, 72, 567, 4383, 33138, 243873, 1735425, 11826486, 76016925] |

# BinomialBell:Rev
[]

BinomialBell:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 1, 0] |
| Row3 | [1, 2, 2, 0] |
| Row4 | [1, 3, 6, 5, 0] |
| Row5 | [1, 4, 12, 20, 15, 0] |
| Row6 | [1, 5, 20, 50, 75, 52, 0] |
| Row7 | [1, 6, 30, 100, 225, 312, 203, 0] |
| Row8 | [1, 7, 42, 175, 525, 1092, 1421, 877, 0] |
| Row9 | [1, 8, 56, 280, 1050, 2912, 5684, 7016, 4140, 0] |

BinomialBell:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 1, 0], [1, 2, 2, 0], [1, 3, 6, 5, 0], [1, 4, 12, 20, 15, 0], [1, 5, 20, 50, 75, 52, 0], [1, 6, 30, 100, 225, 312, 203, 0], [1, 7, 42, 175, 525, 1092, 1421, 877, 0], [1, 8, 56, 280, 1050, 2912, 5684, 7016, 4140, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 1], [0, 2, 2, 1], [0, 5, 6, 3, 1], [0, 15, 20, 12, 4, 1], [0, 52, 75, 50, 20, 5, 1], [0, 203, 312, 225, 100, 30, 6, 1], [0, 877, 1421, 1092, 525, 175, 42, 7, 1], [0, 4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 1], [1, 2, 0], [1, 3, 2], [1, 4, 6, 0], [1, 5, 12, 5], [1, 6, 20, 20, 0], [1, 7, 30, 50, 15]] |
| AccTabl    | [[1], [1, 1], [1, 2, 2], [1, 3, 5, 5], [1, 4, 10, 15, 15], [1, 5, 17, 37, 52, 52], [1, 6, 26, 76, 151, 203, 203], [1, 7, 37, 137, 362, 674, 877, 877], [1, 8, 50, 225, 750, 1842, 3263, 4140, 4140], [1, 9, 65, 345, 1395, 4307, 9991, 17007, 21147, 21147]] |
| RevAccTabl | [[1], [1, 1], [2, 2, 1], [5, 5, 3, 1], [15, 15, 10, 4, 1], [52, 52, 37, 17, 5, 1], [203, 203, 151, 76, 26, 6, 1], [877, 877, 674, 362, 137, 37, 7, 1], [4140, 4140, 3263, 1842, 750, 225, 50, 8, 1], [21147, 21147, 17007, 9991, 4307, 1395, 345, 65, 9, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 2], [0, 2, 4, 5], [0, 5, 11, 14, 15], [0, 15, 35, 47, 51, 52], [0, 52, 127, 177, 197, 202, 203], [0, 203, 515, 740, 840, 870, 876, 877], [0, 877, 2298, 3390, 3915, 4090, 4132, 4139, 4140], [0, 4140, 11156, 16840, 19752, 20802, 21082, 21138, 21146, 21147]] |

BinomialBell:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147] |
| EvenSum      | [1, 1, 1, 3, 7, 28, 96, 459, 1989, 10931] |
| OddSum       | [0, 0, 1, 2, 8, 24, 107, 418, 2151, 10216] |
| AltSum       | [1, 1, 0, 1, -1, 4, -11, 41, -162, 715] |
| AccSum       | [1, 2, 5, 14, 45, 164, 666, 2972, 14419, 75414] |
| AccRevSum    | [1, 1, 3, 11, 45, 200, 958, 4921, 26981, 157203] |
| DiagSum      | [1, 1, 1, 2, 3, 6, 11, 23, 47, 103] |

BinomialBell:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 30, 60, 3900, 4750200, 4860246300, 2682855957600] |
| RowGcd     | [1, 1, 1, 2, 1, 1, 1, 1, 1, 2] |
| RowMax     | [1, 1, 1, 2, 6, 20, 75, 312, 1421, 7016] |
| CentralE   | [1, 1, 6, 50, 525] |
| CentralO   | [1, 2, 12, 100, 1050] |
| ColMiddle  | [1, 1, 1, 2, 6, 12, 50, 100, 525, 1050] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 10, 72, 472, 3035, 19734, 131579, 905720] |
| TransNat0  | [0, 0, 1, 6, 30, 148, 755, 4044, 22841, 136056] |
| TransNat1  | [1, 1, 3, 11, 45, 200, 958, 4921, 26981, 157203] |

BinomialBell:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147]|
| DiagRow2 | [1, 2, 6, 20, 75, 312, 1421, 7016, 37260, 211470]|
| DiagRow3 | [1, 3, 12, 50, 225, 1092, 5684, 31572, 186300, 1163085]|
| DiagRow4 | [1, 4, 20, 100, 525, 2912, 17052, 105240, 683100, 4652340]|
| DiagRow5 | [1, 5, 30, 175, 1050, 6552, 42630, 289410, 2049300, 15120105]|
| DiagRow6 | [1, 6, 42, 280, 1890, 13104, 93786, 694584, 5328180, 42336294]|
| DiagRow7 | [1, 7, 56, 420, 3150, 24024, 187572, 1504932, 12432420, 105840735]|
| DiagRow8 | [1, 8, 72, 600, 4950, 41184, 348348, 3009864, 26640900, 241921680]|
| DiagRow9 | [1, 9, 90, 825, 7425, 66924, 609609, 5643495, 53281800, 514083570]|

BinomialBell:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] |
| DiagCol3 | [0, 5, 20, 50, 100, 175, 280, 420, 600, 825] |
| DiagCol4 | [0, 15, 75, 225, 525, 1050, 1890, 3150, 4950, 7425] |
| DiagCol5 | [0, 52, 312, 1092, 2912, 6552, 13104, 24024, 41184, 66924] |
| DiagCol6 | [0, 203, 1421, 5684, 17052, 42630, 93786, 187572, 348348, 609609] |
| DiagCol7 | [0, 877, 7016, 31572, 105240, 289410, 694584, 1504932, 3009864, 5643495] |
| DiagCol8 | [0, 4140, 37260, 186300, 683100, 2049300, 5328180, 12432420, 26640900, 53281800] |
| DiagCol9 | [0, 21147, 211470, 1163085, 4652340, 15120105, 42336294, 105840735, 241921680, 514083570] |

BinomialBell:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow3 | [1, 5, 13, 25, 41, 61, 85, 113, 145, 181] |
| PolyRow4 | [1, 15, 71, 199, 429, 791, 1315, 2031, 2969, 4159] |
| PolyRow5 | [1, 52, 457, 1876, 5329, 12196, 24217, 43492, 72481, 114004] |
| PolyRow6 | [1, 203, 3355, 20257, 75989, 216151, 513103, 1072205, 2038057, 3600739] |
| PolyRow7 | [1, 877, 27509, 245017, 1215481, 4300781, 12211597, 29702569, 64413617, 127857421] |
| PolyRow8 | [1, 4140, 248127, 3266914, 21453693, 94482336, 321013195, 909102342, 2249734329, 5017898548] |
| PolyRow9 | [1, 21147, 2434129, 47450923, 412820385, 2263917691, 9206900977, 30364532619, 85761187393, 214970494555] |

BinomialBell:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147] |
| PolyCol2 | [1, 1, 3, 13, 71, 457, 3355, 27509, 248127, 2434129] |
| PolyCol3 | [1, 1, 4, 25, 199, 1876, 20257, 245017, 3266914, 47450923] |
| PolyCol4 | [1, 1, 5, 41, 429, 5329, 75989, 1215481, 21453693, 412820385] |
| PolyCol5 | [1, 1, 6, 61, 791, 12196, 216151, 4300781, 94482336, 2263917691] |
| PolyCol6 | [1, 1, 7, 85, 1315, 24217, 513103, 12211597, 321013195, 9206900977] |
| PolyCol7 | [1, 1, 8, 113, 2031, 43492, 1072205, 29702569, 909102342, 30364532619] |
| PolyCol8 | [1, 1, 9, 145, 2969, 72481, 2038057, 64413617, 2249734329, 85761187393] |
| PolyCol9 | [1, 1, 10, 181, 4159, 114004, 3600739, 127857421, 5017898548, 214970494555] |

# BinomialBell:Inv:Rev
[]

BinomialBell:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, -1, 0] |
| Row3 | [1, -2, 0, 0] |
| Row4 | [1, -3, 0, 1, 0] |
| Row5 | [1, -4, 0, 4, 1, 0] |
| Row6 | [1, -5, 0, 10, 5, -2, 0] |
| Row7 | [1, -6, 0, 20, 15, -12, -9, 0] |
| Row8 | [1, -7, 0, 35, 35, -42, -63, -9, 0] |
| Row9 | [1, -8, 0, 56, 70, -112, -252, -72, 50, 0] |

BinomialBell:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, -1, 0], [1, -2, 0, 0], [1, -3, 0, 1, 0], [1, -4, 0, 4, 1, 0], [1, -5, 0, 10, 5, -2, 0], [1, -6, 0, 20, 15, -12, -9, 0], [1, -7, 0, 35, 35, -42, -63, -9, 0], [1, -8, 0, 56, 70, -112, -252, -72, 50, 0]] |
| RevTabl    | [[1], [0, 1], [0, -1, 1], [0, 0, -2, 1], [0, 1, 0, -3, 1], [0, 1, 4, 0, -4, 1], [0, -2, 5, 10, 0, -5, 1], [0, -9, -12, 15, 20, 0, -6, 1], [0, -9, -63, -42, 35, 35, 0, -7, 1], [0, 50, -72, -252, -112, 70, 56, 0, -8, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, -1], [1, -2, 0], [1, -3, 0], [1, -4, 0, 0], [1, -5, 0, 1], [1, -6, 0, 4, 0], [1, -7, 0, 10, 1]] |
| AccTabl    | [[1], [1, 1], [1, 0, 0], [1, -1, -1, -1], [1, -2, -2, -1, -1], [1, -3, -3, 1, 2, 2], [1, -4, -4, 6, 11, 9, 9], [1, -5, -5, 15, 30, 18, 9, 9], [1, -6, -6, 29, 64, 22, -41, -50, -50], [1, -7, -7, 49, 119, 7, -245, -317, -267, -267]] |
| RevAccTabl | [[1], [1, 1], [0, 0, 1], [-1, -1, -1, 1], [-1, -1, -2, -2, 1], [2, 2, 1, -3, -3, 1], [9, 9, 11, 6, -4, -4, 1], [9, 9, 18, 30, 15, -5, -5, 1], [-50, -50, -41, 22, 64, 29, -6, -6, 1], [-267, -267, -317, -245, 7, 119, 49, -7, -7, 1]] |
| AccRevTabl | [[1], [0, 1], [0, -1, 0], [0, 0, -2, -1], [0, 1, 1, -2, -1], [0, 1, 5, 5, 1, 2], [0, -2, 3, 13, 13, 8, 9], [0, -9, -21, -6, 14, 14, 8, 9], [0, -9, -72, -114, -79, -44, -44, -51, -50], [0, 50, -22, -274, -386, -316, -260, -260, -268, -267]] |

BinomialBell:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, -1, -1, 2, 9, 9, -50, -267] |
| EvenSum      | [1, 1, 1, 1, 1, 2, 6, 7, -27, -131] |
| OddSum       | [0, 0, -1, -2, -2, 0, 3, 2, -23, -136] |
| AltSum       | [1, 1, 2, 3, 3, 2, 3, 5, -4, 5] |
| AccSum       | [1, 2, 1, -2, -5, 0, 28, 72, -37, -934] |
| AccRevSum    | [1, 1, -1, -3, -1, 14, 44, 9, -463, -2003] |
| DiagSum      | [1, 1, 1, 0, -1, -2, -3, -3, -1, 5] |

BinomialBell:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 3, 4, 10, 180, 630, 25200] |
| RowGcd     | [1, 1, 1, 2, 3, 4, 1, 1, 1, 2] |
| RowMax     | [1, 1, 1, 2, 3, 4, 10, 20, 63, 252] |
| CentralE   | [1, -1, 0, 10, 35] |
| CentralO   | [1, -2, 0, 20, 70] |
| ColMiddle  | [1, 1, -1, -2, 0, 0, 10, 20, 35, 70] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, -1, -2, 6, 48, 115, -210, -2891, -10584] |
| TransNat0  | [0, 0, -1, -2, 0, 12, 35, 0, -413, -1736] |
| TransNat1  | [1, 1, -1, -3, -1, 14, 44, 9, -463, -2003] |

BinomialBell:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, -1, 0, 1, 1, -2, -9, -9, 50, 267]|
| DiagRow2 | [1, -2, 0, 4, 5, -12, -63, -72, 450, 2670]|
| DiagRow3 | [1, -3, 0, 10, 15, -42, -252, -324, 2250, 14685]|
| DiagRow4 | [1, -4, 0, 20, 35, -112, -756, -1080, 8250, 58740]|
| DiagRow5 | [1, -5, 0, 35, 70, -252, -1890, -2970, 24750, 190905]|
| DiagRow6 | [1, -6, 0, 56, 126, -504, -4158, -7128, 64350, 534534]|
| DiagRow7 | [1, -7, 0, 84, 210, -924, -8316, -15444, 150150, 1336335]|
| DiagRow8 | [1, -8, 0, 120, 330, -1584, -15444, -30888, 321750, 3054480]|
| DiagRow9 | [1, -9, 0, 165, 495, -2574, -27027, -57915, 643500, 6490770]|

BinomialBell:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, -1, -2, -3, -4, -5, -6, -7, -8, -9] |
| DiagCol2 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol3 | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165] |
| DiagCol4 | [0, 1, 5, 15, 35, 70, 126, 210, 330, 495] |
| DiagCol5 | [0, -2, -12, -42, -112, -252, -504, -924, -1584, -2574] |
| DiagCol6 | [0, -9, -63, -252, -756, -1890, -4158, -8316, -15444, -27027] |
| DiagCol7 | [0, -9, -72, -324, -1080, -2970, -7128, -15444, -30888, -57915] |
| DiagCol8 | [0, 50, 450, 2250, 8250, 24750, 64350, 150150, 321750, 643500] |
| DiagCol9 | [0, 267, 2670, 14685, 58740, 190905, 534534, 1336335, 3054480, 6490770] |

BinomialBell:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 0, -1, -2, -3, -4, -5, -6, -7, -8] |
| PolyRow3 | [1, -1, -3, -5, -7, -9, -11, -13, -15, -17] |
| PolyRow4 | [1, -1, 3, 19, 53, 111, 199, 323, 489, 703] |
| PolyRow5 | [1, 2, 41, 178, 497, 1106, 2137, 3746, 6113, 9442] |
| PolyRow6 | [1, 9, 87, 175, -147, -1899, -6941, -18213, -39975, -78047] |
| PolyRow7 | [1, 9, -571, -7739, -44055, -166279, -489491, -1217691, -2680879, -5378615] |
| PolyRow8 | [1, -50, -5701, -72056, -437339, -1792534, -5732465, -15433676, -36604471, -78752474] |
| PolyRow9 | [1, -267, -14575, -33179, 971745, 9669461, 51299953, 197602245, 618450881, 1667925685] |

BinomialBell:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 0, -1, -1, 2, 9, 9, -50, -267] |
| PolyCol2 | [1, 1, -1, -3, 3, 41, 87, -571, -5701, -14575] |
| PolyCol3 | [1, 1, -2, -5, 19, 178, 175, -7739, -72056, -33179] |
| PolyCol4 | [1, 1, -3, -7, 53, 497, -147, -44055, -437339, 971745] |
| PolyCol5 | [1, 1, -4, -9, 111, 1106, -1899, -166279, -1792534, 9669461] |
| PolyCol6 | [1, 1, -5, -11, 199, 2137, -6941, -489491, -5732465, 51299953] |
| PolyCol7 | [1, 1, -6, -13, 323, 3746, -18213, -1217691, -15433676, 197602245] |
| PolyCol8 | [1, 1, -7, -15, 489, 6113, -39975, -2680879, -36604471, 618450881] |
| PolyCol9 | [1, 1, -8, -17, 703, 9442, -78047, -5378615, -78752474, 1667925685] |
