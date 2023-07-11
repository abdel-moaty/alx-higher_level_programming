#!/usr/bin/python3

"""
A function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        otherwise, False.
    """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
