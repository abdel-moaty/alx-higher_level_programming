#!/usr/bin/python3

"""Defines a function that writes a string to a text file (UTF8),
and returns the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8),
    and returns the number of characters written.

    Args:
        filename (str): The path and name of the text file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
