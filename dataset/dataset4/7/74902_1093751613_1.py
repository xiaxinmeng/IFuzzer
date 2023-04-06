import unicodedata

def chars(string):
    accum = []
    for c in string:
        cat = unicodedata.category(c)
        if cat == 'Mn':
            accum.append(c)
        else:
            if accum:
                yield accum
                accum = []
            accum.append(c)
    if accum:
        yield accum