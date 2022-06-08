import re
from datetime import date


def write_oeis_bfile(anum, range, seq, comments, targetdir):
    """
    :param anum: str oeis-A-number
    :param range: range the sequence is to be evaluated on
    :param seq: callable[int] -> int
                the sequence function to be evaluated
    :param comments: list[str] header of the file
    :param targetdir: str directory to put the b-file

    Example usage:

    comments = ["Author: Louisa Lovely",
                "Software: Python 10.4",
                "The divergent series par excellence." ]

    def a(n): return factorial(n)
    path = "C:/Users/Home/"

    write_oeis_bfile("A000142", range(11), a, comments, path)
    """
    if not re.match("^A[0-9]{6}$", anum):
        print("Not a valid A-number! Exiting.")
        return
    filename = targetdir + "b" + anum[1:] + ".txt"
    print("Writing " + anum + " to " + filename)

    file = open(filename, "w+")
    file.write("# OEIS: " + anum + "\n")
    today = date.today()
    timestamp = today.isoformat()
    file.write("# " + timestamp + "\n")
    for c in comments:
        file.write("# " + c + "\n")
    for n in range:
        val = seq(n)
        if len(str(val)) > 1000:
            print("Term too long, exiting.")
            break
        file.write(str(n) + " " + str(val) + "\n")
    file.write("\n")
    file.close()
