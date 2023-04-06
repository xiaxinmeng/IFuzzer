
def decorator_with_params(deco):
    @wraps(deco)
    def decorator(func=None, /, *args, **kwargs):
        if func is not None:
            return deco(func, *args, **kwargs)

        def wrapper(f):
            return deco(f, *args, **kwargs)

        return wrapper

    return decorator
