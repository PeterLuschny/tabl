# FiboLucasRev
['A124038']

FiboLucasRev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [2, 1] |
| Row2 | [1, 2, 1] |
| Row3 | [2, 2, 2, 1] |
| Row4 | [1, 4, 3, 2, 1] |
| Row5 | [2, 3, 6, 4, 2, 1] |
| Row6 | [1, 6, 6, 8, 5, 2, 1] |
| Row7 | [2, 4, 12, 10, 10, 6, 2, 1] |
| Row8 | [1, 8, 10, 20, 15, 12, 7, 2, 1] |
| Row9 | [2, 5, 20, 20, 30, 21, 14, 8, 2, 1] |

FiboLucasRev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [2, 1], [1, 2, 1], [2, 2, 2, 1], [1, 4, 3, 2, 1], [2, 3, 6, 4, 2, 1], [1, 6, 6, 8, 5, 2, 1], [2, 4, 12, 10, 10, 6, 2, 1], [1, 8, 10, 20, 15, 12, 7, 2, 1], [2, 5, 20, 20, 30, 21, 14, 8, 2, 1]] |
| RevTabl    | [[1], [1, 2], [1, 2, 1], [1, 2, 2, 2], [1, 2, 3, 4, 1], [1, 2, 4, 6, 3, 2], [1, 2, 5, 8, 6, 6, 1], [1, 2, 6, 10, 10, 12, 4, 2], [1, 2, 7, 12, 15, 20, 10, 8, 1], [1, 2, 8, 14, 21, 30, 20, 20, 5, 2]] |
| AntiDiag   | [[1], [2], [1, 1], [2, 2], [1, 2, 1], [2, 4, 2], [1, 3, 3, 1], [2, 6, 6, 2], [1, 4, 6, 4, 1], [2, 8, 12, 8, 2]] |
| AccTabl    | [[1], [2, 3], [1, 3, 4], [2, 4, 6, 7], [1, 5, 8, 10, 11], [2, 5, 11, 15, 17, 18], [1, 7, 13, 21, 26, 28, 29], [2, 6, 18, 28, 38, 44, 46, 47], [1, 9, 19, 39, 54, 66, 73, 75, 76], [2, 7, 27, 47, 77, 98, 112, 120, 122, 123]] |
| RevAccTabl | [[1], [3, 2], [4, 3, 1], [7, 6, 4, 2], [11, 10, 8, 5, 1], [18, 17, 15, 11, 5, 2], [29, 28, 26, 21, 13, 7, 1], [47, 46, 44, 38, 28, 18, 6, 2], [76, 75, 73, 66, 54, 39, 19, 9, 1], [123, 122, 120, 112, 98, 77, 47, 27, 7, 2]] |
| AccRevTabl | [[1], [1, 3], [1, 3, 4], [1, 3, 5, 7], [1, 3, 6, 10, 11], [1, 3, 7, 13, 16, 18], [1, 3, 8, 16, 22, 28, 29], [1, 3, 9, 19, 29, 41, 45, 47], [1, 3, 10, 22, 37, 57, 67, 75, 76], [1, 3, 11, 25, 46, 76, 96, 116, 121, 123]] |
| DiffxTabl  | [[1], [2, 2], [1, 4, 3], [2, 4, 6, 4], [1, 8, 9, 8, 5], [2, 6, 18, 16, 10, 6], [1, 12, 18, 32, 25, 12, 7], [2, 8, 36, 40, 50, 36, 14, 8], [1, 16, 30, 80, 75, 72, 49, 16, 9], [2, 10, 60, 80, 150, 126, 98, 64, 18, 10]] |

FiboLucasRev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| EvenSum      | [1, 2, 2, 4, 5, 10, 13, 26, 34, 68] |
| OddSum       | [0, 1, 2, 3, 6, 8, 16, 21, 42, 55] |
| AltSum       | [1, 1, 0, 1, -1, 2, -3, 5, -8, 13] |
| AbsSum       | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| AccSum       | [1, 5, 8, 19, 35, 68, 125, 229, 412, 735] |
| AccRevSum    | [1, 4, 8, 16, 31, 58, 107, 194, 348, 618] |
| DiagSum      | [1, 2, 2, 4, 4, 8, 8, 16, 16, 32] |

