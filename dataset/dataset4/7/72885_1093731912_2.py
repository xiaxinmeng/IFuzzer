def get_numbers_differently():
    yield 1
    raise Exception("oops")
    yield 2