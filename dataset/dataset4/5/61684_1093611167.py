import functools
import inspect

def my_wrapper(fn):
    def wrapped(x, y, z):
        return my_func(x, y)
    wrapped = functools.update_wrapper(wrapped, fn)
    return wrapped

def my_func(x, y):
    pass

wrapper = my_wrapper(my_func)