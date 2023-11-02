# Fibonacci
['A354267', 'A105809', 'A228074']

Fibonacci Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [1, 1, 1] |
| Row3 | [1, 2, 2, 1] |
| Row4 | [2, 3, 4, 3, 1] |
| Row5 | [3, 5, 7, 7, 4, 1] |
| Row6 | [5, 8, 12, 14, 11, 5, 1] |
| Row7 | [8, 13, 20, 26, 25, 16, 6, 1] |
| Row8 | [13, 21, 33, 46, 51, 41, 22, 7, 1] |
| Row9 | [21, 34, 54, 79, 97, 92, 63, 29, 8, 1] |

Fibonacci Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [1, 1, 1], [1, 2, 2, 1], [2, 3, 4, 3, 1], [3, 5, 7, 7, 4, 1], [5, 8, 12, 14, 11, 5, 1], [8, 13, 20, 26, 25, 16, 6, 1], [13, 21, 33, 46, 51, 41, 22, 7, 1], [21, 34, 54, 79, 97, 92, 63, 29, 8, 1]] |
| RevTabl    | [[1], [1, 0], [1, 1, 1], [1, 2, 2, 1], [1, 3, 4, 3, 2], [1, 4, 7, 7, 5, 3], [1, 5, 11, 14, 12, 8, 5], [1, 6, 16, 25, 26, 20, 13, 8], [1, 7, 22, 41, 51, 46, 33, 21, 13], [1, 8, 29, 63, 92, 97, 79, 54, 34, 21]] |
| AntiDiag   | [[1], [0], [1, 1], [1, 1], [2, 2, 1], [3, 3, 2], [5, 5, 4, 1], [8, 8, 7, 3], [13, 13, 12, 7, 1], [21, 21, 20, 14, 4]] |
| AccTabl    | [[1], [0, 1], [1, 2, 3], [1, 3, 5, 6], [2, 5, 9, 12, 13], [3, 8, 15, 22, 26, 27], [5, 13, 25, 39, 50, 55, 56], [8, 21, 41, 67, 92, 108, 114, 115], [13, 34, 67, 113, 164, 205, 227, 234, 235], [21, 55, 109, 188, 285, 377, 440, 469, 477, 478]] |
| RevAccTabl | [[1], [1, 0], [3, 2, 1], [6, 5, 3, 1], [13, 12, 9, 5, 2], [27, 26, 22, 15, 8, 3], [56, 55, 50, 39, 25, 13, 5], [115, 114, 108, 92, 67, 41, 21, 8], [235, 234, 227, 205, 164, 113, 67, 34, 13], [478, 477, 469, 440, 377, 285, 188, 109, 55, 21]] |
| AccRevTabl | [[1], [1, 1], [1, 2, 3], [1, 3, 5, 6], [1, 4, 8, 11, 13], [1, 5, 12, 19, 24, 27], [1, 6, 17, 31, 43, 51, 56], [1, 7, 23, 48, 74, 94, 107, 115], [1, 8, 30, 71, 122, 168, 201, 222, 235], [1, 9, 38, 101, 193, 290, 369, 423, 457, 478]] |

Fibonacci Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 6, 13, 27, 56, 115, 235, 478] |
| EvenSum      | [1, 0, 2, 3, 7, 14, 29, 59, 120, 243] |
| OddSum       | [0, 1, 1, 3, 6, 13, 27, 56, 115, 235] |
| AltSum       | [1, -1, 1, 0, 1, 1, 2, 3, 5, 8] |
| AccSum       | [1, 1, 6, 15, 41, 101, 243, 566, 1292, 2899] |
| AccRevSum    | [1, 2, 6, 15, 37, 88, 205, 469, 1058, 2359] |
| DiagSum      | [1, 0, 2, 2, 5, 8, 15, 26, 46, 80] |

Fibonacci Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 12, 420, 9240, 15600, 96282186, 131378824584] |
| RowGcd     | [1, 1, 1, 2, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 4, 7, 14, 26, 51, 97] |
| CentralE   | [1, 1, 4, 14, 51] |
| CentralO   | [0, 2, 7, 26, 97] |
| ColMiddle  | [1, 0, 1, 2, 4, 7, 14, 26, 51, 97] |
| ColLeft    | [1, 0, 1, 1, 2, 3, 5, 8, 13, 21] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 5, 19, 62, 185, 519, 1392, 3607, 9095] |
| TransNat0  | [0, 1, 3, 9, 24, 61, 149, 354, 823, 1881] |
| TransNat1  | [1, 2, 6, 15, 37, 88, 205, 469, 1058, 2359] |

