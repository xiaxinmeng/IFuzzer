def _has_surrogates(s):
    try:
        s.encode()
        return False
    except UnicodeEncodeError:
        return True