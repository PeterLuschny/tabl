from tablgenerator import isTablGenerator
from sys import setrecursionlimit
import timeit


def PrintTabl(T):
    for n, row in enumerate(T):
        print([n], row)


def TablTest(seq: callable):
    PrintTabl(seq(-10))
    print(isTablGenerator(seq))

    # Increase the default recursion
    setrecursionlimit(2000)

    print(seq(-6))
    print(seq(6))
    print(seq(6, 4))
    row = seq(1000)
    print(row[500] == seq(1000, 500))


def TablBenchmark(seq):
    print("BENCHMARK")
    setup = "from __main__ import seq"
    print(timeit.timeit("seq(-10)", setup=setup))
    print("FIN")
