class Popen4(Popen3):
    def __init__(self, cmd, bufsize=-1):
        p2cread, p2cwrite = os.pipe()
        c2pread, c2pwrite = os.pipe()
        self.pid = os.fork()