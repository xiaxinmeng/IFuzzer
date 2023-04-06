if hasattr(socket, 'SO_EXCLUSIVEADDRUSE'):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 1)
            # Also need to change the value of allow_reuse_address (defined in http.server.HTTPServer)
            HTTPServer.allow_reuse_address = 0