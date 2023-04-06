sock = socket.socket(af, socktype, proto)
if socktype == socket.SOCK_STREAM:
    sock.connect(sa)