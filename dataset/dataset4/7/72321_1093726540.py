def accept(sock):
    client, addr = sock.accept()
    inside = socket(fileno=client.fileno())
    print(inside)
    # <__main__.Socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 42532)>
    return inside

outside = accept(sock)
print(outside)
# <__main__.Socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6>