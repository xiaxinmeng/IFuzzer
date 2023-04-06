def log(msg):
    logging.debug(msg)

class Sender(asynchat.async_chat):

    def __init__(self, conn):
        asynchat.async_chat.__init__(self, conn)
        self.set_terminator("\r\n")
        self.push("220 hello\r\n")
        self.push_callable(log, "hello has been sent")