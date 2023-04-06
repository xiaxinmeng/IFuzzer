def my_decorator(f):
    def wrapper(*args, **kwds):
        return f(*args, **kwds)
    wrapper = wraps(f)(wrapper)
    return wrapper