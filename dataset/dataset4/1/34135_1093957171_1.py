pycon
# file test_doctest.py
"""
    >>> print "\\nhello\\n"
.
    hello
.
    >>>
"""
def _test():
    import doctest, test_doctest
    return doctest.testmod(test_doctest)
if __name__ == "__main__":
    _test()
