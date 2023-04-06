import functools
x = functools.partial(min)
x.__setstate__((x, (), {}, {}))
repr(x)
