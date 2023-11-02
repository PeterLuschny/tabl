# Composition
['A048004']

Composition Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 1] |
| Row3 | [0, 1, 2, 1] |
| Row4 | [0, 1, 4, 2, 1] |
| Row5 | [0, 1, 7, 5, 2, 1] |
| Row6 | [0, 1, 12, 11, 5, 2, 1] |
| Row7 | [0, 1, 20, 23, 12, 5, 2, 1] |
| Row8 | [0, 1, 33, 47, 27, 12, 5, 2, 1] |
| Row9 | [0, 1, 54, 94, 59, 28, 12, 5, 2, 1] |

Composition Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 1], [0, 1, 2, 1], [0, 1, 4, 2, 1], [0, 1, 7, 5, 2, 1], [0, 1, 12, 11, 5, 2, 1], [0, 1, 20, 23, 12, 5, 2, 1], [0, 1, 33, 47, 27, 12, 5, 2, 1], [0, 1, 54, 94, 59, 28, 12, 5, 2, 1]] |
| RevTabl    | [[1], [1, 0], [1, 1, 0], [1, 2, 1, 0], [1, 2, 4, 1, 0], [1, 2, 5, 7, 1, 0], [1, 2, 5, 11, 12, 1, 0], [1, 2, 5, 12, 23, 20, 1, 0], [1, 2, 5, 12, 27, 47, 33, 1, 0], [1, 2, 5, 12, 28, 59, 94, 54, 1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 1, 1], [0, 1, 2], [0, 1, 4, 1], [0, 1, 7, 2], [0, 1, 12, 5, 1], [0, 1, 20, 11, 2]] |
| AccTabl    | [[1], [0, 1], [0, 1, 2], [0, 1, 3, 4], [0, 1, 5, 7, 8], [0, 1, 8, 13, 15, 16], [0, 1, 13, 24, 29, 31, 32], [0, 1, 21, 44, 56, 61, 63, 64], [0, 1, 34, 81, 108, 120, 125, 127, 128], [0, 1, 55, 149, 208, 236, 248, 253, 255, 256]] |
| RevAccTabl | [[1], [1, 0], [2, 1, 0], [4, 3, 1, 0], [8, 7, 5, 1, 0], [16, 15, 13, 8, 1, 0], [32, 31, 29, 24, 13, 1, 0], [64, 63, 61, 56, 44, 21, 1, 0], [128, 127, 125, 120, 108, 81, 34, 1, 0], [256, 255, 253, 248, 236, 208, 149, 55, 1, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 2, 2], [1, 3, 4, 4], [1, 3, 7, 8, 8], [1, 3, 8, 15, 16, 16], [1, 3, 8, 19, 31, 32, 32], [1, 3, 8, 20, 43, 63, 64, 64], [1, 3, 8, 20, 47, 94, 127, 128, 128], [1, 3, 8, 20, 48, 107, 201, 255, 256, 256]] |

Composition Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 4, 8, 16, 32, 64, 128, 256] |
| EvenSum      | [1, 0, 1, 2, 5, 9, 18, 34, 66, 127] |
| OddSum       | [0, 1, 1, 2, 3, 7, 14, 30, 62, 129] |
| AltSum       | [1, -1, 0, 0, 2, 2, 4, 4, 4, -2] |
| AccSum       | [1, 1, 3, 8, 21, 53, 130, 310, 724, 1661] |
| AccRevSum    | [1, 2, 5, 12, 27, 59, 126, 266, 556, 1155] |
| DiagSum      | [1, 0, 1, 1, 2, 3, 6, 10, 19, 34] |

