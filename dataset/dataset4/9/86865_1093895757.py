import timeit
# gen comp
timeit.timeit("''.join(str(_) for _ in range(1000))", number=10000)
11.154560299999957