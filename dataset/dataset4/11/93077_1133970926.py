import io
stream = io.TextIOWrapper(io.BytesIO(b'"")\r\nx\r\n'))
stream.read(1)
stream.read(1)
stream.read(1)
print('-----> tell:', stream.tell())