# OrderedCycle
['A225479', 'A048594', 'A075181']

OrderedCycle Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 2] |
| Row3 | [0, 2, 6, 6] |
| Row4 | [0, 6, 22, 36, 24] |
| Row5 | [0, 24, 100, 210, 240, 120] |
| Row6 | [0, 120, 548, 1350, 2040, 1800, 720] |
| Row7 | [0, 720, 3528, 9744, 17640, 21000, 15120, 5040] |
| Row8 | [0, 5040, 26136, 78792, 162456, 235200, 231840, 141120, 40320] |

OrderedCycle Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[1], [0, 1], [0, 1, 2], [0, 2, 6, 6], [0, 6, 22, 36, 24], [0, 24, 100, 210, 240, 120], [0, 120, 548, 1350, 2040, 1800, 720], [0, 720, 3528, 9744, 17640, 21000, 15120, 5040], [0, 5040, 26136, 78792, 162456, 235200, 231840, 141120, 40320]] |
| RevTabl    | [[1], [1, 0], [2, 1, 0], [6, 6, 2, 0], [24, 36, 22, 6, 0], [120, 240, 210, 100, 24, 0], [720, 1800, 2040, 1350, 548, 120, 0], [5040, 15120, 21000, 17640, 9744, 3528, 720, 0], [40320, 141120, 231840, 235200, 162456, 78792, 26136, 5040, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 2, 2], [0, 6, 6], [0, 24, 22, 6], [0, 120, 100, 36], [0, 720, 548, 210, 24]] |
| AccTabl    | [[1], [0, 1], [0, 1, 3], [0, 2, 8, 14], [0, 6, 28, 64, 88], [0, 24, 124, 334, 574, 694], [0, 120, 668, 2018, 4058, 5858, 6578], [0, 720, 4248, 13992, 31632, 52632, 67752, 72792], [0, 5040, 31176, 109968, 272424, 507624, 739464, 880584, 920904]] |
| RevAccTabl | [[1], [1, 0], [3, 1, 0], [14, 8, 2, 0], [88, 64, 28, 6, 0], [694, 574, 334, 124, 24, 0], [6578, 5858, 4058, 2018, 668, 120, 0], [72792, 67752, 52632, 31632, 13992, 4248, 720, 0], [920904, 880584, 739464, 507624, 272424, 109968, 31176, 5040, 0]] |
| AccRevTabl | [[1], [1, 1], [2, 3, 3], [6, 12, 14, 14], [24, 60, 82, 88, 88], [120, 360, 570, 670, 694, 694], [720, 2520, 4560, 5910, 6458, 6578, 6578], [5040, 20160, 41160, 58800, 68544, 72072, 72792, 72792], [40320, 181440, 413280, 648480, 810936, 889728, 915864, 920904, 920904]] |

OrderedCycle Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 14, 88, 694, 6578, 72792, 920904] |
| EvenSum      | [1, 0, 2, 6, 46, 340, 3308, 36288, 460752] |
| OddSum       | [0, 1, 1, 8, 42, 354, 3270, 36504, 460152] |
| AltSum       | [1, -1, 1, -2, 4, -14, 38, -216, 600] |
| AccSum       | [1, 1, 4, 24, 186, 1750, 19300, 243768, 3467184] |
| AccRevSum    | [1, 2, 8, 46, 342, 3108, 33324, 411360, 5741856] |
| AntiDiagSum  | [1, 0, 1, 1, 4, 12, 52, 256, 1502] |

OrderedCycle Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 792, 8400, 25153200, 76734000, 763351047043200] |
| RowGcd     | [1, 1, 2, 2, 2, 2, 2, 24, 24] |
| RowMax     | [1, 1, 2, 6, 36, 240, 2040, 21000, 235200] |
| ColMiddle  | [1, 0, 1, 2, 22, 100, 1350, 9744, 162456] |
| ColECenter | [1, 1, 22, 1350, 162456] |
| ColOCenter | [0, 2, 100, 9744] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 2, 6, 24, 120, 720, 5040, 40320] |
| TransSqrs  | [0, 1, 9, 80, 802, 9154, 118022, 1701048, 27139608] |
| TransNat0  | [0, 1, 5, 32, 254, 2414, 26746, 338568, 4820952] |
| TransNat1  | [1, 2, 8, 46, 342, 3108, 33324, 411360, 5741856] |

