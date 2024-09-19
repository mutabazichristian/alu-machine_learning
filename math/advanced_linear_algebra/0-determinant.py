#!/usr/bin/env python3
"""Function that calculcates the determinant of a matrix"""
import numpy as np


def determinant(matrix):
    """
    Args:
    a matrix

    Returns:
    determinant of the matrix
    """

    return np.linalg.det(matrix)
