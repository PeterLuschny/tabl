# EulerianZigZag
['A205497']

EulerianZigZag Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 0, 0] |
| Row3 | [1, 1, 0, 0] |
| Row4 | [1, 3, 1, 0, 0] |
| Row5 | [1, 7, 7, 1, 0, 0] |
| Row6 | [1, 14, 31, 14, 1, 0, 0] |
| Row7 | [1, 26, 109, 109, 26, 1, 0, 0] |
| Row8 | [1, 46, 334, 623, 334, 46, 1, 0, 0] |
| Row9 | [1, 79, 937, 2951, 2951, 937, 79, 1, 0, 0] |

EulerianZigZag Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 0, 0], [1, 1, 0, 0], [1, 3, 1, 0, 0], [1, 7, 7, 1, 0, 0], [1, 14, 31, 14, 1, 0, 0], [1, 26, 109, 109, 26, 1, 0, 0], [1, 46, 334, 623, 334, 46, 1, 0, 0], [1, 79, 937, 2951, 2951, 937, 79, 1, 0, 0]] |
| RevTabl    | [[1], [0, 1], [0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 3, 1], [0, 0, 1, 7, 7, 1], [0, 0, 1, 14, 31, 14, 1], [0, 0, 1, 26, 109, 109, 26, 1], [0, 0, 1, 46, 334, 623, 334, 46, 1], [0, 0, 1, 79, 937, 2951, 2951, 937, 79, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 0], [1, 1, 0], [1, 3, 0], [1, 7, 1, 0], [1, 14, 7, 0], [1, 26, 31, 1, 0], [1, 46, 109, 14, 0]] |
| AccTabl    | [[1], [1, 1], [1, 1, 1], [1, 2, 2, 2], [1, 4, 5, 5, 5], [1, 8, 15, 16, 16, 16], [1, 15, 46, 60, 61, 61, 61], [1, 27, 136, 245, 271, 272, 272, 272], [1, 47, 381, 1004, 1338, 1384, 1385, 1385, 1385], [1, 80, 1017, 3968, 6919, 7856, 7935, 7936, 7936, 7936]] |
| RevAccTabl | [[1], [1, 1], [1, 1, 1], [2, 2, 2, 1], [5, 5, 5, 4, 1], [16, 16, 16, 15, 8, 1], [61, 61, 61, 60, 46, 15, 1], [272, 272, 272, 271, 245, 136, 27, 1], [1385, 1385, 1385, 1384, 1338, 1004, 381, 47, 1], [7936, 7936, 7936, 7935, 7856, 6919, 3968, 1017, 80, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 0, 1], [0, 0, 1, 2], [0, 0, 1, 4, 5], [0, 0, 1, 8, 15, 16], [0, 0, 1, 15, 46, 60, 61], [0, 0, 1, 27, 136, 245, 271, 272], [0, 0, 1, 47, 381, 1004, 1338, 1384, 1385], [0, 0, 1, 80, 1017, 3968, 6919, 7856, 7935, 7936]] |
| DiffxTabl  | [[1], [1, 0], [1, 0, 0], [1, 2, 0, 0], [1, 6, 3, 0, 0], [1, 14, 21, 4, 0, 0], [1, 28, 93, 56, 5, 0, 0], [1, 52, 327, 436, 130, 6, 0, 0], [1, 92, 1002, 2492, 1670, 276, 7, 0, 0], [1, 158, 2811, 11804, 14755, 5622, 553, 8, 0, 0]] |

EulerianZigZag Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| EvenSum      | [1, 1, 1, 1, 2, 8, 33, 136, 670, 3968] |
| OddSum       | [0, 0, 0, 1, 3, 8, 28, 136, 715, 3968] |
| AltSum       | [1, 1, 1, 0, -1, 0, 5, 0, -45, 0] |
| AbsSum       | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| AccSum       | [1, 2, 3, 7, 20, 72, 305, 1496, 8310, 51584] |
| AccRevSum    | [1, 1, 1, 3, 10, 40, 183, 952, 5540, 35712] |
| DiagSum      | [1, 1, 1, 1, 2, 4, 9, 22, 59, 170] |

