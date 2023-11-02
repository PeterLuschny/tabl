# PartitionMax
['A026820']

PartitionMax Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 2] |
| Row3 | [0, 1, 2, 3] |
| Row4 | [0, 1, 3, 4, 5] |
| Row5 | [0, 1, 3, 5, 6, 7] |
| Row6 | [0, 1, 4, 7, 9, 10, 11] |
| Row7 | [0, 1, 4, 8, 11, 13, 14, 15] |
| Row8 | [0, 1, 5, 10, 15, 18, 20, 21, 22] |
| Row9 | [0, 1, 5, 12, 18, 23, 26, 28, 29, 30] |

PartitionMax Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3, 4, 5], [0, 1, 3, 5, 6, 7], [0, 1, 4, 7, 9, 10, 11], [0, 1, 4, 8, 11, 13, 14, 15], [0, 1, 5, 10, 15, 18, 20, 21, 22], [0, 1, 5, 12, 18, 23, 26, 28, 29, 30]] |
| RevTabl    | [[1], [1, 0], [2, 1, 0], [3, 2, 1, 0], [5, 4, 3, 1, 0], [7, 6, 5, 3, 1, 0], [11, 10, 9, 7, 4, 1, 0], [15, 14, 13, 11, 8, 4, 1, 0], [22, 21, 20, 18, 15, 10, 5, 1, 0], [30, 29, 28, 26, 23, 18, 12, 5, 1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 1, 2], [0, 1, 2], [0, 1, 3, 3], [0, 1, 3, 4], [0, 1, 4, 5, 5], [0, 1, 4, 7, 6]] |
| AccTabl    | [[1], [0, 1], [0, 1, 3], [0, 1, 3, 6], [0, 1, 4, 8, 13], [0, 1, 4, 9, 15, 22], [0, 1, 5, 12, 21, 31, 42], [0, 1, 5, 13, 24, 37, 51, 66], [0, 1, 6, 16, 31, 49, 69, 90, 112], [0, 1, 6, 18, 36, 59, 85, 113, 142, 172]] |
| RevAccTabl | [[1], [1, 0], [3, 1, 0], [6, 3, 1, 0], [13, 8, 4, 1, 0], [22, 15, 9, 4, 1, 0], [42, 31, 21, 12, 5, 1, 0], [66, 51, 37, 24, 13, 5, 1, 0], [112, 90, 69, 49, 31, 16, 6, 1, 0], [172, 142, 113, 85, 59, 36, 18, 6, 1, 0]] |
| AccRevTabl | [[1], [1, 1], [2, 3, 3], [3, 5, 6, 6], [5, 9, 12, 13, 13], [7, 13, 18, 21, 22, 22], [11, 21, 30, 37, 41, 42, 42], [15, 29, 42, 53, 61, 65, 66, 66], [22, 43, 63, 81, 96, 106, 111, 112, 112], [30, 59, 87, 113, 136, 154, 166, 171, 172, 172]] |

PartitionMax Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 6, 13, 22, 42, 66, 112, 172] |
| EvenSum      | [1, 0, 2, 2, 8, 9, 24, 29, 62, 78] |
| OddSum       | [0, 1, 1, 4, 5, 13, 18, 37, 50, 94] |
| AltSum       | [1, -1, 1, -2, 3, -4, 6, -8, 12, -16] |
| AccSum       | [1, 1, 4, 10, 26, 51, 112, 197, 374, 632] |
| AccRevSum    | [1, 2, 8, 20, 52, 103, 224, 397, 746, 1260] |
| DiagSum      | [1, 0, 1, 1, 3, 3, 7, 8, 15, 18] |

PartitionMax Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 60, 210, 13860, 120120, 13860, 10925460] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| CentralE   | [1, 1, 3, 7, 15] |
| CentralO   | [0, 1, 3, 8, 18] |
| ColMiddle  | [1, 0, 1, 1, 3, 3, 7, 8, 15, 18] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| TransSqrs  | [0, 1, 9, 36, 129, 329, 870, 1829, 3958, 7586] |
| TransNat0  | [0, 1, 5, 14, 39, 81, 182, 331, 634, 1088] |
| TransNat1  | [1, 2, 8, 20, 52, 103, 224, 397, 746, 1260] |

