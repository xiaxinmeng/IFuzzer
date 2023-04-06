from collections import defaultdict
from functools import wraps
import inspect


def foo(*args):
    def decorator(func):
        @wraps(func)
        def wrapper():
            pass
        return wrapper
    return decorator

@foo(dict(), defaultdict(lambda: 1))
def f():
    pass

print(inspect.getsource(f))