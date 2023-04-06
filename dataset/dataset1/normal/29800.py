from functools import partial
p = partial(int)
p.keywords[1] = 10
repr(p)
