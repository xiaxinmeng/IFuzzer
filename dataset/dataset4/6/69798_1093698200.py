def f():
    try:
        raise KeyError
    except Exception:
        try:
            yield
        except Exception:
            pass
        raise