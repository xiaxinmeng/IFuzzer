import math
import cProfile

def fact(n):
    print(sum(1 / math.factorial(n) for n in range(18)))

fact(200)