FiboLucasRev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 2, 2, 12, 12, 120, 60, 840, 840] |
| RowGcd     | [1, 2, 2, 2, 1, 1, 1, 2, 1, 1] |
| RowMax     | [1, 2, 2, 2, 4, 6, 8, 12, 20, 30] |
| CentralE   | [1, 2, 3, 8, 15] |
| CentralO   | [2, 2, 6, 10, 30] |
| ColMiddle  | [1, 2, 2, 2, 3, 6, 8, 10, 15, 30] |
| ColLeft    | [1, 2, 1, 2, 1, 2, 1, 2, 1, 2] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 3, 6, 15, 44, 128, 375, 1123, 3400, 10356] |
| InvBinConv | [1, -1, -2, -1, -4, -16, -41, -113, -344, -1036] |
| TransSqrs  | [0, 1, 6, 19, 50, 120, 268, 573, 1182, 2375] |
| TransNat0  | [0, 1, 4, 9, 20, 40, 78, 147, 272, 495] |
| TransNat1  | [1, 4, 8, 16, 31, 58, 107, 194, 348, 618] |
| PosHalf    | [1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589] |
| NegHalf    | [1, -3, 1, -11, -7, -51, -79, -283, -599, -1731] |

FiboLucasRev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]|
| DiagRow2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]|
| DiagRow3 | [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]|
| DiagRow4 | [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]|
| DiagRow5 | [2, 6, 12, 20, 30, 42, 56, 72, 90, 110]|
| DiagRow6 | [1, 4, 10, 20, 35, 56, 84, 120, 165, 220]|
| DiagRow7 | [2, 8, 20, 40, 70, 112, 168, 240, 330, 440]|
| DiagRow8 | [1, 5, 15, 35, 70, 126, 210, 330, 495, 715]|
| DiagRow9 | [2, 10, 30, 70, 140, 252, 420, 660, 990, 1430]|

FiboLucasRev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 2, 1, 2, 1, 2, 1, 2, 1, 2] |
| DiagCol1 | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| DiagCol2 | [1, 2, 3, 6, 6, 12, 10, 20, 15, 30] |
| DiagCol3 | [1, 2, 4, 8, 10, 20, 20, 40, 35, 70] |
| DiagCol4 | [1, 2, 5, 10, 15, 30, 35, 70, 70, 140] |
| DiagCol5 | [1, 2, 6, 12, 21, 42, 56, 112, 126, 252] |
| DiagCol6 | [1, 2, 7, 14, 28, 56, 84, 168, 210, 420] |
| DiagCol7 | [1, 2, 8, 16, 36, 72, 120, 240, 330, 660] |
| DiagCol8 | [1, 2, 9, 18, 45, 90, 165, 330, 495, 990] |
| DiagCol9 | [1, 2, 10, 20, 55, 110, 220, 440, 715, 1430] |

FiboLucasRev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| PolyRow2 | [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] |
| PolyRow3 | [2, 7, 22, 53, 106, 187, 302, 457, 658, 911] |
| PolyRow4 | [1, 11, 53, 175, 449, 971, 1861, 3263, 5345, 8299] |
| PolyRow5 | [2, 18, 128, 578, 1902, 5042, 11468, 23298, 43418, 75602] |
| PolyRow6 | [1, 29, 309, 1909, 8057, 26181, 70669, 166349, 352689, 688717] |
| PolyRow7 | [2, 47, 746, 6305, 34130, 135947, 435482, 1187741, 2864930, 6274055] |
| PolyRow8 | [1, 76, 1801, 20824, 144577, 705916, 2683561, 8480536, 23272129, 57155212] |
| PolyRow9 | [2, 123, 4348, 68777, 612438, 3665527, 16536848, 60551493, 189041962, 520670963] |

FiboLucasRev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 2, 1, 2, 1, 2, 1, 2, 1, 2] |
| PolyCol1 | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| PolyCol2 | [1, 4, 9, 22, 53, 128, 309, 746, 1801, 4348] |
| PolyCol3 | [1, 5, 16, 53, 175, 578, 1909, 6305, 20824, 68777] |
| PolyCol4 | [1, 6, 25, 106, 449, 1902, 8057, 34130, 144577, 612438] |
| PolyCol5 | [1, 7, 36, 187, 971, 5042, 26181, 135947, 705916, 3665527] |
| PolyCol6 | [1, 8, 49, 302, 1861, 11468, 70669, 435482, 2683561, 16536848] |
| PolyCol7 | [1, 9, 64, 457, 3263, 23298, 166349, 1187741, 8480536, 60551493] |
| PolyCol8 | [1, 10, 81, 658, 5345, 43418, 352689, 2864930, 23272129, 189041962] |
| PolyCol9 | [1, 11, 100, 911, 8299, 75602, 688717, 6274055, 57155212, 520670963] |

# FiboLucasRev:Inv
[]

FiboLucasRev:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [-2, 1] |
| Row2 | [3, -2, 1] |
| Row3 | [-4, 2, -2, 1] |
| Row4 | [6, -2, 1, -2, 1] |
| Row5 | [-10, 5, 0, 0, -2, 1] |
| Row6 | [15, -10, 5, 2, -1, -2, 1] |
| Row7 | [-20, 10, -12, 6, 4, -2, -2, 1] |
| Row8 | [30, -8, 4, -16, 8, 6, -3, -2, 1] |
| Row9 | [-52, 26, 8, -4, -22, 11, 8, -4, -2, 1] |

