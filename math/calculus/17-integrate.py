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
    if not isinstance(C, (int, float)):
        return None

    integral = [C]

    for i in range(len(poly)):
        integral.append(poly[i] / (i + 1))

    integral = [
        int(coef) if isinstance(coef, float) and coef.is_integer() else coef
        for coef in integral
    ]
    while len(integral) > 1 and integral[0] == 0:
        integral.pop(0)

    return integral