EulerianZigZag Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 3, 7, 434, 2834, 4785886, 218441873] |
| RowGcd     | [1, 1, 1, 1, 3, 7, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 3, 7, 31, 109, 623, 2951] |
| CentralE   | [1, 0, 1, 14, 334] |
| CentralO   | [1, 1, 7, 109, 2951] |
| ColMiddle  | [1, 1, 0, 1, 1, 7, 14, 109, 334, 2951] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 1, 1, 4, 19, 116, 845, 7218, 70593, 778888] |
| InvBinConv | [1, -1, 1, 2, -5, -26, 117, 818, -5071, -45502] |
| TransSqrs  | [0, 0, 0, 1, 7, 44, 280, 1884, 13519, 103920] |
| TransNat0  | [0, 0, 0, 1, 5, 24, 122, 680, 4155, 27776] |
| TransNat1  | [1, 1, 1, 3, 10, 40, 183, 952, 5540, 35712] |
| PosHalf    | [1, 2, 4, 12, 44, 204, 1124, 7236, 53172, 439596] |
| NegHalf    | [1, -2, 4, -4, -4, 28, 4, -412, 788, 8572] |

EulerianZigZag Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow3 | [1, 3, 7, 14, 26, 46, 79, 133, 221, 364]|
| DiagRow4 | [1, 7, 31, 109, 334, 937, 2475, 6267, 15393, 36976]|
| DiagRow5 | [1, 14, 109, 623, 2951, 12331, 47191, 169416, 579889, 1914226]|
| DiagRow6 | [1, 26, 334, 2951, 20641, 123216, 656683, 3217526, 14786816, 64657546]|
| DiagRow7 | [1, 46, 937, 12331, 123216, 1019051, 7349140, 47816612, 287357460, 1622135139]|
| DiagRow8 | [1, 79, 2475, 47191, 656683, 7349140, 70148989, 593513485, 4571277561, 32672880245]|
| DiagRow9 | [1, 133, 6267, 169416, 3217526, 47816612, 593513485, 6421463423, 62382094567, 555922552167]|

EulerianZigZag Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 0, 1, 3, 7, 14, 26, 46, 79, 133] |
| DiagCol2 | [0, 0, 1, 7, 31, 109, 334, 937, 2475, 6267] |
| DiagCol3 | [0, 0, 1, 14, 109, 623, 2951, 12331, 47191, 169416] |
| DiagCol4 | [0, 0, 1, 26, 334, 2951, 20641, 123216, 656683, 3217526] |
| DiagCol5 | [0, 0, 1, 46, 937, 12331, 123216, 1019051, 7349140, 47816612] |
| DiagCol6 | [0, 0, 1, 79, 2475, 47191, 656683, 7349140, 70148989, 593513485] |
| DiagCol7 | [0, 0, 1, 133, 6267, 169416, 3217526, 47816612, 593513485, 6421463423] |
| DiagCol8 | [0, 0, 1, 221, 15393, 579889, 14786816, 287357460, 4571277561, 62382094567] |
| DiagCol9 | [0, 0, 1, 364, 36976, 1914226, 64657546, 1622135139, 32672880245, 555922552167] |

EulerianZigZag Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow3 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow4 | [1, 5, 11, 19, 29, 41, 55, 71, 89, 109] |
| PolyRow5 | [1, 16, 51, 112, 205, 336, 511, 736, 1017, 1360] |
| PolyRow6 | [1, 61, 281, 781, 1705, 3221, 5521, 8821, 13361, 19405] |
| PolyRow7 | [1, 272, 1809, 6352, 16505, 35856, 69097, 122144, 202257, 318160] |
| PolyRow8 | [1, 1385, 13293, 58927, 182105, 454581, 984085, 1923083, 3478257, 5920705] |
| PolyRow9 | [1, 7936, 109899, 614848, 2259085, 6477696, 15747991, 34009984, 67168953, 123685120] |

