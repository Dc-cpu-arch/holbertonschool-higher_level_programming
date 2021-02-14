#!/usr/bin/python3

""" Module: contains a function that divides a matrix """


def matrix_divided(matrix, div):
    """ Divides each element of a matrix

    matrix is a list with numbers
    div is an integer to divide each element of the list

    Raises TypeError if matrix or elements are invalid
    Raises TypeError if div is not int or float
    Raises ZeroDivisionError if div is 0

    Returns the list (matrix) with its elements divided
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    j = 0
    for row in matrix:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

        if j == 0:
            j = len(row)
        elif j != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
