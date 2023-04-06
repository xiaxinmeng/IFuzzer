def newbin(f):
    """
        >>> newbin(3.125)
        '0b11001 * 2.0 ** -3'
    """
    n, d = f.as_integer_ratio()
    s = '%s * 2.0 ** %d' % (bin(n), -math.log(d, 2.0))
    return s