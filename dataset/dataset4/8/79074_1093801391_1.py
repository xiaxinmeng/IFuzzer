s.send(str.encode("Foo"))
data = s.recv(1024).decode("utf-8")