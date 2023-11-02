# StirlingSetB
['A154602']

StirlingSetB Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 1] |
| Row2 | [3, 4, 1] |
| Row3 | [11, 19, 9, 1] |
| Row4 | [49, 104, 70, 16, 1] |
| Row5 | [257, 641, 550, 190, 25, 1] |
| Row6 | [1539, 4380, 4531, 2080, 425, 36, 1] |
| Row7 | [10299, 32803, 39515, 22491, 6265, 833, 49, 1] |
| Row8 | [75905, 266768, 365324, 247072, 87206, 16016, 1484, 64, 1] |
| Row9 | [609441, 2337505, 3575820, 2792476, 1192086, 281190, 36204, 2460, 81, 1] |

StirlingSetB Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 1], [3, 4, 1], [11, 19, 9, 1], [49, 104, 70, 16, 1], [257, 641, 550, 190, 25, 1], [1539, 4380, 4531, 2080, 425, 36, 1], [10299, 32803, 39515, 22491, 6265, 833, 49, 1], [75905, 266768, 365324, 247072, 87206, 16016, 1484, 64, 1], [609441, 2337505, 3575820, 2792476, 1192086, 281190, 36204, 2460, 81, 1]] |
| RevTabl    | [[1], [1, 1], [1, 4, 3], [1, 9, 19, 11], [1, 16, 70, 104, 49], [1, 25, 190, 550, 641, 257], [1, 36, 425, 2080, 4531, 4380, 1539], [1, 49, 833, 6265, 22491, 39515, 32803, 10299], [1, 64, 1484, 16016, 87206, 247072, 365324, 266768, 75905], [1, 81, 2460, 36204, 281190, 1192086, 2792476, 3575820, 2337505, 609441]] |
| AntiDiag   | [[1], [1], [3, 1], [11, 4], [49, 19, 1], [257, 104, 9], [1539, 641, 70, 1], [10299, 4380, 550, 16], [75905, 32803, 4531, 190, 1], [609441, 266768, 39515, 2080, 25]] |
| AccTabl    | [[1], [1, 2], [3, 7, 8], [11, 30, 39, 40], [49, 153, 223, 239, 240], [257, 898, 1448, 1638, 1663, 1664], [1539, 5919, 10450, 12530, 12955, 12991, 12992], [10299, 43102, 82617, 105108, 111373, 112206, 112255, 112256], [75905, 342673, 707997, 955069, 1042275, 1058291, 1059775, 1059839, 1059840], [609441, 2946946, 6522766, 9315242, 10507328, 10788518, 10824722, 10827182, 10827263, 10827264]] |
| RevAccTabl | [[1], [2, 1], [8, 7, 3], [40, 39, 30, 11], [240, 239, 223, 153, 49], [1664, 1663, 1638, 1448, 898, 257], [12992, 12991, 12955, 12530, 10450, 5919, 1539], [112256, 112255, 112206, 111373, 105108, 82617, 43102, 10299], [1059840, 1059839, 1059775, 1058291, 1042275, 955069, 707997, 342673, 75905], [10827264, 10827263, 10827182, 10824722, 10788518, 10507328, 9315242, 6522766, 2946946, 609441]] |
| AccRevTabl | [[1], [1, 2], [1, 5, 8], [1, 10, 29, 40], [1, 17, 87, 191, 240], [1, 26, 216, 766, 1407, 1664], [1, 37, 462, 2542, 7073, 11453, 12992], [1, 50, 883, 7148, 29639, 69154, 101957, 112256], [1, 65, 1549, 17565, 104771, 351843, 717167, 983935, 1059840], [1, 82, 2542, 38746, 319936, 1512022, 4304498, 7880318, 10217823, 10827264]] |

StirlingSetB Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 2, 8, 40, 240, 1664, 12992, 112256, 1059840, 10827264] |
| EvenSum      | [1, 1, 4, 20, 120, 832, 6496, 56128, 529920, 5413632] |
| OddSum       | [0, 1, 4, 20, 120, 832, 6496, 56128, 529920, 5413632] |
| AltSum       | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| AccSum       | [1, 3, 18, 120, 904, 7568, 69376, 689216, 7361664, 83996672] |
| AccRevSum    | [1, 3, 14, 80, 536, 4080, 34560, 321088, 3236736, 35103232] |
| DiagSum      | [1, 1, 4, 15, 69, 370, 2251, 15245, 113430, 917829] |

StirlingSetB Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 12, 1881, 50960, 1721501650, 89999024637600, 2559252346698100095, 2696411135497225545898058560, 1432981471391647933263198488937774180] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 4, 19, 104, 641, 4531, 39515, 365324, 3575820] |
| CentralE   | [1, 4, 70, 2080, 87206] |
| CentralO   | [1, 19, 550, 22491, 1192086] |
| ColMiddle  | [1, 1, 4, 19, 70, 550, 2080, 22491, 87206, 1192086] |
| ColLeft    | [1, 1, 3, 11, 49, 257, 1539, 10299, 75905, 609441] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 8, 64, 544, 4976, 48960, 516160, 5804032, 69305344] |
| TransNat0  | [0, 1, 6, 40, 296, 2416, 21568, 208832, 2176896, 24275968] |
| TransNat1  | [1, 3, 14, 80, 536, 4080, 34560, 321088, 3236736, 35103232] |

