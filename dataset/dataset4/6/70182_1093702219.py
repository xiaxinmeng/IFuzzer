def f():
    with some_lock:
        yield 0
        yield 1

def g():
    with another_lock:
        it = f()
        for i in it:
            raise