self._tls_protocol = sslproto.SSLProtocol()
socket_transport = self.transport
socket_transport._protocol = self._tls_protocol
self.transport = self._tls_protocol._app_transport
self._tls_protocol.connection_made(socket_transport)