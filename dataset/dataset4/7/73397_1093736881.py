def simple_gen():
    yield 1, None
    try:
        1/0
    except ZeroDivisionError as err:
        yield None, err
    yield 3, None

class Spam:
    def __init__(self):
        self.gen = simple_gen()
    def get_next(self):
        value, err = next(self.gen)
        if err is not None:
            raise err
        return value