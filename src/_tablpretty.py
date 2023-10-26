
# #@


def PrintPrintTriangle(triangle, centered):
    """Cudos to '200_success' from 'codereview'."""
    largest_element = triangle[-1][len(triangle[-1]) // 2]
    element_width = len(str(largest_element))
    def format_row(row):
        return ' '.join([str(element).center(element_width) for element in row])
    triangle_width = len(format_row(triangle[-1])) if centered else 0
    for row in triangle:
        print(format_row(row).center(triangle_width))


if __name__ == '__main__': 

    from Abel import Abel
    from Delannoy import Delannoy
    from FussCatalan import FussCatalan
    from ChristTree import Ctree

    go = 'y'
    while go == 'y':
        rows = int(input('Enter the number of rows:'))
        PrintPrintTriangle(Delannoy.tab(rows), False)
        PrintPrintTriangle(Abel.tab(rows), True)
        go = input('Do it again ? <y/n> ')
