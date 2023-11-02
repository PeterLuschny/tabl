# Ordinals
['A002262', 'A002260', 'A004736', 'A025581']

Ordinals Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 2] |
| Row3 | [0, 1, 2, 3] |
| Row4 | [0, 1, 2, 3, 4] |
| Row5 | [0, 1, 2, 3, 4, 5] |
| Row6 | [0, 1, 2, 3, 4, 5, 6] |
| Row7 | [0, 1, 2, 3, 4, 5, 6, 7] |
| Row8 | [0, 1, 2, 3, 4, 5, 6, 7, 8] |
| Row9 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |

Ordinals Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] |
| RevTabl    | [[0], [1, 0], [2, 1, 0], [3, 2, 1, 0], [4, 3, 2, 1, 0], [5, 4, 3, 2, 1, 0], [6, 5, 4, 3, 2, 1, 0], [7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]] |
| AntiDiag   | [[0], [0], [0, 1], [0, 1], [0, 1, 2], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]] |
| AccTabl    | [[0], [0, 1], [0, 1, 3], [0, 1, 3, 6], [0, 1, 3, 6, 10], [0, 1, 3, 6, 10, 15], [0, 1, 3, 6, 10, 15, 21], [0, 1, 3, 6, 10, 15, 21, 28], [0, 1, 3, 6, 10, 15, 21, 28, 36], [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]] |
| RevAccTabl | [[0], [1, 0], [3, 1, 0], [6, 3, 1, 0], [10, 6, 3, 1, 0], [15, 10, 6, 3, 1, 0], [21, 15, 10, 6, 3, 1, 0], [28, 21, 15, 10, 6, 3, 1, 0], [36, 28, 21, 15, 10, 6, 3, 1, 0], [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]] |
| AccRevTabl | [[0], [1, 1], [2, 3, 3], [3, 5, 6, 6], [4, 7, 9, 10, 10], [5, 9, 12, 14, 15, 15], [6, 11, 15, 18, 20, 21, 21], [7, 13, 18, 22, 25, 27, 28, 28], [8, 15, 21, 26, 30, 33, 35, 36, 36], [9, 17, 24, 30, 35, 39, 42, 44, 45, 45]] |

Ordinals Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] |
| EvenSum      | [0, 0, 2, 2, 6, 6, 12, 12, 20, 20] |
| OddSum       | [0, 1, 1, 4, 4, 9, 9, 16, 16, 25] |
| AltSum       | [0, -1, 1, -2, 2, -3, 3, -4, 4, -5] |
| AccSum       | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165] |
| AccRevSum    | [0, 2, 8, 20, 40, 70, 112, 168, 240, 330] |
| DiagSum      | [0, 0, 1, 1, 3, 3, 6, 6, 10, 10] |

Ordinals Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 12, 60, 60, 420, 840, 2520] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| CentralE   | [0, 1, 2, 3, 4] |
| CentralO   | [0, 1, 2, 3, 4] |
| ColMiddle  | [0, 0, 1, 1, 2, 2, 3, 3, 4, 4] |
| ColLeft    | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| TransSqrs  | [0, 1, 9, 36, 100, 225, 441, 784, 1296, 2025] |
| TransNat0  | [0, 1, 5, 14, 30, 55, 91, 140, 204, 285] |
| TransNat1  | [0, 2, 8, 20, 40, 70, 112, 168, 240, 330] |

Ordinals Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow2 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow3 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow4 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow5 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow6 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow7 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow8 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|
| DiagRow9 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]|

Ordinals Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] |
| DiagCol3 | [3, 3, 3, 3, 3, 3, 3, 3, 3, 3] |
| DiagCol4 | [4, 4, 4, 4, 4, 4, 4, 4, 4, 4] |
| DiagCol5 | [5, 5, 5, 5, 5, 5, 5, 5, 5, 5] |
| DiagCol6 | [6, 6, 6, 6, 6, 6, 6, 6, 6, 6] |
| DiagCol7 | [7, 7, 7, 7, 7, 7, 7, 7, 7, 7] |
| DiagCol8 | [8, 8, 8, 8, 8, 8, 8, 8, 8, 8] |
| DiagCol9 | [9, 9, 9, 9, 9, 9, 9, 9, 9, 9] |

