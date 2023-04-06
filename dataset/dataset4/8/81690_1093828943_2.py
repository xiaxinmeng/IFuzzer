class iovec(ctypes.Structure):
    _fields_ = [('iov_base', ctypes.c_char_p), ('iov_len', ctypes.c_size_t)]


libc = ctypes.CDLL('libc.so.6')


def test_preadv_libc(path):
    fd = os.open(path, os.O_RDWR | os.O_CREAT)
    buffer = bytes(10)
    buffers = (iovec*1)()
    buffers[0].iov_base = buffer
    buffers[0].iov_len = 10
    try:
        length = libc.preadv2(fd, buffers, len(buffers), 0, os.RWF_NOWAIT)
        print('length:', length)  # length: -1
        print('buffer:', buffer)  # buffer: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    finally:
        os.close(fd)