def f():
    try:
        raise KeyError
    except Exception:
        yield

gen = f()
gen.send(None)
gen.throw(ValueError)
