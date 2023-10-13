#!/usr/bin/python3
"""
    python script, given an n x n 2D matrix,
    rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
        function to rotate a 2D matrix in-place
        Args:
            matrix - given matrix
        Return:
            Rotated matrix
    """
    matrix.reverse()
    copy_matrix = matrix.copy()

    for i in range(len(matrix)):
        matrix[i] = [row[i] for row in copy_matrix]
