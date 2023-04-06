def my_decorator(f):
    def wrapper(*args, **kwds):
        return f(*args, **kwds)
    wrapper = update_wrapper(wrapper, f)
    return wrapper