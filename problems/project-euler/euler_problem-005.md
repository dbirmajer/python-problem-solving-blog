---
title: "Project Euler Problem 5: Smallest Multiple"
date: 2025-08-09
categories: [project-euler, python]
tags: [lcm, number-theory, functools, reduce, python-3.9]
---

## Problem Statement

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Understanding the Problem

We need to find the **Least Common Multiple (LCM)** of all numbers from 1 to 20.

For the smaller example (1 to 10):
- We need a number divisible by: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- That number is 2520
- Verification: 2520 ÷ 8 = 315, 2520 ÷ 9 = 280, etc. (all divide evenly)

## My Solution

```python
from math import lcm
from functools import reduce

reduce(lcm, range(1, 21))
```

**Result:** `232792560`

## How This Solution Works

This elegant solution leverages two powerful Python features:

### Built-in math.lcm (Python 3.9+)
```python
from math import lcm
```

Python's `math.lcm()` function:
- Computes the Least Common Multiple of two or more integers
- Highly optimized implementation
- Handles multiple arguments: `lcm(a, b, c, d)`
- Returns 0 if any argument is 0

### functools.reduce for Cumulative Operations
```python
reduce(lcm, range(1, 21))
```

`reduce` applies `lcm` function cumulatively across the range:
- reduce(lcm, [1, 2, 3, 4, ...]) 
- Step 1: lcm(1, 2) = 2
- Step 2: lcm(2, 3) = 6
- Step 3: lcm(6, 4) = 12
- Step 4: lcm(12, 5) = 60
- ... continues until lcm(..., 20)

## Why This Solution is Excellent

1. **Leverages Standard Library**: Uses Python's optimized `math.lcm`
2. **Incredibly Concise**: Just one line of actual computation
3. **Functional Style**: Clean use of `reduce` for accumulation
4. **Readable**: Intent is immediately clear
5. **Efficient**: Built-in functions are highly optimized

## Alternative Solutions

### Solution 1: Using math.lcm with Multiple Arguments
```python
from math import lcm

def euler_05_direct():
    return lcm(*range(1, 21))  # Unpacks range into arguments
```

### Solution 2: Traditional Loop
```python
from math import lcm

def euler_05_loop():
    result = 1
    for i in range(1, 21):
        result = lcm(result, i)
    return result
```

### Solution 3: Prime Factorization (Most Efficient for Large n)
```python
def euler_05_prime_factorization(n: int) -> int:
    """Mathematical approach using prime powers."""
    from collections import defaultdict
    
    def prime_factors(num):
        factors = defaultdict(int)
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors[d] += 1
                num //= d
            d += 1
        if num > 1:
            factors[num] += 1
        return factors
    
    # Find highest power of each prime up to n
    max_powers = defaultdict(int)
    for i in range(2, n + 1):
        factors = prime_factors(i)
        for prime, power in factors.items():
            max_powers[prime] = max(max_powers[prime], power)
    
    # LCM = product of all prime powers
    result = 1
    for prime, power in max_powers.items():
        result *= prime ** power
    
    return result
```

## Performance Comparison

```python
import time

def benchmark_solutions():
    n = 20
    solutions = [
        ("My Solution", lambda: reduce(lcm, range(1, n + 1))),
        ("Direct lcm(*args)", lambda: lcm(*range(1, n + 1))),
        ("Traditional Loop", lambda: euler_05_loop()),
        ("Prime Factorization", lambda: euler_05_prime_factorization(n)),
    ]
    
    for name, func in solutions:
        start = time.time()
        result = func()
        end = time.time()
        print(f"{name}: {result} ({end-start:.6f}s)")
```

**Results:**
- **My Solution**: Very fast, clean and readable
- **Direct lcm(*args)**: Slightly faster, but less flexible  
- **Traditional Loop**: Same performance, more verbose
- **Prime Factorization**: More complex but scales better for large n

## Mathematical Insights

### Why 232,792,560 is the Answer

The LCM of 1-20 can be calculated by finding the highest power of each prime ≤ 20:

```
Primes ≤ 20: 2, 3, 5, 7, 11, 13, 17, 19

Highest powers needed:
- 2⁴ = 16 (from 16)
- 3² = 9  (from 9 and 18)  
- 5¹ = 5  (from 5, 10, 15, 20)
- 7¹ = 7  (from 7, 14)
- 11¹ = 11 (from 11)
- 13¹ = 13 (from 13)
- 17¹ = 17 (from 17)
- 19¹ = 19 (from 19)

LCM = 2⁴ × 3² × 5 × 7 × 11 × 13 × 17 × 19 = 232,792,560
```

### Pattern Recognition
Notice that for LCM(1, 2, ..., n), we need:
- Highest power of 2 that's ≤ n
- Highest power of 3 that's ≤ n  
- All primes ≤ n (to the first power)

## Python Version Considerations

**Python 3.9+** (Your approach):
```python
from math import lcm
reduce(lcm, range(1, 21))
```

**Python 3.8 and earlier**:
```python
import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

reduce(lcm, range(1, 21))
```

Your solution showcases how Python keeps improving - the built-in `math.lcm` makes this type of problem much more elegant!

## Key Takeaways

1. **Use the standard library** - `math.lcm` is optimized and well-tested
2. **functools.reduce is powerful** for cumulative operations
3. **Mathematical problems often have built-in solutions** in modern Python
4. **Concise doesn't mean unclear** - your one-liner is perfectly readable
5. **LCM problems appear frequently** in number theory and programming contests

## Complete Working Code

```python
from math import lcm
from functools import reduce

def solve_euler_5():
    """Find smallest positive number evenly divisible by all numbers 1-20."""
    return reduce(lcm, range(1, 21))

def solve_euler_5_flexible(n: int) -> int:
    """Find LCM of numbers 1 to n."""
    return reduce(lcm, range(1, n + 1))

def verify_solution(result: int, n: int) -> bool:
    """Verify result is divisible by all numbers 1 to n."""
    return all(result % i == 0 for i in range(1, n + 1))

if __name__ == "__main__":
    # Solve the main problem
    result = solve_euler_5()
    print(f"LCM of numbers 1-20: {result:,}")
    
    # Verify it works
    print(f"Verification: {verify_solution(result, 20)}")
    
    # Show progression for smaller ranges
    for i in [5, 10, 15, 20]:
        lcm_result = solve_euler_5_flexible(i)
        print(f"LCM(1 to {i:2d}): {lcm_result:,}")
    
    # Show individual divisibility for a few numbers
    test_nums = [17, 18, 19, 20]
    for num in test_nums:
        print(f"{result:,} ÷ {num} = {result // num:,} (remainder: {result % num})")
```

## Test Your Understanding

1. **What's the LCM of numbers 1 to 30?** (Warning: it's quite large!)
2. **Find the LCM of only the even numbers: 2, 4, 6, 8, ..., 20**
3. **Can you solve this without using any imports?** (Implement your own LCM and reduce)

```python
# Hint for #2:
def lcm_even_numbers():
    return reduce(lcm, range(2, 21, 2))

# Hint for #3: 
def gcd_custom(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_custom(a, b):
    return a * b // gcd_custom(a, b)
```

## Evolution of the Solution

This shows a great progression in Python programming:
1. **First attempt**: Custom LCM function with error handling
2. **Final solution**: Leverage built-in optimized functions
3. **Result**: More concise, faster, and more maintainable

Sometimes the best solution is recognizing when not to reinvent the wheel!

---

*This is part of my Python Problem Solving series. Check out more solutions on my [GitHub](your-github-link)!*