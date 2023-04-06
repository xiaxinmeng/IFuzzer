def makeSocket(self):
    """
    A factory method which allows subclasses to define the precise
    type of socket they want.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    return s 