FiboLucasRev:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [-2, 1], [3, -2, 1], [-4, 2, -2, 1], [6, -2, 1, -2, 1], [-10, 5, 0, 0, -2, 1], [15, -10, 5, 2, -1, -2, 1], [-20, 10, -12, 6, 4, -2, -2, 1], [30, -8, 4, -16, 8, 6, -3, -2, 1], [-52, 26, 8, -4, -22, 11, 8, -4, -2, 1]] |
| RevTabl    | [[1], [1, -2], [1, -2, 3], [1, -2, 2, -4], [1, -2, 1, -2, 6], [1, -2, 0, 0, 5, -10], [1, -2, -1, 2, 5, -10, 15], [1, -2, -2, 4, 6, -12, 10, -20], [1, -2, -3, 6, 8, -16, 4, -8, 30], [1, -2, -4, 8, 11, -22, -4, 8, 26, -52]] |
| AntiDiag   | [[1], [-2], [3, 1], [-4, -2], [6, 2, 1], [-10, -2, -2], [15, 5, 1, 1], [-20, -10, 0, -2], [30, 10, 5, 0, 1], [-52, -8, -12, 2, -2]] |
| AccTabl    | [[1], [-2, -1], [3, 1, 2], [-4, -2, -4, -3], [6, 4, 5, 3, 4], [-10, -5, -5, -5, -7, -6], [15, 5, 10, 12, 11, 9, 10], [-20, -10, -22, -16, -12, -14, -16, -15], [30, 22, 26, 10, 18, 24, 21, 19, 20], [-52, -26, -18, -22, -44, -33, -25, -29, -31, -30]] |
| RevAccTabl | [[1], [-1, -2], [2, 1, 3], [-3, -4, -2, -4], [4, 3, 5, 4, 6], [-6, -7, -5, -5, -5, -10], [10, 9, 11, 12, 10, 5, 15], [-15, -16, -14, -12, -16, -22, -10, -20], [20, 19, 21, 24, 18, 10, 26, 22, 30], [-30, -31, -29, -25, -33, -44, -22, -18, -26, -52]] |
| AccRevTabl | [[1], [1, -1], [1, -1, 2], [1, -1, 1, -3], [1, -1, 0, -2, 4], [1, -1, -1, -1, 4, -6], [1, -1, -2, 0, 5, -5, 10], [1, -1, -3, 1, 7, -5, 5, -15], [1, -1, -4, 2, 10, -6, -2, -10, 20], [1, -1, -5, 3, 14, -8, -12, -4, 22, -30]] |
| DiffxTabl  | [[1], [-2, 2], [3, -4, 3], [-4, 4, -6, 4], [6, -4, 3, -8, 5], [-10, 10, 0, 0, -10, 6], [15, -20, 15, 8, -5, -12, 7], [-20, 20, -36, 24, 20, -12, -14, 8], [30, -16, 12, -64, 40, 36, -21, -16, 9], [-52, 52, 24, -16, -110, 66, 56, -32, -18, 10]] |

FiboLucasRev:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, -1, 2, -3, 4, -6, 10, -15, 20, -30] |
| EvenSum      | [1, -2, 4, -6, 8, -12, 20, -30, 40, -60] |
| OddSum       | [0, 1, -2, 3, -4, 6, -10, 15, -20, 30] |
| AltSum       | [1, -3, 6, -9, 12, -18, 30, -45, 60, -90] |
| AbsSum       | [1, 3, 6, 9, 12, 18, 36, 57, 78, 138] |
| AccSum       | [1, -3, 6, -13, 22, -38, 72, -125, 190, -310] |
| AccRevSum    | [1, 0, 2, -2, 2, -4, 8, -10, 10, -20] |
| DiagSum      | [1, -2, 4, -6, 9, -14, 22, -32, 46, -72] |

