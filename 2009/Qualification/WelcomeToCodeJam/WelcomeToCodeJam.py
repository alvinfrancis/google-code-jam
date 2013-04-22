#!/usr/bin/python -tt
# encoding: utf-8

import sys
import re


class memoize:
    """Decorator class for memoization of a recursive function"""
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./AlienLanguage.py file'
        sys.exit(1)

    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
            print handle_case(case, [file_handle.readline()])


def handle_case(case, lines, addvar=None):
    """Return a string containing the expected output given a single case.

    Handles the case supplied through the given case and lines and returns a
    string containing the expected output of the given input. The addvar may be
    used to contain any additional input variables that may have been
    preprocessed.

    Args:
        case: Number specifying the current case number
        lines: List of input lines relevant to the case
        addvar: Dict containing additional variables (e.g. preprocessed input)

    Returns:
        A string of the expected output of the corresponding test case.
    """
    return 'Case #%d: %s' % (case,
                             count_subsequence(lines[0][:-1], 0,
                                               'welcome to code jam'))


@memoize
def count_subsequence(text, pos, strtofind):
    """Return the last four digits of the count of strtofind

    Use recursion to implement a top down dynamic programming solution with
    memoization to find the count. Use a class decorator for memoization. Note,
    memoization can be tweaked by noticing that a pos, strtofind combination
    can be cascaded back until the character split in the recursion.

    Args:
        text: String of text to check against
        pos: Int index of where the strtofind can be matched against
        strtofind: String to check for

    Returns:
        A string containing the last four digits of the count of strtofind
        found in text starting from pos.
    """

    # Deal with base case: strtofind is a single letter
    count = 0
    if len(strtofind) == 1:
        count = len(re.findall(strtofind, text[pos:]))
    else:
        for c in re.finditer(strtofind[0], text[pos:]):
            newpos = c.start() + pos + 1
            count += int(count_subsequence(text, newpos, strtofind[1:]))

    return '%s' % ('%04d' % count)[-4:]


if __name__ == '__main__':
    main()
