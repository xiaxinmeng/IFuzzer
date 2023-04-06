def connection_made(self, transport: asyncio.BaseTransport) -> None:
    sock = transport.get_extra_info('socket')  # type: socket.socket
    sock.ioctl(SIO_UDP_CONNRESET, False)