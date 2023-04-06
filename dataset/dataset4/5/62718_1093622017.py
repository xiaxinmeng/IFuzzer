from timeit import timeit

snippet="""
for i in range(10):
    return -1
"""

print(timeit(snippet))