#!/usr/bin/python -tt

import sys


def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./StoreCredit.py file'
        sys.exit(1)

    with open(filename, 'rU') as file_handle:
        cases = int(file_handle.readline())
        for case in range(1, cases + 1):
            print handle_case(case, [file_handle.readline() for x in range(3)])


def handle_case(case, lines):
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
    credit = int(lines[0])
    price_list = [int(e) for e in lines[2].split()]
    result = ''
    for i, price in enumerate(price_list, 1):
        if credit - price in price_list:
            result = ' '.join(map(str, [i, price_list.index(credit - price)]))
            break

    return 'Case #%d: %s' % (case, result)


if __name__ == '__main__':
    main()
