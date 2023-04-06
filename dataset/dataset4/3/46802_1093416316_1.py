HOST = 'localhost'
PORT = None

class Foo(TestCase):
    def setUp(self):
        sock = socket.socket()
        global PORT
        PORT = test_support.bind_port(sock, HOST)