---
layout: post
title: "Project Euler Problem 16: Power Digit Sum"
date: 2025-08-12
categories: [project-euler, big-numbers, algorithms]
tags: [python, arbitrary-precision, digit-manipulation, mathematics]
author: dbirmajer
excerpt: "Calculate the sum of digits in 2^1000 using efficient digit extraction and Python's arbitrary precision arithmetic."
---

# Project Euler Problem 16: Power Digit Sum

## Problem Statement

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

## The Elegant Solution

Here's my solution using efficient digit manipulation:

```python
#!/usr/bin/env python3
"""
Project Euler Problem 16
"""

def sum_of_digits(n: int) -> int:
    accum = 0
    while n >= 10:
        q, r = divmod(n, 10)
        accum += r
        n = q
    return accum + n

print(sum_of_digits(2**1_000))
```

**Result: 1,366**

## Understanding the Scale

Before diving into the algorithm, let's appreciate the magnitude of 2^1000:

- 2^10 = 1,024 (about 10^3)
- 2^100 ≈ 1.27 × 10^30
- **2^1000 ≈ 1.07 × 10^301**

This is a number with **302 digits**! In decimal form, it starts with:
```
107150860718626732094842504906000181056140...
```

No standard programming language's integer type can handle this - except Python's arbitrary precision integers.

## Python's Big Integer Magic

One of Python's greatest strengths is its built-in support for arbitrary precision arithmetic:

```python
# This just works in Python!
huge_number = 2**1000
print(len(str(huge_number)))  # 302 digits
```

In languages like C++ or Java, you'd need special libraries for big integer arithmetic. Python handles this seamlessly.

## The Mathematics Behind Digit Extraction

### The Core Algorithm

My `sum_of_digits` function uses the mathematical relationship between a number and its digits:

For any positive integer n:
```
n = d₀ + d₁×10 + d₂×10² + d₃×10³ + ...
```

Where d₀, d₁, d₂, ... are the digits from right to left.

### The `divmod` Operation

The key insight is using `divmod(n, 10)`:
- **Quotient (q)**: n // 10 (removes the rightmost digit)
- **Remainder (r)**: n % 10 (gives us the rightmost digit)

### Algorithm Walkthrough

Let's trace through with a smaller example: `sum_of_digits(12345)`

| Iteration | n     | divmod(n, 10) | q    | r | accum |
|-----------|-------|---------------|------|---|-------|
| 1         | 12345 | (1234, 5)     | 1234 | 5 | 5     |
| 2         | 1234  | (123, 4)      | 123  | 4 | 9     |
| 3         | 123   | (12, 3)       | 12   | 3 | 12    |
| 4         | 12    | (1, 2)        | 1    | 2 | 14    |
| Final     | 1     | -             | -    | - | 15    |

Result: 1 + 2 + 3 + 4 + 5 = 15 ✓

## Why This Algorithm is Efficient

### Time Complexity: O(log₁₀(n))
The algorithm runs in time proportional to the number of digits in n, which is log₁₀(n).

For 2^1000 with 302 digits, this means just 302 iterations - extremely fast!

### Space Complexity: O(1)
We only store a few variables regardless of the input size.

### Mathematical Efficiency
Using `divmod` is more efficient than string conversion because:
- No string allocation
- Direct arithmetic operations
- Single pass through digits

## Alternative Approaches

### String Conversion Method
```python
def sum_of_digits_string(n: int) -> int:
    return sum(int(digit) for digit in str(n))
```

**Pros**: Extremely concise and readable
**Cons**: 
- Requires string conversion (memory overhead)
- Character-to-integer conversion for each digit
- Less educational about the underlying mathematics

### Recursive Approach
```python
def sum_of_digits_recursive(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) + sum_of_digits_recursive(n // 10)
```

**Pros**: Elegant and mathematical
**Cons**: 
- Stack overflow risk for very large numbers
- Function call overhead
- Less efficient than iterative version

### Performance Comparison

Let's compare the methods:

```python
import time

def benchmark_method(func, n, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        result = func(n)
    end = time.time()
    return result, (end - start) / iterations

# Test with 2^1000
big_num = 2**1000

# My iterative method
result1, time1 = benchmark_method(sum_of_digits, big_num)

# String method
result2, time2 = benchmark_method(sum_of_digits_string, big_num)

print(f"Iterative: {result1} in {time1:.8f}s")
print(f"String:    {result2} in {time2:.8f}s")
```

