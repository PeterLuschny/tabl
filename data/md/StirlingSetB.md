# StirlingSetB
['A154602']

StirlingSetB Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [3, 4, 1] |
| trow3 | [11, 19, 9, 1] |
| trow4 | [49, 104, 70, 16, 1] |
| trow5 | [257, 641, 550, 190, 25, 1] |
| trow6 | [1539, 4380, 4531, 2080, 425, 36, 1] |

StirlingSetB Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 3, 4, 1, 11, 19, 9, 1, 49, 104, 70, 16, 1, 257, 641, 550, 190, 25, 1, 1539, 4380, 4531, 2080, 425, 36, 1] |
| rev      | [1, 1, 1, 1, 4, 3, 1, 9, 19, 11, 1, 16, 70, 104, 49, 1, 25, 190, 550, 641, 257, 1, 36, 425, 2080, 4531, 4380, 1539] |
| accu     | [1, 1, 2, 3, 7, 8, 11, 30, 39, 40, 49, 153, 223, 239, 240, 257, 898, 1448, 1638, 1663, 1664, 1539, 5919, 10450, 12530, 12955, 12991, 12992] |
| revaccu  | [1, 2, 1, 8, 7, 3, 40, 39, 30, 11, 240, 239, 223, 153, 49, 1664, 1663, 1638, 1448, 898, 257, 12992, 12991, 12955, 12530, 10450, 5919, 1539] |
| accurev  | [1, 1, 2, 1, 5, 8, 1, 10, 29, 40, 1, 17, 87, 191, 240, 1, 26, 216, 766, 1407, 1664, 1, 37, 462, 2542, 7073, 11453, 12992] |
| diag     | [1, 1, 3, 1, 11, 4, 49, 19, 1, 257, 104, 9] |

StirlingSetB Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 8, 40, 240, 1664, 12992] |
| evensum   | [1, 1, 4, 20, 120, 832, 6496] |
| oddsum    | [0, 1, 4, 20, 120, 832, 6496] |
| altsum    | [1, 0, 0, 0, 0, 0, 0] |
| diagsum   | [1, 1, 4, 15, 69, 370] |
| accusum   | [1, 3, 18, 120, 904, 7568, 69376] |
| revaccusum | [1, 3, 14, 80, 536, 4080, 34560] |

StirlingSetB Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [1, 4, 9, 16, 25, 36, 49]|
| rdiag2 | [3, 19, 70, 190, 425, 833, 1484]|
| rdiag3 | [11, 104, 550, 2080, 6265, 16016, 36204]|
| rdiag4 | [49, 641, 4531, 22491, 87206, 281190, 786282]|
| rdiag5 | [257, 4380, 39515, 247072, 1192086, 4719624, 15982890]|
| rdiag6 | [1539, 32803, 365324, 2792476, 16333150, 77684398, 312957436]|

StirlingSetB Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 3, 11, 49, 257, 1539] |
| cdiag1 | [1, 4, 19, 104, 641, 4380, 32803] |
| cdiag2 | [1, 9, 70, 550, 4531, 39515, 365324] |
| cdiag3 | [1, 16, 190, 2080, 22491, 247072, 2792476] |
| cdiag4 | [1, 25, 425, 6265, 87206, 1192086, 16333150] |
| cdiag5 | [1, 36, 833, 16016, 281190, 4719624, 77684398] |
| cdiag6 | [1, 49, 1484, 36204, 786282, 15982890, 312957436] |

StirlingSetB Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [3, 8, 15, 24, 35, 48, 63] |
| rpdiag3 | [11, 40, 93, 176, 295, 456, 665] |
| rpdiag4 | [49, 240, 681, 1504, 2865, 4944, 7945] |
| rpdiag5 | [257, 1664, 5691, 14528, 31205, 59712, 105119] |
| rpdiag6 | [1539, 12992, 53079, 155520, 374435, 790464, 1517607] |

StirlingSetB Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 3, 11, 49, 257, 1539] |
| cpdiag1 | [1, 2, 8, 40, 240, 1664, 12992] |
| cpdiag2 | [1, 3, 15, 93, 681, 5691, 53079] |
| cpdiag3 | [1, 4, 24, 176, 1504, 14528, 155520] |
| cpdiag4 | [1, 5, 35, 295, 2865, 31205, 374435] |
| cpdiag5 | [1, 6, 48, 456, 4944, 59712, 790464] |
| cpdiag6 | [1, 7, 63, 665, 7945, 105119, 1517607] |

