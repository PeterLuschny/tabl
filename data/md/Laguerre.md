# Laguerre
['A021009', 'A021010', 'A144084']

Laguerre Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [2, 4, 1] |
| trow3 | [6, 18, 9, 1] |
| trow4 | [24, 96, 72, 16, 1] |
| trow5 | [120, 600, 600, 200, 25, 1] |
| trow6 | [720, 4320, 5400, 2400, 450, 36, 1] |

Laguerre Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 2, 4, 1, 6, 18, 9, 1, 24, 96, 72, 16, 1, 120, 600, 600, 200, 25, 1, 720, 4320, 5400, 2400, 450, 36, 1] |
| rev      | [1, 1, 1, 1, 4, 2, 1, 9, 18, 6, 1, 16, 72, 96, 24, 1, 25, 200, 600, 600, 120, 1, 36, 450, 2400, 5400, 4320, 720] |
| accu     | [1, 1, 2, 2, 6, 7, 6, 24, 33, 34, 24, 120, 192, 208, 209, 120, 720, 1320, 1520, 1545, 1546, 720, 5040, 10440, 12840, 13290, 13326, 13327] |
| revaccu  | [1, 2, 1, 7, 6, 2, 34, 33, 24, 6, 209, 208, 192, 120, 24, 1546, 1545, 1520, 1320, 720, 120, 13327, 13326, 13290, 12840, 10440, 5040, 720] |
| accurev  | [1, 1, 2, 1, 5, 7, 1, 10, 28, 34, 1, 17, 89, 185, 209, 1, 26, 226, 826, 1426, 1546, 1, 37, 487, 2887, 8287, 12607, 13327] |
| diag     | [1, 1, 2, 1, 6, 4, 24, 18, 1, 120, 96, 9] |

Laguerre Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 7, 34, 209, 1546, 13327] |
| evensum   | [1, 1, 3, 15, 97, 745, 6571] |
| oddsum    | [0, 1, 4, 19, 112, 801, 6756] |
| altsum    | [1, 0, -1, -4, -15, -56, -185] |
| diagsum   | [1, 1, 3, 10, 43, 225] |
| accusum   | [1, 3, 15, 97, 753, 6771, 68983] |
| revaccusum | [1, 3, 13, 73, 501, 4051, 37633] |

Laguerre Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [1, 4, 9, 16, 25, 36, 49]|
| rdiag2 | [2, 18, 72, 200, 450, 882, 1568]|
| rdiag3 | [6, 96, 600, 2400, 7350, 18816, 42336]|
| rdiag4 | [24, 600, 5400, 29400, 117600, 381024, 1058400]|
| rdiag5 | [120, 4320, 52920, 376320, 1905120, 7620480, 25613280]|
| rdiag6 | [720, 35280, 564480, 5080320, 31752000, 153679680, 614718720]|

Laguerre Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 2, 6, 24, 120, 720] |
| cdiag1 | [1, 4, 18, 96, 600, 4320, 35280] |
| cdiag2 | [1, 9, 72, 600, 5400, 52920, 564480] |
| cdiag3 | [1, 16, 200, 2400, 29400, 376320, 5080320] |
| cdiag4 | [1, 25, 450, 7350, 117600, 1905120, 31752000] |
| cdiag5 | [1, 36, 882, 18816, 381024, 7620480, 153679680] |
| cdiag6 | [1, 49, 1568, 42336, 1058400, 25613280, 614718720] |

Laguerre Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [2, 7, 14, 23, 34, 47, 62] |
| rpdiag3 | [6, 34, 86, 168, 286, 446, 654] |
| rpdiag4 | [24, 209, 648, 1473, 2840, 4929, 7944] |
| rpdiag5 | [120, 1546, 5752, 14988, 32344, 61870, 108696] |
| rpdiag6 | [720, 13327, 58576, 173007, 414160, 866695, 1649232] |

Laguerre Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 2, 6, 24, 120, 720] |
| cpdiag1 | [1, 2, 7, 34, 209, 1546, 13327] |
| cpdiag2 | [1, 3, 14, 86, 648, 5752, 58576] |
| cpdiag3 | [1, 4, 23, 168, 1473, 14988, 173007] |
| cpdiag4 | [1, 5, 34, 286, 2840, 32344, 414160] |
| cpdiag5 | [1, 6, 47, 446, 4929, 61870, 866695] |
| cpdiag6 | [1, 7, 62, 654, 7944, 108696, 1649232] |

