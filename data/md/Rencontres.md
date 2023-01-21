# Rencontres
['A008290', 'A098825']

Rencontres Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [1, 0, 1] |
| trow3 | [2, 3, 0, 1] |
| trow4 | [9, 8, 6, 0, 1] |
| trow5 | [44, 45, 20, 10, 0, 1] |
| trow6 | [265, 264, 135, 40, 15, 0, 1] |

Rencontres Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, 1, 0, 1, 2, 3, 0, 1, 9, 8, 6, 0, 1, 44, 45, 20, 10, 0, 1, 265, 264, 135, 40, 15, 0, 1] |
| rev      | [1, 1, 0, 1, 0, 1, 1, 0, 3, 2, 1, 0, 6, 8, 9, 1, 0, 10, 20, 45, 44, 1, 0, 15, 40, 135, 264, 265] |
| accu     | [1, 0, 1, 1, 1, 2, 2, 5, 5, 6, 9, 17, 23, 23, 24, 44, 89, 109, 119, 119, 120, 265, 529, 664, 704, 719, 719, 720] |
| revaccu  | [1, 1, 0, 2, 1, 1, 6, 5, 5, 2, 24, 23, 23, 17, 9, 120, 119, 119, 109, 89, 44, 720, 719, 719, 704, 664, 529, 265] |
| accurev  | [1, 1, 1, 1, 1, 2, 1, 1, 4, 6, 1, 1, 7, 15, 24, 1, 1, 11, 31, 76, 120, 1, 1, 16, 56, 191, 455, 720] |
| diag     | [1, 0, 1, 1, 2, 0, 9, 3, 1, 44, 8, 0] |

Rencontres Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 6, 24, 120, 720] |
| evensum   | [1, 0, 2, 2, 16, 64, 416] |
| oddsum    | [0, 1, 0, 4, 8, 56, 304] |
| altsum    | [1, -1, 2, -2, 8, 8, 112] |
| diagsum   | [1, 0, 2, 2, 13, 52] |
| accusum   | [1, 1, 4, 18, 96, 600, 4320] |
| revaccusum | [1, 2, 4, 12, 48, 240, 1440] |

Rencontres Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag2 | [1, 3, 6, 10, 15, 21, 28]|
| rdiag3 | [2, 8, 20, 40, 70, 112, 168]|
| rdiag4 | [9, 45, 135, 315, 630, 1134, 1890]|
| rdiag5 | [44, 264, 924, 2464, 5544, 11088, 20328]|
| rdiag6 | [265, 1855, 7420, 22260, 55650, 122430, 244860]|

Rencontres Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 1, 2, 9, 44, 265] |
| cdiag1 | [1, 0, 3, 8, 45, 264, 1855] |
| cdiag2 | [1, 0, 6, 20, 135, 924, 7420] |
| cdiag3 | [1, 0, 10, 40, 315, 2464, 22260] |
| cdiag4 | [1, 0, 15, 70, 630, 5544, 55650] |
| cdiag5 | [1, 0, 21, 112, 1134, 11088, 122430] |
| cdiag6 | [1, 0, 28, 168, 1890, 20328, 244860] |

Rencontres Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [1, 2, 5, 10, 17, 26, 37] |
| rpdiag3 | [2, 6, 16, 38, 78, 142, 236] |
| rpdiag4 | [9, 24, 65, 168, 393, 824, 1569] |
| rpdiag5 | [44, 120, 326, 872, 2208, 5144, 10970] |
| rpdiag6 | [265, 720, 1957, 5296, 13977, 34960, 81445] |

Rencontres Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 1, 2, 9, 44, 265] |
| cpdiag1 | [1, 1, 2, 6, 24, 120, 720] |
| cpdiag2 | [1, 2, 5, 16, 65, 326, 1957] |
| cpdiag3 | [1, 3, 10, 38, 168, 872, 5296] |
| cpdiag4 | [1, 4, 17, 78, 393, 2208, 13977] |
| cpdiag5 | [1, 5, 26, 142, 824, 5144, 34960] |
| cpdiag6 | [1, 6, 37, 236, 1569, 10970, 81445] |

