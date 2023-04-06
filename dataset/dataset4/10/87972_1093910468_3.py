cpid = os.fork()
if cpid == 0:
    os.kill(os.getpid(), signal.SIGKILL)
    os.write(ctx, b'A')
    time.sleep(10.0)
else:
    async def read_from_child():
        async with connect():
            input = await read_stream.read(1)
            print('Parent received: ', input)

    asyncio.run(read_from_child())