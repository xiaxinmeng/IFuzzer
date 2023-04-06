def __gen(iter1):
    for x in iter1:
        yield x
g = __gen(range(10))