EulerianZigZag Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| PolyCol2 | [1, 1, 1, 3, 11, 51, 281, 1809, 13293, 109899] |
| PolyCol3 | [1, 1, 1, 4, 19, 112, 781, 6352, 58927, 614848] |
| PolyCol4 | [1, 1, 1, 5, 29, 205, 1705, 16505, 182105, 2259085] |
| PolyCol5 | [1, 1, 1, 6, 41, 336, 3221, 35856, 454581, 6477696] |
| PolyCol6 | [1, 1, 1, 7, 55, 511, 5521, 69097, 984085, 15747991] |
| PolyCol7 | [1, 1, 1, 8, 71, 736, 8821, 122144, 1923083, 34009984] |
| PolyCol8 | [1, 1, 1, 9, 89, 1017, 13361, 202257, 3478257, 67168953] |
| PolyCol9 | [1, 1, 1, 10, 109, 1360, 19405, 318160, 5920705, 123685120] |

# EulerianZigZag:Rev
[]

EulerianZigZag:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 0, 1] |
| Row3 | [0, 0, 1, 1] |
| Row4 | [0, 0, 1, 3, 1] |
| Row5 | [0, 0, 1, 7, 7, 1] |
| Row6 | [0, 0, 1, 14, 31, 14, 1] |
| Row7 | [0, 0, 1, 26, 109, 109, 26, 1] |
| Row8 | [0, 0, 1, 46, 334, 623, 334, 46, 1] |
| Row9 | [0, 0, 1, 79, 937, 2951, 2951, 937, 79, 1] |

EulerianZigZag:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 3, 1], [0, 0, 1, 7, 7, 1], [0, 0, 1, 14, 31, 14, 1], [0, 0, 1, 26, 109, 109, 26, 1], [0, 0, 1, 46, 334, 623, 334, 46, 1], [0, 0, 1, 79, 937, 2951, 2951, 937, 79, 1]] |
| RevTabl    | [[1], [1, 0], [1, 0, 0], [1, 1, 0, 0], [1, 3, 1, 0, 0], [1, 7, 7, 1, 0, 0], [1, 14, 31, 14, 1, 0, 0], [1, 26, 109, 109, 26, 1, 0, 0], [1, 46, 334, 623, 334, 46, 1, 0, 0], [1, 79, 937, 2951, 2951, 937, 79, 1, 0, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 3], [0, 0, 1, 7, 1], [0, 0, 1, 14, 7]] |
| AccTabl    | [[1], [0, 1], [0, 0, 1], [0, 0, 1, 2], [0, 0, 1, 4, 5], [0, 0, 1, 8, 15, 16], [0, 0, 1, 15, 46, 60, 61], [0, 0, 1, 27, 136, 245, 271, 272], [0, 0, 1, 47, 381, 1004, 1338, 1384, 1385], [0, 0, 1, 80, 1017, 3968, 6919, 7856, 7935, 7936]] |
| RevAccTabl | [[1], [1, 0], [1, 0, 0], [2, 1, 0, 0], [5, 4, 1, 0, 0], [16, 15, 8, 1, 0, 0], [61, 60, 46, 15, 1, 0, 0], [272, 271, 245, 136, 27, 1, 0, 0], [1385, 1384, 1338, 1004, 381, 47, 1, 0, 0], [7936, 7935, 7856, 6919, 3968, 1017, 80, 1, 0, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 1, 1], [1, 2, 2, 2], [1, 4, 5, 5, 5], [1, 8, 15, 16, 16, 16], [1, 15, 46, 60, 61, 61, 61], [1, 27, 136, 245, 271, 272, 272, 272], [1, 47, 381, 1004, 1338, 1384, 1385, 1385, 1385], [1, 80, 1017, 3968, 6919, 7856, 7935, 7936, 7936, 7936]] |
| DiffxTabl  | [[1], [0, 2], [0, 0, 3], [0, 0, 3, 4], [0, 0, 3, 12, 5], [0, 0, 3, 28, 35, 6], [0, 0, 3, 56, 155, 84, 7], [0, 0, 3, 104, 545, 654, 182, 8], [0, 0, 3, 184, 1670, 3738, 2338, 368, 9], [0, 0, 3, 316, 4685, 17706, 20657, 7496, 711, 10]] |

