def report(exc):
    print('lineno %s, offset %s' % (exc.lineno, exc.offset))
    raise