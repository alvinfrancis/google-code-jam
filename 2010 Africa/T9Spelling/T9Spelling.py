#!/usr/bin/python -tt

import sys
import string


def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./T9Spelling.py file'
        sys.exit(1)

    with open(filename, 'rU') as file_handle:
        file_handle.readline()
        T9dict = getT9dict()
        for i, line in enumerate(file_handle, 1):
            print 'Case #%d: %s' % (i, messagetokeystring(line.strip('\n'),
                                                          T9dict))


def messagetokeystring(message, keydict):
    """
    Return a string representing the key sequence used to get the specified
    message using the given dictionary
    """
    return ''.join([' ' + str(keydict[char])
                    if i - 1 >= 0
                    and str(keydict[char])[0]
                    == str(keydict[message[i - 1]])[0]
                    else str(keydict[char])
                    for i, char in enumerate(message)])


def getT9dict():
    """
    Return a dict mapping each alphabet letter to the corresponding T9 number
    sequence
    """
    T9dict = {}
    all_letters = string.lowercase
    T9dict.update(mapkeystoletter(2, all_letters[0:3]))
    T9dict.update(mapkeystoletter(3, all_letters[3:6]))
    T9dict.update(mapkeystoletter(4, all_letters[6:9]))
    T9dict.update(mapkeystoletter(5, all_letters[9:12]))
    T9dict.update(mapkeystoletter(6, all_letters[12:15]))
    T9dict.update(mapkeystoletter(7, all_letters[15:19]))
    T9dict.update(mapkeystoletter(8, all_letters[19:22]))
    T9dict.update(mapkeystoletter(9, all_letters[22:26]))
    T9dict[' '] = 0

    return T9dict


def mapkeystoletter(key, letters):
    """
    Return a dict mapping each key appropriately to each letter such that each
    letter is mapped to a string containing the key n number of times, where n
    is the position of the letter in the given letters string
    """
    return dict((v, ''.join([str(key) for i in range(k)]))
                for k, v in enumerate(letters, 1))


if __name__ == '__main__':
    main()
