if encoding is None:
    return language
elif sys.platform == 'win32' and encoding not in {'utf8', 'utf-8'}:
    return language
else:
    return language + '.' + encoding