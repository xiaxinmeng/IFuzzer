import itertools

l = []
it = itertools.chain.from_iterable(l)
l.append(it)
next(it)
