import asyncio


async def server():
    async def connection_callback(reader, writer: asyncio.StreamWriter):
        print(f"got connection from {writer.get_extra_info('peername')}")
        writer.close()
        await writer.wait_closed()

    s = await asyncio.start_server(connection_callback, host=[''], port=4567)
    async with s:
        print("starting server")
        await s.serve_forever()


asyncio.run(server())