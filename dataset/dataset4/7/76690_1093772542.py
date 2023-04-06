import doctest

def print_3_dot():
    """
    >>> print_3_dot()
    ...
    """
    print('...')

doctest.run_docstring_examples(print_3_dot, globals())
# --- cut %< 