FiboLucasRev:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 6, 4, 6, 10, 30, 60, 240, 1144] |
| RowGcd     | [1, 2, 1, 2, 2, 1, 1, 2, 1, 1] |
| RowMax     | [1, 2, 3, 4, 6, 10, 15, 20, 30, 52] |
| CentralE   | [1, -2, 1, 2, 8] |
| CentralO   | [-2, 2, 0, 6, -22] |
| ColMiddle  | [1, -2, -2, 2, 1, 0, 2, 6, 8, -22] |
| ColLeft    | [1, -2, 3, -4, 6, -10, 15, -20, 30, -52] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, -1, 0, -3, -3, 6, 44, 93, -21, -741] |
| InvBinConv | [1, 3, 8, 17, 29, 46, 108, 385, 1259, 3023] |
| TransSqrs  | [0, 1, 2, 3, 0, -2, -2, 7, 0, -10] |
| TransNat0  | [0, 1, 0, 1, -2, 2, -2, 5, -10, 10] |
| TransNat1  | [1, 0, 2, -2, 2, -4, 8, -10, 10, -20] |
| PosHalf    | [1, -3, 9, -27, 81, -243, 729, -2187, 6561, -19683] |
| NegHalf    | [1, 5, 17, 45, 121, 405, 1345, 3645, 9545, 32805] |

FiboLucasRev:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]|
| DiagRow2 | [3, 2, 1, 0, -1, -2, -3, -4, -5, -6]|
| DiagRow3 | [-4, -2, 0, 2, 4, 6, 8, 10, 12, 14]|
| DiagRow4 | [6, 5, 5, 6, 8, 11, 15, 20, 26, 33]|
| DiagRow5 | [-10, -10, -12, -16, -22, -30, -40, -52, -66, -82]|
| DiagRow6 | [15, 10, 4, -4, -15, -30, -50, -76, -109, -150]|
| DiagRow7 | [-20, -8, 8, 30, 60, 100, 152, 218, 300, 400]|
| DiagRow8 | [30, 26, 30, 45, 75, 125, 201, 310, 460, 660]|
| DiagRow9 | [-52, -60, -90, -150, -250, -402, -620, -920, -1320, -1840]|

FiboLucasRev:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, -2, 3, -4, 6, -10, 15, -20, 30, -52] |
| DiagCol1 | [1, -2, 2, -2, 5, -10, 10, -8, 26, -60] |
| DiagCol2 | [1, -2, 1, 0, 5, -12, 4, 8, 30, -90] |
| DiagCol3 | [1, -2, 0, 2, 6, -16, -4, 30, 45, -150] |
| DiagCol4 | [1, -2, -1, 4, 8, -22, -15, 60, 75, -250] |
| DiagCol5 | [1, -2, -2, 6, 11, -30, -30, 100, 125, -402] |
| DiagCol6 | [1, -2, -3, 8, 15, -40, -50, 152, 201, -620] |
| DiagCol7 | [1, -2, -4, 10, 20, -52, -76, 218, 310, -920] |
| DiagCol8 | [1, -2, -5, 12, 26, -66, -109, 300, 460, -1320] |
| DiagCol9 | [1, -2, -6, 14, 33, -82, -150, 400, 660, -1840] |

FiboLucasRev:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7] |
| PolyRow2 | [3, 2, 3, 6, 11, 18, 27, 38, 51, 66] |
| PolyRow3 | [-4, -3, 0, 11, 36, 81, 152, 255, 396, 581] |
| PolyRow4 | [6, 4, 6, 36, 142, 396, 894, 1756, 3126, 5172] |
| PolyRow5 | [-10, -6, 0, 86, 522, 1890, 5204, 12030, 24606, 45962] |
| PolyRow6 | [15, 10, 15, 246, 1975, 9090, 30375, 82510, 193791, 408570] |
| PolyRow7 | [-20, -15, 0, 631, 7380, 43605, 177160, 565755, 1526076, 3631705] |
| PolyRow8 | [30, 20, 30, 1716, 27710, 209340, 1033470, 3879500, 12017886, 32281860] |
| PolyRow9 | [-52, -30, 0, 4526, 103860, 1004778, 6028520, 26602230, 94640796, 286949810] |

FiboLucasRev:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, -2, 3, -4, 6, -10, 15, -20, 30, -52] |
| PolyCol1 | [1, -1, 2, -3, 4, -6, 10, -15, 20, -30] |
| PolyCol2 | [1, 0, 3, 0, 6, 0, 15, 0, 30, 0] |
| PolyCol3 | [1, 1, 6, 11, 36, 86, 246, 631, 1716, 4526] |
| PolyCol4 | [1, 2, 11, 36, 142, 522, 1975, 7380, 27710, 103860] |
| PolyCol5 | [1, 3, 18, 81, 396, 1890, 9090, 43605, 209340, 1004778] |
| PolyCol6 | [1, 4, 27, 152, 894, 5204, 30375, 177160, 1033470, 6028520] |
| PolyCol7 | [1, 5, 38, 255, 1756, 12030, 82510, 565755, 3879500, 26602230] |
| PolyCol8 | [1, 6, 51, 396, 3126, 24606, 193791, 1526076, 12017886, 94640796] |
| PolyCol9 | [1, 7, 66, 581, 5172, 45962, 408570, 3631705, 32281860, 286949810] |

