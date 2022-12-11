import csv

# #@

# Special edition of the data file, only for internal use.
# (1) Disregards sequences with less than 28 items (first 6 lines of a triangle),
# (2) makes all items absolute,
# (3) shortens the sequence to 28 entries.
# But otherwise keeps the format of the compressed file.
def shortabsdata(inpath: str, outpath: str) -> None:

    with open(inpath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], [abs(int(t)) for t in seq[1:-1]]] for seq in reader]
        with open(outpath, "w") as outfile:
            for seq in seq_list:
                if len(seq[1]) < 29:
                    continue
                s = (
                    str(seq[1][0:28])
                    .replace("[", ",")
                    .replace("]", ",")
                    .replace(" ", "")
                )
                outfile.write(str(seq[0]) + s + "\n")
