
def can_reiterable(x):
    return hasattr(x, '__iter__') and not hasattr(x, '__next__')