EulerianZigZag:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| EvenSum      | [1, 0, 1, 1, 2, 8, 33, 136, 670, 3968] |
| OddSum       | [0, 1, 0, 1, 3, 8, 28, 136, 715, 3968] |
| AltSum       | [1, -1, 1, 0, -1, 0, 5, 0, -45, 0] |
| AbsSum       | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| AccSum       | [1, 1, 1, 3, 10, 40, 183, 952, 5540, 35712] |
| AccRevSum    | [1, 2, 3, 7, 20, 72, 305, 1496, 8310, 51584] |
| DiagSum      | [1, 0, 1, 0, 1, 1, 2, 4, 9, 22] |

EulerianZigZag:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 3, 7, 434, 2834, 4785886, 218441873] |
| RowGcd     | [1, 1, 1, 1, 3, 7, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 3, 7, 31, 109, 623, 2951] |
| CentralE   | [1, 0, 1, 14, 334] |
| CentralO   | [0, 0, 1, 26, 937] |
| ColMiddle  | [1, 0, 0, 0, 1, 1, 14, 26, 334, 937] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 1, 1, 4, 19, 116, 845, 7218, 70593, 778888] |
| InvBinConv | [1, 1, 1, -2, -5, 26, 117, -818, -5071, 45502] |
| TransSqrs  | [0, 1, 4, 13, 47, 204, 1012, 5692, 35679, 246768] |
| TransNat0  | [0, 1, 2, 5, 15, 56, 244, 1224, 6925, 43648] |
| TransNat1  | [1, 2, 3, 7, 20, 72, 305, 1496, 8310, 51584] |
| PosHalf    | [1, 1, 1, 3, 11, 51, 281, 1809, 13293, 109899] |
| NegHalf    | [1, 1, 1, -1, -1, 7, 1, -103, 197, 2143] |

EulerianZigZag:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 0, 1, 3, 7, 14, 26, 46, 79, 133]|
| DiagRow2 | [0, 0, 1, 7, 31, 109, 334, 937, 2475, 6267]|
| DiagRow3 | [0, 0, 1, 14, 109, 623, 2951, 12331, 47191, 169416]|
| DiagRow4 | [0, 0, 1, 26, 334, 2951, 20641, 123216, 656683, 3217526]|
| DiagRow5 | [0, 0, 1, 46, 937, 12331, 123216, 1019051, 7349140, 47816612]|
| DiagRow6 | [0, 0, 1, 79, 2475, 47191, 656683, 7349140, 70148989, 593513485]|
| DiagRow7 | [0, 0, 1, 133, 6267, 169416, 3217526, 47816612, 593513485, 6421463423]|
| DiagRow8 | [0, 0, 1, 221, 15393, 579889, 14786816, 287357460, 4571277561, 62382094567]|
| DiagRow9 | [0, 0, 1, 364, 36976, 1914226, 64657546, 1622135139, 32672880245, 555922552167]|

EulerianZigZag:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol3 | [1, 3, 7, 14, 26, 46, 79, 133, 221, 364] |
| DiagCol4 | [1, 7, 31, 109, 334, 937, 2475, 6267, 15393, 36976] |
| DiagCol5 | [1, 14, 109, 623, 2951, 12331, 47191, 169416, 579889, 1914226] |
| DiagCol6 | [1, 26, 334, 2951, 20641, 123216, 656683, 3217526, 14786816, 64657546] |
| DiagCol7 | [1, 46, 937, 12331, 123216, 1019051, 7349140, 47816612, 287357460, 1622135139] |
| DiagCol8 | [1, 79, 2475, 47191, 656683, 7349140, 70148989, 593513485, 4571277561, 32672880245] |
| DiagCol9 | [1, 133, 6267, 169416, 3217526, 47816612, 593513485, 6421463423, 62382094567, 555922552167] |

