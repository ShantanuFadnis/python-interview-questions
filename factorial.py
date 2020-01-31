def factorial(n):
    """Returns the factorial of a given integer"""
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_recursive(n):
    """Returns the factorial of a given integer"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    num = int(input('> '))
    print(factorial(num))
    print(factorial_recursive(num))
