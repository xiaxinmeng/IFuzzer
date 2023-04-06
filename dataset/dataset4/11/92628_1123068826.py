def proposal3(iterable):
    g = groupby(iterable)
    return not any(g) or not any(g)

def proposal4(iterable):
    g = groupby(iterable)
    return not (any(g) and any(g))