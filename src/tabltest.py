from tablformat import PrintAll
from tablgenerator import isTablGenerator
from sys import setrecursionlimit


def TablTest(seq: callable, dim=7, short=False):

    PrintAll(seq, dim)

    seqname = seq.__name__
    print("py>", seqname, "(5) =", seq(5))
    print("py>", seqname, "(5, 3) =", seq(5, 3))
    print("py> isTablGenerator(", seqname, ") =", isTablGenerator(seq))

    # Increase the default recursion limit
    setrecursionlimit(2000)

    big = 100 if short else 1000
    Trow = seq(big)
    b = str(big); b2 = str(big // 2)
    print("py> Trow[", b2, "] ==", seqname, "(", b, ",", b2, ") =", 
           Trow[big // 2] == seq(big, big // 2))
    print("py>", seqname, "(", b, ",", b2, ") =") 
    print(Trow[big // 2])
    print()
