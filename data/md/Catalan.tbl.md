# Catalan
['A128899', 'A039598']

Catalan Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 2, 1] |
| Row3 | [0, 5, 4, 1] |
| Row4 | [0, 14, 14, 6, 1] |
| Row5 | [0, 42, 48, 27, 8, 1] |
| Row6 | [0, 132, 165, 110, 44, 10, 1] |
| Row7 | [0, 429, 572, 429, 208, 65, 12, 1] |
| Row8 | [0, 1430, 2002, 1638, 910, 350, 90, 14, 1] |
| Row9 | [0, 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1] |

Catalan Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 2, 1], [0, 5, 4, 1], [0, 14, 14, 6, 1], [0, 42, 48, 27, 8, 1], [0, 132, 165, 110, 44, 10, 1], [0, 429, 572, 429, 208, 65, 12, 1], [0, 1430, 2002, 1638, 910, 350, 90, 14, 1], [0, 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1]] |
| RevTabl    | [[1], [1, 0], [1, 2, 0], [1, 4, 5, 0], [1, 6, 14, 14, 0], [1, 8, 27, 48, 42, 0], [1, 10, 44, 110, 165, 132, 0], [1, 12, 65, 208, 429, 572, 429, 0], [1, 14, 90, 350, 910, 1638, 2002, 1430, 0], [1, 16, 119, 544, 1700, 3808, 6188, 7072, 4862, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 2], [0, 5, 1], [0, 14, 4], [0, 42, 14, 1], [0, 132, 48, 6], [0, 429, 165, 27, 1], [0, 1430, 572, 110, 8]] |
| AccTabl    | [[1], [0, 1], [0, 2, 3], [0, 5, 9, 10], [0, 14, 28, 34, 35], [0, 42, 90, 117, 125, 126], [0, 132, 297, 407, 451, 461, 462], [0, 429, 1001, 1430, 1638, 1703, 1715, 1716], [0, 1430, 3432, 5070, 5980, 6330, 6420, 6434, 6435], [0, 4862, 11934, 18122, 21930, 23630, 24174, 24293, 24309, 24310]] |
| RevAccTabl | [[1], [1, 0], [3, 2, 0], [10, 9, 5, 0], [35, 34, 28, 14, 0], [126, 125, 117, 90, 42, 0], [462, 461, 451, 407, 297, 132, 0], [1716, 1715, 1703, 1638, 1430, 1001, 429, 0], [6435, 6434, 6420, 6330, 5980, 5070, 3432, 1430, 0], [24310, 24309, 24293, 24174, 23630, 21930, 18122, 11934, 4862, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 3, 3], [1, 5, 10, 10], [1, 7, 21, 35, 35], [1, 9, 36, 84, 126, 126], [1, 11, 55, 165, 330, 462, 462], [1, 13, 78, 286, 715, 1287, 1716, 1716], [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435], [1, 17, 136, 680, 2380, 6188, 12376, 19448, 24310, 24310]] |
| DiffxTabl  | [[1], [0, 2], [0, 4, 3], [0, 10, 12, 4], [0, 28, 42, 24, 5], [0, 84, 144, 108, 40, 6], [0, 264, 495, 440, 220, 60, 7], [0, 858, 1716, 1716, 1040, 390, 84, 8], [0, 2860, 6006, 6552, 4550, 2100, 630, 112, 9], [0, 9724, 21216, 24752, 19040, 10200, 3808, 952, 144, 10]] |

Catalan Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| EvenSum      | [1, 0, 1, 4, 15, 56, 210, 792, 3003, 11440] |
| OddSum       | [0, 1, 2, 6, 20, 70, 252, 924, 3432, 12870] |
| AltSum       | [1, -1, -1, -2, -5, -14, -42, -132, -429, -1430] |
| AbsSum       | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| AccSum       | [1, 1, 5, 24, 111, 500, 2210, 9632, 41531, 177564] |
| AccRevSum    | [1, 2, 7, 26, 99, 382, 1486, 5812, 22819, 89846] |
| DiagSum      | [1, 0, 1, 2, 6, 18, 57, 186, 622, 2120] |

