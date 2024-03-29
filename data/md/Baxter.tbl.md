# Baxter
['A359363', 'A056939']

Baxter Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 1] |
| Row3 | [0, 1, 4, 1] |
| Row4 | [0, 1, 10, 10, 1] |
| Row5 | [0, 1, 20, 50, 20, 1] |
| Row6 | [0, 1, 35, 175, 175, 35, 1] |
| Row7 | [0, 1, 56, 490, 980, 490, 56, 1] |
| Row8 | [0, 1, 84, 1176, 4116, 4116, 1176, 84, 1] |
| Row9 | [0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1] |

Baxter Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 1], [0, 1, 4, 1], [0, 1, 10, 10, 1], [0, 1, 20, 50, 20, 1], [0, 1, 35, 175, 175, 35, 1], [0, 1, 56, 490, 980, 490, 56, 1], [0, 1, 84, 1176, 4116, 4116, 1176, 84, 1], [0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1]] |
| RevTabl    | [[1], [1, 0], [1, 1, 0], [1, 4, 1, 0], [1, 10, 10, 1, 0], [1, 20, 50, 20, 1, 0], [1, 35, 175, 175, 35, 1, 0], [1, 56, 490, 980, 490, 56, 1, 0], [1, 84, 1176, 4116, 4116, 1176, 84, 1, 0], [1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 1, 1], [0, 1, 4], [0, 1, 10, 1], [0, 1, 20, 10], [0, 1, 35, 50, 1], [0, 1, 56, 175, 20]] |
| AccTabl    | [[1], [0, 1], [0, 1, 2], [0, 1, 5, 6], [0, 1, 11, 21, 22], [0, 1, 21, 71, 91, 92], [0, 1, 36, 211, 386, 421, 422], [0, 1, 57, 547, 1527, 2017, 2073, 2074], [0, 1, 85, 1261, 5377, 9493, 10669, 10753, 10754], [0, 1, 121, 2641, 16753, 41449, 55561, 58081, 58201, 58202]] |
| RevAccTabl | [[1], [1, 0], [2, 1, 0], [6, 5, 1, 0], [22, 21, 11, 1, 0], [92, 91, 71, 21, 1, 0], [422, 421, 386, 211, 36, 1, 0], [2074, 2073, 2017, 1527, 547, 57, 1, 0], [10754, 10753, 10669, 9493, 5377, 1261, 85, 1, 0], [58202, 58201, 58081, 55561, 41449, 16753, 2641, 121, 1, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 2, 2], [1, 5, 6, 6], [1, 11, 21, 22, 22], [1, 21, 71, 91, 92, 92], [1, 36, 211, 386, 421, 422, 422], [1, 57, 547, 1527, 2017, 2073, 2074, 2074], [1, 85, 1261, 5377, 9493, 10669, 10753, 10754, 10754], [1, 121, 2641, 16753, 41449, 55561, 58081, 58201, 58202, 58202]] |
| DiffxTabl  | [[1], [0, 2], [0, 2, 3], [0, 2, 12, 4], [0, 2, 30, 40, 5], [0, 2, 60, 200, 100, 6], [0, 2, 105, 700, 875, 210, 7], [0, 2, 168, 1960, 4900, 2940, 392, 8], [0, 2, 252, 4704, 20580, 24696, 8232, 672, 9], [0, 2, 360, 10080, 70560, 148176, 98784, 20160, 1080, 10]] |

Baxter Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| EvenSum      | [1, 0, 1, 4, 11, 40, 211, 1092, 5377, 28464] |
| OddSum       | [0, 1, 1, 2, 11, 52, 211, 982, 5377, 29738] |
| AltSum       | [1, -1, 0, 2, 0, -12, 0, 110, 0, -1274] |
| AbsSum       | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| AccSum       | [1, 1, 3, 12, 55, 276, 1477, 8296, 48393, 291010] |
| AccRevSum    | [1, 2, 5, 18, 77, 368, 1899, 10370, 59147, 349212] |
| DiagSum      | [1, 0, 1, 1, 2, 5, 12, 31, 87, 252] |

