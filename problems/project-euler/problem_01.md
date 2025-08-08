# Project Euler Problem 1: Multiples of 3 and 5

## Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Understanding the Problem

We need to:
1. Find all numbers below 1000 that are divisible by 3 OR 5
2. Sum all those numbers

Let's think about some examples:
- 3, 6, 9, 12, 15, 18... (multiples of 3)
- 5, 10, 15, 20, 25, 30... (multiples of 5)
- Note that 15 appears in both lists, but we should only count it once

## My Solution

```python
sum(x for x in range(1_000) if (x % 5) * (x % 3) == 0)
```

**Result:** `233168`

## How This Solution Works

The key insight is in the condition `(x % 5) * (x % 3) == 0`. This works because:

- If `x` is divisible by 3, then `x % 3 == 0`
- If `x` is divisible by 5, then `x % 5 == 0`
- The product of two numbers equals 0 if and only if at least one of them is 0
- So `(x % 5) * (x % 3) == 0` is true when x is divisible by 3 OR 5 (or both)

Let's trace through a few examples:
- x = 6: `(6 % 5) * (6 % 3) = 1 * 0 = 0` ✓ (divisible by 3)
- x = 10: `(10 % 5) * (10 % 3) = 0 * 1 = 0` ✓ (divisible by 5)  
- x = 15: `(15 % 5) * (15 % 3) = 0 * 0 = 0` ✓ (divisible by both)
- x = 7: `(7 % 5) * (7 % 3) = 2 * 1 = 2` ✗ (not divisible by either)

## Alternative Solutions

### Solution 1: Traditional Approach
```python
total = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        total += x
print(total)
```

### Solution 2: Generator Expression with OR
```python
sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
```

### Solution 3: Mathematical Approach (Most Efficient)
```python
def sum_divisible_by(n, limit):
    """Sum of multiples of n below limit"""
    p = (limit - 1) // n
    return n * (p * (p + 1)) // 2

# Sum of multiples of 3 + Sum of multiples of 5 - Sum of multiples of 15
result = sum_divisible_by(3, 1000) + sum_divisible_by(5, 1000) - sum_divisible_by(15, 1000)
```

## Performance Comparison

- **My solution**: O(n) time, very readable and concise
- **Traditional approach**: O(n) time, most readable for beginners
- **Generator expression with OR**: O(n) time, standard Pythonic approach
- **Mathematical approach**: O(1) time, most efficient for large numbers

## List Comprehension vs Generator Expression

This is a perfect opportunity to clarify an important Python concept!

### Generator Expression (what we're using):
```python
# Generator expression - uses parentheses
sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
```

### List Comprehension (different syntax):
```python
# List comprehension - uses square brackets
numbers = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
result = sum(numbers)
```

### Key Differences:

| Generator Expression | List Comprehension |
|---------------------|-------------------|
| Uses `()` parentheses | Uses `[]` square brackets |
| **Lazy evaluation** - generates values on-demand | **Eager evaluation** - creates entire list in memory |
| Memory efficient | Uses more memory |
| Can only iterate once | Can iterate multiple times |
| Returns a generator object | Returns a list object |

### Why Generator Expressions are Better Here:

```python
# Generator - memory efficient (only stores current value)
sum(x for x in range(1_000_000) if x % 3 == 0 or x % 5 == 0)

# List comprehension - creates huge list in memory first!
sum([x for x in range(1_000_000) if x % 3 == 0 or x % 5 == 0])
```

For our Project Euler problem, the generator expression is perfect because:
- We only need to iterate once (for the sum)
- We don't need to store all values in memory
- It's more efficient for large ranges



1. **Concise**: One-liner that's still readable
2. **Creative**: Uses multiplication instead of logical OR
3. **Efficient**: O(n) with minimal overhead
4. **Pythonic**: Uses generator expression with sum()

## Key Takeaways

- Sometimes mathematical properties can lead to elegant solutions
- The modulo operator is powerful for divisibility checks
- Generator expressions are memory-efficient for large ranges
- Multiple approaches exist - choose based on readability vs performance needs

## Test Your Understanding

Try modifying this solution for:
1. Multiples of 3 or 7 below 100
2. Multiples of 4, 6, or 8 below 500
3. Can you extend the multiplication trick to three conditions?

---

*This is part of my Python Problem Solving series. Check out more solutions on my [GitHub](your-github-link)!*