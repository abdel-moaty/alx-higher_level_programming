#!/usr/bin/python3

"""
Defines a function that returns the dictionary description,
with simple data structure(list, dictionary, string, integer and boolean),
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary containing the serialized attributes.
    """
    return obj.__dict__
