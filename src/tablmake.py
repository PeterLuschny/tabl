from os import getcwd
from os.path import join, isfile

tabl_files = [
    "tabltools.py",
    "tablprint.py",
    "Abel.py",
    "Bell.py",
    "Bessel.py",
    "Binomial.py",
    "Catalan.py",
    "CatalanStreched.py",
    "CentralCycleFactorial.py",
    "CentralSetFactorial.py",
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
    "Hermite.py",
    "Laguerre.py",
    "Lah.py",
    "LehmerComtet.py",
    "Motzkin.py",
    "Narayana.py",
    "OrderedCycle.py",
    "Ordinals.py",
    "PartitionNumbers.py",
    "Rencontres.py",
    "RisingFactorial.py",
    "Schroeder.py",
    "Seidel.py",
    "StirlingCycle.py",
    "StirlingSet.py",
    "TernaryTrees.py",
    "Uno.py",
    "Ward.py",
    "Worpitzky.py",
]

import_header = [
    "from functools import cache\n",
    "from itertools import accumulate\n",
    "from sys import setrecursionlimit\n",
    "from typing import Callable\n",
]

dir = join(getcwd(), "src")
dest = open("tabl.py", "w+")

dest.writelines(import_header)
dest.write("setrecursionlimit(2000) \n")

for src in tabl_files:
    file_path = join(dir, src)
    if isfile(file_path):
        start = False if src.startswith("tabl") else True
        src_file = open(file_path, "r")

        for line in src_file:
            if line.startswith("from"):
                continue
            if start and not line.startswith("@"):
                continue
            start = False
            if line.startswith("#"):
                break
            if line != "\n":
                dest.write(line)
        src_file.close()

dest.close()