EulerianZigZag:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] |
| PolyRow3 | [0, 2, 12, 36, 80, 150, 252, 392, 576, 810] |
| PolyRow4 | [0, 5, 44, 171, 464, 1025, 1980, 3479, 5696, 8829] |
| PolyRow5 | [0, 16, 204, 1008, 3280, 8400, 18396, 36064, 65088, 110160] |
| PolyRow6 | [0, 61, 1124, 7029, 27280, 80525, 198756, 432229, 855104, 1571805] |
| PolyRow7 | [0, 272, 7236, 57168, 264080, 896400, 2487492, 5985056, 12944448, 25770960] |
| PolyRow8 | [0, 1385, 53172, 530343, 2913680, 11364525, 35427060, 94231067, 222608448, 479577105] |
| PolyRow9 | [0, 7936, 439596, 5533632, 36145360, 161942400, 566927676, 1666489216, 4298812992, 10018494720] |

EulerianZigZag:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936] |
| PolyCol2 | [1, 2, 4, 12, 44, 204, 1124, 7236, 53172, 439596] |
| PolyCol3 | [1, 3, 9, 36, 171, 1008, 7029, 57168, 530343, 5533632] |
| PolyCol4 | [1, 4, 16, 80, 464, 3280, 27280, 264080, 2913680, 36145360] |
| PolyCol5 | [1, 5, 25, 150, 1025, 8400, 80525, 896400, 11364525, 161942400] |
| PolyCol6 | [1, 6, 36, 252, 1980, 18396, 198756, 2487492, 35427060, 566927676] |
| PolyCol7 | [1, 7, 49, 392, 3479, 36064, 432229, 5985056, 94231067, 1666489216] |
| PolyCol8 | [1, 8, 64, 576, 5696, 65088, 855104, 12944448, 222608448, 4298812992] |
| PolyCol9 | [1, 9, 81, 810, 8829, 110160, 1571805, 25770960, 479577105, 10018494720] |

# EulerianZigZag:Rev:Inv
[]

EulerianZigZag:Rev:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 0, 1] |
| Row3 | [0, 0, -1, 1] |
| Row4 | [0, 0, 2, -3, 1] |
| Row5 | [0, 0, -8, 14, -7, 1] |
| Row6 | [0, 0, 63, -117, 67, -14, 1] |
| Row7 | [0, 0, -959, 1817, -1088, 255, -26, 1] |
| Row8 | [0, 0, 27433, -52270, 31697, -7677, 862, -46, 1] |
| Row9 | [0, 0, -1432725, 2733486, -1662604, 405911, -46687, 2697, -79, 1] |

