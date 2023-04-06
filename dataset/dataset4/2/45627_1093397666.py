@contextlib.contextmanager
def closes(file):
    yield file
    file.close()