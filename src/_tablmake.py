# from io import TextIOWrapper
from os import getcwd
from os.path import join, isfile

tabl_files: list[str] = [
    "_tablinverse.py",
    "_tabltypes.py",
    "_tabltabls.py",
    "_tablpoly.py",
    "_tabltransforms.py",
    "_tablsums.py",
    "_tablviews.py",
    "_tablprofile.py",
    "Abel.py",
    "Baxter.py",
    "Bell.py",
    "Bessel.py",
    "Bessel2.py",
    "Binomial.py",
    "BinomialBell.py",
    "BinomialCatalan.py",
    "Catalan.py",
    "CatalanAer.py",
    "CatalanSqr.py",
    "CentralCyc.py",
    "CentralSet.py",
    "ChebyshevS.py",
    "ChebyshevT.py",
    "ChebyshevU.py",
    "ChristTree.py",
    "Composition.py",
    "CompositionMax.py",
    "Delannoy.py",
    "Euler.py",
    "Eulerian.py",
    "Eulerian2.py",
    "EulerianB.py",
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
    "LabeledGraphs.py",
    "Laguerre.py",
    "Lah.py",
    "Lehmer.py",
    "Leibniz.py",
    "Levin.py",
    "Lozanic.py",
    "Motzkin.py",
    "MotzkinGF.py",
    "Narayana.py",
    "Nicomachus.py",
    "One.py",
    "Ordinals.py",
    "OrderedCyc.py",
    "Partition.py",
    "PartitionMax.py",
    "Polygonal.py",
    "PowLaguerre.py",
    "Rencontres.py",
    "RisingFact.py",
    "Schroeder.py",
    "SchroederP.py",
    "SchroederL.py",
    "Seidel.py",
    "SeidelBoust.py",
    "Sierpinski.py",
    "StirlingCyc.py",
    "StirlingCyc2.py",
    "StirlingCycB.py",
    "StirlingSet.py",
    "StirlingSet2.py",
    "StirlingSetB.py",
    "Sylvester.py",
    "SymPoly.py",
    "TernaryTrees.py",
    "WardSet.py",
    "Worpitzky.py",
    "NumBell.py",
    "NumBernoulli.py",
    "NumEuler.py",
    "NumMotzkin.py",
    "NumPartLists.py",
    "NumParts.py",
    "NumRiordan.py",
    "_tablmake.py",
    "_tablexport.py",
    "_tablhtml.py",
    "_tabldata.py",
    "_tabltraitcard.py",
]


str_tabl_fun: str = """\
tabl_fun: list[tgen] = [
    Abel,
    Baxter,
    Bell,
    Bessel,
    Bessel2,
    Binomial,
    BinomialBell,
    BinomialCatalan,
    Catalan,
    CatalanAer,
    CatalanSqr,
    CentralCycle,
    CentralSet,
    ChebyshevS,
    ChebyshevT,
    ChebyshevU,
    Composition,
    CompoMax,
    Ctree,
    Delannoy,
    Euler,
    Eulerian,
    Eulerian2,
    EulerianB,
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
    LabeledGraphs,
    Laguerre,
    Lah,
    Lehmer,
    Leibniz,
    Levin,
    Lozanic,
    Motzkin,
    MotzkinGF,
    Narayana,
    Nicomachus,
    One,
    Ordinals,
    OrderedCycle,
    PartnumExact,
    PartnumMax,
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
    Sympoly,
    TernaryTree,
    WardSet,
    Worpitzky,
]\n""".format()

import_header: list[str] = [
    "from functools import cache, reduce\n",
    "from itertools import accumulate\n",
    "from math import lcm, gcd, factorial\n",
    "from sys import setrecursionlimit, set_int_max_str_digits\n",
    "from typing import Callable, TypeAlias\n",
    "import contextlib\n",
    "import csv\n",
    "import requests\n",
    "import gzip\n",
    "from fractions import Fraction as frac\n",
    "from sympy import Matrix, Rational\n",
]

data_path: list[str] = [
    "from pathlib import Path\n",
    "path = Path(__file__).parent\n",
    "reldatapath = 'data/oeis_data.csv'\n",
    "datapath = (path / reldatapath).resolve()\n",
    "reloeispath = 'data/oeis.csv'\n",
    "oeispath = (path / reloeispath).resolve()\n",
    "relstrippedpath = 'data/stripped'\n"
    "strippedpath = (path / relstrippedpath).resolve()\n"
    "relcsvpath = 'data/csv'\n",
    "csvpath = (path / relcsvpath).resolve()\n",
    "allcsvfile = 'data/allcsv.csv'\n",
    "allcsvpath = (path / allcsvfile).resolve()\n",
    "relhtmlpath = 'data/html'\n",
    "htmlpath = (path / relhtmlpath).resolve()\n",
    "relmdpath = 'data/md'\n",
    "mdpath = (path / relmdpath).resolve()\n",
    "def GetDataPath() -> Path: return datapath\n",
    "def GetCsvPath() -> Path: return csvpath\n",
    "def GetAllCsvPath() -> Path: return allcsvpath\n",
    "def GetHtmlPath() -> Path: return htmlpath\n",
    "def GetMdPath() -> Path: return mdpath\n",
]

def make() -> None:
    dir: str = join(getcwd(), "src")
    dest = open("tabl.py", "w+")

    dest.writelines(import_header)
    dest.writelines(data_path)
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
            src_file = open(file_path, "r")

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

    make()
