# FussCatalan
['A355173', 'A030237', 'A054445']

FussCatalan Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 2] |
| Row3 | [0, 1, 3, 5] |
| Row4 | [0, 1, 4, 9, 14] |
| Row5 | [0, 1, 5, 14, 28, 42] |
| Row6 | [0, 1, 6, 20, 48, 90, 132] |
| Row7 | [0, 1, 7, 27, 75, 165, 297, 429] |
| Row8 | [0, 1, 8, 35, 110, 275, 572, 1001, 1430] |
| Row9 | [0, 1, 9, 44, 154, 429, 1001, 2002, 3432, 4862] |

FussCatalan Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 2], [0, 1, 3, 5], [0, 1, 4, 9, 14], [0, 1, 5, 14, 28, 42], [0, 1, 6, 20, 48, 90, 132], [0, 1, 7, 27, 75, 165, 297, 429], [0, 1, 8, 35, 110, 275, 572, 1001, 1430], [0, 1, 9, 44, 154, 429, 1001, 2002, 3432, 4862]] |
| RevTabl    | [[1], [1, 0], [2, 1, 0], [5, 3, 1, 0], [14, 9, 4, 1, 0], [42, 28, 14, 5, 1, 0], [132, 90, 48, 20, 6, 1, 0], [429, 297, 165, 75, 27, 7, 1, 0], [1430, 1001, 572, 275, 110, 35, 8, 1, 0], [4862, 3432, 2002, 1001, 429, 154, 44, 9, 1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 1, 2], [0, 1, 3], [0, 1, 4, 5], [0, 1, 5, 9], [0, 1, 6, 14, 14], [0, 1, 7, 20, 28]] |
| AccTabl    | [[1], [0, 1], [0, 1, 3], [0, 1, 4, 9], [0, 1, 5, 14, 28], [0, 1, 6, 20, 48, 90], [0, 1, 7, 27, 75, 165, 297], [0, 1, 8, 35, 110, 275, 572, 1001], [0, 1, 9, 44, 154, 429, 1001, 2002, 3432], [0, 1, 10, 54, 208, 637, 1638, 3640, 7072, 11934]] |
| RevAccTabl | [[1], [1, 0], [3, 1, 0], [9, 4, 1, 0], [28, 14, 5, 1, 0], [90, 48, 20, 6, 1, 0], [297, 165, 75, 27, 7, 1, 0], [1001, 572, 275, 110, 35, 8, 1, 0], [3432, 2002, 1001, 429, 154, 44, 9, 1, 0], [11934, 7072, 3640, 1638, 637, 208, 54, 10, 1, 0]] |
| AccRevTabl | [[1], [1, 1], [2, 3, 3], [5, 8, 9, 9], [14, 23, 27, 28, 28], [42, 70, 84, 89, 90, 90], [132, 222, 270, 290, 296, 297, 297], [429, 726, 891, 966, 993, 1000, 1001, 1001], [1430, 2431, 3003, 3278, 3388, 3423, 3431, 3432, 3432], [4862, 8294, 10296, 11297, 11726, 11880, 11924, 11933, 11934, 11934]] |
| DiffxTabl  | [[1], [0, 2], [0, 2, 6], [0, 2, 9, 20], [0, 2, 12, 36, 70], [0, 2, 15, 56, 140, 252], [0, 2, 18, 80, 240, 540, 924], [0, 2, 21, 108, 375, 990, 2079, 3432], [0, 2, 24, 140, 550, 1650, 4004, 8008, 12870], [0, 2, 27, 176, 770, 2574, 7007, 16016, 30888, 48620]] |

FussCatalan Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| EvenSum      | [1, 0, 2, 3, 18, 33, 186, 379, 2120, 4596] |
| OddSum       | [0, 1, 1, 6, 10, 57, 111, 622, 1312, 7338] |
| AltSum       | [1, -1, 1, -3, 8, -24, 75, -243, 808, -2742] |
| AbsSum       | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| AccSum       | [1, 1, 4, 14, 48, 165, 572, 2002, 7072, 25194] |
| AccRevSum    | [1, 2, 8, 31, 120, 465, 1804, 7007, 27248, 106080] |
| DiagSum      | [1, 0, 1, 1, 3, 4, 10, 15, 35, 56] |

