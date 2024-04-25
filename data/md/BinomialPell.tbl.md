# BinomialPell
['A367211']

BinomialPell Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [2, 2] |
| Row2 | [5, 6, 3] |
| Row3 | [12, 20, 12, 4] |
| Row4 | [29, 60, 50, 20, 5] |
| Row5 | [70, 174, 180, 100, 30, 6] |
| Row6 | [169, 490, 609, 420, 175, 42, 7] |
| Row7 | [408, 1352, 1960, 1624, 840, 280, 56, 8] |
| Row8 | [985, 3672, 6084, 5880, 3654, 1512, 420, 72, 9] |
| Row9 | [2378, 9850, 18360, 20280, 14700, 7308, 2520, 600, 90, 10] |

BinomialPell Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [2, 2], [5, 6, 3], [12, 20, 12, 4], [29, 60, 50, 20, 5], [70, 174, 180, 100, 30, 6], [169, 490, 609, 420, 175, 42, 7], [408, 1352, 1960, 1624, 840, 280, 56, 8], [985, 3672, 6084, 5880, 3654, 1512, 420, 72, 9], [2378, 9850, 18360, 20280, 14700, 7308, 2520, 600, 90, 10]] |
| RevTabl    | [[1], [2, 2], [3, 6, 5], [4, 12, 20, 12], [5, 20, 50, 60, 29], [6, 30, 100, 180, 174, 70], [7, 42, 175, 420, 609, 490, 169], [8, 56, 280, 840, 1624, 1960, 1352, 408], [9, 72, 420, 1512, 3654, 5880, 6084, 3672, 985], [10, 90, 600, 2520, 7308, 14700, 20280, 18360, 9850, 2378]] |
| AntiDiag   | [[1], [2], [5, 2], [12, 6], [29, 20, 3], [70, 60, 12], [169, 174, 50, 4], [408, 490, 180, 20], [985, 1352, 609, 100, 5], [2378, 3672, 1960, 420, 30]] |
| AccTabl    | [[1], [2, 4], [5, 11, 14], [12, 32, 44, 48], [29, 89, 139, 159, 164], [70, 244, 424, 524, 554, 560], [169, 659, 1268, 1688, 1863, 1905, 1912], [408, 1760, 3720, 5344, 6184, 6464, 6520, 6528], [985, 4657, 10741, 16621, 20275, 21787, 22207, 22279, 22288], [2378, 12228, 30588, 50868, 65568, 72876, 75396, 75996, 76086, 76096]] |
| RevAccTabl | [[1], [4, 2], [14, 11, 5], [48, 44, 32, 12], [164, 159, 139, 89, 29], [560, 554, 524, 424, 244, 70], [1912, 1905, 1863, 1688, 1268, 659, 169], [6528, 6520, 6464, 6184, 5344, 3720, 1760, 408], [22288, 22279, 22207, 21787, 20275, 16621, 10741, 4657, 985], [76096, 76086, 75996, 75396, 72876, 65568, 50868, 30588, 12228, 2378]] |
| AccRevTabl | [[1], [2, 4], [3, 9, 14], [4, 16, 36, 48], [5, 25, 75, 135, 164], [6, 36, 136, 316, 490, 560], [7, 49, 224, 644, 1253, 1743, 1912], [8, 64, 344, 1184, 2808, 4768, 6120, 6528], [9, 81, 501, 2013, 5667, 11547, 17631, 21303, 22288], [10, 100, 700, 3220, 10528, 25228, 45508, 63868, 73718, 76096]] |
| DiffxTabl  | [[1], [2, 4], [5, 12, 9], [12, 40, 36, 16], [29, 120, 150, 80, 25], [70, 348, 540, 400, 150, 36], [169, 980, 1827, 1680, 875, 252, 49], [408, 2704, 5880, 6496, 4200, 1680, 392, 64], [985, 7344, 18252, 23520, 18270, 9072, 2940, 576, 81], [2378, 19700, 55080, 81120, 73500, 43848, 17640, 4800, 810, 100]] |

