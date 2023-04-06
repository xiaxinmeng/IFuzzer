def leak():
    def gen():
        while True:
            yield g
    g = gen()
    g.next()