socket.setblocking(0)
socket.send(b'a' * 32 * 1024 * 1024)