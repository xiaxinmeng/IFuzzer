def leak():
    class gen:
        def __iter__(self):
            return self
        def next(self):
            return self.item
    g = gen()
    head, tail = tee(g)
    g.item = head