# RencontresInv
True

RencontresInv Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 1] |
| trow2 | [-1, 0, 1] |
| trow3 | [-2, -3, 0, 1] |
| trow4 | [-3, -8, -6, 0, 1] |
| trow5 | [-4, -15, -20, -10, 0, 1] |
| trow6 | [-5, -24, -45, -40, -15, 0, 1] |

RencontresInv Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 1, -1, 0, 1, -2, -3, 0, 1, -3, -8, -6, 0, 1, -4, -15, -20, -10, 0, 1, -5, -24, -45, -40, -15, 0, 1] |
| rev      | [1, 1, 0, 1, 0, -1, 1, 0, -3, -2, 1, 0, -6, -8, -3, 1, 0, -10, -20, -15, -4, 1, 0, -15, -40, -45, -24, -5] |
| accu     | [1, 0, 1, -1, -1, 0, -2, -5, -5, -4, -3, -11, -17, -17, -16, -4, -19, -39, -49, -49, -48, -5, -29, -74, -114, -129, -129, -128] |
| revaccu  | [1, 1, 0, 0, -1, -1, -4, -5, -5, -2, -16, -17, -17, -11, -3, -48, -49, -49, -39, -19, -4, -128, -129, -129, -114, -74, -29, -5] |
| accurev  | [1, 1, 1, 1, 1, 0, 1, 1, -2, -4, 1, 1, -5, -13, -16, 1, 1, -9, -29, -44, -48, 1, 1, -14, -54, -99, -123, -128] |
| diag     | [1, 0, -1, 1, -2, 0, -3, -3, 1, -4, -8, 0] |

RencontresInv Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 0, -4, -16, -48, -128] |
| evensum   | [1, 0, 0, -2, -8, -24, -64] |
| oddsum    | [0, 1, 0, -2, -8, -24, -64] |
| altsum    | [1, -1, 0, 0, 0, 0, 0] |
| diagsum   | [1, 0, 0, -2, -5, -12] |
| accusum   | [1, 1, -2, -16, -64, -208, -608] |
| revaccusum | [1, 2, 2, -4, -32, -128, -416] |

RencontresInv Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag2 | [-1, -3, -6, -10, -15, -21, -28]|
| rdiag3 | [-2, -8, -20, -40, -70, -112, -168]|
| rdiag4 | [-3, -15, -45, -105, -210, -378, -630]|
| rdiag5 | [-4, -24, -84, -224, -504, -1008, -1848]|
| rdiag6 | [-5, -35, -140, -420, -1050, -2310, -4620]|

RencontresInv Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, -1, -2, -3, -4, -5] |
| cdiag1 | [1, 0, -3, -8, -15, -24, -35] |
| cdiag2 | [1, 0, -6, -20, -45, -84, -140] |
| cdiag3 | [1, 0, -10, -40, -105, -224, -420] |
| cdiag4 | [1, 0, -15, -70, -210, -504, -1050] |
| cdiag5 | [1, 0, -21, -112, -378, -1008, -2310] |
| cdiag6 | [1, 0, -28, -168, -630, -1848, -4620] |

RencontresInv Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [-1, 0, 3, 8, 15, 24, 35] |
| rpdiag3 | [-2, -4, 0, 16, 50, 108, 196] |
| rpdiag4 | [-3, -16, -27, 0, 125, 432, 1029] |
| rpdiag5 | [-4, -48, -162, -256, 0, 1296, 4802] |
| rpdiag6 | [-5, -128, -729, -2048, -3125, 0, 16807] |

RencontresInv Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, -1, -2, -3, -4, -5] |
| cpdiag1 | [1, 1, 0, -4, -16, -48, -128] |
| cpdiag2 | [1, 2, 3, 0, -27, -162, -729] |
| cpdiag3 | [1, 3, 8, 16, 0, -256, -2048] |
| cpdiag4 | [1, 4, 15, 50, 125, 0, -3125] |
| cpdiag5 | [1, 5, 24, 108, 432, 1296, 0] |
| cpdiag6 | [1, 6, 35, 196, 1029, 4802, 16807] |

