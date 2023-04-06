def basename(p):
    i = p.rfind('/') + 1
    return p[i:]

def dirname(p):
    i = p.rfind('/') + 1
    return p[:i]