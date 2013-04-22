#!/usr/bin/python -tt

import sys
import re
import string


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./AlienLanguage.py file'
        sys.exit(1)

    with open(filename, 'rU') as file_handle:
        ldn = dict(zip(['L', 'D', 'N'],
                       [int(n) for n in file_handle.readline().split()]))

        words = [file_handle.readline() for i in range(ldn['D'])]

        for case in range(1, ldn['N'] + 1):
            print handle_case(case,
                              [file_handle.readline()],
                              words=words)


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
    patternstring = string.replace(string.replace(lines[0],
                                                  '(', '['),
                                   ')', ']')
    pattern = re.compile(patternstring)
    count = 0
    for word in args['words']:
        if pattern.match(word):
            count += 1

    return 'Case #%d: %d' % (case, count)


if __name__ == '__main__':
    main()
