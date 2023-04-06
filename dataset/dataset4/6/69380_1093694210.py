def collect(seed, iterable):
    return it.accumulate(it.chain([seed], iterable))