# Polygonal
['A139600', 'A057145', 'A134394', 'A139601']

Polygonal Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 2] |
| Row3 | [0, 1, 3, 3] |
| Row4 | [0, 1, 4, 6, 4] |
| Row5 | [0, 1, 5, 9, 10, 5] |
| Row6 | [0, 1, 6, 12, 16, 15, 6] |
| Row7 | [0, 1, 7, 15, 22, 25, 21, 7] |
| Row8 | [0, 1, 8, 18, 28, 35, 36, 28, 8] |
| Row9 | [0, 1, 9, 21, 34, 45, 51, 49, 36, 9] |

Polygonal Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[0], [0, 1], [0, 1, 2], [0, 1, 3, 3], [0, 1, 4, 6, 4], [0, 1, 5, 9, 10, 5], [0, 1, 6, 12, 16, 15, 6], [0, 1, 7, 15, 22, 25, 21, 7], [0, 1, 8, 18, 28, 35, 36, 28, 8], [0, 1, 9, 21, 34, 45, 51, 49, 36, 9]] |
| RevTabl    | [[0], [1, 0], [2, 1, 0], [3, 3, 1, 0], [4, 6, 4, 1, 0], [5, 10, 9, 5, 1, 0], [6, 15, 16, 12, 6, 1, 0], [7, 21, 25, 22, 15, 7, 1, 0], [8, 28, 36, 35, 28, 18, 8, 1, 0], [9, 36, 49, 51, 45, 34, 21, 9, 1, 0]] |
| AntiDiag   | [[0], [0], [0, 1], [0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 4, 3], [0, 1, 5, 6], [0, 1, 6, 9, 4], [0, 1, 7, 12, 10]] |
| AccTabl    | [[0], [0, 1], [0, 1, 3], [0, 1, 4, 7], [0, 1, 5, 11, 15], [0, 1, 6, 15, 25, 30], [0, 1, 7, 19, 35, 50, 56], [0, 1, 8, 23, 45, 70, 91, 98], [0, 1, 9, 27, 55, 90, 126, 154, 162], [0, 1, 10, 31, 65, 110, 161, 210, 246, 255]] |
| RevAccTabl | [[0], [1, 0], [3, 1, 0], [7, 4, 1, 0], [15, 11, 5, 1, 0], [30, 25, 15, 6, 1, 0], [56, 50, 35, 19, 7, 1, 0], [98, 91, 70, 45, 23, 8, 1, 0], [162, 154, 126, 90, 55, 27, 9, 1, 0], [255, 246, 210, 161, 110, 65, 31, 10, 1, 0]] |
| AccRevTabl | [[0], [1, 1], [2, 3, 3], [3, 6, 7, 7], [4, 10, 14, 15, 15], [5, 15, 24, 29, 30, 30], [6, 21, 37, 49, 55, 56, 56], [7, 28, 53, 75, 90, 97, 98, 98], [8, 36, 72, 107, 135, 153, 161, 162, 162], [9, 45, 94, 145, 190, 224, 245, 254, 255, 255]] |

Polygonal Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 1, 3, 7, 15, 30, 56, 98, 162, 255] |
| EvenSum      | [0, 0, 2, 3, 8, 15, 28, 50, 80, 130] |
| OddSum       | [0, 1, 1, 4, 7, 15, 28, 48, 82, 125] |
| AltSum       | [0, -1, 1, -1, 1, 0, 0, 2, -2, 5] |
| AccSum       | [0, 1, 4, 12, 32, 77, 168, 336, 624, 1089] |
| AccRevSum    | [0, 2, 8, 23, 58, 133, 280, 546, 996, 1716] |
| DiagSum      | [0, 0, 1, 1, 3, 4, 8, 12, 20, 30] |

