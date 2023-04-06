sd = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
sd.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)