Composition Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 4, 70, 660, 1380, 279180, 10481940] |
| RowGcd     | [1, 1, 1, 2, 2, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 4, 7, 12, 23, 47, 94] |
| CentralE   | [1, 1, 4, 11, 27] |
| CentralO   | [0, 1, 7, 23, 59] |
| ColMiddle  | [1, 0, 1, 1, 4, 7, 11, 23, 27, 59] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 5, 18, 51, 131, 314, 726, 1630, 3593] |
| TransNat0  | [0, 1, 3, 8, 19, 43, 94, 202, 428, 899] |
| TransNat1  | [1, 2, 5, 12, 27, 59, 126, 266, 556, 1155] |

Composition Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 1, 2, 2, 2, 2, 2, 2, 2, 2]|
| DiagRow2 | [0, 1, 4, 5, 5, 5, 5, 5, 5, 5]|
| DiagRow3 | [0, 1, 7, 11, 12, 12, 12, 12, 12, 12]|
| DiagRow4 | [0, 1, 12, 23, 27, 28, 28, 28, 28, 28]|
| DiagRow5 | [0, 1, 20, 47, 59, 63, 64, 64, 64, 64]|
| DiagRow6 | [0, 1, 33, 94, 127, 139, 143, 144, 144, 144]|
| DiagRow7 | [0, 1, 54, 185, 269, 303, 315, 319, 320, 320]|
| DiagRow8 | [0, 1, 88, 360, 563, 653, 687, 699, 703, 704]|
| DiagRow9 | [0, 1, 143, 694, 1167, 1394, 1485, 1519, 1531, 1535]|

Composition Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [1, 2, 4, 7, 12, 20, 33, 54, 88, 143] |
| DiagCol3 | [1, 2, 5, 11, 23, 47, 94, 185, 360, 694] |
| DiagCol4 | [1, 2, 5, 12, 27, 59, 127, 269, 563, 1167] |
| DiagCol5 | [1, 2, 5, 12, 28, 63, 139, 303, 653, 1394] |
| DiagCol6 | [1, 2, 5, 12, 28, 64, 143, 315, 687, 1485] |
| DiagCol7 | [1, 2, 5, 12, 28, 64, 144, 319, 699, 1519] |
| DiagCol8 | [1, 2, 5, 12, 28, 64, 144, 320, 703, 1531] |
| DiagCol9 | [1, 2, 5, 12, 28, 64, 144, 320, 704, 1535] |

Composition Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] |
| PolyRow3 | [0, 4, 18, 48, 100, 180, 294, 448, 648, 900] |
| PolyRow4 | [0, 8, 50, 174, 452, 980, 1878, 3290, 5384, 8352] |
| PolyRow5 | [0, 16, 134, 606, 1972, 5180, 11706, 23674, 43976, 76392] |
| PolyRow6 | [0, 32, 346, 2028, 8324, 26680, 71502, 167636, 354568, 691344] |
| PolyRow7 | [0, 64, 874, 6636, 34564, 135880, 433374, 1180564, 2847496, 6238224] |
| PolyRow8 | [0, 128, 2158, 21252, 141524, 686080, 2612418, 8284388, 22812232, 56192544] |
| PolyRow9 | [0, 256, 5242, 67098, 574948, 3449980, 15712926, 58059862, 182614408, 505919448] |

Composition Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 2, 4, 8, 16, 32, 64, 128, 256] |
| PolyCol2 | [1, 2, 6, 18, 50, 134, 346, 874, 2158, 5242] |
| PolyCol3 | [1, 3, 12, 48, 174, 606, 2028, 6636, 21252, 67098] |
| PolyCol4 | [1, 4, 20, 100, 452, 1972, 8324, 34564, 141524, 574948] |
| PolyCol5 | [1, 5, 30, 180, 980, 5180, 26680, 135880, 686080, 3449980] |
| PolyCol6 | [1, 6, 42, 294, 1878, 11706, 71502, 433374, 2612418, 15712926] |
| PolyCol7 | [1, 7, 56, 448, 3290, 23674, 167636, 1180564, 8284388, 58059862] |
| PolyCol8 | [1, 8, 72, 648, 5384, 43976, 354568, 2847496, 22812232, 182614408] |
| PolyCol9 | [1, 9, 90, 900, 8352, 76392, 691344, 6238224, 56192544, 505919448] |