EulerianZigZag:Rev:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 0, 1], [0, 0, -1, 1], [0, 0, 2, -3, 1], [0, 0, -8, 14, -7, 1], [0, 0, 63, -117, 67, -14, 1], [0, 0, -959, 1817, -1088, 255, -26, 1], [0, 0, 27433, -52270, 31697, -7677, 862, -46, 1], [0, 0, -1432725, 2733486, -1662604, 405911, -46687, 2697, -79, 1]] |
| RevTabl    | [[1], [1, 0], [1, 0, 0], [1, -1, 0, 0], [1, -3, 2, 0, 0], [1, -7, 14, -8, 0, 0], [1, -14, 67, -117, 63, 0, 0], [1, -26, 255, -1088, 1817, -959, 0, 0], [1, -46, 862, -7677, 31697, -52270, 27433, 0, 0], [1, -79, 2697, -46687, 405911, -1662604, 2733486, -1432725, 0, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 0], [0, 0, 1], [0, 0, -1], [0, 0, 2, 1], [0, 0, -8, -3], [0, 0, 63, 14, 1], [0, 0, -959, -117, -7]] |
| AccTabl    | [[1], [0, 1], [0, 0, 1], [0, 0, -1, 0], [0, 0, 2, -1, 0], [0, 0, -8, 6, -1, 0], [0, 0, 63, -54, 13, -1, 0], [0, 0, -959, 858, -230, 25, -1, 0], [0, 0, 27433, -24837, 6860, -817, 45, -1, 0], [0, 0, -1432725, 1300761, -361843, 44068, -2619, 78, -1, 0]] |
| RevAccTabl | [[1], [1, 0], [1, 0, 0], [0, -1, 0, 0], [0, -1, 2, 0, 0], [0, -1, 6, -8, 0, 0], [0, -1, 13, -54, 63, 0, 0], [0, -1, 25, -230, 858, -959, 0, 0], [0, -1, 45, -817, 6860, -24837, 27433, 0, 0], [0, -1, 78, -2619, 44068, -361843, 1300761, -1432725, 0, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 1, 1], [1, 0, 0, 0], [1, -2, 0, 0, 0], [1, -6, 8, 0, 0, 0], [1, -13, 54, -63, 0, 0, 0], [1, -25, 230, -858, 959, 0, 0, 0], [1, -45, 817, -6860, 24837, -27433, 0, 0, 0], [1, -78, 2619, -44068, 361843, -1300761, 1432725, 0, 0, 0]] |
| DiffxTabl  | [[1], [0, 2], [0, 0, 3], [0, 0, -3, 4], [0, 0, 6, -12, 5], [0, 0, -24, 56, -35, 6], [0, 0, 189, -468, 335, -84, 7], [0, 0, -2877, 7268, -5440, 1530, -182, 8], [0, 0, 82299, -209080, 158485, -46062, 6034, -368, 9], [0, 0, -4298175, 10933944, -8313020, 2435466, -326809, 21576, -711, 10]] |

EulerianZigZag:Rev:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 1, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 0, 1, -1, 3, -15, 131, -2073, 59993, -3142095] |
| OddSum       | [0, 1, 0, 1, -3, 15, -131, 2073, -59993, 3142095] |
| AltSum       | [1, -1, 1, -2, 6, -30, 262, -4146, 119986, -6284190] |
| AbsSum       | [1, 1, 1, 2, 6, 30, 262, 4146, 119986, 6284190] |
| AccSum       | [1, 1, 1, -1, 1, -3, 21, -307, 8683, -452281] |
| AccRevSum    | [1, 2, 3, 1, -1, 3, -21, 307, -8683, 452281] |
| DiagSum      | [1, 0, 1, 0, 1, -1, 3, -11, 78, -1083] |

EulerianZigZag:Rev:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 6, 56, 109746, 369689436480, 3458920738461805845270, 208656921400838181994868709540900] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 3, 14, 117, 1817, 52270, 2733486] |
| CentralE   | [1, 0, 2, -117, 31697] |
| CentralO   | [0, 0, -8, 1817, -1662604] |
| ColMiddle  | [1, 0, 0, 0, 2, -8, -117, 1817, 31697, -1662604] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 1, 1, -2, 1, 26, -473, 10550, -346349, 15866080] |
| InvBinConv | [1, 1, 1, 4, 25, 256, 4375, 127352, 6368451, 545843326] |
| TransSqrs  | [0, 1, 4, 5, -3, 7, -43, 597, -16629, 863031] |
| TransNat0  | [0, 1, 2, 1, -1, 3, -21, 307, -8683, 452281] |
| TransNat1  | [1, 2, 3, 1, -1, 3, -21, 307, -8683, 452281] |
| PosHalf    | [1, 1, 1, -1, 3, -21, 313, -9351, 532165, -55517313] |
| NegHalf    | [1, 1, 1, 3, 15, 135, 2241, 69537, 4000461, 418414251] |

