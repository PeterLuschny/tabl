# EulerTan
['A162660', 'A350972', 'A155585', 'A009006', 'A000182']

EulerTan Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [0] |
| trow1 | [1, 0] |
| trow2 | [0, 2, 0] |
| trow3 | [-2, 0, 3, 0] |
| trow4 | [0, -8, 0, 4, 0] |
| trow5 | [16, 0, -20, 0, 5, 0] |
| trow6 | [0, 96, 0, -40, 0, 6, 0] |

EulerTan Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [0, 1, 0, 0, 2, 0, -2, 0, 3, 0, 0, -8, 0, 4, 0, 16, 0, -20, 0, 5, 0, 0, 96, 0, -40, 0, 6, 0] |
| rev      | [0, 0, 1, 0, 2, 0, 0, 3, 0, -2, 0, 4, 0, -8, 0, 0, 5, 0, -20, 0, 16, 0, 6, 0, -40, 0, 96, 0] |
| accu     | [0, 1, 1, 0, 2, 2, -2, -2, 1, 1, 0, -8, -8, -4, -4, 16, 16, -4, -4, 1, 1, 0, 96, 96, 56, 56, 62, 62] |
| revaccu  | [0, 1, 1, 2, 2, 0, 1, 1, -2, -2, -4, -4, -8, -8, 0, 1, 1, -4, -4, 16, 16, 62, 62, 56, 56, 96, 96, 0] |
| accurev  | [0, 0, 1, 0, 2, 2, 0, 3, 3, 1, 0, 4, 4, -4, -4, 0, 5, 5, -15, -15, 1, 0, 6, 6, -34, -34, 62, 62] |
| diag     | [0, 1, 0, 0, -2, 2, 0, 0, 0, 16, -8, 3] |

EulerTan Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [0, 1, 2, 1, -4, 1, 62] |
| evensum   | [0, 1, 0, 1, 0, 1, 0] |
| oddsum    | [0, 0, 2, 0, -4, 0, 62] |
| altsum    | [0, 1, -2, 1, 4, 1, -62] |
| diagsum   | [0, 1, 0, 0, 0, 11] |
| accusum   | [0, 2, 4, -2, -24, 26, 428] |
| revaccusum | [0, 1, 4, 7, 0, -19, 68] |

EulerTan Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag1 | [1, 2, 3, 4, 5, 6, 7]|
| rdiag2 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag3 | [-2, -8, -20, -40, -70, -112, -168]|
| rdiag4 | [0, 0, 0, 0, 0, 0, 0]|
| rdiag5 | [16, 96, 336, 896, 2016, 4032, 7392]|
| rdiag6 | [0, 0, 0, 0, 0, 0, 0]|

EulerTan Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [0, 1, 0, -2, 0, 16, 0] |
| cdiag1 | [0, 2, 0, -8, 0, 96, 0] |
| cdiag2 | [0, 3, 0, -20, 0, 336, 0] |
| cdiag3 | [0, 4, 0, -40, 0, 896, 0] |
| cdiag4 | [0, 5, 0, -70, 0, 2016, 0] |
| cdiag5 | [0, 6, 0, -112, 0, 4032, 0] |
| cdiag6 | [0, 7, 0, -168, 0, 7392, 0] |

EulerTan Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [0, 0, 0, 0, 0, 0, 0] |
| rpdiag1 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag2 | [0, 2, 4, 6, 8, 10, 12] |
| rpdiag3 | [-2, 1, 10, 25, 46, 73, 106] |
| rpdiag4 | [0, -4, 16, 84, 224, 460, 816] |
| rpdiag5 | [16, 1, 16, 241, 976, 2641, 5776] |
| rpdiag6 | [0, 62, 64, 666, 3968, 14230, 38592] |

EulerTan Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [0, 1, 0, -2, 0, 16, 0] |
| cpdiag1 | [0, 1, 2, 1, -4, 1, 62] |
| cpdiag2 | [0, 1, 4, 10, 16, 16, 64] |
| cpdiag3 | [0, 1, 6, 25, 84, 241, 666] |
| cpdiag4 | [0, 1, 8, 46, 224, 976, 3968] |
| cpdiag5 | [0, 1, 10, 73, 460, 2641, 14230] |
| cpdiag6 | [0, 1, 12, 106, 816, 5776, 38592] |

