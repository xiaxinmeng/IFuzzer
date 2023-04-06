import contextlib

@contextlib.contextmanager
def foo():
    yield

class StartIrritation(StopIteration):
    pass


with foo():
    raise StartIrritation