StirlingSetB Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]|
| DiagRow2 | [3, 19, 70, 190, 425, 833, 1484, 2460, 3855, 5775]|
| DiagRow3 | [11, 104, 550, 2080, 6265, 16016, 36204, 74400, 141735, 253880]|
| DiagRow4 | [49, 641, 4531, 22491, 87206, 281190, 786282, 1963962, 4477407, 9467887]|
| DiagRow5 | [257, 4380, 39515, 247072, 1192086, 4719624, 15982890, 47710080, 128395839, 316928612]|
| DiagRow6 | [1539, 32803, 365324, 2792476, 16333150, 77684398, 312957436, 1100247148, 3453398377, 9851037625]|
| DiagRow7 | [10299, 266768, 3575820, 32659840, 226854430, 1273177488, 6009565276, 24567605920, 88980093345, 290694358240]|
| DiagRow8 | [75905, 2337505, 36971461, 396255541, 3214789391, 20975230991, 114503039651, 538271502483, 2228251766598, 8269472552198]|
| DiagRow9 | [609441, 21925236, 402741581, 4991365808, 46656245207, 349498569420, 2181984567763, 11679738598528, 54792517079014, 229294798634616]|

StirlingSetB Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 3, 11, 49, 257, 1539, 10299, 75905, 609441] |
| DiagCol1 | [1, 4, 19, 104, 641, 4380, 32803, 266768, 2337505, 21925236] |
| DiagCol2 | [1, 9, 70, 550, 4531, 39515, 365324, 3575820, 36971461, 402741581] |
| DiagCol3 | [1, 16, 190, 2080, 22491, 247072, 2792476, 32659840, 396255541, 4991365808] |
| DiagCol4 | [1, 25, 425, 6265, 87206, 1192086, 16333150, 226854430, 3214789391, 46656245207] |
| DiagCol5 | [1, 36, 833, 16016, 281190, 4719624, 77684398, 1273177488, 20975230991, 349498569420] |
| DiagCol6 | [1, 49, 1484, 36204, 786282, 15982890, 312957436, 6009565276, 114503039651, 2181984567763] |
| DiagCol7 | [1, 64, 2460, 74400, 1963962, 47710080, 1100247148, 24567605920, 538271502483, 11679738598528] |
| DiagCol8 | [1, 81, 3855, 141735, 4477407, 128395839, 3453398377, 88980093345, 2228251766598, 54792517079014] |
| DiagCol9 | [1, 100, 5775, 253880, 9467887, 316928612, 9851037625, 290694358240, 8269472552198, 229294798634616] |

StirlingSetB Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow2 | [3, 8, 15, 24, 35, 48, 63, 80, 99, 120] |
| PolyRow3 | [11, 40, 93, 176, 295, 456, 665, 928, 1251, 1640] |
| PolyRow4 | [49, 240, 681, 1504, 2865, 4944, 7945, 12096, 17649, 24880] |
| PolyRow5 | [257, 1664, 5691, 14528, 31205, 59712, 105119, 173696, 273033, 412160] |
| PolyRow6 | [1539, 12992, 53079, 155520, 374435, 790464, 1517607, 2710784, 4574115, 7369920] |
| PolyRow7 | [10299, 112256, 544053, 1819392, 4887095, 11336064, 23650641, 45521408, 82216467, 141018240] |
| PolyRow8 | [75905, 1059840, 6058545, 23019008, 68718465, 174558720, 394588145, 816215040, 1574116353, 2867886080] |
| PolyRow9 | [609441, 10827264, 72652179, 312413184, 1033170405, 2865993216, 7001918679, 15530747904, 31917555369, 61652866560] |

StirlingSetB Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 3, 11, 49, 257, 1539, 10299, 75905, 609441] |
| PolyCol1 | [1, 2, 8, 40, 240, 1664, 12992, 112256, 1059840, 10827264] |
| PolyCol2 | [1, 3, 15, 93, 681, 5691, 53079, 544053, 6058545, 72652179] |
| PolyCol3 | [1, 4, 24, 176, 1504, 14528, 155520, 1819392, 23019008, 312413184] |
| PolyCol4 | [1, 5, 35, 295, 2865, 31205, 374435, 4887095, 68718465, 1033170405] |
| PolyCol5 | [1, 6, 48, 456, 4944, 59712, 790464, 11336064, 174558720, 2865993216] |
| PolyCol6 | [1, 7, 63, 665, 7945, 105119, 1517607, 23650641, 394588145, 7001918679] |
| PolyCol7 | [1, 8, 80, 928, 12096, 173696, 2710784, 45521408, 816215040, 15530747904] |
| PolyCol8 | [1, 9, 99, 1251, 17649, 273033, 4574115, 82216467, 1574116353, 31917555369] |
| PolyCol9 | [1, 10, 120, 1640, 24880, 412160, 7369920, 141018240, 2867886080, 61652866560] |

# StirlingSetB:Inv
[]