FussCatalan Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 15, 252, 420, 7920, 675675, 200200, 1225224] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 2, 1, 1, 1] |
| RowMax     | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| CentralE   | [1, 1, 4, 20, 110] |
| CentralO   | [0, 1, 5, 27, 154] |
| ColMiddle  | [1, 0, 1, 1, 4, 5, 20, 27, 110, 154] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| BinConv    | [1, 1, 4, 17, 78, 377, 1888, 9697, 50746, 269393] |
| InvBinConv | [1, 1, 0, -1, -2, -3, -4, -5, -6, -7] |
| TransSqrs  | [0, 1, 9, 58, 322, 1645, 7975, 37310, 170144, 761226] |
| TransNat0  | [0, 1, 5, 22, 92, 375, 1507, 6006, 23816, 94146] |
| TransNat1  | [1, 2, 8, 31, 120, 465, 1804, 7007, 27248, 106080] |
| PosHalf    | [1, 1, 4, 15, 56, 210, 792, 3003, 11440, 43758] |
| NegHalf    | [1, 1, 0, 3, 4, 18, 48, 167, 540, 1854] |

FussCatalan Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]|
| DiagRow1 | [0, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934]|
| DiagRow2 | [0, 1, 4, 14, 48, 165, 572, 2002, 7072, 25194]|
| DiagRow3 | [0, 1, 5, 20, 75, 275, 1001, 3640, 13260, 48450]|
| DiagRow4 | [0, 1, 6, 27, 110, 429, 1638, 6188, 23256, 87210]|
| DiagRow5 | [0, 1, 7, 35, 154, 637, 2548, 9996, 38760, 149226]|
| DiagRow6 | [0, 1, 8, 44, 208, 910, 3808, 15504, 62016, 245157]|
| DiagRow7 | [0, 1, 9, 54, 273, 1260, 5508, 23256, 95931, 389367]|
| DiagRow8 | [0, 1, 10, 65, 350, 1700, 7752, 33915, 144210, 600875]|
| DiagRow9 | [0, 1, 11, 77, 440, 2244, 10659, 48279, 211508, 904475]|

FussCatalan Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| DiagCol3 | [5, 9, 14, 20, 27, 35, 44, 54, 65, 77] |
| DiagCol4 | [14, 28, 48, 75, 110, 154, 208, 273, 350, 440] |
| DiagCol5 | [42, 90, 165, 275, 429, 637, 910, 1260, 1700, 2244] |
| DiagCol6 | [132, 297, 572, 1001, 1638, 2548, 3808, 5508, 7752, 10659] |
| DiagCol7 | [429, 1001, 2002, 3640, 6188, 9996, 15504, 23256, 33915, 48279] |
| DiagCol8 | [1430, 3432, 7072, 13260, 23256, 38760, 62016, 95931, 144210, 211508] |
| DiagCol9 | [4862, 11934, 25194, 48450, 87210, 149226, 245157, 389367, 600875, 904475] |

FussCatalan Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171] |
| PolyRow3 | [0, 9, 54, 165, 372, 705, 1194, 1869, 2760, 3897] |
| PolyRow4 | [0, 28, 314, 1416, 4228, 9980, 20238, 36904, 62216, 98748] |
| PolyRow5 | [0, 90, 1926, 12900, 51156, 150630, 366090, 778176, 1498440, 2674386] |
| PolyRow6 | [0, 297, 12282, 122583, 646500, 2376405, 6925182, 17164707, 37759368, 75794625] |
| PolyRow7 | [0, 1001, 80646, 1201701, 8435252, 38722305, 135335706, 391204541, 983263176, 2219987097] |
| PolyRow8 | [0, 3432, 541690, 12065160, 112771908, 646667080, 2711042862, 9140225640, 26250094600, 66665533608] |
| PolyRow9 | [0, 11934, 3704838, 123442194, 1536846228, 11010208230, 55372879914, 217758129498, 714621614664, 2041508615598] |

FussCatalan Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| PolyCol2 | [1, 2, 10, 54, 314, 1926, 12282, 80646, 541690, 3704838] |
| PolyCol3 | [1, 3, 21, 165, 1416, 12900, 122583, 1201701, 12065160, 123442194] |
| PolyCol4 | [1, 4, 36, 372, 4228, 51156, 646500, 8435252, 112771908, 1536846228] |
| PolyCol5 | [1, 5, 55, 705, 9980, 150630, 2376405, 38722305, 646667080, 11010208230] |
| PolyCol6 | [1, 6, 78, 1194, 20238, 366090, 6925182, 135335706, 2711042862, 55372879914] |
| PolyCol7 | [1, 7, 105, 1869, 36904, 778176, 17164707, 391204541, 9140225640, 217758129498] |
| PolyCol8 | [1, 8, 136, 2760, 62216, 1498440, 37759368, 983263176, 26250094600, 714621614664] |
| PolyCol9 | [1, 9, 171, 3897, 98748, 2674386, 75794625, 2219987097, 66665533608, 2041508615598] |

