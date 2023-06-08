#!/usr/bin/python3

import sys

if __name__ == "__main__":
    result = sum(map(int, sys.argv[1:]))
    print(result)
