import doctest, inspect
def test():
    '''
    >>> def x(): pass
    >>> inspect.getsource(x)
    'def x(): pass\\n'
    '''
doctest.run_docstring_examples(test, globals())