PartitionMax Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30]|
| DiagRow1 | [0, 1, 2, 4, 6, 10, 14, 21, 29, 41]|
| DiagRow2 | [0, 1, 3, 5, 9, 13, 20, 28, 40, 54]|
| DiagRow3 | [0, 1, 3, 7, 11, 18, 26, 38, 52, 73]|
| DiagRow4 | [0, 1, 4, 8, 15, 23, 35, 49, 70, 94]|
| DiagRow5 | [0, 1, 4, 10, 18, 30, 44, 65, 89, 123]|
| DiagRow6 | [0, 1, 5, 12, 23, 37, 58, 82, 116, 157]|
| DiagRow7 | [0, 1, 5, 14, 27, 47, 71, 105, 146, 201]|
| DiagRow8 | [0, 1, 6, 16, 34, 57, 90, 131, 186, 252]|
| DiagRow9 | [0, 1, 6, 19, 39, 70, 110, 164, 230, 318]|

PartitionMax Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [2, 2, 3, 3, 4, 4, 5, 5, 6, 6] |
| DiagCol3 | [3, 4, 5, 7, 8, 10, 12, 14, 16, 19] |
| DiagCol4 | [5, 6, 9, 11, 15, 18, 23, 27, 34, 39] |
| DiagCol5 | [7, 10, 13, 18, 23, 30, 37, 47, 57, 70] |
| DiagCol6 | [11, 14, 20, 26, 35, 44, 58, 71, 90, 110] |
| DiagCol7 | [15, 21, 28, 38, 49, 65, 82, 105, 131, 164] |
| DiagCol8 | [22, 29, 40, 52, 70, 89, 116, 146, 186, 230] |
| DiagCol9 | [30, 41, 54, 73, 94, 123, 157, 201, 252, 318] |

PartitionMax Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171] |
| PolyRow3 | [0, 6, 34, 102, 228, 430, 726, 1134, 1672, 2358] |
| PolyRow4 | [0, 13, 126, 543, 1588, 3705, 7458, 13531, 22728, 35973] |
| PolyRow5 | [0, 22, 374, 2352, 9076, 26330, 63402, 133924, 256712, 456606] |
| PolyRow6 | [0, 42, 1242, 11406, 58116, 209730, 604302, 1486422, 3251976, 6500826] |
| PolyRow7 | [0, 66, 3490, 47316, 319812, 1439230, 4969446, 14248080, 35602696, 80030682] |
| PolyRow8 | [0, 112, 10518, 210756, 1890772, 10613880, 43925082, 146815228, 419038536, 1059268032] |
| PolyRow9 | [0, 172, 29174, 868368, 10359124, 72600380, 360295962, 1404339664, 4579440968, 13020195564] |

PartitionMax Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 3, 6, 13, 22, 42, 66, 112, 172] |
| PolyCol2 | [1, 2, 10, 34, 126, 374, 1242, 3490, 10518, 29174] |
| PolyCol3 | [1, 3, 21, 102, 543, 2352, 11406, 47316, 210756, 868368] |
| PolyCol4 | [1, 4, 36, 228, 1588, 9076, 58116, 319812, 1890772, 10359124] |
| PolyCol5 | [1, 5, 55, 430, 3705, 26330, 209730, 1439230, 10613880, 72600380] |
| PolyCol6 | [1, 6, 78, 726, 7458, 63402, 604302, 4969446, 43925082, 360295962] |
| PolyCol7 | [1, 7, 105, 1134, 13531, 133924, 1486422, 14248080, 146815228, 1404339664] |
| PolyCol8 | [1, 8, 136, 1672, 22728, 256712, 3251976, 35602696, 419038536, 4579440968] |
| PolyCol9 | [1, 9, 171, 2358, 35973, 456606, 6500826, 80030682, 1059268032, 13020195564] |

