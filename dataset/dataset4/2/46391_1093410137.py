import operator
def factorial(num):
    return reduce(operator.mul, range(1, num+1))