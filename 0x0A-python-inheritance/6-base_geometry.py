#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: This method should be implemented in the subclass.

        """
        raise Exception("area() is not implemented")
