from io import TextIOWrapper
from os import getcwd
from os.path import join, isfile

tabl_files: list[str] = [
    "_tablinverse.py",
    "_tabltypes.py",
    "_tabltransforms.py",
    "_tablsums.py",
    "_tablviews.py",
    "_tablprofile.py",
    "Abel.py",
    "Baxter.py",
    "Bell.py",
    "Bessel.py",
    "Binomial.py",
    "Catalan.py",
    "CatalanAer.py",
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
    "Hermite.py",
    "Laguerre.py",
    "Lah.py",
    "Lehmer.py",
    "Leibniz.py",
    "Levin.py",
    "Lozanic.py",
    "Motzkin.py",
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
    "_tablmake.py",
    "_tablexport.py",
    "_tablhtml.py",
    "_tabldata.py",
    "_tablsimilarseq.py",
    "_tablsimilartri.py",
    "_tabltraitcard.py",
]

str_tabl_fun: str = """\
tabl_fun: list[tri] = [
    abel,
    baxter,
    bell,
    bessel,
    binomial,
    catalan,
    catalan_aerated,
    central_cycle,
    central_set,
    chebyshevS,
    chebyshevT,
    chebyshevU,
    compo,
    compo_max,
    ctree,
    delannoy,
    euler,
    eulerian,
    eulerian2,
    eulerianB,
    euler_sec,
    euler_tan,
    falling_factorial,
    fibonacci,
    fubini,
    fuss_catalan,
    gaussq2,
    genocchi,
    harmonic,
    hermite,
    laguerre,
    lah,
    lehmer,
    leibniz,
    levin,
    lozanic,
    motzkin,
    narayana,
    nicomachus,
    one,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_max,
    polygonal,
    powlag,
    rencontres,
    rising_factorial,
    schroeder,
    schroeder_paths,
    seidel,
    seidel_boust,
    sierpinski,
    stirling_cycle,
    stirling_cycle2,
    stirling_cycleB,
    stirling_set,
    stirling_set2,
    stirling_setB,
    sylvester,
    sympoly,
    ternary_tree,
    ward_set,
    worpitzky,
]\n""".format()

import_header: list[str] = [
    "from functools import cache, reduce\n",
    "from itertools import accumulate, count\n",
    "from math import lcm, gcd, floor, factorial\n",
    "from sys import setrecursionlimit\n",
    "from typing import Callable, TypeAlias\n",
    "from io import TextIOWrapper\n",
    "import contextlib\n",
    "import csv\n",
    "from fractions import Fraction as frac\n",
    "from sympy import Matrix, Rational\n",
]

data_path: list[str] = [
    "from pathlib import Path\n",
    "path = Path(__file__).parent\n",
    "reldatapath = 'data/oeis_data.csv'\n",
    "datapath = (path / reldatapath).resolve()\n",
    "relcsvpath = 'data/csv'\n",
    "csvpath = (path / relcsvpath).resolve()\n",
    "allcsvfile = 'data/allcsv.csv'\n",
    "allcsvpath = (path / allcsvfile).resolve()\n",
    "def GetDataPath() -> Path: return datapath\n",
    "def GetCsvPath() -> Path: return csvpath\n",
]


dir: str = join(getcwd(), "src")
dest: TextIOWrapper = open("tabl.py", "w+")

dest.writelines(import_header)
dest.writelines(data_path)
dest.write("setrecursionlimit(2100)\n")

for src in tabl_files:
    if src == "_tablmake.py":
        dest.write(str_tabl_fun)
        continue
    print(src)
    file_path: str = join(dir, src)
    if isfile(file_path):
        start: bool = False
        src_file: TextIOWrapper = open(file_path, "r")

        for line in src_file:
            if line.startswith("from"):
                continue
            if not start:
                start: bool = line.startswith("@") or line.startswith("# #@")
                if line.startswith("@"):
                    dest.write(line)
                continue
            else:
                start: bool = True
            if line.startswith("#"):
                continue
            if line.startswith("if __name__"):
                break
            if line != "\n":
                dest.write(line)
        src_file.close()
dest.close()
