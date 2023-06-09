#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:4]
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator in operators:
        result = operators[operator](int(a), int(b))
        print(f"{a} {operator} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
