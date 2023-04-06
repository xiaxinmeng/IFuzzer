import io
def _bad_open1(*args):
    io.open = _bad_open2
    raise Exception


def _bad_open2(*args):
    return 42

io.open = _bad_open1

1/0