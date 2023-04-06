def listdir2(path, dir_fd=None):
    fd = os.open(path, dir_fd)
    try:
        return os.listdir(fd)
    finally:
        os.close(fd)