StirlingSetB:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [-1, 1] |
| Row2 | [1, -4, 1] |
| Row3 | [-1, 17, -9, 1] |
| Row4 | [1, -96, 74, -16, 1] |
| Row5 | [-1, 729, -690, 210, -25, 1] |
| Row6 | [1, -7060, 7579, -2840, 475, -36, 1] |
| Row7 | [-1, 83033, -97307, 41979, -8715, 931, -49, 1] |
| Row8 | [1, -1146656, 1436532, -687232, 166054, -22176, 1652, -64, 1] |
| Row9 | [-1, 18164625, -24010788, 12447812, -3370710, 528150, -49476, 2724, -81, 1] |

StirlingSetB:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [-1, 1], [1, -4, 1], [-1, 17, -9, 1], [1, -96, 74, -16, 1], [-1, 729, -690, 210, -25, 1], [1, -7060, 7579, -2840, 475, -36, 1], [-1, 83033, -97307, 41979, -8715, 931, -49, 1], [1, -1146656, 1436532, -687232, 166054, -22176, 1652, -64, 1], [-1, 18164625, -24010788, 12447812, -3370710, 528150, -49476, 2724, -81, 1]] |
| RevTabl    | [[1], [1, -1], [1, -4, 1], [1, -9, 17, -1], [1, -16, 74, -96, 1], [1, -25, 210, -690, 729, -1], [1, -36, 475, -2840, 7579, -7060, 1], [1, -49, 931, -8715, 41979, -97307, 83033, -1], [1, -64, 1652, -22176, 166054, -687232, 1436532, -1146656, 1], [1, -81, 2724, -49476, 528150, -3370710, 12447812, -24010788, 18164625, -1]] |
| AntiDiag   | [[1], [-1], [1, 1], [-1, -4], [1, 17, 1], [-1, -96, -9], [1, 729, 74, 1], [-1, -7060, -690, -16], [1, 83033, 7579, 210, 1], [-1, -1146656, -97307, -2840, -25]] |
| AccTabl    | [[1], [-1, 0], [1, -3, -2], [-1, 16, 7, 8], [1, -95, -21, -37, -36], [-1, 728, 38, 248, 223, 224], [1, -7059, 520, -2320, -1845, -1881, -1880], [-1, 83032, -14275, 27704, 18989, 19920, 19871, 19872], [1, -1146655, 289877, -397355, -231301, -253477, -251825, -251889, -251888], [-1, 18164624, -5846164, 6601648, 3230938, 3759088, 3709612, 3712336, 3712255, 3712256]] |
| RevAccTabl | [[1], [0, -1], [-2, -3, 1], [8, 7, 16, -1], [-36, -37, -21, -95, 1], [224, 223, 248, 38, 728, -1], [-1880, -1881, -1845, -2320, 520, -7059, 1], [19872, 19871, 19920, 18989, 27704, -14275, 83032, -1], [-251888, -251889, -251825, -253477, -231301, -397355, 289877, -1146655, 1], [3712256, 3712255, 3712336, 3709612, 3759088, 3230938, 6601648, -5846164, 18164624, -1]] |
| AccRevTabl | [[1], [1, 0], [1, -3, -2], [1, -8, 9, 8], [1, -15, 59, -37, -36], [1, -24, 186, -504, 225, 224], [1, -35, 440, -2400, 5179, -1881, -1880], [1, -48, 883, -7832, 34147, -63160, 19873, 19872], [1, -63, 1589, -20587, 145467, -541765, 894767, -251889, -251888], [1, -80, 2644, -46832, 481318, -2889392, 9558420, -14452368, 3712257, 3712256]] |

StirlingSetB:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 0, -2, 8, -36, 224, -1880, 19872, -251888, 3712256] |
| EvenSum      | [1, -1, 2, -10, 76, -716, 8056, -106072, 1604240, -27431056] |
| OddSum       | [0, 1, -4, 18, -112, 940, -9936, 125944, -1856128, 31143312] |
| AltSum       | [1, -2, 6, -28, 188, -1656, 17992, -232016, 3460368, -58574368] |
| AccSum       | [1, -1, -4, 30, -188, 1460, -14464, 175112, -2494512, 40756592] |
| AccRevSum    | [1, 1, -4, 10, -28, 108, -576, 3736, -24368, 78224] |
| DiagSum      | [1, -1, 2, -5, 19, -106, 805, -7767, 90824, -1246829] |

StirlingSetB:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 4, 153, 3552, 5868450, 6496374713400, 2674413767201758365, 8381602311980946048, 4858073254198633258246924716385500] |
| RowGcd     | [1, 1, 4, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 4, 17, 96, 729, 7579, 97307, 1436532, 24010788] |
| CentralE   | [1, -4, 74, -2840, 166054] |
| CentralO   | [-1, 17, -690, 41979, -3370710] |
| ColMiddle  | [1, -1, -4, 17, 74, -690, -2840, 41979, 166054, -3370710] |
| ColLeft    | [1, -1, 1, -1, 1, -1, 1, -1, 1, -1] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 0, -10, 72, -516, 4432, -46264, 573248, -8228592] |
| TransNat0  | [0, 1, -2, 2, 8, -116, 1304, -16136, 227520, -3634032] |
| TransNat1  | [1, 1, -4, 10, -28, 108, -576, 3736, -24368, 78224] |

