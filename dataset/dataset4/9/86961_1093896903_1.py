import asyncio


async def client():
    reader, writer = await asyncio.open_connection("127.0.0.1", 4567)
    print(f"connected to {writer.get_extra_info('peername')}")
    writer.close()
    await writer.wait_closed()


asyncio.run(client())