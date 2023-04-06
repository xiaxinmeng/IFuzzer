class Deco:
    "A decorator."
    def __init__(self, func):
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kwargs):
        pass

@Deco
def double(n):
    "A function."
    return n * 2