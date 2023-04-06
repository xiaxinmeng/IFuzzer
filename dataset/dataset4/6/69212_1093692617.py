@contextmanager
def mymkdtemp():
    yield mkdtemp()