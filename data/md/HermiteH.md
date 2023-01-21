# HermiteH
['A060821']

HermiteH Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [0, 2] |
| trow2 | [2, 0, 4] |
| trow3 | [0, 12, 0, 8] |
| trow4 | [12, 0, 48, 0, 16] |
| trow5 | [0, 120, 0, 160, 0, 32] |
| trow6 | [120, 0, 720, 0, 480, 0, 64] |

HermiteH Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 0, 2, 2, 0, 4, 0, 12, 0, 8, 12, 0, 48, 0, 16, 0, 120, 0, 160, 0, 32, 120, 0, 720, 0, 480, 0, 64] |
| rev      | [1, 2, 0, 4, 0, 2, 8, 0, 12, 0, 16, 0, 48, 0, 12, 32, 0, 160, 0, 120, 0, 64, 0, 480, 0, 720, 0, 120] |
| accu     | [1, 0, 2, 2, 2, 6, 0, 12, 12, 20, 12, 12, 60, 60, 76, 0, 120, 120, 280, 280, 312, 120, 120, 840, 840, 1320, 1320, 1384] |
| revaccu  | [1, 2, 0, 6, 2, 2, 20, 12, 12, 0, 76, 60, 60, 12, 12, 312, 280, 280, 120, 120, 0, 1384, 1320, 1320, 840, 840, 120, 120] |
| accurev  | [1, 2, 2, 4, 4, 6, 8, 8, 20, 20, 16, 16, 64, 64, 76, 32, 32, 192, 192, 312, 312, 64, 64, 544, 544, 1264, 1264, 1384] |
| diag     | [1, 0, 2, 2, 0, 0, 12, 12, 4, 0, 0, 0] |

HermiteH Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 6, 20, 76, 312, 1384] |
| evensum   | [1, 0, 6, 0, 76, 0, 1384] |
| oddsum    | [0, 2, 0, 20, 0, 312, 0] |
| altsum    | [1, -2, 6, -20, 76, -312, 1384] |
| diagsum   | [1, 0, 4, 0, 28, 0] |
| accusum   | [1, 2, 10, 44, 220, 1112, 5944] |
| revaccusum | [1, 4, 14, 56, 236, 1072, 5128] |

HermiteH Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 2, 4, 8, 16, 32, 64]|
| rdiag1 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag2 | [2, 12, 48, 160, 480, 1344, 3584]|
| rdiag3 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag4 | [12, 120, 720, 3360, 13440, 48384, 161280]|
| rdiag5 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag6 | [120, 1680, 13440, 80640, 403200, 1774080, 7096320]|

HermiteH Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 0, 2, 0, 12, 0, 120] |
| cdiag1 | [2, 0, 12, 0, 120, 0, 1680] |
| cdiag2 | [4, 0, 48, 0, 720, 0, 13440] |
| cdiag3 | [8, 0, 160, 0, 3360, 0, 80640] |
| cdiag4 | [16, 0, 480, 0, 13440, 0, 403200] |
| cdiag5 | [32, 0, 1344, 0, 48384, 0, 1774080] |
| cdiag6 | [64, 0, 3584, 0, 161280, 0, 7096320] |

HermiteH Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [0, 2, 4, 6, 8, 10, 12] |
| rpdiag2 | [2, 6, 18, 38, 66, 102, 146] |
| rpdiag3 | [0, 20, 88, 252, 560, 1060, 1800] |
| rpdiag4 | [12, 76, 460, 1740, 4876, 11212, 22476] |
| rpdiag5 | [0, 312, 2544, 12456, 43488, 120600, 284112] |
| rpdiag6 | [120, 1384, 14776, 92136, 396664, 1318120, 3634104] |

HermiteH Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 0, 2, 0, 12, 0, 120] |
| cpdiag1 | [1, 2, 6, 20, 76, 312, 1384] |
| cpdiag2 | [1, 4, 18, 88, 460, 2544, 14776] |
| cpdiag3 | [1, 6, 38, 252, 1740, 12456, 92136] |
| cpdiag4 | [1, 8, 66, 560, 4876, 43488, 396664] |
| cpdiag5 | [1, 10, 102, 1060, 11212, 120600, 1318120] |
| cpdiag6 | [1, 12, 146, 1800, 22476, 284112, 3634104] |

