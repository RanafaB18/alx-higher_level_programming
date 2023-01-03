#!/usr/bin/python3
"""
    Divides a matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a number

    Args:
        matrix (list of lists): list of lists of numbers
        div (int or float): number to divide matrix

    Raises:
        TypeError: if the matrix has unequal row sizes,
                    is empty, rows has other data types
        ZeroDivisionError: if div is 0

    Returns:
        matrix (list): has the resulting
                        numbers from the division of the matrix
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) > 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(type(i) == int or isinstance(i, float)
       for row in matrix for i in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_number = round(element / div, 2)
            new_row.append(new_number)
        new_matrix.append(new_row)
    return new_matrix