Catalan Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 20, 42, 3024, 660, 34320, 450450, 13613600] |
| RowGcd     | [1, 1, 2, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 2, 5, 14, 48, 165, 572, 2002, 7072] |
| CentralE   | [1, 2, 14, 110, 910] |
| CentralO   | [0, 5, 48, 429, 3808] |
| ColMiddle  | [1, 0, 2, 5, 14, 48, 110, 429, 910, 3808] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 1, 5, 28, 165, 1001, 6188, 38760, 245157, 1562275] |
| InvBinConv | [1, 1, -3, 4, 5, -39, 84, 8, -603, 1795] |
| TransSqrs  | [0, 1, 6, 30, 140, 630, 2772, 12012, 51480, 218790] |
| TransNat0  | [0, 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536] |
| TransNat1  | [1, 2, 7, 26, 99, 382, 1486, 5812, 22819, 89846] |
| PosHalf    | [1, 1, 5, 29, 181, 1181, 7941, 54573, 381333, 2699837] |
| NegHalf    | [1, 1, -3, 13, -67, 381, -2307, 14589, -95235, 636925] |

Catalan Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]|
| DiagRow2 | [0, 5, 14, 27, 44, 65, 90, 119, 152, 189]|
| DiagRow3 | [0, 14, 48, 110, 208, 350, 544, 798, 1120, 1518]|
| DiagRow4 | [0, 42, 165, 429, 910, 1700, 2907, 4655, 7084, 10350]|
| DiagRow5 | [0, 132, 572, 1638, 3808, 7752, 14364, 24794, 40480, 63180]|
| DiagRow6 | [0, 429, 2002, 6188, 15504, 33915, 67298, 123970, 215280, 356265]|
| DiagRow7 | [0, 1430, 7072, 23256, 62016, 144210, 303600, 592020, 1085760, 1893294]|
| DiagRow8 | [0, 4862, 25194, 87210, 245157, 600875, 1332045, 2731365, 5259150, 9612108]|
| DiagRow9 | [0, 16796, 90440, 326876, 961400, 2466750, 5722860, 12271350, 24682944, 47071640]|

Catalan Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796] |
| DiagCol2 | [1, 4, 14, 48, 165, 572, 2002, 7072, 25194, 90440] |
| DiagCol3 | [1, 6, 27, 110, 429, 1638, 6188, 23256, 87210, 326876] |
| DiagCol4 | [1, 8, 44, 208, 910, 3808, 15504, 62016, 245157, 961400] |
| DiagCol5 | [1, 10, 65, 350, 1700, 7752, 33915, 144210, 600875, 2466750] |
| DiagCol6 | [1, 12, 90, 544, 2907, 14364, 67298, 303600, 1332045, 5722860] |
| DiagCol7 | [1, 14, 119, 798, 4655, 24794, 123970, 592020, 2731365, 12271350] |
| DiagCol8 | [1, 16, 152, 1120, 7084, 40480, 215280, 1085760, 5259150, 24682944] |
| DiagCol9 | [1, 18, 189, 1518, 10350, 63180, 356265, 1893294, 9612108, 47071640] |

Catalan Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 3, 8, 15, 24, 35, 48, 63, 80, 99] |
| PolyRow3 | [0, 10, 34, 78, 148, 250, 390, 574, 808, 1098] |
| PolyRow4 | [0, 35, 148, 411, 920, 1795, 3180, 5243, 8176, 12195] |
| PolyRow5 | [0, 126, 652, 2178, 5736, 12910, 25956, 47922, 82768, 135486] |
| PolyRow6 | [0, 462, 2892, 11574, 35808, 92910, 211932, 438102, 837984, 1505358] |
| PolyRow7 | [0, 1716, 12882, 61596, 223668, 668820, 1730646, 4005372, 8484456, 16726068] |
| PolyRow8 | [0, 6435, 57540, 328083, 1397496, 4815075, 14133180, 36620115, 85904688, 185844771] |
| PolyRow9 | [0, 24310, 257500, 1748346, 8732920, 34667110, 115419540, 334811050, 869783536, 2064940470] |

Catalan Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| PolyCol2 | [1, 2, 8, 34, 148, 652, 2892, 12882, 57540, 257500] |
| PolyCol3 | [1, 3, 15, 78, 411, 2178, 11574, 61596, 328083, 1748346] |
| PolyCol4 | [1, 4, 24, 148, 920, 5736, 35808, 223668, 1397496, 8732920] |
| PolyCol5 | [1, 5, 35, 250, 1795, 12910, 92910, 668820, 4815075, 34667110] |
| PolyCol6 | [1, 6, 48, 390, 3180, 25956, 211932, 1730646, 14133180, 115419540] |
| PolyCol7 | [1, 7, 63, 574, 5243, 47922, 438102, 4005372, 36620115, 334811050] |
| PolyCol8 | [1, 8, 80, 808, 8176, 82768, 837984, 8484456, 85904688, 869783536] |
| PolyCol9 | [1, 9, 99, 1098, 12195, 135486, 1505358, 16726068, 185844771, 2064940470] |