Fibonacci Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow2 | [1, 2, 4, 7, 11, 16, 22, 29, 37, 46]|
| DiagRow3 | [1, 3, 7, 14, 25, 41, 63, 92, 129, 175]|
| DiagRow4 | [2, 5, 12, 26, 51, 92, 155, 247, 376, 551]|
| DiagRow5 | [3, 8, 20, 46, 97, 189, 344, 591, 967, 1518]|
| DiagRow6 | [5, 13, 33, 79, 176, 365, 709, 1300, 2267, 3785]|
| DiagRow7 | [8, 21, 54, 133, 309, 674, 1383, 2683, 4950, 8735]|
| DiagRow8 | [13, 34, 88, 221, 530, 1204, 2587, 5270, 10220, 18955]|
| DiagRow9 | [21, 55, 143, 364, 894, 2098, 4685, 9955, 20175, 39130]|

Fibonacci Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 1, 1, 2, 3, 5, 8, 13, 21] |
| DiagCol1 | [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] |
| DiagCol2 | [1, 2, 4, 7, 12, 20, 33, 54, 88, 143] |
| DiagCol3 | [1, 3, 7, 14, 26, 46, 79, 133, 221, 364] |
| DiagCol4 | [1, 4, 11, 25, 51, 97, 176, 309, 530, 894] |
| DiagCol5 | [1, 5, 16, 41, 92, 189, 365, 674, 1204, 2098] |
| DiagCol6 | [1, 6, 22, 63, 155, 344, 709, 1383, 2587, 4685] |
| DiagCol7 | [1, 7, 29, 92, 247, 591, 1300, 2683, 5270, 9955] |
| DiagCol8 | [1, 8, 37, 129, 376, 967, 2267, 4950, 10220, 20175] |
| DiagCol9 | [1, 9, 46, 175, 551, 1518, 3785, 8735, 18955, 39130] |

Fibonacci Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [1, 3, 7, 13, 21, 31, 43, 57, 73, 91] |
| PolyRow3 | [1, 6, 21, 52, 105, 186, 301, 456, 657, 910] |
| PolyRow4 | [2, 13, 64, 209, 526, 1117, 2108, 3649, 5914, 9101] |
| PolyRow5 | [3, 27, 193, 837, 2631, 6703, 14757, 29193, 53227, 91011] |
| PolyRow6 | [5, 56, 581, 3350, 13157, 40220, 103301, 233546, 479045, 910112] |
| PolyRow7 | [8, 115, 1746, 13403, 65788, 241323, 723110, 1868371, 4311408, 9101123] |
| PolyRow8 | [13, 235, 5243, 53617, 328945, 1447943, 5061775, 14946973, 38802677, 91011235] |
| PolyRow9 | [21, 478, 15737, 214476, 1644733, 8687666, 35432433, 119575792, 349224101, 910112358] |

Fibonacci Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 1, 1, 2, 3, 5, 8, 13, 21] |
| PolyCol1 | [1, 1, 3, 6, 13, 27, 56, 115, 235, 478] |
| PolyCol2 | [1, 2, 7, 21, 64, 193, 581, 1746, 5243, 15737] |
| PolyCol3 | [1, 3, 13, 52, 209, 837, 3350, 13403, 53617, 214476] |
| PolyCol4 | [1, 4, 21, 105, 526, 2631, 13157, 65788, 328945, 1644733] |
| PolyCol5 | [1, 5, 31, 186, 1117, 6703, 40220, 241323, 1447943, 8687666] |
| PolyCol6 | [1, 6, 43, 301, 2108, 14757, 103301, 723110, 5061775, 35432433] |
| PolyCol7 | [1, 7, 57, 456, 3649, 29193, 233546, 1868371, 14946973, 119575792] |
| PolyCol8 | [1, 8, 73, 657, 5914, 53227, 479045, 4311408, 38802677, 349224101] |
| PolyCol9 | [1, 9, 91, 910, 9101, 91011, 910112, 9101123, 91011235, 910112358] |

