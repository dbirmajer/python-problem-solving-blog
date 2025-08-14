---
layout: post
title: "Project Euler Problem 10: Summation of Primes"
date: 2025-08-11
categories: [project-euler, primes, optimization]
tags: [python, sympy, performance, mathematics]
author: dbirmajer
excerpt: "Find the sum of all prime numbers below 2,000,000 using an elegant Python solution with performance analysis."
---

# Project Euler Problem 10: Summation of Primes

## Problem Statement

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

## The Elegant Solution

Here's my solution using Python's sympy library:

```python
from sympy.ntheory.generate import primerange
sum(primerange(2, 2_000_000))
```

**Result: 142,913,828,922**

That's it! Two lines of code that efficiently solve a problem involving 2 million numbers.

## Why This Solution Works

### 1. **Leveraging Optimized Libraries**
The `sympy.ntheory.generate.primerange` function uses highly optimized prime generation algorithms under the hood, likely implementing variants of the Sieve of Eratosthenes.

### 2. **Memory Efficient**
Unlike generating all primes and storing them in a list, `primerange` returns a generator that yields primes on-demand, keeping memory usage minimal.

### 3. **Readable and Maintainable**
The code clearly expresses the mathematical intent: "sum all primes in range [2, 2,000,000)".

## Alternative Approaches (And Why They're Slower)

### Naive Brute Force Approach
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Don't actually run this for 2 million!
naive_sum = sum(n for n in range(2, 2_000_000) if is_prime(n))
```

**Time Complexity**: O(n√n) - extremely slow for large n

### Sieve of Eratosthenes Implementation
```python
def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit using the Sieve of Eratosthenes."""
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
    
    return [i for i in range(2, limit) if is_prime[i]]

primes = sieve_of_eratosthenes(2_000_000)
sieve_sum = sum(primes)
```

**Time Complexity**: O(n log log n) - much better, but requires O(n) memory

## Performance Comparison

Here's a timing comparison for smaller ranges to illustrate the difference:

```python
import time
from sympy.ntheory.generate import primerange

def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Test with 100,000 (smaller range for comparison)
limit = 100_000

# Sympy approach
result_sympy, time_sympy = time_function(lambda: sum(primerange(2, limit)))

# Sieve approach  
result_sieve, time_sieve = time_function(lambda: sum(sieve_of_eratosthenes(limit)))

print(f"Sympy: {result_sympy} in {time_sympy:.4f}s")
print(f"Sieve: {result_sieve} in {time_sieve:.4f}s")
```

For the full 2,000,000 range, sympy's optimized implementation significantly outperforms hand-rolled solutions.

## Key Takeaways

### 1. **Don't Reinvent the Wheel**
When dealing with well-studied mathematical problems like prime generation, leverage existing optimized libraries.

### 2. **Consider Memory vs. Time Tradeoffs**
Generator-based approaches (like `primerange`) often provide excellent memory efficiency without sacrificing speed.

### 3. **Readable Code is Maintainable Code**
The sympy solution is not just fast—it's immediately understandable to any Python developer.

### 4. **Know Your Libraries**
Python's rich ecosystem includes specialized libraries like sympy for mathematical operations. Familiarizing yourself with these tools can dramatically simplify complex problems.

## Extending the Solution

Want to explore further? Try these variations:

```python
# Sum of primes in different ranges
from sympy.ntheory.generate import primerange

ranges = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 2_000_000]
for limit in ranges:
    prime_sum = sum(primerange(2, limit))
    prime_count = len(list(primerange(2, limit)))
    print(f"Primes below {limit:,}: count={prime_count}, sum={prime_sum:,}")
```

This reveals interesting patterns about prime distribution and their cumulative sums.

## Final Thoughts

Project Euler problems often have elegant solutions when you leverage the right tools. This problem beautifully demonstrates how Python's ecosystem can turn a computationally intensive mathematical problem into a simple, readable solution.

The key insight isn't just about finding any solution—it's about finding the most **Pythonic** solution that balances performance, readability, and maintainability.

---

**Links:**
- [Project Euler Problem 10](https://projecteuler.net/problem=10)
- [SymPy Documentation](https://docs.sympy.org/latest/modules/ntheory/generate.html#sympy.ntheory.generate.primerange)
- [Sieve of Eratosthenes - Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)