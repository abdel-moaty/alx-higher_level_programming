#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[integer ** 2 for integer in row] for row in matrix]
    return result
