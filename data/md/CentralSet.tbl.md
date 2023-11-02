# CentralSet
['A269945', 'A008957', 'A036969']

CentralSet Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, 1, 1] |
| Row3 | [0, 1, 5, 1] |
| Row4 | [0, 1, 21, 14, 1] |
| Row5 | [0, 1, 85, 147, 30, 1] |
| Row6 | [0, 1, 341, 1408, 627, 55, 1] |
| Row7 | [0, 1, 1365, 13013, 11440, 2002, 91, 1] |
| Row8 | [0, 1, 5461, 118482, 196053, 61490, 5278, 140, 1] |
| Row9 | [0, 1, 21845, 1071799, 3255330, 1733303, 251498, 12138, 204, 1] |

CentralSet Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, 1, 1], [0, 1, 5, 1], [0, 1, 21, 14, 1], [0, 1, 85, 147, 30, 1], [0, 1, 341, 1408, 627, 55, 1], [0, 1, 1365, 13013, 11440, 2002, 91, 1], [0, 1, 5461, 118482, 196053, 61490, 5278, 140, 1], [0, 1, 21845, 1071799, 3255330, 1733303, 251498, 12138, 204, 1]] |
| RevTabl    | [[1], [1, 0], [1, 1, 0], [1, 5, 1, 0], [1, 14, 21, 1, 0], [1, 30, 147, 85, 1, 0], [1, 55, 627, 1408, 341, 1, 0], [1, 91, 2002, 11440, 13013, 1365, 1, 0], [1, 140, 5278, 61490, 196053, 118482, 5461, 1, 0], [1, 204, 12138, 251498, 1733303, 3255330, 1071799, 21845, 1, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, 1], [0, 1, 1], [0, 1, 5], [0, 1, 21, 1], [0, 1, 85, 14], [0, 1, 341, 147, 1], [0, 1, 1365, 1408, 30]] |
| AccTabl    | [[1], [0, 1], [0, 1, 2], [0, 1, 6, 7], [0, 1, 22, 36, 37], [0, 1, 86, 233, 263, 264], [0, 1, 342, 1750, 2377, 2432, 2433], [0, 1, 1366, 14379, 25819, 27821, 27912, 27913], [0, 1, 5462, 123944, 319997, 381487, 386765, 386905, 386906], [0, 1, 21846, 1093645, 4348975, 6082278, 6333776, 6345914, 6346118, 6346119]] |
| RevAccTabl | [[1], [1, 0], [2, 1, 0], [7, 6, 1, 0], [37, 36, 22, 1, 0], [264, 263, 233, 86, 1, 0], [2433, 2432, 2377, 1750, 342, 1, 0], [27913, 27912, 27821, 25819, 14379, 1366, 1, 0], [386906, 386905, 386765, 381487, 319997, 123944, 5462, 1, 0], [6346119, 6346118, 6345914, 6333776, 6082278, 4348975, 1093645, 21846, 1, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 2, 2], [1, 6, 7, 7], [1, 15, 36, 37, 37], [1, 31, 178, 263, 264, 264], [1, 56, 683, 2091, 2432, 2433, 2433], [1, 92, 2094, 13534, 26547, 27912, 27913, 27913], [1, 141, 5419, 66909, 262962, 381444, 386905, 386906, 386906], [1, 205, 12343, 263841, 1997144, 5252474, 6324273, 6346118, 6346119, 6346119]] |

CentralSet Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 7, 37, 264, 2433, 27913, 386906, 6346119] |
| EvenSum      | [1, 0, 1, 5, 22, 115, 969, 12896, 206793, 3528877] |
| OddSum       | [0, 1, 1, 2, 15, 149, 1464, 15017, 180113, 2817242] |
| AltSum       | [1, -1, 0, 3, 7, -34, -495, -2121, 26680, 711635] |
| AccSum       | [1, 1, 3, 14, 96, 847, 9335, 125211, 1991467, 36918672] |
| AccRevSum    | [1, 2, 5, 21, 126, 1001, 10129, 126006, 1877593, 32888637] |
| DiagSum      | [1, 0, 1, 1, 2, 6, 23, 100, 490, 2804] |

CentralSet Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 5, 42, 24990, 12439680, 3123120, 943260039381660, 56022696483932096138220] |
| RowGcd     | [1, 1, 1, 5, 7, 1, 11, 13, 1, 17] |
| RowMax     | [1, 1, 1, 5, 21, 147, 1408, 13013, 196053, 3255330] |
| CentralE   | [1, 1, 21, 1408, 196053] |
| CentralO   | [0, 1, 85, 13013, 3255330] |
| ColMiddle  | [1, 0, 1, 1, 21, 85, 1408, 13013, 196053, 3255330] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 5, 30, 227, 2169, 25480, 358993, 5959213, 114813254] |
| TransNat0  | [0, 1, 3, 14, 89, 737, 7696, 98093, 1490687, 26542518] |
| TransNat1  | [1, 2, 5, 21, 126, 1001, 10129, 126006, 1877593, 32888637] |

