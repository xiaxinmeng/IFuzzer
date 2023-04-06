
def slow_dictionary(d):
    while len(d) > 0:
        # Remove first element
        key = next(iter(d))
        del d[key]
