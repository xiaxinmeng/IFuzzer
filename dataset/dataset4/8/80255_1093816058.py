
import asyncio
import platform


async def close_server():
    def handler(reader, writer):
        pass
    s = await asyncio.start_server(handler, host='127.0.0.1', port=34567)
    s.close()
    await s.wait_closed()
    assert s.sockets is None


print("version: ", platform.python_version())
asyncio.get_event_loop().run_until_complete(close_server())
