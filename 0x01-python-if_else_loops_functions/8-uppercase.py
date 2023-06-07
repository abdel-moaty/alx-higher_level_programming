#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if 97 <= ord(char) <= 122:
            uppercased = chr(ord(char) - 32)
        else:
            uppercased = char
        print("{}".format(uppercased), end="")
    print("")
