#!/usr/bin/env python3
"""Module for calculating the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """
    Calculate the definiteness of a given matrix.

    Args:
        matrix (numpy.ndarray): The input matrix.

    Returns:
        str: The definiteness of the matrix, or None if it doesn't fit any category.

    Raises:
        TypeError: If matrix is not a numpy.ndarray.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        return None

    try:
        eigvals = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None

    positive = np.all(eigvals > 0)
    negative = np.all(eigvals < 0)
    zero = np.any(np.isclose(eigvals, 0))

    if positive:
        return "Positive definite"
    elif positive or (zero and np.any(eigvals > 0)):
        return "Positive semi-definite"
    elif negative:
        return "Negative definite"
    elif negative or (zero and np.any(eigvals < 0)):
        return "Negative semi-definite"
    elif np.any(eigvals > 0) and np.any(eigvals < 0):
        return "Indefinite"
    else:
        return None


if __name__ == "__main__":
    # You can add test cases here if needed
    pass
