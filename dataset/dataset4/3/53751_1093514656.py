def fsdecode(value):
    if isinstance(value, str):
        return value
    elif isinstance(value, bytes):
        encoding = sys.getfilesystemencoding()
        if encoding == 'mbcs':
            return value.decode(encoding)
        else:
            return value.decode(encoding, 'surrogateescape')
    else:
        raise TypeError("expect bytes or str, not %s" % type(value).__name__)