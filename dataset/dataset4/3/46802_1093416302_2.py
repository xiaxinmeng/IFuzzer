def bind_port(sock, host='127.0.0.1', *args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, 0))
    port = s.getsockname()[1]
    s.close()
    del s

    sock.bind((host, port))
    return port