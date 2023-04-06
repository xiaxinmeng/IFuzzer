import itertools
it = itertools.chain.from_iterable((f() for f in [lambda: it]))
list(it)