# EulerTanRev
True

EulerTanRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [0] |
| trow1 | [0, 1] |
| trow2 | [0, 2, 0] |
| trow3 | [0, 3, 0, -2] |
| trow4 | [0, 4, 0, -8, 0] |
| trow5 | [0, 5, 0, -20, 0, 16] |
| trow6 | [0, 6, 0, -40, 0, 96, 0] |

EulerTanRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [0, 0, 1, 0, 2, 0, 0, 3, 0, -2, 0, 4, 0, -8, 0, 0, 5, 0, -20, 0, 16, 0, 6, 0, -40, 0, 96, 0] |
| rev      | [0, 1, 0, 0, 2, 0, -2, 0, 3, 0, 0, -8, 0, 4, 0, 16, 0, -20, 0, 5, 0, 0, 96, 0, -40, 0, 6, 0] |
| accu     | [0, 0, 1, 0, 2, 2, 0, 3, 3, 1, 0, 4, 4, -4, -4, 0, 5, 5, -15, -15, 1, 0, 6, 6, -34, -34, 62, 62] |
| revaccu  | [0, 1, 0, 2, 2, 0, 1, 3, 3, 0, -4, -4, 4, 4, 0, 1, -15, -15, 5, 5, 0, 62, 62, -34, -34, 6, 6, 0] |
| accurev  | [0, 1, 1, 0, 2, 2, -2, -2, 1, 1, 0, -8, -8, -4, -4, 16, 16, -4, -4, 1, 1, 0, 96, 96, 56, 56, 62, 62] |
| diag     | [0, 0, 0, 1, 0, 2, 0, 3, 0, 0, 4, 0] |

EulerTanRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [0, 1, 2, 1, -4, 1, 62] |
| evensum   | [0, 0, 0, 0, 0, 0, 0] |
| oddsum    | [0, 1, 2, 1, -4, 1, 62] |
| altsum    | [0, -1, -2, -1, 4, -1, -62] |
| diagsum   | [0, 0, 1, 2, 3, 4] |
| accusum   | [0, 1, 4, 7, 0, -19, 68] |
| revaccusum | [0, 2, 4, -2, -24, 26, 428] |

EulerTanRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [0, 1, 0, -2, 0, 16, 0]|
| rdiag1 | [0, 2, 0, -8, 0, 96, 0]|
| rdiag2 | [0, 3, 0, -20, 0, 336, 0]|
| rdiag3 | [0, 4, 0, -40, 0, 896, 0]|
| rdiag4 | [0, 5, 0, -70, 0, 2016, 0]|
| rdiag5 | [0, 6, 0, -112, 0, 4032, 0]|
| rdiag6 | [0, 7, 0, -168, 0, 7392, 0]|

EulerTanRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| cdiag2 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag3 | [-2, -8, -20, -40, -70, -112, -168] |
| cdiag4 | [0, 0, 0, 0, 0, 0, 0] |
| cdiag5 | [16, 96, 336, 896, 2016, 4032, 7392] |
| cdiag6 | [0, 0, 0, 0, 0, 0, 0] |

EulerTanRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [0, 0, 0, 0, 0, 0, 0] |
| rpdiag1 | [0, 1, 2, 3, 4, 5, 6] |
| rpdiag2 | [0, 2, 4, 6, 8, 10, 12] |
| rpdiag3 | [0, 1, -10, -45, -116, -235, -414] |
| rpdiag4 | [0, -4, -56, -204, -496, -980, -1704] |
| rpdiag5 | [0, 1, 362, 3363, 15124, 47525, 120126] |
| rpdiag6 | [0, 62, 2764, 22266, 95768, 295030, 737892] |

EulerTanRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [0, 0, 0, 0, 0, 0, 0] |
| cpdiag1 | [0, 1, 2, 1, -4, 1, 62] |
| cpdiag2 | [0, 2, 4, -10, -56, 362, 2764] |
| cpdiag3 | [0, 3, 6, -45, -204, 3363, 22266] |
| cpdiag4 | [0, 4, 8, -116, -496, 15124, 95768] |
| cpdiag5 | [0, 5, 10, -235, -980, 47525, 295030] |
| cpdiag6 | [0, 6, 12, -414, -1704, 120126, 737892] |
