# FussCatalan
['A030237', 'A054445', 'A355173']

FussCatalan Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 2] |
| trow3 | [0, 1, 3, 5] |
| trow4 | [0, 1, 4, 9, 14] |
| trow5 | [0, 1, 5, 14, 28, 42] |
| trow6 | [0, 1, 6, 20, 48, 90, 132] |

FussCatalan Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 2, 0, 1, 3, 5, 0, 1, 4, 9, 14, 0, 1, 5, 14, 28, 42, 0, 1, 6, 20, 48, 90, 132] |
| rev      | [1, 1, 0, 2, 1, 0, 5, 3, 1, 0, 14, 9, 4, 1, 0, 42, 28, 14, 5, 1, 0, 132, 90, 48, 20, 6, 1, 0] |
| accu     | [1, 0, 1, 0, 1, 3, 0, 1, 4, 9, 0, 1, 5, 14, 28, 0, 1, 6, 20, 48, 90, 0, 1, 7, 27, 75, 165, 297] |
| revaccu  | [1, 1, 0, 3, 1, 0, 9, 4, 1, 0, 28, 14, 5, 1, 0, 90, 48, 20, 6, 1, 0, 297, 165, 75, 27, 7, 1, 0] |
| accurev  | [1, 1, 1, 2, 3, 3, 5, 8, 9, 9, 14, 23, 27, 28, 28, 42, 70, 84, 89, 90, 90, 132, 222, 270, 290, 296, 297, 297] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 3] |

FussCatalan Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 9, 28, 90, 297] |
| evensum   | [1, 0, 2, 3, 18, 33, 186] |
| oddsum    | [0, 1, 1, 6, 10, 57, 111] |
| altsum    | [1, -1, 1, -3, 8, -24, 75] |
| diagsum   | [1, 0, 1, 1, 3, 4] |
| accusum   | [1, 1, 4, 14, 48, 165, 572] |
| revaccusum | [1, 2, 8, 31, 120, 465, 1804] |

FussCatalan Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 2, 5, 14, 42, 132]|
| rdiag1 | [0, 1, 3, 9, 28, 90, 297]|
| rdiag2 | [0, 1, 4, 14, 48, 165, 572]|
| rdiag3 | [0, 1, 5, 20, 75, 275, 1001]|
| rdiag4 | [0, 1, 6, 27, 110, 429, 1638]|
| rdiag5 | [0, 1, 7, 35, 154, 637, 2548]|
| rdiag6 | [0, 1, 8, 44, 208, 910, 3808]|

FussCatalan Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag2 | [2, 3, 4, 5, 6, 7, 8] |
| cdiag3 | [5, 9, 14, 20, 27, 35, 44] |
| cdiag4 | [14, 28, 48, 75, 110, 154, 208] |
| cdiag5 | [42, 90, 165, 275, 429, 637, 910] |
| cdiag6 | [132, 297, 572, 1001, 1638, 2548, 3808] |

FussCatalan Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 3, 10, 21, 36, 55, 78] |
| rpdiag3 | [0, 9, 54, 165, 372, 705, 1194] |
| rpdiag4 | [0, 28, 314, 1416, 4228, 9980, 20238] |
| rpdiag5 | [0, 90, 1926, 12900, 51156, 150630, 366090] |
| rpdiag6 | [0, 297, 12282, 122583, 646500, 2376405, 6925182] |

FussCatalan Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 3, 9, 28, 90, 297] |
| cpdiag2 | [1, 2, 10, 54, 314, 1926, 12282] |
| cpdiag3 | [1, 3, 21, 165, 1416, 12900, 122583] |
| cpdiag4 | [1, 4, 36, 372, 4228, 51156, 646500] |
| cpdiag5 | [1, 5, 55, 705, 9980, 150630, 2376405] |
| cpdiag6 | [1, 6, 78, 1194, 20238, 366090, 6925182] |

# FussCatalanRev
True

FussCatalanRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [2, 1, 0] |
| trow3 | [5, 3, 1, 0] |
| trow4 | [14, 9, 4, 1, 0] |
| trow5 | [42, 28, 14, 5, 1, 0] |
| trow6 | [132, 90, 48, 20, 6, 1, 0] |

FussCatalanRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 2, 1, 0, 5, 3, 1, 0, 14, 9, 4, 1, 0, 42, 28, 14, 5, 1, 0, 132, 90, 48, 20, 6, 1, 0] |
| rev      | [1, 0, 1, 0, 1, 2, 0, 1, 3, 5, 0, 1, 4, 9, 14, 0, 1, 5, 14, 28, 42, 0, 1, 6, 20, 48, 90, 132] |
| accu     | [1, 1, 1, 2, 3, 3, 5, 8, 9, 9, 14, 23, 27, 28, 28, 42, 70, 84, 89, 90, 90, 132, 222, 270, 290, 296, 297, 297] |
| revaccu  | [1, 1, 1, 3, 3, 2, 9, 9, 8, 5, 28, 28, 27, 23, 14, 90, 90, 89, 84, 70, 42, 297, 297, 296, 290, 270, 222, 132] |
| accurev  | [1, 0, 1, 0, 1, 3, 0, 1, 4, 9, 0, 1, 5, 14, 28, 0, 1, 6, 20, 48, 90, 0, 1, 7, 27, 75, 165, 297] |
| diag     | [1, 1, 2, 0, 5, 1, 14, 3, 0, 42, 9, 1] |

FussCatalanRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 9, 28, 90, 297] |
| evensum   | [1, 1, 2, 6, 18, 57, 186] |
| oddsum    | [0, 0, 1, 3, 10, 33, 111] |
| altsum    | [1, 1, 1, 3, 8, 24, 75] |
| diagsum   | [1, 1, 2, 6, 17, 52] |
| accusum   | [1, 2, 8, 31, 120, 465, 1804] |
| revaccusum | [1, 1, 4, 14, 48, 165, 572] |

FussCatalanRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag2 | [2, 3, 4, 5, 6, 7, 8]|
| rdiag3 | [5, 9, 14, 20, 27, 35, 44]|
| rdiag4 | [14, 28, 48, 75, 110, 154, 208]|
| rdiag5 | [42, 90, 165, 275, 429, 637, 910]|
| rdiag6 | [132, 297, 572, 1001, 1638, 2548, 3808]|

FussCatalanRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 2, 5, 14, 42, 132] |
| cdiag1 | [0, 1, 3, 9, 28, 90, 297] |
| cdiag2 | [0, 1, 4, 14, 48, 165, 572] |
| cdiag3 | [0, 1, 5, 20, 75, 275, 1001] |
| cdiag4 | [0, 1, 6, 27, 110, 429, 1638] |
| cdiag5 | [0, 1, 7, 35, 154, 637, 2548] |
| cdiag6 | [0, 1, 8, 44, 208, 910, 3808] |

FussCatalanRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [2, 3, 4, 5, 6, 7, 8] |
| rpdiag3 | [5, 9, 15, 23, 33, 45, 59] |
| rpdiag4 | [14, 28, 56, 104, 178, 284, 428] |
| rpdiag5 | [42, 90, 210, 468, 954, 1782, 3090] |
| rpdiag6 | [132, 297, 792, 2103, 5100, 11157, 22272] |

FussCatalanRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 2, 5, 14, 42, 132] |
| cpdiag1 | [1, 1, 3, 9, 28, 90, 297] |
| cpdiag2 | [1, 1, 4, 15, 56, 210, 792] |
| cpdiag3 | [1, 1, 5, 23, 104, 468, 2103] |
| cpdiag4 | [1, 1, 6, 33, 178, 954, 5100] |
| cpdiag5 | [1, 1, 7, 45, 284, 1782, 11157] |
| cpdiag6 | [1, 1, 8, 59, 428, 3090, 22272] |
