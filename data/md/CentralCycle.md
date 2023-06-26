# CentralCycle
['A269940', 'A111999', 'A259456']

CentralCycle Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 2, 3] |
| Row3 | [0, 6, 20, 15] |
| Row4 | [0, 24, 130, 210, 105] |
| Row5 | [0, 120, 924, 2380, 2520, 945] |
| Row6 | [0, 720, 7308, 26432, 44100, 34650, 10395] |
| Row7 | [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135] |
| Row8 | [0, 40320, 623376, 3678840, 11098780, 18858840, 18288270, 9459450, 2027025] |

CentralCycle Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[1], [0, 1], [0, 2, 3], [0, 6, 20, 15], [0, 24, 130, 210, 105], [0, 120, 924, 2380, 2520, 945], [0, 720, 7308, 26432, 44100, 34650, 10395], [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135], [0, 40320, 623376, 3678840, 11098780, 18858840, 18288270, 9459450, 2027025]] |
| RevTabl    | [[1], [1, 0], [3, 2, 0], [15, 20, 6, 0], [105, 210, 130, 24, 0], [945, 2520, 2380, 924, 120, 0], [10395, 34650, 44100, 26432, 7308, 720, 0], [135135, 540540, 866250, 705320, 303660, 64224, 5040, 0], [2027025, 9459450, 18288270, 18858840, 11098780, 3678840, 623376, 40320, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 2], [0, 6, 3], [0, 24, 20], [0, 120, 130, 15], [0, 720, 924, 210], [0, 5040, 7308, 2380, 105]] |
| AccTabl    | [[1], [0, 1], [0, 2, 5], [0, 6, 26, 41], [0, 24, 154, 364, 469], [0, 120, 1044, 3424, 5944, 6889], [0, 720, 8028, 34460, 78560, 113210, 123605], [0, 5040, 69264, 372924, 1078244, 1944494, 2485034, 2620169], [0, 40320, 663696, 4342536, 15441316, 34300156, 52588426, 62047876, 64074901]] |
| RevAccTabl | [[1], [1, 0], [5, 2, 0], [41, 26, 6, 0], [469, 364, 154, 24, 0], [6889, 5944, 3424, 1044, 120, 0], [123605, 113210, 78560, 34460, 8028, 720, 0], [2620169, 2485034, 1944494, 1078244, 372924, 69264, 5040, 0], [64074901, 62047876, 52588426, 34300156, 15441316, 4342536, 663696, 40320, 0]] |
| AccRevTabl | [[1], [1, 1], [3, 5, 5], [15, 35, 41, 41], [105, 315, 445, 469, 469], [945, 3465, 5845, 6769, 6889, 6889], [10395, 45045, 89145, 115577, 122885, 123605, 123605], [135135, 675675, 1541925, 2247245, 2550905, 2615129, 2620169, 2620169], [2027025, 11486475, 29774745, 48633585, 59732365, 63411205, 64034581, 64074901, 64074901]] |

CentralCycle Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 5, 41, 469, 6889, 123605, 2620169, 64074901] |
| EvenSum      | [1, 0, 3, 20, 235, 3444, 61803, 1310084, 32037451] |
| OddSum       | [0, 1, 2, 21, 234, 3445, 61802, 1310085, 32037450] |
| AltSum       | [1, -1, 1, -1, 1, -1, 1, -1, 1] |
| AccSum       | [1, 1, 7, 73, 1011, 17421, 358583, 8575169, 233499227] |
| AccRevSum    | [1, 2, 13, 132, 1803, 30802, 630257, 15006352, 407249783] |
| AntiDiagSum  | [1, 0, 1, 2, 9, 44, 265, 1854, 14833] |

CentralCycle Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 6, 60, 10920, 1413720, 39840292800, 6652505239380000, 2048503569859181635200] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 3, 20, 210, 2520, 44100, 866250, 18858840] |
| ColMiddle  | [1, 0, 2, 6, 130, 924, 26432, 303660, 11098780] |
| ColECenter | [1, 2, 130, 26432, 11098780] |
| ColOCenter | [0, 6, 924, 303660] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025] |
| TransSqrs  | [0, 1, 14, 221, 4114, 89181, 2213910, 62017301, 1936315234] |
| TransNat0  | [0, 1, 8, 91, 1334, 23913, 506652, 12386183, 343174882] |
| TransNat1  | [1, 2, 13, 132, 1803, 30802, 630257, 15006352, 407249783] |