StirlingSetB:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [-1, -4, -9, -16, -25, -36, -49, -64, -81, -100]|
| DiagRow2 | [1, 17, 74, 210, 475, 931, 1652, 2724, 4245, 6325]|
| DiagRow3 | [-1, -96, -690, -2840, -8715, -22176, -49476, -100080, -187605, -330880]|
| DiagRow4 | [1, 729, 7579, 41979, 166054, 528150, 1438458, 3485658, 7707183, 15827383]|
| DiagRow5 | [-1, -7060, -97307, -687232, -3370710, -13006392, -42224490, -120192864, -308369919, -727106380]|
| DiagRow6 | [1, 83033, 1436532, 12447812, 73502330, 336073562, 1275590756, 4196756564, 12322357619, 32965275915]|
| DiagRow7 | [-1, -1146656, -24010788, -248149040, -1724283770, -9167835072, -40044216212, -150231628976, -498945642195, -1499056004160]|
| DiagRow8 | [1, 18164625, 448512021, 5410685621, 43452161071, 264582272383, 1312610750451, 5551818806963, 20649462986438, 69063422294438]|
| DiagRow9 | [-1, -324488068, -9263024749, -128249515152, -1173170731447, -8078528373916, -45023002083059, -212622436229632, -878088454231846, -3244340330395736]|

StirlingSetB:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, -1, 1, -1, 1, -1, 1, -1, 1, -1] |
| DiagCol1 | [1, -4, 17, -96, 729, -7060, 83033, -1146656, 18164625, -324488068] |
| DiagCol2 | [1, -9, 74, -690, 7579, -97307, 1436532, -24010788, 448512021, -9263024749] |
| DiagCol3 | [1, -16, 210, -2840, 41979, -687232, 12447812, -248149040, 5410685621, -128249515152] |
| DiagCol4 | [1, -25, 475, -8715, 166054, -3370710, 73502330, -1724283770, 43452161071, -1173170731447] |
| DiagCol5 | [1, -36, 931, -22176, 528150, -13006392, 336073562, -9167835072, 264582272383, -8078528373916] |
| DiagCol6 | [1, -49, 1652, -49476, 1438458, -42224490, 1275590756, -40044216212, 1312610750451, -45023002083059] |
| DiagCol7 | [1, -64, 2724, -100080, 3485658, -120192864, 4196756564, -150231628976, 5551818806963, -212622436229632] |
| DiagCol8 | [1, -81, 4245, -187605, 7707183, -308369919, 12322357619, -498945642195, 20649462986438, -878088454231846] |
| DiagCol9 | [1, -100, 6325, -330880, 15827383, -727106380, 32965275915, -1499056004160, 69063422294438, -3244340330395736] |

StirlingSetB:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8] |
| PolyRow2 | [1, -2, -3, -2, 1, 6, 13, 22, 33, 46] |
| PolyRow3 | [-1, 8, 5, -4, -13, -16, -7, 20, 71, 152] |
| PolyRow4 | [1, -36, -7, 28, 33, -4, -71, -132, -127, 28] |
| PolyRow5 | [-1, 224, 9, -136, -61, 144, 269, 104, -441, -1216] |
| PolyRow6 | [1, -1880, -11, 808, 97, -824, -635, 904, 2593, 2152] |
| PolyRow7 | [-1, 19872, 13, -6448, -141, 4864, 1217, -6672, -7673, 5984] |
| PolyRow8 | [1, -251888, -15, 66064, 193, -37104, -2063, 40720, 17409, -66032] |
| PolyRow9 | [-1, 3712256, 17, -821728, -253, 367424, 3221, -300448, -33913, 432512] |

StirlingSetB:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, -1, 1, -1, 1, -1, 1, -1, 1, -1] |
| PolyCol1 | [1, 0, -2, 8, -36, 224, -1880, 19872, -251888, 3712256] |
| PolyCol2 | [1, 1, -3, 5, -7, 9, -11, 13, -15, 17] |
| PolyCol3 | [1, 2, -2, -4, 28, -136, 808, -6448, 66064, -821728] |
| PolyCol4 | [1, 3, 1, -13, 33, -61, 97, -141, 193, -253] |
| PolyCol5 | [1, 4, 6, -16, -4, 144, -824, 4864, -37104, 367424] |
| PolyCol6 | [1, 5, 13, -7, -71, 269, -635, 1217, -2063, 3221] |
| PolyCol7 | [1, 6, 22, 20, -132, 104, 904, -6672, 40720, -300448] |
| PolyCol8 | [1, 7, 33, 71, -127, -441, 2593, -7673, 17409, -33913] |
| PolyCol9 | [1, 8, 46, 152, 28, -1216, 2152, 5984, -66032, 432512] |

# StirlingSetB:Rev
[]

