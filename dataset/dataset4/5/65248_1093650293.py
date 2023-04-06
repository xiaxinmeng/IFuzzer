import _socket

class socket(_socket.socket):
    def __init__(self):
        _socket.socket.__init__(self)
        self.attr = self.__init__
        raise Exception()

socket()