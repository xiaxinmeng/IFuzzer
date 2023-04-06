class C:
    pass
c = C()
cycle = set([c])
c.foo = cycle