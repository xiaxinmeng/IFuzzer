# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def f():
    """
    >>> f()
    u'xyz'
    """
    return "xyz"

if __name__ == "__main__":
    import doctest
    doctest.testmod()