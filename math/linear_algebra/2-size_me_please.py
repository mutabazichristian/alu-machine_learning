#!/usr/bin/env python3
def matrix_shape(matrix):
    """Function that return the shape of matrix, all dimensions"""
    shape = []
    while isinstance(matrix, list):
        shape.append((len(matrix)))
        matrix = matrix[0]

    return shape
