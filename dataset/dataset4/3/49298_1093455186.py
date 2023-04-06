def subsets(iterable):
    l = list(iterable)
    for selector in itertools.product([False, True], repeat=len(l)):
        yield [element for indicator, element in zip(selector, l) if indicator]