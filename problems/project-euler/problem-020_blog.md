---
layout: post
title: "Project Euler Problem 20: Factorial Digit Sum"
date: 2025-08-13
categories: [project-euler, factorial, big-numbers]
tags: [python, combinatorics, arbitrary-precision, digit-manipulation, mathematics]
author: dbirmajer
excerpt: "Calculate the sum of digits in 100! using efficient digit extraction and exploring the explosive growth of factorials."
---

# Project Euler Problem 20: Factorial Digit Sum

## Problem Statement

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3,628,800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

## The Elegant Solution

Here's my solution leveraging Python's built-in mathematical functions and our proven digit extraction algorithm:

```python
#!/usr/bin/env python3
"""
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
```

**Result: 648**

## The Mind-Boggling Scale of 100!

Before diving into the solution, let's appreciate the astronomical size of 100!:

### Factorial Growth Visualization
```python
from math import factorial

for n in [5, 10, 15, 20, 25, 50, 100]:
    fact_n = factorial(n)
    digits = len(str(fact_n))
    print(f"{n:3}! has {digits:3} digits")
```

Output:
```
  5! has   3 digits  (120)
 10! has   7 digits  (3,628,800)
 15! has  13 digits  
 20! has  19 digits  
 25! has  26 digits  
 50! has  65 digits  
100! has 158 digits  
```

**100! is a 158-digit number!** It starts with:
```
93326215443944152681699238856266700490715968264381...
```

### Stirling's Approximation

We can estimate the number of digits in n! using **Stirling's approximation**:

```
n! ≈ √(2πn) × (n/e)^n
```

The number of digits is approximately:
```
digits ≈ log₁₀(n!) ≈ n×log₁₀(n) - n×log₁₀(e) + 0.5×log₁₀(2πn)
```

For n = 100:
```python
import math

n = 100
stirling_digits = n * math.log10(n) - n * math.log10(math.e) + 0.5 * math.log10(2 * math.pi * n)
print(f"Stirling approximation: {stirling_digits:.1f} digits")
print(f"Actual digits: {len(str(factorial(100)))} digits")
```

Remarkably close!

## Code Reuse: The Power of Modular Design

Notice how this solution elegantly reuses the `sum_of_digits` function from Problem 16. This demonstrates a key programming principle: **write reusable, well-tested functions**.

### The Same Algorithm, Different Context
- **Problem 16**: Sum digits of 2^1000 (302 digits)
- **Problem 20**: Sum digits of 100! (158 digits)

The digit extraction algorithm works identically for both, showcasing its generality.

## Mathematical Deep Dive: Factorial Properties

### What Makes Factorials Special?

Factorials appear throughout mathematics:

1. **Combinatorics**: C(n,k) = n! / (k!(n-k)!)
2. **Probability**: Permutations and arrangements
3. **Calculus**: Taylor series expansions
4. **Number Theory**: Wilson's theorem and more

### Trailing Zeros in Factorials

An interesting side question: How many trailing zeros does 100! have?

```python
def count_trailing_zeros(n):
    """Count trailing zeros in n! using Legendre's formula"""
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count

print(f"100! has {count_trailing_zeros(100)} trailing zeros")
```

**Answer: 24 trailing zeros**

This comes from counting factors of 10 = 2×5 in the prime factorization, where factors of 5 are the limiting constraint.

### Prime Factorization of Factorials

The prime factorization of n! follows **Legendre's formula**:

For a prime p, the exponent of p in n! is:
```
e_p(n!) = ⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + ...
```

```python
def prime_power_in_factorial(n, p):
    """Calculate the power of prime p in n!"""
    power = 0
    pk = p
    while pk <= n:
        power += n // pk
        pk *= p
    return power

# Examples for 100!
print(f"Power of 2 in 100!: {prime_power_in_factorial(100, 2)}")   # 97
print(f"Power of 5 in 100!: {prime_power_in_factorial(100, 5)}")   # 24
print(f"Power of 7 in 100!: {prime_power_in_factorial(100, 7)}")   # 16
```

## Alternative Implementations

### Iterative Factorial with Digit Sum Tracking
```python
def factorial_digit_sum_iterative(n):
    """Calculate factorial and digit sum simultaneously"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return sum_of_digits(result)
```

### String-Based Approach
```python
def factorial_digit_sum_string(n):
    """Using string conversion (less efficient but more readable)"""
    return sum(int(digit) for digit in str(factorial(n)))
```

### Custom Factorial Implementation
```python
def my_factorial(n):
    """Custom factorial implementation"""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(sum_of_digits(my_factorial(100)))
```

## Performance Analysis

### Why `math.factorial()` is Optimal

Python's `math.factorial()` is implemented in C with optimizations:
- Efficient multiplication algorithms
- Memory management optimizations
- Hardware-optimized arithmetic

