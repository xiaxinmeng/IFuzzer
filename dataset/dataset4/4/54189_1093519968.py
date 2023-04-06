import timeit

s = "str(38210.0)"
t = timeit.Timer(stmt=s)

t.timeit(number=10000000)
t.timeit(number=10000000)
t.timeit(number=10000000)