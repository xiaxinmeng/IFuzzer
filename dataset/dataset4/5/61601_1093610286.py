import socket
import multiprocessing
import multiprocessing.reduction
import multiprocessing.connection

def socketpair():
    with socket.socket() as l:
        l.bind(('localhost', 0))
        l.listen(1)
        s = socket.socket()
        s.connect(l.getsockname())
        a, _ = l.accept()
        return s, a

def bar(s):
    print(s)
    s.sendall(b'from bar')

if __name__ == '__main__':
    a, b = socketpair()
    p = multiprocessing.Process(target=bar, args=(b,))
    p.start()
    b.close()
    print(a.recv(100))