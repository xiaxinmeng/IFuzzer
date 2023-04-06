class MyThread(threading.Thread):
    def __init__(self, socket_conn):
        threading.Thread.__init__(self)
        self.my_conn = socket_conn

    @use_my_excepthook
    def run(self):
        """ Do stuff """