Ordinals Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136, 171] |
| PolyRow3 | [0, 6, 34, 102, 228, 430, 726, 1134, 1672, 2358] |
| PolyRow4 | [0, 10, 98, 426, 1252, 2930, 5910, 10738, 18056, 28602] |
| PolyRow5 | [0, 15, 258, 1641, 6372, 18555, 44790, 94773, 181896, 323847] |
| PolyRow6 | [0, 21, 642, 6015, 30948, 112305, 324726, 800667, 1754760, 3512493] |
| PolyRow7 | [0, 28, 1538, 21324, 145636, 659180, 2284278, 6565468, 16434824, 36993276] |
| PolyRow8 | [0, 36, 3586, 73812, 669924, 3784180, 15721206, 52683876, 150652552, 381367044] |
| PolyRow9 | [0, 45, 8194, 250959, 3029220, 21362305, 106420470, 415866339, 1358612104, 3868151445] |

Ordinals Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] |
| PolyCol2 | [0, 2, 10, 34, 98, 258, 642, 1538, 3586, 8194] |
| PolyCol3 | [0, 3, 21, 102, 426, 1641, 6015, 21324, 73812, 250959] |
| PolyCol4 | [0, 4, 36, 228, 1252, 6372, 30948, 145636, 669924, 3029220] |
| PolyCol5 | [0, 5, 55, 430, 2930, 18555, 112305, 659180, 3784180, 21362305] |
| PolyCol6 | [0, 6, 78, 726, 5910, 44790, 324726, 2284278, 15721206, 106420470] |
| PolyCol7 | [0, 7, 105, 1134, 10738, 94773, 800667, 6565468, 52683876, 415866339] |
| PolyCol8 | [0, 8, 136, 1672, 18056, 181896, 1754760, 16434824, 150652552, 1358612104] |
| PolyCol9 | [0, 9, 171, 2358, 28602, 323847, 3512493, 36993276, 381367044, 3868151445] |

# Ordinals:Rev
[]

Ordinals:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [1, 0] |
| Row2 | [2, 1, 0] |
| Row3 | [3, 2, 1, 0] |
| Row4 | [4, 3, 2, 1, 0] |
| Row5 | [5, 4, 3, 2, 1, 0] |
| Row6 | [6, 5, 4, 3, 2, 1, 0] |
| Row7 | [7, 6, 5, 4, 3, 2, 1, 0] |
| Row8 | [8, 7, 6, 5, 4, 3, 2, 1, 0] |
| Row9 | [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] |

Ordinals:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[0], [1, 0], [2, 1, 0], [3, 2, 1, 0], [4, 3, 2, 1, 0], [5, 4, 3, 2, 1, 0], [6, 5, 4, 3, 2, 1, 0], [7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]] |
| RevTabl    | [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] |
| AntiDiag   | [[0], [1], [2, 0], [3, 1], [4, 2, 0], [5, 3, 1], [6, 4, 2, 0], [7, 5, 3, 1], [8, 6, 4, 2, 0], [9, 7, 5, 3, 1]] |
| AccTabl    | [[0], [1, 1], [2, 3, 3], [3, 5, 6, 6], [4, 7, 9, 10, 10], [5, 9, 12, 14, 15, 15], [6, 11, 15, 18, 20, 21, 21], [7, 13, 18, 22, 25, 27, 28, 28], [8, 15, 21, 26, 30, 33, 35, 36, 36], [9, 17, 24, 30, 35, 39, 42, 44, 45, 45]] |
| RevAccTabl | [[0], [1, 1], [3, 3, 2], [6, 6, 5, 3], [10, 10, 9, 7, 4], [15, 15, 14, 12, 9, 5], [21, 21, 20, 18, 15, 11, 6], [28, 28, 27, 25, 22, 18, 13, 7], [36, 36, 35, 33, 30, 26, 21, 15, 8], [45, 45, 44, 42, 39, 35, 30, 24, 17, 9]] |
| AccRevTabl | [[0], [0, 1], [0, 1, 3], [0, 1, 3, 6], [0, 1, 3, 6, 10], [0, 1, 3, 6, 10, 15], [0, 1, 3, 6, 10, 15, 21], [0, 1, 3, 6, 10, 15, 21, 28], [0, 1, 3, 6, 10, 15, 21, 28, 36], [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]] |