# HermiteHRev
True

HermiteHRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [2, 0] |
| trow2 | [4, 0, 2] |
| trow3 | [8, 0, 12, 0] |
| trow4 | [16, 0, 48, 0, 12] |
| trow5 | [32, 0, 160, 0, 120, 0] |
| trow6 | [64, 0, 480, 0, 720, 0, 120] |

HermiteHRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 2, 0, 4, 0, 2, 8, 0, 12, 0, 16, 0, 48, 0, 12, 32, 0, 160, 0, 120, 0, 64, 0, 480, 0, 720, 0, 120] |
| rev      | [1, 0, 2, 2, 0, 4, 0, 12, 0, 8, 12, 0, 48, 0, 16, 0, 120, 0, 160, 0, 32, 120, 0, 720, 0, 480, 0, 64] |
| accu     | [1, 2, 2, 4, 4, 6, 8, 8, 20, 20, 16, 16, 64, 64, 76, 32, 32, 192, 192, 312, 312, 64, 64, 544, 544, 1264, 1264, 1384] |
| revaccu  | [1, 2, 2, 6, 4, 4, 20, 20, 8, 8, 76, 64, 64, 16, 16, 312, 312, 192, 192, 32, 32, 1384, 1264, 1264, 544, 544, 64, 64] |
| accurev  | [1, 0, 2, 2, 2, 6, 0, 12, 12, 20, 12, 12, 60, 60, 76, 0, 120, 120, 280, 280, 312, 120, 120, 840, 840, 1320, 1320, 1384] |
| diag     | [1, 2, 4, 0, 8, 0, 16, 0, 2, 32, 0, 12] |

HermiteHRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 6, 20, 76, 312, 1384] |
| evensum   | [1, 2, 6, 20, 76, 312, 1384] |
| oddsum    | [0, 0, 0, 0, 0, 0, 0] |
| altsum    | [1, 2, 6, 20, 76, 312, 1384] |
| diagsum   | [1, 2, 4, 8, 18, 44] |
| accusum   | [1, 4, 14, 56, 236, 1072, 5128] |
| revaccusum | [1, 2, 10, 44, 220, 1112, 5944] |

HermiteHRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 0, 2, 0, 12, 0, 120]|
| rdiag1 | [2, 0, 12, 0, 120, 0, 1680]|
| rdiag2 | [4, 0, 48, 0, 720, 0, 13440]|
| rdiag3 | [8, 0, 160, 0, 3360, 0, 80640]|
| rdiag4 | [16, 0, 480, 0, 13440, 0, 403200]|
| rdiag5 | [32, 0, 1344, 0, 48384, 0, 1774080]|
| rdiag6 | [64, 0, 3584, 0, 161280, 0, 7096320]|

HermiteHRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 2, 4, 8, 16, 32, 64] |
| cdiag1 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag2 | [2, 12, 48, 160, 480, 1344, 3584] |
| cdiag3 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag4 | [12, 120, 720, 3360, 13440, 48384, 161280] |
| cdiag5 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag6 | [120, 1680, 13440, 80640, 403200, 1774080, 7096320] |

HermiteHRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [2, 2, 2, 2, 2, 2, 2] |
| rpdiag2 | [4, 6, 12, 22, 36, 54, 76] |
| rpdiag3 | [8, 20, 56, 116, 200, 308, 440] |
| rpdiag4 | [16, 76, 400, 1420, 3856, 8716, 17296] |
| rpdiag5 | [32, 312, 2592, 11192, 33312, 79032, 161312] |
| rpdiag6 | [64, 1384, 21184, 150184, 683584, 2337064, 6549184] |

HermiteHRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 2, 4, 8, 16, 32, 64] |
| cpdiag1 | [1, 2, 6, 20, 76, 312, 1384] |
| cpdiag2 | [1, 2, 12, 56, 400, 2592, 21184] |
| cpdiag3 | [1, 2, 22, 116, 1420, 11192, 150184] |
| cpdiag4 | [1, 2, 36, 200, 3856, 33312, 683584] |
| cpdiag5 | [1, 2, 54, 308, 8716, 79032, 2337064] |
| cpdiag6 | [1, 2, 76, 440, 17296, 161312, 6549184] |
