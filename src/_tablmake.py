from os import getcwd
from os.path import join, isfile


tabl_files: list[str] = [
    "_tablpaths.py",
    "_tablinverse.py",
    "_tabltypes.py",
    "_tabltabls.py",
    "_tablpoly.py",
    "_tabltransforms.py",
    "_tablsums.py",
    "_tablviews.py",
    "Abel.py",
    "Baxter.py",
    "Bell.py",
    "Bessel.py",
    "Bessel2.py",
    "BinaryPell.py",
    "Binomial.py",
    "BinomialBell.py",
    "BinomialCatalan.py",
    "BinomialPell.py",
    "BinomialDiffPell.py",
    "Catalan.py",
    "CatalanPaths.py",
    "CentralCyc.py",
    "CentralSet.py",
    "Chains.py",
    "Charlier.py",
    "ChebyshevS.py",
    "ChebyshevT.py",
    "ChebyshevU.py",
    "Composition.py",
    "CompositionMax.py",
    "CTree.py",
    "Delannoy.py",
    "Divisibility.py",
    "DistLattices.py",
    "DyckPaths.py",
    "Euclid.py",
    "Euler.py",
    "Eulerian.py",
    "Eulerian2.py",
    "EulerianB.py",
    "EulerianZigZag.py",
    "EulerSec.py",
    "EulerTan.py",
    "FallingFact.py",
    "Fibonacci.py",
    "Fubini.py",
    "FussCatalan.py",
    "Gaussq2.py",
    "Genocchi.py",
    "Harmonic.py",
    "HermiteE.py",
    "HermiteH.py",
    "HyperHarmonic.py",
    "Kekule.py",
    "LabeledGraphs.py",
    "Laguerre.py",
    "Lah.py",
    "Lehmer.py",
    "Leibniz.py",
    "Levin.py",
    "Lozanic.py",
    "Moebius.py",
    "Monotone.py",
    "Motzkin.py",
    "MotzkinPoly.py",
    "Narayana.py",
    "Naturals.py",
    "Nicomachus.py",
    "One.py",
    "Ordinals.py",
    "OrderedCyc.py",
    "Parades.py",
    "Partition.py",
    "PartitionDist.py",
    "PartitionMax.py",
    "Pascal.py",
    "Polygonal.py",
    "PowLaguerre.py",
    "Rencontres.py",
    "RisingFact.py",
    "Schroeder.py",
    "SchroederPaths.py",
    "SchroederL.py",
    "Seidel.py",
    "SeidelBoust.py",
    "Sierpinski.py",
    "StirlingCycle.py",
    "StirlingCyc2.py",
    "StirlingCycB.py",
    "StirlingSet.py",
    "StirlingSet2.py",
    "StirlingSetB.py",
    "Sylvester.py",
    "TernaryTrees.py",
    "WardSet.py",
    "Worpitzky.py",
    "NumBell.py",
    "NumBernoulli.py",
    "NumDivisors",
    "NumEuler.py",
    "NumEulerPhi.py",
    "NumMotzkin.py",
    "NumPartLists.py",
    "NumParts.py",
    "NumRiordan.py",
    "_tablmake.py",
    "_tablexport.py",
    "_tablhtml.py",
    "_tabltraits.py",
    "_tablstatistic.py",
    "_tabldata.py",
    "_tablsinglemake.py",
]


str_tabl_fun: str = """\
tabl_fun: list[tgen] = [
    Abel,
    Baxter,
    Bell,
    Bessel,
    Bessel2,
    BinaryPell,
    Binomial,
    BinomialBell,
    BinomialCatalan,
    BinomialPell,
    BinomialDiffPell,
    Catalan,
    CatalanPaths,
    CentralCycle,
    CentralSet,
    Chains,
    Charlier,
    ChebyshevS,
    ChebyshevT,
    ChebyshevU,
    Composition,
    CompoMax,
    CTree,
    Delannoy,
    Divisibility,
    DyckPaths,
    Euclid,
    Euler,
    Eulerian,
    Eulerian2,
    EulerianB,
    EulerianZigZag,
    EulerSec,
    EulerTan,
    FallingFactorial,
    Fibonacci,
    Fubini,
    FussCatalan,
    Gaussq2,
    Genocchi,
    Harmonic,
    HermiteE,
    HermiteH,
    HyperHarmonic,
    Kekule,
    LabeledGraphs,
    Laguerre,
    Lah,
    Lehmer,
    Leibniz,
    Levin,
    Lozanic,
    Moebius,
    Monotone,
    Motzkin,
    MotzkinPoly,
    Narayana,
    Naturals,
    Nicomachus,
    One,
    Ordinals,
    OrderedCycle,
    Parades,
    PartnumExact,
    PartnumDist,
    PartnumMax,
    Pascal,
    Polygonal,
    PowLaguerre,
    Rencontres,
    RisingFactorial,
    Schroeder,
    SchroederL,
    SchroederPaths,
    Seidel,
    SeidelBoust,
    Sierpinski,
    StirlingCycle,
    StirlingCycle2,
    StirlingCycleB,
    StirlingSet,
    StirlingSet2,
    StirlingSetB,
    Sylvester,
    TernaryTree,
    WardSet,
    Worpitzky,
]\n""".format()

import_header: list[str] = [
    "from os import remove\n",
    "import datetime\n",
    "from functools import cache, reduce\n",
    "from itertools import accumulate\n",
    "from math import lcm, gcd, factorial\n",
    "from sys import setrecursionlimit, set_int_max_str_digits\n",
    "from typing import Callable, TypeAlias\n",
    "from inspect import signature\n",
    # "from tabulate import tabulate\n",  # needed by pandas
    "import traceback\n",
    "import contextlib\n",
    "import csv\n",
    "import urllib.request\n",
    "import urllib.error\n",
    "import requests\n",
    "from requests import get\n",
    "import time\n",
    "import gzip\n",
    "import sqlite3\n",
    "import pandas as pd\n",
    "from fractions import Fraction\n",
    "from pathlib import Path\n",
]


def MakeTabl() -> None:
    """
    This function generates a 'tabl.py' file by combining the contents of multiple source files.
    It reads the source files from the 'src' directory and writes the combined content to 'tabl.py'.
    The function also sets the recursion limit and the maximum number of digits for integer conversion.

    Parameters:
    None

    Returns:
    None
    """
    dir = join(getcwd(), "src")
    dest = open(join(dir, "tabl.py"), "w+", encoding="utf-8")

    dest.writelines(import_header)
    dest.write("setrecursionlimit(3000)\n")
    dest.write("set_int_max_str_digits(5000)\n")

    for src in tabl_files:
        if src == "_tablmake.py":
            dest.write(str_tabl_fun)
            continue
        print(src)
        file_path: str = join(dir, src)
        if isfile(file_path):
            start: bool = False
            src_file = open(file_path, "r", encoding="utf-8")

            for line in src_file:
                if line.startswith("from"):
                    continue
                if not start:
                    start = line.startswith("@") or line.startswith("# #@")
                    if line.startswith("@"):
                        dest.write(line)
                    continue
                else:
                    start = True
                if line.startswith("#"):
                    continue
                if line.startswith("if __name__"):
                    break
                if line != "\n":
                    dest.write(line)
            src_file.close()
    dest.close()


if __name__ == "__main__":
    MakeTabl()