BinomialPell Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| EvenSum      | [1, 2, 8, 24, 84, 280, 960, 3264, 11152, 38048] |
| OddSum       | [0, 2, 6, 24, 80, 280, 952, 3264, 11136, 38048] |
| AltSum       | [1, 0, 2, 0, 4, 0, 8, 0, 16, 0] |
| AbsSum       | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| AccSum       | [1, 6, 30, 136, 580, 2376, 9464, 36928, 141840, 538080] |
| AccRevSum    | [1, 6, 26, 104, 404, 1544, 5832, 21824, 81040, 298976] |
| DiagSum      | [1, 2, 7, 18, 52, 142, 397, 1098, 3051, 8460] |

BinomialPell Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 30, 60, 8700, 182700, 72044700, 489903960, 868599721080, 178062942821400] |
| RowGcd     | [1, 2, 1, 4, 1, 2, 1, 8, 1, 2] |
| RowMax     | [1, 2, 6, 20, 60, 180, 609, 1960, 6084, 20280] |
| CentralE   | [1, 6, 50, 420, 3654] |
| CentralO   | [2, 20, 180, 1624, 14700] |
| ColMiddle  | [1, 2, 6, 20, 50, 180, 420, 1624, 3654, 14700] |
| ColLeft    | [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378] |
| ColRight   | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| BinConv    | [1, 4, 20, 112, 654, 3896, 23528, 143552, 882790, 5462616] |
| InvBinConv | [1, 0, -4, 16, 14, -144, 344, 832, -5018, 6560] |
| TransSqrs  | [0, 2, 18, 104, 520, 2424, 10808, 46656, 196416, 810400] |
| TransNat0  | [0, 2, 12, 56, 240, 984, 3920, 15296, 58752, 222880] |
| TransNat1  | [1, 6, 26, 104, 404, 1544, 5832, 21824, 81040, 298976] |
| PosHalf    | [1, 6, 35, 204, 1189, 6930, 40391, 235416, 1372105, 7997214] |
| NegHalf    | [1, -2, 11, -36, 149, -550, 2143, -8136, 31273, -119498] |

BinomialPell Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]|
| DiagRow1 | [2, 6, 12, 20, 30, 42, 56, 72, 90, 110]|
| DiagRow2 | [5, 20, 50, 100, 175, 280, 420, 600, 825, 1100]|
| DiagRow3 | [12, 60, 180, 420, 840, 1512, 2520, 3960, 5940, 8580]|
| DiagRow4 | [29, 174, 609, 1624, 3654, 7308, 13398, 22968, 37323, 58058]|
| DiagRow5 | [70, 490, 1960, 5880, 14700, 32340, 64680, 120120, 210210, 350350]|
| DiagRow6 | [169, 1352, 6084, 20280, 55770, 133848, 290004, 580008, 1087515, 1933360]|
| DiagRow7 | [408, 3672, 18360, 67320, 201960, 525096, 1225224, 2625480, 5250960, 9918480]|
| DiagRow8 | [985, 9850, 54175, 216700, 704275, 1971970, 4929925, 11268400, 23945350, 47890700]|
| DiagRow9 | [2378, 26158, 156948, 680108, 2380378, 7141134, 19043024, 46247344, 104056524, 219674884]|

BinomialPell Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378] |
| DiagCol1 | [2, 6, 20, 60, 174, 490, 1352, 3672, 9850, 26158] |
| DiagCol2 | [3, 12, 50, 180, 609, 1960, 6084, 18360, 54175, 156948] |
| DiagCol3 | [4, 20, 100, 420, 1624, 5880, 20280, 67320, 216700, 680108] |
| DiagCol4 | [5, 30, 175, 840, 3654, 14700, 55770, 201960, 704275, 2380378] |
| DiagCol5 | [6, 42, 280, 1512, 7308, 32340, 133848, 525096, 1971970, 7141134] |
| DiagCol6 | [7, 56, 420, 2520, 13398, 64680, 290004, 1225224, 4929925, 19043024] |
| DiagCol7 | [8, 72, 600, 3960, 22968, 120120, 580008, 2625480, 11268400, 46247344] |
| DiagCol8 | [9, 90, 825, 5940, 37323, 210210, 1087515, 5250960, 23945350, 104056524] |
| DiagCol9 | [10, 110, 1100, 8580, 58058, 350350, 1933360, 9918480, 47890700, 219674884] |