Ordinals:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] |
| EvenSum      | [0, 1, 2, 4, 6, 9, 12, 16, 20, 25] |
| OddSum       | [0, 0, 1, 2, 4, 6, 9, 12, 16, 20] |
| AltSum       | [0, 1, 1, 2, 2, 3, 3, 4, 4, 5] |
| AccSum       | [0, 2, 8, 20, 40, 70, 112, 168, 240, 330] |
| AccRevSum    | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165] |
| DiagSum      | [0, 1, 2, 4, 6, 9, 12, 16, 20, 25] |

Ordinals:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 12, 60, 60, 420, 840, 2520] |
| RowGcd     | [1, 1, 2, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| CentralE   | [0, 1, 2, 3, 4] |
| CentralO   | [1, 2, 3, 4, 5] |
| ColMiddle  | [0, 1, 1, 2, 2, 3, 3, 4, 4, 5] |
| ColLeft    | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| ColRight   | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 6, 20, 50, 105, 196, 336, 540] |
| TransNat0  | [0, 0, 1, 4, 10, 20, 35, 56, 84, 120] |
| TransNat1  | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165] |

Ordinals:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]|
| DiagRow3 | [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]|
| DiagRow4 | [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]|
| DiagRow5 | [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]|
| DiagRow6 | [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]|
| DiagRow7 | [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]|
| DiagRow8 | [8, 8, 8, 8, 8, 8, 8, 8, 8, 8]|
| DiagRow9 | [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]|

Ordinals:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol2 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol3 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol4 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol5 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol6 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol7 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol8 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| DiagCol9 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |

Ordinals:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] |
| PolyRow3 | [3, 6, 11, 18, 27, 38, 51, 66, 83, 102] |
| PolyRow4 | [4, 10, 26, 58, 112, 194, 310, 466, 668, 922] |
| PolyRow5 | [5, 15, 57, 179, 453, 975, 1865, 3267, 5349, 8303] |
| PolyRow6 | [6, 21, 120, 543, 1818, 4881, 11196, 22875, 42798, 74733] |
| PolyRow7 | [7, 28, 247, 1636, 7279, 24412, 67183, 160132, 342391, 672604] |
| PolyRow8 | [8, 36, 502, 4916, 29124, 122068, 403106, 1120932, 2739136, 6053444] |
| PolyRow9 | [9, 45, 1013, 14757, 116505, 610349, 2418645, 7846533, 21913097, 54481005] |

Ordinals:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyCol1 | [0, 1, 3, 6, 10, 15, 21, 28, 36, 45] |
| PolyCol2 | [0, 1, 4, 11, 26, 57, 120, 247, 502, 1013] |
| PolyCol3 | [0, 1, 5, 18, 58, 179, 543, 1636, 4916, 14757] |
| PolyCol4 | [0, 1, 6, 27, 112, 453, 1818, 7279, 29124, 116505] |
| PolyCol5 | [0, 1, 7, 38, 194, 975, 4881, 24412, 122068, 610349] |
| PolyCol6 | [0, 1, 8, 51, 310, 1865, 11196, 67183, 403106, 2418645] |
| PolyCol7 | [0, 1, 9, 66, 466, 3267, 22875, 160132, 1120932, 7846533] |
| PolyCol8 | [0, 1, 10, 83, 668, 5349, 42798, 342391, 2739136, 21913097] |
| PolyCol9 | [0, 1, 11, 102, 922, 8303, 74733, 672604, 6053444, 54481005] |
