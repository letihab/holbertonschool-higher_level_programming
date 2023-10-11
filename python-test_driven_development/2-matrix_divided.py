#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
matrix must be a list of lists of integers or floats, otherwise 
raise a TypeError exception with the message matrix must be a 
matrix (list of lists) of integers/floats

Each row of the matrix must be of the same size, otherwise raise a TypeError exception
 with the message Each row of the matrix must have the same size
"""



def matrix_divided(matrix, div):
    """divide a matrix by a number div"""
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"
    new_matrix = []
    new_list = []
    row_size = len(matrix[0])
    if not matrix:
        raise TypeError(list_error)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    if not all(len(row) == row_size for row in matrix):
            raise TypeError(len_error)
    for row in matrix:
            new_row = [round(num / div, 2) for num in row]
            new_matrix.append(new_row)
    return new_matrix

    