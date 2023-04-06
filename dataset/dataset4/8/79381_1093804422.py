# untested
def dumb_range_repr(r):
    if len(r) < 5:
        return f"<range object {list(r)}>"
    else:
        return f"<range object [{r[0]}, {r[1]}, ..., {r[-2]}, {r[-1]}]>"