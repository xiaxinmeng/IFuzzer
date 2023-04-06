def custommax(it):
    best = -9999999
    for x in it:
        if x > best:
            best = x
    return best