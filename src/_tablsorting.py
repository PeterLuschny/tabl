
import operator
from _tablpaths import GetCsvPath

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists where each inner list represents a row.
        cols:  a list specifying the column numbers to sort by,
               e.g. (1,0) would sort by column 1, then by column 0.
    """
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col))
    return table

def SortByAnum(table):
    return [row for row in sort_table(table, (2,1)) if row[2] != 'A000000']


def SortByTrait(table):
    return [row for row in sort_table(table, (1,2)) if row[2] != 'A000000']

def GetTraits(Tname: str):

    filepath = (GetCsvPath() / f"{Tname}.csv").resolve()
    seq_list = []
    with open(filepath, "r") as oeisdata:
        reader = csv.reader(oeisdata)
        seq_list = [[seq[0], seq[1], seq[2]] for seq in reader]
    return seq_list
 

if __name__ == '__main__':

    import csv
    from pathlib import Path
 
    for s in GetTraits("Abel"):
        print(s)

    for s in SortByAnum(GetTraits("Abel")):
        print(s)
    
    for s in SortByTrait(GetTraits("Bell")):
        print(s)
    