EulerianZigZag:Rev:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 0, -1, -3, -7, -14, -26, -46, -79, -133]|
| DiagRow2 | [0, 0, 2, 14, 67, 255, 862, 2697, 8032, 23126]|
| DiagRow3 | [0, 0, -8, -117, -1088, -7677, -46687, -257182, -1327170, -6540011]|
| DiagRow4 | [0, 0, 63, 1817, 31697, 405911, 4375886, 41982693, 372180485, 3116647291]|
| DiagRow5 | [0, 0, -959, -52270, -1662604, -37853350, -712081619, -11750624311, -177156964174, -2500336506353]|
| DiagRow6 | [0, 0, 27433, 2733486, 154793280, 6154289173, 199208998807, 5591810089464, 142104975360830, 3356229435131075]|
| DiagRow7 | [0, 0, -1432725, -254341160, -25159461133, -1721461938866, -94792091963686, -4485286353475037, -190746379418077070, -7494823680677219742]|
| DiagRow8 | [0, 0, 133274626, 41335203874, 7037233631831, 819129620967807, 76033775274207949, 6020545287205625832, 425956770141307229865, 27712235106044010793486]|
| DiagRow9 | [0, 0, -21658628724, -11561489287787, -3348533619843939, -657031436012106189, -102059131224317023802, -13444508380177135006914, -1574982076198927709327350, -169006150747481425226476966]|

EulerianZigZag:Rev:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol2 | [1, -1, 2, -8, 63, -959, 27433, -1432725, 133274626, -21658628724] |
| DiagCol3 | [1, -3, 14, -117, 1817, -52270, 2733486, -254341160, 41335203874, -11561489287787] |
| DiagCol4 | [1, -7, 67, -1088, 31697, -1662604, 154793280, -25159461133, 7037233631831, -3348533619843939] |
| DiagCol5 | [1, -14, 255, -7677, 405911, -37853350, 6154289173, -1721461938866, 819129620967807, -657031436012106189] |
| DiagCol6 | [1, -26, 862, -46687, 4375886, -712081619, 199208998807, -94792091963686, 76033775274207949, -102059131224317023802] |
| DiagCol7 | [1, -46, 2697, -257182, 41982693, -11750624311, 5591810089464, -4485286353475037, 6020545287205625832, -13444508380177135006914] |
| DiagCol8 | [1, -79, 8032, -1327170, 372180485, -177156964174, 142104975360830, -190746379418077070, 425956770141307229865, -1574982076198927709327350] |
| DiagCol9 | [1, -133, 23126, -6540011, 3116647291, -2500336506353, 3356229435131075, -7494823680677219742, 27712235106044010793486, -169006150747481425226476966] |

EulerianZigZag:Rev:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] |
| PolyRow3 | [0, 0, 4, 18, 48, 100, 180, 294, 448, 648] |
| PolyRow4 | [0, 0, 0, 18, 96, 300, 720, 1470, 2688, 4536] |
| PolyRow5 | [0, 0, 0, -18, 0, 300, 1440, 4410, 10752, 22680] |
| PolyRow6 | [0, 0, 4, 162, 432, 700, 1620, 6174, 21952, 64152] |
| PolyRow7 | [0, 0, -84, -2502, -6576, -8100, -2340, 14406, 49728, 131544] |
| PolyRow8 | [0, 0, 2596, 71910, 189456, 237700, 100260, -211974, -459200, -105624] |
| PolyRow9 | [0, 0, -137988, -3760074, -9911760, -12475500, -5369220, 10967082, 24835776, 11965320] |

EulerianZigZag:Rev:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 1, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 2, 4, 4, 0, 0, 4, -84, 2596, -137988] |
| PolyCol3 | [1, 3, 9, 18, 18, -18, 162, -2502, 71910, -3760074] |
| PolyCol4 | [1, 4, 16, 48, 96, 0, 432, -6576, 189456, -9911760] |
| PolyCol5 | [1, 5, 25, 100, 300, 300, 700, -8100, 237700, -12475500] |
| PolyCol6 | [1, 6, 36, 180, 720, 1440, 1620, -2340, 100260, -5369220] |
| PolyCol7 | [1, 7, 49, 294, 1470, 4410, 6174, 14406, -211974, 10967082] |
| PolyCol8 | [1, 8, 64, 448, 2688, 10752, 21952, 49728, -459200, 24835776] |
| PolyCol9 | [1, 9, 81, 648, 4536, 22680, 64152, 131544, -105624, 11965320] |