# LaguerreInv
True

LaguerreInv Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [-1, 1] |
| trow2 | [2, -4, 1] |
| trow3 | [-6, 18, -9, 1] |
| trow4 | [24, -96, 72, -16, 1] |
| trow5 | [-120, 600, -600, 200, -25, 1] |
| trow6 | [720, -4320, 5400, -2400, 450, -36, 1] |

LaguerreInv Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, -1, 1, 2, -4, 1, -6, 18, -9, 1, 24, -96, 72, -16, 1, -120, 600, -600, 200, -25, 1, 720, -4320, 5400, -2400, 450, -36, 1] |
| rev      | [1, 1, -1, 1, -4, 2, 1, -9, 18, -6, 1, -16, 72, -96, 24, 1, -25, 200, -600, 600, -120, 1, -36, 450, -2400, 5400, -4320, 720] |
| accu     | [1, -1, 0, 2, -2, -1, -6, 12, 3, 4, 24, -72, 0, -16, -15, -120, 480, -120, 80, 55, 56, 720, -3600, 1800, -600, -150, -186, -185] |
| revaccu  | [1, 0, -1, -1, -2, 2, 4, 3, 12, -6, -15, -16, 0, -72, 24, 56, 55, 80, -120, 480, -120, -185, -186, -150, -600, 1800, -3600, 720] |
| accurev  | [1, 1, 0, 1, -3, -1, 1, -8, 10, 4, 1, -15, 57, -39, -15, 1, -24, 176, -424, 176, 56, 1, -35, 415, -1985, 3415, -905, -185] |
| diag     | [1, -1, 2, 1, -6, -4, 24, 18, 1, -120, -96, -9] |

LaguerreInv Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 0, -1, 4, -15, 56, -185] |
| evensum   | [1, -1, 3, -15, 97, -745, 6571] |
| oddsum    | [0, 1, -4, 19, -112, 801, -6756] |
| altsum    | [1, -2, 7, -34, 209, -1546, 13327] |
| diagsum   | [1, -1, 3, -10, 43, -225] |
| accusum   | [1, -1, -1, 13, -79, 431, -2201] |
| revaccusum | [1, 1, -3, 7, -11, -39, 721] |

LaguerreInv Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [-1, -4, -9, -16, -25, -36, -49]|
| rdiag2 | [2, 18, 72, 200, 450, 882, 1568]|
| rdiag3 | [-6, -96, -600, -2400, -7350, -18816, -42336]|
| rdiag4 | [24, 600, 5400, 29400, 117600, 381024, 1058400]|
| rdiag5 | [-120, -4320, -52920, -376320, -1905120, -7620480, -25613280]|
| rdiag6 | [720, 35280, 564480, 5080320, 31752000, 153679680, 614718720]|

LaguerreInv Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, -1, 2, -6, 24, -120, 720] |
| cdiag1 | [1, -4, 18, -96, 600, -4320, 35280] |
| cdiag2 | [1, -9, 72, -600, 5400, -52920, 564480] |
| cdiag3 | [1, -16, 200, -2400, 29400, -376320, 5080320] |
| cdiag4 | [1, -25, 450, -7350, 117600, -1905120, 31752000] |
| cdiag5 | [1, -36, 882, -18816, 381024, -7620480, 153679680] |
| cdiag6 | [1, -49, 1568, -42336, 1058400, -25613280, 614718720] |

LaguerreInv Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [-1, 0, 1, 2, 3, 4, 5] |
| rpdiag2 | [2, -1, -2, -1, 2, 7, 14] |
| rpdiag3 | [-6, 4, 2, -6, -14, -16, -6] |
| rpdiag4 | [24, -15, 8, 33, 24, -31, -120] |
| rpdiag5 | [-120, 56, -88, -102, 104, 380, 456] |
| rpdiag6 | [720, -185, 592, -9, -1328, -1505, 720] |

LaguerreInv Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, -1, 2, -6, 24, -120, 720] |
| cpdiag1 | [1, 0, -1, 4, -15, 56, -185] |
| cpdiag2 | [1, 1, -2, 2, 8, -88, 592] |
| cpdiag3 | [1, 2, -1, -6, 33, -102, -9] |
| cpdiag4 | [1, 3, 2, -14, 24, 104, -1328] |
| cpdiag5 | [1, 4, 7, -16, -31, 380, -1505] |
| cpdiag6 | [1, 5, 14, -6, -120, 456, 720] |

