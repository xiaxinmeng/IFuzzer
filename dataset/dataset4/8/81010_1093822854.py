@contextlib.contextmanager
def throw_unraisable_exceptions():
    unraisable = None
    old_hook = sys.unraisablehook

    def hook(exc):
        nonlocal unraisable
        unraisable = exc

    sys.unraisablehook = hook
    try:
        yield
        if unraisable is not None:
            raise unraisable
    finally:
        unraisable = None
        sys.unraisablehook = old_hook