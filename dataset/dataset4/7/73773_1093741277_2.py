import sys

def f():
    try:
        raise KeyError
    except Exception:
        print(sys.exc_info())
        try:
            yield
        except Exception:
            pass
        print(sys.exc_info())
        raise

gen = f()
gen.send(None)
gen.throw(ValueError)