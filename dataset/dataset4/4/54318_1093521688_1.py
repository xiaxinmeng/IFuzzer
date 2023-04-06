naa=(''.join((str(n),)+s) for n in itertools.count(1)
     for s in itertools.product(string.ascii_uppercase[0:5], repeat=2))