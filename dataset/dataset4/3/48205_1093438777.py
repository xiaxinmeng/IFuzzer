# This program works fine with Python 2.5 and 2.6:
def f():
    """
    >>> f()
    'xyz'
    """
    return "xyz"

if __name__ == "__main__":
    import doctest
    doctest.testmod()