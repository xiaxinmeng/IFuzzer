def cast(type):
    def wrapper(func):
        @wraps(func)
        def newfunc(*args, **keywords):
            return type(func(*args, **keywords))

        return newfunc

    return wrapper