from __future__ import unicode_literals

def print_string():
    """
    >>> print '缺陷'
    缺陷
    """
    pass

def print_unicode():
    """
    >>> print u'缺陷'
    缺陷
    """
    pass

def string_repr():
    """
    >>> '缺陷'
    u'\u7f3a\u9677'
    """
    pass

def unicode_repr():
    """
    >>> u'缺陷'
    u'\u7f3a\u9677'
    """
    pass

def unicode_escape_repr():
    """
    >>> u'\u7f3a\u9677'
    u'\u7f3a\u9677'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()