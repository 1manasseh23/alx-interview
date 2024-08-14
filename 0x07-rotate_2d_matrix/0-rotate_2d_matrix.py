#!/usr/bin/python3
"""This an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Transpose the matrix"""

    # This loop iterates over each row of the matrix
    # The variable i represents the current row index
    for i in range(len(matrix)):
        # This loop starts from the next column of the current
        # row and goes up to the last column
        for j in range(i, len(matrix)):
            """
            This line performs the actual swap between the elements at
            positions (i, j) and (j, i). It uses tuple unpacking to
            simultaneously assign new values to both variables
            """
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
