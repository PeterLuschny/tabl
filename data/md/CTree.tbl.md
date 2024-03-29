# CTree
['A106465', 'A106470']

CTree Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 1] |
| Row2 | [1, 0, 1] |
| Row3 | [1, 1, 1, 1] |
| Row4 | [1, 0, 1, 0, 1] |
| Row5 | [1, 1, 1, 1, 1, 1] |
| Row6 | [1, 0, 1, 0, 1, 0, 1] |
| Row7 | [1, 1, 1, 1, 1, 1, 1, 1] |
| Row8 | [1, 0, 1, 0, 1, 0, 1, 0, 1] |
| Row9 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |

CTree Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] |
| RevTabl    | [[1], [1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] |
| AntiDiag   | [[1], [1], [1, 1], [1, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]] |
| AccTabl    | [[1], [1, 2], [1, 1, 2], [1, 2, 3, 4], [1, 1, 2, 2, 3], [1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |
| RevAccTabl | [[1], [2, 1], [2, 1, 1], [4, 3, 2, 1], [3, 2, 2, 1, 1], [6, 5, 4, 3, 2, 1], [4, 3, 3, 2, 2, 1, 1], [8, 7, 6, 5, 4, 3, 2, 1], [5, 4, 4, 3, 3, 2, 2, 1, 1], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]] |
| AccRevTabl | [[1], [1, 2], [1, 1, 2], [1, 2, 3, 4], [1, 1, 2, 2, 3], [1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |
| DiffxTabl  | [[1], [1, 2], [1, 0, 3], [1, 2, 3, 4], [1, 0, 3, 0, 5], [1, 2, 3, 4, 5, 6], [1, 0, 3, 0, 5, 0, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 0, 3, 0, 5, 0, 7, 0, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |

CTree Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| EvenSum      | [1, 1, 2, 2, 3, 3, 4, 4, 5, 5] |
| OddSum       | [0, 1, 0, 2, 0, 3, 0, 4, 0, 5] |
| AltSum       | [1, 0, 2, 0, 3, 0, 4, 0, 5, 0] |
| AbsSum       | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| AccSum       | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| AccRevSum    | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| DiagSum      | [1, 1, 2, 1, 3, 2, 4, 2, 5, 3] |

CTree Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| CentralE   | [1, 0, 1, 0, 1] |
| CentralO   | [1, 1, 1, 1, 1] |
| ColMiddle  | [1, 1, 0, 1, 1, 1, 0, 1, 1, 1] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 2, 2, 8, 8, 32, 32, 128, 128, 512] |
| InvBinConv | [1, 0, 2, 0, 8, 0, 32, 0, 128, 0] |
| TransSqrs  | [0, 1, 4, 14, 20, 55, 56, 140, 120, 285] |
| TransNat0  | [0, 1, 2, 6, 6, 15, 12, 28, 20, 45] |
| TransNat1  | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| PosHalf    | [1, 3, 5, 15, 21, 63, 85, 255, 341, 1023] |
| NegHalf    | [1, -1, 5, -5, 21, -21, 85, -85, 341, -341] |

CTree Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow4 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow5 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow6 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow7 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow8 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow9 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|

CTree Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol4 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol5 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol6 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol7 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol8 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol9 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |

CTree Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow2 | [1, 2, 5, 10, 17, 26, 37, 50, 65, 82] |
| PolyRow3 | [1, 4, 15, 40, 85, 156, 259, 400, 585, 820] |
| PolyRow4 | [1, 3, 21, 91, 273, 651, 1333, 2451, 4161, 6643] |
| PolyRow5 | [1, 6, 63, 364, 1365, 3906, 9331, 19608, 37449, 66430] |
| PolyRow6 | [1, 4, 85, 820, 4369, 16276, 47989, 120100, 266305, 538084] |
| PolyRow7 | [1, 8, 255, 3280, 21845, 97656, 335923, 960800, 2396745, 5380840] |
| PolyRow8 | [1, 5, 341, 7381, 69905, 406901, 1727605, 5884901, 17043521, 43584805] |
| PolyRow9 | [1, 10, 1023, 29524, 349525, 2441406, 12093235, 47079208, 153391689, 435848050] |

CTree Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| PolyCol2 | [1, 3, 5, 15, 21, 63, 85, 255, 341, 1023] |
| PolyCol3 | [1, 4, 10, 40, 91, 364, 820, 3280, 7381, 29524] |
| PolyCol4 | [1, 5, 17, 85, 273, 1365, 4369, 21845, 69905, 349525] |
| PolyCol5 | [1, 6, 26, 156, 651, 3906, 16276, 97656, 406901, 2441406] |
| PolyCol6 | [1, 7, 37, 259, 1333, 9331, 47989, 335923, 1727605, 12093235] |
| PolyCol7 | [1, 8, 50, 400, 2451, 19608, 120100, 960800, 5884901, 47079208] |
| PolyCol8 | [1, 9, 65, 585, 4161, 37449, 266305, 2396745, 17043521, 153391689] |
| PolyCol9 | [1, 10, 82, 820, 6643, 66430, 538084, 5380840, 43584805, 435848050] |

# CTree:Inv
[]

CTree:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [-1, 1] |
| Row2 | [-1, 0, 1] |
| Row3 | [1, -1, -1, 1] |
| Row4 | [0, 0, -1, 0, 1] |
| Row5 | [0, 0, 1, -1, -1, 1] |
| Row6 | [0, 0, 0, 0, -1, 0, 1] |
| Row7 | [0, 0, 0, 0, 1, -1, -1, 1] |
| Row8 | [0, 0, 0, 0, 0, 0, -1, 0, 1] |
| Row9 | [0, 0, 0, 0, 0, 0, 1, -1, -1, 1] |

CTree:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [-1, 1], [-1, 0, 1], [1, -1, -1, 1], [0, 0, -1, 0, 1], [0, 0, 1, -1, -1, 1], [0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 1, -1, -1, 1], [0, 0, 0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 0, 1, -1, -1, 1]] |
| RevTabl    | [[1], [1, -1], [1, 0, -1], [1, -1, -1, 1], [1, 0, -1, 0, 0], [1, -1, -1, 1, 0, 0], [1, 0, -1, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]] |
| AntiDiag   | [[1], [-1], [-1, 1], [1, 0], [0, -1, 1], [0, 0, -1], [0, 0, -1, 1], [0, 0, 1, 0], [0, 0, 0, -1, 1], [0, 0, 0, 0, -1]] |
| AccTabl    | [[1], [-1, 0], [-1, -1, 0], [1, 0, -1, 0], [0, 0, -1, -1, 0], [0, 0, 1, 0, -1, 0], [0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, -1, 0]] |
| RevAccTabl | [[1], [0, -1], [0, -1, -1], [0, -1, 0, 1], [0, -1, -1, 0, 0], [0, -1, 0, 1, 0, 0], [0, -1, -1, 0, 0, 0, 0], [0, -1, 0, 1, 0, 0, 0, 0], [0, -1, -1, 0, 0, 0, 0, 0, 0], [0, -1, 0, 1, 0, 0, 0, 0, 0, 0]] |
| AccRevTabl | [[1], [1, 0], [1, 1, 0], [1, 0, -1, 0], [1, 1, 0, 0, 0], [1, 0, -1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]] |
| DiffxTabl  | [[1], [-1, 2], [-1, 0, 3], [1, -2, -3, 4], [0, 0, -3, 0, 5], [0, 0, 3, -4, -5, 6], [0, 0, 0, 0, -5, 0, 7], [0, 0, 0, 0, 5, -6, -7, 8], [0, 0, 0, 0, 0, 0, -7, 0, 9], [0, 0, 0, 0, 0, 0, 7, -8, -9, 10]] |

CTree:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, -1, 0, 0, 0, 0, 0, 0, 0, 0] |
| OddSum       | [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| AltSum       | [1, -2, 0, 0, 0, 0, 0, 0, 0, 0] |
| AbsSum       | [1, 2, 2, 4, 2, 4, 2, 4, 2, 4] |
| AccSum       | [1, -1, -2, 0, -2, 0, -2, 0, -2, 0] |
| AccRevSum    | [1, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| DiagSum      | [1, -1, 0, 1, 0, -1, 0, 1, 0, -1] |

CTree:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| CentralE   | [1, 0, -1, 0, 0] |
| CentralO   | [-1, -1, 1, 0, 0] |
| ColMiddle  | [1, -1, 0, -1, -1, 1, 0, 0, 0, 0] |
| ColLeft    | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 0, 0, -4, -5, -4, -14, 8, -27, 40] |
| InvBinConv | [1, 2, 0, 0, -5, -14, -14, -48, -27, -110] |
| TransSqrs  | [0, 1, 4, 4, 12, 4, 20, 4, 28, 4] |
| TransNat0  | [0, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| TransNat1  | [1, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| PosHalf    | [1, -1, -3, 3, -3, 3, -3, 3, -3, 3] |
| NegHalf    | [1, 3, -3, -9, -3, -9, -3, -9, -3, -9] |

CTree:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0]|
| DiagRow2 | [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]|
| DiagRow3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow4 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow5 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow6 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow7 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow8 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow9 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|

CTree:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol2 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol3 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol4 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol5 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol6 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol7 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol8 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol9 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |

CTree:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow2 | [-1, 0, 3, 8, 15, 24, 35, 48, 63, 80] |
| PolyRow3 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |
| PolyRow4 | [0, 0, 12, 72, 240, 600, 1260, 2352, 4032, 6480] |
| PolyRow5 | [0, 0, 12, 144, 720, 2400, 6300, 14112, 28224, 51840] |
| PolyRow6 | [0, 0, 48, 648, 3840, 15000, 45360, 115248, 258048, 524880] |
| PolyRow7 | [0, 0, 48, 1296, 11520, 60000, 226800, 691488, 1806336, 4199040] |
| PolyRow8 | [0, 0, 192, 5832, 61440, 375000, 1632960, 5647152, 16515072, 42515280] |
| PolyRow9 | [0, 0, 192, 11664, 184320, 1500000, 8164800, 33882912, 115605504, 340122240] |

CTree:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 1, 3, 3, 12, 12, 48, 48, 192, 192] |
| PolyCol3 | [1, 2, 8, 16, 72, 144, 648, 1296, 5832, 11664] |
| PolyCol4 | [1, 3, 15, 45, 240, 720, 3840, 11520, 61440, 184320] |
| PolyCol5 | [1, 4, 24, 96, 600, 2400, 15000, 60000, 375000, 1500000] |
| PolyCol6 | [1, 5, 35, 175, 1260, 6300, 45360, 226800, 1632960, 8164800] |
| PolyCol7 | [1, 6, 48, 288, 2352, 14112, 115248, 691488, 5647152, 33882912] |
| PolyCol8 | [1, 7, 63, 441, 4032, 28224, 258048, 1806336, 16515072, 115605504] |
| PolyCol9 | [1, 8, 80, 640, 6480, 51840, 524880, 4199040, 42515280, 340122240] |

# CTree:Rev
[]

CTree:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 1] |
| Row2 | [1, 0, 1] |
| Row3 | [1, 1, 1, 1] |
| Row4 | [1, 0, 1, 0, 1] |
| Row5 | [1, 1, 1, 1, 1, 1] |
| Row6 | [1, 0, 1, 0, 1, 0, 1] |
| Row7 | [1, 1, 1, 1, 1, 1, 1, 1] |
| Row8 | [1, 0, 1, 0, 1, 0, 1, 0, 1] |
| Row9 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |

CTree:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] |
| RevTabl    | [[1], [1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] |
| AntiDiag   | [[1], [1], [1, 1], [1, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]] |
| AccTabl    | [[1], [1, 2], [1, 1, 2], [1, 2, 3, 4], [1, 1, 2, 2, 3], [1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |
| RevAccTabl | [[1], [2, 1], [2, 1, 1], [4, 3, 2, 1], [3, 2, 2, 1, 1], [6, 5, 4, 3, 2, 1], [4, 3, 3, 2, 2, 1, 1], [8, 7, 6, 5, 4, 3, 2, 1], [5, 4, 4, 3, 3, 2, 2, 1, 1], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]] |
| AccRevTabl | [[1], [1, 2], [1, 1, 2], [1, 2, 3, 4], [1, 1, 2, 2, 3], [1, 2, 3, 4, 5, 6], [1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 2, 2, 3, 3, 4, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |
| DiffxTabl  | [[1], [1, 2], [1, 0, 3], [1, 2, 3, 4], [1, 0, 3, 0, 5], [1, 2, 3, 4, 5, 6], [1, 0, 3, 0, 5, 0, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1, 0, 3, 0, 5, 0, 7, 0, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] |

CTree:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| EvenSum      | [1, 1, 2, 2, 3, 3, 4, 4, 5, 5] |
| OddSum       | [0, 1, 0, 2, 0, 3, 0, 4, 0, 5] |
| AltSum       | [1, 0, 2, 0, 3, 0, 4, 0, 5, 0] |
| AbsSum       | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| AccSum       | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| AccRevSum    | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| DiagSum      | [1, 1, 2, 1, 3, 2, 4, 2, 5, 3] |

CTree:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| CentralE   | [1, 0, 1, 0, 1] |
| CentralO   | [1, 1, 1, 1, 1] |
| ColMiddle  | [1, 1, 0, 1, 1, 1, 0, 1, 1, 1] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 2, 2, 8, 8, 32, 32, 128, 128, 512] |
| InvBinConv | [1, 0, 2, 0, 8, 0, 32, 0, 128, 0] |
| TransSqrs  | [0, 1, 4, 14, 20, 55, 56, 140, 120, 285] |
| TransNat0  | [0, 1, 2, 6, 6, 15, 12, 28, 20, 45] |
| TransNat1  | [1, 3, 4, 10, 9, 21, 16, 36, 25, 55] |
| PosHalf    | [1, 3, 5, 15, 21, 63, 85, 255, 341, 1023] |
| NegHalf    | [1, -1, 5, -5, 21, -21, 85, -85, 341, -341] |

CTree:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow4 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow5 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow6 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow7 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow8 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow9 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|

CTree:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol2 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol4 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol5 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol6 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol7 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol8 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol9 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |

CTree:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow2 | [1, 2, 5, 10, 17, 26, 37, 50, 65, 82] |
| PolyRow3 | [1, 4, 15, 40, 85, 156, 259, 400, 585, 820] |
| PolyRow4 | [1, 3, 21, 91, 273, 651, 1333, 2451, 4161, 6643] |
| PolyRow5 | [1, 6, 63, 364, 1365, 3906, 9331, 19608, 37449, 66430] |
| PolyRow6 | [1, 4, 85, 820, 4369, 16276, 47989, 120100, 266305, 538084] |
| PolyRow7 | [1, 8, 255, 3280, 21845, 97656, 335923, 960800, 2396745, 5380840] |
| PolyRow8 | [1, 5, 341, 7381, 69905, 406901, 1727605, 5884901, 17043521, 43584805] |
| PolyRow9 | [1, 10, 1023, 29524, 349525, 2441406, 12093235, 47079208, 153391689, 435848050] |

CTree:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 2, 2, 4, 3, 6, 4, 8, 5, 10] |
| PolyCol2 | [1, 3, 5, 15, 21, 63, 85, 255, 341, 1023] |
| PolyCol3 | [1, 4, 10, 40, 91, 364, 820, 3280, 7381, 29524] |
| PolyCol4 | [1, 5, 17, 85, 273, 1365, 4369, 21845, 69905, 349525] |
| PolyCol5 | [1, 6, 26, 156, 651, 3906, 16276, 97656, 406901, 2441406] |
| PolyCol6 | [1, 7, 37, 259, 1333, 9331, 47989, 335923, 1727605, 12093235] |
| PolyCol7 | [1, 8, 50, 400, 2451, 19608, 120100, 960800, 5884901, 47079208] |
| PolyCol8 | [1, 9, 65, 585, 4161, 37449, 266305, 2396745, 17043521, 153391689] |
| PolyCol9 | [1, 10, 82, 820, 6643, 66430, 538084, 5380840, 43584805, 435848050] |

# CTree:Inv:Rev
[]

CTree:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, -1] |
| Row2 | [1, 0, -1] |
| Row3 | [1, -1, -1, 1] |
| Row4 | [1, 0, -1, 0, 0] |
| Row5 | [1, -1, -1, 1, 0, 0] |
| Row6 | [1, 0, -1, 0, 0, 0, 0] |
| Row7 | [1, -1, -1, 1, 0, 0, 0, 0] |
| Row8 | [1, 0, -1, 0, 0, 0, 0, 0, 0] |
| Row9 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |

CTree:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, -1], [1, 0, -1], [1, -1, -1, 1], [1, 0, -1, 0, 0], [1, -1, -1, 1, 0, 0], [1, 0, -1, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]] |
| RevTabl    | [[1], [-1, 1], [-1, 0, 1], [1, -1, -1, 1], [0, 0, -1, 0, 1], [0, 0, 1, -1, -1, 1], [0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 1, -1, -1, 1], [0, 0, 0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 0, 1, -1, -1, 1]] |
| AntiDiag   | [[1], [1], [1, -1], [1, 0], [1, -1, -1], [1, 0, -1], [1, -1, -1, 1], [1, 0, -1, 0], [1, -1, -1, 1, 0], [1, 0, -1, 0, 0]] |
| AccTabl    | [[1], [1, 0], [1, 1, 0], [1, 0, -1, 0], [1, 1, 0, 0, 0], [1, 0, -1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]] |
| RevAccTabl | [[1], [0, 1], [0, 1, 1], [0, -1, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, -1, 0, 1]] |
| AccRevTabl | [[1], [-1, 0], [-1, -1, 0], [1, 0, -1, 0], [0, 0, -1, -1, 0], [0, 0, 1, 0, -1, 0], [0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, -1, 0]] |
| DiffxTabl  | [[1], [1, -2], [1, 0, -3], [1, -2, -3, 4], [1, 0, -3, 0, 0], [1, -2, -3, 4, 0, 0], [1, 0, -3, 0, 0, 0, 0], [1, -2, -3, 4, 0, 0, 0, 0], [1, 0, -3, 0, 0, 0, 0, 0, 0], [1, -2, -3, 4, 0, 0, 0, 0, 0, 0]] |

CTree:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| OddSum       | [0, -1, 0, 0, 0, 0, 0, 0, 0, 0] |
| AltSum       | [1, 2, 0, 0, 0, 0, 0, 0, 0, 0] |
| AbsSum       | [1, 2, 2, 4, 2, 4, 2, 4, 2, 4] |
| AccSum       | [1, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| AccRevSum    | [1, -1, -2, 0, -2, 0, -2, 0, -2, 0] |
| DiagSum      | [1, 1, 0, 1, -1, 0, 0, 0, 0, 0] |

CTree:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| CentralE   | [1, 0, -1, 0, 0] |
| CentralO   | [1, -1, -1, 1, 0] |
| ColMiddle  | [1, 1, 0, -1, -1, -1, 0, 1, 0, 0] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 0, 0, -4, -5, -4, -14, 8, -27, 40] |
| InvBinConv | [1, -2, 0, 0, -5, 14, -14, 48, -27, 110] |
| TransSqrs  | [0, -1, -4, 4, -4, 4, -4, 4, -4, 4] |
| TransNat0  | [0, -1, -2, 0, -2, 0, -2, 0, -2, 0] |
| TransNat1  | [1, -1, -2, 0, -2, 0, -2, 0, -2, 0] |
| PosHalf    | [1, 1, 3, 3, 12, 12, 48, 48, 192, 192] |
| NegHalf    | [1, -3, 3, -9, 12, -36, 48, -144, 192, -576] |

CTree:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow2 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow3 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow4 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow5 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow6 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow7 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow8 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]|
| DiagRow9 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]|

