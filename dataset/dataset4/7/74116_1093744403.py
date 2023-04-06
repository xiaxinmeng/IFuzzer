async def do_nothing(client_reader, client_writer):
    await asyncio.sleep(10000)

mb = b'*' * (4096*4)
async def write_cmd(writer):
    writer.write(mb)
    await writer.drain()

async def amain():
    srv = await asyncio.start_unix_server(do_nothing, b'\x00qwe')
    (reader, writer) = await asyncio.open_unix_connection(b'\x00qwe')
    await asyncio.gather(*(write_cmd(writer) for i in range(200)))

loop = asyncio.get_event_loop()
loop.run_until_complete(amain())