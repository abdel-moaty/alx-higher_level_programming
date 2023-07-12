#!/usr/bin/python3

"""Defines a function that returns a list of lists of integers,
representing the Pascal’s triangle of n."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
        Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