# PartitionMax:Rev
[]

PartitionMax:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [2, 1, 0] |
| Row3 | [3, 2, 1, 0] |
| Row4 | [5, 4, 3, 1, 0] |
| Row5 | [7, 6, 5, 3, 1, 0] |
| Row6 | [11, 10, 9, 7, 4, 1, 0] |
| Row7 | [15, 14, 13, 11, 8, 4, 1, 0] |
| Row8 | [22, 21, 20, 18, 15, 10, 5, 1, 0] |
| Row9 | [30, 29, 28, 26, 23, 18, 12, 5, 1, 0] |

PartitionMax:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [2, 1, 0], [3, 2, 1, 0], [5, 4, 3, 1, 0], [7, 6, 5, 3, 1, 0], [11, 10, 9, 7, 4, 1, 0], [15, 14, 13, 11, 8, 4, 1, 0], [22, 21, 20, 18, 15, 10, 5, 1, 0], [30, 29, 28, 26, 23, 18, 12, 5, 1, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3, 4, 5], [0, 1, 3, 5, 6, 7], [0, 1, 4, 7, 9, 10, 11], [0, 1, 4, 8, 11, 13, 14, 15], [0, 1, 5, 10, 15, 18, 20, 21, 22], [0, 1, 5, 12, 18, 23, 26, 28, 29, 30]] |
| AntiDiag   | [[1], [1], [2, 0], [3, 1], [5, 2, 0], [7, 4, 1], [11, 6, 3, 0], [15, 10, 5, 1], [22, 14, 9, 3, 0], [30, 21, 13, 7, 1]] |
| AccTabl    | [[1], [1, 1], [2, 3, 3], [3, 5, 6, 6], [5, 9, 12, 13, 13], [7, 13, 18, 21, 22, 22], [11, 21, 30, 37, 41, 42, 42], [15, 29, 42, 53, 61, 65, 66, 66], [22, 43, 63, 81, 96, 106, 111, 112, 112], [30, 59, 87, 113, 136, 154, 166, 171, 172, 172]] |
| RevAccTabl | [[1], [1, 1], [3, 3, 2], [6, 6, 5, 3], [13, 13, 12, 9, 5], [22, 22, 21, 18, 13, 7], [42, 42, 41, 37, 30, 21, 11], [66, 66, 65, 61, 53, 42, 29, 15], [112, 112, 111, 106, 96, 81, 63, 43, 22], [172, 172, 171, 166, 154, 136, 113, 87, 59, 30]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 3], [0, 1, 3, 6], [0, 1, 4, 8, 13], [0, 1, 4, 9, 15, 22], [0, 1, 5, 12, 21, 31, 42], [0, 1, 5, 13, 24, 37, 51, 66], [0, 1, 6, 16, 31, 49, 69, 90, 112], [0, 1, 6, 18, 36, 59, 85, 113, 142, 172]] |

PartitionMax:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 6, 13, 22, 42, 66, 112, 172] |
| EvenSum      | [1, 1, 2, 4, 8, 13, 24, 37, 62, 94] |
| OddSum       | [0, 0, 1, 2, 5, 9, 18, 29, 50, 78] |
| AltSum       | [1, 1, 1, 2, 3, 4, 6, 8, 12, 16] |
| AccSum       | [1, 2, 8, 20, 52, 103, 224, 397, 746, 1260] |
| AccRevSum    | [1, 1, 4, 10, 26, 51, 112, 197, 374, 632] |
| DiagSum      | [1, 1, 2, 4, 7, 12, 20, 31, 48, 72] |

PartitionMax:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 60, 210, 13860, 120120, 13860, 10925460] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| CentralE   | [1, 1, 3, 7, 15] |
| CentralO   | [1, 2, 5, 11, 23] |
| ColMiddle  | [1, 1, 1, 2, 3, 5, 7, 11, 15, 23] |
| ColLeft    | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 6, 25, 69, 198, 429, 982, 1934] |
| TransNat0  | [0, 0, 1, 4, 13, 29, 70, 131, 262, 460] |
| TransNat1  | [1, 1, 4, 10, 26, 51, 112, 197, 374, 632] |

