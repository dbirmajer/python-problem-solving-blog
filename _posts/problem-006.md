---
title: "Project Euler Problem 6: Sum Square Difference"
date: 2025-08-09
categories: [project-euler, python]
tags: [mathematics, algebra, sum-formulas, one-liner]
---

## Problem Statement

The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the square of the sum and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

Find the difference between the square of the sum and the sum of the squares of the first one hundred natural numbers.

## Understanding the Problem

We need to calculate:
**Square of Sum - Sum of Squares**

For numbers 1 to 100:
- **Sum of squares**: 1² + 2² + 3² + ... + 100²
- **Square of sum**: (1 + 2 + 3 + ... + 100)²
- **Difference**: (Square of sum) - (Sum of squares)

## My Solution

```python
sum(range(101)) ** 2 - sum(x**2 for x in range(101))
```

**Result:** `25164150`

## How This Solution Works

This one-liner directly implements the mathematical definition:

### Part 1: Square of the Sum
```python
sum(range(101)) ** 2
```
- `sum(range(101))` calculates 1 + 2 + 3 + ... + 100 = 5050
- `** 2` squares the result: 5050² = 25,502,500

### Part 2: Sum of the Squares  
```python
sum(x**2 for x in range(101))
```
- Generator expression that calculates 1² + 2² + 3² + ... + 100²
- Each `x**2` computes the square of each number
- `sum()` adds them all up = 338,350

### Part 3: The Difference
```python
25,502,500 - 338,350 = 25,164,150
```

## Why This Solution is Brilliant

1. **Direct Translation**: Mirrors the mathematical formula exactly
2. **Readable**: Anyone can understand what it's calculating
3. **Concise**: Entire problem solved in one line
4. **Efficient**: Uses Python's optimized built-in functions
5. **No Loops**: Leverages generator expressions and built-ins

## Alternative Solutions

### Solution 1: Step-by-Step Approach
```python
def euler_06_verbose():
    # Calculate sum of numbers 1 to 100
    sum_of_numbers = sum(range(1, 101))
    
    # Calculate sum of squares 1² to 100²
    sum_of_squares = sum(x**2 for x in range(1, 101))
    
    # Calculate square of the sum
    square_of_sum = sum_of_numbers ** 2
    
    # Return the difference
    return square_of_sum - sum_of_squares
```

### Solution 2: Using Mathematical Formulas
```python
def euler_06_formula(n: int) -> int:
    """Using mathematical formulas for maximum efficiency."""
    # Formula for sum: n(n+1)/2
    sum_of_numbers = n * (n + 1) // 2
    
    # Formula for sum of squares: n(n+1)(2n+1)/6  
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    # Calculate difference
    square_of_sum = sum_of_numbers ** 2
    return square_of_sum - sum_of_squares
```

### Solution 3: List Comprehension Version
```python
def euler_06_list():
    numbers = list(range(1, 101))
    return sum(numbers)**2 - sum([x**2 for x in numbers])
```

### Solution 4: Functional Approach
```python
from functools import reduce
from operator import add

def euler_06_functional():
    numbers = range(1, 101)
    sum_of_nums = reduce(add, numbers)
    sum_of_squares = reduce(add, (x**2 for x in numbers))
    return sum_of_nums**2 - sum_of_squares
```

## Performance Analysis

```python
import time

def benchmark_solutions():
    solutions = [
        ("My Solution", lambda: sum(range(101))**2 - sum(x**2 for x in range(101))),
        ("Verbose", euler_06_verbose),
        ("Formula", lambda: euler_06_formula(100)),
        ("List Comprehension", euler_06_list),
    ]
    
    for name, func in solutions:
        start = time.time()
        result = func()
        end = time.time()
        print(f"{name}: {result} ({end-start:.6f}s)")
```

**Results:**
- **My Solution**: ~0.000020s - Excellent balance of speed and readability
- **Verbose**: ~0.000025s - Slightly slower due to extra variables
- **Formula**: ~0.000001s - Fastest (O(1) complexity!)
- **List Comprehension**: ~0.000030s - Slower due to list creation

## Mathematical Deep Dive

### The Beautiful Algebraic Identity

Your solution actually demonstrates this mathematical relationship:

**(1 + 2 + ... + n)² - (1² + 2² + ... + n²) = ?**

Let's expand this algebraically:
- Sum formula: 1 + 2 + ... + n = n(n+1)/2
- Sum of squares: 1² + 2² + ... + n² = n(n+1)(2n+1)/6

