import asyncio


class Serve(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.write(b"OK")

async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(lambda: Serve(), '127.0.0.1', 8088)

    async with server:
        await server.serve_forever()

asyncio.run(main(), debug=True)