import doctest

def test():
    """
    >>> print 42 #doctest: +ELLIPSIS
    ...
    """

def run():
    "Run the test."
    doctest.testmod()

if __name__ == '__main__':
    run()