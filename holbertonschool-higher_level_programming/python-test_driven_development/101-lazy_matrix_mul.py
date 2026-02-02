#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices using NumPy, ensuring
    compatibility with Holberton expected error messages.
    """

    # Check if inputs are lists (scalar check)
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check that each element of m_a and m_b is a list
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check that all elements are int or float
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # Multiply using NumPy; catch ValueError to match Holberton expected output
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        a_shape = np.array(m_a).shape
        b_shape = np.array(m_b).shape
        raise ValueError(
            f"shapes {a_shape} and {b_shape} not aligned: "
            f"{a_shape[1]} (dim 1) != {b_shape[0]} (dim 0)"
        )
