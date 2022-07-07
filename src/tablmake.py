from os import getcwd
from os.path import join, isfile

tabl_files = [
    "tabltools.py",
    "tablsums.py",
    "tablprint.py",
    "tablprofile.py",
    "Abel.py",
    "Bell.py",
    "Bessel.py",
    "Binomial.py",
    "Catalan.py",
    "CatalanAerated.py",
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
    "PolygonalNumbers.py",
    "Rencontres.py",
    "RisingFactorial.py",
    "Schroeder.py",
    "Seidel.py",
    "StirlingCycle.py",
    "StirlingSet.py",
    "SymmetricPolynomial.py",
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
        start = False 
        src_file = open(file_path, "r")

        for line in src_file:
            if line.startswith("from"):
                continue
            if not start: 
                start = line.startswith("@") or line.startswith("#@")
                if line.startswith("@"): 
                    dest.write(line)
                continue
            else:
                start = True
            if line.startswith("#"):
                break
            if line != "\n":
                dest.write(line)
        src_file.close()

s = '''\
tabl_fun = [
    abel,
    bell,
    bessel,
    binomial,
    catalan,
    catalan_aerated,
    cc_factorial,
    cs_factorial,
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
    hermite,
    laguerre,
    lah,
    lehmer,
    motzkin,
    narayana,
    ordinals,
    ordered_cycle,
    partnum_exact,
    partnum_atmost,
    polygonal,
    rencontres,
    rising_factorial,
    schroeder,
    seidel,
    seidel_boust,
    stirling_cycle,
    stirling_set,
    sympoly,
    ternary_tree,
    uno,
    ward,
    worpitzky,
]\n'''.format(length='multi-line', ordinal='second')
dest.write(s)

dest.close()
