def create(file):
    fd = os.open(file, os.O_EXCL | os.O_CREAT | os.O_WRONLY)
    return os.fdopen(fd)