
addr, port, errnm, elapsed = struct.unpack("=4s!H=H=Q")
addr = socket.inet_ntoa(addr)