CentralSet Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, 1, 5, 14, 30, 55, 91, 140, 204, 285]|
| DiagRow2 | [0, 1, 21, 147, 627, 2002, 5278, 12138, 25194, 48279]|
| DiagRow3 | [0, 1, 85, 1408, 11440, 61490, 251498, 846260, 2458676, 6369275]|
| DiagRow4 | [0, 1, 341, 13013, 196053, 1733303, 10787231, 52253971, 209609235, 725520510]|
| DiagRow5 | [0, 1, 1365, 118482, 3255330, 46587905, 434928221, 2995372800, 16410363840, 75177525150]|
| DiagRow6 | [0, 1, 5461, 1071799, 53157079, 1217854704, 16875270660, 163648537860, 1213911823620, 7303291360770]|
| DiagRow7 | [0, 1, 21845, 9668036, 860181300, 31306548900, 638816292660, 8657594647800, 86347951359480, 677914551581850]|
| DiagRow8 | [0, 1, 87381, 87099705, 13850000505, 796513723005, 23793900258765, 448016038000965, 5974284925007685, 60885363603137535]|
| DiagRow9 | [0, 1, 349525, 784246870, 222384254950, 20135227330075, 876715636645615, 22829501498692900, 405183736699184740, 5336898188553325075]|

CentralSet Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol2 | [1, 5, 21, 85, 341, 1365, 5461, 21845, 87381, 349525] |
| DiagCol3 | [1, 14, 147, 1408, 13013, 118482, 1071799, 9668036, 87099705, 784246870] |
| DiagCol4 | [1, 30, 627, 11440, 196053, 3255330, 53157079, 860181300, 13850000505, 222384254950] |
| DiagCol5 | [1, 55, 2002, 61490, 1733303, 46587905, 1217854704, 31306548900, 796513723005, 20135227330075] |
| DiagCol6 | [1, 91, 5278, 251498, 10787231, 434928221, 16875270660, 638816292660, 23793900258765, 876715636645615] |
| DiagCol7 | [1, 140, 12138, 846260, 52253971, 2995372800, 163648537860, 8657594647800, 448016038000965, 22829501498692900] |
| DiagCol8 | [1, 204, 25194, 2458676, 209609235, 16410363840, 1213911823620, 86347951359480, 5974284925007685, 405183736699184740] |
| DiagCol9 | [1, 285, 48279, 6369275, 725520510, 75177525150, 7303291360770, 677914551581850, 60885363603137535, 5336898188553325075] |

CentralSet Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] |
| PolyRow3 | [0, 7, 30, 75, 148, 255, 402, 595, 840, 1143] |
| PolyRow4 | [0, 37, 214, 651, 1492, 2905, 5082, 8239, 12616, 18477] |
| PolyRow5 | [0, 264, 2030, 7410, 19476, 42380, 81474, 143430, 236360, 369936] |
| PolyRow6 | [0, 2433, 24486, 105969, 316500, 763905, 1603338, 3047121, 5375304, 8946945] |
| PolyRow7 | [0, 27913, 362622, 1845291, 6222484, 16567005, 37779378, 77175007, 145162056, 256015089] |
| PolyRow8 | [0, 386906, 6430198, 38230932, 144803540, 423433030, 1045140666, 2287104848, 4572924232, 8521650450] |
| PolyRow9 | [0, 6346119, 133915022, 925255515, 3919847700, 12545252255, 33413840034, 78117394467, 165621556040, 325372117815] |

CentralSet Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 2, 7, 37, 264, 2433, 27913, 386906, 6346119] |
| PolyCol2 | [1, 2, 6, 30, 214, 2030, 24486, 362622, 6430198, 133915022] |
| PolyCol3 | [1, 3, 12, 75, 651, 7410, 105969, 1845291, 38230932, 925255515] |
| PolyCol4 | [1, 4, 20, 148, 1492, 19476, 316500, 6222484, 144803540, 3919847700] |
| PolyCol5 | [1, 5, 30, 255, 2905, 42380, 763905, 16567005, 423433030, 12545252255] |
| PolyCol6 | [1, 6, 42, 402, 5082, 81474, 1603338, 37779378, 1045140666, 33413840034] |
| PolyCol7 | [1, 7, 56, 595, 8239, 143430, 3047121, 77175007, 2287104848, 78117394467] |
| PolyCol8 | [1, 8, 72, 840, 12616, 236360, 5375304, 145162056, 4572924232, 165621556040] |
| PolyCol9 | [1, 9, 90, 1143, 18477, 369936, 8946945, 256015089, 8521650450, 325372117815] |

# CentralSet:Inv
[]

CentralSet:Inv Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [0, 1] |
| Row2 | [0, -1, 1] |
| Row3 | [0, 4, -5, 1] |
| Row4 | [0, -36, 49, -14, 1] |
| Row5 | [0, 576, -820, 273, -30, 1] |
| Row6 | [0, -14400, 21076, -7645, 1023, -55, 1] |
| Row7 | [0, 518400, -773136, 296296, -44473, 3003, -91, 1] |
| Row8 | [0, -25401600, 38402064, -15291640, 2475473, -191620, 7462, -140, 1] |
| Row9 | [0, 1625702400, -2483133696, 1017067024, -173721912, 14739153, -669188, 16422, -204, 1] |

