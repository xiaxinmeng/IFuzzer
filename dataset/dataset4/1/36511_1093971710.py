def iterzip(*collections):
    iterables = map(iter, collections)
    while 1:
        yield tuple([i.next() for i in iterables])