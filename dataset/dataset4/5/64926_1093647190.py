def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    sentinel = object()
    it = chain.from_iterable(zip_longest(fillvalue=sentinel, *iterables))
    return (i for i in it if i is not sentinel)