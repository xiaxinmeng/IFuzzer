def negative(fname, flags):
    return -1


with open('/tmp/foo.txt', 'w', encoding='utf-8', opener=negative) as fp:
    print('oops', file=fp)