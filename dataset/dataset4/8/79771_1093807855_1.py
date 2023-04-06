def _create_socket(af, socktype, proto): # or adding *args, **kwargs?
    socket.socket(af, socktype, proto)

sock = create_socket(af, socktype, proto) 
if socktype == socket.SOCK_STREAM:
    sock.connect(sa)