# Fibonacci:Rev
[]

Fibonacci:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 1, 1] |
| Row3 | [1, 2, 2, 1] |
| Row4 | [1, 3, 4, 3, 2] |
| Row5 | [1, 4, 7, 7, 5, 3] |
| Row6 | [1, 5, 11, 14, 12, 8, 5] |
| Row7 | [1, 6, 16, 25, 26, 20, 13, 8] |
| Row8 | [1, 7, 22, 41, 51, 46, 33, 21, 13] |
| Row9 | [1, 8, 29, 63, 92, 97, 79, 54, 34, 21] |

Fibonacci:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 1, 1], [1, 2, 2, 1], [1, 3, 4, 3, 2], [1, 4, 7, 7, 5, 3], [1, 5, 11, 14, 12, 8, 5], [1, 6, 16, 25, 26, 20, 13, 8], [1, 7, 22, 41, 51, 46, 33, 21, 13], [1, 8, 29, 63, 92, 97, 79, 54, 34, 21]] |
| RevTabl    | [[1], [0, 1], [1, 1, 1], [1, 2, 2, 1], [2, 3, 4, 3, 1], [3, 5, 7, 7, 4, 1], [5, 8, 12, 14, 11, 5, 1], [8, 13, 20, 26, 25, 16, 6, 1], [13, 21, 33, 46, 51, 41, 22, 7, 1], [21, 34, 54, 79, 97, 92, 63, 29, 8, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 1], [1, 2, 1], [1, 3, 2], [1, 4, 4, 1], [1, 5, 7, 3], [1, 6, 11, 7, 2], [1, 7, 16, 14, 5]] |
| AccTabl    | [[1], [1, 1], [1, 2, 3], [1, 3, 5, 6], [1, 4, 8, 11, 13], [1, 5, 12, 19, 24, 27], [1, 6, 17, 31, 43, 51, 56], [1, 7, 23, 48, 74, 94, 107, 115], [1, 8, 30, 71, 122, 168, 201, 222, 235], [1, 9, 38, 101, 193, 290, 369, 423, 457, 478]] |
| RevAccTabl | [[1], [1, 1], [3, 2, 1], [6, 5, 3, 1], [13, 11, 8, 4, 1], [27, 24, 19, 12, 5, 1], [56, 51, 43, 31, 17, 6, 1], [115, 107, 94, 74, 48, 23, 7, 1], [235, 222, 201, 168, 122, 71, 30, 8, 1], [478, 457, 423, 369, 290, 193, 101, 38, 9, 1]] |
| AccRevTabl | [[1], [0, 1], [1, 2, 3], [1, 3, 5, 6], [2, 5, 9, 12, 13], [3, 8, 15, 22, 26, 27], [5, 13, 25, 39, 50, 55, 56], [8, 21, 41, 67, 92, 108, 114, 115], [13, 34, 67, 113, 164, 205, 227, 234, 235], [21, 55, 109, 188, 285, 377, 440, 469, 477, 478]] |

Fibonacci:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 6, 13, 27, 56, 115, 235, 478] |
| EvenSum      | [1, 1, 2, 3, 7, 13, 29, 56, 120, 235] |
| OddSum       | [0, 0, 1, 3, 6, 14, 27, 59, 115, 243] |
| AltSum       | [1, 1, 1, 0, 1, -1, 2, -3, 5, -8] |
| AccSum       | [1, 2, 6, 15, 37, 88, 205, 469, 1058, 2359] |
| AccRevSum    | [1, 1, 6, 15, 41, 101, 243, 566, 1292, 2899] |
| DiagSum      | [1, 1, 1, 2, 4, 6, 10, 16, 27, 43] |

Fibonacci:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 12, 420, 9240, 15600, 96282186, 131378824584] |
| RowGcd     | [1, 1, 1, 2, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 4, 7, 14, 26, 51, 97] |
| CentralE   | [1, 1, 4, 14, 51] |
| CentralO   | [1, 2, 7, 25, 92] |
| ColMiddle  | [1, 1, 1, 2, 4, 7, 14, 25, 51, 92] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 1, 1, 2, 3, 5, 8, 13, 21] |
| TransSqrs  | [0, 0, 5, 19, 78, 250, 747, 2071, 5479, 13955] |
| TransNat0  | [0, 0, 3, 9, 28, 74, 187, 451, 1057, 2421] |
| TransNat1  | [1, 1, 6, 15, 41, 101, 243, 566, 1292, 2899] |

