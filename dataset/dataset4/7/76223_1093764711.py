def str_fun():
    """
    >>> str_fun()
    'foo'
    >>> str_fun()
    "foo"
    >>> str_fun()
    '''foo'''
    """
    return 'foo'


def dict_fun():
    """
    >>> dict_fun()
    {'foo': 1, 'bar': 2}
    >>> dict_fun()
    {'bar': 2, 'foo': 1}
    >>> dict_fun()
    dict(foo=1, bar=2)
    """
    return {'foo': 1, 'bar': 2}


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ACCEPT_EQUAL_VALUES)