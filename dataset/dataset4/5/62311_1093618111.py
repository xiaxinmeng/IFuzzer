it = iter([328, 28, 2989, 22])
functools.reduce(max, it, next(it, None))
2989