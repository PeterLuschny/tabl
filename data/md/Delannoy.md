# Delannoy
['A008288']

Delannoy Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [1, 3, 1] |
| trow3 | [1, 5, 5, 1] |
| trow4 | [1, 7, 13, 7, 1] |
| trow5 | [1, 9, 25, 25, 9, 1] |
| trow6 | [1, 11, 41, 63, 41, 11, 1] |

Delannoy Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 1, 3, 1, 1, 5, 5, 1, 1, 7, 13, 7, 1, 1, 9, 25, 25, 9, 1, 1, 11, 41, 63, 41, 11, 1] |
| rev      | [1, 1, 1, 1, 3, 1, 1, 5, 5, 1, 1, 7, 13, 7, 1, 1, 9, 25, 25, 9, 1, 1, 11, 41, 63, 41, 11, 1] |
| accu     | [1, 1, 2, 1, 4, 5, 1, 6, 11, 12, 1, 8, 21, 28, 29, 1, 10, 35, 60, 69, 70, 1, 12, 53, 116, 157, 168, 169] |
| revaccu  | [1, 2, 1, 5, 4, 1, 12, 11, 6, 1, 29, 28, 21, 8, 1, 70, 69, 60, 35, 10, 1, 169, 168, 157, 116, 53, 12, 1] |
| accurev  | [1, 1, 2, 1, 4, 5, 1, 6, 11, 12, 1, 8, 21, 28, 29, 1, 10, 35, 60, 69, 70, 1, 12, 53, 116, 157, 168, 169] |
| diag     | [1, 1, 1, 1, 1, 3, 1, 5, 1, 1, 7, 5] |

Delannoy Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 5, 12, 29, 70, 169] |
| evensum   | [1, 1, 2, 6, 15, 35, 84] |
| oddsum    | [0, 1, 3, 6, 14, 35, 85] |
| altsum    | [1, 0, -1, 0, 1, 0, -1] |
| diagsum   | [1, 1, 2, 4, 7, 13] |
| accusum   | [1, 3, 10, 30, 87, 245, 676] |
| revaccusum | [1, 3, 10, 30, 87, 245, 676] |

Delannoy Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [1, 3, 5, 7, 9, 11, 13]|
| rdiag2 | [1, 5, 13, 25, 41, 61, 85]|
| rdiag3 | [1, 7, 25, 63, 129, 231, 377]|
| rdiag4 | [1, 9, 41, 129, 321, 681, 1289]|
| rdiag5 | [1, 11, 61, 231, 681, 1683, 3653]|
| rdiag6 | [1, 13, 85, 377, 1289, 3653, 8989]|

Delannoy Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [1, 3, 5, 7, 9, 11, 13] |
| cdiag2 | [1, 5, 13, 25, 41, 61, 85] |
| cdiag3 | [1, 7, 25, 63, 129, 231, 377] |
| cdiag4 | [1, 9, 41, 129, 321, 681, 1289] |
| cdiag5 | [1, 11, 61, 231, 681, 1683, 3653] |
| cdiag6 | [1, 13, 85, 377, 1289, 3653, 8989] |

Delannoy Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [1, 5, 11, 19, 29, 41, 55] |
| rpdiag3 | [1, 12, 39, 88, 165, 276, 427] |
| rpdiag4 | [1, 29, 139, 409, 941, 1861, 3319] |
| rpdiag5 | [1, 70, 495, 1900, 5365, 12546, 25795] |
| rpdiag6 | [1, 169, 1763, 8827, 30589, 84581, 200479] |

Delannoy Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 2, 5, 12, 29, 70, 169] |
| cpdiag2 | [1, 3, 11, 39, 139, 495, 1763] |
| cpdiag3 | [1, 4, 19, 88, 409, 1900, 8827] |
| cpdiag4 | [1, 5, 29, 165, 941, 5365, 30589] |
| cpdiag5 | [1, 6, 41, 276, 1861, 12546, 84581] |
| cpdiag6 | [1, 7, 55, 427, 3319, 25795, 200479] |

# DelannoyRev
True

DelannoyRev Triangle view
| trow  |  list  |
| :---  |  :---  |
| trow0 | [1] |
| trow1 | [1, 1] |
| trow2 | [1, 3, 1] |
| trow3 | [1, 5, 5, 1] |
| trow4 | [1, 7, 13, 7, 1] |
| trow5 | [1, 9, 25, 25, 9, 1] |
| trow6 | [1, 11, 41, 63, 41, 11, 1] |