# Composition:Inv
[]

Composition:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, -1, 1] |
| Row3 | [0, 1, -2, 1] |
| Row4 | [0, 1, 0, -2, 1] |
| Row5 | [0, -1, 3, -1, -2, 1] |
| Row6 | [0, -3, 4, 1, -1, -2, 1] |
| Row7 | [0, -5, 3, 4, 0, -1, -2, 1] |
| Row8 | [0, -5, -1, 6, 2, 0, -1, -2, 1] |
| Row9 | [0, -1, -11, 8, 5, 1, 0, -1, -2, 1] |

Composition:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, -1, 1], [0, 1, -2, 1], [0, 1, 0, -2, 1], [0, -1, 3, -1, -2, 1], [0, -3, 4, 1, -1, -2, 1], [0, -5, 3, 4, 0, -1, -2, 1], [0, -5, -1, 6, 2, 0, -1, -2, 1], [0, -1, -11, 8, 5, 1, 0, -1, -2, 1]] |
| RevTabl    | [[1], [1, 0], [1, -1, 0], [1, -2, 1, 0], [1, -2, 0, 1, 0], [1, -2, -1, 3, -1, 0], [1, -2, -1, 1, 4, -3, 0], [1, -2, -1, 0, 4, 3, -5, 0], [1, -2, -1, 0, 2, 6, -1, -5, 0], [1, -2, -1, 0, 1, 5, 8, -11, -1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, -1], [0, 1, 1], [0, 1, -2], [0, -1, 0, 1], [0, -3, 3, -2], [0, -5, 4, -1, 1], [0, -5, 3, 1, -2]] |
| AccTabl    | [[1], [0, 1], [0, -1, 0], [0, 1, -1, 0], [0, 1, 1, -1, 0], [0, -1, 2, 1, -1, 0], [0, -3, 1, 2, 1, -1, 0], [0, -5, -2, 2, 2, 1, -1, 0], [0, -5, -6, 0, 2, 2, 1, -1, 0], [0, -1, -12, -4, 1, 2, 2, 1, -1, 0]] |
| RevAccTabl | [[1], [1, 0], [0, -1, 0], [0, -1, 1, 0], [0, -1, 1, 1, 0], [0, -1, 1, 2, -1, 0], [0, -1, 1, 2, 1, -3, 0], [0, -1, 1, 2, 2, -2, -5, 0], [0, -1, 1, 2, 2, 0, -6, -5, 0], [0, -1, 1, 2, 2, 1, -4, -12, -1, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 0, 0], [1, -1, 0, 0], [1, -1, -1, 0, 0], [1, -1, -2, 1, 0, 0], [1, -1, -2, -1, 3, 0, 0], [1, -1, -2, -2, 2, 5, 0, 0], [1, -1, -2, -2, 0, 6, 5, 0, 0], [1, -1, -2, -2, -1, 4, 12, 1, 0, 0]] |

Composition:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 0, 1, -2, 1, 1, 4, 1, 1, -8] |
| OddSum       | [0, 1, -1, 2, -1, -1, -4, -1, -1, 8] |
| AltSum       | [1, -1, 2, -4, 2, 2, 8, 2, 2, -16] |
| AccSum       | [1, 1, -1, 0, 1, 1, 0, -3, -7, -12] |
| AccRevSum    | [1, 2, 1, 0, -1, -1, 0, 3, 7, 12] |
| DiagSum      | [1, 0, 1, -1, 2, -1, 0, -2, -1, -3] |

