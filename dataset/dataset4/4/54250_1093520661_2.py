# echo client program
data = b'hello\r\n'
import socket
clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  clie.connect(('localhost', 12345))

  clie.send(data)
  data = clie.recv(4096)
  print(repr(data), 'recv()')

  clie.send(data)
  file = clie.makefile('rb')
  data = file.readline()
  print(repr(data), 'makefile(mode = "rb")')

  clie.send(data)
  file = clie.makefile('r', newline = '')
  data = file.readline()
  print(repr(data), 'makefile(mode = "r", newline = "")') ## '\r' is still silently dropped
finally:
  clie.close()