OrderedCycle Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 2, 6, 24, 120, 720, 5040, 40320]|
| DiagRow1 | [0, 1, 6, 36, 240, 1800, 15120, 141120, 1451520]|
| DiagRow2 | [0, 2, 22, 210, 2040, 21000, 231840, 2751840, 35078400]|
| DiagRow3 | [0, 6, 100, 1350, 17640, 235200, 3265920, 47628000, 731808000]|
| DiagRow4 | [0, 24, 548, 9744, 162456, 2693880, 45556560, 795175920, 14411295360]|
| DiagRow5 | [0, 120, 3528, 78792, 1614816, 32319000, 649479600, 13293292320, 279281882880]|
| DiagRow6 | [0, 720, 26136, 708744, 17368320, 410031600, 9604465200, 226750764240, 5444670591360]|
| DiagRow7 | [0, 5040, 219168, 7036200, 201828000, 5519487600, 148370508000, 3986353491120, 108116216208000]|
| DiagRow8 | [0, 40320, 2053152, 76521456, 2526193824, 78864820320, 2402005525920, 72622987557120, 2202727143576960]|

OrderedCycle Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 2, 6, 24, 120, 720, 5040, 40320] |
| DiagCol2 | [2, 6, 22, 100, 548, 3528, 26136, 219168, 2053152] |
| DiagCol3 | [6, 36, 210, 1350, 9744, 78792, 708744, 7036200, 76521456] |
| DiagCol4 | [24, 240, 2040, 17640, 162456, 1614816, 17368320, 201828000, 2526193824] |
| DiagCol5 | [120, 1800, 21000, 235200, 2693880, 32319000, 410031600, 5519487600, 78864820320] |
| DiagCol6 | [720, 15120, 231840, 3265920, 45556560, 649479600, 9604465200, 148370508000, 2402005525920] |
| DiagCol7 | [5040, 141120, 2751840, 47628000, 795175920, 13293292320, 226750764240, 3986353491120, 72622987557120] |
| DiagCol8 | [40320, 1451520, 35078400, 731808000, 14411295360, 279281882880, 5444670591360, 108116216208000, 2202727143576960] |

OrderedCycle Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow2 | [0, 3, 10, 21, 36, 55, 78, 105, 136] |
| PolyRow3 | [0, 14, 76, 222, 488, 910, 1524, 2366, 3472] |
| PolyRow4 | [0, 88, 772, 3132, 8824, 20080, 39708, 71092, 118192] |
| PolyRow5 | [0, 694, 9808, 55242, 199456, 553870, 1293264, 2670178, 5029312] |
| PolyRow6 | [0, 6578, 149552, 1169262, 5410208, 18333050, 50545008, 120348662, 256809152] |
| PolyRow7 | [0, 72792, 2660544, 28873800, 171209664, 707959800, 2304709632, 6328330344, 15298865280] |
| PolyRow8 | [0, 920904, 54093696, 814870584, 6192052800, 31244562600, 120100860864, 380302313496, 1041597412224] |

OrderedCycle Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 3, 14, 88, 694, 6578, 72792, 920904] |
| PolyCol2 | [1, 2, 10, 76, 772, 9808, 149552, 2660544, 54093696] |
| PolyCol3 | [1, 3, 21, 222, 3132, 55242, 1169262, 28873800, 814870584] |
| PolyCol4 | [1, 4, 36, 488, 8824, 199456, 5410208, 171209664, 6192052800] |
| PolyCol5 | [1, 5, 55, 910, 20080, 553870, 18333050, 707959800, 31244562600] |
| PolyCol6 | [1, 6, 78, 1524, 39708, 1293264, 50545008, 2304709632, 120100860864] |
| PolyCol7 | [1, 7, 105, 2366, 71092, 2670178, 120348662, 6328330344, 380302313496] |
| PolyCol8 | [1, 8, 136, 3472, 118192, 5029312, 256809152, 15298865280, 1041597412224] |

