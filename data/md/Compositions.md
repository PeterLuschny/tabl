# Compositions
['A048004']

Compositions Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 1] |
| trow3 | [0, 1, 2, 1] |
| trow4 | [0, 1, 4, 2, 1] |
| trow5 | [0, 1, 7, 5, 2, 1] |
| trow6 | [0, 1, 12, 11, 5, 2, 1] |

Compositions Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 4, 2, 1, 0, 1, 7, 5, 2, 1, 0, 1, 12, 11, 5, 2, 1] |
| rev      | [1, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 4, 1, 0, 1, 2, 5, 7, 1, 0, 1, 2, 5, 11, 12, 1, 0] |
| accu     | [1, 0, 1, 0, 1, 2, 0, 1, 3, 4, 0, 1, 5, 7, 8, 0, 1, 8, 13, 15, 16, 0, 1, 13, 24, 29, 31, 32] |
| revaccu  | [1, 1, 0, 2, 1, 0, 4, 3, 1, 0, 8, 7, 5, 1, 0, 16, 15, 13, 8, 1, 0, 32, 31, 29, 24, 13, 1, 0] |
| accurev  | [1, 1, 1, 1, 2, 2, 1, 3, 4, 4, 1, 3, 7, 8, 8, 1, 3, 8, 15, 16, 16, 1, 3, 8, 19, 31, 32, 32] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 2] |

Compositions Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 4, 8, 16, 32] |
| evensum   | [1, 0, 1, 2, 5, 9, 18] |
| oddsum    | [0, 1, 1, 2, 3, 7, 14] |
| altsum    | [1, -1, 0, 0, 2, 2, 4] |
| diagsum   | [1, 0, 1, 1, 2, 3] |
| accusum   | [1, 1, 3, 8, 21, 53, 130] |
| revaccusum | [1, 2, 5, 12, 27, 59, 126] |

Compositions Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [0, 1, 2, 2, 2, 2, 2]|
| rdiag2 | [0, 1, 4, 5, 5, 5, 5]|
| rdiag3 | [0, 1, 7, 11, 12, 12, 12]|
| rdiag4 | [0, 1, 12, 23, 27, 28, 28]|
| rdiag5 | [0, 1, 20, 47, 59, 63, 64]|
| rdiag6 | [0, 1, 33, 94, 127, 139, 143]|

Compositions Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag2 | [1, 2, 4, 7, 12, 20, 33] |
| cdiag3 | [1, 2, 5, 11, 23, 47, 94] |
| cdiag4 | [1, 2, 5, 12, 27, 59, 127] |
| cdiag5 | [1, 2, 5, 12, 28, 63, 139] |
| cdiag6 | [1, 2, 5, 12, 28, 64, 143] |

Compositions Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 2, 6, 12, 20, 30, 42] |
| rpdiag3 | [0, 4, 18, 48, 100, 180, 294] |
| rpdiag4 | [0, 8, 50, 174, 452, 980, 1878] |
| rpdiag5 | [0, 16, 134, 606, 1972, 5180, 11706] |
| rpdiag6 | [0, 32, 346, 2028, 8324, 26680, 71502] |

Compositions Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 2, 4, 8, 16, 32] |
| cpdiag2 | [1, 2, 6, 18, 50, 134, 346] |
| cpdiag3 | [1, 3, 12, 48, 174, 606, 2028] |
| cpdiag4 | [1, 4, 20, 100, 452, 1972, 8324] |
| cpdiag5 | [1, 5, 30, 180, 980, 5180, 26680] |
| cpdiag6 | [1, 6, 42, 294, 1878, 11706, 71502] |

# CompositionsInv
True

CompositionsInv Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, -1, 1] |
| trow3 | [0, 1, -2, 1] |
| trow4 | [0, 1, 0, -2, 1] |
| trow5 | [0, -1, 3, -1, -2, 1] |
| trow6 | [0, -3, 4, 1, -1, -2, 1] |

CompositionsInv Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, -1, 1, 0, 1, -2, 1, 0, 1, 0, -2, 1, 0, -1, 3, -1, -2, 1, 0, -3, 4, 1, -1, -2, 1] |
| rev      | [1, 1, 0, 1, -1, 0, 1, -2, 1, 0, 1, -2, 0, 1, 0, 1, -2, -1, 3, -1, 0, 1, -2, -1, 1, 4, -3, 0] |
| accu     | [1, 0, 1, 0, -1, 0, 0, 1, -1, 0, 0, 1, 1, -1, 0, 0, -1, 2, 1, -1, 0, 0, -3, 1, 2, 1, -1, 0] |
| revaccu  | [1, 1, 0, 0, -1, 0, 0, -1, 1, 0, 0, -1, 1, 1, 0, 0, -1, 1, 2, -1, 0, 0, -1, 1, 2, 1, -3, 0] |
| accurev  | [1, 1, 1, 1, 0, 0, 1, -1, 0, 0, 1, -1, -1, 0, 0, 1, -1, -2, 1, 0, 0, 1, -1, -2, -1, 3, 0, 0] |
| diag     | [1, 0, 0, 1, 0, -1, 0, 1, 1, 0, 1, -2] |

