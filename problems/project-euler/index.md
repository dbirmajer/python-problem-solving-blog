 ---
layout: page
title: "Project Euler Solutions"
permalink: /problems/project-euler/
---

# Project Euler Solutions

> "Project Euler exists to encourage, challenge, and develop the skills and enjoyment of anyone with an interest in the fascinating world of mathematics."

Mathematical problems that require both programming skills and mathematical insight to solve efficiently.

## 🎯 My Approach

Each solution focuses on:
- **Elegant Python code** using modern language features
- **Mathematical understanding** of the underlying concepts  
- **Performance considerations** and optimization techniques
- **Multiple solution approaches** from basic to advanced
- **Real-world applicability** of the patterns used

## 📋 Solved Problems

### Beginner Level ⭐
| Problem | Title | Key Insight |
|---------|-------|-------------|
| [001](problem-001.md) | Multiples of 3 and 5 | Multiplication trick for OR conditions |
| [006](problem-006.md) | Sum Square Difference | Direct mathematical translation |
| [016](problem-016.md) | Power Digit Sum | Working with Large Numbers |
| [020](problem-020.md) | Factorial Digit Sum | Working with Large Numbers |

### Intermediate Level ⭐⭐  
| Problem | Title | Key Insight |
|---------|-------|-------------|
| [002](problem-002.md) | Even Fibonacci Numbers | Infinite generators + takewhile |
| [025x](problem-025.md) | Fibonacci Numbers | Infinite generators + dropwhile |
| [003](problem-003.md) | Largest Prime Factor | Leveraging specialized libraries |
| [004](problem-004.md) | Largest Palindrome Product | Smart loop bounds to avoid duplicates |
| [005](problem-005.md) | Smallest Multiple | Built-in LCM with functional reduce |
| [007](problem-007.md) | 10001st Prime | Efficient prime generation |
| [010](problem-010.md) | Summation of Primes | Efficient prime generation |
| [012](problem-012.md) | Highly Divisible Triangular Numbers | Working with Generators |


## 🔥 Solution Highlights

### Most Elegant
**Problem 6**: `sum(range(101)) ** 2 - sum(x**2 for x in range(101))`

### Most Creative  
**Problem 1**: `sum(x for x in range(1_000) if (x % 5) * (x % 3) == 0)`

### Best Use of Libraries
**Problem 3**: `max(primes.factorise(600_851_475_143))`

### Most Functional
**Problem 5**: `reduce(lcm, range(1, 21))`

## 📊 Technologies & Concepts

**Python Features Used:**
- Generator expressions and functions
- Type hints and modern syntax  
- functools.reduce for accumulation
- Built-in math functions (gcd, lcm)
- String manipulation and slicing
- List comprehensions vs generators

**External Libraries:**
- **primePy**: Prime number operations
- **itertools**: Advanced iteration tools
- **typing**: Type annotations

**Mathematical Concepts:**
- Modular arithmetic
- Prime factorization  
- Fibonacci sequences
- Palindrome detection
- Least Common Multiple
- Number theory patterns

## 🎓 Learning Path

**If you're new to these concepts:**

1. **Start with Problem 1** - Basic modulo operations
2. **Try Problem 6** - Mathematical translation  
3. **Move to Problem 2** - Learn generators
4. **Tackle Problem 4** - String manipulation + optimization
5. **Challenge yourself with Problem 5** - Functional programming
6. **Explore Problems 3 & 7** - Using external libraries

**For each problem, try to:**
- Understand the mathematical concept first
- Code a basic solution  
- Optimize for performance
- Learn the Python idioms used

---

*Ready to start? Jump into [Problem 1](problem-001.md) or browse by difficulty level above!*