# RencontresRev
True

RencontresRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, 0, 1] |
| trow3 | [1, 0, 3, 2] |
| trow4 | [1, 0, 6, 8, 9] |
| trow5 | [1, 0, 10, 20, 45, 44] |
| trow6 | [1, 0, 15, 40, 135, 264, 265] |

RencontresRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, 0, 1, 1, 0, 3, 2, 1, 0, 6, 8, 9, 1, 0, 10, 20, 45, 44, 1, 0, 15, 40, 135, 264, 265] |
| rev      | [1, 0, 1, 1, 0, 1, 2, 3, 0, 1, 9, 8, 6, 0, 1, 44, 45, 20, 10, 0, 1, 265, 264, 135, 40, 15, 0, 1] |
| accu     | [1, 1, 1, 1, 1, 2, 1, 1, 4, 6, 1, 1, 7, 15, 24, 1, 1, 11, 31, 76, 120, 1, 1, 16, 56, 191, 455, 720] |
| revaccu  | [1, 1, 1, 2, 1, 1, 6, 4, 1, 1, 24, 15, 7, 1, 1, 120, 76, 31, 11, 1, 1, 720, 455, 191, 56, 16, 1, 1] |
| accurev  | [1, 0, 1, 1, 1, 2, 2, 5, 5, 6, 9, 17, 23, 23, 24, 44, 89, 109, 119, 119, 120, 265, 529, 664, 704, 719, 719, 720] |
| diag     | [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 3] |

RencontresRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 2, 6, 24, 120, 720] |
| evensum   | [1, 1, 2, 4, 16, 56, 416] |
| oddsum    | [0, 0, 0, 2, 8, 64, 304] |
| altsum    | [1, 1, 2, 2, 8, -8, 112] |
| diagsum   | [1, 1, 1, 1, 2, 4] |
| accusum   | [1, 2, 4, 12, 48, 240, 1440] |
| revaccusum | [1, 1, 4, 18, 96, 600, 4320] |

RencontresRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 1, 2, 9, 44, 265]|
| rdiag1 | [1, 0, 3, 8, 45, 264, 1855]|
| rdiag2 | [1, 0, 6, 20, 135, 924, 7420]|
| rdiag3 | [1, 0, 10, 40, 315, 2464, 22260]|
| rdiag4 | [1, 0, 15, 70, 630, 5544, 55650]|
| rdiag5 | [1, 0, 21, 112, 1134, 11088, 122430]|
| rdiag6 | [1, 0, 28, 168, 1890, 20328, 244860]|

RencontresRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag2 | [1, 3, 6, 10, 15, 21, 28] |
| cdiag3 | [2, 8, 20, 40, 70, 112, 168] |
| cdiag4 | [9, 45, 135, 315, 630, 1134, 1890] |
| cdiag5 | [44, 264, 924, 2464, 5544, 11088, 20328] |
| cdiag6 | [265, 1855, 7420, 22260, 55650, 122430, 244860] |

RencontresRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 2, 5, 10, 17, 26, 37] |
| rpdiag3 | [1, 6, 29, 82, 177, 326, 541] |
| rpdiag4 | [1, 24, 233, 1000, 2913, 6776, 13609] |
| rpdiag5 | [1, 120, 2329, 14968, 58017, 168376, 405145] |
| rpdiag6 | [1, 720, 27949, 269488, 1393137, 5055376, 14600845] |

RencontresRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 1, 2, 6, 24, 120, 720] |
| cpdiag2 | [1, 1, 5, 29, 233, 2329, 27949] |
| cpdiag3 | [1, 1, 10, 82, 1000, 14968, 269488] |
| cpdiag4 | [1, 1, 17, 177, 2913, 58017, 1393137] |
| cpdiag5 | [1, 1, 26, 326, 6776, 168376, 5055376] |
| cpdiag6 | [1, 1, 37, 541, 13609, 405145, 14600845] |