CentralSet:Inv Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [0, 1], [0, -1, 1], [0, 4, -5, 1], [0, -36, 49, -14, 1], [0, 576, -820, 273, -30, 1], [0, -14400, 21076, -7645, 1023, -55, 1], [0, 518400, -773136, 296296, -44473, 3003, -91, 1], [0, -25401600, 38402064, -15291640, 2475473, -191620, 7462, -140, 1], [0, 1625702400, -2483133696, 1017067024, -173721912, 14739153, -669188, 16422, -204, 1]] |
| RevTabl    | [[1], [1, 0], [1, -1, 0], [1, -5, 4, 0], [1, -14, 49, -36, 0], [1, -30, 273, -820, 576, 0], [1, -55, 1023, -7645, 21076, -14400, 0], [1, -91, 3003, -44473, 296296, -773136, 518400, 0], [1, -140, 7462, -191620, 2475473, -15291640, 38402064, -25401600, 0], [1, -204, 16422, -669188, 14739153, -173721912, 1017067024, -2483133696, 1625702400, 0]] |
| AntiDiag   | [[1], [0], [0, 1], [0, -1], [0, 4, 1], [0, -36, -5], [0, 576, 49, 1], [0, -14400, -820, -14], [0, 518400, 21076, 273, 1], [0, -25401600, -773136, -7645, -30]] |
| AccTabl    | [[1], [0, 1], [0, -1, 0], [0, 4, -1, 0], [0, -36, 13, -1, 0], [0, 576, -244, 29, -1, 0], [0, -14400, 6676, -969, 54, -1, 0], [0, 518400, -254736, 41560, -2913, 90, -1, 0], [0, -25401600, 13000464, -2291176, 184297, -7323, 139, -1, 0], [0, 1625702400, -857431296, 159635728, -14086184, 652969, -16219, 203, -1, 0]] |
| RevAccTabl | [[1], [1, 0], [0, -1, 0], [0, -1, 4, 0], [0, -1, 13, -36, 0], [0, -1, 29, -244, 576, 0], [0, -1, 54, -969, 6676, -14400, 0], [0, -1, 90, -2913, 41560, -254736, 518400, 0], [0, -1, 139, -7323, 184297, -2291176, 13000464, -25401600, 0], [0, -1, 203, -16219, 652969, -14086184, 159635728, -857431296, 1625702400, 0]] |
| AccRevTabl | [[1], [1, 1], [1, 0, 0], [1, -4, 0, 0], [1, -13, 36, 0, 0], [1, -29, 244, -576, 0, 0], [1, -54, 969, -6676, 14400, 0, 0], [1, -90, 2913, -41560, 254736, -518400, 0, 0], [1, -139, 7323, -184297, 2291176, -13000464, 25401600, 0, 0], [1, -203, 16219, -652969, 14086184, -159635728, 857431296, -1625702400, 0, 0]] |

CentralSet:Inv Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 0, 1, -5, 50, -850, 22100, -817700, 40885000, -2657525000] |
| OddSum       | [0, 1, -1, 5, -50, 850, -22100, 817700, -40885000, 2657525000] |
| AltSum       | [1, -1, 2, -10, 100, -1700, 44200, -1635400, 81770000, -5315050000] |
| AccSum       | [1, 1, -1, 3, -24, 360, -8640, 302400, -14515200, 914457600] |
| AccRevSum    | [1, 2, 1, -3, 24, -360, 8640, -302400, 14515200, -914457600] |
| DiagSum      | [1, 0, 1, -1, 5, -41, 626, -15234, 539750, -26182411] |

CentralSet:Inv Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 20, 1764, 10745280, 326939342400, 352300447699200, 27645512323747439317996800, 154247614654991126666726732897894400] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 5, 49, 820, 21076, 773136, 38402064, 2483133696] |
| CentralE   | [1, -1, 49, -7645, 2475473] |
| CentralO   | [0, 4, -820, 296296, -173721912] |
| ColMiddle  | [1, 0, -1, 4, 49, -820, -7645, 296296, 2475473, -173721912] |
| ColLeft    | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| ColRight   | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| TransSqrs  | [0, 1, 3, -7, 50, -702, 16128, -547200, 25660800, -1587600000] |
| TransNat0  | [0, 1, 1, -3, 24, -360, 8640, -302400, 14515200, -914457600] |
| TransNat1  | [1, 2, 1, -3, 24, -360, 8640, -302400, 14515200, -914457600] |

