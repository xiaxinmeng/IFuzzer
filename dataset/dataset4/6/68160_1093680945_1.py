if reuseport_supported:
    self.assertTrue(
        sock.getsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEPORT))