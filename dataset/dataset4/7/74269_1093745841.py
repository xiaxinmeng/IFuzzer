import asyncio
async def handle_connection(reader, writer):
    try:
        await reader.readexactly(42)
    except BaseException as err:
        print('Interesting: %r.' % err)
        raise
    finally:
        writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_connection, '127.0.0.1', 8888)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('KeyboardInterrupt catched.')
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()