# FussCatalan:Rev
[]

FussCatalan:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [2, 1, 0] |
| Row3 | [5, 3, 1, 0] |
| Row4 | [14, 9, 4, 1, 0] |
| Row5 | [42, 28, 14, 5, 1, 0] |
| Row6 | [132, 90, 48, 20, 6, 1, 0] |
| Row7 | [429, 297, 165, 75, 27, 7, 1, 0] |
| Row8 | [1430, 1001, 572, 275, 110, 35, 8, 1, 0] |
| Row9 | [4862, 3432, 2002, 1001, 429, 154, 44, 9, 1, 0] |

FussCatalan:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [2, 1, 0], [5, 3, 1, 0], [14, 9, 4, 1, 0], [42, 28, 14, 5, 1, 0], [132, 90, 48, 20, 6, 1, 0], [429, 297, 165, 75, 27, 7, 1, 0], [1430, 1001, 572, 275, 110, 35, 8, 1, 0], [4862, 3432, 2002, 1001, 429, 154, 44, 9, 1, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 2], [0, 1, 3, 5], [0, 1, 4, 9, 14], [0, 1, 5, 14, 28, 42], [0, 1, 6, 20, 48, 90, 132], [0, 1, 7, 27, 75, 165, 297, 429], [0, 1, 8, 35, 110, 275, 572, 1001, 1430], [0, 1, 9, 44, 154, 429, 1001, 2002, 3432, 4862]] |
| AntiDiag   | [[1], [1], [2, 0], [5, 1], [14, 3, 0], [42, 9, 1], [132, 28, 4, 0], [429, 90, 14, 1], [1430, 297, 48, 5, 0], [4862, 1001, 165, 20, 1]] |
| AccTabl    | [[1], [1, 1], [2, 3, 3], [5, 8, 9, 9], [14, 23, 27, 28, 28], [42, 70, 84, 89, 90, 90], [132, 222, 270, 290, 296, 297, 297], [429, 726, 891, 966, 993, 1000, 1001, 1001], [1430, 2431, 3003, 3278, 3388, 3423, 3431, 3432, 3432], [4862, 8294, 10296, 11297, 11726, 11880, 11924, 11933, 11934, 11934]] |
| RevAccTabl | [[1], [1, 1], [3, 3, 2], [9, 9, 8, 5], [28, 28, 27, 23, 14], [90, 90, 89, 84, 70, 42], [297, 297, 296, 290, 270, 222, 132], [1001, 1001, 1000, 993, 966, 891, 726, 429], [3432, 3432, 3431, 3423, 3388, 3278, 3003, 2431, 1430], [11934, 11934, 11933, 11924, 11880, 11726, 11297, 10296, 8294, 4862]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 3], [0, 1, 4, 9], [0, 1, 5, 14, 28], [0, 1, 6, 20, 48, 90], [0, 1, 7, 27, 75, 165, 297], [0, 1, 8, 35, 110, 275, 572, 1001], [0, 1, 9, 44, 154, 429, 1001, 2002, 3432], [0, 1, 10, 54, 208, 637, 1638, 3640, 7072, 11934]] |
| DiffxTabl  | [[1], [1, 0], [2, 2, 0], [5, 6, 3, 0], [14, 18, 12, 4, 0], [42, 56, 42, 20, 5, 0], [132, 180, 144, 80, 30, 6, 0], [429, 594, 495, 300, 135, 42, 7, 0], [1430, 2002, 1716, 1100, 550, 210, 56, 8, 0], [4862, 6864, 6006, 4004, 2145, 924, 308, 72, 9, 0]] |

FussCatalan:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| EvenSum      | [1, 1, 2, 6, 18, 57, 186, 622, 2120, 7338] |
| OddSum       | [0, 0, 1, 3, 10, 33, 111, 379, 1312, 4596] |
| AltSum       | [1, 1, 1, 3, 8, 24, 75, 243, 808, 2742] |
| AbsSum       | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| AccSum       | [1, 2, 8, 31, 120, 465, 1804, 7007, 27248, 106080] |
| AccRevSum    | [1, 1, 4, 14, 48, 165, 572, 2002, 7072, 25194] |
| DiagSum      | [1, 1, 2, 6, 17, 52, 164, 534, 1780, 6049] |

