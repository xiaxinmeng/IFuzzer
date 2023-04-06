import asyncio


class EchoServerProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        print(type(transport), isinstance(transport, asyncio.DatagramTransport))


async def main():
    transport, protocol = await asyncio.get_running_loop().create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 9999))