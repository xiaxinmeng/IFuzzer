lsts = [lst1, lst2, ...]
joiner = [None, 'STOP', None]
lsts_joined = list(itertools.chain.from_iterable(lst + joiner for lst in lsts))[:-len(joiner)]