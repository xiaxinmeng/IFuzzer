if sock is not None:
    type = sock.type
if type & socket.SOCK_STREAM != socket.SOCK_STREAM:
    raise NotImplementedError