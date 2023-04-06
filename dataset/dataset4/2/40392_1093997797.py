def gen():
        l = []
        l.append('eggs')
        l = l[-1:]
        yield l
        l.append('ham')
        l = l[-1:]
        yield l