Fibonacci:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 1, 1, 2, 3, 5, 8, 13, 21]|
| DiagRow1 | [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]|
| DiagRow2 | [1, 2, 4, 7, 12, 20, 33, 54, 88, 143]|
| DiagRow3 | [1, 3, 7, 14, 26, 46, 79, 133, 221, 364]|
| DiagRow4 | [1, 4, 11, 25, 51, 97, 176, 309, 530, 894]|
| DiagRow5 | [1, 5, 16, 41, 92, 189, 365, 674, 1204, 2098]|
| DiagRow6 | [1, 6, 22, 63, 155, 344, 709, 1383, 2587, 4685]|
| DiagRow7 | [1, 7, 29, 92, 247, 591, 1300, 2683, 5270, 9955]|
| DiagRow8 | [1, 8, 37, 129, 376, 967, 2267, 4950, 10220, 20175]|
| DiagRow9 | [1, 9, 46, 175, 551, 1518, 3785, 8735, 18955, 39130]|

Fibonacci:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol2 | [1, 2, 4, 7, 11, 16, 22, 29, 37, 46] |
| DiagCol3 | [1, 3, 7, 14, 25, 41, 63, 92, 129, 175] |
| DiagCol4 | [2, 5, 12, 26, 51, 92, 155, 247, 376, 551] |
| DiagCol5 | [3, 8, 20, 46, 97, 189, 344, 591, 967, 1518] |
| DiagCol6 | [5, 13, 33, 79, 176, 365, 709, 1300, 2267, 3785] |
| DiagCol7 | [8, 21, 54, 133, 309, 674, 1383, 2683, 4950, 8735] |
| DiagCol8 | [13, 34, 88, 221, 530, 1204, 2587, 5270, 10220, 18955] |
| DiagCol9 | [21, 55, 143, 364, 894, 2098, 4685, 9955, 20175, 39130] |

Fibonacci:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 3, 7, 13, 21, 31, 43, 57, 73, 91] |
| PolyRow3 | [1, 6, 21, 52, 105, 186, 301, 456, 657, 910] |
| PolyRow4 | [1, 13, 79, 289, 781, 1741, 3403, 6049, 10009, 15661] |
| PolyRow5 | [1, 27, 269, 1399, 4929, 13571, 31597, 65199, 122849, 215659] |
| PolyRow6 | [1, 56, 935, 7054, 32837, 112676, 314491, 756890, 1629929, 3219472] |
| PolyRow7 | [1, 115, 3189, 34777, 213337, 910431, 3041245, 8525749, 20960817, 46543627] |
| PolyRow8 | [1, 235, 10847, 171913, 1394365, 7415711, 29686795, 97029997, 272533433, 680669875] |
| PolyRow9 | [1, 478, 36637, 845116, 9068977, 60119266, 288429133, 1099068832, 3526542721, 9906062662] |

Fibonacci:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 3, 6, 13, 27, 56, 115, 235, 478] |
| PolyCol2 | [1, 1, 7, 21, 79, 269, 935, 3189, 10847, 36637] |
| PolyCol3 | [1, 1, 13, 52, 289, 1399, 7054, 34777, 171913, 845116] |
| PolyCol4 | [1, 1, 21, 105, 781, 4929, 32837, 213337, 1394365, 9068977] |
| PolyCol5 | [1, 1, 31, 186, 1741, 13571, 112676, 910431, 7415711, 60119266] |
| PolyCol6 | [1, 1, 43, 301, 3403, 31597, 314491, 3041245, 29686795, 288429133] |
| PolyCol7 | [1, 1, 57, 456, 6049, 65199, 756890, 8525749, 97029997, 1099068832] |
| PolyCol8 | [1, 1, 73, 657, 10009, 122849, 1629929, 20960817, 272533433, 3526542721] |
| PolyCol9 | [1, 1, 91, 910, 15661, 215659, 3219472, 46543627, 680669875, 9906062662] |
