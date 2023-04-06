sock = socket.socket(af, socktype, proto)
if timeout:
    sock.settimeout(timeout)
if socktype == socket.SOCK_STREAM:
    sock.connect(sa)