# FiboLucasRev:Rev
[]

FiboLucasRev:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 2] |
| Row2 | [1, 2, 1] |
| Row3 | [1, 2, 2, 2] |
| Row4 | [1, 2, 3, 4, 1] |
| Row5 | [1, 2, 4, 6, 3, 2] |
| Row6 | [1, 2, 5, 8, 6, 6, 1] |
| Row7 | [1, 2, 6, 10, 10, 12, 4, 2] |
| Row8 | [1, 2, 7, 12, 15, 20, 10, 8, 1] |
| Row9 | [1, 2, 8, 14, 21, 30, 20, 20, 5, 2] |

FiboLucasRev:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 2], [1, 2, 1], [1, 2, 2, 2], [1, 2, 3, 4, 1], [1, 2, 4, 6, 3, 2], [1, 2, 5, 8, 6, 6, 1], [1, 2, 6, 10, 10, 12, 4, 2], [1, 2, 7, 12, 15, 20, 10, 8, 1], [1, 2, 8, 14, 21, 30, 20, 20, 5, 2]] |
| RevTabl    | [[1], [2, 1], [1, 2, 1], [2, 2, 2, 1], [1, 4, 3, 2, 1], [2, 3, 6, 4, 2, 1], [1, 6, 6, 8, 5, 2, 1], [2, 4, 12, 10, 10, 6, 2, 1], [1, 8, 10, 20, 15, 12, 7, 2, 1], [2, 5, 20, 20, 30, 21, 14, 8, 2, 1]] |
| AntiDiag   | [[1], [1], [1, 2], [1, 2], [1, 2, 1], [1, 2, 2], [1, 2, 3, 2], [1, 2, 4, 4], [1, 2, 5, 6, 1], [1, 2, 6, 8, 3]] |
| AccTabl    | [[1], [1, 3], [1, 3, 4], [1, 3, 5, 7], [1, 3, 6, 10, 11], [1, 3, 7, 13, 16, 18], [1, 3, 8, 16, 22, 28, 29], [1, 3, 9, 19, 29, 41, 45, 47], [1, 3, 10, 22, 37, 57, 67, 75, 76], [1, 3, 11, 25, 46, 76, 96, 116, 121, 123]] |
| RevAccTabl | [[1], [3, 1], [4, 3, 1], [7, 5, 3, 1], [11, 10, 6, 3, 1], [18, 16, 13, 7, 3, 1], [29, 28, 22, 16, 8, 3, 1], [47, 45, 41, 29, 19, 9, 3, 1], [76, 75, 67, 57, 37, 22, 10, 3, 1], [123, 121, 116, 96, 76, 46, 25, 11, 3, 1]] |
| AccRevTabl | [[1], [2, 3], [1, 3, 4], [2, 4, 6, 7], [1, 5, 8, 10, 11], [2, 5, 11, 15, 17, 18], [1, 7, 13, 21, 26, 28, 29], [2, 6, 18, 28, 38, 44, 46, 47], [1, 9, 19, 39, 54, 66, 73, 75, 76], [2, 7, 27, 47, 77, 98, 112, 120, 122, 123]] |
| DiffxTabl  | [[1], [1, 4], [1, 4, 3], [1, 4, 6, 8], [1, 4, 9, 16, 5], [1, 4, 12, 24, 15, 12], [1, 4, 15, 32, 30, 36, 7], [1, 4, 18, 40, 50, 72, 28, 16], [1, 4, 21, 48, 75, 120, 70, 64, 9], [1, 4, 24, 56, 105, 180, 140, 160, 45, 20]] |

FiboLucasRev:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| EvenSum      | [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] |
| OddSum       | [0, 2, 2, 4, 6, 10, 16, 26, 42, 68] |
| AltSum       | [1, -1, 0, -1, -1, -2, -3, -5, -8, -13] |
| AbsSum       | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| AccSum       | [1, 4, 8, 16, 31, 58, 107, 194, 348, 618] |
| AccRevSum    | [1, 5, 8, 19, 35, 68, 125, 229, 412, 735] |
| DiagSum      | [1, 1, 3, 3, 4, 5, 8, 11, 15, 20] |

