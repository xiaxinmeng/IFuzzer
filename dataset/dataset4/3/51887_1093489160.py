while request_buffer.split("\n")[-1] != "" or request_buffer == "":
    request_buffer += self.conn.recv(1024)
    print("Got a line!")

print("Got an empty line!")
self.handleRequest(request_buffer)