BinomialPell Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] |
| PolyRow2 | [5, 14, 29, 50, 77, 110, 149, 194, 245, 302] |
| PolyRow3 | [12, 48, 132, 288, 540, 912, 1428, 2112, 2988, 4080] |
| PolyRow4 | [29, 164, 589, 1604, 3629, 7204, 12989, 21764, 34429, 52004] |
| PolyRow5 | [70, 560, 2610, 8800, 23870, 55440, 114730, 217280, 383670, 640240] |
| PolyRow6 | [169, 1912, 11537, 47944, 155233, 420344, 995737, 2127112, 4186169, 7708408] |
| PolyRow7 | [408, 6528, 50952, 260352, 1003320, 3159168, 8548008, 20562432, 45041112, 91424640] |
| PolyRow8 | [985, 22288, 224953, 1411600, 6462841, 23618320, 72872473, 197117968, 480032665, 1073068816] |
| PolyRow9 | [2378, 76096, 993054, 7647872, 41552050, 176008128, 618458246, 1879016704, 5082340122, 12501761600] |

BinomialPell Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378] |
| PolyCol1 | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| PolyCol2 | [1, 6, 29, 132, 589, 2610, 11537, 50952, 224953, 993054] |
| PolyCol3 | [1, 8, 50, 288, 1604, 8800, 47944, 260352, 1411600, 7647872] |
| PolyCol4 | [1, 10, 77, 540, 3629, 23870, 155233, 1003320, 6462841, 41552050] |
| PolyCol5 | [1, 12, 110, 912, 7204, 55440, 420344, 3159168, 23618320, 176008128] |
| PolyCol6 | [1, 14, 149, 1428, 12989, 114730, 995737, 8548008, 72872473, 618458246] |
| PolyCol7 | [1, 16, 194, 2112, 21764, 217280, 2127112, 20562432, 197117968, 1879016704] |
| PolyCol8 | [1, 18, 245, 2988, 34429, 383670, 4186169, 45041112, 480032665, 5082340122] |
| PolyCol9 | [1, 20, 302, 4080, 52004, 640240, 7708408, 91424640, 1073068816, 12501761600] |

# BinomialPell:Rev
[]

BinomialPell:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [2, 2] |
| Row2 | [3, 6, 5] |
| Row3 | [4, 12, 20, 12] |
| Row4 | [5, 20, 50, 60, 29] |
| Row5 | [6, 30, 100, 180, 174, 70] |
| Row6 | [7, 42, 175, 420, 609, 490, 169] |
| Row7 | [8, 56, 280, 840, 1624, 1960, 1352, 408] |
| Row8 | [9, 72, 420, 1512, 3654, 5880, 6084, 3672, 985] |
| Row9 | [10, 90, 600, 2520, 7308, 14700, 20280, 18360, 9850, 2378] |