FiboLucasRev:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 2, 2, 12, 12, 120, 60, 840, 840] |
| RowGcd     | [1, 2, 2, 2, 1, 1, 1, 2, 1, 1] |
| RowMax     | [1, 2, 2, 2, 4, 6, 8, 12, 20, 30] |
| CentralE   | [1, 2, 3, 8, 15] |
| CentralO   | [1, 2, 4, 10, 21] |
| ColMiddle  | [1, 1, 2, 2, 3, 4, 8, 10, 15, 21] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 2, 1, 2, 1, 2, 1, 2, 1, 2] |
| BinConv    | [1, 3, 6, 15, 44, 128, 375, 1123, 3400, 10356] |
| InvBinConv | [1, 1, -2, 1, -4, 16, -41, 113, -344, 1036] |
| TransSqrs  | [0, 2, 6, 28, 66, 170, 376, 818, 1694, 3428] |
| TransNat0  | [0, 2, 4, 12, 24, 50, 96, 182, 336, 612] |
| TransNat1  | [1, 5, 8, 19, 35, 68, 125, 229, 412, 735] |
| PosHalf    | [1, 4, 9, 22, 53, 128, 309, 746, 1801, 4348] |
| NegHalf    | [1, 0, 1, -2, 5, -12, 29, -70, 169, -408] |

FiboLucasRev:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]|
| DiagRow1 | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10]|
| DiagRow2 | [1, 2, 3, 6, 6, 12, 10, 20, 15, 30]|
| DiagRow3 | [1, 2, 4, 8, 10, 20, 20, 40, 35, 70]|
| DiagRow4 | [1, 2, 5, 10, 15, 30, 35, 70, 70, 140]|
| DiagRow5 | [1, 2, 6, 12, 21, 42, 56, 112, 126, 252]|
| DiagRow6 | [1, 2, 7, 14, 28, 56, 84, 168, 210, 420]|
| DiagRow7 | [1, 2, 8, 16, 36, 72, 120, 240, 330, 660]|
| DiagRow8 | [1, 2, 9, 18, 45, 90, 165, 330, 495, 990]|
| DiagRow9 | [1, 2, 10, 20, 55, 110, 220, 440, 715, 1430]|

FiboLucasRev:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] |
| DiagCol2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| DiagCol3 | [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] |
| DiagCol4 | [1, 3, 6, 10, 15, 21, 28, 36, 45, 55] |
| DiagCol5 | [2, 6, 12, 20, 30, 42, 56, 72, 90, 110] |
| DiagCol6 | [1, 4, 10, 20, 35, 56, 84, 120, 165, 220] |
| DiagCol7 | [2, 8, 20, 40, 70, 112, 168, 240, 330, 440] |
| DiagCol8 | [1, 5, 15, 35, 70, 126, 210, 330, 495, 715] |
| DiagCol9 | [2, 10, 30, 70, 140, 252, 420, 660, 990, 1430] |

FiboLucasRev:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] |
| PolyRow2 | [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] |
| PolyRow3 | [1, 7, 29, 79, 169, 311, 517, 799, 1169, 1639] |
| PolyRow4 | [1, 11, 65, 223, 569, 1211, 2281, 3935, 6353, 9739] |
| PolyRow5 | [1, 18, 181, 934, 3273, 8986, 20893, 43086, 81169, 142498] |
| PolyRow6 | [1, 29, 441, 2941, 12377, 39261, 103009, 235901, 487761, 931357] |
| PolyRow7 | [1, 47, 1165, 11347, 64745, 263911, 855157, 2347115, 5682577, 12473695] |
| PolyRow8 | [1, 76, 2929, 37816, 262777, 1245436, 4563481, 13906264, 36899281, 87913612] |
| PolyRow9 | [1, 123, 7589, 139939, 1298697, 7843211, 35349133, 128914899, 400584209, 1098282907] |

FiboLucasRev:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 3, 4, 7, 11, 18, 29, 47, 76, 123] |
| PolyCol2 | [1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589] |
| PolyCol3 | [1, 7, 16, 79, 223, 934, 2941, 11347, 37816, 139939] |
| PolyCol4 | [1, 9, 25, 169, 569, 3273, 12377, 64745, 262777, 1298697] |
| PolyCol5 | [1, 11, 36, 311, 1211, 8986, 39261, 263911, 1245436, 7843211] |
| PolyCol6 | [1, 13, 49, 517, 2281, 20893, 103009, 855157, 4563481, 35349133] |
| PolyCol7 | [1, 15, 64, 799, 3935, 43086, 235901, 2347115, 13906264, 128914899] |
| PolyCol8 | [1, 17, 81, 1169, 6353, 81169, 487761, 5682577, 36899281, 400584209] |
| PolyCol9 | [1, 19, 100, 1639, 9739, 142498, 931357, 12473695, 87913612, 1098282907] |

# FiboLucasRev:Inv:Rev
[]

FiboLucasRev:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, -2] |
| Row2 | [1, -2, 3] |
| Row3 | [1, -2, 2, -4] |
| Row4 | [1, -2, 1, -2, 6] |
| Row5 | [1, -2, 0, 0, 5, -10] |
| Row6 | [1, -2, -1, 2, 5, -10, 15] |
| Row7 | [1, -2, -2, 4, 6, -12, 10, -20] |
| Row8 | [1, -2, -3, 6, 8, -16, 4, -8, 30] |
| Row9 | [1, -2, -4, 8, 11, -22, -4, 8, 26, -52] |

