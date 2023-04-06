from functools import wraps, WRAPPER_ASSIGNMENTS, partial

my_wraps = partial(wraps, assigned=(list(WRAPPER_ASSIGNMENTS) + ['__defaults__', '__kwdefaults__']))

def g(a: float, b=10):
    return a * b

def f(a: int, b=1):
    return a * b

assert f(3) == 3

f = my_wraps(g)(f)

assert f(3) == 30 == g(3)
assert f.__defaults__ == (10,)  # ... because now got g defaults!