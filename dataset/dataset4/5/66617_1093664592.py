import tempfile
def generator():
    with tempfile.TemporaryDirectory():
        yield
g = generator()
next(g)