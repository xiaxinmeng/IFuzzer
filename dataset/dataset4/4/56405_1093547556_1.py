def pipe_buffer_size(fd):
    if hasattr(os, 'fpathconf'): # better than sys.platform == "win32"?
        pipe_buf = 512
    else:
        pipe_buf = os.fpathconf(fd, "PC_PIPE_BUF")