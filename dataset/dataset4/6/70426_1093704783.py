if self._tunnel_host:
	server_hostname = self._tunnel_host
else:
	server_hostname = self.host

self.sock = self._context.wrap_socket(self.sock,
									  server_hostname=server_hostname)