def token_names():
    import tokenize
    res = {}
    names = dir(tokenize)
    for name in names:
        attr = getattr(tokenize, name)
        if type(attr) is type(1):
            res[attr] = name
    return res