CentralCycle Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025]|
| DiagRow1 | [0, 2, 20, 210, 2520, 34650, 540540, 9459450, 183783600]|
| DiagRow2 | [0, 6, 130, 2380, 44100, 866250, 18288270, 416215800, 10199989800]|
| DiagRow3 | [0, 24, 924, 26432, 705320, 18858840, 520059540, 14980405440, 453247114320]|
| DiagRow4 | [0, 120, 7308, 303660, 11098780, 389449060, 13642629000, 486591585480, 17856935296200]|
| DiagRow5 | [0, 720, 64224, 3678840, 177331440, 7934927000, 345240896000, 14972984666640, 656598399256800]|
| DiagRow6 | [0, 5040, 623376, 47324376, 2920525608, 162831789120, 8637235647040, 448594185959920, 23209044289551120]|
| DiagRow7 | [0, 40320, 6636960, 647536032, 49952862960, 3404554433280, 216752221445760, 13306928148113600, 803351393628623840]|
| DiagRow8 | [0, 362880, 76998240, 9418945536, 890577127440, 73017236532240, 5505619701582000, 395063504843607600, 27563542664861323120]|

CentralCycle Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 2, 6, 24, 120, 720, 5040, 40320, 362880] |
| DiagCol2 | [3, 20, 130, 924, 7308, 64224, 623376, 6636960, 76998240] |
| DiagCol3 | [15, 210, 2380, 26432, 303660, 3678840, 47324376, 647536032, 9418945536] |
| DiagCol4 | [105, 2520, 44100, 705320, 11098780, 177331440, 2920525608, 49952862960, 890577127440] |
| DiagCol5 | [945, 34650, 866250, 18858840, 389449060, 7934927000, 162831789120, 3404554433280, 73017236532240] |
| DiagCol6 | [10395, 540540, 18288270, 520059540, 13642629000, 345240896000, 8637235647040, 216752221445760, 5505619701582000] |
| DiagCol7 | [135135, 9459450, 416215800, 14980405440, 486591585480, 14972984666640, 448594185959920, 13306928148113600, 395063504843607600] |
| DiagCol8 | [2027025, 183783600, 10199989800, 453247114320, 17856935296200, 656598399256800, 23209044289551120, 803351393628623840, 27563542664861323120] |

CentralCycle Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow2 | [0, 5, 16, 33, 56, 85, 120, 161, 208] |
| PolyRow3 | [0, 41, 212, 603, 1304, 2405, 3996, 6167, 9008] |
| PolyRow4 | [0, 469, 3928, 15417, 42496, 95245, 186264, 330673, 546112] |
| PolyRow5 | [0, 6889, 93536, 506691, 1780384, 4849325, 11162304, 22795591, 42566336] |
| PolyRow6 | [0, 123605, 2721808, 20351601, 91160576, 301755925, 817557840, 1920637313, 4055038336] |
| PolyRow7 | [0, 2620169, 93593216, 966015531, 5516187584, 22190803925, 70766573184, 191243348471, 456531848576] |
| PolyRow8 | [0, 64074901, 3713245504, 52906036329, 385133814016, 1882926644125, 7067769414336, 21972157620049, 59305251856384] |

CentralCycle Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 5, 41, 469, 6889, 123605, 2620169, 64074901] |
| PolyCol2 | [1, 2, 16, 212, 3928, 93536, 2721808, 93593216, 3713245504] |
| PolyCol3 | [1, 3, 33, 603, 15417, 506691, 20351601, 966015531, 52906036329] |
| PolyCol4 | [1, 4, 56, 1304, 42496, 1780384, 91160576, 5516187584, 385133814016] |
| PolyCol5 | [1, 5, 85, 2405, 95245, 4849325, 301755925, 22190803925, 1882926644125] |
| PolyCol6 | [1, 6, 120, 3996, 186264, 11162304, 817557840, 70766573184, 7067769414336] |
| PolyCol7 | [1, 7, 161, 6167, 330673, 22795591, 1920637313, 191243348471, 21972157620049] |
| PolyCol8 | [1, 8, 208, 9008, 546112, 42566336, 4055038336, 456531848576, 59305251856384] |