# Catalan:Inv
[]

Catalan:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, -2, 1] |
| Row3 | [0, 3, -4, 1] |
| Row4 | [0, -4, 10, -6, 1] |
| Row5 | [0, 5, -20, 21, -8, 1] |
| Row6 | [0, -6, 35, -56, 36, -10, 1] |
| Row7 | [0, 7, -56, 126, -120, 55, -12, 1] |
| Row8 | [0, -8, 84, -252, 330, -220, 78, -14, 1] |
| Row9 | [0, 9, -120, 462, -792, 715, -364, 105, -16, 1] |

Catalan:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, -2, 1], [0, 3, -4, 1], [0, -4, 10, -6, 1], [0, 5, -20, 21, -8, 1], [0, -6, 35, -56, 36, -10, 1], [0, 7, -56, 126, -120, 55, -12, 1], [0, -8, 84, -252, 330, -220, 78, -14, 1], [0, 9, -120, 462, -792, 715, -364, 105, -16, 1]] |
| RevTabl    | [[1], [1, 0], [1, -2, 0], [1, -4, 3, 0], [1, -6, 10, -4, 0], [1, -8, 21, -20, 5, 0], [1, -10, 36, -56, 35, -6, 0], [1, -12, 55, -120, 126, -56, 7, 0], [1, -14, 78, -220, 330, -252, 84, -8, 0], [1, -16, 105, -364, 715, -792, 462, -120, 9, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, -2], [0, 3, 1], [0, -4, -4], [0, 5, 10, 1], [0, -6, -20, -6], [0, 7, 35, 21, 1], [0, -8, -56, -56, -8]] |
| AccTabl    | [[1], [0, 1], [0, -2, -1], [0, 3, -1, 0], [0, -4, 6, 0, 1], [0, 5, -15, 6, -2, -1], [0, -6, 29, -27, 9, -1, 0], [0, 7, -49, 77, -43, 12, 0, 1], [0, -8, 76, -176, 154, -66, 12, -2, -1], [0, 9, -111, 351, -441, 274, -90, 15, -1, 0]] |
| RevAccTabl | [[1], [1, 0], [-1, -2, 0], [0, -1, 3, 0], [1, 0, 6, -4, 0], [-1, -2, 6, -15, 5, 0], [0, -1, 9, -27, 29, -6, 0], [1, 0, 12, -43, 77, -49, 7, 0], [-1, -2, 12, -66, 154, -176, 76, -8, 0], [0, -1, 15, -90, 274, -441, 351, -111, 9, 0]] |
| AccRevTabl | [[1], [1, 1], [1, -1, -1], [1, -3, 0, 0], [1, -5, 5, 1, 1], [1, -7, 14, -6, -1, -1], [1, -9, 27, -29, 6, 0, 0], [1, -11, 44, -76, 50, -6, 1, 1], [1, -13, 65, -155, 175, -77, 7, -1, -1], [1, -15, 90, -274, 441, -351, 111, -9, 0, 0]] |
| DiffxTabl  | [[1], [0, 2], [0, -4, 3], [0, 6, -12, 4], [0, -8, 30, -24, 5], [0, 10, -60, 84, -40, 6], [0, -12, 105, -224, 180, -60, 7], [0, 14, -168, 504, -600, 330, -84, 8], [0, -16, 252, -1008, 1650, -1320, 546, -112, 9], [0, 18, -360, 1848, -3960, 4290, -2548, 840, -144, 10]] |

Catalan:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, -1, 0, 1, -1, 0, 1, -1, 0] |
| EvenSum      | [1, 0, 1, -4, 11, -28, 72, -188, 493, -1292] |
| OddSum       | [0, 1, -2, 4, -10, 27, -72, 189, -494, 1292] |
| AltSum       | [1, -1, 3, -8, 21, -55, 144, -377, 987, -2584] |
| AbsSum       | [1, 1, 3, 8, 21, 55, 144, 377, 987, 2584] |
| AccSum       | [1, 1, -3, 2, 3, -7, 4, 5, -11, 6] |
| AccRevSum    | [1, 2, -1, -2, 3, 0, -4, 4, 1, -6] |
| DiagSum      | [1, 0, 1, -2, 4, -8, 16, -32, 64, -128] |

