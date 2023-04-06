def sub(pattern, repl, string, count=0, flags=0):
    print('re.sub: pattern=%s, repl=%s, string=%s' % (pattern.__class__.__name__, repl.__class__.__name__, string.__class__.__name__))
    return _compile(pattern, flags).sub(repl, string, count)