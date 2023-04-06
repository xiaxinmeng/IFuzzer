s = socket.socket()
s.bind(('',50007))
s.listen(1);
s.close();