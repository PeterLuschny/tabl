# CompositionMax
['A126198']

CompositionMax Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [0, 1, 2] |
| trow3 | [0, 1, 3, 4] |
| trow4 | [0, 1, 5, 7, 8] |
| trow5 | [0, 1, 8, 13, 15, 16] |
| trow6 | [0, 1, 13, 24, 29, 31, 32] |

CompositionMax Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 0, 1, 2, 0, 1, 3, 4, 0, 1, 5, 7, 8, 0, 1, 8, 13, 15, 16, 0, 1, 13, 24, 29, 31, 32] |
| rev      | [1, 1, 0, 2, 1, 0, 4, 3, 1, 0, 8, 7, 5, 1, 0, 16, 15, 13, 8, 1, 0, 32, 31, 29, 24, 13, 1, 0] |
| accu     | [1, 0, 1, 0, 1, 3, 0, 1, 4, 8, 0, 1, 6, 13, 21, 0, 1, 9, 22, 37, 53, 0, 1, 14, 38, 67, 98, 130] |
| revaccu  | [1, 1, 0, 3, 1, 0, 8, 4, 1, 0, 21, 13, 6, 1, 0, 53, 37, 22, 9, 1, 0, 130, 98, 67, 38, 14, 1, 0] |
| accurev  | [1, 1, 1, 2, 3, 3, 4, 7, 8, 8, 8, 15, 20, 21, 21, 16, 31, 44, 52, 53, 53, 32, 63, 92, 116, 129, 130, 130] |
| diag     | [1, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 3] |

CompositionMax Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 8, 21, 53, 130] |
| evensum   | [1, 0, 2, 3, 13, 23, 74] |
| oddsum    | [0, 1, 1, 5, 8, 30, 56] |
| altsum    | [1, -1, 1, -2, 5, -7, 18] |
| diagsum   | [1, 0, 1, 1, 3, 4] |
| accusum   | [1, 1, 4, 13, 41, 122, 348] |
| revaccusum | [1, 2, 8, 27, 85, 249, 692] |

CompositionMax Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 2, 4, 8, 16, 32]|
| rdiag1 | [0, 1, 3, 7, 15, 31, 63]|
| rdiag2 | [0, 1, 5, 13, 29, 61, 125]|
| rdiag3 | [0, 1, 8, 24, 56, 120, 248]|
| rdiag4 | [0, 1, 13, 44, 108, 236, 492]|
| rdiag5 | [0, 1, 21, 81, 208, 464, 976]|
| rdiag6 | [0, 1, 34, 149, 401, 912, 1936]|

CompositionMax Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag2 | [2, 3, 5, 8, 13, 21, 34] |
| cdiag3 | [4, 7, 13, 24, 44, 81, 149] |
| cdiag4 | [8, 15, 29, 56, 108, 208, 401] |
| cdiag5 | [16, 31, 61, 120, 236, 464, 912] |
| cdiag6 | [32, 63, 125, 248, 492, 976, 1936] |

CompositionMax Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 3, 10, 21, 36, 55, 78] |
| rpdiag3 | [0, 8, 46, 138, 308, 580, 978] |
| rpdiag4 | [0, 21, 206, 885, 2580, 6005, 12066] |
| rpdiag5 | [0, 53, 890, 5529, 21188, 61205, 146958] |
| rpdiag6 | [0, 130, 3750, 33978, 171988, 618330, 1777290] |

CompositionMax Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [1, 1, 3, 8, 21, 53, 130] |
| cpdiag2 | [1, 2, 10, 46, 206, 890, 3750] |
| cpdiag3 | [1, 3, 21, 138, 885, 5529, 33978] |
| cpdiag4 | [1, 4, 36, 308, 2580, 21188, 171988] |
| cpdiag5 | [1, 5, 55, 580, 6005, 61205, 618330] |
| cpdiag6 | [1, 6, 78, 978, 12066, 146958, 1777290] |

# CompositionMaxRev
True

CompositionMaxRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [2, 1, 0] |
| trow3 | [4, 3, 1, 0] |
| trow4 | [8, 7, 5, 1, 0] |
| trow5 | [16, 15, 13, 8, 1, 0] |
| trow6 | [32, 31, 29, 24, 13, 1, 0] |

CompositionMaxRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 2, 1, 0, 4, 3, 1, 0, 8, 7, 5, 1, 0, 16, 15, 13, 8, 1, 0, 32, 31, 29, 24, 13, 1, 0] |
| rev      | [1, 0, 1, 0, 1, 2, 0, 1, 3, 4, 0, 1, 5, 7, 8, 0, 1, 8, 13, 15, 16, 0, 1, 13, 24, 29, 31, 32] |
| accu     | [1, 1, 1, 2, 3, 3, 4, 7, 8, 8, 8, 15, 20, 21, 21, 16, 31, 44, 52, 53, 53, 32, 63, 92, 116, 129, 130, 130] |
| revaccu  | [1, 1, 1, 3, 3, 2, 8, 8, 7, 4, 21, 21, 20, 15, 8, 53, 53, 52, 44, 31, 16, 130, 130, 129, 116, 92, 63, 32] |
| accurev  | [1, 0, 1, 0, 1, 3, 0, 1, 4, 8, 0, 1, 6, 13, 21, 0, 1, 9, 22, 37, 53, 0, 1, 14, 38, 67, 98, 130] |
| diag     | [1, 1, 2, 0, 4, 1, 8, 3, 0, 16, 7, 1] |

CompositionMaxRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 3, 8, 21, 53, 130] |
| evensum   | [1, 1, 2, 5, 13, 30, 74] |
| oddsum    | [0, 0, 1, 3, 8, 23, 56] |
| altsum    | [1, 1, 1, 2, 5, 7, 18] |
| diagsum   | [1, 1, 2, 5, 11, 24] |
| accusum   | [1, 2, 8, 27, 85, 249, 692] |
| revaccusum | [1, 1, 4, 13, 41, 122, 348] |

CompositionMaxRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag2 | [2, 3, 5, 8, 13, 21, 34]|
| rdiag3 | [4, 7, 13, 24, 44, 81, 149]|
| rdiag4 | [8, 15, 29, 56, 108, 208, 401]|
| rdiag5 | [16, 31, 61, 120, 236, 464, 912]|
| rdiag6 | [32, 63, 125, 248, 492, 976, 1936]|

CompositionMaxRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 2, 4, 8, 16, 32] |
| cdiag1 | [0, 1, 3, 7, 15, 31, 63] |
| cdiag2 | [0, 1, 5, 13, 29, 61, 125] |
| cdiag3 | [0, 1, 8, 24, 56, 120, 248] |
| cdiag4 | [0, 1, 13, 44, 108, 236, 492] |
| cdiag5 | [0, 1, 21, 81, 208, 464, 976] |
| cdiag6 | [0, 1, 34, 149, 401, 912, 1936] |

CompositionMaxRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [2, 3, 4, 5, 6, 7, 8] |
| rpdiag3 | [4, 8, 14, 22, 32, 44, 58] |
| rpdiag4 | [8, 21, 50, 101, 180, 293, 446] |
| rpdiag5 | [16, 53, 178, 475, 1052, 2041, 3598] |
| rpdiag6 | [32, 130, 642, 2330, 6508, 15162, 31070] |

CompositionMaxRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 2, 4, 8, 16, 32] |
| cpdiag1 | [1, 1, 3, 8, 21, 53, 130] |
| cpdiag2 | [1, 1, 4, 14, 50, 178, 642] |
| cpdiag3 | [1, 1, 5, 22, 101, 475, 2330] |
| cpdiag4 | [1, 1, 6, 32, 180, 1052, 6508] |
| cpdiag5 | [1, 1, 7, 44, 293, 2041, 15162] |
| cpdiag6 | [1, 1, 8, 58, 446, 3598, 31070] |
