#!/usr/bin/python -tt
# encoding: utf-8

import sys
from collections import Counter


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./TicTacToeTomek.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            print handle_case(case,
                              [file_handle.readline() for i in range(5)])


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

    # blank line in 5th line -- ignore
    grid = [list(line.strip()) for line in lines[:-1]]
    grid_lines = get_grid_lines(grid)
    result = 'Game has not completed'

    lines_status = [check_win(g_line) for g_line in grid_lines]
    result = ('X won' if 'X' in lines_status else
              'O won' if 'O' in lines_status else
              'Game has not completed' if '.' in lines_status else
              'Draw')

    return 'Case #%d: %s' % (case, result)


def check_win(line):
    """Checks given line list for win conditions and returns the winner."""
    count = Counter(line)
    for k in 'XO':
        if count[k] == len(line) or (count[k] == len(line) - 1
                                     and 'T' in count):
            return k
    if '.' in count:
        return '.'
    return None


def get_grid_lines(grid):
    """Return a list of all 'lines' in the grid."""
    lines = []
    g_height, g_width = len(grid), len(grid[0])
    for i in range(g_height):
        lines.append(get_row(grid, i))
    for i in range(g_width):
        lines.append(get_column(grid, i))
    lines.append(get_diag_NWSE(grid))
    lines.append(get_diag_SWNE(grid))
    return lines


def get_column(grid, index):
    """Return a list containing the elements of the column at index."""
    return [grid[e][index] for e in range(len(grid))]


def get_row(grid, index):
    """Return a list containing the elements of the row at index."""
    return [grid[index][e] for e in range(len(grid[0]))]


def get_diag_NWSE(grid):
    """Return a list containing the elements of the diagonal (NW to SE)."""
    return [grid[e][e] for e in range(len(grid))]


def get_diag_SWNE(grid):
    """Return a list containing the elements of the diagonal (SW to NE)."""
    return [grid[-(e + 1)][e] for e in range(len(grid))]


if __name__ == '__main__':
    main()