FussCatalan:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 15, 252, 420, 7920, 675675, 200200, 1225224] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 2, 1, 1, 1] |
| RowMax     | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| CentralE   | [1, 1, 4, 20, 110] |
| CentralO   | [1, 3, 14, 75, 429] |
| ColMiddle  | [1, 1, 1, 3, 4, 14, 20, 75, 110, 429] |
| ColLeft    | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 1, 4, 17, 78, 377, 1888, 9697, 50746, 269393] |
| InvBinConv | [1, -1, 0, 1, -2, 3, -4, 5, -6, 7] |
| TransSqrs  | [0, 0, 1, 7, 34, 145, 583, 2275, 8736, 33252] |
| TransNat0  | [0, 0, 1, 5, 20, 75, 275, 1001, 3640, 13260] |
| TransNat1  | [1, 1, 4, 14, 48, 165, 572, 2002, 7072, 25194] |
| PosHalf    | [1, 2, 10, 54, 314, 1926, 12282, 80646, 541690, 3704838] |
| NegHalf    | [1, -2, 6, -30, 166, -990, 6198, -40174, 267270, -1814526] |

FussCatalan:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]|
| DiagRow3 | [5, 9, 14, 20, 27, 35, 44, 54, 65, 77]|
| DiagRow4 | [14, 28, 48, 75, 110, 154, 208, 273, 350, 440]|
| DiagRow5 | [42, 90, 165, 275, 429, 637, 910, 1260, 1700, 2244]|
| DiagRow6 | [132, 297, 572, 1001, 1638, 2548, 3808, 5508, 7752, 10659]|
| DiagRow7 | [429, 1001, 2002, 3640, 6188, 9996, 15504, 23256, 33915, 48279]|
| DiagRow8 | [1430, 3432, 7072, 13260, 23256, 38760, 62016, 95931, 144210, 211508]|
| DiagRow9 | [4862, 11934, 25194, 48450, 87210, 149226, 245157, 389367, 600875, 904475]|

FussCatalan:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| DiagCol1 | [0, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| DiagCol2 | [0, 1, 4, 14, 48, 165, 572, 2002, 7072, 25194] |
| DiagCol3 | [0, 1, 5, 20, 75, 275, 1001, 3640, 13260, 48450] |
| DiagCol4 | [0, 1, 6, 27, 110, 429, 1638, 6188, 23256, 87210] |
| DiagCol5 | [0, 1, 7, 35, 154, 637, 2548, 9996, 38760, 149226] |
| DiagCol6 | [0, 1, 8, 44, 208, 910, 3808, 15504, 62016, 245157] |
| DiagCol7 | [0, 1, 9, 54, 273, 1260, 5508, 23256, 95931, 389367] |
| DiagCol8 | [0, 1, 10, 65, 350, 1700, 7752, 33915, 144210, 600875] |
| DiagCol9 | [0, 1, 11, 77, 440, 2244, 10659, 48279, 211508, 904475] |

FussCatalan:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| PolyRow3 | [5, 9, 15, 23, 33, 45, 59, 75, 93, 113] |
| PolyRow4 | [14, 28, 56, 104, 178, 284, 428, 616, 854, 1148] |
| PolyRow5 | [42, 90, 210, 468, 954, 1782, 3090, 5040, 7818, 11634] |
| PolyRow6 | [132, 297, 792, 2103, 5100, 11157, 22272, 41187, 71508, 117825] |
| PolyRow7 | [429, 1001, 3003, 9447, 27233, 69789, 160431, 336443, 653877, 1193073] |
| PolyRow8 | [1430, 3432, 11440, 42440, 145338, 436360, 1155332, 2747880, 5978590, 12080168] |
| PolyRow9 | [4862, 11934, 43758, 190694, 775422, 2727822, 8319134, 22441878, 54662334, 122312702] |

FussCatalan:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862] |
| PolyCol1 | [1, 1, 3, 9, 28, 90, 297, 1001, 3432, 11934] |
| PolyCol2 | [1, 1, 4, 15, 56, 210, 792, 3003, 11440, 43758] |
| PolyCol3 | [1, 1, 5, 23, 104, 468, 2103, 9447, 42440, 190694] |
| PolyCol4 | [1, 1, 6, 33, 178, 954, 5100, 27233, 145338, 775422] |
| PolyCol5 | [1, 1, 7, 45, 284, 1782, 11157, 69789, 436360, 2727822] |
| PolyCol6 | [1, 1, 8, 59, 428, 3090, 22272, 160431, 1155332, 8319134] |
| PolyCol7 | [1, 1, 9, 75, 616, 5040, 41187, 336443, 2747880, 22441878] |
| PolyCol8 | [1, 1, 10, 93, 854, 7818, 71508, 653877, 5978590, 54662334] |
| PolyCol9 | [1, 1, 11, 113, 1148, 11634, 117825, 1193073, 12080168, 122312702] |