CentralSet:Inv Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow1 | [0, -1, -5, -14, -30, -55, -91, -140, -204, -285]|
| DiagRow2 | [0, 4, 49, 273, 1023, 3003, 7462, 16422, 32946, 61446]|
| DiagRow3 | [0, -36, -820, -7645, -44473, -191620, -669188, -1999370, -5293970, -12728936]|
| DiagRow4 | [0, 576, 21076, 296296, 2475473, 14739153, 68943381, 268880381, 909450751, 2742417535]|
| DiagRow5 | [0, -14400, -773136, -15291640, -173721912, -1367593305, -8261931405, -40796457506, -171757365650, -635225929065]|
| DiagRow6 | [0, 518400, 38402064, 1017067024, 15088541896, 151847872396, 1151541572401, 7026231453265, 36053226248115, 160557508344855]|
| DiagRow7 | [0, -25401600, -2483133696, -84865562640, -1593719752240, -19967312312156, -185789298737900, -1373222414339685, -8439654758970225, -44565094136562600]|
| DiagRow8 | [0, 1625702400, 202759531776, 8689315795776, 201529405816816, 3076822378767280, 34475213865472380, 303626807076050640, 2202549127844351265, 13611213226804376865]|
| DiagRow9 | [0, -131681894400, -20407635072000, -1071814846360896, -30092049283982400, -550075031295652720, -7307216948928239200, -75623248541039633200, -639475825269193557040, -4573116447815658471025]|

CentralSet:Inv Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| DiagCol1 | [1, -1, 4, -36, 576, -14400, 518400, -25401600, 1625702400, -131681894400] |
| DiagCol2 | [1, -5, 49, -820, 21076, -773136, 38402064, -2483133696, 202759531776, -20407635072000] |
| DiagCol3 | [1, -14, 273, -7645, 296296, -15291640, 1017067024, -84865562640, 8689315795776, -1071814846360896] |
| DiagCol4 | [1, -30, 1023, -44473, 2475473, -173721912, 15088541896, -1593719752240, 201529405816816, -30092049283982400] |
| DiagCol5 | [1, -55, 3003, -191620, 14739153, -1367593305, 151847872396, -19967312312156, 3076822378767280, -550075031295652720] |
| DiagCol6 | [1, -91, 7462, -669188, 68943381, -8261931405, 1151541572401, -185789298737900, 34475213865472380, -7307216948928239200] |
| DiagCol7 | [1, -140, 16422, -1999370, 268880381, -40796457506, 7026231453265, -1373222414339685, 303626807076050640, -75623248541039633200] |
| DiagCol8 | [1, -204, 32946, -5293970, 909450751, -171757365650, 36053226248115, -8439654758970225, 2202549127844351265, -639475825269193557040] |
| DiagCol9 | [1, -285, 61446, -12728936, 2742417535, -635225929065, 160557508344855, -44565094136562600, 13611213226804376865, -4573116447815658471025] |

CentralSet:Inv Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] |
| PolyRow2 | [0, 0, 2, 6, 12, 20, 30, 42, 56, 72] |
| PolyRow3 | [0, 0, -4, -6, 0, 20, 60, 126, 224, 360] |
| PolyRow4 | [0, 0, 28, 36, 0, -80, -180, -252, -224, 0] |
| PolyRow5 | [0, 0, -392, -468, 0, 880, 1800, 2268, 1792, 0] |
| PolyRow6 | [0, 0, 9016, 10296, 0, -17600, -34200, -40824, -30464, 0] |
| PolyRow7 | [0, 0, -306544, -339768, 0, 545600, 1026000, 1183896, 852992, 0] |
| PolyRow8 | [0, 0, 14407568, 15629328, 0, -24006400, -44118000, -49723632, -34972672, 0] |
| PolyRow9 | [0, 0, -893269216, -953389008, 0, 1416377600, 2558844000, 2834247024, 1958469632, 0] |

CentralSet:Inv Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol1 | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 2, 2, -4, 28, -392, 9016, -306544, 14407568, -893269216] |
| PolyCol3 | [1, 3, 6, -6, 36, -468, 10296, -339768, 15629328, -953389008] |
| PolyCol4 | [1, 4, 12, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol5 | [1, 5, 20, 20, -80, 880, -17600, 545600, -24006400, 1416377600] |
| PolyCol6 | [1, 6, 30, 60, -180, 1800, -34200, 1026000, -44118000, 2558844000] |
| PolyCol7 | [1, 7, 42, 126, -252, 2268, -40824, 1183896, -49723632, 2834247024] |
| PolyCol8 | [1, 8, 56, 224, -224, 1792, -30464, 852992, -34972672, 1958469632] |
| PolyCol9 | [1, 9, 72, 360, 0, 0, 0, 0, 0, 0] |

# CentralSet:Rev
[]

CentralSet:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, 1, 0] |
| Row3 | [1, 5, 1, 0] |
| Row4 | [1, 14, 21, 1, 0] |
| Row5 | [1, 30, 147, 85, 1, 0] |
| Row6 | [1, 55, 627, 1408, 341, 1, 0] |
| Row7 | [1, 91, 2002, 11440, 13013, 1365, 1, 0] |
| Row8 | [1, 140, 5278, 61490, 196053, 118482, 5461, 1, 0] |
| Row9 | [1, 204, 12138, 251498, 1733303, 3255330, 1071799, 21845, 1, 0] |

