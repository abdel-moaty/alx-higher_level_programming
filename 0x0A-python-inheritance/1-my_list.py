#!/usr/bin/python3

"""A class MyList that inherits from list."""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted(): Prints the list, sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
