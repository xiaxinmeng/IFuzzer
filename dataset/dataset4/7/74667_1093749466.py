
import threading
import socket

def getservbyname_loop(service, port):
        while True:
                result = socket.getservbyname(service)
                if result != port:
                        raise RuntimeError("thread-safety broken, got %d, expected %d" % (result, port))

thread1 = threading.Thread(target=getservbyname_loop, args=("ssh", 22))
thread2 = threading.Thread(target=getservbyname_loop, args=("smtp", 25))
thread1.start()
thread2.start()
