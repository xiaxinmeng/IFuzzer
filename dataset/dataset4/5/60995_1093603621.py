b = [1]
import itertools
b += itertools.chain.from_iterable([c] for c in b)