Catalan:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 12, 60, 840, 2520, 27720, 360360, 720720] |
| RowGcd     | [1, 1, 2, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 2, 4, 10, 21, 56, 126, 330, 792] |
| CentralE   | [1, -2, 10, -56, 330] |
| CentralO   | [0, 3, -20, 126, -792] |
| ColMiddle  | [1, 0, -2, 3, 10, -20, -56, 126, 330, -792] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 1, -3, -2, 21, -4, -150, 155, 1029, -2072] |
| InvBinConv | [1, 1, 5, 22, 101, 476, 2282, 11075, 54245, 267592] |
| TransSqrs  | [0, 1, 2, -4, -2, 11, -8, -11, 26, -12] |
| TransNat0  | [0, 1, 0, -2, 2, 1, -4, 3, 2, -6] |
| TransNat1  | [1, 2, -1, -2, 3, 0, -4, 4, 1, -6] |
| PosHalf    | [1, 1, -3, 5, -3, -11, 45, -91, 93, 85] |
| NegHalf    | [1, 1, 5, 21, 85, 341, 1365, 5461, 21845, 87381] |

Catalan:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, -2, -4, -6, -8, -10, -12, -14, -16, -18]|
| DiagRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171]|
| DiagRow3 | [0, -4, -20, -56, -120, -220, -364, -560, -816, -1140]|
| DiagRow4 | [0, 5, 35, 126, 330, 715, 1365, 2380, 3876, 5985]|
| DiagRow5 | [0, -6, -56, -252, -792, -2002, -4368, -8568, -15504, -26334]|
| DiagRow6 | [0, 7, 84, 462, 1716, 5005, 12376, 27132, 54264, 100947]|
| DiagRow7 | [0, -8, -120, -792, -3432, -11440, -31824, -77520, -170544, -346104]|
| DiagRow8 | [0, 9, 165, 1287, 6435, 24310, 75582, 203490, 490314, 1081575]|
| DiagRow9 | [0, -10, -220, -2002, -11440, -48620, -167960, -497420, -1307504, -3124550]|

Catalan:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] |
| DiagCol2 | [1, -4, 10, -20, 35, -56, 84, -120, 165, -220] |
| DiagCol3 | [1, -6, 21, -56, 126, -252, 462, -792, 1287, -2002] |
| DiagCol4 | [1, -8, 36, -120, 330, -792, 1716, -3432, 6435, -11440] |
| DiagCol5 | [1, -10, 55, -220, 715, -2002, 5005, -11440, 24310, -48620] |
| DiagCol6 | [1, -12, 78, -364, 1365, -4368, 12376, -31824, 75582, -167960] |
| DiagCol7 | [1, -14, 105, -560, 2380, -8568, 27132, -77520, 203490, -497420] |
| DiagCol8 | [1, -16, 136, -816, 3876, -15504, 54264, -170544, 490314, -1307504] |
| DiagCol9 | [1, -18, 171, -1140, 5985, -26334, 100947, -346104, 1081575, -3124550] |

Catalan:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, -1, 0, 3, 8, 15, 24, 35, 48, 63] |
| PolyRow3 | [0, 0, -2, 0, 12, 40, 90, 168, 280, 432] |
| PolyRow4 | [0, 1, 0, -3, 16, 105, 336, 805, 1632, 2961] |
| PolyRow5 | [0, -1, 2, -3, 20, 275, 1254, 3857, 9512, 20295] |
| PolyRow6 | [0, 0, 0, 0, 24, 720, 4680, 18480, 55440, 139104] |
| PolyRow7 | [0, 1, -2, 3, 28, 1885, 17466, 88543, 323128, 953433] |
| PolyRow8 | [0, -1, 0, 3, 32, 4935, 65184, 424235, 1883328, 6534927] |
| PolyRow9 | [0, 0, 2, 0, 36, 12920, 243270, 2032632, 10976840, 44791056] |

Catalan:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, -1, 0, 1, -1, 0, 1, -1, 0] |
| PolyCol2 | [1, 2, 0, -2, 0, 2, 0, -2, 0, 2] |
| PolyCol3 | [1, 3, 3, 0, -3, -3, 0, 3, 3, 0] |
| PolyCol4 | [1, 4, 8, 12, 16, 20, 24, 28, 32, 36] |
| PolyCol5 | [1, 5, 15, 40, 105, 275, 720, 1885, 4935, 12920] |
| PolyCol6 | [1, 6, 24, 90, 336, 1254, 4680, 17466, 65184, 243270] |
| PolyCol7 | [1, 7, 35, 168, 805, 3857, 18480, 88543, 424235, 2032632] |
| PolyCol8 | [1, 8, 48, 280, 1632, 9512, 55440, 323128, 1883328, 10976840] |
| PolyCol9 | [1, 9, 63, 432, 2961, 20295, 139104, 953433, 6534927, 44791056] |

# Catalan:Rev
[]

