if not(stdin is None or stdin in (PIPE, DEVNULL) or isinstance(stdin, int)):
    try:
        stdin.fileno()
    except (AttributeError, UnsupportedOperation, OSError):
        inputdata = stdin.read()
        stdin = PIPE