
import timeit
cache = {i: (i, i + 1, None, f'a{i}') for i in range(1000)}
timeit.timeit('list(cache.items())', number=1000, globals=locals())
# 0.18165644304826856
timeit.timeit('list(cache.values())', number=1000, globals=locals())
# 0.04786261299159378
