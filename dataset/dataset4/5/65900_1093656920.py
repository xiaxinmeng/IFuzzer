class Helloer(asyncio.DatagramProtocol):

    def connection_made(self, transport):
        print('(helloer) connection made')
        self.transport = transport

    def connection_lost(self, transport):
        print('(helloer listener) connection lost!')

    def datagram_received(self, data, addr):
        print('(helloer listener) received data from {}: {}'.format(addr, data))

    def error_received(self, exc):
        print('(helloer listener) error received: {}'.format(exc))

loop = asyncio.get_event_loop()
# WORKS:
coro = loop.create_datagram_endpoint(Helloer, local_addr=('127.0.0.1', 8888))
# FAILS (blocks?):
# coro = loop.create_datagram_endpoint(Helloer, local_addr=('127.0.0.1', 8888), remote_addr=('127.0.0.1', 9999))
transport, protocol = loop.run_until_complete(coro)
loop.run_forever()