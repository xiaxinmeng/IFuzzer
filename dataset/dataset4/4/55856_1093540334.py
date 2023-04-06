@contextmanager
def func():
    while True:
        print('begin func')
        yield
        print('end func')
        yield