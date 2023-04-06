async def bug():
    reader, writer = await asyncio.open_connection("::1", "1066")
    while True:
        writer.write("foo\n".encode())
        await writer.drain()
        # Uncommenting this makes drain() raise BrokenPipeError
        # when the server closes the connection.
        #await asyncio.sleep(0.1)

loop = asyncio.get_event_loop()
loop.run_until_complete(bug())