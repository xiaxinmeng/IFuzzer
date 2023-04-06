def test_preadv_stdlib(path):
    fd = os.open(path, os.O_RDWR | os.O_CREAT)
    buffer = bytearray(10)
    buffers = [buffer]
    try:
        length = os.preadv(fd, buffers, 0, os.RWF_NOWAIT)
        # OSError: [Errno 95] Operation not supported
        print('length:', length)
        print('buffer:', buffer)
    finally:
        os.close(fd)