class MyAsyncChat(asynchat.async_chat):
    def push (self, data):
        self.producer_fifo.push (simple_producer (data))