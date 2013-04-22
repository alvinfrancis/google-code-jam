#!/usr/bin/python -tt
# encoding: utf-8

import sys
import string
from collections import deque


class Labeler:
    """Class for proper labeling of drainage basins."""

    labels = []

    def __init__(self):
        self.labels = deque([c for c in string.lowercase])

    def get_label(self):
        """Pop and return the appropriate character from labels."""
        return self.labels.popleft()


class memoize:
    """Decorator class for memoization of a recursive function."""
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


class Basins:
    """Class to hold the matrix of basins."""

    basins = [[]]

    def __init__(self, basins):
        self.basins = basins

    def print_basins(self):
        """Print the basins matrix."""
        for y in self.basins:
            for x in y:
                print '%s' % (x),
            print

    def get_level(self, x, y):
        """Return the level of the given basin x, y coordinates."""
        return self.basins[y][x]


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./Watersheds.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            hw = dict(zip(['H', 'W'],
                          [int(n) for n in file_handle.readline().split()]))
            print handle_case(case,
                              [file_handle.readline() for x in range(hw['H'])],
                              h=hw['H'], w=hw['W'])


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
    labeler = Labeler()

    basins = Basins([[int(w) for w in h.split()] for h in lines])

    # Break into new line
    s = '\n'
    # Use get label on each coordinate and join the results to create a matrix
    s += '\n'.join([' '.join([get_label(basins, x, y, labeler)
                              for x in range(args['w'])])
                    for y in range(args['h'])])
    return 'Case #%d: %s' % (case, s)


@memoize
def get_label(basins, x, y, labeler):
    """Return the char label of the given basin using the given labeler class.

    Use recursion to implement the solution. The label is the label of the
    neighboring drain/sink. Use a class decorator for memoization. The label of
    a basin is the label of its corresponding sink.  The Labeler will be used
    for applying the proper label to unlabeled sinks.  The use of a class for
    basins is necessary for memoization hashing (list cannot be hashed).

    Args:
        basins: Basins class containing basin matrix
        x: Number x coordinate of the basin to get label
        y: Number y coordinate of the basin to get label
        labeler: Labeler class to use for labeling of the basin if necessary

    Returns:
        A string character of the label of the given basin coordinates.
    """

    nd = get_neighbor_drain(basins, x, y)
    if nd:
        return get_label(basins, nd[0], nd[1], labeler)
    else:
        return labeler.get_label()


def get_neighbor_drain(basins, x, y):
    """Return a tuple of the neighboring drain coordinates in the form (x, y).

    Args:
        basins: Lists of lists of tuples (2d matrix of tuples) with tuple of
            the form: (height, label)
        x: Number x coordinate of the basin to get label
        y: Number y coordinate of the basin to get label

    Returns:
        A tuple of the x, y coordinates of the neighboring drain. Returns None
        if the given basin is a sink.
    """
    n = []
    xubound = len(basins.basins[0])
    yubound = len(basins.basins)

    # North
    n.append((x,
              get_offset(y, -1, yubound)))
    if None in n[-1]:
        n.pop(-1)
    # West
    n.append((get_offset(x, -1, xubound),
              y))
    if None in n[-1]:
        n.pop(-1)
    # East
    n.append((get_offset(x, 1, xubound),
              y))
    if None in n[-1]:
        n.pop(-1)
    # South
    n.append((x,
              get_offset(y, 1, yubound)))
    if None in n[-1]:
        n.pop(-1)

    if n:
        drain = min(enumerate(n),
                    key=lambda x:
                    (basins.get_level(x[1][0], x[1][1]), x[0]))[1]
        if basins.get_level(drain[0], drain[1]) < basins.get_level(x, y):
            return drain
    return


def get_offset(coord, offset, ubound):
    """Return the coordinate described by coord modified by the offset.

    @TODO: Check if there is a more pythonic way.

    Args:
        coord: Int coordinate
        offset: Int offset. Can be zero.

    Returns:
        The offsetted coordinate. None if the offset exceeds bounds.
    """
    offset_coord = coord + offset
    if offset_coord >= 0 and offset_coord < ubound:
        return offset_coord
    else:
        return


if __name__ == '__main__':
    main()
