# https://github.com/jazzband/prettytable

from tabulate import tabulate

# #@

table = [
        ["Row0", [1]],
        ["Row1", [0, 1]],
        ["Row2", [0, 2, 1]],
        ["Row3", [0, 9, 6, 1]],
        ["Row4", [0, 64, 48, 12, 1]],
        ["Row5", [0, 625, 500, 150, 20, 1]],
        ["Row6", [0, 7776, 6480, 2160, 360, 30, 1]],
        ["Row7", [0, 117649, 100842, 36015, 6860, 735, 42, 1]],
        ["Row8", [0, 2097152, 1835008, 688128, 143360, 17920, 1344, 56, 1]],
        [
            "Row9",
            [0, 43046721, 38263752, 14880348, 3306744, 459270, 40824, 2268, 72, 1],
        ]]
print(tabulate(table, ["Row", "Seq"], tablefmt="github"))


def PrintPrintTriangle(triangle: list[list[int]], centered: bool):
    """Cudos to '200_success' from 'codereview'."""
    largest_element = triangle[-1][len(triangle[-1]) // 2]
    element_width = len(str(largest_element))

    def format_row(row):
        return " ".join([str(element).center(element_width) for element in row])

    triangle_width = len(format_row(triangle[-1])) if centered else 0
    for row in triangle:
        print(format_row(row).center(triangle_width))


from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Row", "Seq"]

x.add_rows(
    [
        ["Row0", [1]],
        ["Row1", [0, 1]],
        ["Row2", [0, 2, 1]],
        ["Row3", [0, 9, 6, 1]],
        ["Row4", [0, 64, 48, 12, 1]],
        ["Row5", [0, 625, 500, 150, 20, 1]],
        ["Row6", [0, 7776, 6480, 2160, 360, 30, 1]],
        ["Row7", [0, 117649, 100842, 36015, 6860, 735, 42, 1]],
        ["Row8", [0, 2097152, 1835008, 688128, 143360, 17920, 1344, 56, 1]],
        [
            "Row9",
            [0, 43046721, 38263752, 14880348, 3306744, 459270, 40824, 2268, 72, 1],
        ],
    ]
)
print(x)

x.field_names = ["Row", "Seq"]

x.add_rows(
    [
        ["Row0", "1"],
        ["Row1", "0, 1"],
        ["Row2", "0, 2, 1"],
        ["Row3", "0, 9, 6, 1"],
        ["Row4", "0, 64, 48, 12, 1"],
        ["Row5", "0, 625, 500, 150, 20, 1"],
        ["Row6", "0, 7776, 6480, 2160, 360, 30, 1"],
        ["Row7", "0, 117649, 100842, 36015, 6860, 735, 42, 1"],
        ["Row8", "0, 2097152, 1835008, 688128, 143360, 17920, 1344, 56, 1"],
        [
            "Row9",
            "0, 43046721, 38263752, 14880348, 3306744, 459270, 40824, 2268, 72, 1",
        ],
    ]
)
print(x)

from prettytable.colortable import ColorTable, Themes

y = ColorTable(theme=Themes.OCEAN)
# y = PrettyTable()
y.field_names = ["Trait", "Seq"]
y.add_rows(
    [
        [" RowSum", "1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261"],
        [" EvenSum", "1, 0, 2, 6, 38, 270, 2342, 23646, 272918, 3543630"],
        [" OddSum", "0, 1, 1, 7, 37, 271, 2341, 23647, 272917, 3543631"],
        [" AltSum", "1, -1, 1, -1, 1, -1, 1, -1, 1, -1"],
        [" AccSum", "1, 1, 4, 21, 142, 1175, 11476, 129073, 1641802, 23292459"],
        [" AccRevSum", "1, 2, 8, 44, 308, 2612, 25988, 296564, 3816548, 54667412"],
        [" DiagSum", "1, 0, 1, 1, 3, 7, 21, 67, 237, 907"],
    ]
)
print(y)

if __name__ == "__main__":
    from Abel import Abel
    from Delannoy import Delannoy
    from ChristTree import Ctree

    def interactive():
        go = "y"
        while go == "y":
            rows = int(input("Enter the number of rows:"))
            PrintPrintTriangle(Delannoy.tab(rows), False)
            PrintPrintTriangle(Abel.tab(rows), True)
            go = input("Do it again ? <y/n> ")
