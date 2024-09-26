#!/usr/bin/env python3
"""
Function that calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Args:
    A list representing the polynomial's coefficient

    Returns:

    """
    if (not isinstance(poly, list)) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)
    return derivative