StirlingSetB:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 1] |
| Row2 | [1, 4, 3] |
| Row3 | [1, 9, 19, 11] |
| Row4 | [1, 16, 70, 104, 49] |
| Row5 | [1, 25, 190, 550, 641, 257] |
| Row6 | [1, 36, 425, 2080, 4531, 4380, 1539] |
| Row7 | [1, 49, 833, 6265, 22491, 39515, 32803, 10299] |
| Row8 | [1, 64, 1484, 16016, 87206, 247072, 365324, 266768, 75905] |
| Row9 | [1, 81, 2460, 36204, 281190, 1192086, 2792476, 3575820, 2337505, 609441] |

StirlingSetB:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 1], [1, 4, 3], [1, 9, 19, 11], [1, 16, 70, 104, 49], [1, 25, 190, 550, 641, 257], [1, 36, 425, 2080, 4531, 4380, 1539], [1, 49, 833, 6265, 22491, 39515, 32803, 10299], [1, 64, 1484, 16016, 87206, 247072, 365324, 266768, 75905], [1, 81, 2460, 36204, 281190, 1192086, 2792476, 3575820, 2337505, 609441]] |
| RevTabl    | [[1], [1, 1], [3, 4, 1], [11, 19, 9, 1], [49, 104, 70, 16, 1], [257, 641, 550, 190, 25, 1], [1539, 4380, 4531, 2080, 425, 36, 1], [10299, 32803, 39515, 22491, 6265, 833, 49, 1], [75905, 266768, 365324, 247072, 87206, 16016, 1484, 64, 1], [609441, 2337505, 3575820, 2792476, 1192086, 281190, 36204, 2460, 81, 1]] |
| AntiDiag   | [[1], [1], [1, 1], [1, 4], [1, 9, 3], [1, 16, 19], [1, 25, 70, 11], [1, 36, 190, 104], [1, 49, 425, 550, 49], [1, 64, 833, 2080, 641]] |
| AccTabl    | [[1], [1, 2], [1, 5, 8], [1, 10, 29, 40], [1, 17, 87, 191, 240], [1, 26, 216, 766, 1407, 1664], [1, 37, 462, 2542, 7073, 11453, 12992], [1, 50, 883, 7148, 29639, 69154, 101957, 112256], [1, 65, 1549, 17565, 104771, 351843, 717167, 983935, 1059840], [1, 82, 2542, 38746, 319936, 1512022, 4304498, 7880318, 10217823, 10827264]] |
| RevAccTabl | [[1], [2, 1], [8, 5, 1], [40, 29, 10, 1], [240, 191, 87, 17, 1], [1664, 1407, 766, 216, 26, 1], [12992, 11453, 7073, 2542, 462, 37, 1], [112256, 101957, 69154, 29639, 7148, 883, 50, 1], [1059840, 983935, 717167, 351843, 104771, 17565, 1549, 65, 1], [10827264, 10217823, 7880318, 4304498, 1512022, 319936, 38746, 2542, 82, 1]] |
| AccRevTabl | [[1], [1, 2], [3, 7, 8], [11, 30, 39, 40], [49, 153, 223, 239, 240], [257, 898, 1448, 1638, 1663, 1664], [1539, 5919, 10450, 12530, 12955, 12991, 12992], [10299, 43102, 82617, 105108, 111373, 112206, 112255, 112256], [75905, 342673, 707997, 955069, 1042275, 1058291, 1059775, 1059839, 1059840], [609441, 2946946, 6522766, 9315242, 10507328, 10788518, 10824722, 10827182, 10827263, 10827264]] |

StirlingSetB:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 2, 8, 40, 240, 1664, 12992, 112256, 1059840, 10827264] |
| EvenSum      | [1, 1, 4, 20, 120, 832, 6496, 56128, 529920, 5413632] |
| OddSum       | [0, 1, 4, 20, 120, 832, 6496, 56128, 529920, 5413632] |
| AltSum       | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| AccSum       | [1, 3, 14, 80, 536, 4080, 34560, 321088, 3236736, 35103232] |
| AccRevSum    | [1, 3, 18, 120, 904, 7568, 69376, 689216, 7361664, 83996672] |
| DiagSum      | [1, 1, 2, 5, 13, 36, 107, 331, 1074, 3619] |

StirlingSetB:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 12, 1881, 50960, 1721501650, 89999024637600, 2559252346698100095, 2696411135497225545898058560, 1432981471391647933263198488937774180] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 4, 19, 104, 641, 4531, 39515, 365324, 3575820] |
| CentralE   | [1, 4, 70, 2080, 87206] |
| CentralO   | [1, 9, 190, 6265, 281190] |
| ColMiddle  | [1, 1, 4, 9, 70, 190, 2080, 6265, 87206, 281190] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 1, 3, 11, 49, 257, 1539, 10299, 75905, 609441] |
| TransSqrs  | [0, 1, 16, 184, 2016, 22416, 257856, 3093056, 38803456, 509346304] |
| TransNat0  | [0, 1, 10, 80, 664, 5904, 56384, 576960, 6301824, 73169408] |
| TransNat1  | [1, 3, 18, 120, 904, 7568, 69376, 689216, 7361664, 83996672] |

