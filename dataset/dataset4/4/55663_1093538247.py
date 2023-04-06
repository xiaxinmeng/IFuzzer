def _has_surrogates(s):
    import email.utils
    f = re.compile('[\udc80-\udcff]').search
    email.utils._has_surrogates = f
    return f(s)