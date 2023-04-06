def iterboom():
    raise AssertionError
    yield 1

next(1 for x in iterboom())