FiboLucasRev:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, -2], [1, -2, 3], [1, -2, 2, -4], [1, -2, 1, -2, 6], [1, -2, 0, 0, 5, -10], [1, -2, -1, 2, 5, -10, 15], [1, -2, -2, 4, 6, -12, 10, -20], [1, -2, -3, 6, 8, -16, 4, -8, 30], [1, -2, -4, 8, 11, -22, -4, 8, 26, -52]] |
| RevTabl    | [[1], [-2, 1], [3, -2, 1], [-4, 2, -2, 1], [6, -2, 1, -2, 1], [-10, 5, 0, 0, -2, 1], [15, -10, 5, 2, -1, -2, 1], [-20, 10, -12, 6, 4, -2, -2, 1], [30, -8, 4, -16, 8, 6, -3, -2, 1], [-52, 26, 8, -4, -22, 11, 8, -4, -2, 1]] |
| AntiDiag   | [[1], [1], [1, -2], [1, -2], [1, -2, 3], [1, -2, 2], [1, -2, 1, -4], [1, -2, 0, -2], [1, -2, -1, 0, 6], [1, -2, -2, 2, 5]] |
| AccTabl    | [[1], [1, -1], [1, -1, 2], [1, -1, 1, -3], [1, -1, 0, -2, 4], [1, -1, -1, -1, 4, -6], [1, -1, -2, 0, 5, -5, 10], [1, -1, -3, 1, 7, -5, 5, -15], [1, -1, -4, 2, 10, -6, -2, -10, 20], [1, -1, -5, 3, 14, -8, -12, -4, 22, -30]] |
| RevAccTabl | [[1], [-1, 1], [2, -1, 1], [-3, 1, -1, 1], [4, -2, 0, -1, 1], [-6, 4, -1, -1, -1, 1], [10, -5, 5, 0, -2, -1, 1], [-15, 5, -5, 7, 1, -3, -1, 1], [20, -10, -2, -6, 10, 2, -4, -1, 1], [-30, 22, -4, -12, -8, 14, 3, -5, -1, 1]] |
| AccRevTabl | [[1], [-2, -1], [3, 1, 2], [-4, -2, -4, -3], [6, 4, 5, 3, 4], [-10, -5, -5, -5, -7, -6], [15, 5, 10, 12, 11, 9, 10], [-20, -10, -22, -16, -12, -14, -16, -15], [30, 22, 26, 10, 18, 24, 21, 19, 20], [-52, -26, -18, -22, -44, -33, -25, -29, -31, -30]] |
| DiffxTabl  | [[1], [1, -4], [1, -4, 9], [1, -4, 6, -16], [1, -4, 3, -8, 30], [1, -4, 0, 0, 25, -60], [1, -4, -3, 8, 25, -60, 105], [1, -4, -6, 16, 30, -72, 70, -160], [1, -4, -9, 24, 40, -96, 28, -64, 270], [1, -4, -12, 32, 55, -132, -28, 64, 234, -520]] |

FiboLucasRev:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, -1, 2, -3, 4, -6, 10, -15, 20, -30] |
| EvenSum      | [1, 1, 4, 3, 8, 6, 20, 15, 40, 30] |
| OddSum       | [0, -2, -2, -6, -4, -12, -10, -30, -20, -60] |
| AltSum       | [1, 3, 6, 9, 12, 18, 30, 45, 60, 90] |
| AbsSum       | [1, 3, 6, 9, 12, 18, 36, 57, 78, 138] |
| AccSum       | [1, 0, 2, -2, 2, -4, 8, -10, 10, -20] |
| AccRevSum    | [1, -3, 6, -13, 22, -38, 72, -125, 190, -310] |
| DiagSum      | [1, 1, -1, -1, 2, 1, -4, -3, 4, 4] |

FiboLucasRev:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 6, 4, 6, 10, 30, 60, 240, 1144] |
| RowGcd     | [1, 2, 1, 2, 2, 1, 1, 2, 1, 1] |
| RowMax     | [1, 2, 3, 4, 6, 10, 15, 20, 30, 52] |
| CentralE   | [1, -2, 1, 2, 8] |
| CentralO   | [1, -2, 0, 4, 11] |
| ColMiddle  | [1, 1, -2, -2, 1, 0, 2, 4, 8, 11] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, -2, 3, -4, 6, -10, 15, -20, 30, -52] |
| BinConv    | [1, -1, 0, -3, -3, 6, 44, 93, -21, -741] |
| InvBinConv | [1, -3, 8, -17, 29, -46, 108, -385, 1259, -3023] |
| TransSqrs  | [0, -2, 10, -30, 80, -172, 382, -798, 1440, -2620] |
| TransNat0  | [0, -2, 4, -10, 18, -32, 62, -110, 170, -280] |
| TransNat1  | [1, -3, 6, -13, 22, -38, 72, -125, 190, -310] |
| PosHalf    | [1, 0, 3, 0, 6, 0, 15, 0, 30, 0] |
| NegHalf    | [1, -4, 11, -24, 46, -84, 151, -264, 446, -744] |