Catalan:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 2, 0] |
| Row3 | [1, 4, 5, 0] |
| Row4 | [1, 6, 14, 14, 0] |
| Row5 | [1, 8, 27, 48, 42, 0] |
| Row6 | [1, 10, 44, 110, 165, 132, 0] |
| Row7 | [1, 12, 65, 208, 429, 572, 429, 0] |
| Row8 | [1, 14, 90, 350, 910, 1638, 2002, 1430, 0] |
| Row9 | [1, 16, 119, 544, 1700, 3808, 6188, 7072, 4862, 0] |

Catalan:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 2, 0], [1, 4, 5, 0], [1, 6, 14, 14, 0], [1, 8, 27, 48, 42, 0], [1, 10, 44, 110, 165, 132, 0], [1, 12, 65, 208, 429, 572, 429, 0], [1, 14, 90, 350, 910, 1638, 2002, 1430, 0], [1, 16, 119, 544, 1700, 3808, 6188, 7072, 4862, 0]] |
| RevTabl    | [[1], [0, 1], [0, 2, 1], [0, 5, 4, 1], [0, 14, 14, 6, 1], [0, 42, 48, 27, 8, 1], [0, 132, 165, 110, 44, 10, 1], [0, 429, 572, 429, 208, 65, 12, 1], [0, 1430, 2002, 1638, 910, 350, 90, 14, 1], [0, 4862, 7072, 6188, 3808, 1700, 544, 119, 16, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 2], [1, 4, 0], [1, 6, 5], [1, 8, 14, 0], [1, 10, 27, 14], [1, 12, 44, 48, 0], [1, 14, 65, 110, 42]] |
| AccTabl    | [[1], [1, 1], [1, 3, 3], [1, 5, 10, 10], [1, 7, 21, 35, 35], [1, 9, 36, 84, 126, 126], [1, 11, 55, 165, 330, 462, 462], [1, 13, 78, 286, 715, 1287, 1716, 1716], [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435], [1, 17, 136, 680, 2380, 6188, 12376, 19448, 24310, 24310]] |
| RevAccTabl | [[1], [1, 1], [3, 3, 1], [10, 10, 5, 1], [35, 35, 21, 7, 1], [126, 126, 84, 36, 9, 1], [462, 462, 330, 165, 55, 11, 1], [1716, 1716, 1287, 715, 286, 78, 13, 1], [6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1], [24310, 24310, 19448, 12376, 6188, 2380, 680, 136, 17, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 2, 3], [0, 5, 9, 10], [0, 14, 28, 34, 35], [0, 42, 90, 117, 125, 126], [0, 132, 297, 407, 451, 461, 462], [0, 429, 1001, 1430, 1638, 1703, 1715, 1716], [0, 1430, 3432, 5070, 5980, 6330, 6420, 6434, 6435], [0, 4862, 11934, 18122, 21930, 23630, 24174, 24293, 24309, 24310]] |
| DiffxTabl  | [[1], [1, 0], [1, 4, 0], [1, 8, 15, 0], [1, 12, 42, 56, 0], [1, 16, 81, 192, 210, 0], [1, 20, 132, 440, 825, 792, 0], [1, 24, 195, 832, 2145, 3432, 3003, 0], [1, 28, 270, 1400, 4550, 9828, 14014, 11440, 0], [1, 32, 357, 2176, 8500, 22848, 43316, 56576, 43758, 0]] |

Catalan:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| EvenSum      | [1, 1, 1, 6, 15, 70, 210, 924, 3003, 12870] |
| OddSum       | [0, 0, 2, 4, 20, 56, 252, 792, 3432, 11440] |
| AltSum       | [1, 1, -1, 2, -5, 14, -42, 132, -429, 1430] |
| AbsSum       | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| AccSum       | [1, 2, 7, 26, 99, 382, 1486, 5812, 22819, 89846] |
| AccRevSum    | [1, 1, 5, 24, 111, 500, 2210, 9632, 41531, 177564] |
| DiagSum      | [1, 1, 1, 3, 5, 12, 23, 52, 105, 232] |

