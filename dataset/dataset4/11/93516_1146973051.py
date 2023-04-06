from time import perf_counter
import coverage

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

t0 = perf_counter()
cov = coverage.Coverage()
cov.start()
fib(35)
cov.stop()
cov.save()
t1 = perf_counter()
print(t1 - t0)