FiboLucasRev:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, -2, 3, -4, 6, -10, 15, -20, 30, -52]|
| DiagRow1 | [1, -2, 2, -2, 5, -10, 10, -8, 26, -60]|
| DiagRow2 | [1, -2, 1, 0, 5, -12, 4, 8, 30, -90]|
| DiagRow3 | [1, -2, 0, 2, 6, -16, -4, 30, 45, -150]|
| DiagRow4 | [1, -2, -1, 4, 8, -22, -15, 60, 75, -250]|
| DiagRow5 | [1, -2, -2, 6, 11, -30, -30, 100, 125, -402]|
| DiagRow6 | [1, -2, -3, 8, 15, -40, -50, 152, 201, -620]|
| DiagRow7 | [1, -2, -4, 10, 20, -52, -76, 218, 310, -920]|
| DiagRow8 | [1, -2, -5, 12, 26, -66, -109, 300, 460, -1320]|
| DiagRow9 | [1, -2, -6, 14, 33, -82, -150, 400, 660, -1840]|

FiboLucasRev:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2] |
| DiagCol2 | [3, 2, 1, 0, -1, -2, -3, -4, -5, -6] |
| DiagCol3 | [-4, -2, 0, 2, 4, 6, 8, 10, 12, 14] |
| DiagCol4 | [6, 5, 5, 6, 8, 11, 15, 20, 26, 33] |
| DiagCol5 | [-10, -10, -12, -16, -22, -30, -40, -52, -66, -82] |
| DiagCol6 | [15, 10, 4, -4, -15, -30, -50, -76, -109, -150] |
| DiagCol7 | [-20, -8, 8, 30, 60, 100, 152, 218, 300, 400] |
| DiagCol8 | [30, 26, 30, 45, 75, 125, 201, 310, 460, 660] |
| DiagCol9 | [-52, -60, -90, -150, -250, -402, -620, -920, -1320, -1840] |

FiboLucasRev:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, -1, -3, -5, -7, -9, -11, -13, -15, -17] |
| PolyRow2 | [1, 2, 9, 22, 41, 66, 97, 134, 177, 226] |
| PolyRow3 | [1, -3, -27, -95, -231, -459, -803, -1287, -1935, -2771] |
| PolyRow4 | [1, 4, 81, 436, 1417, 3516, 7369, 13756, 23601, 37972] |
| PolyRow5 | [1, -6, -243, -2030, -8967, -28134, -71291, -156078, -307215, -557702] |
| PolyRow6 | [1, 10, 729, 8950, 52585, 206466, 628945, 1609294, 3625905, 7415290] |
| PolyRow7 | [1, -15, -2187, -38795, -297255, -1439559, -5216915, -15480387, -39688335, -91011455] |
| PolyRow8 | [1, 20, 6561, 179140, 1837385, 11111916, 48222745, 166578476, 487099185, 1254375460] |
| PolyRow9 | [1, -30, -19683, -842630, -11832135, -90904734, -478472555, -1942725798, -6528057615, -18991734110] |

FiboLucasRev:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, -1, 2, -3, 4, -6, 10, -15, 20, -30] |
| PolyCol2 | [1, -3, 9, -27, 81, -243, 729, -2187, 6561, -19683] |
| PolyCol3 | [1, -5, 22, -95, 436, -2030, 8950, -38795, 179140, -842630] |
| PolyCol4 | [1, -7, 41, -231, 1417, -8967, 52585, -297255, 1837385, -11832135] |
| PolyCol5 | [1, -9, 66, -459, 3516, -28134, 206466, -1439559, 11111916, -90904734] |
| PolyCol6 | [1, -11, 97, -803, 7369, -71291, 628945, -5216915, 48222745, -478472555] |
| PolyCol7 | [1, -13, 134, -1287, 13756, -156078, 1609294, -15480387, 166578476, -1942725798] |
| PolyCol8 | [1, -15, 177, -1935, 23601, -307215, 3625905, -39688335, 487099185, -6528057615] |
| PolyCol9 | [1, -17, 226, -2771, 37972, -557702, 7415290, -91011455, 1254375460, -18991734110] |