StirlingSetB:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 3, 11, 49, 257, 1539, 10299, 75905, 609441]|
| DiagRow1 | [1, 4, 19, 104, 641, 4380, 32803, 266768, 2337505, 21925236]|
| DiagRow2 | [1, 9, 70, 550, 4531, 39515, 365324, 3575820, 36971461, 402741581]|
| DiagRow3 | [1, 16, 190, 2080, 22491, 247072, 2792476, 32659840, 396255541, 4991365808]|
| DiagRow4 | [1, 25, 425, 6265, 87206, 1192086, 16333150, 226854430, 3214789391, 46656245207]|
| DiagRow5 | [1, 36, 833, 16016, 281190, 4719624, 77684398, 1273177488, 20975230991, 349498569420]|
| DiagRow6 | [1, 49, 1484, 36204, 786282, 15982890, 312957436, 6009565276, 114503039651, 2181984567763]|
| DiagRow7 | [1, 64, 2460, 74400, 1963962, 47710080, 1100247148, 24567605920, 538271502483, 11679738598528]|
| DiagRow8 | [1, 81, 3855, 141735, 4477407, 128395839, 3453398377, 88980093345, 2228251766598, 54792517079014]|
| DiagRow9 | [1, 100, 5775, 253880, 9467887, 316928612, 9851037625, 290694358240, 8269472552198, 229294798634616]|

StirlingSetB:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] |
| DiagCol2 | [3, 19, 70, 190, 425, 833, 1484, 2460, 3855, 5775] |
| DiagCol3 | [11, 104, 550, 2080, 6265, 16016, 36204, 74400, 141735, 253880] |
| DiagCol4 | [49, 641, 4531, 22491, 87206, 281190, 786282, 1963962, 4477407, 9467887] |
| DiagCol5 | [257, 4380, 39515, 247072, 1192086, 4719624, 15982890, 47710080, 128395839, 316928612] |
| DiagCol6 | [1539, 32803, 365324, 2792476, 16333150, 77684398, 312957436, 1100247148, 3453398377, 9851037625] |
| DiagCol7 | [10299, 266768, 3575820, 32659840, 226854430, 1273177488, 6009565276, 24567605920, 88980093345, 290694358240] |
| DiagCol8 | [75905, 2337505, 36971461, 396255541, 3214789391, 20975230991, 114503039651, 538271502483, 2228251766598, 8269472552198] |
| DiagCol9 | [609441, 21925236, 402741581, 4991365808, 46656245207, 349498569420, 2181984567763, 11679738598528, 54792517079014, 229294798634616] |

StirlingSetB:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow2 | [1, 8, 21, 40, 65, 96, 133, 176, 225, 280] |
| PolyRow3 | [1, 40, 183, 496, 1045, 1896, 3115, 4768, 6921, 9640] |
| PolyRow4 | [1, 240, 1929, 7456, 20385, 45456, 88585, 156864, 258561, 403120] |
| PolyRow5 | [1, 1664, 23691, 131008, 465605, 1277376, 2954959, 6056576, 11340873, 19797760] |
| PolyRow6 | [1, 12992, 329565, 2613376, 12088865, 40837056, 112199437, 266289920, 566614881, 1107801280] |
| PolyRow7 | [1, 112256, 5095551, 58038016, 349735445, 1455501696, 4751318131, 13061229056, 31587890121, 69178176640] |
| PolyRow8 | [1, 1059840, 86394513, 1415303680, 11117979585, 57028471296, 221251539985, 704619629568, 1937156666625, 4752725893120] |
| PolyRow9 | [1, 10827264, 1589803923, 37501484032, 384271283205, 2430301318656, 11208800425879, 41362490370048, 129285914272137, 355391191221760] |

StirlingSetB:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 2, 8, 40, 240, 1664, 12992, 112256, 1059840, 10827264] |
| PolyCol2 | [1, 3, 21, 183, 1929, 23691, 329565, 5095551, 86394513, 1589803923] |
| PolyCol3 | [1, 4, 40, 496, 7456, 131008, 2613376, 58038016, 1415303680, 37501484032] |
| PolyCol4 | [1, 5, 65, 1045, 20385, 465605, 12088865, 349735445, 11117979585, 384271283205] |
| PolyCol5 | [1, 6, 96, 1896, 45456, 1277376, 40837056, 1455501696, 57028471296, 2430301318656] |
| PolyCol6 | [1, 7, 133, 3115, 88585, 2954959, 112199437, 4751318131, 221251539985, 11208800425879] |
| PolyCol7 | [1, 8, 176, 4768, 156864, 6056576, 266289920, 13061229056, 704619629568, 41362490370048] |
| PolyCol8 | [1, 9, 225, 6921, 258561, 11340873, 566614881, 31587890121, 1937156666625, 129285914272137] |
| PolyCol9 | [1, 10, 280, 9640, 403120, 19797760, 1107801280, 69178176640, 4752725893120, 355391191221760] |

# StirlingSetB:Inv:Rev
[]

