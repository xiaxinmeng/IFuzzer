def sugar(*args, **kw):
    return args[0].submit(args[1], args[2:], kw)