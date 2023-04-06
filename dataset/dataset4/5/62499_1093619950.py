@contextlib.contextmanager
def kill_on_error(proc):
    """Context manager killing the subprocess if a Python exception is raised."""
    with proc:
        try:
            yield proc
        except:
            proc.kill()
            raise