BinomialPell:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [2, 2], [3, 6, 5], [4, 12, 20, 12], [5, 20, 50, 60, 29], [6, 30, 100, 180, 174, 70], [7, 42, 175, 420, 609, 490, 169], [8, 56, 280, 840, 1624, 1960, 1352, 408], [9, 72, 420, 1512, 3654, 5880, 6084, 3672, 985], [10, 90, 600, 2520, 7308, 14700, 20280, 18360, 9850, 2378]] |
| RevTabl    | [[1], [2, 2], [5, 6, 3], [12, 20, 12, 4], [29, 60, 50, 20, 5], [70, 174, 180, 100, 30, 6], [169, 490, 609, 420, 175, 42, 7], [408, 1352, 1960, 1624, 840, 280, 56, 8], [985, 3672, 6084, 5880, 3654, 1512, 420, 72, 9], [2378, 9850, 18360, 20280, 14700, 7308, 2520, 600, 90, 10]] |
| AntiDiag   | [[1], [2], [3, 2], [4, 6], [5, 12, 5], [6, 20, 20], [7, 30, 50, 12], [8, 42, 100, 60], [9, 56, 175, 180, 29], [10, 72, 280, 420, 174]] |
| AccTabl    | [[1], [2, 4], [3, 9, 14], [4, 16, 36, 48], [5, 25, 75, 135, 164], [6, 36, 136, 316, 490, 560], [7, 49, 224, 644, 1253, 1743, 1912], [8, 64, 344, 1184, 2808, 4768, 6120, 6528], [9, 81, 501, 2013, 5667, 11547, 17631, 21303, 22288], [10, 100, 700, 3220, 10528, 25228, 45508, 63868, 73718, 76096]] |
| RevAccTabl | [[1], [4, 2], [14, 9, 3], [48, 36, 16, 4], [164, 135, 75, 25, 5], [560, 490, 316, 136, 36, 6], [1912, 1743, 1253, 644, 224, 49, 7], [6528, 6120, 4768, 2808, 1184, 344, 64, 8], [22288, 21303, 17631, 11547, 5667, 2013, 501, 81, 9], [76096, 73718, 63868, 45508, 25228, 10528, 3220, 700, 100, 10]] |
| AccRevTabl | [[1], [2, 4], [5, 11, 14], [12, 32, 44, 48], [29, 89, 139, 159, 164], [70, 244, 424, 524, 554, 560], [169, 659, 1268, 1688, 1863, 1905, 1912], [408, 1760, 3720, 5344, 6184, 6464, 6520, 6528], [985, 4657, 10741, 16621, 20275, 21787, 22207, 22279, 22288], [2378, 12228, 30588, 50868, 65568, 72876, 75396, 75996, 76086, 76096]] |
| DiffxTabl  | [[1], [2, 4], [3, 12, 15], [4, 24, 60, 48], [5, 40, 150, 240, 145], [6, 60, 300, 720, 870, 420], [7, 84, 525, 1680, 3045, 2940, 1183], [8, 112, 840, 3360, 8120, 11760, 9464, 3264], [9, 144, 1260, 6048, 18270, 35280, 42588, 29376, 8865], [10, 180, 1800, 10080, 36540, 88200, 141960, 146880, 88650, 23780]] |

BinomialPell:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| EvenSum      | [1, 2, 8, 24, 84, 280, 960, 3264, 11152, 38048] |
| OddSum       | [0, 2, 6, 24, 80, 280, 952, 3264, 11136, 38048] |
| AltSum       | [1, 0, 2, 0, 4, 0, 8, 0, 16, 0] |
| AbsSum       | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| AccSum       | [1, 6, 26, 104, 404, 1544, 5832, 21824, 81040, 298976] |
| AccRevSum    | [1, 6, 30, 136, 580, 2376, 9464, 36928, 141840, 538080] |
| DiagSum      | [1, 2, 5, 10, 22, 46, 99, 210, 449, 956] |

BinomialPell:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 2, 30, 60, 8700, 182700, 72044700, 489903960, 868599721080, 178062942821400] |
| RowGcd     | [1, 2, 1, 4, 1, 2, 1, 8, 1, 2] |
| RowMax     | [1, 2, 6, 20, 60, 180, 609, 1960, 6084, 20280] |
| CentralE   | [1, 6, 50, 420, 3654] |
| CentralO   | [2, 12, 100, 840, 7308] |
| ColMiddle  | [1, 2, 6, 12, 50, 100, 420, 840, 3654, 7308] |
| ColLeft    | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| ColRight   | [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378] |
| BinConv    | [1, 4, 20, 112, 654, 3896, 23528, 143552, 882790, 5462616] |
| InvBinConv | [1, 0, -4, -16, 14, 144, 344, -832, -5018, -6560] |
| TransSqrs  | [0, 2, 26, 200, 1224, 6584, 32600, 152384, 682816, 2962336] |
| TransNat0  | [0, 2, 16, 88, 416, 1816, 7552, 30400, 119552, 461984] |
| TransNat1  | [1, 6, 30, 136, 580, 2376, 9464, 36928, 141840, 538080] |
| PosHalf    | [1, 6, 29, 132, 589, 2610, 11537, 50952, 224953, 993054] |
| NegHalf    | [1, -2, 5, -12, 29, -70, 169, -408, 985, -2378] |

