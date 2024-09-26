#!/usr/bin/env python3
"""
Function to Calculate the give intranet summation
"""
def summation_i_squared(n):
    if not isinstance(n,(int,float)):
        return None  
    return factorial(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * n * factorial(n-1)
