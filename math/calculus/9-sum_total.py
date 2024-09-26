#!/usr/bin/env python3
"""
Function to Calculate the give intranet summation
"""
def summation_i_squared(n):
    if not isinstance(n,(int,float)):
        return None  
    return factorial(n)

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * a * factorial(a-1)