Polygonal Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 3, 12, 90, 240, 11550, 2520, 149940] |
| RowGcd     | [1, 1, 2, 3, 2, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 2, 3, 6, 10, 16, 25, 36, 51] |
| CentralE   | [0, 1, 4, 12, 28] |
| CentralO   | [0, 1, 5, 15, 34] |
| ColMiddle  | [0, 0, 1, 1, 4, 5, 12, 15, 28, 34] |
| ColLeft    | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| TransSqrs  | [0, 1, 9, 40, 135, 387, 980, 2240, 4698, 9165] |
| TransNat0  | [0, 1, 5, 16, 43, 103, 224, 448, 834, 1461] |
| TransNat1  | [0, 2, 8, 23, 58, 133, 280, 546, 996, 1716] |

Polygonal Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow1 | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]|
| DiagRow2 | [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]|
| DiagRow3 | [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]|
| DiagRow4 | [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]|
| DiagRow5 | [0, 1, 7, 18, 34, 55, 81, 112, 148, 189]|
| DiagRow6 | [0, 1, 8, 21, 40, 65, 96, 133, 176, 225]|
| DiagRow7 | [0, 1, 9, 24, 46, 75, 111, 154, 204, 261]|
| DiagRow8 | [0, 1, 10, 27, 52, 85, 126, 175, 232, 297]|
| DiagRow9 | [0, 1, 11, 30, 58, 95, 141, 196, 260, 333]|

Polygonal Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| DiagCol3 | [3, 6, 9, 12, 15, 18, 21, 24, 27, 30] |
| DiagCol4 | [4, 10, 16, 22, 28, 34, 40, 46, 52, 58] |
| DiagCol5 | [5, 15, 25, 35, 45, 55, 65, 75, 85, 95] |
| DiagCol6 | [6, 21, 36, 51, 66, 81, 96, 111, 126, 141] |
| DiagCol7 | [7, 28, 49, 70, 91, 112, 133, 154, 175, 196] |
| DiagCol8 | [8, 36, 64, 92, 120, 148, 176, 204, 232, 260] |
| DiagCol9 | [9, 45, 81, 117, 153, 189, 225, 261, 297, 333] |

Polygonal Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171] |
| PolyRow3 | [0, 7, 38, 111, 244, 455, 762, 1183, 1736, 2439] |
| PolyRow4 | [0, 15, 130, 525, 1476, 3355, 6630, 11865, 19720, 30951] |
| PolyRow5 | [0, 30, 414, 2316, 8340, 23130, 53970, 111384, 209736, 367830] |
| PolyRow6 | [0, 56, 1242, 9696, 44900, 152280, 420126, 1000832, 2136456, 4188600] |
| PolyRow7 | [0, 98, 3542, 38946, 233012, 968930, 3165738, 8713922, 21102536, 46273122] |
| PolyRow8 | [0, 162, 9682, 151302, 1174788, 6004330, 23267382, 74075022, 203646472, 499692978] |
| PolyRow9 | [0, 255, 25550, 572025, 5786580, 36430355, 167660610, 617914605, 1929694280, 5300831655] |

Polygonal Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [0, 1, 3, 7, 15, 30, 56, 98, 162, 255] |
| PolyCol2 | [0, 2, 10, 38, 130, 414, 1242, 3542, 9682, 25550] |
| PolyCol3 | [0, 3, 21, 111, 525, 2316, 9696, 38946, 151302, 572025] |
| PolyCol4 | [0, 4, 36, 244, 1476, 8340, 44900, 233012, 1174788, 5786580] |
| PolyCol5 | [0, 5, 55, 455, 3355, 23130, 152280, 968930, 6004330, 36430355] |
| PolyCol6 | [0, 6, 78, 762, 6630, 53970, 420126, 3165738, 23267382, 167660610] |
| PolyCol7 | [0, 7, 105, 1183, 11865, 111384, 1000832, 8713922, 74075022, 617914605] |
| PolyCol8 | [0, 8, 136, 1736, 19720, 209736, 2136456, 21102536, 203646472, 1929694280] |
| PolyCol9 | [0, 9, 171, 2439, 30951, 367830, 4188600, 46273122, 499692978, 5300831655] |

