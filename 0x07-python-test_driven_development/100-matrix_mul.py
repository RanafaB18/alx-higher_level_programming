#!/usr/bin/python3
"""matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Raises:
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_
        ValueError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        int : multiplication of 2 mmatrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(rows, list) for rows in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(rows, list) for rows in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if not m_b or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    if not all(type(i) == int or isinstance(i, float)
       for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(i) == int or isinstance(i, float)
       for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")
    m_a_length = len(m_a[0])
    m_b_length = len(m_b[0])
    if not all(len(rows) == m_a_length for rows in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(rows) == m_b_length for rows in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    # Multiply the matrices and return the result
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
