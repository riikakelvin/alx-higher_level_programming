#!/usr/bin/python3

'''Defines a matrix division function.'''


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Arguments:
        matrix (list): A list containing lists of ints or floats.
        div (int/float): divisor.
    Prompt/ Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains different sizes of rows.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.
    Returns:
        A new matrix representing the results of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