The iterative method typically outperforms string conversion, especially for very large numbers.

## Deep Dive: Why `divmod` is Special

### What `divmod` Does
```python
q, r = divmod(a, b)
# Equivalent to:
# q = a // b  (floor division)
# r = a % b   (remainder)
```

### Why It's Efficient
Many processors have a single instruction that computes both quotient and remainder simultaneously. Python's `divmod` leverages this hardware optimization.

### Mathematical Properties
For any integers a and b (b ≠ 0):
```
a = b × q + r, where 0 ≤ r < |b|
```

This is the **Division Algorithm** from number theory, fundamental to our digit extraction.

## The Beauty of the Loop Structure

```python
while n >= 10:
    q, r = divmod(n, 10)
    accum += r
    n = q
return accum + n
```

### Why `n >= 10`?
- When n < 10, it's a single digit
- No need to extract - just add it directly
- This avoids an extra iteration and `divmod` call

### The Final `+ n`
After the loop, n contains the leftmost digit, which we add to complete the sum.

## Applications Beyond Project Euler

This digit manipulation technique appears in many contexts:

### Digital Root Calculation
```python
def digital_root(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n
```

### Digit Reversal
```python
def reverse_digits(n):
    result = 0
    while n > 0:
        q, r = divmod(n, 10)
        result = result * 10 + r
        n = q
    return result
```

### Palindrome Checking
```python
def is_palindrome(n):
    return n == reverse_digits(n)
```

## Powers of 2: Mathematical Properties

### Why 2^1000?
Powers of 2 have fascinating digit properties:
- 2^10 = 1,024 (digit sum: 7)
- 2^100 has digit sum 115
- 2^1000 has digit sum 1,366

### Pattern Analysis
```python
# Investigate digit sum patterns
for i in range(1, 21):
    power = 2**i
    digit_sum = sum_of_digits(power)
    print(f"2^{i:2} = {power:8} → digit sum = {digit_sum}")
```

This reveals interesting patterns in how digit sums grow with powers.

## Extending the Solution

### Generalized Power Digit Sum
```python
def power_digit_sum(base, exponent):
    return sum_of_digits(base**exponent)

# Examples:
print(power_digit_sum(2, 1000))    # Problem 16
print(power_digit_sum(3, 500))     # What about 3^500?
print(power_digit_sum(10, 100))    # 10^100 = 1 + 99 zeros → sum = 1
```

### Factorial Digit Sum (Problem 20 Preview)
```python
import math
print(sum_of_digits(math.factorial(100)))  # Project Euler Problem 20
```

## Key Programming Insights

### 1. **Choose the Right Data Structures**
Integers for mathematical operations, not strings for computation.

### 2. **Leverage Language Strengths**
Python's arbitrary precision integers make this problem trivial in terms of number handling.

### 3. **Understand the Mathematics**
The division algorithm provides the foundation for efficient digit manipulation.

### 4. **Optimize for the Problem Scale**
302 digits requires an algorithm that scales with digit count, not number magnitude.

## Educational Value

This problem teaches several important concepts:

1. **Arbitrary Precision Arithmetic**: How computers handle very large numbers
2. **Digit Manipulation**: Fundamental techniques for working with number representations
3. **Algorithm Efficiency**: Comparing mathematical vs. string-based approaches
4. **Number Theory**: The division algorithm in practical application

## Final Thoughts

Project Euler Problem 16 elegantly combines:
- **Computational Scale**: Working with 302-digit numbers
- **Mathematical Insight**: Using number theory for efficient digit extraction
- **Algorithmic Efficiency**: O(log n) solution with O(1) space
- **Language Features**: Leveraging Python's big integer support

The solution demonstrates that sometimes the most elegant code comes from understanding the mathematical structure of the problem. Rather than treating the number as a string of characters, we work with it as a mathematical object, using the division algorithm to systematically extract its digits.

This approach is not just faster - it's more mathematically meaningful and generalizes to many other digit-manipulation problems.

---

**Links:**
- [Project Euler Problem 16](https://projecteuler.net/problem=16)
- [Python's Arbitrary Precision Integers](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Division Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Division_algorithm)
- [Powers of Two - Wikipedia](https://en.wikipedia.org/wiki/Power_of_two)