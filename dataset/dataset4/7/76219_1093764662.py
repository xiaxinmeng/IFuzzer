@contextlib.contextmanager
def dont_close_socket(sock):
    assert not sock._closed
    sock._io_refs += 1
    try:
        yield sock
    finally:
        sock._io_refs -= 1