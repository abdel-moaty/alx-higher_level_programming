#!/usr/bin/python3

"""
Defines a function that adds a new attribute to an object if it’s possible.
"""


def add_attribute(obj, atr_name, atr_value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: Object to add the attribute to.
        atr_name: Attribute name.
        atr_value: Attribute value.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, atr_name, atr_value)
