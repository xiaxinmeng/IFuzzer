def secondmax(iterable):
    """return the second largest value in iterable"""
    m = max(iterable)
    return max(i for i in iterable if i<m)