CentralSet:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, 1, 0], [1, 5, 1, 0], [1, 14, 21, 1, 0], [1, 30, 147, 85, 1, 0], [1, 55, 627, 1408, 341, 1, 0], [1, 91, 2002, 11440, 13013, 1365, 1, 0], [1, 140, 5278, 61490, 196053, 118482, 5461, 1, 0], [1, 204, 12138, 251498, 1733303, 3255330, 1071799, 21845, 1, 0]] |
| RevTabl    | [[1], [0, 1], [0, 1, 1], [0, 1, 5, 1], [0, 1, 21, 14, 1], [0, 1, 85, 147, 30, 1], [0, 1, 341, 1408, 627, 55, 1], [0, 1, 1365, 13013, 11440, 2002, 91, 1], [0, 1, 5461, 118482, 196053, 61490, 5278, 140, 1], [0, 1, 21845, 1071799, 3255330, 1733303, 251498, 12138, 204, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, 1], [1, 5, 0], [1, 14, 1], [1, 30, 21, 0], [1, 55, 147, 1], [1, 91, 627, 85, 0], [1, 140, 2002, 1408, 1]] |
| AccTabl    | [[1], [1, 1], [1, 2, 2], [1, 6, 7, 7], [1, 15, 36, 37, 37], [1, 31, 178, 263, 264, 264], [1, 56, 683, 2091, 2432, 2433, 2433], [1, 92, 2094, 13534, 26547, 27912, 27913, 27913], [1, 141, 5419, 66909, 262962, 381444, 386905, 386906, 386906], [1, 205, 12343, 263841, 1997144, 5252474, 6324273, 6346118, 6346119, 6346119]] |
| RevAccTabl | [[1], [1, 1], [2, 2, 1], [7, 7, 6, 1], [37, 37, 36, 15, 1], [264, 264, 263, 178, 31, 1], [2433, 2433, 2432, 2091, 683, 56, 1], [27913, 27913, 27912, 26547, 13534, 2094, 92, 1], [386906, 386906, 386905, 381444, 262962, 66909, 5419, 141, 1], [6346119, 6346119, 6346118, 6324273, 5252474, 1997144, 263841, 12343, 205, 1]] |
| AccRevTabl | [[1], [0, 1], [0, 1, 2], [0, 1, 6, 7], [0, 1, 22, 36, 37], [0, 1, 86, 233, 263, 264], [0, 1, 342, 1750, 2377, 2432, 2433], [0, 1, 1366, 14379, 25819, 27821, 27912, 27913], [0, 1, 5462, 123944, 319997, 381487, 386765, 386905, 386906], [0, 1, 21846, 1093645, 4348975, 6082278, 6333776, 6345914, 6346118, 6346119]] |

CentralSet:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 2, 7, 37, 264, 2433, 27913, 386906, 6346119] |
| EvenSum      | [1, 1, 1, 2, 22, 149, 969, 15017, 206793, 2817242] |
| OddSum       | [0, 0, 1, 5, 15, 115, 1464, 12896, 180113, 3528877] |
| AltSum       | [1, 1, 0, -3, 7, 34, -495, 2121, 26680, -711635] |
| AccSum       | [1, 2, 5, 21, 126, 1001, 10129, 126006, 1877593, 32888637] |
| AccRevSum    | [1, 1, 3, 14, 96, 847, 9335, 125211, 1991467, 36918672] |
| DiagSum      | [1, 1, 1, 2, 6, 16, 52, 204, 804, 3552] |

CentralSet:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 5, 42, 24990, 12439680, 3123120, 943260039381660, 56022696483932096138220] |
| RowGcd     | [1, 1, 1, 5, 7, 1, 11, 13, 1, 17] |
| RowMax     | [1, 1, 1, 5, 21, 147, 1408, 13013, 196053, 3255330] |
| CentralE   | [1, 1, 21, 1408, 196053] |
| CentralO   | [1, 5, 147, 11440, 1733303] |
| ColMiddle  | [1, 1, 1, 5, 21, 147, 1408, 11440, 196053, 1733303] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, 1, 9, 107, 1399, 20716, 353428, 6870205, 151083569] |
| TransNat0  | [0, 0, 1, 7, 59, 583, 6902, 97298, 1604561, 30572553] |
| TransNat1  | [1, 1, 3, 14, 96, 847, 9335, 125211, 1991467, 36918672] |

CentralSet:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]|
| DiagRow2 | [1, 5, 21, 85, 341, 1365, 5461, 21845, 87381, 349525]|
| DiagRow3 | [1, 14, 147, 1408, 13013, 118482, 1071799, 9668036, 87099705, 784246870]|
| DiagRow4 | [1, 30, 627, 11440, 196053, 3255330, 53157079, 860181300, 13850000505, 222384254950]|
| DiagRow5 | [1, 55, 2002, 61490, 1733303, 46587905, 1217854704, 31306548900, 796513723005, 20135227330075]|
| DiagRow6 | [1, 91, 5278, 251498, 10787231, 434928221, 16875270660, 638816292660, 23793900258765, 876715636645615]|
| DiagRow7 | [1, 140, 12138, 846260, 52253971, 2995372800, 163648537860, 8657594647800, 448016038000965, 22829501498692900]|
| DiagRow8 | [1, 204, 25194, 2458676, 209609235, 16410363840, 1213911823620, 86347951359480, 5974284925007685, 405183736699184740]|
| DiagRow9 | [1, 285, 48279, 6369275, 725520510, 75177525150, 7303291360770, 677914551581850, 60885363603137535, 5336898188553325075]|

