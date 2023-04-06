def sort(sequence, cmpfunc=None):
    sorted = list(sequence)
    sorted.sort(cmpfunc)
    return sorted