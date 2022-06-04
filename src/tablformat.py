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