CentralSet:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, 1, 5, 14, 30, 55, 91, 140, 204, 285] |
| DiagCol2 | [0, 1, 21, 147, 627, 2002, 5278, 12138, 25194, 48279] |
| DiagCol3 | [0, 1, 85, 1408, 11440, 61490, 251498, 846260, 2458676, 6369275] |
| DiagCol4 | [0, 1, 341, 13013, 196053, 1733303, 10787231, 52253971, 209609235, 725520510] |
| DiagCol5 | [0, 1, 1365, 118482, 3255330, 46587905, 434928221, 2995372800, 16410363840, 75177525150] |
| DiagCol6 | [0, 1, 5461, 1071799, 53157079, 1217854704, 16875270660, 163648537860, 1213911823620, 7303291360770] |
| DiagCol7 | [0, 1, 21845, 9668036, 860181300, 31306548900, 638816292660, 8657594647800, 86347951359480, 677914551581850] |
| DiagCol8 | [0, 1, 87381, 87099705, 13850000505, 796513723005, 23793900258765, 448016038000965, 5974284925007685, 60885363603137535] |
| DiagCol9 | [0, 1, 349525, 784246870, 222384254950, 20135227330075, 876715636645615, 22829501498692900, 405183736699184740, 5336898188553325075] |

CentralSet:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| PolyRow3 | [1, 7, 15, 25, 37, 51, 67, 85, 105, 127] |
| PolyRow4 | [1, 37, 121, 259, 457, 721, 1057, 1471, 1969, 2557] |
| PolyRow5 | [1, 264, 1345, 3790, 8169, 15076, 25129, 38970, 57265, 80704] |
| PolyRow6 | [1, 2433, 19371, 71689, 188685, 408201, 776743, 1349601, 2190969, 3374065] |
| PolyRow7 | [1, 27913, 351663, 1713649, 5497741, 13894881, 30069403, 58326073, 104277849, 175014361] |
| PolyRow8 | [1, 386906, 7791217, 50362828, 197920145, 586014526, 1443941761, 3126705632, 6150938593, 11234784610] |
| PolyRow9 | [1, 6346119, 205355905, 1767466081, 8541537105, 29741852971, 83737304209, 203052994005, 440694547681, 877905446095] |

CentralSet:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 2, 7, 37, 264, 2433, 27913, 386906, 6346119] |
| PolyCol2 | [1, 1, 3, 15, 121, 1345, 19371, 351663, 7791217, 205355905] |
| PolyCol3 | [1, 1, 4, 25, 259, 3790, 71689, 1713649, 50362828, 1767466081] |
| PolyCol4 | [1, 1, 5, 37, 457, 8169, 188685, 5497741, 197920145, 8541537105] |
| PolyCol5 | [1, 1, 6, 51, 721, 15076, 408201, 13894881, 586014526, 29741852971] |
| PolyCol6 | [1, 1, 7, 67, 1057, 25129, 776743, 30069403, 1443941761, 83737304209] |
| PolyCol7 | [1, 1, 8, 85, 1471, 38970, 1349601, 58326073, 3126705632, 203052994005] |
| PolyCol8 | [1, 1, 9, 105, 1969, 57265, 2190969, 104277849, 6150938593, 440694547681] |
| PolyCol9 | [1, 1, 10, 127, 2557, 80704, 3374065, 175014361, 11234784610, 877905446095] |

# CentralSet:Inv:Rev
[]

CentralSet:Inv:Rev Triangle view

|  Row   |  Seq   |
| :---   |  :---  |
| Row0 | [1] |
| Row1 | [1, 0] |
| Row2 | [1, -1, 0] |
| Row3 | [1, -5, 4, 0] |
| Row4 | [1, -14, 49, -36, 0] |
| Row5 | [1, -30, 273, -820, 576, 0] |
| Row6 | [1, -55, 1023, -7645, 21076, -14400, 0] |
| Row7 | [1, -91, 3003, -44473, 296296, -773136, 518400, 0] |
| Row8 | [1, -140, 7462, -191620, 2475473, -15291640, 38402064, -25401600, 0] |
| Row9 | [1, -204, 16422, -669188, 14739153, -173721912, 1017067024, -2483133696, 1625702400, 0] |

CentralSet:Inv:Rev Triangles

