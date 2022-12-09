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
    "Bell.py",
    "Bessel.py",
    "Binomial.py",
    "Catalan.py",
    "CatalanAerated.py",
    "CentralCycleFactorial.py",
    "CentralSetFactorial.py",
    "ChebyshevU2.py",
    "Delannoy.py",
    "Euler.py",
    "Eulerian.py",
    "Eulerian2.py",
    "EulerianB.py",
    "EulerSecant.py",
    "EulerTangent.py",
    "FallingFactorial.py",
    "Fibonacci.py",
    "Fubini.py",
    "Genocchi.py",
    "HarmonicPolys.py",
    "Hermite.py",
    "Laguerre.py",
    "Lah.py",
    "LehmerComtet.py",
    "Leibniz.py",
    "Levin.py",
    "Motzkin.py",
    "Narayana.py",
    "Nicomachus.py",
    "Ordinals.py",
    "OrderedCycle.py",
    "PartitionNumbers.py",
    "PolygonalNumbers.py",
    "PowerLaguerre.py",
    "Rencontres.py",
    "RisingFactorial.py",
    "Schroeder.py",
    "SchroederBiPaths.py",
    "Seidel.py",
    "StirlingCycle.py",
    "StirlingSet.py",
    "StirlingCycle2.py",
    "StirlingSet2.py",
    "SymmetricPolynomial.py",
    "TernaryTrees.py",
    "Uno.py",
    "WardCycle.py",
    "WardSet.py",
    "Worpitzky.py",
    "_tablmake.py",
    "_tablexport.py",
    "_tablsearch.py",
]

str_tabl_fun: str = '''\
tabl_fun: list[tri] = [
    abel,
    bell,
    bessel,
    bilatpath,
    binomial,
    catalan,
    catalan_aerated,
    cc_factorial,
    cs_factorial,
    chebyshevU2,
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
    genocchi,
    harmonic,
    hermite,
    laguerre,
    lah,
    lehmer,
    leibniz,
    levin,
    motzkin,
    narayana,
    nicomachus,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_atmost,
    polygonal,
    powlag,
    rencontres,
    rising_factorial,
    schroeder,
    seidel,
    seidel_boust,
    stirling_cycle,
    stirling_set,
    stirling_cycle2,
    stirling_set2,
    sympoly,
    ternary_tree,
    uno,
    ward_cycle,
    ward_set,
    worpitzky,
]\n'''.format()

import_header: list[str] = [
    "from functools import cache\n",
    "from itertools import accumulate\n",
    "from sys import setrecursionlimit\n",
    "from typing import Callable, TypeAlias\n",
    "from io import TextIOWrapper\n",
    "from pathlib import Path\n",
    "import contextlib\n",
    "import csv\n",
    "from sympy import Matrix, Rational\n",
]

dir: str = join(getcwd(), "src")
dest: TextIOWrapper = open("tabl.py", "w+")

dest.writelines(import_header)
dest.write("setrecursionlimit(2100)\n")

for src in tabl_files:
    if src == "_tablmake.py":
        dest.write(str_tabl_fun)
        continue
    file_path: str = join(dir, src)
    if isfile(file_path):
        start: bool = False
        src_file: TextIOWrapper = open(file_path, "r")

        for line in src_file:
            if line.startswith("@set_attributes("):
                s = line[1+line.find('"') : line.rfind('"')]
                print(s)
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