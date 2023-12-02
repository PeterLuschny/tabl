from _tabltypes import tgen
from _tablpaths import GetDataPath
from _tablhtml import CsvToHtml
from _tabldata import SaveTraitsToDB, ConvertDBtoCSVandMD
from _tablstatistic import SingleStatistic, PrintSummary


# #@


def SingleMake(fun: tgen) -> None:
    """
    - Saves the traits of the triangle 'fun' to a database, a CSV file, and Markdown file.
    - Then the HTML file is updated.
    - The traits statistics is displayed.

    Args:
        fun (tgen): The generator of the triangle.

    Returns:
        None
    """
    SaveTraitsToDB(fun)
    ConvertDBtoCSVandMD(GetDataPath(fun.id, "db"), fun.id)
    CsvToHtml(fun)
    SingleStatistic(fun)
    PrintSummary(fun.id)


if __name__ == "__main__":
    from Eulerian import Eulerian as triangle
    SingleMake(triangle)