# RencontresInvRev
True

RencontresInvRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 0] |
| trow2 | [1, 0, -1] |
| trow3 | [1, 0, -3, -2] |
| trow4 | [1, 0, -6, -8, -3] |
| trow5 | [1, 0, -10, -20, -15, -4] |
| trow6 | [1, 0, -15, -40, -45, -24, -5] |

RencontresInvRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 0, 1, 0, -1, 1, 0, -3, -2, 1, 0, -6, -8, -3, 1, 0, -10, -20, -15, -4, 1, 0, -15, -40, -45, -24, -5] |
| rev      | [1, 0, 1, -1, 0, 1, -2, -3, 0, 1, -3, -8, -6, 0, 1, -4, -15, -20, -10, 0, 1, -5, -24, -45, -40, -15, 0, 1] |
| accu     | [1, 1, 1, 1, 1, 0, 1, 1, -2, -4, 1, 1, -5, -13, -16, 1, 1, -9, -29, -44, -48, 1, 1, -14, -54, -99, -123, -128] |
| revaccu  | [1, 1, 1, 0, 1, 1, -4, -2, 1, 1, -16, -13, -5, 1, 1, -48, -44, -29, -9, 1, 1, -128, -123, -99, -54, -14, 1, 1] |
| accurev  | [1, 0, 1, -1, -1, 0, -2, -5, -5, -4, -3, -11, -17, -17, -16, -4, -19, -39, -49, -49, -48, -5, -29, -74, -114, -129, -129, -128] |
| diag     | [1, 1, 1, 0, 1, 0, 1, 0, -1, 1, 0, -3] |

RencontresInvRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 1, 0, -4, -16, -48, -128] |
| evensum   | [1, 1, 0, -2, -8, -24, -64] |
| oddsum    | [0, 0, 0, -2, -8, -24, -64] |
| altsum    | [1, 1, 0, 0, 0, 0, 0] |
| diagsum   | [1, 1, 1, 1, 0, -2] |
| accusum   | [1, 2, 2, -4, -32, -128, -416] |
| revaccusum | [1, 1, -2, -16, -64, -208, -608] |

RencontresInvRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, -1, -2, -3, -4, -5]|
| rdiag1 | [1, 0, -3, -8, -15, -24, -35]|
| rdiag2 | [1, 0, -6, -20, -45, -84, -140]|
| rdiag3 | [1, 0, -10, -40, -105, -224, -420]|
| rdiag4 | [1, 0, -15, -70, -210, -504, -1050]|
| rdiag5 | [1, 0, -21, -112, -378, -1008, -2310]|
| rdiag6 | [1, 0, -28, -168, -630, -1848, -4620]|

RencontresInvRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag2 | [-1, -3, -6, -10, -15, -21, -28] |
| cdiag3 | [-2, -8, -20, -40, -70, -112, -168] |
| cdiag4 | [-3, -15, -45, -105, -210, -378, -630] |
| cdiag5 | [-4, -24, -84, -224, -504, -1008, -1848] |
| cdiag6 | [-5, -35, -140, -420, -1050, -2310, -4620] |

RencontresInvRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [1, 0, -3, -8, -15, -24, -35] |
| rpdiag3 | [1, -4, -27, -80, -175, -324, -539] |
| rpdiag4 | [1, -16, -135, -512, -1375, -3024, -5831] |
| rpdiag5 | [1, -48, -567, -2816, -9375, -24624, -55223] |
| rpdiag6 | [1, -128, -2187, -14336, -59375, -186624, -487403] |

RencontresInvRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 1, 0, -4, -16, -48, -128] |
| cpdiag2 | [1, 1, -3, -27, -135, -567, -2187] |
| cpdiag3 | [1, 1, -8, -80, -512, -2816, -14336] |
| cpdiag4 | [1, 1, -15, -175, -1375, -9375, -59375] |
| cpdiag5 | [1, 1, -24, -324, -3024, -24624, -186624] |
| cpdiag6 | [1, 1, -35, -539, -5831, -55223, -487403] |
