async def send_from_open_file(f, s):
    data = f.read()
    f.close()
    await s.send(data)

async def send_filename(filename, s):
    f = open(filename)
    t = asyncio.create_task(send_from_open_file(f, s))
    t.cancel()
    await asyncio.sleep(1)