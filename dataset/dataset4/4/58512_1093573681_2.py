def utf8bmp_encode(s):
    return re.sub('[^\x00-\uffff]', lambda m: '\\U%08x' % ord(m.group()), s).encode('utf-8')