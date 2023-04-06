def toepoch(d):
    x, y = divmod(d, timedellta(0, 1))
    return x, y.microseconds