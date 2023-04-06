import gc, sys

def iterfind():
    yield 1

def _get_first_or_none():
    it = iterfind()
    try:
        raise RuntimeError()
    except:
        return next(it)

def test():
    _get_first_or_none()
    gc.collect();
    print(sys.exc_info()) # crash
test()
