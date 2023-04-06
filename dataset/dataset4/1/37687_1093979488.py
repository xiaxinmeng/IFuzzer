def sort(sequence, cmpfunc=None):
    sorted = list(sequence)
    if cmpfunc is None:
        sorted.sort()
    else:
        sorted.sort(cmpfunc)
    return sorted