import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 22)

    writer.close()

asyncio.run(tcp_client())