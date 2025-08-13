#!/usr/bin/env python3
"""
Returns:
    Project Euler Problem 20
"""

from math import factorial


def sum_of_digits(n: int) -> int:
    accum = 0
    while n >= 10:
        q, r = divmod(n, 10)
        accum += r
        n = q
    return accum + n


print(sum_of_digits(factorial(100)))
