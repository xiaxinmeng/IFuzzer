fd = os.open(...)
try:
    if not stat.S_ISREG(os.fstat(fd).st_mode):
        raise OSError(None, "Not a regular file", ...)
    f = os.fdopen(fd, ...)
except EnvironmentError:
    os.close(fd)