| Flat       |  Seq  |
| :---       | :---  |
| Triangle   | [[1], [1, 0], [1, -1, 0], [1, -5, 4, 0], [1, -14, 49, -36, 0], [1, -30, 273, -820, 576, 0], [1, -55, 1023, -7645, 21076, -14400, 0], [1, -91, 3003, -44473, 296296, -773136, 518400, 0], [1, -140, 7462, -191620, 2475473, -15291640, 38402064, -25401600, 0], [1, -204, 16422, -669188, 14739153, -173721912, 1017067024, -2483133696, 1625702400, 0]] |
| RevTabl    | [[1], [0, 1], [0, -1, 1], [0, 4, -5, 1], [0, -36, 49, -14, 1], [0, 576, -820, 273, -30, 1], [0, -14400, 21076, -7645, 1023, -55, 1], [0, 518400, -773136, 296296, -44473, 3003, -91, 1], [0, -25401600, 38402064, -15291640, 2475473, -191620, 7462, -140, 1], [0, 1625702400, -2483133696, 1017067024, -173721912, 14739153, -669188, 16422, -204, 1]] |
| AntiDiag   | [[1], [1], [1, 0], [1, -1], [1, -5, 0], [1, -14, 4], [1, -30, 49, 0], [1, -55, 273, -36], [1, -91, 1023, -820, 0], [1, -140, 3003, -7645, 576]] |
| AccTabl    | [[1], [1, 1], [1, 0, 0], [1, -4, 0, 0], [1, -13, 36, 0, 0], [1, -29, 244, -576, 0, 0], [1, -54, 969, -6676, 14400, 0, 0], [1, -90, 2913, -41560, 254736, -518400, 0, 0], [1, -139, 7323, -184297, 2291176, -13000464, 25401600, 0, 0], [1, -203, 16219, -652969, 14086184, -159635728, 857431296, -1625702400, 0, 0]] |
| RevAccTabl | [[1], [1, 1], [0, 0, 1], [0, 0, -4, 1], [0, 0, 36, -13, 1], [0, 0, -576, 244, -29, 1], [0, 0, 14400, -6676, 969, -54, 1], [0, 0, -518400, 254736, -41560, 2913, -90, 1], [0, 0, 25401600, -13000464, 2291176, -184297, 7323, -139, 1], [0, 0, -1625702400, 857431296, -159635728, 14086184, -652969, 16219, -203, 1]] |
| AccRevTabl | [[1], [0, 1], [0, -1, 0], [0, 4, -1, 0], [0, -36, 13, -1, 0], [0, 576, -244, 29, -1, 0], [0, -14400, 6676, -969, 54, -1, 0], [0, 518400, -254736, 41560, -2913, 90, -1, 0], [0, -25401600, 13000464, -2291176, 184297, -7323, 139, -1, 0], [0, 1625702400, -857431296, 159635728, -14086184, 652969, -16219, 203, -1, 0]] |

CentralSet:Inv:Rev Row sums

| Trait        |   Seq  |
| :---         |  :---  |
| RowSum       | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| EvenSum      | [1, 1, 1, 5, 50, 850, 22100, 817700, 40885000, 2657525000] |
| OddSum       | [0, 0, -1, -5, -50, -850, -22100, -817700, -40885000, -2657525000] |
| AltSum       | [1, 1, 2, 10, 100, 1700, 44200, 1635400, 81770000, 5315050000] |
| AccSum       | [1, 2, 1, -3, 24, -360, 8640, -302400, 14515200, -914457600] |
| AccRevSum    | [1, 1, -1, 3, -24, 360, -8640, 302400, -14515200, 914457600] |
| DiagSum      | [1, 1, 1, 0, -4, -9, 20, 183, 113, -4205] |

CentralSet:Inv:Rev Transforms

| Trans      |   Seq  |
| :---       |  :---  |
| RowLcm     | [1, 1, 1, 20, 1764, 10745280, 326939342400, 352300447699200, 27645512323747439317996800, 154247614654991126666726732897894400] |
| RowGcd     | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| RowMax     | [1, 1, 1, 5, 49, 820, 21076, 773136, 38402064, 2483133696] |
| CentralE   | [1, -1, 49, -7645, 2475473] |
| CentralO   | [1, -5, 273, -44473, 14739153] |
| ColMiddle  | [1, 1, -1, -5, 49, 273, -7645, -44473, 2475473, 14739153] |
| ColLeft    | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| ColRight   | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0] |
| TransSqrs  | [0, 0, -1, 11, -142, 2898, -87552, 3686400, -206582400, 14872636800] |
| TransNat0  | [0, 0, -1, 3, -24, 360, -8640, 302400, -14515200, 914457600] |
| TransNat1  | [1, 1, -1, 3, -24, 360, -8640, 302400, -14515200, 914457600] |

CentralSet:Inv:Rev Diagonals as rows

