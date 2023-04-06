@contextmanager
def elapsed(cb: Callable[[float, float], None], counter=time.perf_counter):
    t0 = counter()
    try:
        yield
    finally:
        t1 = counter()
        cb(t0, t1)