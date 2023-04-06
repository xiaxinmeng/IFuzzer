from functools import wraps
from inspect import signature

def g(a: float, b=10):
    return a * b

def f(a: int, b=1):
    return a * b

assert f(3) == 3

f = wraps(g)(f)

assert str(signature(f)) == '(a: float, b=10)'  # signature says that b defaults to 10
assert f.__defaults__ == (1,)  # ... but it's a lie!
assert f(3) == 3 != g(3) == 30  # ... and one that can lead to problems!