StirlingSetB:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, -1] |
| Row2 | [1, -4, 1] |
| Row3 | [1, -9, 17, -1] |
| Row4 | [1, -16, 74, -96, 1] |
| Row5 | [1, -25, 210, -690, 729, -1] |
| Row6 | [1, -36, 475, -2840, 7579, -7060, 1] |
| Row7 | [1, -49, 931, -8715, 41979, -97307, 83033, -1] |
| Row8 | [1, -64, 1652, -22176, 166054, -687232, 1436532, -1146656, 1] |
| Row9 | [1, -81, 2724, -49476, 528150, -3370710, 12447812, -24010788, 18164625, -1] |

StirlingSetB:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, -1], [1, -4, 1], [1, -9, 17, -1], [1, -16, 74, -96, 1], [1, -25, 210, -690, 729, -1], [1, -36, 475, -2840, 7579, -7060, 1], [1, -49, 931, -8715, 41979, -97307, 83033, -1], [1, -64, 1652, -22176, 166054, -687232, 1436532, -1146656, 1], [1, -81, 2724, -49476, 528150, -3370710, 12447812, -24010788, 18164625, -1]] |
| RevTabl    | [[1], [-1, 1], [1, -4, 1], [-1, 17, -9, 1], [1, -96, 74, -16, 1], [-1, 729, -690, 210, -25, 1], [1, -7060, 7579, -2840, 475, -36, 1], [-1, 83033, -97307, 41979, -8715, 931, -49, 1], [1, -1146656, 1436532, -687232, 166054, -22176, 1652, -64, 1], [-1, 18164625, -24010788, 12447812, -3370710, 528150, -49476, 2724, -81, 1]] |
| AntiDiag   | [[1], [1], [1, -1], [1, -4], [1, -9, 1], [1, -16, 17], [1, -25, 74, -1], [1, -36, 210, -96], [1, -49, 475, -690, 1], [1, -64, 931, -2840, 729]] |
| AccTabl    | [[1], [1, 0], [1, -3, -2], [1, -8, 9, 8], [1, -15, 59, -37, -36], [1, -24, 186, -504, 225, 224], [1, -35, 440, -2400, 5179, -1881, -1880], [1, -48, 883, -7832, 34147, -63160, 19873, 19872], [1, -63, 1589, -20587, 145467, -541765, 894767, -251889, -251888], [1, -80, 2644, -46832, 481318, -2889392, 9558420, -14452368, 3712257, 3712256]] |
| RevAccTabl | [[1], [0, 1], [-2, -3, 1], [8, 9, -8, 1], [-36, -37, 59, -15, 1], [224, 225, -504, 186, -24, 1], [-1880, -1881, 5179, -2400, 440, -35, 1], [19872, 19873, -63160, 34147, -7832, 883, -48, 1], [-251888, -251889, 894767, -541765, 145467, -20587, 1589, -63, 1], [3712256, 3712257, -14452368, 9558420, -2889392, 481318, -46832, 2644, -80, 1]] |
| AccRevTabl | [[1], [-1, 0], [1, -3, -2], [-1, 16, 7, 8], [1, -95, -21, -37, -36], [-1, 728, 38, 248, 223, 224], [1, -7059, 520, -2320, -1845, -1881, -1880], [-1, 83032, -14275, 27704, 18989, 19920, 19871, 19872], [1, -1146655, 289877, -397355, -231301, -253477, -251825, -251889, -251888], [-1, 18164624, -5846164, 6601648, 3230938, 3759088, 3709612, 3712336, 3712255, 3712256]] |

StirlingSetB:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 0, -2, 8, -36, 224, -1880, 19872, -251888, 3712256] |
| EvenSum      | [1, 1, 2, 18, 76, 940, 8056, 125944, 1604240, 31143312] |
| OddSum       | [0, -1, -4, -10, -112, -716, -9936, -106072, -1856128, -27431056] |
| AltSum       | [1, 2, 6, 28, 188, 1656, 17992, 232016, 3460368, 58574368] |
| AccSum       | [1, 1, -4, 10, -28, 108, -576, 3736, -24368, 78224] |
| AccRevSum    | [1, -1, -4, 30, -188, 1460, -14464, 175112, -2494512, 40756592] |
| DiagSum      | [1, 1, 0, -3, -7, 2, 49, 79, -262, -1243] |

StirlingSetB:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 4, 153, 3552, 5868450, 6496374713400, 2674413767201758365, 8381602311980946048, 4858073254198633258246924716385500] |
| RowGcd     | [1, 1, 4, 1, 2, 1, 1, 1, 2, 1] |
| RowMax     | [1, 1, 4, 17, 96, 729, 7579, 97307, 1436532, 24010788] |
| CentralE   | [1, -4, 74, -2840, 166054] |
| CentralO   | [1, -9, 210, -8715, 528150] |
| ColMiddle  | [1, 1, -4, -9, 74, 210, -2840, -8715, 166054, 528150] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, -1, 1, -1, 1, -1, 1, -1, 1, -1] |
| TransSqrs  | [0, -1, 0, 50, -568, 6244, -78896, 1153368, -19187904, 357876720] |
| TransNat0  | [0, -1, -2, 22, -152, 1236, -12584, 155240, -2242624, 37044336] |
| TransNat1  | [1, -1, -4, 30, -188, 1460, -14464, 175112, -2494512, 40756592] |

