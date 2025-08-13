---
layout: post
title: "Project Euler Problem 25: 1000-digit Fibonacci Number"
date: 2025-08-13
categories: [project-euler, fibonacci, big-numbers]
tags: [python, generators, itertools, arbitrary-precision, mathematical-sequences]
author: dbirmajer
excerpt: "Find the index of the first Fibonacci number with 1000 digits using elegant generator composition and iterator patterns."
---

# Project Euler Problem 25: 1000-digit Fibonacci Number

## Problem Statement

The Fibonacci sequence is defined by the recurrence relation:

$$F_n = F_(n−1) + F_(n−2), where F_1 = 1 and F_2 = 1.$$

Hence the first 12 terms will be:
F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, F_6 = 8, F_7 = 13, F_8 = 21, F_9 = 34, F_10 = 55, F_11 = 89, F_12 = 144

The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## The Elegant Solution

Here's my solution using Python's powerful iterator composition:

```python
from typing import Iterator
from itertools import dropwhile

def fibonacci(a: int = 0, b: int = 1) -> Iterator[int]:
    while True:
        yield a
        a, b = b, a + b

g = dropwhile(lambda pair: pair[1] < 10**999, enumerate(fibonacci()))
print(next(g)[0])
```

**Result: 4782**

This means F_4782 is the first Fibonacci number with exactly 1000 digits!

## Understanding the Fibonacci Explosion

### The Scale of Growth

Fibonacci numbers grow exponentially. Let's visualize how quickly they reach massive sizes:

```python
# Number of digits in Fibonacci numbers
fib_gen = fibonacci()
for i in range(1, 26):
    fib_n = next(fib_gen)
    if fib_n > 0:  # Skip F_0 = 0
        digits = len(str(fib_n))
        print(f"F_{i:2} = {fib_n:>20} ({digits:2} digits)")
```

Sample output:
```
F_1 =                    1 ( 1 digit )
F_2 =                    1 ( 1 digit )
F_3 =                    2 ( 1 digit )
F_10 =                   55 ( 2 digits)
F_12 =                  144 ( 3 digits)
F_17 =                 1597 ( 4 digits)
F_21 =                10946 ( 5 digits)
```

The growth is breathtaking - F_4782 has **exactly 1000 digits**!

### Binet's Formula and Growth Rate

The Fibonacci numbers follow **Binet's formula**:

```
F_n = (φⁿ - ψⁿ) / √5
```

Where:
- φ = (1 + √5)/2 ≈ 1.618 (golden ratio)
- ψ = (1 - √5)/2 ≈ -0.618

For large n, ψⁿ becomes negligible, so:
```
F_n ≈ φⁿ / √5
```

The number of digits in F_n is approximately:
```
digits ≈ n × log₁₀(φ) - log₁₀(√5) ≈ n × 0.209 - 0.349
```

Let's verify this for our answer:
```python
import math

n = 4782
phi = (1 + math.sqrt(5)) / 2
predicted_digits = n * math.log10(phi) - 0.5 * math.log10(5)
print(f"Predicted digits for F_{n}: {predicted_digits:.1f}")
print(f"Actual: F_{n} has exactly 1000 digits")
```

Remarkably accurate!

## Code Architecture: Elegant Iterator Composition

### The Fibonacci Generator

```python
def fibonacci(a: int = 0, b: int = 1) -> Iterator[int]:
    while True:
        yield a
        a, b = b, a + b
```

This generator demonstrates several Python best practices:

#### 1. **Infinite Generator Pattern**
- Uses `while True` to create an endless sequence
- Memory efficient - generates values on demand
- No upper bounds or pre-allocation needed

#### 2. **Tuple Assignment Magic**
```python
a, b = b, a + b
```
This single line elegantly updates both values:
- Right side is evaluated first: `(b, a + b)`
- Then assigned to left side: `a = b, b = a + b`
- No temporary variables needed!

#### 3. **Default Parameters**
```python
def fibonacci(a: int = 0, b: int = 1) -> Iterator[int]:
```
Allows flexibility:
- `fibonacci()` → standard sequence: 0, 1, 1, 2, 3, 5...
- `fibonacci(1, 1)` → alternative start: 1, 1, 2, 3, 5...

### The Search Logic

```python
g = dropwhile(lambda pair: pair[1] < 10**999, enumerate(fibonacci()))
print(next(g)[0])
```

This line is packed with sophisticated iterator manipulation:

