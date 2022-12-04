#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        matrixLength = len(matrix)
        for i in range(0, matrixLength):
            length = len(matrix[i])
            for j in range(0, length):
                if j == length - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
            print()
