def decorate_callable(self, func, async_func=False):
    def patched(func):
        if async_func:
            yield from func(*args, **keywargs)
        else:
            return func(*args, **keywargs)
    if async_func:
        patched = types.coroutine(async_func)  