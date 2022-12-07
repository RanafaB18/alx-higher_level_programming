#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0:
        for array in matrix:
            new_array = []
            for num in array:
                new_array.append(num * num)
            new_matrix.append(new_array)
        return new_matrix
