#!/usr/bin/python -tt
# encoding: utf-8

import sys


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./Lawnmower.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            N, M = map(int, file_handle.readline().split())
            print handle_case(case,
                              [file_handle.readline() for i in range(N)],
                              N=N, M=M)


def handle_case(case, lines, **args):
    """Return a string containing the expected output given a single case.

    Handles the case supplied through the given case and lines and returns a
    string containing the expected output of the given input. The **args may be
    used to contain any additional input variables that may have been
    preprocessed.

    Args:
        case: Number specifying the current case number
        lines: List of input lines relevant to the case
        **args: Additional arguments (e.g. preprocessed input)

    Returns:
        A string of the expected output of the corresponding test case.
    """

    grid = [list(line.split()) for line in lines]

    result = 'YES'
    if any((h, w)
           for h in range(len(grid))
           for w in range(len(grid[0]))
           if not check_cell(grid, h, w)):
        result = 'NO'

    return 'Case #%d: %s' % (case, result)


def check_cell(grid, h, w):
    """Checks if cell is valid.

    A cell is only valid if it is the maximum value for either its row or
    column.
    """
    val = int(grid[h][w])
    val_check1 = max([int(e) for e in get_column(grid, w)])
    val_check2 = max([int(e) for e in get_row(grid, h)])
    return val == val_check1 or val == val_check2


def get_column(grid, index):
    """Return a list containing the elements of the column at index."""
    return [grid[e][index] for e in range(len(grid))]


def get_row(grid, index):
    """Return a list containing the elements of the row at index."""
    return [grid[index][e] for e in range(len(grid[0]))]


if __name__ == '__main__':
    main()