Catalan:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 20, 42, 3024, 660, 34320, 450450, 13613600] |
| RowGcd     | [1, 1, 2, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 2, 5, 14, 48, 165, 572, 2002, 7072] |
| CentralE   | [1, 2, 14, 110, 910] |
| CentralO   | [1, 4, 27, 208, 1700] |
| ColMiddle  | [1, 1, 2, 4, 14, 27, 110, 208, 910, 1700] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 1, 5, 28, 165, 1001, 6188, 38760, 245157, 1562275] |
| InvBinConv | [1, -1, -3, -4, 5, 39, 84, -8, -603, -1795] |
| TransSqrs  | [0, 0, 2, 24, 188, 1220, 7116, 38752, 201176, 1008252] |
| TransNat0  | [0, 0, 2, 14, 76, 374, 1748, 7916, 35096, 153254] |
| TransNat1  | [1, 1, 5, 24, 111, 500, 2210, 9632, 41531, 177564] |
| PosHalf    | [1, 2, 8, 34, 148, 652, 2892, 12882, 57540, 257500] |
| NegHalf    | [1, -2, 0, -2, -4, -12, -36, -114, -372, -1244] |

Catalan:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]|
| DiagRow2 | [1, 4, 14, 48, 165, 572, 2002, 7072, 25194, 90440]|
| DiagRow3 | [1, 6, 27, 110, 429, 1638, 6188, 23256, 87210, 326876]|
| DiagRow4 | [1, 8, 44, 208, 910, 3808, 15504, 62016, 245157, 961400]|
| DiagRow5 | [1, 10, 65, 350, 1700, 7752, 33915, 144210, 600875, 2466750]|
| DiagRow6 | [1, 12, 90, 544, 2907, 14364, 67298, 303600, 1332045, 5722860]|
| DiagRow7 | [1, 14, 119, 798, 4655, 24794, 123970, 592020, 2731365, 12271350]|
| DiagRow8 | [1, 16, 152, 1120, 7084, 40480, 215280, 1085760, 5259150, 24682944]|
| DiagRow9 | [1, 18, 189, 1518, 10350, 63180, 356265, 1893294, 9612108, 47071640]|

Catalan:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] |
| DiagCol2 | [0, 5, 14, 27, 44, 65, 90, 119, 152, 189] |
| DiagCol3 | [0, 14, 48, 110, 208, 350, 544, 798, 1120, 1518] |
| DiagCol4 | [0, 42, 165, 429, 910, 1700, 2907, 4655, 7084, 10350] |
| DiagCol5 | [0, 132, 572, 1638, 3808, 7752, 14364, 24794, 40480, 63180] |
| DiagCol6 | [0, 429, 2002, 6188, 15504, 33915, 67298, 123970, 215280, 356265] |
| DiagCol7 | [0, 1430, 7072, 23256, 62016, 144210, 303600, 592020, 1085760, 1893294] |
| DiagCol8 | [0, 4862, 25194, 87210, 245157, 600875, 1332045, 2731365, 5259150, 9612108] |
| DiagCol9 | [0, 16796, 90440, 326876, 961400, 2466750, 5722860, 12271350, 24682944, 47071640] |

Catalan:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] |
| PolyRow3 | [1, 10, 29, 58, 97, 146, 205, 274, 353, 442] |
| PolyRow4 | [1, 35, 181, 523, 1145, 2131, 3565, 5531, 8113, 11395] |
| PolyRow5 | [1, 126, 1181, 4966, 14289, 32966, 65821, 118686, 198401, 312814] |
| PolyRow6 | [1, 462, 7941, 48838, 185193, 530526, 1265677, 2654646, 5060433, 8960878] |
| PolyRow7 | [1, 1716, 54573, 492724, 2467137, 8786436, 25066621, 61189668, 133071009, 264735892] |
| PolyRow8 | [1, 6435, 381333, 5068915, 33563481, 148733571, 507709165, 1443039123, 3581326065, 8006545891] |
| PolyRow9 | [1, 24310, 2699837, 52955950, 464221105, 2561439806, 10466643805, 34648845862, 98156060225, 246643289830] |

Catalan:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310] |
| PolyCol2 | [1, 1, 5, 29, 181, 1181, 7941, 54573, 381333, 2699837] |
| PolyCol3 | [1, 1, 7, 58, 523, 4966, 48838, 492724, 5068915, 52955950] |
| PolyCol4 | [1, 1, 9, 97, 1145, 14289, 185193, 2467137, 33563481, 464221105] |
| PolyCol5 | [1, 1, 11, 146, 2131, 32966, 530526, 8786436, 148733571, 2561439806] |
| PolyCol6 | [1, 1, 13, 205, 3565, 65821, 1265677, 25066621, 507709165, 10466643805] |
| PolyCol7 | [1, 1, 15, 274, 5531, 118686, 2654646, 61189668, 1443039123, 34648845862] |
| PolyCol8 | [1, 1, 17, 353, 8113, 198401, 5060433, 133071009, 3581326065, 98156060225] |
| PolyCol9 | [1, 1, 19, 442, 11395, 312814, 8960878, 264735892, 8006545891, 246643289830] |