StirlingSetB:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]|
| DiagRow1 | [1, -4, 17, -96, 729, -7060, 83033, -1146656, 18164625, -324488068]|
| DiagRow2 | [1, -9, 74, -690, 7579, -97307, 1436532, -24010788, 448512021, -9263024749]|
| DiagRow3 | [1, -16, 210, -2840, 41979, -687232, 12447812, -248149040, 5410685621, -128249515152]|
| DiagRow4 | [1, -25, 475, -8715, 166054, -3370710, 73502330, -1724283770, 43452161071, -1173170731447]|
| DiagRow5 | [1, -36, 931, -22176, 528150, -13006392, 336073562, -9167835072, 264582272383, -8078528373916]|
| DiagRow6 | [1, -49, 1652, -49476, 1438458, -42224490, 1275590756, -40044216212, 1312610750451, -45023002083059]|
| DiagRow7 | [1, -64, 2724, -100080, 3485658, -120192864, 4196756564, -150231628976, 5551818806963, -212622436229632]|
| DiagRow8 | [1, -81, 4245, -187605, 7707183, -308369919, 12322357619, -498945642195, 20649462986438, -878088454231846]|
| DiagRow9 | [1, -100, 6325, -330880, 15827383, -727106380, 32965275915, -1499056004160, 69063422294438, -3244340330395736]|

StirlingSetB:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [-1, -4, -9, -16, -25, -36, -49, -64, -81, -100] |
| DiagCol2 | [1, 17, 74, 210, 475, 931, 1652, 2724, 4245, 6325] |
| DiagCol3 | [-1, -96, -690, -2840, -8715, -22176, -49476, -100080, -187605, -330880] |
| DiagCol4 | [1, 729, 7579, 41979, 166054, 528150, 1438458, 3485658, 7707183, 15827383] |
| DiagCol5 | [-1, -7060, -97307, -687232, -3370710, -13006392, -42224490, -120192864, -308369919, -727106380] |
| DiagCol6 | [1, 83033, 1436532, 12447812, 73502330, 336073562, 1275590756, 4196756564, 12322357619, 32965275915] |
| DiagCol7 | [-1, -1146656, -24010788, -248149040, -1724283770, -9167835072, -40044216212, -150231628976, -498945642195, -1499056004160] |
| DiagCol8 | [1, 18164625, 448512021, 5410685621, 43452161071, 264582272383, 1312610750451, 5551818806963, 20649462986438, 69063422294438] |
| DiagCol9 | [-1, -324488068, -9263024749, -128249515152, -1173170731447, -8078528373916, -45023002083059, -212622436229632, -878088454231846, -3244340330395736] |

StirlingSetB:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 0, -1, -2, -3, -4, -5, -6, -7, -8] |
| PolyRow2 | [1, -2, -3, -2, 1, 6, 13, 22, 33, 46] |
| PolyRow3 | [1, 8, 43, 100, 173, 256, 343, 428, 505, 568] |
| PolyRow4 | [1, -36, -487, -1892, -4767, -9604, -16871, -27012, -40447, -57572] |
| PolyRow5 | [1, 224, 6903, 41992, 144701, 371376, 795379, 1506968, 2613177, 4237696] |
| PolyRow6 | [1, -1880, -125483, -1173464, -5459423, -17653304, -45626075, -101293688, -201460319, -368660888] |
| PolyRow7 | [1, 19872, 2805731, 40056496, 250647981, 1018398656, 3169604047, 8230334736, 18743492921, 38645622496] |
| PolyRow8 | [1, -251888, -74339151, -1614629360, -13565320127, -69182844144, -259099218383, -786467342576, -2049967211775, -4760451967472] |
| PolyRow9 | [1, 3712256, 2273625199, 74963332576, 844710565373, 5403999445696, 24343329125611, 86350563990944, 257552236838521, 673503972300928] |

StirlingSetB:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 0, -2, 8, -36, 224, -1880, 19872, -251888, 3712256] |
| PolyCol2 | [1, -1, -3, 43, -487, 6903, -125483, 2805731, -74339151, 2273625199] |
| PolyCol3 | [1, -2, -2, 100, -1892, 41992, -1173464, 40056496, -1614629360, 74963332576] |
| PolyCol4 | [1, -3, 1, 173, -4767, 144701, -5459423, 250647981, -13565320127, 844710565373] |
| PolyCol5 | [1, -4, 6, 256, -9604, 371376, -17653304, 1018398656, -69182844144, 5403999445696] |
| PolyCol6 | [1, -5, 13, 343, -16871, 795379, -45626075, 3169604047, -259099218383, 24343329125611] |
| PolyCol7 | [1, -6, 22, 428, -27012, 1506968, -101293688, 8230334736, -786467342576, 86350563990944] |
| PolyCol8 | [1, -7, 33, 505, -40447, 2613177, -201460319, 18743492921, -2049967211775, 257552236838521] |
| PolyCol9 | [1, -8, 46, 568, -57572, 4237696, -368660888, 38645622496, -4760451967472, 673503972300928] |
