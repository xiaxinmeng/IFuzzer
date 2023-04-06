@contextlib.contextmanager
def capture_stdout():
    import sys
    import tempfile
    stdout_fd = sys.stdout.fileno()
    with tempfile.TemporaryFile(mode='w+b') as tmp:
        stdout_copy = os.dup(stdout_fd)
        try:
            sys.stdout.flush()
            os.dup2(tmp.fileno(), stdout_fd)
            yield tmp
        finally:
            sys.stdout.flush()
            os.dup2(stdout_copy, stdout_fd)
            os.close(stdout_copy)