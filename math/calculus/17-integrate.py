#!/usr/bin/env python3
"""
Function that calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Arguments:
    A list with the polynomial's coefficients, reverse order
    The constant, if any

    Returns:
    A list of the integral's polynomial, reverse order
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    integral = [C]
    for i in range(1, len(poly)):
        integral.append(poly[i] / i)
    return integral