```python
import time

def benchmark_factorial_methods(n):
    # Built-in factorial
    start = time.time()
    result1 = factorial(n)
    time1 = time.time() - start
    
    # Custom implementation
    start = time.time()
    result2 = my_factorial(n)
    time2 = time.time() - start
    
    print(f"math.factorial({n}): {time1:.6f}s")
    print(f"custom factorial({n}): {time2:.6f}s")
    print(f"Speedup: {time2/time1:.1f}x")

benchmark_factorial_methods(100)
```

The built-in version is typically much faster.

## Digit Sum Patterns in Factorials

### Exploring the Pattern
```python
factorial_digit_sums = []
for n in range(1, 21):
    fact_n = factorial(n)
    digit_sum = sum_of_digits(fact_n)
    factorial_digit_sums.append(digit_sum)
    print(f"{n:2}! digit sum: {digit_sum:3}")
```

### Digital Root of Factorials
The digital root is the single digit obtained by iteratively summing digits:

```python
def digital_root(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n

# Digital roots of n! for n = 1 to 20
for n in range(1, 21):
    fact_n = factorial(n)
    dr = digital_root(fact_n)
    print(f"Digital root of {n}!: {dr}")
```

**Interesting observation**: For n ≥ 5, the digital root of n! follows a predictable pattern due to factors of 9.

## The Connection to Problem 16

Both problems showcase the same algorithmic pattern:
1. **Generate a large number** (2^1000 or 100!)
2. **Extract digits efficiently** using the division algorithm
3. **Sum the digits** with minimal memory usage

This demonstrates how seemingly different mathematical objects (powers vs. factorials) can share computational approaches.

## Computational Complexity

### Time Complexity
- `factorial(100)`: O(n log n) for multiplication of large numbers
- `sum_of_digits()`: O(log₁₀(100!)) ≈ O(158) = O(1) for this specific problem

### Space Complexity
- Storing 100!: O(log₁₀(100!)) ≈ O(158) digits
- Digit extraction: O(1) additional space

The bottleneck is computing the factorial, not summing its digits.

## Extensions and Variations

### Generalized Factorial Digit Sum
```python
def factorial_digit_sum_range(start, end):
    """Calculate factorial digit sums for a range of values"""
    results = {}
    for n in range(start, end + 1):
        results[n] = sum_of_digits(factorial(n))
    return results

# Find all n where sum of digits in n! exceeds some threshold
high_digit_sums = {n: ds for n, ds in factorial_digit_sum_range(1, 100).items() if ds > 500}
print(high_digit_sums)
```

### Double Factorial
```python
def double_factorial(n):
    """n!! = n × (n-2) × (n-4) × ..."""
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

print(f"100!! digit sum: {sum_of_digits(double_factorial(100))}")
```

### Subfactorial (Derangements)
```python
def subfactorial(n):
    """!n = number of derangements of n objects"""
    if n == 0:
        return 1
    return (n - 1) * (subfactorial(n - 1) + subfactorial(n - 2))

# Note: This recursive version is inefficient; use dynamic programming for larger n
```

## Real-World Applications

### Cryptography
Large factorials appear in:
- RSA key generation
- Primality testing algorithms
- Combinatorial cryptographic schemes

### Combinatorics Problems
- Permutation counting
- Probability calculations
- Graph theory (counting spanning trees)

### Statistical Physics
- Stirling's approximation in entropy calculations
- Partition functions in thermodynamics

## Key Programming Lessons

### 1. **Leverage Standard Libraries**
`math.factorial()` is optimized and tested - use it rather than rolling your own.

### 2. **Write Reusable Functions**
The `sum_of_digits()` function works for any large integer, making it valuable across multiple problems.

### 3. **Understand Your Data**
Knowing that 100! has 158 digits helps us understand the scale and choose appropriate algorithms.

### 4. **Mathematical Insight Drives Efficiency**
Understanding factorial properties (like trailing zeros) can lead to optimization opportunities.

## Final Thoughts

Project Euler Problem 20 beautifully demonstrates:

1. **Computational Scale**: Working with 158-digit numbers seamlessly in Python
2. **Code Reuse**: Leveraging proven algorithms across different mathematical contexts  
3. **Mathematical Beauty**: Connecting factorials to digit manipulation, prime factorization, and combinatorics
4. **Algorithmic Efficiency**: O(log n) digit processing regardless of the source of the large number

The elegance lies not just in the brevity of the code, but in how it combines Python's powerful built-in functions with a mathematically sound digit extraction algorithm. This solution exemplifies the principle that the best code often comes from understanding both the mathematical structure of the problem and the computational tools available in your language.

Whether you're computing 2^1000 or 100!, the fundamental challenge remains the same: efficiently processing the digits of astronomically large numbers. Mastering this pattern opens doors to solving entire classes of mathematical computation problems.

---

**Links:**
- [Project Euler Problem 20](https://projecteuler.net/problem=20)
- [Factorial - Wikipedia](https://en.wikipedia.org/wiki/Factorial)
- [Stirling's Approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation)
- [Legendre's Formula](https://en.wikipedia.org/wiki/Legendre%27s_formula)