# CentralCycle:Rev
[]

CentralCycle:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [3, 2, 0] |
| Row3 | [15, 20, 6, 0] |
| Row4 | [105, 210, 130, 24, 0] |
| Row5 | [945, 2520, 2380, 924, 120, 0] |
| Row6 | [10395, 34650, 44100, 26432, 7308, 720, 0] |
| Row7 | [135135, 540540, 866250, 705320, 303660, 64224, 5040, 0] |
| Row8 | [2027025, 9459450, 18288270, 18858840, 11098780, 3678840, 623376, 40320, 0] |

CentralCycle:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Tabl       | [[1], [1, 0], [3, 2, 0], [15, 20, 6, 0], [105, 210, 130, 24, 0], [945, 2520, 2380, 924, 120, 0], [10395, 34650, 44100, 26432, 7308, 720, 0], [135135, 540540, 866250, 705320, 303660, 64224, 5040, 0], [2027025, 9459450, 18288270, 18858840, 11098780, 3678840, 623376, 40320, 0]] |
| RevTabl    | [[1], [0, 1], [0, 2, 3], [0, 6, 20, 15], [0, 24, 130, 210, 105], [0, 120, 924, 2380, 2520, 945], [0, 720, 7308, 26432, 44100, 34650, 10395], [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135], [0, 40320, 623376, 3678840, 11098780, 18858840, 18288270, 9459450, 2027025]] |
| AntiDiag   | [[1], [1], [3, 0], [15, 2], [105, 20, 0], [945, 210, 6], [10395, 2520, 130, 0], [135135, 34650, 2380, 24], [2027025, 540540, 44100, 924, 0]] |
| AccTabl    | [[1], [1, 1], [3, 5, 5], [15, 35, 41, 41], [105, 315, 445, 469, 469], [945, 3465, 5845, 6769, 6889, 6889], [10395, 45045, 89145, 115577, 122885, 123605, 123605], [135135, 675675, 1541925, 2247245, 2550905, 2615129, 2620169, 2620169], [2027025, 11486475, 29774745, 48633585, 59732365, 63411205, 64034581, 64074901, 64074901]] |
| RevAccTabl | [[1], [1, 1], [5, 5, 3], [41, 41, 35, 15], [469, 469, 445, 315, 105], [6889, 6889, 6769, 5845, 3465, 945], [123605, 123605, 122885, 115577, 89145, 45045, 10395], [2620169, 2620169, 2615129, 2550905, 2247245, 1541925, 675675, 135135], [64074901, 64074901, 64034581, 63411205, 59732365, 48633585, 29774745, 11486475, 2027025]] |
| AccRevTabl | [[1], [0, 1], [0, 2, 5], [0, 6, 26, 41], [0, 24, 154, 364, 469], [0, 120, 1044, 3424, 5944, 6889], [0, 720, 8028, 34460, 78560, 113210, 123605], [0, 5040, 69264, 372924, 1078244, 1944494, 2485034, 2620169], [0, 40320, 663696, 4342536, 15441316, 34300156, 52588426, 62047876, 64074901]] |

CentralCycle:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 5, 41, 469, 6889, 123605, 2620169, 64074901] |
| EvenSum      | [1, 1, 3, 21, 235, 3445, 61803, 1310085, 32037451] |
| OddSum       | [0, 0, 2, 20, 234, 3444, 61802, 1310084, 32037450] |
| AltSum       | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| AccSum       | [1, 2, 13, 132, 1803, 30802, 630257, 15006352, 407249783] |
| AccRevSum    | [1, 1, 7, 73, 1011, 17421, 358583, 8575169, 233499227] |
| AntiDiagSum  | [1, 1, 3, 17, 125, 1161, 13045, 172189, 2612589] |

CentralCycle:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 6, 60, 10920, 1413720, 39840292800, 6652505239380000, 2048503569859181635200] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 3, 20, 210, 2520, 44100, 866250, 18858840] |
| ColMiddle  | [1, 1, 2, 20, 130, 2380, 26432, 705320, 11098780] |
| ColECenter | [1, 2, 130, 26432, 11098780] |
| ColOCenter | [1, 20, 2380, 705320] |
| ColLeft    | [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 2, 44, 946, 22276, 583866, 16999020, 546310786] |
| TransNat0  | [0, 0, 2, 32, 542, 10532, 234978, 5955000, 169424326] |
| TransNat1  | [1, 1, 7, 73, 1011, 17421, 358583, 8575169, 233499227] |

