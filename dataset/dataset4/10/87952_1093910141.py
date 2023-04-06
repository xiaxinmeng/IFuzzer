def equal(a, b):
    flag = (a == b)
    if isinstance(flag, bool):
        return flag
    else:
        return all(flag)