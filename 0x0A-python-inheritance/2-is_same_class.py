#!/usr/bin/python3

"""
A function that returns True if
the object is
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class,
        False otherwise.
    """
    return type(obj) is a_class
