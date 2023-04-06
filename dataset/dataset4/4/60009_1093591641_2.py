@contextlib.contextmanager
def redirect_stdout(stream):
    old_stdout = sys.stdout
    sys.stdout = stream
    yield
    sys.stdout = old_stdout