def accept(sock):
    client, addr = sock.accept()
    inside = socket(fileno=client.fileno())
    client.detach()
    print(inside)
    return inside
    # after return, the client socket is closed by due to detach the fd isn't no longer close