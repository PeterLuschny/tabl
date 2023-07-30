# Euclid
['A217831']

Euclid Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [1, 1] |
| Row2 | [0, 1, 0] |
| Row3 | [0, 1, 1, 0] |
| Row4 | [0, 1, 0, 1, 0] |
| Row5 | [0, 1, 1, 1, 1, 0] |
| Row6 | [0, 1, 0, 0, 0, 1, 0] |
| Row7 | [0, 1, 1, 1, 1, 1, 1, 0] |
| Row8 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |

Euclid Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[0], [1, 1], [0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0]] |
| RevTabl    | [[0], [1, 1], [0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0]] |
| AntiDiag   | [[0], [1], [0, 1], [0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 1, 0]] |
| AccTabl    | [[0], [1, 2], [0, 1, 1], [0, 1, 2, 2], [0, 1, 1, 2, 2], [0, 1, 2, 3, 4, 4], [0, 1, 1, 1, 1, 2, 2], [0, 1, 2, 3, 4, 5, 6, 6], [0, 1, 1, 2, 2, 3, 3, 4, 4]] |
| RevAccTabl | [[0], [2, 1], [1, 1, 0], [2, 2, 1, 0], [2, 2, 1, 1, 0], [4, 4, 3, 2, 1, 0], [2, 2, 1, 1, 1, 1, 0], [6, 6, 5, 4, 3, 2, 1, 0], [4, 4, 3, 3, 2, 2, 1, 1, 0]] |
| AccRevTabl | [[0], [1, 2], [0, 1, 1], [0, 1, 2, 2], [0, 1, 1, 2, 2], [0, 1, 2, 3, 4, 4], [0, 1, 1, 1, 1, 2, 2], [0, 1, 2, 3, 4, 5, 6, 6], [0, 1, 1, 2, 2, 3, 3, 4, 4]] |

Euclid Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 2, 1, 2, 2, 4, 2, 6, 4] |
| EvenSum      | [0, 1, 0, 1, 0, 2, 0, 3, 0] |
| OddSum       | [0, 1, 1, 1, 2, 2, 2, 3, 4] |
| AltSum       | [0, 0, -1, 0, -2, 0, -2, 0, -4] |
| AccSum       | [0, 3, 2, 5, 6, 14, 8, 27, 20] |
| AccRevSum    | [0, 3, 2, 5, 6, 14, 8, 27, 20] |
| AntiDiagSum  | [0, 1, 1, 1, 1, 2, 1, 3, 2] |

Euclid Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColMiddle  | [0, 1, 1, 1, 0, 1, 0, 1, 0] |
| ColECenter | [0, 1, 0, 0, 0] |
| ColOCenter | [1, 1, 1, 1] |
| ColLeft    | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 1, 1, 5, 10, 30, 26, 91, 84] |
| TransNat0  | [0, 1, 1, 3, 4, 10, 6, 21, 16] |
| TransNat1  | [0, 3, 2, 5, 6, 14, 8, 27, 20] |

Euclid Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow3 | [0, 1, 1, 0, 1, 1, 0, 1, 1]|
| DiagRow4 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow5 | [0, 1, 1, 1, 1, 0, 1, 1, 1]|
| DiagRow6 | [0, 1, 0, 0, 0, 1, 0, 1, 0]|
| DiagRow7 | [0, 1, 1, 1, 1, 1, 1, 0, 1]|
| DiagRow8 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|

Euclid Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol3 | [0, 1, 1, 0, 1, 1, 0, 1, 1] |
| DiagCol4 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol5 | [0, 1, 1, 1, 1, 0, 1, 1, 1] |
| DiagCol6 | [0, 1, 0, 0, 0, 1, 0, 1, 0] |
| DiagCol7 | [0, 1, 1, 1, 1, 1, 1, 0, 1] |
| DiagCol8 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |

Euclid Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow3 | [0, 2, 6, 12, 20, 30, 42, 56, 72] |
| PolyRow4 | [0, 2, 10, 30, 68, 130, 222, 350, 520] |
| PolyRow5 | [0, 4, 30, 120, 340, 780, 1554, 2800, 4680] |
| PolyRow6 | [0, 2, 34, 246, 1028, 3130, 7782, 16814, 32776] |
| PolyRow7 | [0, 6, 126, 1092, 5460, 19530, 55986, 137256, 299592] |
| PolyRow8 | [0, 4, 170, 2460, 17476, 81380, 287934, 840700, 2130440] |

Euclid Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [0, 2, 1, 2, 2, 4, 2, 6, 4] |
| PolyCol2 | [0, 3, 2, 6, 10, 30, 34, 126, 170] |
| PolyCol3 | [0, 4, 3, 12, 30, 120, 246, 1092, 2460] |
| PolyCol4 | [0, 5, 4, 20, 68, 340, 1028, 5460, 17476] |
| PolyCol5 | [0, 6, 5, 30, 130, 780, 3130, 19530, 81380] |
| PolyCol6 | [0, 7, 6, 42, 222, 1554, 7782, 55986, 287934] |
| PolyCol7 | [0, 8, 7, 56, 350, 2800, 16814, 137256, 840700] |
| PolyCol8 | [0, 9, 8, 72, 520, 4680, 32776, 299592, 2130440] |

# Euclid:Rev
[]

