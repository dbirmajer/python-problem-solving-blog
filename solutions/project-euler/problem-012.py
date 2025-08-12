#!/usr/bin/env python3
"""
Returns:
    Project Euler Problem 12
"""

from math import prod
from itertools import (count, accumulate)
from more_itertools import first_true
from collections import Counter
from primePy import primes

def num_factors(n: int) -> int:
    return  prod([a+1 for a in Counter(primes.factors(n)).values()])


triangular = accumulate(count(1))
print(first_true(triangular, pred=lambda t: num_factors(t) > 500))