# StirlingSetBInv
True

StirlingSetBInv Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [-1, 1] |
| trow2 | [1, -4, 1] |
| trow3 | [-1, 17, -9, 1] |
| trow4 | [1, -96, 74, -16, 1] |
| trow5 | [-1, 729, -690, 210, -25, 1] |
| trow6 | [1, -7060, 7579, -2840, 475, -36, 1] |

StirlingSetBInv Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, -1, 1, 1, -4, 1, -1, 17, -9, 1, 1, -96, 74, -16, 1, -1, 729, -690, 210, -25, 1, 1, -7060, 7579, -2840, 475, -36, 1] |
| rev      | [1, 1, -1, 1, -4, 1, 1, -9, 17, -1, 1, -16, 74, -96, 1, 1, -25, 210, -690, 729, -1, 1, -36, 475, -2840, 7579, -7060, 1] |
| accu     | [1, -1, 0, 1, -3, -2, -1, 16, 7, 8, 1, -95, -21, -37, -36, -1, 728, 38, 248, 223, 224, 1, -7059, 520, -2320, -1845, -1881, -1880] |
| revaccu  | [1, 0, -1, -2, -3, 1, 8, 7, 16, -1, -36, -37, -21, -95, 1, 224, 223, 248, 38, 728, -1, -1880, -1881, -1845, -2320, 520, -7059, 1] |
| accurev  | [1, 1, 0, 1, -3, -2, 1, -8, 9, 8, 1, -15, 59, -37, -36, 1, -24, 186, -504, 225, 224, 1, -35, 440, -2400, 5179, -1881, -1880] |
| diag     | [1, -1, 1, 1, -1, -4, 1, 17, 1, -1, -96, -9] |

StirlingSetBInv Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 0, -2, 8, -36, 224, -1880] |
| evensum   | [1, -1, 2, -10, 76, -716, 8056] |
| oddsum    | [0, 1, -4, 18, -112, 940, -9936] |
| altsum    | [1, -2, 6, -28, 188, -1656, 17992] |
| diagsum   | [1, -1, 2, -5, 19, -106] |
| accusum   | [1, -1, -4, 30, -188, 1460, -14464] |
| revaccusum | [1, 1, -4, 10, -28, 108, -576] |

StirlingSetBInv Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [-1, -4, -9, -16, -25, -36, -49]|
| rdiag2 | [1, 17, 74, 210, 475, 931, 1652]|
| rdiag3 | [-1, -96, -690, -2840, -8715, -22176, -49476]|
| rdiag4 | [1, 729, 7579, 41979, 166054, 528150, 1438458]|
| rdiag5 | [-1, -7060, -97307, -687232, -3370710, -13006392, -42224490]|
| rdiag6 | [1, 83033, 1436532, 12447812, 73502330, 336073562, 1275590756]|

StirlingSetBInv Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, -1, 1, -1, 1, -1, 1] |
| cdiag1 | [1, -4, 17, -96, 729, -7060, 83033] |
| cdiag2 | [1, -9, 74, -690, 7579, -97307, 1436532] |
| cdiag3 | [1, -16, 210, -2840, 41979, -687232, 12447812] |
| cdiag4 | [1, -25, 475, -8715, 166054, -3370710, 73502330] |
| cdiag5 | [1, -36, 931, -22176, 528150, -13006392, 336073562] |
| cdiag6 | [1, -49, 1652, -49476, 1438458, -42224490, 1275590756] |

StirlingSetBInv Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [-1, 0, 1, 2, 3, 4, 5] |
| rpdiag2 | [1, -2, -3, -2, 1, 6, 13] |
| rpdiag3 | [-1, 8, 5, -4, -13, -16, -7] |
| rpdiag4 | [1, -36, -7, 28, 33, -4, -71] |
| rpdiag5 | [-1, 224, 9, -136, -61, 144, 269] |
| rpdiag6 | [1, -1880, -11, 808, 97, -824, -635] |

StirlingSetBInv Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, -1, 1, -1, 1, -1, 1] |
| cpdiag1 | [1, 0, -2, 8, -36, 224, -1880] |
| cpdiag2 | [1, 1, -3, 5, -7, 9, -11] |
| cpdiag3 | [1, 2, -2, -4, 28, -136, 808] |
| cpdiag4 | [1, 3, 1, -13, 33, -61, 97] |
| cpdiag5 | [1, 4, 6, -16, -4, 144, -824] |
| cpdiag6 | [1, 5, 13, -7, -71, 269, -635] |

