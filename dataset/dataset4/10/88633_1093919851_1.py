def my_decorator(func):
    @functools.wraps_with_name(func, my_decorator)
    def my_decorator_inner(*args, **kwargs):
        return func(*args, **kwargs)
    return my_decorator