Composition:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 2, 6, 12, 60, 30, 440] |
| RowGcd     | [1, 1, 1, 2, 2, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 2, 3, 4, 5, 6, 11] |
| CentralE   | [1, -1, 0, 1, 2] |
| CentralO   | [0, 1, 3, 4, 5] |
| ColMiddle  | [1, 0, -1, 1, 0, 3, 1, 4, 2, 5] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 3, 2, -1, -5, -8, -5, 7, 36] |
| TransNat0  | [0, 1, 1, 0, -1, -1, 0, 3, 7, 12] |
| TransNat1  | [1, 2, 1, 0, -1, -1, 0, 3, 7, 12] |

Composition:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, -1, -2, -2, -2, -2, -2, -2, -2, -2]|
| DiagRow2 | [0, 1, 0, -1, -1, -1, -1, -1, -1, -1]|
| DiagRow3 | [0, 1, 3, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow4 | [0, -1, 4, 4, 2, 1, 1, 1, 1, 1]|
| DiagRow5 | [0, -3, 3, 6, 5, 3, 2, 2, 2, 2]|
| DiagRow6 | [0, -5, -1, 8, 7, 6, 4, 3, 3, 3]|
| DiagRow7 | [0, -5, -11, 10, 10, 8, 7, 5, 4, 4]|
| DiagRow8 | [0, -1, -28, 9, 15, 11, 9, 8, 6, 5]|
| DiagRow9 | [0, 9, -57, 4, 22, 17, 12, 10, 9, 7]|

Composition:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, -1, 1, 1, -1, -3, -5, -5, -1, 9] |
| DiagCol2 | [1, -2, 0, 3, 4, 3, -1, -11, -28, -57] |
| DiagCol3 | [1, -2, -1, 1, 4, 6, 8, 10, 9, 4] |
| DiagCol4 | [1, -2, -1, 0, 2, 5, 7, 10, 15, 22] |
| DiagCol5 | [1, -2, -1, 0, 1, 3, 6, 8, 11, 17] |
| DiagCol6 | [1, -2, -1, 0, 1, 2, 4, 7, 9, 12] |
| DiagCol7 | [1, -2, -1, 0, 1, 2, 3, 5, 8, 10] |
| DiagCol8 | [1, -2, -1, 0, 1, 2, 3, 4, 6, 9] |
| DiagCol9 | [1, -2, -1, 0, 1, 2, 3, 4, 5, 7] |

Composition:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 0, 2, 6, 12, 20, 30, 42, 56, 72] |
| PolyRow3 | [0, 0, 2, 12, 36, 80, 150, 252, 392, 576] |
| PolyRow4 | [0, 0, 2, 30, 132, 380, 870, 1722, 3080, 5112] |
| PolyRow5 | [0, 0, 2, 78, 492, 1820, 5070, 11802, 24248, 45432] |
| PolyRow6 | [0, 0, 2, 216, 1908, 8960, 30150, 82152, 193256, 407808] |
| PolyRow7 | [0, 0, 2, 606, 7452, 44300, 179790, 572922, 1542296, 3664152] |
| PolyRow8 | [0, 0, 2, 1758, 29532, 220700, 1076910, 4006842, 12331928, 32966712] |
| PolyRow9 | [0, 0, 2, 5136, 117324, 1100720, 6454110, 28031472, 98622776, 296640864] |

Composition:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 2, 2, 2, 2, 2, 2, 2, 2, 2] |
| PolyCol3 | [1, 3, 6, 12, 30, 78, 216, 606, 1758, 5136] |
| PolyCol4 | [1, 4, 12, 36, 132, 492, 1908, 7452, 29532, 117324] |
| PolyCol5 | [1, 5, 20, 80, 380, 1820, 8960, 44300, 220700, 1100720] |
| PolyCol6 | [1, 6, 30, 150, 870, 5070, 30150, 179790, 1076910, 6454110] |
| PolyCol7 | [1, 7, 42, 252, 1722, 11802, 82152, 572922, 4006842, 28031472] |
| PolyCol8 | [1, 8, 56, 392, 3080, 24248, 193256, 1542296, 12331928, 98622776] |
| PolyCol9 | [1, 9, 72, 576, 5112, 45432, 407808, 3664152, 32966712, 296640864] |