# OrderedCycle:Rev
[]

OrderedCycle:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [2, 1, 0] |
| Row3 | [6, 6, 2, 0] |
| Row4 | [24, 36, 22, 6, 0] |
| Row5 | [120, 240, 210, 100, 24, 0] |
| Row6 | [720, 1800, 2040, 1350, 548, 120, 0] |
| Row7 | [5040, 15120, 21000, 17640, 9744, 3528, 720, 0] |
| Row8 | [40320, 141120, 231840, 235200, 162456, 78792, 26136, 5040, 0] |

OrderedCycle:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[1], [1, 0], [2, 1, 0], [6, 6, 2, 0], [24, 36, 22, 6, 0], [120, 240, 210, 100, 24, 0], [720, 1800, 2040, 1350, 548, 120, 0], [5040, 15120, 21000, 17640, 9744, 3528, 720, 0], [40320, 141120, 231840, 235200, 162456, 78792, 26136, 5040, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 2], [0, 2, 6, 6], [0, 6, 22, 36, 24], [0, 24, 100, 210, 240, 120], [0, 120, 548, 1350, 2040, 1800, 720], [0, 720, 3528, 9744, 17640, 21000, 15120, 5040], [0, 5040, 26136, 78792, 162456, 235200, 231840, 141120, 40320]] |
| AntiDiag   | [[1], [1], [2, 0], [6, 1], [24, 6, 0], [120, 36, 2], [720, 240, 22, 0], [5040, 1800, 210, 6], [40320, 15120, 2040, 100, 0]] |
| AccTabl    | [[1], [1, 1], [2, 3, 3], [6, 12, 14, 14], [24, 60, 82, 88, 88], [120, 360, 570, 670, 694, 694], [720, 2520, 4560, 5910, 6458, 6578, 6578], [5040, 20160, 41160, 58800, 68544, 72072, 72792, 72792], [40320, 181440, 413280, 648480, 810936, 889728, 915864, 920904, 920904]] |
| RevAccTabl | [[1], [1, 1], [3, 3, 2], [14, 14, 12, 6], [88, 88, 82, 60, 24], [694, 694, 670, 570, 360, 120], [6578, 6578, 6458, 5910, 4560, 2520, 720], [72792, 72792, 72072, 68544, 58800, 41160, 20160, 5040], [920904, 920904, 915864, 889728, 810936, 648480, 413280, 181440, 40320]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 3], [0, 2, 8, 14], [0, 6, 28, 64, 88], [0, 24, 124, 334, 574, 694], [0, 120, 668, 2018, 4058, 5858, 6578], [0, 720, 4248, 13992, 31632, 52632, 67752, 72792], [0, 5040, 31176, 109968, 272424, 507624, 739464, 880584, 920904]] |

OrderedCycle:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 3, 14, 88, 694, 6578, 72792, 920904] |
| EvenSum      | [1, 1, 2, 8, 46, 354, 3308, 36504, 460752] |
| OddSum       | [0, 0, 1, 6, 42, 340, 3270, 36288, 460152] |
| AltSum       | [1, 1, 1, 2, 4, 14, 38, 216, 600] |
| AccSum       | [1, 2, 8, 46, 342, 3108, 33324, 411360, 5741856] |
| AccRevSum    | [1, 1, 4, 24, 186, 1750, 19300, 243768, 3467184] |
| AntiDiagSum  | [1, 1, 2, 7, 30, 158, 982, 7056, 57580] |

OrderedCycle:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 2, 6, 792, 8400, 25153200, 76734000, 763351047043200] |
| RowGcd     | [1, 1, 2, 2, 2, 2, 2, 24, 24] |
| RowMax     | [1, 1, 2, 6, 36, 240, 2040, 21000, 235200] |
| ColMiddle  | [1, 1, 1, 6, 22, 210, 1350, 17640, 162456] |
| ColECenter | [1, 1, 22, 1350, 162456] |
| ColOCenter | [1, 6, 210, 17640] |
| ColLeft    | [1, 1, 2, 6, 24, 120, 720, 5040, 40320] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 14, 178, 2364, 33878, 527904, 8942232] |
| TransNat0  | [0, 0, 1, 10, 98, 1056, 12722, 170976, 2546280] |
| TransNat1  | [1, 1, 4, 24, 186, 1750, 19300, 243768, 3467184] |