| DiagRow  |   Seq  |
| :---     |  :---  |
| DiagRow0 | [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]|
| DiagRow1 | [1, -1, 4, -36, 576, -14400, 518400, -25401600, 1625702400, -131681894400]|
| DiagRow2 | [1, -5, 49, -820, 21076, -773136, 38402064, -2483133696, 202759531776, -20407635072000]|
| DiagRow3 | [1, -14, 273, -7645, 296296, -15291640, 1017067024, -84865562640, 8689315795776, -1071814846360896]|
| DiagRow4 | [1, -30, 1023, -44473, 2475473, -173721912, 15088541896, -1593719752240, 201529405816816, -30092049283982400]|
| DiagRow5 | [1, -55, 3003, -191620, 14739153, -1367593305, 151847872396, -19967312312156, 3076822378767280, -550075031295652720]|
| DiagRow6 | [1, -91, 7462, -669188, 68943381, -8261931405, 1151541572401, -185789298737900, 34475213865472380, -7307216948928239200]|
| DiagRow7 | [1, -140, 16422, -1999370, 268880381, -40796457506, 7026231453265, -1373222414339685, 303626807076050640, -75623248541039633200]|
| DiagRow8 | [1, -204, 32946, -5293970, 909450751, -171757365650, 36053226248115, -8439654758970225, 2202549127844351265, -639475825269193557040]|
| DiagRow9 | [1, -285, 61446, -12728936, 2742417535, -635225929065, 160557508344855, -44565094136562600, 13611213226804376865, -4573116447815658471025]|

CentralSet:Inv:Rev Diagonals as columns

| DiagCol  |   Seq  |
| :---     |  :---  |
| DiagCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| DiagCol1 | [0, -1, -5, -14, -30, -55, -91, -140, -204, -285] |
| DiagCol2 | [0, 4, 49, 273, 1023, 3003, 7462, 16422, 32946, 61446] |
| DiagCol3 | [0, -36, -820, -7645, -44473, -191620, -669188, -1999370, -5293970, -12728936] |
| DiagCol4 | [0, 576, 21076, 296296, 2475473, 14739153, 68943381, 268880381, 909450751, 2742417535] |
| DiagCol5 | [0, -14400, -773136, -15291640, -173721912, -1367593305, -8261931405, -40796457506, -171757365650, -635225929065] |
| DiagCol6 | [0, 518400, 38402064, 1017067024, 15088541896, 151847872396, 1151541572401, 7026231453265, 36053226248115, 160557508344855] |
| DiagCol7 | [0, -25401600, -2483133696, -84865562640, -1593719752240, -19967312312156, -185789298737900, -1373222414339685, -8439654758970225, -44565094136562600] |
| DiagCol8 | [0, 1625702400, 202759531776, 8689315795776, 201529405816816, 3076822378767280, 34475213865472380, 303626807076050640, 2202549127844351265, 13611213226804376865] |
| DiagCol9 | [0, -131681894400, -20407635072000, -1071814846360896, -30092049283982400, -550075031295652720, -7307216948928239200, -75623248541039633200, -639475825269193557040, -4573116447815658471025] |

CentralSet:Inv:Rev Polynomial values as rows

| PolyRow  |   Seq  |
| :---     |  :---  |
| PolyRow0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow1 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyRow2 | [1, 0, -1, -2, -3, -4, -5, -6, -7, -8] |
| PolyRow3 | [1, 0, 7, 22, 45, 76, 115, 162, 217, 280] |
| PolyRow4 | [1, 0, -119, -572, -1575, -3344, -6095, -10044, -15407, -22400] |
| PolyRow5 | [1, 0, 3689, 26884, 99225, 264176, 579025, 1114884, 1956689, 3203200] |
| PolyRow6 | [1, 0, -180761, -1989416, -9823275, -32757824, -86274725, -193989816, -389381111, -717516800] |
| PolyRow7 | [1, 0, 12834031, 212867512, 1404728325, 5863650496, 18549065875, 48691443816, 111752378857, 231757926400] |
| PolyRow8 | [1, 0, -1244901007, -31078656752, -273922023375, -1430730721024, -5434876301375, -16652473785072, -43695180133087, -101973487616000] |
| PolyRow9 | [1, 0, 158102427889, 5936023439632, 69850115960625, 456403100006656, 2081557623426625, 7443655781927184, 22328237048007457, 58634755379200000] |

CentralSet:Inv:Rev Polynomial values as columns

| PolyCol  |   Seq  |
| :---     |  :---  |
| PolyCol0 | [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] |
| PolyCol1 | [1, 1, 0, 0, 0, 0, 0, 0, 0, 0] |
| PolyCol2 | [1, 1, -1, 7, -119, 3689, -180761, 12834031, -1244901007, 158102427889] |
| PolyCol3 | [1, 1, -2, 22, -572, 26884, -1989416, 212867512, -31078656752, 5936023439632] |
| PolyCol4 | [1, 1, -3, 45, -1575, 99225, -9823275, 1404728325, -273922023375, 69850115960625] |
| PolyCol5 | [1, 1, -4, 76, -3344, 264176, -32757824, 5863650496, -1430730721024, 456403100006656] |
| PolyCol6 | [1, 1, -5, 115, -6095, 579025, -86274725, 18549065875, -5434876301375, 2081557623426625] |
| PolyCol7 | [1, 1, -6, 162, -10044, 1114884, -193989816, 48691443816, -16652473785072, 7443655781927184] |
| PolyCol8 | [1, 1, -7, 217, -15407, 1956689, -389381111, 111752378857, -43695180133087, 22328237048007457] |
| PolyCol9 | [1, 1, -8, 280, -22400, 3203200, -717516800, 231757926400, -101973487616000, 58634755379200000] |