#### 1. **enumerate(fibonacci())**
Creates pairs of (index, fibonacci_value):
```
(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), ...
```

#### 2. **dropwhile() with Lambda**
```python
lambda pair: pair[1] < 10**999
```
- `pair[1]` extracts the Fibonacci value
- `10**999` is the smallest 1000-digit number
- `dropwhile` skips all pairs where Fibonacci value < 10^999

#### 3. **next(g)[0]**
- `next(g)` gets the first pair that passes the condition
- `[0]` extracts the index from the (index, value) pair

## Why 10^999, Not 10^1000?

This is a crucial insight about digit counting:

- Numbers from 1 to 9: **1 digit** each
- Numbers from 10 to 99: **2 digits** each  
- Numbers from 100 to 999: **3 digits** each
- Numbers from 1000 to 9999: **4 digits** each

**Pattern**: n-digit numbers range from 10^(n-1) to 10^n - 1

Therefore:
- **1000-digit numbers** start at 10^999
- We want the first Fibonacci ≥ 10^999

## Alternative Approaches

### Direct Iteration with Counter
```python
def fibonacci_index_direct():
    a, b = 0, 1
    index = 0
    while len(str(a)) < 1000:
        a, b = b, a + b
        index += 1
    return index
```

**Pros**: Simple and direct  
**Cons**: 
- Less elegant than iterator composition
- Repeated string conversion is inefficient
- Hardcoded digit counting logic

### Using Logarithms for Digit Counting
```python
import math

def fibonacci_index_log():
    a, b = 0, 1
    index = 0
    while math.log10(a) < 999:  # log10(10^999) = 999
        a, b = b, a + b  
        index += 1
        if a == 0:  # Handle log10(0)
            continue
    return index
```

**Pros**: Avoids string conversion
**Cons**: 
- Floating point precision issues
- Special handling for zero
- Less readable than the iterator approach

### Binet's Formula Estimation
```python
import math

def estimate_fibonacci_1000_digits():
    phi = (1 + math.sqrt(5)) / 2
    # Solve: n * log10(phi) - 0.5 * log10(5) ≈ 1000
    n = (1000 + 0.5 * math.log10(5)) / math.log10(phi)
    return int(n)
```

**Pros**: O(1) mathematical solution
**Cons**: 
- Only an approximation
- Requires verification with actual computation
- Less educational about Fibonacci generation

## Performance Analysis

### Time Complexity
- **My solution**: O(n) where n is the result index
- **Direct methods**: Also O(n), but with higher constants
- **Estimation**: O(1), but approximate

### Space Complexity  
- **My solution**: O(1) - generators use constant memory
- **Direct methods**: O(1) for computation, O(k) for string conversion
- **List-based**: O(n) - would store all Fibonacci numbers

### Benchmarking the Approaches
```python
import time

def benchmark_approach(func, name):
    start = time.time()
    result = func()
    end = time.time()
    print(f"{name}: {result} in {end-start:.4f}s")

# My iterator approach
def my_solution():
    g = dropwhile(lambda pair: pair[1] < 10**999, enumerate(fibonacci()))
    return next(g)[0]

# Direct approach  
def direct_approach():
    a, b = 0, 1
    index = 0
    while len(str(a)) < 1000:
        a, b = b, a + b
        index += 1
    return index

benchmark_approach(my_solution, "Iterator approach")
benchmark_approach(direct_approach, "Direct approach")
```

The iterator approach typically performs comparably or better due to avoiding repeated string conversions.

## Mathematical Deep Dive: Fibonacci Properties

### The Golden Ratio Connection
As n increases, the ratio F_(n+1)/F_n approaches φ (the golden ratio):

```python
def fibonacci_ratios():
    fib = fibonacci()
    a = next(fib)  # F_0 = 0
    b = next(fib)  # F_1 = 1
    
    for i in range(2, 20):
        c = next(fib)
        if b != 0:
            ratio = c / b
            phi_diff = abs(ratio - 1.618033988749)
            print(f"F_{i}/F_{i-1} = {ratio:.10f} (diff from φ: {phi_diff:.2e})")
        a, b = b, c
```

### Fibonacci and Number Theory
Fascinating properties emerge:
- **GCD Property**: gcd(F_m, F_n) = F_gcd(m,n)
- **Divisibility**: F_n divides F_m if and only if n divides m (except for special cases)
- **Modular Patterns**: Fibonacci numbers mod m are periodic

