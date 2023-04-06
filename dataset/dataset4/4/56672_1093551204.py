class ThreadedRPC(Thread, SimpleXMLRPCServer):
    def __init__(self):
        Thread.__init__(self)
        SimpleXMLRPCServer.__init__(self)
        # python bug workaround, which eliminate hang on test_exception
        self._BaseServer__is_shut_down.set()
        self.daemon = True

    def run(self):
        raise Exception('race-condition!')
        self.serve_forever()


def main():
    rpc = ThreadedRPC(RPC_LISTEN_ADDR, allow_none=True)
    rpc.start() # from Thread

    # term set by signal handler
    while rpc.isAlive() and not term:
        time.sleep(0.5)

    # note, thread may die in any time! regardles of isAlive()
    # if thread dead before calling serve_forever(), will hang here without a workaround
    rpc.shutdown() # from xmlrpcservr. 

    rpc.join() # from thread (no problem, as thread is not Alive)