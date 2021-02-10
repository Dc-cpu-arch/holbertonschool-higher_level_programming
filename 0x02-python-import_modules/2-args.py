#!/usr/bin/python3
import sys
if __name__ == '__main__':

    length = len(sys.argv) - 1
    if length == 0:
        print('{} arguments.'.format(length))
    else:

        if length == 1:
            print('{} argument:'.format(length))
        else:
            print('{} arguments:'.format(length))

        for i in range(0, length):
            print('{:d}: {}'.format(i, sys.argv[i]))