# LaguerreRev
True

LaguerreRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [1, 4, 2] |
| trow3 | [1, 9, 18, 6] |
| trow4 | [1, 16, 72, 96, 24] |
| trow5 | [1, 25, 200, 600, 600, 120] |
| trow6 | [1, 36, 450, 2400, 5400, 4320, 720] |

LaguerreRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 1, 4, 2, 1, 9, 18, 6, 1, 16, 72, 96, 24, 1, 25, 200, 600, 600, 120, 1, 36, 450, 2400, 5400, 4320, 720] |
| rev      | [1, 1, 1, 2, 4, 1, 6, 18, 9, 1, 24, 96, 72, 16, 1, 120, 600, 600, 200, 25, 1, 720, 4320, 5400, 2400, 450, 36, 1] |
| accu     | [1, 1, 2, 1, 5, 7, 1, 10, 28, 34, 1, 17, 89, 185, 209, 1, 26, 226, 826, 1426, 1546, 1, 37, 487, 2887, 8287, 12607, 13327] |
| revaccu  | [1, 2, 1, 7, 5, 1, 34, 28, 10, 1, 209, 185, 89, 17, 1, 1546, 1426, 826, 226, 26, 1, 13327, 12607, 8287, 2887, 487, 37, 1] |
| accurev  | [1, 1, 2, 2, 6, 7, 6, 24, 33, 34, 24, 120, 192, 208, 209, 120, 720, 1320, 1520, 1545, 1546, 720, 5040, 10440, 12840, 13290, 13326, 13327] |
| diag     | [1, 1, 1, 1, 1, 4, 1, 9, 2, 1, 16, 18] |

LaguerreRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 7, 34, 209, 1546, 13327] |
| evensum   | [1, 1, 3, 19, 97, 801, 6571] |
| oddsum    | [0, 1, 4, 15, 112, 745, 6756] |
| altsum    | [1, 0, -1, 4, -15, 56, -185] |
| diagsum   | [1, 1, 2, 5, 12, 35] |
| accusum   | [1, 3, 13, 73, 501, 4051, 37633] |
| revaccusum | [1, 3, 15, 97, 753, 6771, 68983] |

LaguerreRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 2, 6, 24, 120, 720]|
| rdiag1 | [1, 4, 18, 96, 600, 4320, 35280]|
| rdiag2 | [1, 9, 72, 600, 5400, 52920, 564480]|
| rdiag3 | [1, 16, 200, 2400, 29400, 376320, 5080320]|
| rdiag4 | [1, 25, 450, 7350, 117600, 1905120, 31752000]|
| rdiag5 | [1, 36, 882, 18816, 381024, 7620480, 153679680]|
| rdiag6 | [1, 49, 1568, 42336, 1058400, 25613280, 614718720]|

LaguerreRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [1, 4, 9, 16, 25, 36, 49] |
| cdiag2 | [2, 18, 72, 200, 450, 882, 1568] |
| cdiag3 | [6, 96, 600, 2400, 7350, 18816, 42336] |
| cdiag4 | [24, 600, 5400, 29400, 117600, 381024, 1058400] |
| cdiag5 | [120, 4320, 52920, 376320, 1905120, 7620480, 25613280] |
| cdiag6 | [720, 35280, 564480, 5080320, 31752000, 153679680, 614718720] |

LaguerreRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [1, 7, 17, 31, 49, 71, 97] |
| rpdiag3 | [1, 34, 139, 352, 709, 1246, 1999] |
| rpdiag4 | [1, 209, 1473, 5233, 13505, 28881, 54529] |
| rpdiag5 | [1, 1546, 19091, 95836, 318181, 830126, 1847671] |
| rpdiag6 | [1, 13327, 291793, 2080999, 8916145, 28436431, 74717857] |

LaguerreRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 2, 7, 34, 209, 1546, 13327] |
| cpdiag2 | [1, 3, 17, 139, 1473, 19091, 291793] |
| cpdiag3 | [1, 4, 31, 352, 5233, 95836, 2080999] |
| cpdiag4 | [1, 5, 49, 709, 13505, 318181, 8916145] |
| cpdiag5 | [1, 6, 71, 1246, 28881, 830126, 28436431] |
| cpdiag6 | [1, 7, 97, 1999, 54529, 1847671, 74717857] |

