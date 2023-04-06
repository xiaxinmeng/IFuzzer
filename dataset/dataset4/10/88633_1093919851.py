def wraps_with_name(func, decorator, **kwargs):
    def wraps_with_name_decorator(wrapped):
        new_name = f'{func.__name__}@{decorator.__name__}'
        new_code = wrapped.__code__.replace(co_name=new_name)
        # would be nice if `types.FunctionType` had a `.replace(...)` too!
        new_wrapped = types.FunctionType(
            new_code,
            wrapped.__globals__,
            new_name,
            wrapped.__defaults__,
            wrapped.__closure__,
        )
        return functools.wraps(func, **kwargs)(new_wrapped)
    return better_wraps_decorator