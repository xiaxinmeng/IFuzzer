with open('big', 'wb') as fobj:
    for _ in xrange(1024 * 1024 * 5):
        fobj.write('1' + '0' * 1023)