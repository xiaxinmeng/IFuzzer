import asyncio

async def handle_connection(reader, writer):
    try:
        await reader.readexactly(42)
    except BaseException as err:
        print('Interesting: %r.' % err)
        raise
    finally:
        writer.close()

async def main():
    listener = await asyncio.start_server(handle_connection, '127.0.0.1', 8888)
    try:
        async with listener:
            await listener.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')

asyncio.run(main())