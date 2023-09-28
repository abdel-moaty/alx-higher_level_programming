#!/usr/bin/python3
"""
Defines a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search.

    Args:
        list_of_integers (List[int]): The list of unsorted integers.

    Returns:
        int: The index of a peak element from the list, or None if empty.
    """
    if not list_of_integers:
        return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
