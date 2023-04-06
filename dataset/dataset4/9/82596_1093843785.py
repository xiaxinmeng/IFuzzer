
@contextmanager
def some_context():
    ...
    yield

@some_context()
def some_function():
    # we are inside a with some_context() now. 
    ...