Baxter Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 4, 10, 100, 175, 1960, 8232, 493920] |
| RowGcd     | [1, 1, 1, 4, 10, 10, 35, 14, 84, 24] |
| RowMax     | [1, 1, 1, 4, 10, 50, 175, 980, 4116, 24696] |
| CentralE   | [1, 1, 10, 175, 4116] |
| CentralO   | [0, 1, 20, 490, 14112] |
| ColMiddle  | [1, 0, 1, 1, 10, 20, 175, 490, 4116, 14112] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| BinConv    | [1, 1, 3, 16, 105, 806, 6867, 63316, 620433, 6383026] |
| InvBinConv | [1, 1, -1, -8, 17, 206, -565, -8420, 26369, 445186] |
| TransSqrs  | [0, 1, 5, 26, 147, 876, 5427, 34630, 226193, 1505626] |
| TransNat0  | [0, 1, 3, 12, 55, 276, 1477, 8296, 48393, 291010] |
| TransNat1  | [1, 2, 5, 18, 77, 368, 1899, 10370, 59147, 349212] |
| PosHalf    | [1, 1, 3, 13, 69, 417, 2763, 19609, 146793, 1146833] |
| NegHalf    | [1, 1, -1, -3, 13, 17, -241, 121, 5081, -13327] |

Baxter Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165]|
| DiagRow2 | [0, 1, 10, 50, 175, 490, 1176, 2520, 4950, 9075]|
| DiagRow3 | [0, 1, 20, 175, 980, 4116, 14112, 41580, 108900, 259545]|
| DiagRow4 | [0, 1, 35, 490, 4116, 24696, 116424, 457380, 1557270, 4723719]|
| DiagRow5 | [0, 1, 56, 1176, 14112, 116424, 731808, 3737448, 16195608, 61408347]|
| DiagRow6 | [0, 1, 84, 2520, 41580, 457380, 3737448, 24293412, 131589315, 614083470]|
| DiagRow7 | [0, 1, 120, 4950, 108900, 1557270, 16195608, 131589315, 877262100, 4971151900]|
| DiagRow8 | [0, 1, 165, 9075, 259545, 4723719, 61408347, 614083470, 4971151900, 33803832920]|
| DiagRow9 | [0, 1, 220, 15730, 572572, 13026013, 208416208, 2530768240, 24584605760, 198520691512]|

Baxter Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [1, 4, 10, 20, 35, 56, 84, 120, 165, 220] |
| DiagCol3 | [1, 10, 50, 175, 490, 1176, 2520, 4950, 9075, 15730] |
| DiagCol4 | [1, 20, 175, 980, 4116, 14112, 41580, 108900, 259545, 572572] |
| DiagCol5 | [1, 35, 490, 4116, 24696, 116424, 457380, 1557270, 4723719, 13026013] |
| DiagCol6 | [1, 56, 1176, 14112, 116424, 731808, 3737448, 16195608, 61408347, 208416208] |
| DiagCol7 | [1, 84, 2520, 41580, 457380, 3737448, 24293412, 131589315, 614083470, 2530768240] |
| DiagCol8 | [1, 120, 4950, 108900, 1557270, 16195608, 131589315, 877262100, 4971151900, 24584605760] |
| DiagCol9 | [1, 165, 9075, 259545, 4723719, 61408347, 614083470, 4971151900, 33803832920, 198520691512] |

Baxter Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] |
| PolyRow3 | [0, 6, 26, 66, 132, 230, 366, 546, 776, 1062] |
| PolyRow4 | [0, 22, 138, 444, 1060, 2130, 3822, 6328, 9864, 14670] |
| PolyRow5 | [0, 92, 834, 3396, 9668, 22380, 45222, 82964, 141576, 228348] |
| PolyRow6 | [0, 422, 5526, 28452, 96500, 257130, 584682, 1187816, 2217672, 3876750] |
| PolyRow7 | [0, 2074, 39218, 255198, 1030660, 3159530, 8080854, 18171118, 37102088, 70269210] |
| PolyRow8 | [0, 10754, 293586, 2413668, 11603780, 40912230, 117659094, 292765256, 653559048, 1340705610] |
| PolyRow9 | [0, 58202, 2293666, 23819214, 136281476, 552516130, 1786353702, 4917539606, 12000022024, 26658514026] |

Baxter Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| PolyCol2 | [1, 2, 6, 26, 138, 834, 5526, 39218, 293586, 2293666] |
| PolyCol3 | [1, 3, 12, 66, 444, 3396, 28452, 255198, 2413668, 23819214] |
| PolyCol4 | [1, 4, 20, 132, 1060, 9668, 96500, 1030660, 11603780, 136281476] |
| PolyCol5 | [1, 5, 30, 230, 2130, 22380, 257130, 3159530, 40912230, 552516130] |
| PolyCol6 | [1, 6, 42, 366, 3822, 45222, 584682, 8080854, 117659094, 1786353702] |
| PolyCol7 | [1, 7, 56, 546, 6328, 82964, 1187816, 18171118, 292765256, 4917539606] |
| PolyCol8 | [1, 8, 72, 776, 9864, 141576, 2217672, 37102088, 653559048, 12000022024] |
| PolyCol9 | [1, 9, 90, 1062, 14670, 228348, 3876750, 70269210, 1340705610, 26658514026] |

