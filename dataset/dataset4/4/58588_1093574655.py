if _charset == 'us-ascii':
    try:
        _text.encode(_charset)
    except UnicodeEncodeError:
        try:
            _text.encode('latin-1')
        except UnicodeEncodeError:
            _charset = 'utf-8'
        else:
            _charset = 'latin-1'