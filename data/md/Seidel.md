# Seidel
['A008281', 'A008282', 'A010094']

Seidel Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 1] |
| trow3 | [0, 1, 2, 2] |
| trow4 | [0, 2, 4, 5, 5] |
| trow5 | [0, 5, 10, 14, 16, 16] |
| trow6 | [0, 16, 32, 46, 56, 61, 61] |

Seidel Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 1, 0, 1, 2, 2, 0, 2, 4, 5, 5, 0, 5, 10, 14, 16, 16, 0, 16, 32, 46, 56, 61, 61] |
| rev      | [1, 1, 0, 1, 1, 0, 2, 2, 1, 0, 5, 5, 4, 2, 0, 16, 16, 14, 10, 5, 0, 61, 61, 56, 46, 32, 16, 0] |
| accu     | [1, 0, 1, 0, 1, 2, 0, 1, 3, 5, 0, 2, 6, 11, 16, 0, 5, 15, 29, 45, 61, 0, 16, 48, 94, 150, 211, 272] |
| revaccu  | [1, 1, 0, 2, 1, 0, 5, 3, 1, 0, 16, 11, 6, 2, 0, 61, 45, 29, 15, 5, 0, 272, 211, 150, 94, 48, 16, 0] |
| accurev  | [1, 1, 1, 1, 2, 2, 2, 4, 5, 5, 5, 10, 14, 16, 16, 16, 32, 46, 56, 61, 61, 61, 122, 178, 224, 256, 272, 272] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 2, 2] |

Seidel Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 5, 16, 61, 272] |
| evensum   | [1, 0, 1, 2, 9, 26, 149] |
| oddsum    | [0, 1, 1, 3, 7, 35, 123] |
| altsum    | [1, -1, 0, -1, 2, -9, 26] |
| diagsum   | [1, 0, 1, 1, 2, 4] |
| accusum   | [1, 1, 3, 9, 35, 155, 791] |
| revaccusum | [1, 2, 5, 16, 61, 272, 1385] |

Seidel Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 2, 5, 16, 61]|
| rdiag1 | [0, 1, 2, 5, 16, 61, 272]|
| rdiag2 | [0, 1, 4, 14, 56, 256, 1324]|
| rdiag3 | [0, 2, 10, 46, 224, 1202, 7120]|
| rdiag4 | [0, 5, 32, 178, 1024, 6320, 42272]|
| rdiag5 | [0, 16, 122, 800, 5296, 36976, 275792]|
| rdiag6 | [0, 61, 544, 4094, 30656, 238816, 1965664]|

Seidel Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 2, 5, 16, 61] |
| cdiag2 | [1, 2, 4, 10, 32, 122, 544] |
| cdiag3 | [2, 5, 14, 46, 178, 800, 4094] |
| cdiag4 | [5, 16, 56, 224, 1024, 5296, 30656] |
| cdiag5 | [16, 61, 256, 1202, 6320, 36976, 238816] |
| cdiag6 | [61, 272, 1324, 7120, 42272, 275792, 1965664] |

Seidel Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 2, 6, 12, 20, 30, 42] |
| rpdiag3 | [0, 5, 26, 75, 164, 305, 510] |
| rpdiag4 | [0, 16, 140, 582, 1672, 3860, 7716] |
| rpdiag5 | [0, 61, 930, 5667, 21556, 62025, 148566] |
| rpdiag6 | [0, 272, 7280, 65406, 330176, 1185380, 3404112] |

Seidel Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 2, 5, 16, 61, 272] |
| cpdiag2 | [1, 2, 6, 26, 140, 930, 7280] |
| cpdiag3 | [1, 3, 12, 75, 582, 5667, 65406] |
| cpdiag4 | [1, 4, 20, 164, 1672, 21556, 330176] |
| cpdiag5 | [1, 5, 30, 305, 3860, 62025, 1185380] |
| cpdiag6 | [1, 6, 42, 510, 7716, 148566, 3404112] |

# SeidelRev
True

SeidelRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, 1, 0] |
| trow3 | [2, 2, 1, 0] |
| trow4 | [5, 5, 4, 2, 0] |
| trow5 | [16, 16, 14, 10, 5, 0] |
| trow6 | [61, 61, 56, 46, 32, 16, 0] |

SeidelRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, 1, 0, 2, 2, 1, 0, 5, 5, 4, 2, 0, 16, 16, 14, 10, 5, 0, 61, 61, 56, 46, 32, 16, 0] |
| rev      | [1, 0, 1, 0, 1, 1, 0, 1, 2, 2, 0, 2, 4, 5, 5, 0, 5, 10, 14, 16, 16, 0, 16, 32, 46, 56, 61, 61] |
| accu     | [1, 1, 1, 1, 2, 2, 2, 4, 5, 5, 5, 10, 14, 16, 16, 16, 32, 46, 56, 61, 61, 61, 122, 178, 224, 256, 272, 272] |
| revaccu  | [1, 1, 1, 2, 2, 1, 5, 5, 4, 2, 16, 16, 14, 10, 5, 61, 61, 56, 46, 32, 16, 272, 272, 256, 224, 178, 122, 61] |
| accurev  | [1, 0, 1, 0, 1, 2, 0, 1, 3, 5, 0, 2, 6, 11, 16, 0, 5, 15, 29, 45, 61, 0, 16, 48, 94, 150, 211, 272] |
| diag     | [1, 1, 1, 0, 2, 1, 5, 2, 0, 16, 5, 1] |

SeidelRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 5, 16, 61, 272] |
| evensum   | [1, 1, 1, 3, 9, 35, 149] |
| oddsum    | [0, 0, 1, 2, 7, 26, 123] |
| altsum    | [1, 1, 0, 1, 2, 9, 26] |
| diagsum   | [1, 1, 1, 3, 7, 22] |
| accusum   | [1, 2, 5, 16, 61, 272, 1385] |
| revaccusum | [1, 1, 3, 9, 35, 155, 791] |

SeidelRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 2, 5, 16, 61]|
| rdiag2 | [1, 2, 4, 10, 32, 122, 544]|
| rdiag3 | [2, 5, 14, 46, 178, 800, 4094]|
| rdiag4 | [5, 16, 56, 224, 1024, 5296, 30656]|
| rdiag5 | [16, 61, 256, 1202, 6320, 36976, 238816]|
| rdiag6 | [61, 272, 1324, 7120, 42272, 275792, 1965664]|

SeidelRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 2, 5, 16, 61] |
| cdiag1 | [0, 1, 2, 5, 16, 61, 272] |
| cdiag2 | [0, 1, 4, 14, 56, 256, 1324] |
| cdiag3 | [0, 2, 10, 46, 224, 1202, 7120] |
| cdiag4 | [0, 5, 32, 178, 1024, 6320, 42272] |
| cdiag5 | [0, 16, 122, 800, 5296, 36976, 275792] |
| cdiag6 | [0, 61, 544, 4094, 30656, 238816, 1965664] |

SeidelRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag3 | [2, 5, 10, 17, 26, 37, 50] |
| rpdiag4 | [5, 16, 47, 110, 217, 380, 611] |
| rpdiag5 | [16, 61, 264, 865, 2224, 4821, 9256] |
| rpdiag6 | [61, 272, 1799, 8470, 28721, 77516, 178267] |

SeidelRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 2, 5, 16, 61] |
| cpdiag1 | [1, 1, 2, 5, 16, 61, 272] |
| cpdiag2 | [1, 1, 3, 10, 47, 264, 1799] |
| cpdiag3 | [1, 1, 4, 17, 110, 865, 8470] |
| cpdiag4 | [1, 1, 5, 26, 217, 2224, 28721] |
| cpdiag5 | [1, 1, 6, 37, 380, 4821, 77516] |
| cpdiag6 | [1, 1, 7, 50, 611, 9256, 178267] |
