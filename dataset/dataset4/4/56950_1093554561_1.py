def move2(src, dst):
    try:
        fd = os.open(dst, os.O_EXCL | os.O_CREAT)
    except OSError:
        raise Error('Destination exists')
    try:
        move(src, dst)
    finally:
        os.close(fd)