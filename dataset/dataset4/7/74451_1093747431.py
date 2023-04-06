def unlink(filename):
    try:
        _unlink(filename)
    except OSError:
        pass