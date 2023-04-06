def call(*popenargs, timeout=None, **kwargs):
    p = Popen(*popenargs, **kwargs)
    try:
        if timeout is None:
            try:
                return p.wait()
            except:
                p.wait()  # Let the child handle SIGINT
                raise
        else:
            return p.wait(timeout=timeout)
    except:
        p.kill()  # Last resort to avoid leaving a zombie
        p.wait()
        raise