# Composition:Rev
[]

Composition:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 1, 0] |
| Row3 | [1, 2, 1, 0] |
| Row4 | [1, 2, 4, 1, 0] |
| Row5 | [1, 2, 5, 7, 1, 0] |
| Row6 | [1, 2, 5, 11, 12, 1, 0] |
| Row7 | [1, 2, 5, 12, 23, 20, 1, 0] |
| Row8 | [1, 2, 5, 12, 27, 47, 33, 1, 0] |
| Row9 | [1, 2, 5, 12, 28, 59, 94, 54, 1, 0] |

Composition:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 1, 0], [1, 2, 1, 0], [1, 2, 4, 1, 0], [1, 2, 5, 7, 1, 0], [1, 2, 5, 11, 12, 1, 0], [1, 2, 5, 12, 23, 20, 1, 0], [1, 2, 5, 12, 27, 47, 33, 1, 0], [1, 2, 5, 12, 28, 59, 94, 54, 1, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 1], [0, 1, 2, 1], [0, 1, 4, 2, 1], [0, 1, 7, 5, 2, 1], [0, 1, 12, 11, 5, 2, 1], [0, 1, 20, 23, 12, 5, 2, 1], [0, 1, 33, 47, 27, 12, 5, 2, 1], [0, 1, 54, 94, 59, 28, 12, 5, 2, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 1], [1, 2, 0], [1, 2, 1], [1, 2, 4, 0], [1, 2, 5, 1], [1, 2, 5, 7, 0], [1, 2, 5, 11, 1]] |
| AccTabl    | [[1], [1, 1], [1, 2, 2], [1, 3, 4, 4], [1, 3, 7, 8, 8], [1, 3, 8, 15, 16, 16], [1, 3, 8, 19, 31, 32, 32], [1, 3, 8, 20, 43, 63, 64, 64], [1, 3, 8, 20, 47, 94, 127, 128, 128], [1, 3, 8, 20, 48, 107, 201, 255, 256, 256]] |
| RevAccTabl | [[1], [1, 1], [2, 2, 1], [4, 4, 3, 1], [8, 8, 7, 3, 1], [16, 16, 15, 8, 3, 1], [32, 32, 31, 19, 8, 3, 1], [64, 64, 63, 43, 20, 8, 3, 1], [128, 128, 127, 94, 47, 20, 8, 3, 1], [256, 256, 255, 201, 107, 48, 20, 8, 3, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 2], [0, 1, 3, 4], [0, 1, 5, 7, 8], [0, 1, 8, 13, 15, 16], [0, 1, 13, 24, 29, 31, 32], [0, 1, 21, 44, 56, 61, 63, 64], [0, 1, 34, 81, 108, 120, 125, 127, 128], [0, 1, 55, 149, 208, 236, 248, 253, 255, 256]] |

Composition:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 4, 8, 16, 32, 64, 128, 256] |
| EvenSum      | [1, 1, 1, 2, 5, 7, 18, 30, 66, 129] |
| OddSum       | [0, 0, 1, 2, 3, 9, 14, 34, 62, 127] |
| AltSum       | [1, 1, 0, 0, 2, -2, 4, -4, 4, 2] |
| AccSum       | [1, 2, 5, 12, 27, 59, 126, 266, 556, 1155] |
| AccRevSum    | [1, 1, 3, 8, 21, 53, 130, 310, 724, 1661] |
| DiagSum      | [1, 1, 1, 2, 3, 4, 7, 9, 15, 20] |

Composition:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 4, 70, 660, 1380, 279180, 10481940] |
| RowGcd     | [1, 1, 1, 2, 2, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 4, 7, 12, 23, 47, 94] |
| CentralE   | [1, 1, 4, 11, 27] |
| CentralO   | [1, 2, 5, 12, 28] |
| ColMiddle  | [1, 1, 1, 2, 4, 5, 11, 12, 27, 28] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 6, 27, 101, 338, 1034, 2974, 8147] |
| TransNat0  | [0, 0, 1, 4, 13, 37, 98, 246, 596, 1405] |
| TransNat1  | [1, 1, 3, 8, 21, 53, 130, 310, 724, 1661] |

