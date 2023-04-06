def set_keepalive(writer: asyncio.StreamWriter) -> None:
	keep_idle = 30
	keep_interval = 5
	keep_count = 10  # Fixed to 10 on Windows
	sock: socket.socket = writer.transport.get_extra_info('socket')
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
	try:  # POSIX
		sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, keep_idle)
		sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, keep_interval)
		sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, keep_count)
	except AttributeError:  # Windows
		sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, keep_idle * 1000, keep_interval * 1000))