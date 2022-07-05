import timeit

# UNDER CONSTRUCTION -- IGNORE

def TablBenchmark(seq):
    print("BENCHMARK")
    setup = "from __main__ import seq"
    print(timeit.timeit("seq(-10)", setup=setup))
    print("FIN")