# Catalan:Inv:Rev
[]

Catalan:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, -2, 0] |
| Row3 | [1, -4, 3, 0] |
| Row4 | [1, -6, 10, -4, 0] |
| Row5 | [1, -8, 21, -20, 5, 0] |
| Row6 | [1, -10, 36, -56, 35, -6, 0] |
| Row7 | [1, -12, 55, -120, 126, -56, 7, 0] |
| Row8 | [1, -14, 78, -220, 330, -252, 84, -8, 0] |
| Row9 | [1, -16, 105, -364, 715, -792, 462, -120, 9, 0] |

Catalan:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, -2, 0], [1, -4, 3, 0], [1, -6, 10, -4, 0], [1, -8, 21, -20, 5, 0], [1, -10, 36, -56, 35, -6, 0], [1, -12, 55, -120, 126, -56, 7, 0], [1, -14, 78, -220, 330, -252, 84, -8, 0], [1, -16, 105, -364, 715, -792, 462, -120, 9, 0]] |
| RevTabl    | [[1], [0, 1], [0, -2, 1], [0, 3, -4, 1], [0, -4, 10, -6, 1], [0, 5, -20, 21, -8, 1], [0, -6, 35, -56, 36, -10, 1], [0, 7, -56, 126, -120, 55, -12, 1], [0, -8, 84, -252, 330, -220, 78, -14, 1], [0, 9, -120, 462, -792, 715, -364, 105, -16, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, -2], [1, -4, 0], [1, -6, 3], [1, -8, 10, 0], [1, -10, 21, -4], [1, -12, 36, -20, 0], [1, -14, 55, -56, 5]] |
| AccTabl    | [[1], [1, 1], [1, -1, -1], [1, -3, 0, 0], [1, -5, 5, 1, 1], [1, -7, 14, -6, -1, -1], [1, -9, 27, -29, 6, 0, 0], [1, -11, 44, -76, 50, -6, 1, 1], [1, -13, 65, -155, 175, -77, 7, -1, -1], [1, -15, 90, -274, 441, -351, 111, -9, 0, 0]] |
| RevAccTabl | [[1], [1, 1], [-1, -1, 1], [0, 0, -3, 1], [1, 1, 5, -5, 1], [-1, -1, -6, 14, -7, 1], [0, 0, 6, -29, 27, -9, 1], [1, 1, -6, 50, -76, 44, -11, 1], [-1, -1, 7, -77, 175, -155, 65, -13, 1], [0, 0, -9, 111, -351, 441, -274, 90, -15, 1]] |
| AccRevTabl | [[1], [0, 1], [0, -2, -1], [0, 3, -1, 0], [0, -4, 6, 0, 1], [0, 5, -15, 6, -2, -1], [0, -6, 29, -27, 9, -1, 0], [0, 7, -49, 77, -43, 12, 0, 1], [0, -8, 76, -176, 154, -66, 12, -2, -1], [0, 9, -111, 351, -441, 274, -90, 15, -1, 0]] |
| DiffxTabl  | [[1], [1, 0], [1, -4, 0], [1, -8, 9, 0], [1, -12, 30, -16, 0], [1, -16, 63, -80, 25, 0], [1, -20, 108, -224, 175, -36, 0], [1, -24, 165, -480, 630, -336, 49, 0], [1, -28, 234, -880, 1650, -1512, 588, -64, 0], [1, -32, 315, -1456, 3575, -4752, 3234, -960, 81, 0]] |

Catalan:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, -1, 0, 1, -1, 0, 1, -1, 0] |
| EvenSum      | [1, 1, 1, 4, 11, 27, 72, 189, 493, 1292] |
| OddSum       | [0, 0, -2, -4, -10, -28, -72, -188, -494, -1292] |
| AltSum       | [1, 1, 3, 8, 21, 55, 144, 377, 987, 2584] |
| AbsSum       | [1, 1, 3, 8, 21, 55, 144, 377, 987, 2584] |
| AccSum       | [1, 2, -1, -2, 3, 0, -4, 4, 1, -6] |
| AccRevSum    | [1, 1, -3, 2, 3, -7, 4, 5, -11, 6] |
| DiagSum      | [1, 1, 1, -1, -3, -2, 3, 8, 5, -9] |

