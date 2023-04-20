"""
Timing the recursive Fibonacci function
Expected to be ~1.6^n (i.e. O(fibonacci(n))
"""

import time

def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number. Uses the 0-start sequence."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 5 million attempts for each n value
times = []
for n in range(4, 12):
    start = time.time()
    for i in range(5000000):
        fibonacci(n)
    end = time.time()
    times.append(end - start)

# Ratios of consecutive n values
for i in range(1, len(times)):
    print(f'{times[i] / times[i - 1]:.2f}')

"""
Output on my machine:
1.56
1.70
1.61
1.61
1.61
1.73
1.64
"""