# LaguerreInvRev
True

LaguerreInvRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, -1] |
| trow2 | [1, -4, 2] |
| trow3 | [1, -9, 18, -6] |
| trow4 | [1, -16, 72, -96, 24] |
| trow5 | [1, -25, 200, -600, 600, -120] |
| trow6 | [1, -36, 450, -2400, 5400, -4320, 720] |

LaguerreInvRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, -1, 1, -4, 2, 1, -9, 18, -6, 1, -16, 72, -96, 24, 1, -25, 200, -600, 600, -120, 1, -36, 450, -2400, 5400, -4320, 720] |
| rev      | [1, -1, 1, 2, -4, 1, -6, 18, -9, 1, 24, -96, 72, -16, 1, -120, 600, -600, 200, -25, 1, 720, -4320, 5400, -2400, 450, -36, 1] |
| accu     | [1, 1, 0, 1, -3, -1, 1, -8, 10, 4, 1, -15, 57, -39, -15, 1, -24, 176, -424, 176, 56, 1, -35, 415, -1985, 3415, -905, -185] |
| revaccu  | [1, 0, 1, -1, -3, 1, 4, 10, -8, 1, -15, -39, 57, -15, 1, 56, 176, -424, 176, -24, 1, -185, -905, 3415, -1985, 415, -35, 1] |
| accurev  | [1, -1, 0, 2, -2, -1, -6, 12, 3, 4, 24, -72, 0, -16, -15, -120, 480, -120, 80, 55, 56, 720, -3600, 1800, -600, -150, -186, -185] |
| diag     | [1, 1, 1, -1, 1, -4, 1, -9, 2, 1, -16, 18] |

LaguerreInvRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 0, -1, 4, -15, 56, -185] |
| evensum   | [1, 1, 3, 19, 97, 801, 6571] |
| oddsum    | [0, -1, -4, -15, -112, -745, -6756] |
| altsum    | [1, 2, 7, 34, 209, 1546, 13327] |
| diagsum   | [1, 1, 0, -3, -6, 3] |
| accusum   | [1, 1, -3, 7, -11, -39, 721] |
| revaccusum | [1, -1, -1, 13, -79, 431, -2201] |

LaguerreInvRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, -1, 2, -6, 24, -120, 720]|
| rdiag1 | [1, -4, 18, -96, 600, -4320, 35280]|
| rdiag2 | [1, -9, 72, -600, 5400, -52920, 564480]|
| rdiag3 | [1, -16, 200, -2400, 29400, -376320, 5080320]|
| rdiag4 | [1, -25, 450, -7350, 117600, -1905120, 31752000]|
| rdiag5 | [1, -36, 882, -18816, 381024, -7620480, 153679680]|
| rdiag6 | [1, -49, 1568, -42336, 1058400, -25613280, 614718720]|

LaguerreInvRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [-1, -4, -9, -16, -25, -36, -49] |
| cdiag2 | [2, 18, 72, 200, 450, 882, 1568] |
| cdiag3 | [-6, -96, -600, -2400, -7350, -18816, -42336] |
| cdiag4 | [24, 600, 5400, 29400, 117600, 381024, 1058400] |
| cdiag5 | [-120, -4320, -52920, -376320, -1905120, -7620480, -25613280] |
| cdiag6 | [720, 35280, 564480, 5080320, 31752000, 153679680, 614718720] |

LaguerreInvRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 0, -1, -2, -3, -4, -5] |
| rpdiag2 | [1, -1, 1, 7, 17, 31, 49] |
| rpdiag3 | [1, 4, 7, -26, -131, -344, -701] |
| rpdiag4 | [1, -15, -127, -47, 1089, 4721, 12865] |
| rpdiag5 | [1, 56, 1711, 4966, -4579, -70124, -278069] |
| rpdiag6 | [1, -185, -23231, -148337, -238703, 836071, 6495985] |

LaguerreInvRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 0, -1, 4, -15, 56, -185] |
| cpdiag2 | [1, -1, 1, 7, -127, 1711, -23231] |
| cpdiag3 | [1, -2, 7, -26, -47, 4966, -148337] |
| cpdiag4 | [1, -3, 17, -131, 1089, -4579, -238703] |
| cpdiag5 | [1, -4, 31, -344, 4721, -70124, 836071] |
| cpdiag6 | [1, -5, 49, -701, 12865, -278069, 6495985] |
