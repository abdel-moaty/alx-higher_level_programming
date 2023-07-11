#!/usr/bin/python3

"""Defines a function that appends a string at the end of a text file (UTF8),
and returns the number of characters added."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8),
    and returns the number of characters added.

    Args:
        filename (str): The path and name of the text file to append to.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
