def utf8bmp_encode(s):
    return ''.join(c if ord(c) <= 0xffff else '\\U%08x' % ord(c) for c in s).encode('utf-8')