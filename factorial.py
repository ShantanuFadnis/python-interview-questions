def fact(n):
    if n == 0 or n == 1:
        return 1
    
    res = 1
    for i in range(1, n + 1):
        res *= i
    
    return res

if __name__ == '__main__':
    res = fact(int(input('> ')))
    print(res)
