#!/usr/bin/python3

"""Defines a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The path and name of the text file to be read.

    Returns:
        None

    Example:
        read_file("example.txt")
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