OrderedCycle:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 2, 6, 24, 120, 720, 5040, 40320]|
| DiagRow2 | [2, 6, 22, 100, 548, 3528, 26136, 219168, 2053152]|
| DiagRow3 | [6, 36, 210, 1350, 9744, 78792, 708744, 7036200, 76521456]|
| DiagRow4 | [24, 240, 2040, 17640, 162456, 1614816, 17368320, 201828000, 2526193824]|
| DiagRow5 | [120, 1800, 21000, 235200, 2693880, 32319000, 410031600, 5519487600, 78864820320]|
| DiagRow6 | [720, 15120, 231840, 3265920, 45556560, 649479600, 9604465200, 148370508000, 2402005525920]|
| DiagRow7 | [5040, 141120, 2751840, 47628000, 795175920, 13293292320, 226750764240, 3986353491120, 72622987557120]|
| DiagRow8 | [40320, 1451520, 35078400, 731808000, 14411295360, 279281882880, 5444670591360, 108116216208000, 2202727143576960]|

OrderedCycle:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 2, 6, 24, 120, 720, 5040, 40320] |
| DiagCol1 | [0, 1, 6, 36, 240, 1800, 15120, 141120, 1451520] |
| DiagCol2 | [0, 2, 22, 210, 2040, 21000, 231840, 2751840, 35078400] |
| DiagCol3 | [0, 6, 100, 1350, 17640, 235200, 3265920, 47628000, 731808000] |
| DiagCol4 | [0, 24, 548, 9744, 162456, 2693880, 45556560, 795175920, 14411295360] |
| DiagCol5 | [0, 120, 3528, 78792, 1614816, 32319000, 649479600, 13293292320, 279281882880] |
| DiagCol6 | [0, 720, 26136, 708744, 17368320, 410031600, 9604465200, 226750764240, 5444670591360] |
| DiagCol7 | [0, 5040, 219168, 7036200, 201828000, 5519487600, 148370508000, 3986353491120, 108116216208000] |
| DiagCol8 | [0, 40320, 2053152, 76521456, 2526193824, 78864820320, 2402005525920, 72622987557120, 2202727143576960] |

OrderedCycle:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow3 | [6, 14, 26, 42, 62, 86, 114, 146, 182] |
| PolyRow4 | [24, 88, 232, 492, 904, 1504, 2328, 3412, 4792] |
| PolyRow5 | [120, 694, 2624, 7374, 16984, 34070, 61824, 104014, 164984] |
| PolyRow6 | [720, 6578, 35888, 134478, 390128, 946970, 2019888, 3908918, 7013648] |
| PolyRow7 | [5040, 72792, 575280, 2887128, 10586736, 31175640, 78316272, 174588120, 354762288] |
| PolyRow8 | [40320, 920904, 10569984, 71281656, 331267200, 1185826920, 3513544704, 9032906904, 20804747136] |

OrderedCycle:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 2, 6, 24, 120, 720, 5040, 40320] |
| PolyCol1 | [1, 1, 3, 14, 88, 694, 6578, 72792, 920904] |
| PolyCol2 | [1, 1, 4, 26, 232, 2624, 35888, 575280, 10569984] |
| PolyCol3 | [1, 1, 5, 42, 492, 7374, 134478, 2887128, 71281656] |
| PolyCol4 | [1, 1, 6, 62, 904, 16984, 390128, 10586736, 331267200] |
| PolyCol5 | [1, 1, 7, 86, 1504, 34070, 946970, 31175640, 1185826920] |
| PolyCol6 | [1, 1, 8, 114, 2328, 61824, 2019888, 78316272, 3513544704] |
| PolyCol7 | [1, 1, 9, 146, 3412, 104014, 3908918, 174588120, 9032906904] |
| PolyCol8 | [1, 1, 10, 182, 4792, 164984, 7013648, 354762288, 20804747136] |
