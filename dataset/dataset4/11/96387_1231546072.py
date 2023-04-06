import socket

class TestUnclosedSocket:
    def __init__(self):
        self.s = socket.socket()
ins = TestUnclosedSocket()