Composition:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [1, 2, 4, 7, 12, 20, 33, 54, 88, 143]|
| DiagRow3 | [1, 2, 5, 11, 23, 47, 94, 185, 360, 694]|
| DiagRow4 | [1, 2, 5, 12, 27, 59, 127, 269, 563, 1167]|
| DiagRow5 | [1, 2, 5, 12, 28, 63, 139, 303, 653, 1394]|
| DiagRow6 | [1, 2, 5, 12, 28, 64, 143, 315, 687, 1485]|
| DiagRow7 | [1, 2, 5, 12, 28, 64, 144, 319, 699, 1519]|
| DiagRow8 | [1, 2, 5, 12, 28, 64, 144, 320, 703, 1531]|
| DiagRow9 | [1, 2, 5, 12, 28, 64, 144, 320, 704, 1535]|

Composition:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 1, 2, 2, 2, 2, 2, 2, 2, 2] |
| DiagCol2 | [0, 1, 4, 5, 5, 5, 5, 5, 5, 5] |
| DiagCol3 | [0, 1, 7, 11, 12, 12, 12, 12, 12, 12] |
| DiagCol4 | [0, 1, 12, 23, 27, 28, 28, 28, 28, 28] |
| DiagCol5 | [0, 1, 20, 47, 59, 63, 64, 64, 64, 64] |
| DiagCol6 | [0, 1, 33, 94, 127, 139, 143, 144, 144, 144] |
| DiagCol7 | [0, 1, 54, 185, 269, 303, 315, 319, 320, 320] |
| DiagCol8 | [0, 1, 88, 360, 563, 653, 687, 699, 703, 704] |
| DiagCol9 | [0, 1, 143, 694, 1167, 1394, 1485, 1519, 1531, 1535] |

Composition:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow3 | [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] |
| PolyRow4 | [1, 8, 29, 70, 137, 236, 373, 554, 785, 1072] |
| PolyRow5 | [1, 16, 97, 322, 793, 1636, 3001, 5062, 8017, 12088] |
| PolyRow6 | [1, 32, 337, 1564, 4889, 12136, 25897, 49652, 87889, 146224] |
| PolyRow7 | [1, 64, 1193, 7828, 31321, 94136, 234769, 513388, 1018193, 1872496] |
| PolyRow8 | [1, 128, 4297, 40228, 207449, 759136, 2222833, 5565092, 12405073, 25282144] |
| PolyRow9 | [1, 256, 15641, 210166, 1403737, 6281636, 21679681, 62358346, 156719441, 354959272] |

Composition:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 2, 4, 8, 16, 32, 64, 128, 256] |
| PolyCol2 | [1, 1, 3, 9, 29, 97, 337, 1193, 4297, 15641] |
| PolyCol3 | [1, 1, 4, 16, 70, 322, 1564, 7828, 40228, 210166] |
| PolyCol4 | [1, 1, 5, 25, 137, 793, 4889, 31321, 207449, 1403737] |
| PolyCol5 | [1, 1, 6, 36, 236, 1636, 12136, 94136, 759136, 6281636] |
| PolyCol6 | [1, 1, 7, 49, 373, 3001, 25897, 234769, 2222833, 21679681] |
| PolyCol7 | [1, 1, 8, 64, 554, 5062, 49652, 513388, 5565092, 62358346] |
| PolyCol8 | [1, 1, 9, 81, 785, 8017, 87889, 1018193, 12405073, 156719441] |
| PolyCol9 | [1, 1, 10, 100, 1072, 12088, 146224, 1872496, 25282144, 354959272] |

# Composition:Inv:Rev
[]

