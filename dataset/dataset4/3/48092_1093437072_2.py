def closingiterator(it):
    def wrapper():
        for x in it:
            yield x
    return closing(wrapper())