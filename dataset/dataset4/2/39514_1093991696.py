import socket

def test():
    s = socket.socket()
    s.connect(('koeln.ccc.de', 80))
    s.send('GET / HTTP/1.1\r\nHost: koeln.ccc.de\r\n\r\n')
    # I know, I get only len(MTU)
    s.recv(30000)
    s.shutdown(2)
    s.close()
    del s

for i in range (500):
    test()