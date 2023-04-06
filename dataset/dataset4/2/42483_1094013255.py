def pickle_set(s):
    return set, list(s)

pickle(set, pickle_set, set)

def pickle_frozenset(s):
    return frozenset, list(s)

pickle(set, pickle_set, set)