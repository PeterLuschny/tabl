from tablformat import PrintTabl, PrintRows, PrintTerms
from tablgenerator import isTablGenerator
from sys import setrecursionlimit
import timeit


def TablTest(seq: callable, short=False):

    PrintTerms(seq, 3)
    PrintRows(seq, 10)
    PrintTabl(seq, 5)

    print(seq(5))
    print(seq(5, 3))

    print(isTablGenerator(seq))

    # Increase the default recursion limit
    setrecursionlimit(2000)

    big = 100 if short else 1000
    row = seq(big)
    print(row[big // 2] == seq(big, big // 2))
    print(row[big // 2])


def TablBenchmark(seq):
    print("BENCHMARK")
    setup = "from __main__ import seq"
    print(timeit.timeit("seq(-10)", setup=setup))
    print("FIN")
