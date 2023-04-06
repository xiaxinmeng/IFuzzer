import math
import cProfile

def fact(n):
    return sum(1 / math.factorial(n) for n in range(18))