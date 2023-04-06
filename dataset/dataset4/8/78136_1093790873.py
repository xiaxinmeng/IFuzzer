def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("fib(10)", setup="from __main__ import fib"))