BinomialPell:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 2, 5, 12, 29, 70, 169, 408, 985, 2378]|
| DiagRow1 | [2, 6, 20, 60, 174, 490, 1352, 3672, 9850, 26158]|
| DiagRow2 | [3, 12, 50, 180, 609, 1960, 6084, 18360, 54175, 156948]|
| DiagRow3 | [4, 20, 100, 420, 1624, 5880, 20280, 67320, 216700, 680108]|
| DiagRow4 | [5, 30, 175, 840, 3654, 14700, 55770, 201960, 704275, 2380378]|
| DiagRow5 | [6, 42, 280, 1512, 7308, 32340, 133848, 525096, 1971970, 7141134]|
| DiagRow6 | [7, 56, 420, 2520, 13398, 64680, 290004, 1225224, 4929925, 19043024]|
| DiagRow7 | [8, 72, 600, 3960, 22968, 120120, 580008, 2625480, 11268400, 46247344]|
| DiagRow8 | [9, 90, 825, 5940, 37323, 210210, 1087515, 5250960, 23945350, 104056524]|
| DiagRow9 | [10, 110, 1100, 8580, 58058, 350350, 1933360, 9918480, 47890700, 219674884]|

BinomialPell:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| DiagCol1 | [2, 6, 12, 20, 30, 42, 56, 72, 90, 110] |
| DiagCol2 | [5, 20, 50, 100, 175, 280, 420, 600, 825, 1100] |
| DiagCol3 | [12, 60, 180, 420, 840, 1512, 2520, 3960, 5940, 8580] |
| DiagCol4 | [29, 174, 609, 1624, 3654, 7308, 13398, 22968, 37323, 58058] |
| DiagCol5 | [70, 490, 1960, 5880, 14700, 32340, 64680, 120120, 210210, 350350] |
| DiagCol6 | [169, 1352, 6084, 20280, 55770, 133848, 290004, 580008, 1087515, 1933360] |
| DiagCol7 | [408, 3672, 18360, 67320, 201960, 525096, 1225224, 2625480, 5250960, 9918480] |
| DiagCol8 | [985, 9850, 54175, 216700, 704275, 1971970, 4929925, 11268400, 23945350, 47890700] |
| DiagCol9 | [2378, 26158, 156948, 680108, 2380378, 7141134, 19043024, 46247344, 104056524, 219674884] |

BinomialPell:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] |
| PolyRow2 | [3, 14, 35, 66, 107, 158, 219, 290, 371, 462] |
| PolyRow3 | [4, 48, 204, 544, 1140, 2064, 3388, 5184, 7524, 10480] |
| PolyRow4 | [5, 164, 1189, 4484, 12149, 26980, 52469, 92804, 152869, 238244] |
| PolyRow5 | [6, 560, 6930, 36960, 129470, 352656, 812490, 1661120, 3105270, 5414640] |
| PolyRow6 | [7, 1912, 40391, 304648, 1379743, 4609592, 12581647, 29733256, 63079703, 123063928] |
| PolyRow7 | [8, 6528, 235416, 2511104, 14703720, 60252288, 194830328, 532210176, 1281382344, 2796986240] |
| PolyRow8 | [9, 22288, 1372105, 20698128, 156695401, 787561744, 3017002473, 9526293520, 26029628233, 63569688336] |
| PolyRow9 | [10, 76096, 7997214, 170607232, 1669880050, 10294272960, 46719132166, 170515842304, 528758278362, 1444806913600] |

BinomialPell:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyCol1 | [1, 4, 14, 48, 164, 560, 1912, 6528, 22288, 76096] |
| PolyCol2 | [1, 6, 35, 204, 1189, 6930, 40391, 235416, 1372105, 7997214] |
| PolyCol3 | [1, 8, 66, 544, 4484, 36960, 304648, 2511104, 20698128, 170607232] |
| PolyCol4 | [1, 10, 107, 1140, 12149, 129470, 1379743, 14703720, 156695401, 1669880050] |
| PolyCol5 | [1, 12, 158, 2064, 26980, 352656, 4609592, 60252288, 787561744, 10294272960] |
| PolyCol6 | [1, 14, 219, 3388, 52469, 812490, 12581647, 194830328, 3017002473, 46719132166] |
| PolyCol7 | [1, 16, 290, 5184, 92804, 1661120, 29733256, 532210176, 9526293520, 170515842304] |
| PolyCol8 | [1, 18, 371, 7524, 152869, 3105270, 63079703, 1281382344, 26029628233, 528758278362] |
| PolyCol9 | [1, 20, 462, 10480, 238244, 5414640, 123063928, 2796986240, 63569688336, 1444806913600] |
