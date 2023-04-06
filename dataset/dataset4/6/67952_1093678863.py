def wrapper(func):
    return functools.wraps(func)(functools.partial(func))