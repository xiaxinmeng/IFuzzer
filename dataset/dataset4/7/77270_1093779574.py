def distance(p, q):
    # TODO error checking that p and q have the same number of items
    return hypot(*(x-y for x,y in zip(p, q)))