
from functools import wraps, WRAPPER_ASSIGNMENTS, partial

# First, I need to add `__defaults__` and `__kwdefaults__` to wraps, because they don't come for free...
my_wraps = partial(wraps, assigned=(list(WRAPPER_ASSIGNMENTS) + ['__defaults__', '__kwdefaults__']))

def g(a: float, b=10):
    return a * b

def f(a: int,  *, b=1):
    return a * b

# all is well (for now)...
assert f(3) == 3
assert g(3) == 30
