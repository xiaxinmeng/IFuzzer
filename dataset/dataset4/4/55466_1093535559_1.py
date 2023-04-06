class MyServer(asyncore.dispatcher):
    def __init__(self, listenaddr):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(listenaddr)
        self.listen(5)
    def handle_accept(self):
        while 1:
            r=self.accept()
            if r is None:
                break
            my_conn_handler(r[0])