#!/usr/bin/python3


"""
Modulo that divide a matrix by the div given by the user
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    Function that divide matrix by div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif matrix == []:
        raise ValueError("matrix must be a matrix (list of lists) "
                         "of integers/floats")
    new_matrix = []
    for row in matrix:
        if row == matrix[0]:
            len_1 = len(row)
        len_2 = len(row)
        if len_1 != len_2:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for j in range(len(row)):
            if isinstance(row[j], (int, float)):
                new_row.append(round(row[j] / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        new_matrix.append(new_row)
    return new_matrix