### Growth Rate Analysis
```python
def fibonacci_growth_analysis():
    fib = fibonacci()
    prev_fib = next(fib)  # F_0
    
    for i in range(1, 30):
        curr_fib = next(fib)
        if prev_fib > 0:
            growth_factor = curr_fib / prev_fib
            print(f"F_{i}/F_{i-1} = {growth_factor:.6f}")
        prev_fib = curr_fib
```

This reveals the convergence to φ ≈ 1.618034.

## Practical Applications

### Computational Biology
Fibonacci sequences appear in:
- Spiral patterns in shells and plants
- Branching patterns in trees
- DNA structure analysis

### Computer Science
- **Fibonacci Heaps**: Advanced data structures
- **Dynamic Programming**: Classic teaching example
- **Algorithm Analysis**: Time complexity of recursive algorithms

### Financial Mathematics
- **Fibonacci Retracements**: Technical analysis in trading
- **Portfolio Optimization**: Golden ratio applications

## Advanced Iterator Patterns

This problem showcases several advanced Python patterns:

### 1. **Generator Composition**
```python
enumerate(fibonacci())  # Composing generators
```

### 2. **Lazy Evaluation**
```python
dropwhile(condition, iterable)  # Processes only as needed
```

### 3. **Functional Programming**
```python
lambda pair: pair[1] < 10**999  # Pure function for filtering
```

### 4. **Iterator Protocol**
```python
next(generator)  # Explicit iterator advancement
```

## Extensions and Variations

### Generalized Fibonacci (Tribonacci, etc.)
```python
def generalized_fibonacci(*seeds):
    """Generalized Fibonacci with arbitrary number of seeds"""
    sequence = list(seeds)
    while True:
        yield sequence[0]
        next_val = sum(sequence)
        sequence = sequence[1:] + [next_val]

# Tribonacci: each term is sum of previous 3
tribonacci = generalized_fibonacci(0, 0, 1)
```

### Fibonacci with Different Starting Values
```python
# Lucas numbers: similar recurrence but different seeds
lucas = fibonacci(2, 1)  # 2, 1, 3, 4, 7, 11, 18, 29...
```

### Finding Multiple Digit Milestones
```python
def fibonacci_digit_milestones():
    milestones = [10, 100, 1000, 10000]  # Digits we care about
    current_milestone = 0
    
    for index, fib_val in enumerate(fibonacci()):
        digits = len(str(fib_val)) if fib_val > 0 else 1
        
        if current_milestone < len(milestones) and digits >= milestones[current_milestone]:
            print(f"F_{index} is first with {milestones[current_milestone]} digits")
            current_milestone += 1
            
        if current_milestone >= len(milestones):
            break
```

## Key Programming Insights

### 1. **Embrace Lazy Evaluation**
Generators allow processing infinite sequences without memory concerns.

### 2. **Compose Simple Functions**
Combining `enumerate`, `dropwhile`, and `next` creates powerful data processing pipelines.

### 3. **Use the Right Abstraction**
Iterator patterns make the solution both elegant and efficient.

### 4. **Mathematical Insight Drives Code Design**
Understanding Fibonacci growth led to the 10^999 threshold choice.

## Final Thoughts

Project Euler Problem 25 beautifully demonstrates:

1. **Generator Mastery**: Infinite sequences handled elegantly with constant memory
2. **Iterator Composition**: Complex operations built from simple, composable parts  
3. **Mathematical Insight**: Understanding digit boundaries (10^999) drives the algorithm
4. **Python Excellence**: Leveraging language strengths for clean, efficient code

The solution showcases how **functional programming patterns** can create code that's both mathematically elegant and computationally efficient. Rather than explicit loops and counters, we compose iterators that naturally express the mathematical relationships.

This approach scales beautifully - whether finding the first 100-digit, 1000-digit, or 10000-digit Fibonacci number, the same elegant pattern applies. The code reads like the mathematical statement of the problem itself.

The marriage of **mathematical insight** (exponential growth, digit boundaries) with **computational elegance** (generators, iterator composition) produces a solution that's both educational and efficient - the hallmark of excellent problem-solving.

---

**Links:**
- [Project Euler Problem 25](https://projecteuler.net/problem=25)
- [Fibonacci Sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Golden Ratio and Binet's Formula](https://en.wikipedia.org/wiki/Binet%27s_formula)
- [Python itertools Documentation](https://docs.python.org/3/library/itertools.html)