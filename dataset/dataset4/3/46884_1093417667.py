while len(data) < size:
    data = data + sock.recv(size - len(data))