from operator import mul
def factorial(num):
    return reduce(mul, range(2, num+1), 1)