CTree:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0] |
| DiagCol2 | [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] |
| DiagCol3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol4 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol5 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol6 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol7 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol8 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol9 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |

CTree:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 0, -1, -2, -3, -4, -5, -6, -7, -8] |
| PolyRow2 | [1, 0, -3, -8, -15, -24, -35, -48, -63, -80] |
| PolyRow3 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |
| PolyRow4 | [1, 0, -3, -8, -15, -24, -35, -48, -63, -80] |
| PolyRow5 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |
| PolyRow6 | [1, 0, -3, -8, -15, -24, -35, -48, -63, -80] |
| PolyRow7 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |
| PolyRow8 | [1, 0, -3, -8, -15, -24, -35, -48, -63, -80] |
| PolyRow9 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |

CTree:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, -1, -3, 3, -3, 3, -3, 3, -3, 3] |
| PolyCol3 | [1, -2, -8, 16, -8, 16, -8, 16, -8, 16] |
| PolyCol4 | [1, -3, -15, 45, -15, 45, -15, 45, -15, 45] |
| PolyCol5 | [1, -4, -24, 96, -24, 96, -24, 96, -24, 96] |
| PolyCol6 | [1, -5, -35, 175, -35, 175, -35, 175, -35, 175] |
| PolyCol7 | [1, -6, -48, 288, -48, 288, -48, 288, -48, 288] |
| PolyCol8 | [1, -7, -63, 441, -63, 441, -63, 441, -63, 441] |
| PolyCol9 | [1, -8, -80, 640, -80, 640, -80, 640, -80, 640] |

