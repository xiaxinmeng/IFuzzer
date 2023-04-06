def f():
    yield

def g():
    try:
        raise KeyError('a')
    except Exception:
        yield from f()

gen = g()
gen.send(None)
gen.throw(ValueError)