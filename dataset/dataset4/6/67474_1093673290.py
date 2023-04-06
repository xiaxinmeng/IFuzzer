rd.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, support.SOCK_MAX_SIZE // 3)
wr.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, support.SOCK_MAX_SIZE // 3)