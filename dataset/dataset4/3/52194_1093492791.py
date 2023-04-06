# iotest.py
import time
import threading
from socket import *

# CPU-bound thread (just hammers the CPU)
def spin():
    while True:
        pass

# I/O-bound thread (an echo TCP server)
def echo_server():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    s.bind(("",15000))
    s.listen(1)
    while True:
        c,a = s.accept()
        while True:
            data = c.recv(8192)
            if not data:
                break
            c.sendall(data)
        c.close()
    s.close()

# Launch the CPU-bound thread
t1 = threading.Thread(target=spin)
t1.daemon=True
t1.start()

# Run the I/O server
echo_server()