# Baxter:Rev
[]

Baxter:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 1, 0] |
| Row3 | [1, 4, 1, 0] |
| Row4 | [1, 10, 10, 1, 0] |
| Row5 | [1, 20, 50, 20, 1, 0] |
| Row6 | [1, 35, 175, 175, 35, 1, 0] |
| Row7 | [1, 56, 490, 980, 490, 56, 1, 0] |
| Row8 | [1, 84, 1176, 4116, 4116, 1176, 84, 1, 0] |
| Row9 | [1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1, 0] |

Baxter:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 1, 0], [1, 4, 1, 0], [1, 10, 10, 1, 0], [1, 20, 50, 20, 1, 0], [1, 35, 175, 175, 35, 1, 0], [1, 56, 490, 980, 490, 56, 1, 0], [1, 84, 1176, 4116, 4116, 1176, 84, 1, 0], [1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 1], [0, 1, 4, 1], [0, 1, 10, 10, 1], [0, 1, 20, 50, 20, 1], [0, 1, 35, 175, 175, 35, 1], [0, 1, 56, 490, 980, 490, 56, 1], [0, 1, 84, 1176, 4116, 4116, 1176, 84, 1], [0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 1], [1, 4, 0], [1, 10, 1], [1, 20, 10, 0], [1, 35, 50, 1], [1, 56, 175, 20, 0], [1, 84, 490, 175, 1]] |
| AccTabl    | [[1], [1, 1], [1, 2, 2], [1, 5, 6, 6], [1, 11, 21, 22, 22], [1, 21, 71, 91, 92, 92], [1, 36, 211, 386, 421, 422, 422], [1, 57, 547, 1527, 2017, 2073, 2074, 2074], [1, 85, 1261, 5377, 9493, 10669, 10753, 10754, 10754], [1, 121, 2641, 16753, 41449, 55561, 58081, 58201, 58202, 58202]] |
| RevAccTabl | [[1], [1, 1], [2, 2, 1], [6, 6, 5, 1], [22, 22, 21, 11, 1], [92, 92, 91, 71, 21, 1], [422, 422, 421, 386, 211, 36, 1], [2074, 2074, 2073, 2017, 1527, 547, 57, 1], [10754, 10754, 10753, 10669, 9493, 5377, 1261, 85, 1], [58202, 58202, 58201, 58081, 55561, 41449, 16753, 2641, 121, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 2], [0, 1, 5, 6], [0, 1, 11, 21, 22], [0, 1, 21, 71, 91, 92], [0, 1, 36, 211, 386, 421, 422], [0, 1, 57, 547, 1527, 2017, 2073, 2074], [0, 1, 85, 1261, 5377, 9493, 10669, 10753, 10754], [0, 1, 121, 2641, 16753, 41449, 55561, 58081, 58201, 58202]] |
| DiffxTabl  | [[1], [1, 0], [1, 2, 0], [1, 8, 3, 0], [1, 20, 30, 4, 0], [1, 40, 150, 80, 5, 0], [1, 70, 525, 700, 175, 6, 0], [1, 112, 1470, 3920, 2450, 336, 7, 0], [1, 168, 3528, 16464, 20580, 7056, 588, 8, 0], [1, 240, 7560, 56448, 123480, 84672, 17640, 960, 9, 0]] |

Baxter:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| EvenSum      | [1, 1, 1, 2, 11, 52, 211, 982, 5377, 29738] |
| OddSum       | [0, 0, 1, 4, 11, 40, 211, 1092, 5377, 28464] |
| AltSum       | [1, 1, 0, -2, 0, 12, 0, -110, 0, 1274] |
| AbsSum       | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| AccSum       | [1, 2, 5, 18, 77, 368, 1899, 10370, 59147, 349212] |
| AccRevSum    | [1, 1, 3, 12, 55, 276, 1477, 8296, 48393, 291010] |
| DiagSum      | [1, 1, 1, 2, 5, 12, 31, 87, 252, 751] |

Baxter:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 4, 10, 100, 175, 1960, 8232, 493920] |
| RowGcd     | [1, 1, 1, 4, 10, 10, 35, 14, 84, 24] |
| RowMax     | [1, 1, 1, 4, 10, 50, 175, 980, 4116, 24696] |
| CentralE   | [1, 1, 10, 175, 4116] |
| CentralO   | [1, 4, 50, 980, 24696] |
| ColMiddle  | [1, 1, 1, 4, 10, 50, 175, 980, 4116, 24696] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| BinConv    | [1, 1, 3, 16, 105, 806, 6867, 63316, 620433, 6383026] |
| InvBinConv | [1, -1, -1, 8, 17, -206, -565, 8420, 26369, -445186] |
| TransSqrs  | [0, 0, 1, 8, 59, 416, 2895, 20112, 140161, 981808] |
| TransNat0  | [0, 0, 1, 6, 33, 184, 1055, 6222, 37639, 232808] |
| TransNat1  | [1, 1, 3, 12, 55, 276, 1477, 8296, 48393, 291010] |
| PosHalf    | [1, 2, 6, 26, 138, 834, 5526, 39218, 293586, 2293666] |
| NegHalf    | [1, -2, 2, 6, -26, -34, 482, -242, -10162, 26654] |

