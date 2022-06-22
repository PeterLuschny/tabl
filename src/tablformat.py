def PrintTabl(T, k=None):
    t = T if k == None else T(-k)
    print(t)


def PrintRows(T, k=None):
    t = T if k == None else T(-k)
    for n, row in enumerate(t):
        print([n], row)


def PrintTerms(T, k=None):
    t = T if k == None else T(-k)
    for n, row in enumerate(t):
        for k, term in enumerate(row):
            print([n, k], term)


def PrintRowArray(F, rows, cols):
    for j in range(rows):
        print([F(j + k, k) for k in range(cols)])


def PrintColArray(F, rows, cols):
    for j in range(cols):
        print([F(j + k, j) for k in range(rows)])


def PrintViews(T, rows=7, cols=None, verbose=True):
    if cols == None: cols = rows
    print()
    if verbose: print("Triangle view")
    PrintRows(T(-rows))
    print()
    if verbose: print("Diagonals -> rows")
    PrintRowArray(T, rows, cols)
    print()
    if verbose: print("Diagonals -> columns")
    PrintColArray(T, rows, cols)
    print()
