import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.transport.write(b'Say something')

    def data_received(self, data):
        self.transport.write(data)
        self.transport.close()

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
loop.run_forever()