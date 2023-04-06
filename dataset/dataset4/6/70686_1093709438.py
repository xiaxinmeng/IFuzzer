body = (
   b"HTTP/1.1 200 OK\r\n"
   b"Content-Length: 3\r\n"
   b"\r\n"
   b"abc"
   b"HTTP/1.1 408 Next response should not be read yet\r\n"
)