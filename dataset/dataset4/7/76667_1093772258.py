def g1():
    yield from g2()
def g2():
    yield 1/0
for i in g1(): pass