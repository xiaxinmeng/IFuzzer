def to_hex(a):
    if type(a) == type(0.0):
        return a.hex()
    elif type(a) == type(1):
        return hex(a)
    else:
        raise TypeError('Must be int or float')