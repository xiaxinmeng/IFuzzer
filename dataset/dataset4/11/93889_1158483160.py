def func(self):
    return "ok"
bound = func.__get__(42)

from pickle import dumps, loads
loads(dumps(bound)) # AttributeError: 'int' object has no attribute 'func'