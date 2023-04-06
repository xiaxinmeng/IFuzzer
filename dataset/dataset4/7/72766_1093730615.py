d = dict.fromkeys(range(100))
for k in range(99):
    del d[k]

it = iter(d)
assert next(it) == 99
d.clear()
d[0] = None
next(it)