Euclid:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [0] |
| Row1 | [1, 1] |
| Row2 | [0, 1, 0] |
| Row3 | [0, 1, 1, 0] |
| Row4 | [0, 1, 0, 1, 0] |
| Row5 | [0, 1, 1, 1, 1, 0] |
| Row6 | [0, 1, 0, 0, 0, 1, 0] |
| Row7 | [0, 1, 1, 1, 1, 1, 1, 0] |
| Row8 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |

Euclid:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[0], [1, 1], [0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0]] |
| RevTabl    | [[0], [1, 1], [0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0]] |
| AntiDiag   | [[0], [1], [0, 1], [0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 1, 0]] |
| AccTabl    | [[0], [1, 2], [0, 1, 1], [0, 1, 2, 2], [0, 1, 1, 2, 2], [0, 1, 2, 3, 4, 4], [0, 1, 1, 1, 1, 2, 2], [0, 1, 2, 3, 4, 5, 6, 6], [0, 1, 1, 2, 2, 3, 3, 4, 4]] |
| RevAccTabl | [[0], [2, 1], [1, 1, 0], [2, 2, 1, 0], [2, 2, 1, 1, 0], [4, 4, 3, 2, 1, 0], [2, 2, 1, 1, 1, 1, 0], [6, 6, 5, 4, 3, 2, 1, 0], [4, 4, 3, 3, 2, 2, 1, 1, 0]] |
| AccRevTabl | [[0], [1, 2], [0, 1, 1], [0, 1, 2, 2], [0, 1, 1, 2, 2], [0, 1, 2, 3, 4, 4], [0, 1, 1, 1, 1, 2, 2], [0, 1, 2, 3, 4, 5, 6, 6], [0, 1, 1, 2, 2, 3, 3, 4, 4]] |

Euclid:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [0, 2, 1, 2, 2, 4, 2, 6, 4] |
| EvenSum      | [0, 1, 0, 1, 0, 2, 0, 3, 0] |
| OddSum       | [0, 1, 1, 1, 2, 2, 2, 3, 4] |
| AltSum       | [0, 0, -1, 0, -2, 0, -2, 0, -4] |
| AccSum       | [0, 3, 2, 5, 6, 14, 8, 27, 20] |
| AccRevSum    | [0, 3, 2, 5, 6, 14, 8, 27, 20] |
| AntiDiagSum  | [0, 1, 1, 1, 1, 2, 1, 3, 2] |

Euclid:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [0, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColMiddle  | [0, 1, 1, 1, 0, 1, 0, 1, 0] |
| ColECenter | [0, 1, 0, 0, 0] |
| ColOCenter | [1, 1, 1, 1] |
| ColLeft    | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 1, 1, 5, 10, 30, 26, 91, 84] |
| TransNat0  | [0, 1, 1, 3, 4, 10, 6, 21, 16] |
| TransNat1  | [0, 3, 2, 5, 6, 14, 8, 27, 20] |

Euclid:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [0, 1, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow3 | [0, 1, 1, 0, 1, 1, 0, 1, 1]|
| DiagRow4 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|
| DiagRow5 | [0, 1, 1, 1, 1, 0, 1, 1, 1]|
| DiagRow6 | [0, 1, 0, 0, 0, 1, 0, 1, 0]|
| DiagRow7 | [0, 1, 1, 1, 1, 1, 1, 0, 1]|
| DiagRow8 | [0, 1, 0, 1, 0, 1, 0, 1, 0]|

Euclid:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol3 | [0, 1, 1, 0, 1, 1, 0, 1, 1] |
| DiagCol4 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |
| DiagCol5 | [0, 1, 1, 1, 1, 0, 1, 1, 1] |
| DiagCol6 | [0, 1, 0, 0, 0, 1, 0, 1, 0] |
| DiagCol7 | [0, 1, 1, 1, 1, 1, 1, 0, 1] |
| DiagCol8 | [0, 1, 0, 1, 0, 1, 0, 1, 0] |

Euclid:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow3 | [0, 2, 6, 12, 20, 30, 42, 56, 72] |
| PolyRow4 | [0, 2, 10, 30, 68, 130, 222, 350, 520] |
| PolyRow5 | [0, 4, 30, 120, 340, 780, 1554, 2800, 4680] |
| PolyRow6 | [0, 2, 34, 246, 1028, 3130, 7782, 16814, 32776] |
| PolyRow7 | [0, 6, 126, 1092, 5460, 19530, 55986, 137256, 299592] |
| PolyRow8 | [0, 4, 170, 2460, 17476, 81380, 287934, 840700, 2130440] |

Euclid:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [0, 1, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [0, 2, 1, 2, 2, 4, 2, 6, 4] |
| PolyCol2 | [0, 3, 2, 6, 10, 30, 34, 126, 170] |
| PolyCol3 | [0, 4, 3, 12, 30, 120, 246, 1092, 2460] |
| PolyCol4 | [0, 5, 4, 20, 68, 340, 1028, 5460, 17476] |
| PolyCol5 | [0, 6, 5, 30, 130, 780, 3130, 19530, 81380] |
| PolyCol6 | [0, 7, 6, 42, 222, 1554, 7782, 55986, 287934] |
| PolyCol7 | [0, 8, 7, 56, 350, 2800, 16814, 137256, 840700] |
| PolyCol8 | [0, 9, 8, 72, 520, 4680, 32776, 299592, 2130440] |
