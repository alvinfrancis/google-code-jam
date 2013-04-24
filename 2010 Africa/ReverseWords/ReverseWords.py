#!/usr/bin/python -tt

import sys


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./ReverseWords.py file'
        sys.exit(1)

    with open(filename, 'rU') as file_handle:
        file_handle.readline()
        for case, line in enumerate(file_handle, 1):
            print handle_case(case, [line])


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
    result = ' '.join(reversed(lines[0].split()))
    return 'Case #%d: %s' % (case, result)


if __name__ == '__main__':
    main()
