'''
This script generates a 'tabl.py' file by combining the contents of multiple source files.
The script also sets the recursion limit and the maximum number of digits for integer conversion.
Modules:
    os: Provides functions for interacting with the operating system.
    os.path: Provides functions for manipulating file paths.
    datetime: Supplies classes for manipulating dates and times.
    functools: Provides higher-order functions that act on or return other functions.
    itertools: Implements a number of iterator building blocks.
    math: Provides access to mathematical functions.
    sys: Provides access to some variables used or maintained by the interpreter.
    typing: Provides runtime support for type hints.
    inspect: Provides several useful functions to help get information about live objects.
    traceback: Provides a standard interface to extract, format, and print stack traces of Python programs.
    contextlib: Utilities for common tasks involving the with statement.
    csv: Implements classes to read and write tabular data in CSV format.
    requests: Allows you to send HTTP requests.
    time: Provides various time-related functions.
    gzip: Provides a simple interface to compress and decompress files.
    sqlite3: Provides a SQL interface compliant with the DB-API 2.0 specification.
    pandas: Provides data structures and data analysis tools.
    fractions: Provides support for rational number arithmetic.
    pathlib: Offers classes representing filesystem paths with semantics appropriate for different operating systems.
Functions:
    MakeTabl: Generates a 'tabl.py' file by combining the contents of multiple source files.
Usage:
    Run this script directly to generate the 'tabl.py' file.
'''

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
    "CentralCycle.py",
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
    "FiboLucas.py",
    "FiboLucasInv.py",
    "FiboLucasRev.py",
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
    "Lucas.py",
    "LucasPoly.py",
    "Moebius.py",
    "Monotone.py",
    "Motzkin.py",
    "MotzkinPoly.py",
    "Narayana.py",
    "Naturals.py",
    "Nicomachus.py",
    "One.py",
    "Ordinals.py",
    "OrderedCycle.py",
    "Parades.py",
    "Partition.py",
    "PartitionDist.py",
    "PartitionMax.py",
    "Pascal.py",
    "Polygonal.py",
    "Powers.py",
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
    "StirlingCycle2.py",
    "StirlingCycleB.py",
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
    "_tabloeis.py",
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
    FiboLucas,
    FiboLucasInv,
    FiboLucasRev,
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
    Lucas,
    LucasPoly,
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
    Powers,
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
    TernaryTrees,
    WardSet,
    Worpitzky,
]\n""".format()

import_header: list[str] = [
    "from os import remove\n",
    "from datetime import datetime\n",
    "from functools import cache, reduce\n",
    "from itertools import accumulate\n",
    "from math import lcm, gcd, factorial\n",
    "from sys import setrecursionlimit, set_int_max_str_digits\n",
    "from typing import Callable, TypeAlias, Any\n",
    "from inspect import signature\n",
    "import traceback\n",
    "import contextlib\n",
    "import csv\n",
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
