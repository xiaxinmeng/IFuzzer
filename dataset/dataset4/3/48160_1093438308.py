def ssl(sock, keyfile=None, certfile=None):
    if hasattr(sock, "_sock"):
        sock = sock._sock
    return _realssl(sock, keyfile, certfile)