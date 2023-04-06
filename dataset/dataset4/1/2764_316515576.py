class int_with_socket(int):
    def __new__(cls, socket):
        obj = int.__new__(cls, socket._fileno)
        obj.socket = socket
        return obj