import re
from datetime import date
from io import TextIOWrapper
from typing import Callable


def write_oeis_bfile(
    anum: str,
    rng: range,
    seq: Callable[[int], int],
    comments: list[str],
    targetdir: str,
) -> None:
    """
    :param anum: oeis-A-number
    :param range: range the sequence is to be evaluated on
    :param seq: the sequence function to be evaluated
    :param comments: header of the file
    :param targetdir: directory to put the b-file

    Example usage:

    comments = ["Author: Louisa Lovely",
                "Software: Python 10.4",
                "The divergent series par excellence." ]

    def seq(n: int) -> int: return factorial(n)
    path = "C:/Users/Home/"

    write_oeis_bfile("A000142", range(11), seq, comments, path)
    """
    if not re.match("^A[0-9]{6}$", anum):
        print("Not a valid A-number! Exiting.")
        return

    filename: str = targetdir + "b" + anum[1:] + ".txt"
    print("Writing " + anum + " to " + filename)

    file: TextIOWrapper = open(filename, "w+")
    file.write("# OEIS: " + anum + "\n")
    today: date = date.today()
    timestamp: str = today.isoformat()
    file.write("# " + timestamp + "\n")
    for c in comments:
        file.write("# " + c + "\n")
    for n in rng:
        val: int = seq(n)
        if len(str(val)) > 1000:
            print("Term too long, exiting.")
            break
        file.write(str(n) + " " + str(val) + "\n")
    file.write("\n")
    file.close()
    print("Done!")
