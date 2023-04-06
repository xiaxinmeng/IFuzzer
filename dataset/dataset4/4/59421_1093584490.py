def replace_stdout():
    """Set stdout encoder error handler to backslashreplace (as stderr error
    handler) to avoid UnicodeEncodeError when printing a traceback"""
    import atexit

    stdout = sys.stdout
    sys.stdout = open(stdout.fileno(), 'w',
        encoding=stdout.encoding,
        errors="backslashreplace",
        closefd=False,
        newline='\n')

    def restore_stdout():
        sys.stdout.close()
        sys.stdout = stdout
    atexit.register(restore_stdout)