"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

"""
from random import uniform


def truncate(n, decimals=3):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def estimate_pi(n, r=0.5, h=0, k=0):
    inner = 0
    total = 0
    pi = 0
    for _ in range(n):
        total += 1
        x = round(uniform(h - r, h + r), 1)
        y = round(uniform(k - r, k + r), 1)
        if ((x - h) ** 2) + ((y - k) ** 2) <= r ** 2:
            inner += 1
        pi = truncate((inner / total) * 4)
    print(f'Final estimation of Pi after {n} iterations: {pi}')


TEST_CASES = [5, 10, 50, 100, 1000, 5000, 10000, 50000, 100000, 500000]
for case in TEST_CASES:
    estimate_pi(case)
