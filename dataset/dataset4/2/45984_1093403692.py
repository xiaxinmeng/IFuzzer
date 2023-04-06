def group(iterable, n=2):
    return itertools.izip(*(iter(iterable),)*n)