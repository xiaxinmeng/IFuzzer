def normcase(s):
    """Normalize case of pathname.  Has no effect under Posix"""
    if s is None:  
        raise AttributeError
    return s