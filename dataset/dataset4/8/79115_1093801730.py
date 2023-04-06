import select, socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)
s.bind(('0.0.0.0', 6666))
s.listen(100)

select.select([s], [], [], None)
s.close()