DelannoyRev Flattened seqs
| flat      |   seq  |
| :---      |  :---  |
| tabl     | [1, 1, 1, 1, 3, 1, 1, 5, 5, 1, 1, 7, 13, 7, 1, 1, 9, 25, 25, 9, 1, 1, 11, 41, 63, 41, 11, 1] |
| rev      | [1, 1, 1, 1, 3, 1, 1, 5, 5, 1, 1, 7, 13, 7, 1, 1, 9, 25, 25, 9, 1, 1, 11, 41, 63, 41, 11, 1] |
| accu     | [1, 1, 2, 1, 4, 5, 1, 6, 11, 12, 1, 8, 21, 28, 29, 1, 10, 35, 60, 69, 70, 1, 12, 53, 116, 157, 168, 169] |
| revaccu  | [1, 2, 1, 5, 4, 1, 12, 11, 6, 1, 29, 28, 21, 8, 1, 70, 69, 60, 35, 10, 1, 169, 168, 157, 116, 53, 12, 1] |
| accurev  | [1, 1, 2, 1, 4, 5, 1, 6, 11, 12, 1, 8, 21, 28, 29, 1, 10, 35, 60, 69, 70, 1, 12, 53, 116, 157, 168, 169] |
| diag     | [1, 1, 1, 1, 1, 3, 1, 5, 1, 1, 7, 5] |

DelannoyRev Row sums
| sum        |   seq  |
| :---       |  :---  |
| sum       | [1, 2, 5, 12, 29, 70, 169] |
| evensum   | [1, 1, 2, 6, 15, 35, 84] |
| oddsum    | [0, 1, 3, 6, 14, 35, 85] |
| altsum    | [1, 0, -1, 0, 1, 0, -1] |
| diagsum   | [1, 1, 2, 4, 7, 13] |
| accusum   | [1, 3, 10, 30, 87, 245, 676] |
| revaccusum | [1, 3, 10, 30, 87, 245, 676] |

DelannoyRev Diagonals as rows
| rdiag  |   seq  |
| :---   |  :---  |
| rdiag0 | [1, 1, 1, 1, 1, 1, 1]|
| rdiag1 | [1, 3, 5, 7, 9, 11, 13]|
| rdiag2 | [1, 5, 13, 25, 41, 61, 85]|
| rdiag3 | [1, 7, 25, 63, 129, 231, 377]|
| rdiag4 | [1, 9, 41, 129, 321, 681, 1289]|
| rdiag5 | [1, 11, 61, 231, 681, 1683, 3653]|
| rdiag6 | [1, 13, 85, 377, 1289, 3653, 8989]|

DelannoyRev Diagonals as columns
| cdiag  |   seq  |
| :---   |  :---  |
| cdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cdiag1 | [1, 3, 5, 7, 9, 11, 13] |
| cdiag2 | [1, 5, 13, 25, 41, 61, 85] |
| cdiag3 | [1, 7, 25, 63, 129, 231, 377] |
| cdiag4 | [1, 9, 41, 129, 321, 681, 1289] |
| cdiag5 | [1, 11, 61, 231, 681, 1683, 3653] |
| cdiag6 | [1, 13, 85, 377, 1289, 3653, 8989] |

DelannoyRev Polynomial values as rows
| rpdiag  |   seq  |
| :---    |  :---  |
| rpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| rpdiag1 | [1, 2, 3, 4, 5, 6, 7] |
| rpdiag2 | [1, 5, 11, 19, 29, 41, 55] |
| rpdiag3 | [1, 12, 39, 88, 165, 276, 427] |
| rpdiag4 | [1, 29, 139, 409, 941, 1861, 3319] |
| rpdiag5 | [1, 70, 495, 1900, 5365, 12546, 25795] |
| rpdiag6 | [1, 169, 1763, 8827, 30589, 84581, 200479] |

DelannoyRev Polynomial values as columns
| cpdiag  |   seq  |
| :---    |  :---  |
| cpdiag0 | [1, 1, 1, 1, 1, 1, 1] |
| cpdiag1 | [1, 2, 5, 12, 29, 70, 169] |
| cpdiag2 | [1, 3, 11, 39, 139, 495, 1763] |
| cpdiag3 | [1, 4, 19, 88, 409, 1900, 8827] |
| cpdiag4 | [1, 5, 29, 165, 941, 5365, 30589] |
| cpdiag5 | [1, 6, 41, 276, 1861, 12546, 84581] |
| cpdiag6 | [1, 7, 55, 427, 3319, 25795, 200479] |