Composition:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, -1, 0] |
| Row3 | [1, -2, 1, 0] |
| Row4 | [1, -2, 0, 1, 0] |
| Row5 | [1, -2, -1, 3, -1, 0] |
| Row6 | [1, -2, -1, 1, 4, -3, 0] |
| Row7 | [1, -2, -1, 0, 4, 3, -5, 0] |
| Row8 | [1, -2, -1, 0, 2, 6, -1, -5, 0] |
| Row9 | [1, -2, -1, 0, 1, 5, 8, -11, -1, 0] |

Composition:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, -1, 0], [1, -2, 1, 0], [1, -2, 0, 1, 0], [1, -2, -1, 3, -1, 0], [1, -2, -1, 1, 4, -3, 0], [1, -2, -1, 0, 4, 3, -5, 0], [1, -2, -1, 0, 2, 6, -1, -5, 0], [1, -2, -1, 0, 1, 5, 8, -11, -1, 0]] |
| RevTabl    | [[1], [0, 1], [0, -1, 1], [0, 1, -2, 1], [0, 1, 0, -2, 1], [0, -1, 3, -1, -2, 1], [0, -3, 4, 1, -1, -2, 1], [0, -5, 3, 4, 0, -1, -2, 1], [0, -5, -1, 6, 2, 0, -1, -2, 1], [0, -1, -11, 8, 5, 1, 0, -1, -2, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, -1], [1, -2, 0], [1, -2, 1], [1, -2, 0, 0], [1, -2, -1, 1], [1, -2, -1, 3, 0], [1, -2, -1, 1, -1]] |
| AccTabl    | [[1], [1, 1], [1, 0, 0], [1, -1, 0, 0], [1, -1, -1, 0, 0], [1, -1, -2, 1, 0, 0], [1, -1, -2, -1, 3, 0, 0], [1, -1, -2, -2, 2, 5, 0, 0], [1, -1, -2, -2, 0, 6, 5, 0, 0], [1, -1, -2, -2, -1, 4, 12, 1, 0, 0]] |
| RevAccTabl | [[1], [1, 1], [0, 0, 1], [0, 0, -1, 1], [0, 0, -1, -1, 1], [0, 0, 1, -2, -1, 1], [0, 0, 3, -1, -2, -1, 1], [0, 0, 5, 2, -2, -2, -1, 1], [0, 0, 5, 6, 0, -2, -2, -1, 1], [0, 0, 1, 12, 4, -1, -2, -2, -1, 1]] |
| AccRevTabl | [[1], [0, 1], [0, -1, 0], [0, 1, -1, 0], [0, 1, 1, -1, 0], [0, -1, 2, 1, -1, 0], [0, -3, 1, 2, 1, -1, 0], [0, -5, -2, 2, 2, 1, -1, 0], [0, -5, -6, 0, 2, 2, 1, -1, 0], [0, -1, -12, -4, 1, 2, 2, 1, -1, 0]] |

Composition:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 1, 1, 2, 1, -1, 4, -1, 1, 8] |
| OddSum       | [0, 0, -1, -2, -1, 1, -4, 1, -1, -8] |
| AltSum       | [1, 1, 2, 4, 2, -2, 8, -2, 2, 16] |
| AccSum       | [1, 2, 1, 0, -1, -1, 0, 3, 7, 12] |
| AccRevSum    | [1, 1, -1, 0, 1, 1, 0, -3, -7, -12] |
| DiagSum      | [1, 1, 1, 0, -1, 0, -1, -1, 1, -2] |

Composition:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 2, 2, 6, 12, 60, 30, 440] |
| RowGcd     | [1, 1, 1, 2, 2, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 2, 2, 3, 4, 5, 6, 11] |
| CentralE   | [1, -1, 0, 1, 2] |
| CentralO   | [1, -2, -1, 0, 1] |
| ColMiddle  | [1, 1, -1, -2, 0, -1, 1, 0, 2, 1] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, -1, 2, 7, 5, -8, -47, -105, -180] |
| TransNat0  | [0, 0, -1, 0, 1, 1, 0, -3, -7, -12] |
| TransNat1  | [1, 1, -1, 0, 1, 1, 0, -3, -7, -12] |

