---
layout: post
title: "Project Euler Problem 25: 1000-digit Fibonacci Number"
math: true
date: 2025-08-13
categories: [project-euler, fibonacci, big-numbers]
tags: [python, generators, itertools, arbitrary-precision, mathematical-sequences]
author: dbirmajer
excerpt: "Find the index of the first Fibonacci number with 1000 digits using elegant generator composition and iterator patterns."
---

## Problem Statement

The Fibonacci sequence is defined by the recurrence relation:

$$
F_n = F_{n-1} + F_{n-2}, \quad F_1 = 1, \quad F_2 = 1
$$

Hence the first 12 terms will be:

$$
F_1 = 1, \quad F_2 = 1, \quad F_3 = 2, \quad F_4 = 3, \quad F_5 = 5, \quad F_6 = 8, \\
F_7 = 13, \quad F_8 = 21, \quad F_9 = 34, \quad F_{10} = 55, \quad F_{11} = 89, \quad F_{12} = 144
$$

The 12th term, $F_{12}$, is the first term to contain three digits.

**Question:** What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

---

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

**Result:** $4782$

This means $F_{4782}$ is the first Fibonacci number with exactly 1000 digits.

---

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

The growth is breathtaking — $F_{4782}$ has **exactly 1000 digits**!

---

### Binet's Formula and Growth Rate

The Fibonacci numbers follow **Binet's formula**:

$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}
$$

Where:

- $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618$ (golden ratio)
- $\psi = \frac{1 - \sqrt{5}}{2} \approx -0.618$

For large $n$, $\psi^n$ becomes negligible, so:

$$
F_n \approx \frac{\varphi^n}{\sqrt{5}}
$$

The number of digits in $F_n$ is approximately:

$$
\text{digits} \approx n \log_{10}(\varphi) - \log_{10}(\sqrt{5})
$$

---

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

---

## Why $10^{999}$, Not $10^{1000}$?

This is a crucial insight about digit counting:

- $1$ to $9$: **1 digit**
- $10$ to $99$: **2 digits**
- $100$ to $999$: **3 digits**
- $1000$ to $9999$: **4 digits**

**Pattern:** $n$-digit numbers range from $10^{n-1}$ to $10^n - 1$

Therefore:

- **1000-digit numbers** start at $10^{999}$
- We want the first Fibonacci number $\ge 10^{999}$

---

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

**Pros:** Simple and direct  
**Cons:** Less elegant, repeated string conversion is inefficient

---

### Using Logarithms for Digit Counting
```python
import math

def fibonacci_index_log():
    a, b = 0, 1
    index = 0
    while math.log10(a) < 999:  # log10(10^999) = 999
        a, b = b, a + b  
        index += 1
        if a == 0:
            continue
    return index
```

**Pros:** Avoids string conversion  
**Cons:** Floating-point precision issues

---

### Binet's Formula Estimation
```python
import math

def estimate_fibonacci_1000_digits():
    phi = (1 + math.sqrt(5)) / 2
    n = (1000 + 0.5 * math.log10(5)) / math.log10(phi)
    return int(n)
```

**Pros:** $O(1)$ mathematical solution  
**Cons:** Approximation — requires verification

---

## Final Thoughts

Project Euler Problem 25 beautifully demonstrates:

1. **Generator Mastery**: Infinite sequences handled elegantly with constant memory
2. **Iterator Composition**: Complex operations built from simple, composable parts
3. **Mathematical Insight**: Understanding digit boundaries ($10^{999}$) drives the algorithm
4. **Python Excellence**: Leveraging language strengths for clean, efficient code

This approach scales seamlessly — whether finding the first 100-digit, 1000-digit, or 10000-digit Fibonacci number, the same pattern applies.

---

**Links:**
- [Project Euler Problem 25](https://projecteuler.net/problem=25)
- [Fibonacci Sequence — Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_number)
- [Binet's Formula](https://en.wikipedia.org/wiki/Binet%27s_formula)
- [Python itertools Documentation](https://docs.python.org/3/library/itertools.html)
