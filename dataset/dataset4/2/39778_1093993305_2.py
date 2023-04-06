def g():
    result = lambda x: x+y
    for y in range(3):
        yield result