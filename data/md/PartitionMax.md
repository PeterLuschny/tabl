# PartitionMax
['A008284', 'A058398', 'A072233']

PartitionMax Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 2] |
| trow3 | [0, 1, 2, 3] |
| trow4 | [0, 1, 3, 4, 5] |
| trow5 | [0, 1, 3, 5, 6, 7] |
| trow6 | [0, 1, 4, 7, 9, 10, 11] |

PartitionMax Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 3, 4, 5, 0, 1, 3, 5, 6, 7, 0, 1, 4, 7, 9, 10, 11] |
| rev      | [1, 1, 0, 2, 1, 0, 3, 2, 1, 0, 5, 4, 3, 1, 0, 7, 6, 5, 3, 1, 0, 11, 10, 9, 7, 4, 1, 0] |
| accu     | [1, 0, 1, 0, 1, 3, 0, 1, 3, 6, 0, 1, 4, 8, 13, 0, 1, 4, 9, 15, 22, 0, 1, 5, 12, 21, 31, 42] |
| revaccu  | [1, 1, 0, 3, 1, 0, 6, 3, 1, 0, 13, 8, 4, 1, 0, 22, 15, 9, 4, 1, 0, 42, 31, 21, 12, 5, 1, 0] |
| accurev  | [1, 1, 1, 2, 3, 3, 3, 5, 6, 6, 5, 9, 12, 13, 13, 7, 13, 18, 21, 22, 22, 11, 21, 30, 37, 41, 42, 42] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2] |

PartitionMax Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 6, 13, 22, 42] |
| evensum   | [1, 0, 2, 2, 8, 9, 24] |
| oddsum    | [0, 1, 1, 4, 5, 13, 18] |
| altsum    | [1, -1, 1, -2, 3, -4, 6] |
| diagsum   | [1, 0, 1, 1, 3, 3] |
| accusum   | [1, 1, 4, 10, 26, 51, 112] |
| revaccusum | [1, 2, 8, 20, 52, 103, 224] |

PartitionMax Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 2, 3, 5, 7, 11]|
| rdiag1 | [0, 1, 2, 4, 6, 10, 14]|
| rdiag2 | [0, 1, 3, 5, 9, 13, 20]|
| rdiag3 | [0, 1, 3, 7, 11, 18, 26]|
| rdiag4 | [0, 1, 4, 8, 15, 23, 35]|
| rdiag5 | [0, 1, 4, 10, 18, 30, 44]|
| rdiag6 | [0, 1, 5, 12, 23, 37, 58]|

PartitionMax Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag2 | [2, 2, 3, 3, 4, 4, 5] |
| cdiag3 | [3, 4, 5, 7, 8, 10, 12] |
| cdiag4 | [5, 6, 9, 11, 15, 18, 23] |
| cdiag5 | [7, 10, 13, 18, 23, 30, 37] |
| cdiag6 | [11, 14, 20, 26, 35, 44, 58] |

PartitionMax Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 3, 10, 21, 36, 55, 78] |
| rpdiag3 | [0, 6, 34, 102, 228, 430, 726] |
| rpdiag4 | [0, 13, 126, 543, 1588, 3705, 7458] |
| rpdiag5 | [0, 22, 374, 2352, 9076, 26330, 63402] |
| rpdiag6 | [0, 42, 1242, 11406, 58116, 209730, 604302] |

PartitionMax Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 3, 6, 13, 22, 42] |
| cpdiag2 | [1, 2, 10, 34, 126, 374, 1242] |
| cpdiag3 | [1, 3, 21, 102, 543, 2352, 11406] |
| cpdiag4 | [1, 4, 36, 228, 1588, 9076, 58116] |
| cpdiag5 | [1, 5, 55, 430, 3705, 26330, 209730] |
| cpdiag6 | [1, 6, 78, 726, 7458, 63402, 604302] |

# PartitionMaxRev
True

PartitionMaxRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [2, 1, 0] |
| trow3 | [3, 2, 1, 0] |
| trow4 | [5, 4, 3, 1, 0] |
| trow5 | [7, 6, 5, 3, 1, 0] |
| trow6 | [11, 10, 9, 7, 4, 1, 0] |

PartitionMaxRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 2, 1, 0, 3, 2, 1, 0, 5, 4, 3, 1, 0, 7, 6, 5, 3, 1, 0, 11, 10, 9, 7, 4, 1, 0] |
| rev      | [1, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 3, 4, 5, 0, 1, 3, 5, 6, 7, 0, 1, 4, 7, 9, 10, 11] |
| accu     | [1, 1, 1, 2, 3, 3, 3, 5, 6, 6, 5, 9, 12, 13, 13, 7, 13, 18, 21, 22, 22, 11, 21, 30, 37, 41, 42, 42] |
| revaccu  | [1, 1, 1, 3, 3, 2, 6, 6, 5, 3, 13, 13, 12, 9, 5, 22, 22, 21, 18, 13, 7, 42, 42, 41, 37, 30, 21, 11] |
| accurev  | [1, 0, 1, 0, 1, 3, 0, 1, 3, 6, 0, 1, 4, 8, 13, 0, 1, 4, 9, 15, 22, 0, 1, 5, 12, 21, 31, 42] |
| diag     | [1, 1, 2, 0, 3, 1, 5, 2, 0, 7, 4, 1] |

PartitionMaxRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 6, 13, 22, 42] |
| evensum   | [1, 1, 2, 4, 8, 13, 24] |
| oddsum    | [0, 0, 1, 2, 5, 9, 18] |
| altsum    | [1, 1, 1, 2, 3, 4, 6] |
| diagsum   | [1, 1, 2, 4, 7, 12] |
| accusum   | [1, 2, 8, 20, 52, 103, 224] |
| revaccusum | [1, 1, 4, 10, 26, 51, 112] |

PartitionMaxRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag2 | [2, 2, 3, 3, 4, 4, 5]|
| rdiag3 | [3, 4, 5, 7, 8, 10, 12]|
| rdiag4 | [5, 6, 9, 11, 15, 18, 23]|
| rdiag5 | [7, 10, 13, 18, 23, 30, 37]|
| rdiag6 | [11, 14, 20, 26, 35, 44, 58]|

PartitionMaxRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 2, 3, 5, 7, 11] |
| cdiag1 | [0, 1, 2, 4, 6, 10, 14] |
| cdiag2 | [0, 1, 3, 5, 9, 13, 20] |
| cdiag3 | [0, 1, 3, 7, 11, 18, 26] |
| cdiag4 | [0, 1, 4, 8, 15, 23, 35] |
| cdiag5 | [0, 1, 4, 10, 18, 30, 44] |
| cdiag6 | [0, 1, 5, 12, 23, 37, 58] |

PartitionMaxRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [2, 3, 4, 5, 6, 7, 8] |
| rpdiag3 | [3, 6, 11, 18, 27, 38, 51] |
| rpdiag4 | [5, 13, 33, 71, 133, 225, 353] |
| rpdiag5 | [7, 22, 79, 232, 559, 1162, 2167] |
| rpdiag6 | [11, 42, 219, 878, 2691, 6786, 14867] |

PartitionMaxRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 2, 3, 5, 7, 11] |
| cpdiag1 | [1, 1, 3, 6, 13, 22, 42] |
| cpdiag2 | [1, 1, 4, 11, 33, 79, 219] |
| cpdiag3 | [1, 1, 5, 18, 71, 232, 878] |
| cpdiag4 | [1, 1, 6, 27, 133, 559, 2691] |
| cpdiag5 | [1, 1, 7, 38, 225, 1162, 6786] |
| cpdiag6 | [1, 1, 8, 51, 353, 2167, 14867] |