CentralCycle:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]|
| DiagRow2 | [3, 20, 130, 924, 7308, 64224, 623376, 6636960, 76998240]|
| DiagRow3 | [15, 210, 2380, 26432, 303660, 3678840, 47324376, 647536032, 9418945536]|
| DiagRow4 | [105, 2520, 44100, 705320, 11098780, 177331440, 2920525608, 49952862960, 890577127440]|
| DiagRow5 | [945, 34650, 866250, 18858840, 389449060, 7934927000, 162831789120, 3404554433280, 73017236532240]|
| DiagRow6 | [10395, 540540, 18288270, 520059540, 13642629000, 345240896000, 8637235647040, 216752221445760, 5505619701582000]|
| DiagRow7 | [135135, 9459450, 416215800, 14980405440, 486591585480, 14972984666640, 448594185959920, 13306928148113600, 395063504843607600]|
| DiagRow8 | [2027025, 183783600, 10199989800, 453247114320, 17856935296200, 656598399256800, 23209044289551120, 803351393628623840, 27563542664861323120]|

CentralCycle:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025] |
| DiagCol1 | [0, 2, 20, 210, 2520, 34650, 540540, 9459450, 183783600] |
| DiagCol2 | [0, 6, 130, 2380, 44100, 866250, 18288270, 416215800, 10199989800] |
| DiagCol3 | [0, 24, 924, 26432, 705320, 18858840, 520059540, 14980405440, 453247114320] |
| DiagCol4 | [0, 120, 7308, 303660, 11098780, 389449060, 13642629000, 486591585480, 17856935296200] |
| DiagCol5 | [0, 720, 64224, 3678840, 177331440, 7934927000, 345240896000, 14972984666640, 656598399256800] |
| DiagCol6 | [0, 5040, 623376, 47324376, 2920525608, 162831789120, 8637235647040, 448594185959920, 23209044289551120] |
| DiagCol7 | [0, 40320, 6636960, 647536032, 49952862960, 3404554433280, 216752221445760, 13306928148113600, 803351393628623840] |
| DiagCol8 | [0, 362880, 76998240, 9418945536, 890577127440, 73017236532240, 5505619701582000, 395063504843607600, 27563542664861323120] |

CentralCycle:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [3, 5, 7, 9, 11, 13, 15, 17, 19] |
| PolyRow3 | [15, 41, 79, 129, 191, 265, 351, 449, 559] |
| PolyRow4 | [105, 469, 1237, 2553, 4561, 7405, 11229, 16177, 22393] |
| PolyRow5 | [945, 6889, 24817, 64593, 138961, 263545, 456849, 740257, 1138033] |
| PolyRow6 | [10395, 123605, 607519, 1991817, 5154371, 11407645, 22585095, 41127569, 70169707] |
| PolyRow7 | [135135, 2620169, 17560063, 72473697, 225443951, 581896585, 1315007919, 2689741313, 5090512447] |
| PolyRow8 | [2027025, 64074901, 585330109, 3039768729, 11361813721, 34187248525, 88152599781, 202456201969, 424884156769] |

CentralCycle:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 3, 15, 105, 945, 10395, 135135, 2027025] |
| PolyCol1 | [1, 1, 5, 41, 469, 6889, 123605, 2620169, 64074901] |
| PolyCol2 | [1, 1, 7, 79, 1237, 24817, 607519, 17560063, 585330109] |
| PolyCol3 | [1, 1, 9, 129, 2553, 64593, 1991817, 72473697, 3039768729] |
| PolyCol4 | [1, 1, 11, 191, 4561, 138961, 5154371, 225443951, 11361813721] |
| PolyCol5 | [1, 1, 13, 265, 7405, 263545, 11407645, 581896585, 34187248525] |
| PolyCol6 | [1, 1, 15, 351, 11229, 456849, 22585095, 1315007919, 88152599781] |
| PolyCol7 | [1, 1, 17, 449, 16177, 740257, 41127569, 2689741313, 202456201969] |
| PolyCol8 | [1, 1, 19, 559, 22393, 1138033, 70169707, 5090512447, 424884156769] |
