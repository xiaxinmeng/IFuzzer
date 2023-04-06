def f():
    yield

def g():
    try:
        raise RuntimeError('a')
    except Exception as exc:
        print(f'handling: {exc!r}')
        yield from f()

def h():
    try:
        raise RuntimeError('b')
    except Exception as exc:
        print(f'handling: {exc!r}')
        yield from g()

gen = h()
gen.send(None)
gen.throw(ValueError)