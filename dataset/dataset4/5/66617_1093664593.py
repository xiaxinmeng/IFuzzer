import tempfile
import gc

def generator():
    with tempfile.TemporaryDirectory():
        print("before yield")
        yield
        print("after yield")
g = generator()
next(g)

g = None
gc.collect()