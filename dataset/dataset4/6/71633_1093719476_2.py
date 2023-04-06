
addr, port, errnm, elapsed = struct.unpack("=4sHHQ")
addr = socket.inet_ntoa(addr)
port = socket.ntohs(port)
