@contextlib.contextmanager
def popen_killer(proc):
    try:
        yield
    except:
        # Close pipes
        if proc.stdin:
            proc.stdin.close()
        if proc.stdout:
            proc.stdout.close()
        if proc.stderr:
            proc.stderr.close()
        try:
            proc.kill()
        except OSError:
            # process already terminated
            pass
        proc.wait()
        raise


def popen_communicate(proc):
    with popen_killer(proc):
        return proc.communicate()