# Polygonal:Rev
[]

Polygonal:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [1, 0] |
| Row2 | [2, 1, 0] |
| Row3 | [3, 3, 1, 0] |
| Row4 | [4, 6, 4, 1, 0] |
| Row5 | [5, 10, 9, 5, 1, 0] |
| Row6 | [6, 15, 16, 12, 6, 1, 0] |
| Row7 | [7, 21, 25, 22, 15, 7, 1, 0] |
| Row8 | [8, 28, 36, 35, 28, 18, 8, 1, 0] |
| Row9 | [9, 36, 49, 51, 45, 34, 21, 9, 1, 0] |

Polygonal:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[0], [1, 0], [2, 1, 0], [3, 3, 1, 0], [4, 6, 4, 1, 0], [5, 10, 9, 5, 1, 0], [6, 15, 16, 12, 6, 1, 0], [7, 21, 25, 22, 15, 7, 1, 0], [8, 28, 36, 35, 28, 18, 8, 1, 0], [9, 36, 49, 51, 45, 34, 21, 9, 1, 0]] |
| RevTabl    | [[0], [0, 1], [0, 1, 2], [0, 1, 3, 3], [0, 1, 4, 6, 4], [0, 1, 5, 9, 10, 5], [0, 1, 6, 12, 16, 15, 6], [0, 1, 7, 15, 22, 25, 21, 7], [0, 1, 8, 18, 28, 35, 36, 28, 8], [0, 1, 9, 21, 34, 45, 51, 49, 36, 9]] |
| AntiDiag   | [[0], [1], [2, 0], [3, 1], [4, 3, 0], [5, 6, 1], [6, 10, 4, 0], [7, 15, 9, 1], [8, 21, 16, 5, 0], [9, 28, 25, 12, 1]] |
| AccTabl    | [[0], [1, 1], [2, 3, 3], [3, 6, 7, 7], [4, 10, 14, 15, 15], [5, 15, 24, 29, 30, 30], [6, 21, 37, 49, 55, 56, 56], [7, 28, 53, 75, 90, 97, 98, 98], [8, 36, 72, 107, 135, 153, 161, 162, 162], [9, 45, 94, 145, 190, 224, 245, 254, 255, 255]] |
| RevAccTabl | [[0], [1, 1], [3, 3, 2], [7, 7, 6, 3], [15, 15, 14, 10, 4], [30, 30, 29, 24, 15, 5], [56, 56, 55, 49, 37, 21, 6], [98, 98, 97, 90, 75, 53, 28, 7], [162, 162, 161, 153, 135, 107, 72, 36, 8], [255, 255, 254, 245, 224, 190, 145, 94, 45, 9]] |
| AccRevTabl | [[0], [0, 1], [0, 1, 3], [0, 1, 4, 7], [0, 1, 5, 11, 15], [0, 1, 6, 15, 25, 30], [0, 1, 7, 19, 35, 50, 56], [0, 1, 8, 23, 45, 70, 91, 98], [0, 1, 9, 27, 55, 90, 126, 154, 162], [0, 1, 10, 31, 65, 110, 161, 210, 246, 255]] |

Polygonal:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 1, 3, 7, 15, 30, 56, 98, 162, 255] |
| EvenSum      | [0, 1, 2, 4, 8, 15, 28, 48, 80, 125] |
| OddSum       | [0, 0, 1, 3, 7, 15, 28, 50, 82, 130] |
| AltSum       | [0, 1, 1, 1, 1, 0, 0, -2, -2, -5] |
| AccSum       | [0, 2, 8, 23, 58, 133, 280, 546, 996, 1716] |
| AccRevSum    | [0, 1, 4, 12, 32, 77, 168, 336, 624, 1089] |
| DiagSum      | [0, 1, 2, 4, 7, 12, 20, 32, 50, 75] |

