while not request_buffer.endswith(('\r', '\n')):
    request_buffer += self.conn.recv(1024)
    print("Got a line!")

print("Got an empty line!")
self.handleRequest(request_buffer)