Baxter:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [1, 4, 10, 20, 35, 56, 84, 120, 165, 220]|
| DiagRow3 | [1, 10, 50, 175, 490, 1176, 2520, 4950, 9075, 15730]|
| DiagRow4 | [1, 20, 175, 980, 4116, 14112, 41580, 108900, 259545, 572572]|
| DiagRow5 | [1, 35, 490, 4116, 24696, 116424, 457380, 1557270, 4723719, 13026013]|
| DiagRow6 | [1, 56, 1176, 14112, 116424, 731808, 3737448, 16195608, 61408347, 208416208]|
| DiagRow7 | [1, 84, 2520, 41580, 457380, 3737448, 24293412, 131589315, 614083470, 2530768240]|
| DiagRow8 | [1, 120, 4950, 108900, 1557270, 16195608, 131589315, 877262100, 4971151900, 24584605760]|
| DiagRow9 | [1, 165, 9075, 259545, 4723719, 61408347, 614083470, 4971151900, 33803832920, 198520691512]|

Baxter:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 1, 4, 10, 20, 35, 56, 84, 120, 165] |
| DiagCol2 | [0, 1, 10, 50, 175, 490, 1176, 2520, 4950, 9075] |
| DiagCol3 | [0, 1, 20, 175, 980, 4116, 14112, 41580, 108900, 259545] |
| DiagCol4 | [0, 1, 35, 490, 4116, 24696, 116424, 457380, 1557270, 4723719] |
| DiagCol5 | [0, 1, 56, 1176, 14112, 116424, 731808, 3737448, 16195608, 61408347] |
| DiagCol6 | [0, 1, 84, 2520, 41580, 457380, 3737448, 24293412, 131589315, 614083470] |
| DiagCol7 | [0, 1, 120, 4950, 108900, 1557270, 16195608, 131589315, 877262100, 4971151900] |
| DiagCol8 | [0, 1, 165, 9075, 259545, 4723719, 61408347, 614083470, 4971151900, 33803832920] |
| DiagCol9 | [0, 1, 220, 15730, 572572, 13026013, 208416208, 2530768240, 24584605760, 198520691512] |

Baxter:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow3 | [1, 6, 13, 22, 33, 46, 61, 78, 97, 118] |
| PolyRow4 | [1, 22, 69, 148, 265, 426, 637, 904, 1233, 1630] |
| PolyRow5 | [1, 92, 417, 1132, 2417, 4476, 7537, 11852, 17697, 25372] |
| PolyRow6 | [1, 422, 2763, 9484, 24125, 51426, 97447, 169688, 277209, 430750] |
| PolyRow7 | [1, 2074, 19609, 85066, 257665, 631906, 1346809, 2595874, 4637761, 7807690] |
| PolyRow8 | [1, 10754, 146793, 804556, 2900945, 8182446, 19609849, 41823608, 81694881, 148967290] |
| PolyRow9 | [1, 58202, 1146833, 7939738, 34070369, 110503226, 297725617, 702505658, 1500002753, 2962057114] |

Baxter:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 2, 6, 22, 92, 422, 2074, 10754, 58202] |
| PolyCol2 | [1, 1, 3, 13, 69, 417, 2763, 19609, 146793, 1146833] |
| PolyCol3 | [1, 1, 4, 22, 148, 1132, 9484, 85066, 804556, 7939738] |
| PolyCol4 | [1, 1, 5, 33, 265, 2417, 24125, 257665, 2900945, 34070369] |
| PolyCol5 | [1, 1, 6, 46, 426, 4476, 51426, 631906, 8182446, 110503226] |
| PolyCol6 | [1, 1, 7, 61, 637, 7537, 97447, 1346809, 19609849, 297725617] |
| PolyCol7 | [1, 1, 8, 78, 904, 11852, 169688, 2595874, 41823608, 702505658] |
| PolyCol8 | [1, 1, 9, 97, 1233, 17697, 277209, 4637761, 81694881, 1500002753] |
| PolyCol9 | [1, 1, 10, 118, 1630, 25372, 430750, 7807690, 148967290, 2962057114] |