CompositionsInv Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 0, 0, 0, 0, 0] |
| evensum   | [1, 0, 1, -2, 1, 1, 4] |
| oddsum    | [0, 1, -1, 2, -1, -1, -4] |
| altsum    | [1, -1, 2, -4, 2, 2, 8] |
| diagsum   | [1, 0, 1, -1, 2, -1] |
| accusum   | [1, 1, -1, 0, 1, 1, 0] |
| revaccusum | [1, 2, 1, 0, -1, -1, 0] |

CompositionsInv Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [0, -1, -2, -2, -2, -2, -2]|
| rdiag2 | [0, 1, 0, -1, -1, -1, -1]|
| rdiag3 | [0, 1, 3, 1, 0, 0, 0]|
| rdiag4 | [0, -1, 4, 4, 2, 1, 1]|
| rdiag5 | [0, -3, 3, 6, 5, 3, 2]|
| rdiag6 | [0, -5, -1, 8, 7, 6, 4]|

CompositionsInv Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, -1, 1, 1, -1, -3, -5] |
| cdiag2 | [1, -2, 0, 3, 4, 3, -1] |
| cdiag3 | [1, -2, -1, 1, 4, 6, 8] |
| cdiag4 | [1, -2, -1, 0, 2, 5, 7] |
| cdiag5 | [1, -2, -1, 0, 1, 3, 6] |
| cdiag6 | [1, -2, -1, 0, 1, 2, 4] |

CompositionsInv Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 0, 2, 6, 12, 20, 30] |
| rpdiag3 | [0, 0, 2, 12, 36, 80, 150] |
| rpdiag4 | [0, 0, 2, 30, 132, 380, 870] |
| rpdiag5 | [0, 0, 2, 78, 492, 1820, 5070] |
| rpdiag6 | [0, 0, 2, 216, 1908, 8960, 30150] |

CompositionsInv Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 0, 0, 0, 0, 0] |
| cpdiag2 | [1, 2, 2, 2, 2, 2, 2] |
| cpdiag3 | [1, 3, 6, 12, 30, 78, 216] |
| cpdiag4 | [1, 4, 12, 36, 132, 492, 1908] |
| cpdiag5 | [1, 5, 20, 80, 380, 1820, 8960] |
| cpdiag6 | [1, 6, 30, 150, 870, 5070, 30150] |

# CompositionsRev
True

CompositionsRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, 1, 0] |
| trow3 | [1, 2, 1, 0] |
| trow4 | [1, 2, 4, 1, 0] |
| trow5 | [1, 2, 5, 7, 1, 0] |
| trow6 | [1, 2, 5, 11, 12, 1, 0] |

CompositionsRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 2, 4, 1, 0, 1, 2, 5, 7, 1, 0, 1, 2, 5, 11, 12, 1, 0] |
| rev      | [1, 0, 1, 0, 1, 1, 0, 1, 2, 1, 0, 1, 4, 2, 1, 0, 1, 7, 5, 2, 1, 0, 1, 12, 11, 5, 2, 1] |
| accu     | [1, 1, 1, 1, 2, 2, 1, 3, 4, 4, 1, 3, 7, 8, 8, 1, 3, 8, 15, 16, 16, 1, 3, 8, 19, 31, 32, 32] |
| revaccu  | [1, 1, 1, 2, 2, 1, 4, 4, 3, 1, 8, 8, 7, 3, 1, 16, 16, 15, 8, 3, 1, 32, 32, 31, 19, 8, 3, 1] |
| accurev  | [1, 0, 1, 0, 1, 2, 0, 1, 3, 4, 0, 1, 5, 7, 8, 0, 1, 8, 13, 15, 16, 0, 1, 13, 24, 29, 31, 32] |
| diag     | [1, 1, 1, 0, 1, 1, 1, 2, 0, 1, 2, 1] |

CompositionsRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 4, 8, 16, 32] |
| evensum   | [1, 1, 1, 2, 5, 7, 18] |
| oddsum    | [0, 0, 1, 2, 3, 9, 14] |
| altsum    | [1, 1, 0, 0, 2, -2, 4] |
| diagsum   | [1, 1, 1, 2, 3, 4] |
| accusum   | [1, 2, 5, 12, 27, 59, 126] |
| revaccusum | [1, 1, 3, 8, 21, 53, 130] |

CompositionsRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag2 | [1, 2, 4, 7, 12, 20, 33]|
| rdiag3 | [1, 2, 5, 11, 23, 47, 94]|
| rdiag4 | [1, 2, 5, 12, 27, 59, 127]|
| rdiag5 | [1, 2, 5, 12, 28, 63, 139]|
| rdiag6 | [1, 2, 5, 12, 28, 64, 143]|

CompositionsRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [0, 1, 2, 2, 2, 2, 2] |
| cdiag2 | [0, 1, 4, 5, 5, 5, 5] |
| cdiag3 | [0, 1, 7, 11, 12, 12, 12] |
| cdiag4 | [0, 1, 12, 23, 27, 28, 28] |
| cdiag5 | [0, 1, 20, 47, 59, 63, 64] |
| cdiag6 | [0, 1, 33, 94, 127, 139, 143] |

CompositionsRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag3 | [1, 4, 9, 16, 25, 36, 49] |
| rpdiag4 | [1, 8, 29, 70, 137, 236, 373] |
| rpdiag5 | [1, 16, 97, 322, 793, 1636, 3001] |
| rpdiag6 | [1, 32, 337, 1564, 4889, 12136, 25897] |

CompositionsRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 1, 2, 4, 8, 16, 32] |
| cpdiag2 | [1, 1, 3, 9, 29, 97, 337] |
| cpdiag3 | [1, 1, 4, 16, 70, 322, 1564] |
| cpdiag4 | [1, 1, 5, 25, 137, 793, 4889] |
| cpdiag5 | [1, 1, 6, 36, 236, 1636, 12136] |
| cpdiag6 | [1, 1, 7, 49, 373, 3001, 25897] |

# CompositionsInvRev
True

CompositionsInvRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, -1, 0] |
| trow3 | [1, -2, 1, 0] |
| trow4 | [1, -2, 0, 1, 0] |
| trow5 | [1, -2, -1, 3, -1, 0] |
| trow6 | [1, -2, -1, 1, 4, -3, 0] |

CompositionsInvRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, -1, 0, 1, -2, 1, 0, 1, -2, 0, 1, 0, 1, -2, -1, 3, -1, 0, 1, -2, -1, 1, 4, -3, 0] |
| rev      | [1, 0, 1, 0, -1, 1, 0, 1, -2, 1, 0, 1, 0, -2, 1, 0, -1, 3, -1, -2, 1, 0, -3, 4, 1, -1, -2, 1] |
| accu     | [1, 1, 1, 1, 0, 0, 1, -1, 0, 0, 1, -1, -1, 0, 0, 1, -1, -2, 1, 0, 0, 1, -1, -2, -1, 3, 0, 0] |
| revaccu  | [1, 1, 1, 0, 0, 1, 0, 0, -1, 1, 0, 0, -1, -1, 1, 0, 0, 1, -2, -1, 1, 0, 0, 3, -1, -2, -1, 1] |
| accurev  | [1, 0, 1, 0, -1, 0, 0, 1, -1, 0, 0, 1, 1, -1, 0, 0, -1, 2, 1, -1, 0, 0, -3, 1, 2, 1, -1, 0] |
| diag     | [1, 1, 1, 0, 1, -1, 1, -2, 0, 1, -2, 1] |

CompositionsInvRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 0, 0, 0, 0, 0] |
| evensum   | [1, 1, 1, 2, 1, -1, 4] |
| oddsum    | [0, 0, -1, -2, -1, 1, -4] |
| altsum    | [1, 1, 2, 4, 2, -2, 8] |
| diagsum   | [1, 1, 1, 0, -1, 0] |
| accusum   | [1, 2, 1, 0, -1, -1, 0] |
| revaccusum | [1, 1, -1, 0, 1, 1, 0] |

CompositionsInvRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, -1, 1, 1, -1, -3, -5]|
| rdiag2 | [1, -2, 0, 3, 4, 3, -1]|
| rdiag3 | [1, -2, -1, 1, 4, 6, 8]|
| rdiag4 | [1, -2, -1, 0, 2, 5, 7]|
| rdiag5 | [1, -2, -1, 0, 1, 3, 6]|
| rdiag6 | [1, -2, -1, 0, 1, 2, 4]|

CompositionsInvRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [0, -1, -2, -2, -2, -2, -2] |
| cdiag2 | [0, 1, 0, -1, -1, -1, -1] |
| cdiag3 | [0, 1, 3, 1, 0, 0, 0] |
| cdiag4 | [0, -1, 4, 4, 2, 1, 1] |
| cdiag5 | [0, -3, 3, 6, 5, 3, 2] |
| cdiag6 | [0, -5, -1, 8, 7, 6, 4] |

CompositionsInvRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 0, -1, -2, -3, -4, -5] |
| rpdiag3 | [1, 0, 1, 4, 9, 16, 25] |
| rpdiag4 | [1, 0, 5, 22, 57, 116, 205] |
| rpdiag5 | [1, 0, 1, -14, -87, -284, -695] |
| rpdiag6 | [1, 0, -31, -392, -2007, -6784, -17975] |

CompositionsInvRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 1, 0, 0, 0, 0, 0] |
| cpdiag2 | [1, 1, -1, 1, 5, 1, -31] |
| cpdiag3 | [1, 1, -2, 4, 22, -14, -392] |
| cpdiag4 | [1, 1, -3, 9, 57, -87, -2007] |
| cpdiag5 | [1, 1, -4, 16, 116, -284, -6784] |
| cpdiag6 | [1, 1, -5, 25, 205, -695, -17975] |