Catalan:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 12, 60, 840, 2520, 27720, 360360, 720720] |
| RowGcd     | [1, 1, 2, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 2, 4, 10, 21, 56, 126, 330, 792] |
| CentralE   | [1, -2, 10, -56, 330] |
| CentralO   | [1, -4, 21, -120, 715] |
| ColMiddle  | [1, 1, -2, -4, 10, 21, -56, -120, 330, 715] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 1, -3, -2, 21, -4, -150, 155, 1029, -2072] |
| InvBinConv | [1, -1, 5, -22, 101, -476, 2282, -11075, 54245, -267592] |
| TransSqrs  | [0, 0, -2, 8, -2, -24, 40, -4, -70, 96] |
| TransNat0  | [0, 0, -2, 2, 2, -6, 4, 4, -10, 6] |
| TransNat1  | [1, 1, -3, 2, 3, -7, 4, 5, -11, 6] |
| PosHalf    | [1, 2, 0, -2, 0, 2, 0, -2, 0, 2] |
| NegHalf    | [1, -2, 8, -30, 112, -418, 1560, -5822, 21728, -81090] |

Catalan:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]|
| DiagRow2 | [1, -4, 10, -20, 35, -56, 84, -120, 165, -220]|
| DiagRow3 | [1, -6, 21, -56, 126, -252, 462, -792, 1287, -2002]|
| DiagRow4 | [1, -8, 36, -120, 330, -792, 1716, -3432, 6435, -11440]|
| DiagRow5 | [1, -10, 55, -220, 715, -2002, 5005, -11440, 24310, -48620]|
| DiagRow6 | [1, -12, 78, -364, 1365, -4368, 12376, -31824, 75582, -167960]|
| DiagRow7 | [1, -14, 105, -560, 2380, -8568, 27132, -77520, 203490, -497420]|
| DiagRow8 | [1, -16, 136, -816, 3876, -15504, 54264, -170544, 490314, -1307504]|
| DiagRow9 | [1, -18, 171, -1140, 5985, -26334, 100947, -346104, 1081575, -3124550]|

Catalan:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, -2, -4, -6, -8, -10, -12, -14, -16, -18] |
| DiagCol2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171] |
| DiagCol3 | [0, -4, -20, -56, -120, -220, -364, -560, -816, -1140] |
| DiagCol4 | [0, 5, 35, 126, 330, 715, 1365, 2380, 3876, 5985] |
| DiagCol5 | [0, -6, -56, -252, -792, -2002, -4368, -8568, -15504, -26334] |
| DiagCol6 | [0, 7, 84, 462, 1716, 5005, 12376, 27132, 54264, 100947] |
| DiagCol7 | [0, -8, -120, -792, -3432, -11440, -31824, -77520, -170544, -346104] |
| DiagCol8 | [0, 9, 165, 1287, 6435, 24310, 75582, 203490, 490314, 1081575] |
| DiagCol9 | [0, -10, -220, -2002, -11440, -48620, -167960, -497420, -1307504, -3124550] |

Catalan:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, -1, -3, -5, -7, -9, -11, -13, -15, -17] |
| PolyRow3 | [1, 0, 5, 16, 33, 56, 85, 120, 161, 208] |
| PolyRow4 | [1, 1, -3, -35, -119, -279, -539, -923, -1455, -2159] |
| PolyRow5 | [1, -1, -11, 31, 305, 1111, 2869, 6119, 11521, 19855] |
| PolyRow6 | [1, 0, 45, 160, -231, -3024, -12155, -34320, -79695, -162656] |
| PolyRow7 | [1, 1, -91, -1079, -3263, -559, 30421, 146329, 458081, 1156897] |
| PolyRow8 | [1, -1, 93, 3955, 26537, 80631, 102949, -220597, -1770735, -6492113] |
| PolyRow9 | [1, 0, 85, -10064, -133551, -711704, -2227595, -4302360, -2756159, 16657264] |

Catalan:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, -1, 0, 1, -1, 0, 1, -1, 0] |
| PolyCol2 | [1, 1, -3, 5, -3, -11, 45, -91, 93, 85] |
| PolyCol3 | [1, 1, -5, 16, -35, 31, 160, -1079, 3955, -10064] |
| PolyCol4 | [1, 1, -7, 33, -119, 305, -231, -3263, 26537, -133551] |
| PolyCol5 | [1, 1, -9, 56, -279, 1111, -3024, -559, 80631, -711704] |
| PolyCol6 | [1, 1, -11, 85, -539, 2869, -12155, 30421, 102949, -2227595] |
| PolyCol7 | [1, 1, -13, 120, -923, 6119, -34320, 146329, -220597, -4302360] |
| PolyCol8 | [1, 1, -15, 161, -1455, 11521, -79695, 458081, -1770735, -2756159] |
| PolyCol9 | [1, 1, -17, 208, -2159, 19855, -162656, 1156897, -6492113, 16657264] |