# CTree:Rev:Inv
[]

CTree:Rev:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [-1, 1] |
| Row2 | [-1, 0, 1] |
| Row3 | [1, -1, -1, 1] |
| Row4 | [0, 0, -1, 0, 1] |
| Row5 | [0, 0, 1, -1, -1, 1] |
| Row6 | [0, 0, 0, 0, -1, 0, 1] |
| Row7 | [0, 0, 0, 0, 1, -1, -1, 1] |
| Row8 | [0, 0, 0, 0, 0, 0, -1, 0, 1] |
| Row9 | [0, 0, 0, 0, 0, 0, 1, -1, -1, 1] |

CTree:Rev:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [-1, 1], [-1, 0, 1], [1, -1, -1, 1], [0, 0, -1, 0, 1], [0, 0, 1, -1, -1, 1], [0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 1, -1, -1, 1], [0, 0, 0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 0, 1, -1, -1, 1]] |
| RevTabl    | [[1], [1, -1], [1, 0, -1], [1, -1, -1, 1], [1, 0, -1, 0, 0], [1, -1, -1, 1, 0, 0], [1, 0, -1, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0], [1, -1, -1, 1, 0, 0, 0, 0, 0, 0]] |
| AntiDiag   | [[1], [-1], [-1, 1], [1, 0], [0, -1, 1], [0, 0, -1], [0, 0, -1, 1], [0, 0, 1, 0], [0, 0, 0, -1, 1], [0, 0, 0, 0, -1]] |
| AccTabl    | [[1], [-1, 0], [-1, -1, 0], [1, 0, -1, 0], [0, 0, -1, -1, 0], [0, 0, 1, 0, -1, 0], [0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 1, 0, -1, 0], [0, 0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 0, 0, 1, 0, -1, 0]] |
| RevAccTabl | [[1], [0, -1], [0, -1, -1], [0, -1, 0, 1], [0, -1, -1, 0, 0], [0, -1, 0, 1, 0, 0], [0, -1, -1, 0, 0, 0, 0], [0, -1, 0, 1, 0, 0, 0, 0], [0, -1, -1, 0, 0, 0, 0, 0, 0], [0, -1, 0, 1, 0, 0, 0, 0, 0, 0]] |
| AccRevTabl | [[1], [1, 0], [1, 1, 0], [1, 0, -1, 0], [1, 1, 0, 0, 0], [1, 0, -1, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0, 0, 0, 0]] |
| DiffxTabl  | [[1], [-1, 2], [-1, 0, 3], [1, -2, -3, 4], [0, 0, -3, 0, 5], [0, 0, 3, -4, -5, 6], [0, 0, 0, 0, -5, 0, 7], [0, 0, 0, 0, 5, -6, -7, 8], [0, 0, 0, 0, 0, 0, -7, 0, 9], [0, 0, 0, 0, 0, 0, 7, -8, -9, 10]] |

