def to_unicode(obj, encoding='utf8', errors='strict'):
    # the encoding default should look at sys's value
    try:
        return unicode(obj)
    except UnicodeDecodeError:
        return unicode(obj, encoding=encoding, errors=errors)