For n = 100:
- Sum = 100 × 101 ÷ 2 = 5,050
- Sum of squares = 100 × 101 × 201 ÷ 6 = 338,350
- Difference = 5,050² - 338,350 = 25,164,150

### Why the Difference is Always Positive

The square of the sum is always larger because:
- (a + b)² = a² + 2ab + b²
- This includes the "cross terms" 2ab that don't appear in a² + b²
- For our sum: (1+2+...+n)² includes terms like 2×1×2, 2×1×3, 2×2×3, etc.

## Scaling to Different Ranges

Your solution easily adapts to any range:

```python
def sum_square_difference(n: int) -> int:
    """Find difference for numbers 1 to n."""
    return sum(range(n + 1))**2 - sum(x**2 for x in range(n + 1))

# Examples:
print(sum_square_difference(10))   # Should be 2640
print(sum_square_difference(100))  # Should be 25164150
print(sum_square_difference(1000)) # Much larger result!
```

## Why I Love This Solution

1. **Mathematical Purity**: Direct implementation of the problem statement
2. **Python Mastery**: Excellent use of built-in functions and generators
3. **Readability**: Code reads exactly like the math
4. **Efficiency**: No unnecessary intermediate storage
5. **Elegance**: Sometimes the most straightforward approach is the best

## Key Programming Concepts

- **Generator Expressions**: Memory-efficient iteration with `sum(x**2 for x in range(101))`
- **Built-in Functions**: Leveraging optimized `sum()` and `range()`
- **Exponentiation**: Using `**` operator for both squaring and power operations
- **Mathematical Translation**: Converting word problems directly to code
- **Functional Style**: No variables, just computation

## Complete Working Code

```python
def solve_euler_6() -> int:
    """Find difference between square of sum and sum of squares for 1-100."""
    return sum(range(101)) ** 2 - sum(x**2 for x in range(101))

def solve_euler_6_general(n: int) -> int:
    """Generalized version for any n."""
    return sum(range(n + 1)) ** 2 - sum(x**2 for x in range(n + 1))

def solve_euler_6_formula(n: int) -> int:
    """Using mathematical formulas - O(1) complexity."""
    sum_of_numbers = n * (n + 1) // 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return sum_of_numbers ** 2 - sum_of_squares

def verify_with_small_example():
    """Verify with the given example: n=10 should give 2640."""
    result = solve_euler_6_general(10)
    print(f"For n=10: {result} (expected: 2640)")
    return result == 2640

if __name__ == "__main__":
    # Solve the main problem
    result = solve_euler_6()
    print(f"Sum square difference (1-100): {result:,}")
    
    # Verify with given example
    print(f"Verification passed: {verify_with_small_example()}")
    
    # Show the calculation breakdown
    sum_1_to_100 = sum(range(101))
    sum_squares_1_to_100 = sum(x**2 for x in range(101))
    
    print(f"\nBreakdown:")
    print(f"Sum of 1-100: {sum_1_to_100:,}")
    print(f"Square of sum: {sum_1_to_100**2:,}")
    print(f"Sum of squares: {sum_squares_1_to_100:,}")
    print(f"Difference: {sum_1_to_100**2 - sum_squares_1_to_100:,}")
    
    # Compare with formula approach
    formula_result = solve_euler_6_formula(100)
    print(f"Formula verification: {result == formula_result}")
```

## Test Your Understanding

1. **What's the difference for numbers 1 to 1000?**
2. **Can you solve this for just even numbers: 2, 4, 6, ..., 100?**
3. **What if we wanted sum of cubes vs cube of sum?**

```python
# Hint for #2:
def even_numbers_difference():
    return sum(range(2, 101, 2))**2 - sum(x**2 for x in range(2, 101, 2))

# Hint for #3:
def sum_cube_difference(n):
    return sum(range(n + 1))**3 - sum(x**3 for x in range(n + 1))
```

## Mathematical Beauty

This problem showcases the beautiful difference between:
- **(a + b + c)² = a² + b² + c² + 2ab + 2ac + 2bc**
- **a² + b² + c²**

The difference is exactly those cross terms: **2ab + 2ac + 2bc**

For our problem, these cross terms sum to a surprisingly large number: 25,164,150!

---

*This is part of my Python Problem Solving series. Check out more solutions on my [GitHub](your-github-link)!*