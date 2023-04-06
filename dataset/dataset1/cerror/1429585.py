import socket, time
from threading import Thread

class cthread(Thread):
        def __init__ (self):
                Thread.__init__(self)

        def run(self):
                socket.setdefaulttimeout(5)
                res = socket.getaddrinfo('19.54.123.2', 33, 
0, socket.SOCK_STREAM)[0]
                sock = socket.socket(res[0], res[1], res[2])
                try:
                        sock.connect(res[4])
                except: pass

def main():
        for i in range(1900):

                ct = cthread()
                ct.start()

if __name__ == '__main__':
        main()