CTree:Rev:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, -1, 0, 0, 0, 0, 0, 0, 0, 0] |
| OddSum       | [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| AltSum       | [1, -2, 0, 0, 0, 0, 0, 0, 0, 0] |
| AbsSum       | [1, 2, 2, 4, 2, 4, 2, 4, 2, 4] |
| AccSum       | [1, -1, -2, 0, -2, 0, -2, 0, -2, 0] |
| AccRevSum    | [1, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| DiagSum      | [1, -1, 0, 1, 0, -1, 0, 1, 0, -1] |

CTree:Rev:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| CentralE   | [1, 0, -1, 0, 0] |
| CentralO   | [-1, -1, 1, 0, 0] |
| ColMiddle  | [1, -1, 0, -1, -1, 1, 0, 0, 0, 0] |
| ColLeft    | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 0, 0, -4, -5, -4, -14, 8, -27, 40] |
| InvBinConv | [1, 2, 0, 0, -5, -14, -14, -48, -27, -110] |
| TransSqrs  | [0, 1, 4, 4, 12, 4, 20, 4, 28, 4] |
| TransNat0  | [0, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| TransNat1  | [1, 1, 2, 0, 2, 0, 2, 0, 2, 0] |
| PosHalf    | [1, -1, -3, 3, -3, 3, -3, 3, -3, 3] |
| NegHalf    | [1, 3, -3, -9, -3, -9, -3, -9, -3, -9] |

CTree:Rev:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0]|
| DiagRow2 | [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]|
| DiagRow3 | [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow4 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow5 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow6 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow7 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow8 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow9 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|

CTree:Rev:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol2 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol3 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol4 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol5 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol6 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol7 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol8 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| DiagCol9 | [1, 0, -1, 0, 0, 0, 0, 0, 0, 0] |

CTree:Rev:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow2 | [-1, 0, 3, 8, 15, 24, 35, 48, 63, 80] |
| PolyRow3 | [1, 0, 3, 16, 45, 96, 175, 288, 441, 640] |
| PolyRow4 | [0, 0, 12, 72, 240, 600, 1260, 2352, 4032, 6480] |
| PolyRow5 | [0, 0, 12, 144, 720, 2400, 6300, 14112, 28224, 51840] |
| PolyRow6 | [0, 0, 48, 648, 3840, 15000, 45360, 115248, 258048, 524880] |
| PolyRow7 | [0, 0, 48, 1296, 11520, 60000, 226800, 691488, 1806336, 4199040] |
| PolyRow8 | [0, 0, 192, 5832, 61440, 375000, 1632960, 5647152, 16515072, 42515280] |
| PolyRow9 | [0, 0, 192, 11664, 184320, 1500000, 8164800, 33882912, 115605504, 340122240] |

CTree:Rev:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, -1, -1, 1, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 1, 3, 3, 12, 12, 48, 48, 192, 192] |
| PolyCol3 | [1, 2, 8, 16, 72, 144, 648, 1296, 5832, 11664] |
| PolyCol4 | [1, 3, 15, 45, 240, 720, 3840, 11520, 61440, 184320] |
| PolyCol5 | [1, 4, 24, 96, 600, 2400, 15000, 60000, 375000, 1500000] |
| PolyCol6 | [1, 5, 35, 175, 1260, 6300, 45360, 226800, 1632960, 8164800] |
| PolyCol7 | [1, 6, 48, 288, 2352, 14112, 115248, 691488, 5647152, 33882912] |
| PolyCol8 | [1, 7, 63, 441, 4032, 28224, 258048, 1806336, 16515072, 115605504] |
| PolyCol9 | [1, 8, 80, 640, 6480, 51840, 524880, 4199040, 42515280, 340122240] |

