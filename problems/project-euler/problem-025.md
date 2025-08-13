# Project Euler Problem 25 — 1000-Digit Fibonacci Number

**Problem statement:**  
The Fibonacci sequence is defined by:

\[
F_1 = 1, \quad F_2 = 1, \quad F_n = F_{n-1} + F_{n-2}
\]

Find the index of the first term in the Fibonacci sequence to contain **1000 digits**.

---

## Brute‑Force Python Generator Solution

We can solve this efficiently using Python's **generators** and **itertools**:

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

### How it works:
1. **`fibonacci()` generator**: Yields Fibonacci numbers indefinitely, using constant memory.
2. **`enumerate()`**: Pairs each Fibonacci number with its index.
3. **`dropwhile(...)`**: Skips all terms until the first number with at least 1000 digits.
4. **`next(g)[0]`**: Retrieves the index of the first such term.

Running the code gives the result:

```
4782
```

(Using 0-based indexing here; in standard 1-based indexing, the term is also the 4782nd.)

---

## Mathematical Shortcut — Binet’s Formula

We can avoid generating all Fibonacci numbers by using an **approximation** based on **Binet’s formula**:

\[
F_n = \frac{\varphi^n}{\sqrt{5}} \quad \text{for large } n, \quad \varphi = \frac{1 + \sqrt{5}}{2}
\]

Taking base‑10 logarithms:

\[
\log_{10}(F_n) \approx n \log_{10}(\varphi) - \frac{1}{2} \log_{10}(5)
\]

We want:

\[
\log_{10}(F_n) \ge 999
\]

Solving for \(n\):

\[
n \ge \frac{999 + 0.5 \log_{10}(5)}{\log_{10}(\varphi)}
\]

Python implementation:

```python
import math

phi = (1 + math.sqrt(5)) / 2
n = math.ceil((999 + 0.5 * math.log10(5)) / math.log10(phi))
print(n)
```

Output:

```
4782
```

---

## Comparison

| Method               | Complexity  | Pros                          | Cons                               |
|----------------------|-------------|--------------------------------|------------------------------------|
| Generator (Exact)    | O(n)        | Simple, intuitive, exact      | Must compute thousands of terms   |
| Binet’s Formula      | O(1)        | Instant, mathematically elegant| Requires logs & approximations    |

Both methods give **4782** as the index of the first 1000-digit Fibonacci number.

---

## Conclusion

This problem showcases the power of combining **Pythonic iteration techniques** (generators, `itertools`) with **mathematical analysis** (Binet’s formula, logarithms).  
The brute-force generator method is easy to write and understand, while the mathematical shortcut gives an instant result.

Try solving other Project Euler problems using both approaches — you’ll get better at both **coding** and **math**!
