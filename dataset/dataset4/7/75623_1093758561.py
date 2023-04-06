import io
def _bad_open(*args):
    return 42

io.open = _bad_open
1/0