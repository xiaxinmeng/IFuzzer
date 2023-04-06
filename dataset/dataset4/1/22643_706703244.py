def run_with_broken_pipe_awareness(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except BrokenPipeError as exc:
        sys.stdout = None
        sys.exit(exc.errno)