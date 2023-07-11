#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    A class representing a rebellious integer.
    """
    def __eq__(self, other):
        """
        Override the equality (==) operator.

        Args:
            other: The value to compare against.

        Returns:
            bool: True if the values are not equal; False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality (!=) operator.

        Args:
            other: The value to compare against.

        Returns:
            bool: True if the values are equal; False otherwise.
        """
        return super().__eq__(other)
