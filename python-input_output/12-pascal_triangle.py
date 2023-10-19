#!/usr/bin/python3
"""
create a function that returns a list
of lists of integers representing the Pascal's
triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers"""

    if n <= 0:
        return []

    result = [[1]]

    for i in range(1, n):
        prev_row = result[-1]
        new_row = [1]

        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)
        new_row.append(1)

        result.append(new_row)
    return result
