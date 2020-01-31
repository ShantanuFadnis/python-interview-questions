def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_arr(n):
    temp = [0] * (n + 1)
    temp[0] = 1
    temp[1] = 1
    for i in range(2, n):
        temp[i] = temp[i - 1] + temp[i - 2]
    return temp[n - 1]


def fib_memoization(n):
    if n == 1 or n == 2:
        return 1
    first = 1
    second = 1
    res = 0
    for _ in range(2, n):
        res = first + second
        first = second
        second = res
    return res


if __name__ == '__main__':
    n = int(input('> '))
    res = fib_recursive(n)
    print(res)
    res = fib_arr(n)
    print(res)
    res = fib_memoization(n)
    print(res)
