#!/usr/bin/python3
def fizzbuzz():
    for numer in range(1, 101):
        result = ""
        if numer % 3 == 0:
            result += "Fizz"
        if numer % 5 == 0:
            result += "Buzz"
        print(result or numer, end=" ")
