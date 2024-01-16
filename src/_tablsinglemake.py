from _tablmake import MakeTabl
from tabl import *

# Make sure that everything is up to date but do not include
# 'MakeTabl' in 'SingleMake' as this would be circular.
MakeTabl()


# #@


def SingleMake(fun: tgen) -> None:
    """
    - Saves the traits of the triangle 'fun' to a database, a CSV file, and Markdown file.
    - Then the HTML file is created/updated.
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
    from Abel import Abel as triangle
    SingleMake(triangle)
