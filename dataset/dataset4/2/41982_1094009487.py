if self.allow_reuse_address:
    self.socket.setsockopt(socket.SOL_SOCKET,
                           socket.SO_REUSEADDR, 1)
    self.socket.bind(self.server_address)