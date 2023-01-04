#!/usr/bin/python3.5
"""

Multiplies 2 matrices with numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication
    """
    return (np.matmul(m_a, m_b))