Polygonal:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 3, 12, 90, 240, 11550, 2520, 149940] |
| RowGcd     | [1, 1, 2, 3, 2, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 2, 3, 6, 10, 16, 25, 36, 51] |
| CentralE   | [0, 1, 4, 12, 28] |
| CentralO   | [1, 3, 9, 22, 45] |
| ColMiddle  | [0, 1, 1, 3, 4, 9, 12, 22, 28, 45] |
| ColLeft    | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| ColRight   | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 7, 31, 107, 308, 770, 1722, 3522] |
| TransNat0  | [0, 0, 1, 5, 17, 47, 112, 238, 462, 834] |
| TransNat1  | [0, 1, 4, 12, 32, 77, 168, 336, 624, 1089] |

Polygonal:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]|
| DiagRow3 | [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]|
| DiagRow4 | [4, 10, 16, 22, 28, 34, 40, 46, 52, 58]|
| DiagRow5 | [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]|
| DiagRow6 | [6, 21, 36, 51, 66, 81, 96, 111, 126, 141]|
| DiagRow7 | [7, 28, 49, 70, 91, 112, 133, 154, 175, 196]|
| DiagRow8 | [8, 36, 64, 92, 120, 148, 176, 204, 232, 260]|
| DiagRow9 | [9, 45, 81, 117, 153, 189, 225, 261, 297, 333]|

Polygonal:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol1 | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] |
| DiagCol2 | [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] |
| DiagCol3 | [0, 1, 5, 12, 22, 35, 51, 70, 92, 117] |
| DiagCol4 | [0, 1, 6, 15, 28, 45, 66, 91, 120, 153] |
| DiagCol5 | [0, 1, 7, 18, 34, 55, 81, 112, 148, 189] |
| DiagCol6 | [0, 1, 8, 21, 40, 65, 96, 133, 176, 225] |
| DiagCol7 | [0, 1, 9, 24, 46, 75, 111, 154, 204, 261] |
| DiagCol8 | [0, 1, 10, 27, 52, 85, 126, 175, 232, 297] |
| DiagCol9 | [0, 1, 11, 30, 58, 95, 141, 196, 260, 333] |

Polygonal:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| PolyRow3 | [3, 7, 13, 21, 31, 43, 57, 73, 91, 111] |
| PolyRow4 | [4, 15, 40, 85, 156, 259, 400, 585, 820, 1111] |
| PolyRow5 | [5, 30, 117, 332, 765, 1530, 2765, 4632, 7317, 11030] |
| PolyRow6 | [6, 56, 324, 1248, 3650, 8856, 18816, 36224, 64638, 108600] |
| PolyRow7 | [7, 98, 853, 4534, 17003, 50362, 126313, 280238, 565999, 1061458] |
| PolyRow8 | [8, 162, 2152, 16022, 77688, 282298, 838472, 2148462, 4919272, 10309778] |
| PolyRow9 | [9, 255, 5245, 55395, 349545, 1564039, 5514525, 16346955, 42484585, 99598095] |

Polygonal:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyCol1 | [0, 1, 3, 7, 15, 30, 56, 98, 162, 255] |
| PolyCol2 | [0, 1, 4, 13, 40, 117, 324, 853, 2152, 5245] |
| PolyCol3 | [0, 1, 5, 21, 85, 332, 1248, 4534, 16022, 55395] |
| PolyCol4 | [0, 1, 6, 31, 156, 765, 3650, 17003, 77688, 349545] |
| PolyCol5 | [0, 1, 7, 43, 259, 1530, 8856, 50362, 282298, 1564039] |
| PolyCol6 | [0, 1, 8, 57, 400, 2765, 18816, 126313, 838472, 5514525] |
| PolyCol7 | [0, 1, 9, 73, 585, 4632, 36224, 280238, 2148462, 16346955] |
| PolyCol8 | [0, 1, 10, 91, 820, 7317, 64638, 565999, 4919272, 42484585] |
| PolyCol9 | [0, 1, 11, 111, 1111, 11030, 108600, 1061458, 10309778, 99598095] |