Composition:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, -1, 1, 1, -1, -3, -5, -5, -1, 9]|
| DiagRow2 | [1, -2, 0, 3, 4, 3, -1, -11, -28, -57]|
| DiagRow3 | [1, -2, -1, 1, 4, 6, 8, 10, 9, 4]|
| DiagRow4 | [1, -2, -1, 0, 2, 5, 7, 10, 15, 22]|
| DiagRow5 | [1, -2, -1, 0, 1, 3, 6, 8, 11, 17]|
| DiagRow6 | [1, -2, -1, 0, 1, 2, 4, 7, 9, 12]|
| DiagRow7 | [1, -2, -1, 0, 1, 2, 3, 5, 8, 10]|
| DiagRow8 | [1, -2, -1, 0, 1, 2, 3, 4, 6, 9]|
| DiagRow9 | [1, -2, -1, 0, 1, 2, 3, 4, 5, 7]|

Composition:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, -1, -2, -2, -2, -2, -2, -2, -2, -2] |
| DiagCol2 | [0, 1, 0, -1, -1, -1, -1, -1, -1, -1] |
| DiagCol3 | [0, 1, 3, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol4 | [0, -1, 4, 4, 2, 1, 1, 1, 1, 1] |
| DiagCol5 | [0, -3, 3, 6, 5, 3, 2, 2, 2, 2] |
| DiagCol6 | [0, -5, -1, 8, 7, 6, 4, 3, 3, 3] |
| DiagCol7 | [0, -5, -11, 10, 10, 8, 7, 5, 4, 4] |
| DiagCol8 | [0, -1, -28, 9, 15, 11, 9, 8, 6, 5] |
| DiagCol9 | [0, 9, -57, 4, 22, 17, 12, 10, 9, 7] |

Composition:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 0, -1, -2, -3, -4, -5, -6, -7, -8] |
| PolyRow3 | [1, 0, 1, 4, 9, 16, 25, 36, 49, 64] |
| PolyRow4 | [1, 0, 5, 22, 57, 116, 205, 330, 497, 712] |
| PolyRow5 | [1, 0, 1, -14, -87, -284, -695, -1434, -2639, -4472] |
| PolyRow6 | [1, 0, -31, -392, -2007, -6784, -17975, -40536, -81487, -150272] |
| PolyRow7 | [1, 0, -167, -2606, -16407, -66284, -204815, -528282, -1196111, -2453912] |
| PolyRow8 | [1, 0, -487, -10058, -79383, -386284, -1397135, -4129782, -10543183, -24078968] |
| PolyRow9 | [1, 0, -983, -23504, -207639, -1108784, -4345535, -13796208, -37580879, -91106144] |

Composition:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 1, -1, 1, 5, 1, -31, -167, -487, -983] |
| PolyCol3 | [1, 1, -2, 4, 22, -14, -392, -2606, -10058, -23504] |
| PolyCol4 | [1, 1, -3, 9, 57, -87, -2007, -16407, -79383, -207639] |
| PolyCol5 | [1, 1, -4, 16, 116, -284, -6784, -66284, -386284, -1108784] |
| PolyCol6 | [1, 1, -5, 25, 205, -695, -17975, -204815, -1397135, -4345535] |
| PolyCol7 | [1, 1, -6, 36, 330, -1434, -40536, -528282, -4129782, -13796208] |
| PolyCol8 | [1, 1, -7, 49, 497, -2639, -81487, -1196111, -10543183, -37580879] |
| PolyCol9 | [1, 1, -8, 64, 712, -4472, -150272, -2453912, -24078968, -91106144] |
