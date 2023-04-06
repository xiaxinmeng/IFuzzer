import optparse

def foo():
    """
    >>> foo() #doctest: +ELLIPSIS
    Traceback (most recent call last):
          . . .
    ...OptionError: option bar: foo
    """
    raise optparse.OptionError('foo', 'bar')

if __name__ == "__main__":
    import doctest
    doctest.testmod()