# StirlingSetBRev
True

StirlingSetBRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [1, 4, 3] |
| trow3 | [1, 9, 19, 11] |
| trow4 | [1, 16, 70, 104, 49] |
| trow5 | [1, 25, 190, 550, 641, 257] |
| trow6 | [1, 36, 425, 2080, 4531, 4380, 1539] |

StirlingSetBRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 1, 4, 3, 1, 9, 19, 11, 1, 16, 70, 104, 49, 1, 25, 190, 550, 641, 257, 1, 36, 425, 2080, 4531, 4380, 1539] |
| rev      | [1, 1, 1, 3, 4, 1, 11, 19, 9, 1, 49, 104, 70, 16, 1, 257, 641, 550, 190, 25, 1, 1539, 4380, 4531, 2080, 425, 36, 1] |
| accu     | [1, 1, 2, 1, 5, 8, 1, 10, 29, 40, 1, 17, 87, 191, 240, 1, 26, 216, 766, 1407, 1664, 1, 37, 462, 2542, 7073, 11453, 12992] |
| revaccu  | [1, 2, 1, 8, 5, 1, 40, 29, 10, 1, 240, 191, 87, 17, 1, 1664, 1407, 766, 216, 26, 1, 12992, 11453, 7073, 2542, 462, 37, 1] |
| accurev  | [1, 1, 2, 3, 7, 8, 11, 30, 39, 40, 49, 153, 223, 239, 240, 257, 898, 1448, 1638, 1663, 1664, 1539, 5919, 10450, 12530, 12955, 12991, 12992] |
| diag     | [1, 1, 1, 1, 1, 4, 1, 9, 3, 1, 16, 19] |

StirlingSetBRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 8, 40, 240, 1664, 12992] |
| evensum   | [1, 1, 4, 20, 120, 832, 6496] |
| oddsum    | [0, 1, 4, 20, 120, 832, 6496] |
| altsum    | [1, 0, 0, 0, 0, 0, 0] |
| diagsum   | [1, 1, 2, 5, 13, 36] |
| accusum   | [1, 3, 14, 80, 536, 4080, 34560] |
| revaccusum | [1, 3, 18, 120, 904, 7568, 69376] |

StirlingSetBRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 3, 11, 49, 257, 1539]|
| rdiag1 | [1, 4, 19, 104, 641, 4380, 32803]|
| rdiag2 | [1, 9, 70, 550, 4531, 39515, 365324]|
| rdiag3 | [1, 16, 190, 2080, 22491, 247072, 2792476]|
| rdiag4 | [1, 25, 425, 6265, 87206, 1192086, 16333150]|
| rdiag5 | [1, 36, 833, 16016, 281190, 4719624, 77684398]|
| rdiag6 | [1, 49, 1484, 36204, 786282, 15982890, 312957436]|

StirlingSetBRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [1, 4, 9, 16, 25, 36, 49] |
| cdiag2 | [3, 19, 70, 190, 425, 833, 1484] |
| cdiag3 | [11, 104, 550, 2080, 6265, 16016, 36204] |
| cdiag4 | [49, 641, 4531, 22491, 87206, 281190, 786282] |
| cdiag5 | [257, 4380, 39515, 247072, 1192086, 4719624, 15982890] |
| cdiag6 | [1539, 32803, 365324, 2792476, 16333150, 77684398, 312957436] |

StirlingSetBRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [1, 8, 21, 40, 65, 96, 133] |
| rpdiag3 | [1, 40, 183, 496, 1045, 1896, 3115] |
| rpdiag4 | [1, 240, 1929, 7456, 20385, 45456, 88585] |
| rpdiag5 | [1, 1664, 23691, 131008, 465605, 1277376, 2954959] |
| rpdiag6 | [1, 12992, 329565, 2613376, 12088865, 40837056, 112199437] |

StirlingSetBRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 2, 8, 40, 240, 1664, 12992] |
| cpdiag2 | [1, 3, 21, 183, 1929, 23691, 329565] |
| cpdiag3 | [1, 4, 40, 496, 7456, 131008, 2613376] |
| cpdiag4 | [1, 5, 65, 1045, 20385, 465605, 12088865] |
| cpdiag5 | [1, 6, 96, 1896, 45456, 1277376, 40837056] |
| cpdiag6 | [1, 7, 133, 3115, 88585, 2954959, 112199437] |

# StirlingSetBInvRev
True

StirlingSetBInvRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, -1] |
| trow2 | [1, -4, 1] |
| trow3 | [1, -9, 17, -1] |
| trow4 | [1, -16, 74, -96, 1] |
| trow5 | [1, -25, 210, -690, 729, -1] |
| trow6 | [1, -36, 475, -2840, 7579, -7060, 1] |

StirlingSetBInvRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, -1, 1, -4, 1, 1, -9, 17, -1, 1, -16, 74, -96, 1, 1, -25, 210, -690, 729, -1, 1, -36, 475, -2840, 7579, -7060, 1] |
| rev      | [1, -1, 1, 1, -4, 1, -1, 17, -9, 1, 1, -96, 74, -16, 1, -1, 729, -690, 210, -25, 1, 1, -7060, 7579, -2840, 475, -36, 1] |
| accu     | [1, 1, 0, 1, -3, -2, 1, -8, 9, 8, 1, -15, 59, -37, -36, 1, -24, 186, -504, 225, 224, 1, -35, 440, -2400, 5179, -1881, -1880] |
| revaccu  | [1, 0, 1, -2, -3, 1, 8, 9, -8, 1, -36, -37, 59, -15, 1, 224, 225, -504, 186, -24, 1, -1880, -1881, 5179, -2400, 440, -35, 1] |
| accurev  | [1, -1, 0, 1, -3, -2, -1, 16, 7, 8, 1, -95, -21, -37, -36, -1, 728, 38, 248, 223, 224, 1, -7059, 520, -2320, -1845, -1881, -1880] |
| diag     | [1, 1, 1, -1, 1, -4, 1, -9, 1, 1, -16, 17] |

StirlingSetBInvRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 0, -2, 8, -36, 224, -1880] |
| evensum   | [1, 1, 2, 18, 76, 940, 8056] |
| oddsum    | [0, -1, -4, -10, -112, -716, -9936] |
| altsum    | [1, 2, 6, 28, 188, 1656, 17992] |
| diagsum   | [1, 1, 0, -3, -7, 2] |
| accusum   | [1, 1, -4, 10, -28, 108, -576] |
| revaccusum | [1, -1, -4, 30, -188, 1460, -14464] |

StirlingSetBInvRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, -1, 1, -1, 1, -1, 1]|
| rdiag1 | [1, -4, 17, -96, 729, -7060, 83033]|
| rdiag2 | [1, -9, 74, -690, 7579, -97307, 1436532]|
| rdiag3 | [1, -16, 210, -2840, 41979, -687232, 12447812]|
| rdiag4 | [1, -25, 475, -8715, 166054, -3370710, 73502330]|
| rdiag5 | [1, -36, 931, -22176, 528150, -13006392, 336073562]|
| rdiag6 | [1, -49, 1652, -49476, 1438458, -42224490, 1275590756]|

StirlingSetBInvRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [-1, -4, -9, -16, -25, -36, -49] |
| cdiag2 | [1, 17, 74, 210, 475, 931, 1652] |
| cdiag3 | [-1, -96, -690, -2840, -8715, -22176, -49476] |
| cdiag4 | [1, 729, 7579, 41979, 166054, 528150, 1438458] |
| cdiag5 | [-1, -7060, -97307, -687232, -3370710, -13006392, -42224490] |
| cdiag6 | [1, 83033, 1436532, 12447812, 73502330, 336073562, 1275590756] |

StirlingSetBInvRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 0, -1, -2, -3, -4, -5] |
| rpdiag2 | [1, -2, -3, -2, 1, 6, 13] |
| rpdiag3 | [1, 8, 43, 100, 173, 256, 343] |
| rpdiag4 | [1, -36, -487, -1892, -4767, -9604, -16871] |
| rpdiag5 | [1, 224, 6903, 41992, 144701, 371376, 795379] |
| rpdiag6 | [1, -1880, -125483, -1173464, -5459423, -17653304, -45626075] |

StirlingSetBInvRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 0, -2, 8, -36, 224, -1880] |
| cpdiag2 | [1, -1, -3, 43, -487, 6903, -125483] |
| cpdiag3 | [1, -2, -2, 100, -1892, 41992, -1173464] |
| cpdiag4 | [1, -3, 1, 173, -4767, 144701, -5459423] |
| cpdiag5 | [1, -4, 6, 256, -9604, 371376, -17653304] |
| cpdiag6 | [1, -5, 13, 343, -16871, 795379, -45626075] |
