import threading
import signal
import os
import httplib

def killer():
    while 1:
        os.kill(os.getpid(), signal.SIGINT)

def go():
    signal.signal(signal.SIGINT, lambda x,y: None)
    thread = threading.Thread(target=killer)
    thread.start()
    while 1:
        connection = httplib.HTTPConnection("localhost:80")
        connection.connect()
        connection.close()
        
if __name__ == '__main__':
    go()