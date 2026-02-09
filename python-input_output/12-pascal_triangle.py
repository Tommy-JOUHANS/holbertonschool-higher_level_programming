#!/user/bin/env python3
"""Module that contains the function pascal_triangle
that returns a list of lists of integers representing
 the Pascal’s triangle of n.

"""


from math import factorial


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
     the Pascal’s triangle of n.

    Args:
        n: number of rows of the triangle

    Returns:
        A list of lists of integers representing the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)

    return triangle
