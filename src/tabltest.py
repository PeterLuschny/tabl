from tablgenerator import isTablGenerator
from sys import setrecursionlimit
import timeit


def PrintTabl(T):
    print(T)


def PrintRows(T):
    for n, row in enumerate(T):
        print([n], row)


def PrintTerms(T):
    for n, row in enumerate(T):
        for k, term in enumerate(row):
            print([n, k], term)


def TablTest(seq: callable):
    PrintTerms(seq(-3))
    PrintRows(seq(-10))
    PrintTabl(seq(-5))

    print(seq(5))
    print(seq(5, 3))

    print(isTablGenerator(seq))

    # Increase the default recursion limit
    setrecursionlimit(2000)
    row = seq(1000)
    print(row[500] == seq(1000, 500))
    print(row[500])


def TablBenchmark(seq):
    print("BENCHMARK")
    setup = "from __main__ import seq"
    print(timeit.timeit("seq(-10)", setup=setup))
    print("FIN")
