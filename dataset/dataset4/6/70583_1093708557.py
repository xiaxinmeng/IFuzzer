socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('0.0.0.0', port))
socket.setblocking(False)
while True:
    data, addr = await loop.sock_recvfrom(sock, 4096)
    # process packet