PartitionMax:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]|
| DiagRow3 | [3, 4, 5, 7, 8, 10, 12, 14, 16, 19]|
| DiagRow4 | [5, 6, 9, 11, 15, 18, 23, 27, 34, 39]|
| DiagRow5 | [7, 10, 13, 18, 23, 30, 37, 47, 57, 70]|
| DiagRow6 | [11, 14, 20, 26, 35, 44, 58, 71, 90, 110]|
| DiagRow7 | [15, 21, 28, 38, 49, 65, 82, 105, 131, 164]|
| DiagRow8 | [22, 29, 40, 52, 70, 89, 116, 146, 186, 230]|
| DiagRow9 | [30, 41, 54, 73, 94, 123, 157, 201, 252, 318]|

PartitionMax:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| DiagCol1 | [0, 1, 2, 4, 6, 10, 14, 21, 29, 41] |
| DiagCol2 | [0, 1, 3, 5, 9, 13, 20, 28, 40, 54] |
| DiagCol3 | [0, 1, 3, 7, 11, 18, 26, 38, 52, 73] |
| DiagCol4 | [0, 1, 4, 8, 15, 23, 35, 49, 70, 94] |
| DiagCol5 | [0, 1, 4, 10, 18, 30, 44, 65, 89, 123] |
| DiagCol6 | [0, 1, 5, 12, 23, 37, 58, 82, 116, 157] |
| DiagCol7 | [0, 1, 5, 14, 27, 47, 71, 105, 146, 201] |
| DiagCol8 | [0, 1, 6, 16, 34, 57, 90, 131, 186, 252] |
| DiagCol9 | [0, 1, 6, 19, 39, 70, 110, 164, 230, 318] |

PartitionMax:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| PolyRow3 | [3, 6, 11, 18, 27, 38, 51, 66, 83, 102] |
| PolyRow4 | [5, 13, 33, 71, 133, 225, 353, 523, 741, 1013] |
| PolyRow5 | [7, 22, 79, 232, 559, 1162, 2167, 3724, 6007, 9214] |
| PolyRow6 | [11, 42, 219, 878, 2691, 6786, 14867, 29334, 53403, 91226] |
| PolyRow7 | [15, 66, 503, 2820, 11223, 34910, 91071, 208608, 432575, 829338] |
| PolyRow8 | [22, 112, 1296, 10228, 52522, 199752, 615172, 1623196, 3807678, 8144032] |
| PolyRow9 | [30, 172, 3016, 33552, 223186, 1043500, 3815772, 11662576, 31108102, 74574156] |

PartitionMax:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 2, 3, 5, 7, 11, 15, 22, 30] |
| PolyCol1 | [1, 1, 3, 6, 13, 22, 42, 66, 112, 172] |
| PolyCol2 | [1, 1, 4, 11, 33, 79, 219, 503, 1296, 3016] |
| PolyCol3 | [1, 1, 5, 18, 71, 232, 878, 2820, 10228, 33552] |
| PolyCol4 | [1, 1, 6, 27, 133, 559, 2691, 11223, 52522, 223186] |
| PolyCol5 | [1, 1, 7, 38, 225, 1162, 6786, 34910, 199752, 1043500] |
| PolyCol6 | [1, 1, 8, 51, 353, 2167, 14867, 91071, 615172, 3815772] |
| PolyCol7 | [1, 1, 9, 66, 523, 3724, 29334, 208608, 1623196, 11662576] |
| PolyCol8 | [1, 1, 10, 83, 741, 6007, 53403, 432575, 3807678, 31108102] |
| PolyCol9 | [1, 1, 11, 102, 1013, 9214, 91226, 829338, 8144032, 74574156] |
