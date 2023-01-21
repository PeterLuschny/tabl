# Baxter
['A359363', 'A056939']

Baxter Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 1] |
| trow3 | [0, 1, 4, 1] |
| trow4 | [0, 1, 10, 10, 1] |
| trow5 | [0, 1, 20, 50, 20, 1] |
| trow6 | [0, 1, 35, 175, 175, 35, 1] |

Baxter Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 1, 0, 1, 4, 1, 0, 1, 10, 10, 1, 0, 1, 20, 50, 20, 1, 0, 1, 35, 175, 175, 35, 1] |
| rev      | [1, 1, 0, 1, 1, 0, 1, 4, 1, 0, 1, 10, 10, 1, 0, 1, 20, 50, 20, 1, 0, 1, 35, 175, 175, 35, 1, 0] |
| accu     | [1, 0, 1, 0, 1, 2, 0, 1, 5, 6, 0, 1, 11, 21, 22, 0, 1, 21, 71, 91, 92, 0, 1, 36, 211, 386, 421, 422] |
| revaccu  | [1, 1, 0, 2, 1, 0, 6, 5, 1, 0, 22, 21, 11, 1, 0, 92, 91, 71, 21, 1, 0, 422, 421, 386, 211, 36, 1, 0] |
| accurev  | [1, 1, 1, 1, 2, 2, 1, 5, 6, 6, 1, 11, 21, 22, 22, 1, 21, 71, 91, 92, 92, 1, 36, 211, 386, 421, 422, 422] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 4] |

Baxter Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 6, 22, 92, 422] |
| evensum   | [1, 0, 1, 4, 11, 40, 211] |
| oddsum    | [0, 1, 1, 2, 11, 52, 211] |
| altsum    | [1, -1, 0, 2, 0, -12, 0] |
| diagsum   | [1, 0, 1, 1, 2, 5] |
| accusum   | [1, 1, 3, 12, 55, 276, 1477] |
| revaccusum | [1, 2, 5, 18, 77, 368, 1899] |

Baxter Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [0, 1, 4, 10, 20, 35, 56]|
| rdiag2 | [0, 1, 10, 50, 175, 490, 1176]|
| rdiag3 | [0, 1, 20, 175, 980, 4116, 14112]|
| rdiag4 | [0, 1, 35, 490, 4116, 24696, 116424]|
| rdiag5 | [0, 1, 56, 1176, 14112, 116424, 731808]|
| rdiag6 | [0, 1, 84, 2520, 41580, 457380, 3737448]|

Baxter Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag2 | [1, 4, 10, 20, 35, 56, 84] |
| cdiag3 | [1, 10, 50, 175, 490, 1176, 2520] |
| cdiag4 | [1, 20, 175, 980, 4116, 14112, 41580] |
| cdiag5 | [1, 35, 490, 4116, 24696, 116424, 457380] |
| cdiag6 | [1, 56, 1176, 14112, 116424, 731808, 3737448] |

Baxter Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 2, 6, 12, 20, 30, 42] |
| rpdiag3 | [0, 6, 26, 66, 132, 230, 366] |
| rpdiag4 | [0, 22, 138, 444, 1060, 2130, 3822] |
| rpdiag5 | [0, 92, 834, 3396, 9668, 22380, 45222] |
| rpdiag6 | [0, 422, 5526, 28452, 96500, 257130, 584682] |

Baxter Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 2, 6, 22, 92, 422] |
| cpdiag2 | [1, 2, 6, 26, 138, 834, 5526] |
| cpdiag3 | [1, 3, 12, 66, 444, 3396, 28452] |
| cpdiag4 | [1, 4, 20, 132, 1060, 9668, 96500] |
| cpdiag5 | [1, 5, 30, 230, 2130, 22380, 257130] |
| cpdiag6 | [1, 6, 42, 366, 3822, 45222, 584682] |

# BaxterRev
True

BaxterRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, 1, 0] |
| trow3 | [1, 4, 1, 0] |
| trow4 | [1, 10, 10, 1, 0] |
| trow5 | [1, 20, 50, 20, 1, 0] |
| trow6 | [1, 35, 175, 175, 35, 1, 0] |

BaxterRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, 1, 0, 1, 4, 1, 0, 1, 10, 10, 1, 0, 1, 20, 50, 20, 1, 0, 1, 35, 175, 175, 35, 1, 0] |
| rev      | [1, 0, 1, 0, 1, 1, 0, 1, 4, 1, 0, 1, 10, 10, 1, 0, 1, 20, 50, 20, 1, 0, 1, 35, 175, 175, 35, 1] |
| accu     | [1, 1, 1, 1, 2, 2, 1, 5, 6, 6, 1, 11, 21, 22, 22, 1, 21, 71, 91, 92, 92, 1, 36, 211, 386, 421, 422, 422] |
| revaccu  | [1, 1, 1, 2, 2, 1, 6, 6, 5, 1, 22, 22, 21, 11, 1, 92, 92, 91, 71, 21, 1, 422, 422, 421, 386, 211, 36, 1] |
| accurev  | [1, 0, 1, 0, 1, 2, 0, 1, 5, 6, 0, 1, 11, 21, 22, 0, 1, 21, 71, 91, 92, 0, 1, 36, 211, 386, 421, 422] |
| diag     | [1, 1, 1, 0, 1, 1, 1, 4, 0, 1, 10, 1] |

BaxterRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 6, 22, 92, 422] |
| evensum   | [1, 1, 1, 2, 11, 52, 211] |
| oddsum    | [0, 0, 1, 4, 11, 40, 211] |
| altsum    | [1, 1, 0, -2, 0, 12, 0] |
| diagsum   | [1, 1, 1, 2, 5, 12] |
| accusum   | [1, 2, 5, 18, 77, 368, 1899] |
| revaccusum | [1, 1, 3, 12, 55, 276, 1477] |

BaxterRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag2 | [1, 4, 10, 20, 35, 56, 84]|
| rdiag3 | [1, 10, 50, 175, 490, 1176, 2520]|
| rdiag4 | [1, 20, 175, 980, 4116, 14112, 41580]|
| rdiag5 | [1, 35, 490, 4116, 24696, 116424, 457380]|
| rdiag6 | [1, 56, 1176, 14112, 116424, 731808, 3737448]|

BaxterRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [0, 1, 4, 10, 20, 35, 56] |
| cdiag2 | [0, 1, 10, 50, 175, 490, 1176] |
| cdiag3 | [0, 1, 20, 175, 980, 4116, 14112] |
| cdiag4 | [0, 1, 35, 490, 4116, 24696, 116424] |
| cdiag5 | [0, 1, 56, 1176, 14112, 116424, 731808] |
| cdiag6 | [0, 1, 84, 2520, 41580, 457380, 3737448] |

BaxterRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag3 | [1, 6, 13, 22, 33, 46, 61] |
| rpdiag4 | [1, 22, 69, 148, 265, 426, 637] |
| rpdiag5 | [1, 92, 417, 1132, 2417, 4476, 7537] |
| rpdiag6 | [1, 422, 2763, 9484, 24125, 51426, 97447] |

BaxterRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 1, 2, 6, 22, 92, 422] |
| cpdiag2 | [1, 1, 3, 13, 69, 417, 2763] |
| cpdiag3 | [1, 1, 4, 22, 148, 1132, 9484] |
| cpdiag4 | [1, 1, 5, 33, 265, 2417, 24125] |
| cpdiag5 | [1, 1, 6, 46, 426, 4476, 51426] |
| cpdiag6 | [1, 1, 7, 61, 637, 7537, 97447] |
