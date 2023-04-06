if code := getattr(socket, "TCP_NOTSENT_LOWAT", None):
    sock.setsockopt(socket.SOL_TCP, code, 42)