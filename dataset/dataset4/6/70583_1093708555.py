class MyProtocol(aio.DatagramProtocol):
    def __init__(self, fut):
        self._fut = fut

    def datagram_received(self, data, addr):
        self.fut.set_result((data, addr))

fut = aio.Future()
loop.create_datagram_endpoint(lambda: MyProtocol(fut), ...)
yield from fut