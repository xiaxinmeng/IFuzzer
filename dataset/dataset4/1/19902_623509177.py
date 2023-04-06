def g():
    try:
        raise KeyError
    except KeyError:
        pass

    try:
        yield
    except Exception:
        # This is where the crash occurs on some platforms without the
        # `gi_exc_state.exc_type != Py_None` check in _gen_throw().
        raise RuntimeError

gen = g()
gen.send(None)
gen.throw(ValueError)