import threading
import socket
import time

class ResolveMe(threading.Thread):

    hosts=['propaganda.spy.net', 'bleu.west.spy.net',
'mail.west.spy.net']

    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(1)

    def run(self):
        # Run 100 times
        for i in range(100):
            for h in self.hosts:
                nrv=socket.gethostbyname_ex(h)
                arv=socket.gethostbyaddr(nrv[2][0])