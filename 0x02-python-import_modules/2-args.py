#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    args = len(argv)

    print(f"{args} argument{'s' if args != 1 else ''}", end='')
    print('.' if args == 0 else ':')

    for i, arg in enumerate(argv):
        print(f"{i+1}: {arg}")
